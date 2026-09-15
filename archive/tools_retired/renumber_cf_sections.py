#!/usr/bin/env python3
"""Shift CF-2…CF-15 stable labels to CF-3…CF-16 (high → low) for integration-map insertion."""

from __future__ import annotations

import argparse
from pathlib import Path

SKIP_DIRS = {"archive", ".git", "__pycache__", "node_modules"}
EXTENSIONS = {".md", ".py", ".json", ".csv"}
SELF_NAME = "renumber_cf_sections.py"
SKIP_FILES = {SELF_NAME, "doc_architecture.md"}
FIRST, LAST = 2, 15


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in EXTENSIONS:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in SKIP_FILES:
            continue
        yield path


def transform(text: str) -> str:
    for n in range(LAST, FIRST - 1, -1):
        text = text.replace(f"CF-{n}", f"__TEMP_CF_{n + 1}__")

    for n in range(FIRST + 1, LAST + 2):
        text = text.replace(f"__TEMP_CF_{n}__", f"CF-{n}")

    for n in range(LAST, FIRST - 1, -1):
        text = text.replace(f"cf-{n}", f"__ANCHOR_{n + 1}__")

    for n in range(FIRST + 1, LAST + 2):
        text = text.replace(f"__ANCHOR_{n}__", f"cf-{n}")

    for n in range(LAST, FIRST - 1, -1):
        text = text.replace(f"cf_{n:02d}_", f"__FILE_{n + 1:02d}__")

    for n in range(FIRST + 1, LAST + 2):
        text = text.replace(f"__FILE_{n:02d}__", f"cf_{n:02d}_")

    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="Repository root")
    parser.add_argument("--dry-run", action="store_true", help="Print changed paths only")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    changed: list[Path] = []
    for path in sorted(iter_files(root)):
        original = path.read_text(encoding="utf-8")
        updated = transform(original)
        if updated != original:
            changed.append(path)
            if not args.dry_run:
                path.write_text(updated, encoding="utf-8")
    for path in changed:
        print(path.relative_to(root))
    print(f"{'Would update' if args.dry_run else 'Updated'} {len(changed)} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
