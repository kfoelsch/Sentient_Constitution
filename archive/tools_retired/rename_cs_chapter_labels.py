#!/usr/bin/env python3
"""Rename legacy Chapter CS-3/CS-4/CS-5 systems labels to CS-3/CS-4/CS-5."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {"archive", ".git", ".cursor", "node_modules", "__pycache__"}
EXTENSIONS = {".md", ".py", ".json", ".csv"}

# Longest / most specific patterns first.
REPLACEMENTS: list[tuple[str, str]] = [
    ("CS-3: Information types and handling", "CS-3: Information types and handling"),
    ("CS-4: System classification and handling", "CS-4: System classification and handling"),
    ("CS-5: Critical system stewardship", "CS-5: Critical system stewardship"),
    (
        "CS-5 — Critical system steward conduct, conflicts of interest, and independence",
        "CS-5 — Critical system steward conduct, conflicts of interest, and independence",
    ),
    ("CS-3 — Information types and handling", "CS-3 — Information types and handling"),
    ("CS-4 — System classification and handling", "CS-4 — System classification and handling"),
    ("CS-5 — Critical system stewardship", "CS-5 — Critical system stewardship"),
    ("SYS-CS-3", "SYS-CS-3"),
    ("SYS-CS-4", "SYS-CS-4"),
    ("SYS-CS-5", "SYS-CS-5"),
    ("CS-4/CS-5", "CS-4/CS-5"),
    ("CS-3/CS-4/CS-5", "CS-3/CS-4/CS-5"),
    ("CS-3–CS-5", "CS-3–CS-5"),
    ("CS-3/CS-4", "CS-3/CS-4"),
    ("CS-4–CS-5", "CS-4–CS-5"),
    ("CS-4/CS-5", "CS-4/CS-5"),
    ("CS-3 → CS-4 → CS-5", "CS-3 → CS-4 → CS-5"),
    ("CS-3/CS-4/CS-5", "CS-3/CS-4/CS-5"),
    ("CS-3–CS-5", "CS-3–CS-5"),
    ("CS-3/CS-4", "CS-3/CS-4"),
    ("CS-4/CS-5", "CS-4/CS-5"),
    ("CS-3, CS-4, CS-5", "CS-3, CS-4, CS-5"),
    ("**CS-3, CS-4, CS-5**", "**CS-3, CS-4, CS-5**"),
    ("CS-3/CS-4/CS-5", "CS-3/CS-4/CS-5"),
    ("CS-3/CS-4", "CS-3/CS-4"),
    ("CS-3–CS-5", "CS-3–CS-5"),
    ("CS-3", "CS-3"),
    ("CS-4", "CS-4"),
    ("CS-5", "CS-5"),
    ("**CS-3–CS-5**", "**CS-3–CS-5**"),
    ("CS-3–CS-5", "CS-3–CS-5"),
    ("Chapters CS-3–CS-5", "CS-3–CS-5"),
    ("Chapters **CS-3, CS-4, CS-5**", "**CS-3, CS-4, CS-5**"),
    ("Chapters **CS-3, CS-4, CS-5** only", "**CS-3, CS-4, CS-5** only"),
    ("**CS-3–CS-5**", "**CS-3–CS-5**"),
    ("**CS-3–CS-5** headings", "**CS-3–CS-5** headings"),
    ("**CS-3–CS-5**", "**CS-3–CS-5**"),
    ("CS-3–CS-5", "CS-3–CS-5"),
    ("**CS-4 — System classification and handling**", "**CS-4 — System classification and handling**"),
    ("**CS-5**, and named protocols", "**CS-5**, and named protocols"),
    ("CS-3", "CS-3"),
    ("CS-4", "CS-4"),
    ("CS-5", "CS-5"),
    ("CS-3–CS-5 taxonomy", "CS-3–CS-5 taxonomy"),
    ("CS section label", "CS section label"),
    ("CS-3", "CS-3"),
    ("CS-4", "CS-4"),
    ("CS-5", "CS-5"),
    ("Type N via CS-3", "Type N via CS-3"),
    ("preserving CS-4 as", "preserving CS-4 as"),
    ("**CS-4/CS-5** tables", "**CS-4/CS-5** tables"),
    ("CS-4/CS-5 tables", "CS-4/CS-5 tables"),
    ("**CS-4/CS-5**", "**CS-4/CS-5**"),
    ("where **CS-4/CS-5**", "where **CS-4/CS-5**"),
    ("CS-4/CS-5", "CS-4/CS-5"),
    ("for **CS-4**", "for **CS-4**"),
]


def iter_files() -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in EXTENSIONS:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        paths.append(path)
    return sorted(paths)


def migrate_text(text: str) -> str:
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    return text


def main() -> int:
    changed: list[Path] = []
    for path in iter_files():
        original = path.read_text(encoding="utf-8")
        updated = migrate_text(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed.append(path)

    for path in changed:
        print(path.relative_to(ROOT))
    print(f"\nUpdated {len(changed)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
