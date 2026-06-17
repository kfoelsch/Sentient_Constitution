#!/usr/bin/env python3
"""Shift institutional-design CI-2 labels to CI-3 for integration-map insertion."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

SKIP_DIRS = {"archive", ".git", "__pycache__", "node_modules"}
EXTENSIONS = {".md", ".py", ".json", ".csv"}
SKIP_FILES = {"renumber_ci_institutional.py", "ci_02_implementation_integration_map.md", "doc_architecture.md"}

CI2_MAIN = re.compile(r"CI-2(?!\d)")
CI2_ANCHOR = re.compile(r"ci-2(?!\d)")


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
    text = text.replace("CI-2.", "CI-3.")
    text = CI2_MAIN.sub("CI-3", text)
    text = CI2_ANCHOR.sub("ci-3", text)
    text = text.replace("ci_02_institutional_design", "ci_03_institutional_design")
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--dry-run", action="store_true")
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
