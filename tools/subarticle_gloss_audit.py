#!/usr/bin/env python3
"""Require an *In plain terms* line in each Chapter Ten `#### Article …` sub-article.

Operates on `core_10-10_rights_part_*.md`. Stops a sub-article block at the next
`####` sub-article, or at a `###` / `##` section boundary. Optional `--root`
matches other corpus tools.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

SUBARTICLE = re.compile(r"^#### Article .+:")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Workspace root. Default: .")
    return p.parse_args()


def subarticle_gloss_errors(root: pathlib.Path) -> list[str]:
    """Return one error string per failed sub-article (standalone API for wrappers)."""
    parts = sorted(root.glob("core_10-10_rights_part_*.md"))
    all_err: list[str] = []
    for path in parts:
        all_err.extend(scan_file(path))
    return all_err


def scan_file(path: pathlib.Path) -> list[str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    errors: list[str] = []
    i = 0
    while i < len(lines):
        if not SUBARTICLE.match(lines[i]):
            i += 1
            continue
        title = lines[i].strip()
        start_line = i + 1
        j = i + 1
        while j < len(lines):
            t = lines[j]
            if t.startswith("#### ") and j > i:
                break
            if t.startswith("### ") and not t.startswith("####"):
                break
            if t.startswith("## ") and not t.startswith("###"):
                break
            j += 1
        block = "\n".join(lines[i:j])
        if "In plain terms" not in block:
            rel = path.name
            errors.append(
                f"{rel}:{start_line}: sub-article missing *In plain terms* line — {title}"
            )
        i = j
    return errors


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve()
    parts = sorted(root.glob("core_10-10_rights_part_*.md"))
    if not parts:
        print("subarticle-gloss audit: no core_10-10_rights_part_*.md under --root")
        return 1

    all_err = subarticle_gloss_errors(root)

    print("Subarticle plain-terms audit (Chapter Ten):")
    print("- Scope: " + ", ".join(p.name for p in parts))
    if all_err:
        print("- Result: FAIL")
        for e in all_err:
            print(f"  - {e}")
        return 1
    print("- Result: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
