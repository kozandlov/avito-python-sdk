#!/usr/bin/env python3
"""Patch-bump project version in pyproject.toml."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

VERSION_RE = re.compile(r'(?m)^version\s*=\s*"(\d+)\.(\d+)\.(\d+)"\s*$')


def bump_patch(version: str) -> str:
    major, minor, patch = version.split(".")
    return f"{major}.{minor}.{int(patch) + 1}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Bump patch version in pyproject.toml")
    parser.add_argument("--file", default="pyproject.toml", help="Path to pyproject.toml")
    parser.add_argument("--dry-run", action="store_true", help="Print new version without writing file")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"File not found: {path}", file=sys.stderr)
        return 1

    content = path.read_text(encoding="utf-8")
    match = VERSION_RE.search(content)
    if match is None:
        print("Could not find semantic version in pyproject.toml", file=sys.stderr)
        return 1

    current_version = ".".join(match.groups())
    new_version = bump_patch(current_version)

    if not args.dry_run:
        updated = VERSION_RE.sub(f'version = "{new_version}"', content, count=1)
        path.write_text(updated, encoding="utf-8")

    print(new_version)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
