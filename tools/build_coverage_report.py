#!/usr/bin/env python3
"""Build coverage report comparing patched specs to generated methods."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}


def count_ops_from_spec(spec: dict[str, Any]) -> int:
    count = 0
    paths = spec.get("paths", {})
    if not isinstance(paths, dict):
        return 0
    for path_item in paths.values():
        if isinstance(path_item, dict):
            count += sum(1 for m in path_item if m.lower() in HTTP_METHODS)
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description="Build coverage report")
    parser.add_argument("--manifest", default="specs/manifest.json")
    parser.add_argument("--patched", default="specs/patched")
    parser.add_argument("--map", default="docs/generated-method-map.json")
    parser.add_argument("--out", default="docs/final-compliance-report.md")
    args = parser.parse_args()

    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    method_map = json.loads(Path(args.map).read_text(encoding="utf-8"))

    rows: list[dict[str, Any]] = []
    total_raw = 0
    total_patched = 0
    total_generated = 0
    total_typed = 0

    for entry in manifest.get("entries", []):
        slug = entry["slug"]
        raw_ops = int(entry.get("operations", 0))
        patched_file = Path(args.patched) / f"{slug}.json"
        patched_spec = json.loads(patched_file.read_text(encoding="utf-8"))
        patched_ops = count_ops_from_spec(patched_spec)
        generated_entries = method_map.get(slug, [])
        generated_ops = len(generated_entries)
        typed_ops = sum(1 for entry in generated_entries if entry.get("response_model") not in {None, "", "Any"})

        total_raw += raw_ops
        total_patched += patched_ops
        total_generated += generated_ops
        total_typed += typed_ops

        rows.append(
            {
                "slug": slug,
                "raw": raw_ops,
                "patched": patched_ops,
                "generated": generated_ops,
                "typed": typed_ops,
                "status": "OK" if patched_ops == generated_ops and patched_ops == typed_ops else "GAP",
            }
        )

    raw_cov = (total_generated / total_raw * 100.0) if total_raw else 0.0
    patched_cov = (total_generated / total_patched * 100.0) if total_patched else 0.0
    typed_cov = (total_typed / total_patched * 100.0) if total_patched else 0.0

    lines: list[str] = []
    lines.append("# Final Compliance Report")
    lines.append("")
    lines.append(f"Generated at: {datetime.now(timezone.utc).isoformat()}")
    lines.append("")
    lines.append("| slug | raw ops | patched ops | generated methods | typed methods | status |")
    lines.append("|---|---:|---:|---:|---:|---|")
    for row in rows:
        lines.append(
            f"| {row['slug']} | {row['raw']} | {row['patched']} | {row['generated']} | {row['typed']} | {row['status']} |"
        )
    lines.append("")
    lines.append(f"Total raw operations: **{total_raw}**")
    lines.append(f"Total patched operations: **{total_patched}**")
    lines.append(f"Total generated methods: **{total_generated}**")
    lines.append(f"Total typed methods: **{total_typed}**")
    lines.append(f"Coverage vs raw: **{raw_cov:.2f}%**")
    lines.append(f"Coverage vs patched: **{patched_cov:.2f}%**")
    lines.append(f"Typed coverage vs patched: **{typed_cov:.2f}%**")
    lines.append("")
    lines.append("Notes:")
    lines.append("- `raw` can include duplicated operations caused by known spec quirks.")
    lines.append("- generation targets normalized `patched` specs.")

    Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
