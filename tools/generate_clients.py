#!/usr/bin/env python3
"""Generate typed per-slug async API modules from patched Avito OpenAPI specs."""

from __future__ import annotations

import argparse
import json
import keyword
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

HTTP_METHODS = ["get", "post", "put", "patch", "delete", "head", "options"]


@dataclass
class OperationSpec:
    slug: str
    operation_id: str
    python_method: str
    method: str
    path: str
    summary: str
    response_status: str | None
    response_schema: dict[str, Any] | None
    schema_kind: str
    response_model: str


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def reset_dir(path: Path) -> None:
    """Clean generated directory to avoid stale files between runs."""
    ensure_dir(path)
    for child in path.iterdir():
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()


def snake_case(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "_", value)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    return value.lower().strip("_")


def pascal_case(value: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", " ", value)
    parts = [p for p in cleaned.split() if p]
    if not parts:
        return "X"
    return "".join(p[:1].upper() + p[1:] for p in parts)


def py_name_from_operation_id(operation_id: str) -> str:
    name = snake_case(operation_id)
    if not name:
        name = "op"
    if name[0].isdigit() or keyword.iskeyword(name):
        name = f"op_{name}"
    return name


def to_safe_identifier(name: str) -> tuple[str, bool]:
    normalized = snake_case(name)
    if not normalized:
        normalized = "field"
    if normalized[0].isdigit():
        normalized = f"field_{normalized}"
    if keyword.iskeyword(normalized):
        normalized = f"{normalized}_"
    return normalized, normalized != name


def dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for item in items:
        if item not in seen:
            out.append(item)
            seen.add(item)
    return out


def parse_ref_name(ref: str) -> str:
    return ref.split("/")[-1]


def choose_success_response(op: dict[str, Any]) -> tuple[str | None, dict[str, Any] | None, str]:
    responses = op.get("responses")
    if not isinstance(responses, dict):
        return None, None, "none"

    def score(code: str) -> tuple[int, int]:
        if code == "200":
            return (0, 200)
        if code == "201":
            return (1, 201)
        if code == "202":
            return (2, 202)
        if code == "204":
            return (3, 204)
        if code.isdigit() and code.startswith("2"):
            return (4, int(code))
        return (9, 999)

    candidates = sorted((k for k in responses.keys() if k.isdigit() and k.startswith("2")), key=score)
    if not candidates:
        return None, None, "none"

    status = candidates[0]
    response_obj = responses.get(status, {})
    if not isinstance(response_obj, dict):
        return status, None, "none"

    if status == "204":
        return status, None, "none"

    content = response_obj.get("content")
    if not isinstance(content, dict) or not content:
        return status, None, "none"

    schema: dict[str, Any] | None = None
    for key in ("application/json",):
        candidate = content.get(key)
        if isinstance(candidate, dict):
            possible = candidate.get("schema")
            if isinstance(possible, dict):
                schema = possible
                break

    if schema is None:
        for media, candidate in content.items():
            if not isinstance(media, str) or not isinstance(candidate, dict):
                continue
            if "json" in media:
                possible = candidate.get("schema")
                if isinstance(possible, dict):
                    schema = possible
                    break

    if schema is None:
        return status, None, "none"

    if "$ref" in schema:
        kind = "ref"
    elif schema.get("type") == "array":
        kind = "array"
    elif schema.get("type") == "object" or "properties" in schema:
        kind = "object"
    elif "oneOf" in schema:
        kind = "oneOf"
    elif "anyOf" in schema:
        kind = "anyOf"
    elif "allOf" in schema:
        kind = "allOf"
    else:
        kind = schema.get("type", "inline")

    return status, schema, str(kind)


class ModelBuilder:
    """Generate typed Pydantic model module for one slug."""

    def __init__(self, slug: str, spec: dict[str, Any]) -> None:
        self.slug = slug
        self.spec = spec
        self.components = spec.get("components", {}).get("schemas", {})
        if not isinstance(self.components, dict):
            self.components = {}

        self.model_defs: dict[str, list[str]] = {}
        self.model_order: list[str] = []
        self.component_map: dict[str, str] = {}
        self.class_names: set[str] = set()
        self.inline_counter = 0

        self.need_field = False
        self.need_literal = False
        self.need_root_model = False

    def unique_class_name(self, base: str) -> str:
        candidate = pascal_case(base)
        if not candidate[0].isalpha():
            candidate = f"X{candidate}"
        if keyword.iskeyword(candidate.lower()):
            candidate = f"{candidate}Model"

        idx = 2
        unique = candidate
        while unique in self.class_names:
            unique = f"{candidate}{idx}"
            idx += 1
        self.class_names.add(unique)
        return unique

    def add_model_def(self, class_name: str, lines: list[str]) -> None:
        if class_name in self.model_defs:
            return
        self.model_defs[class_name] = lines
        self.model_order.append(class_name)

    def apply_nullable(self, type_expr: str, schema: dict[str, Any]) -> str:
        if schema.get("nullable") is True and "None" not in type_expr:
            return f"{type_expr} | None"
        return type_expr

    def schema_from_ref(self, ref: str) -> dict[str, Any]:
        return self.components.get(parse_ref_name(ref), {}) if isinstance(ref, str) else {}

    def merge_allof(self, schema: dict[str, Any]) -> dict[str, Any] | None:
        all_of = schema.get("allOf")
        if not isinstance(all_of, list):
            return None

        merged: dict[str, Any] = {"type": "object", "properties": {}, "required": []}

        for part in all_of:
            part_schema = part
            if isinstance(part_schema, dict) and "$ref" in part_schema:
                part_schema = self.schema_from_ref(part_schema["$ref"])
            if not isinstance(part_schema, dict):
                continue

            props = part_schema.get("properties")
            if isinstance(props, dict):
                merged["properties"].update(props)

            req = part_schema.get("required")
            if isinstance(req, list):
                merged["required"] = dedupe(list(merged["required"]) + [str(x) for x in req])

            if "additionalProperties" in part_schema and "additionalProperties" not in merged:
                merged["additionalProperties"] = part_schema["additionalProperties"]

        own_props = schema.get("properties")
        if isinstance(own_props, dict):
            merged["properties"].update(own_props)
        own_req = schema.get("required")
        if isinstance(own_req, list):
            merged["required"] = dedupe(list(merged["required"]) + [str(x) for x in own_req])

        if merged.get("properties") or "additionalProperties" in merged:
            return merged
        return None

    def ensure_component_model(self, component_name: str) -> str:
        if component_name in self.component_map:
            return self.component_map[component_name]

        class_name = self.unique_class_name(component_name)
        self.component_map[component_name] = class_name
        schema = self.components.get(component_name, {})
        self.build_model(class_name, schema, hint=component_name)
        return class_name

    def infer_type(self, schema: dict[str, Any] | None, hint: str, *, allow_inline: bool = True) -> str:
        if not isinstance(schema, dict):
            return "Any"

        if "$ref" in schema:
            return self.ensure_component_model(parse_ref_name(str(schema["$ref"])))

        if "oneOf" in schema and isinstance(schema["oneOf"], list):
            variants = [self.infer_type(x, f"{hint}Variant{i}") for i, x in enumerate(schema["oneOf"], start=1)]
            result = " | ".join(dedupe(variants)) if variants else "Any"
            return self.apply_nullable(result, schema)

        if "anyOf" in schema and isinstance(schema["anyOf"], list):
            variants = [self.infer_type(x, f"{hint}Option{i}") for i, x in enumerate(schema["anyOf"], start=1)]
            result = " | ".join(dedupe(variants)) if variants else "Any"
            return self.apply_nullable(result, schema)

        if "allOf" in schema:
            merged = self.merge_allof(schema)
            if merged is not None:
                return self.infer_type(merged, hint, allow_inline=allow_inline)
            return self.apply_nullable("dict[str, Any]", schema)

        enum_values = schema.get("enum")
        if isinstance(enum_values, list) and enum_values:
            literal_values = [repr(v) for v in enum_values if isinstance(v, (str, int, float, bool)) or v is None]
            if literal_values:
                self.need_literal = True
                return self.apply_nullable(f"Literal[{', '.join(literal_values)}]", schema)

        schema_type = schema.get("type")

        if schema_type == "array" or "items" in schema:
            item_type = self.infer_type(schema.get("items", {}), f"{hint}Item")
            return self.apply_nullable(f"list[{item_type}]", schema)

        if schema_type == "object" or "properties" in schema or "additionalProperties" in schema:
            props = schema.get("properties")
            if allow_inline and isinstance(props, dict) and props:
                self.inline_counter += 1
                class_name = self.unique_class_name(f"{hint}Model{self.inline_counter}")
                self.build_model(class_name, schema, hint=class_name)
                return self.apply_nullable(class_name, schema)

            addl = schema.get("additionalProperties")
            if isinstance(addl, dict):
                value_type = self.infer_type(addl, f"{hint}Value")
                return self.apply_nullable(f"dict[str, {value_type}]", schema)
            return self.apply_nullable("dict[str, Any]", schema)

        primitive = {
            "string": "str",
            "integer": "int",
            "number": "float",
            "boolean": "bool",
        }.get(schema_type)
        if primitive is not None:
            return self.apply_nullable(primitive, schema)

        return self.apply_nullable("Any", schema)

    def build_model(self, class_name: str, schema: dict[str, Any] | None, *, hint: str) -> None:
        if class_name in self.model_defs:
            return

        if not isinstance(schema, dict):
            self.need_root_model = True
            self.add_model_def(class_name, [f"class {class_name}(RootModel[Any]):", "    pass", ""])
            return

        if "$ref" in schema:
            schema = self.schema_from_ref(str(schema["$ref"]))

        if "allOf" in schema:
            merged = self.merge_allof(schema)
            if merged is not None:
                schema = merged

        if "oneOf" in schema or "anyOf" in schema:
            self.need_root_model = True
            self.add_model_def(class_name, [f"class {class_name}(RootModel[dict[str, Any]]):", "    pass", ""])
            return

        schema_type = schema.get("type")
        if schema_type == "array":
            self.need_root_model = True
            item_type = self.infer_type(schema.get("items", {}), f"{hint}Item", allow_inline=True)
            self.add_model_def(class_name, [f"class {class_name}(RootModel[list[{item_type}]]):", "    pass", ""])
            return

        if schema_type in {"string", "integer", "number", "boolean"}:
            self.need_root_model = True
            primitive = self.infer_type(schema, hint, allow_inline=False)
            self.add_model_def(class_name, [f"class {class_name}(RootModel[{primitive}]):", "    pass", ""])
            return

        properties = schema.get("properties")
        additional = schema.get("additionalProperties")

        if not isinstance(properties, dict) and isinstance(additional, dict):
            self.need_root_model = True
            value_type = self.infer_type(additional, f"{hint}Value")
            self.add_model_def(class_name, [f"class {class_name}(RootModel[dict[str, {value_type}]]):", "    pass", ""])
            return

        lines: list[str] = [f"class {class_name}(_BaseModel):"]

        if not isinstance(properties, dict) or not properties:
            lines.append("    pass")
            lines.append("")
            self.add_model_def(class_name, lines)
            return

        required = set(schema.get("required", [])) if isinstance(schema.get("required"), list) else set()

        for source_name, prop_schema in properties.items():
            prop_type = self.infer_type(prop_schema if isinstance(prop_schema, dict) else {}, f"{class_name}{pascal_case(source_name)}")
            py_name, alias_needed = to_safe_identifier(source_name)
            if source_name in required:
                if alias_needed:
                    self.need_field = True
                    lines.append(f"    {py_name}: {prop_type} = Field(alias={source_name!r})")
                else:
                    lines.append(f"    {py_name}: {prop_type}")
            else:
                if alias_needed:
                    self.need_field = True
                    lines.append(f"    {py_name}: {prop_type} = Field(default=None, alias={source_name!r})")
                else:
                    lines.append(f"    {py_name}: {prop_type} = None")

        lines.append("")
        self.add_model_def(class_name, lines)

    def render_module(self) -> str:
        imports = ["Any"]
        if self.need_literal:
            imports.append("Literal")

        pydantic_imports = ["BaseModel", "ConfigDict", "ValidationError"]
        if self.need_field:
            pydantic_imports.append("Field")
        if self.need_root_model:
            pydantic_imports.append("RootModel")

        lines: list[str] = []
        lines.append(f'"""Generated response models for slug: {self.slug}."""')
        lines.append("")
        lines.append("from __future__ import annotations")
        lines.append("")
        lines.append(f"from typing import {', '.join(dedupe(imports))}")
        lines.append(f"from pydantic import {', '.join(dedupe(pydantic_imports))}")
        lines.append("")
        lines.append("class _BaseModel(BaseModel):")
        lines.append("    model_config = ConfigDict(extra=\"forbid\")")
        lines.append("")

        for class_name in self.model_order:
            lines.extend(self.model_defs[class_name])

        all_items = ", ".join(repr(name) for name in self.model_order)
        lines.append(f"__all__ = [{all_items}]")
        lines.append("")
        return "\n".join(lines)


def extract_operations(slug: str, spec: dict[str, Any], model_builder: ModelBuilder) -> list[OperationSpec]:
    operations: list[OperationSpec] = []
    paths = spec.get("paths", {})
    if not isinstance(paths, dict):
        return operations

    class_name = "".join(part.capitalize() for part in slug.replace("-", "_").split("_")) + "Api"

    for path, path_item in paths.items():
        if not isinstance(path_item, dict):
            continue

        for method in HTTP_METHODS:
            op = path_item.get(method)
            if not isinstance(op, dict):
                continue

            op_id = str(op.get("operationId") or f"{method}_{snake_case(path)}")
            python_method = py_name_from_operation_id(op_id)
            response_status, response_schema, schema_kind = choose_success_response(op)

            if response_status is None or response_schema is None:
                response_model = "None"
            else:
                response_model = model_builder.unique_class_name(
                    f"{class_name}{pascal_case(python_method)}Response"
                )
                model_builder.build_model(response_model, response_schema, hint=response_model)

            operations.append(
                OperationSpec(
                    slug=slug,
                    operation_id=op_id,
                    python_method=python_method,
                    method=method.upper(),
                    path=path,
                    summary=str(op.get("summary") or ""),
                    response_status=response_status,
                    response_schema=response_schema,
                    schema_kind=schema_kind,
                    response_model=response_model,
                )
            )

    return operations


def render_slug_module(slug: str, operations: list[OperationSpec]) -> str:
    class_name = "".join(part.capitalize() for part in slug.replace("-", "_").split("_")) + "Api"
    model_module = slug.replace("-", "_")

    model_names = sorted({op.response_model for op in operations if op.response_model != "None"})

    lines: list[str] = []
    lines.append(f'"""Generated API module for slug: {slug}."""')
    lines.append("")
    lines.append("from __future__ import annotations")
    lines.append("")
    lines.append("from typing import Any, Optional")
    lines.append("from pydantic import ValidationError")
    lines.append("")
    lines.append("from pyavitoapi.transport.errors import AvitoValidationError")
    lines.append("from pyavitoapi.transport.http import AvitoHttpTransport")
    if model_names:
        lines.append(f"from pyavitoapi.generated_models.{model_module} import {', '.join(model_names)}")
    lines.append("")
    lines.append("")
    lines.append(f"class {class_name}:")
    lines.append("    \"\"\"Generated async API client.\"\"\"")
    lines.append("")
    lines.append("    def __init__(self, transport: AvitoHttpTransport) -> None:")
    lines.append("        self._transport = transport")
    lines.append("")

    for op in operations:
        summary = op.summary.replace('"', "'")
        return_type = op.response_model if op.response_model != "None" else "None"

        lines.append(f"    async def {op.python_method}(")
        lines.append("        self,")
        lines.append("        *,")
        lines.append("        path_params: Optional[dict[str, Any]] = None,")
        lines.append("        query: Optional[dict[str, Any]] = None,")
        lines.append("        json_body: Optional[dict[str, Any]] = None,")
        lines.append("        headers: Optional[dict[str, str]] = None,")
        lines.append(f"    ) -> {return_type}:")
        lines.append(f"        \"\"\"{summary}\"\"\"")
        lines.append("        payload = await self._transport.request(")
        lines.append(f"            method=\"{op.method}\",")
        lines.append(f"            path_template=\"{op.path}\",")
        lines.append("            path_params=path_params,")
        lines.append("            query=query,")
        lines.append("            json_body=json_body,")
        lines.append("            headers=headers,")
        lines.append("        )")

        if op.response_model == "None":
            lines.append("        return None")
        else:
            lines.append("        try:")
            lines.append(f"            return {op.response_model}.model_validate(payload)")
            lines.append("        except ValidationError as exc:")
            lines.append("            raise AvitoValidationError(")
            lines.append(
                f"                \"Response validation failed for {slug}.{op.python_method} ({op.method} {op.path})\",")
            lines.append("                payload=payload,")
            lines.append("                details={")
            lines.append(f"                    \"slug\": \"{slug}\",")
            lines.append(f"                    \"operation_id\": \"{op.operation_id}\",")
            lines.append(f"                    \"python_method\": \"{op.python_method}\",")
            lines.append(f"                    \"http_method\": \"{op.method}\",")
            lines.append(f"                    \"path\": \"{op.path}\",")
            lines.append("                    \"errors\": exc.errors(),")
            lines.append("                },")
            lines.append("            ) from exc")
        lines.append("")

    lines.append(f"__all__ = [\"{class_name}\"]")
    lines.append("")
    return "\n".join(lines)


def render_generated_init(index: list[dict[str, str]]) -> str:
    lines = ["\"\"\"Generated Avito API modules.\"\"\"", ""]
    all_items: list[str] = []
    for item in index:
        lines.append(f"from .{item['module']} import {item['class_name']}")
        all_items.append(f'"{item["class_name"]}"')
    lines.append("")
    lines.append("__all__ = [")
    for entry in all_items:
        lines.append(f"    {entry},")
    lines.append("]")
    lines.append("")
    return "\n".join(lines)


def render_registry(index: list[dict[str, str]]) -> str:
    lines: list[str] = []
    lines.append('"""Generated slug registry."""')
    lines.append("")
    lines.append("from __future__ import annotations")
    lines.append("")
    lines.append("from typing import Any")
    lines.append("")
    for item in index:
        lines.append(f"from pyavitoapi.generated.{item['module']} import {item['class_name']}")
    lines.append("")
    lines.append("REGISTRY: dict[str, type[Any]] = {")
    for item in index:
        lines.append(f"    \"{item['slug']}\": {item['class_name']},")
    lines.append("}")
    lines.append("")
    return "\n".join(lines)


def render_models_init(model_modules: list[str]) -> str:
    lines = ["\"\"\"Generated response models for Avito API modules.\"\"\"", ""]
    lines.append("__all__ = [")
    for module in sorted(model_modules):
        lines.append(f"    \"{module}\",")
    lines.append("]")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate typed API clients from patched specs")
    parser.add_argument("--in-dir", default="specs/patched", help="patched specs directory")
    parser.add_argument("--out-dir", default="src/pyavitoapi/generated", help="generated output directory")
    parser.add_argument(
        "--models-out-dir",
        default="src/pyavitoapi/generated_models",
        help="generated typed response models directory",
    )
    parser.add_argument(
        "--report",
        default="docs/generated-method-map.json",
        help="generated method map report",
    )
    parser.add_argument(
        "--typed-map",
        default="docs/typed-response-map.json",
        help="typed response map report",
    )
    args = parser.parse_args()

    in_dir = Path(args.in_dir)
    out_dir = Path(args.out_dir)
    models_out_dir = Path(args.models_out_dir)
    reset_dir(out_dir)
    reset_dir(models_out_dir)

    method_map: dict[str, list[dict[str, Any]]] = {}
    typed_map: dict[str, list[dict[str, Any]]] = {}
    index: list[dict[str, str]] = []
    model_modules: list[str] = []

    for spec_file in sorted(in_dir.glob("*.json")):
        slug = spec_file.stem
        spec = json.loads(spec_file.read_text(encoding="utf-8"))

        model_builder = ModelBuilder(slug=slug, spec=spec)
        ops = extract_operations(slug=slug, spec=spec, model_builder=model_builder)

        module_name = slug.replace("-", "_")
        class_name = "".join(part.capitalize() for part in module_name.split("_")) + "Api"

        module_code = render_slug_module(slug, ops)
        models_code = model_builder.render_module()

        (out_dir / f"{module_name}.py").write_text(module_code, encoding="utf-8")
        (models_out_dir / f"{module_name}.py").write_text(models_code, encoding="utf-8")

        model_modules.append(module_name)
        index.append({"slug": slug, "module": module_name, "class_name": class_name})

        entries = [
            {
                "operation_id": op.operation_id,
                "python_method": op.python_method,
                "http_method": op.method,
                "path": op.path,
                "response_status": op.response_status,
                "response_model": op.response_model,
                "schema_kind": op.schema_kind,
            }
            for op in ops
        ]

        method_map[slug] = entries
        typed_map[slug] = entries

    (out_dir / "__init__.py").write_text(render_generated_init(index), encoding="utf-8")
    (models_out_dir / "__init__.py").write_text(render_models_init(model_modules), encoding="utf-8")

    registry_code = render_registry(index)
    Path("src/pyavitoapi/generated_registry.py").write_text(registry_code, encoding="utf-8")

    report_path = Path(args.report)
    ensure_dir(report_path.parent)
    report_path.write_text(json.dumps(method_map, ensure_ascii=False, indent=2), encoding="utf-8")

    typed_map_path = Path(args.typed_map)
    ensure_dir(typed_map_path.parent)
    typed_map_path.write_text(json.dumps(typed_map, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
