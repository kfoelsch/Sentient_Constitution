#!/usr/bin/env python3
"""LEGACY — do not run on the live corpus without review.

One-off migration aid from an obsolete Chapter Seven layout. Current article IDs
and titles live in core_constitution.md; verify with `make reference-audit`.
See tools/README.md (Legacy Chapter Seven migration scripts).
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Longest / most specific first
PAIRS = [
    ("Articles VIII-D through III-H", "Articles IX-A through IV-E"),
    ("Article VIII-H", "Article IX-E"),
    ("Articles VIII-H", "Articles IX-E"),
    ("Art III-H", "Art IV-E"),
    ("Article VIII-G", "Article IX-D"),
    ("Articles VIII-G", "Articles IX-D"),
    ("Art III-G", "Art IV-D"),
    ("Article VIII-F", "Article IX-C"),
    ("Articles VIII-F", "Articles IX-C"),
    ("Art III-F", "Art IV-C"),
    ("Article VIII-E", "Article IX-B"),
    ("Articles VIII-E", "Articles IX-B"),
    ("Art III-E", "Art IV-B"),
    ("Article VIII-D", "Article IX-A"),
    ("Articles VIII-D", "Articles IX-A"),
    ("Art III-D", "Art IV-A"),
]


def main() -> None:
    for path in sorted(ROOT.rglob("*.md")):
        if "/.git/" in str(path):
            continue
        raw = path.read_text(encoding="utf-8")
        out = raw
        for a, b in PAIRS:
            out = out.replace(a, b)
        if out != raw:
            path.write_text(out, encoding="utf-8", newline="\n")
            print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
