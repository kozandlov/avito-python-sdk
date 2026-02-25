#!/usr/bin/env python3
"""Fetch Avito OpenAPI specs and save raw snapshots + manifest."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx

LIST_URL = "https://developers.avito.ru/web/1/openapi/list"
INFO_URL_TEMPLATE = "https://developers.avito.ru/web/1/openapi/info/{slug}"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def fetch_json(client: httpx.Client, url: str) -> Any:
    response = client.get(url, timeout=60.0)
    response.raise_for_status()
    return response.json()


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch Avito OpenAPI specs")
    parser.add_argument("--out", default="specs/raw", help="raw spec output directory")
    parser.add_argument("--manifest", default="specs/manifest.json", help="manifest path")
    args = parser.parse_args()

    out_dir = Path(args.out)
    ensure_dir(out_dir)

    entries: list[dict[str, Any]] = []

    with httpx.Client(follow_redirects=True) as client:
        api_list = fetch_json(client, LIST_URL)

        for item in api_list:
            slug = item["slug"]
            info_url = INFO_URL_TEMPLATE.format(slug=slug)
            info = fetch_json(client, info_url)

            swagger_raw = info.get("swagger")
            if not isinstance(swagger_raw, str):
                raise RuntimeError(f"No swagger string in info for slug={slug}")

            spec_json = json.loads(swagger_raw)
            spec_bytes = json.dumps(spec_json, ensure_ascii=False, indent=2).encode("utf-8")
            out_file = out_dir / f"{slug}.json"
            out_file.write_bytes(spec_bytes)

            paths = spec_json.get("paths", {})
            op_count = 0
            if isinstance(paths, dict):
                for path_item in paths.values():
                    if isinstance(path_item, dict):
                        op_count += sum(
                            1
                            for method in path_item.keys()
                            if method.lower() in {"get", "post", "put", "delete", "patch", "head", "options"}
                        )

            entries.append(
                {
                    "slug": slug,
                    "title": item.get("title"),
                    "source": info_url,
                    "raw_file": str(out_file.as_posix()),
                    "sha256": sha256_bytes(spec_bytes),
                    "operations": op_count,
                }
            )

    manifest = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_list_url": LIST_URL,
        "slug_count": len(entries),
        "entries": sorted(entries, key=lambda x: x["slug"]),
    }

    manifest_path = Path(args.manifest)
    ensure_dir(manifest_path.parent)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
