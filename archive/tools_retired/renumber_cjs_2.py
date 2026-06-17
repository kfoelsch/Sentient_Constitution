#!/usr/bin/env python3
"""Swap CJS-2.1 (overlap) and CJS-2.2 (router) so router and primary-owner definition come first."""

from __future__ import annotations

import sys
from pathlib import Path

SKIP_DIRS = {"archive", ".git", "__pycache__", "node_modules"}
EXTENSIONS = {".md", ".py", ".json", ".csv"}

ANCHOR_REPLACEMENTS = [
    (
        "cjs-21-intentional-overlap-non-duplication-discipline",
        "cjs-22-intentional-overlap-non-duplication-discipline",
    ),
    (
        "cjs-22-topic-router-stable-ids",
        "cjs-21-topic-router-stable-ids",
    ),
]

TEMP_OVERLAP = "__CJS_2_OVERLAP__"
TEMP_ROUTER = "__CJS_2_ROUTER__"


def transform(text: str) -> str:
    text = text.replace("CJS-2.1", TEMP_OVERLAP)
    text = text.replace("CJS-2.2", TEMP_ROUTER)
    text = text.replace(TEMP_ROUTER, "CJS-2.1")
    text = text.replace(TEMP_OVERLAP, "CJS-2.2")

    for old, new in ANCHOR_REPLACEMENTS:
        text = text.replace(old, new)
    return text


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in EXTENSIONS:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name == "renumber_cjs_2.py":
            continue
        yield path


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    changed: list[Path] = []
    for path in sorted(iter_files(root.resolve())):
        original = path.read_text(encoding="utf-8")
        updated = transform(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed.append(path)
    for path in changed:
        print(path.relative_to(root.resolve()))
    print(f"Updated {len(changed)} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
