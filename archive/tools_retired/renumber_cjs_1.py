#!/usr/bin/env python3
"""Renumber CJS-1 subsections: boundary first, then preamble, then identifiers."""

from __future__ import annotations

import sys
from pathlib import Path

SKIP_DIRS = {"archive", ".git", "__pycache__", "node_modules"}
EXTENSIONS = {".md", ".py", ".json", ".csv"}

ANCHOR_REPLACEMENTS = [
    (
        "cjs-13-joint-structural-boundary-and-owner-discipline",
        "cjs-11-joint-structural-boundary-and-owner-discipline",
    ),
    (
        "cjs-12-section-identifiers-and-article-references",
        "cjs-13-section-identifiers-and-article-references",
    ),
    (
        "cjs-11-shared-implementation-corpus-preamble-contract",
        "cjs-12-shared-implementation-corpus-preamble-contract",
    ),
]

TEMP_14 = "__CJS_1_4_KEEP__"
TEMP_15 = "__CJS_1_5_KEEP__"
TEMP_BOUNDARY = "__CJS_1_BOUNDARY__"
TEMP_PREAMBLE = "__CJS_1_PREAMBLE__"
TEMP_IDENTIFIERS = "__CJS_1_IDENTIFIERS__"


def transform(text: str) -> str:
    text = text.replace("CJS-1.5", TEMP_15)
    text = text.replace("CJS-1.4", TEMP_14)
    text = text.replace("CJS-1.3", TEMP_BOUNDARY)
    text = text.replace("CJS-1.2", TEMP_IDENTIFIERS)
    text = text.replace("CJS-1.1", TEMP_PREAMBLE)
    text = text.replace(TEMP_BOUNDARY, "CJS-1.1")
    text = text.replace(TEMP_PREAMBLE, "CJS-1.2")
    text = text.replace(TEMP_IDENTIFIERS, "CJS-1.3")
    text = text.replace(TEMP_14, "CJS-1.4")
    text = text.replace(TEMP_15, "CJS-1.5")

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
        if path.name == "renumber_cjs_1.py":
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
