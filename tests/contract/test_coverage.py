"""Contract test: generated methods must cover all patched OpenAPI operations."""

from __future__ import annotations

import json
from pathlib import Path

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}


def _count_ops(spec: dict) -> int:
    paths = spec.get("paths", {})
    count = 0
    if isinstance(paths, dict):
        for path_item in paths.values():
            if isinstance(path_item, dict):
                count += sum(1 for m in path_item if m.lower() in HTTP_METHODS)
    return count


def test_generated_methods_cover_all_patched_operations() -> None:
    root = Path(__file__).resolve().parents[2]
    patched_dir = root / "specs" / "patched"
    method_map_path = root / "docs" / "generated-method-map.json"

    method_map = json.loads(method_map_path.read_text(encoding="utf-8"))

    for spec_file in sorted(patched_dir.glob("*.json")):
        slug = spec_file.stem
        spec = json.loads(spec_file.read_text(encoding="utf-8"))
        expected = _count_ops(spec)
        generated = len(method_map.get(slug, []))
        assert generated == expected, f"slug={slug}: generated={generated}, expected={expected}"


def test_generated_methods_have_typed_response_models() -> None:
    root = Path(__file__).resolve().parents[2]
    method_map_path = root / "docs" / "generated-method-map.json"
    method_map = json.loads(method_map_path.read_text(encoding="utf-8"))

    missing: list[str] = []
    for slug, entries in method_map.items():
        for entry in entries:
            model = entry.get("response_model")
            if model in {None, "", "Any"}:
                missing.append(f"{slug}:{entry.get('operation_id')}")

    assert not missing, f"Operations without typed response model: {missing[:20]}"
