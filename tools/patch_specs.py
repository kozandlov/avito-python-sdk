#!/usr/bin/env python3
"""Normalize Avito OpenAPI specs for deterministic code generation."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}
INVISIBLE_CHARS = "\u200e\u200f\u202a\u202b\u202c\u202d\u202e\ufeff"


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def normalize_path_key(path: str) -> str:
    normalized = path
    for ch in INVISIBLE_CHARS:
        normalized = normalized.replace(ch, "")
    normalized = normalized.strip()
    if normalized.startswith("/token"):
        return "/token"
    return normalized


def slugify(value: str) -> str:
    lowered = value.lower()
    lowered = re.sub(r"[^a-z0-9]+", "_", lowered)
    lowered = lowered.strip("_")
    return lowered or "op"


def fallback_operation_id(method: str, path: str) -> str:
    return f"{method.lower()}_{slugify(path)}"


def ensure_unique_operation_ids(spec: dict[str, Any]) -> None:
    paths = spec.get("paths")
    if not isinstance(paths, dict):
        return

    seen: dict[str, int] = {}
    for path, path_item in paths.items():
        if not isinstance(path_item, dict):
            continue
        for method, op in path_item.items():
            if method.lower() not in HTTP_METHODS or not isinstance(op, dict):
                continue
            op_id = op.get("operationId")
            if not isinstance(op_id, str) or not op_id.strip():
                op_id = fallback_operation_id(method, path)
            candidate = op_id
            idx = 2
            while candidate in seen:
                candidate = f"{op_id}_{idx}"
                idx += 1
            seen[candidate] = 1
            op["operationId"] = candidate


def fix_messenger_send_message_required(spec: dict[str, Any]) -> None:
    components = spec.get("components")
    if not isinstance(components, dict):
        return
    schemas = components.get("schemas")
    if not isinstance(schemas, dict):
        return
    body = schemas.get("sendMessageRequestBody")
    if not isinstance(body, dict):
        return
    props = body.get("properties")
    if not isinstance(props, dict):
        return
    if "message" in props and "type" in props:
        body["required"] = ["type", "message"]


def normalize_paths(spec: dict[str, Any]) -> None:
    paths = spec.get("paths")
    if not isinstance(paths, dict):
        return

    merged: dict[str, Any] = {}
    for path_key, path_item in paths.items():
        normalized_key = normalize_path_key(path_key)
        existing = merged.get(normalized_key)
        if existing is None:
            merged[normalized_key] = path_item
            continue

        if not isinstance(existing, dict) or not isinstance(path_item, dict):
            continue

        for method, op in path_item.items():
            if method.lower() in HTTP_METHODS and method not in existing:
                existing[method] = op
            elif method == "parameters":
                existing_params = existing.get("parameters")
                if not isinstance(existing_params, list):
                    existing_params = []
                new_params = op if isinstance(op, list) else []
                existing["parameters"] = existing_params + [p for p in new_params if p not in existing_params]

    spec["paths"] = merged


def patch_spec(slug: str, spec: dict[str, Any]) -> dict[str, Any]:
    normalize_paths(spec)
    ensure_unique_operation_ids(spec)
    if slug == "messenger":
        fix_messenger_send_message_required(spec)
    return spec


def main() -> None:
    parser = argparse.ArgumentParser(description="Patch Avito OpenAPI specs")
    parser.add_argument("--in-dir", default="specs/raw", help="input directory")
    parser.add_argument("--out-dir", default="specs/patched", help="output directory")
    args = parser.parse_args()

    in_dir = Path(args.in_dir)
    out_dir = Path(args.out_dir)
    ensure_dir(out_dir)

    for file_path in sorted(in_dir.glob("*.json")):
        slug = file_path.stem
        spec = json.loads(file_path.read_text(encoding="utf-8"))
        patched = patch_spec(slug, spec)
        out_file = out_dir / file_path.name
        out_file.write_text(json.dumps(patched, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
