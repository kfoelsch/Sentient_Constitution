#!/usr/bin/env python3
"""Renumber CJS-5 letter cluster IDs (CJS-5A.1 … CJS-5E.5) to numeric CJS-5.2 … CJS-5.23.

Also rewrites legacy markdown anchor slugs (cjs-5a1-… → cjs-52-…) and family
banner headings that used letter suffixes.

Run from repository root after reviewing the mapping in CLUSTER_RENUMBER_MAP.
"""

from __future__ import annotations

import sys
from pathlib import Path

SKIP_DIRS = {"archive", ".git", "__pycache__", "node_modules", "ai_corpus"}
EXTENSIONS = {".md", ".py", ".json", ".csv", ".mmd"}

# Longest / most specific IDs first when applying via ordered replacement.
CLUSTER_RENUMBER_MAP: tuple[tuple[str, str], ...] = (
    ("CJS-5E.5", "CJS-5.23"),
    ("CJS-5E.4", "CJS-5.22"),
    ("CJS-5E.3", "CJS-5.21"),
    ("CJS-5E.2", "CJS-5.20"),
    ("CJS-5E.1", "CJS-5.19"),
    ("CJS-5D.3", "CJS-5.18"),
    ("CJS-5D.2", "CJS-5.17"),
    ("CJS-5D.1", "CJS-5.16"),
    ("CJS-5C.4", "CJS-5.15"),
    ("CJS-5C.3", "CJS-5.14"),
    ("CJS-5C.2", "CJS-5.13"),
    ("CJS-5C.1", "CJS-5.12"),
    ("CJS-5B.4", "CJS-5.11"),
    ("CJS-5B.3", "CJS-5.10"),
    ("CJS-5B.2", "CJS-5.9"),
    ("CJS-5B.1", "CJS-5.8"),
    ("CJS-5A.6", "CJS-5.7"),
    ("CJS-5A.5", "CJS-5.6"),
    ("CJS-5A.4", "CJS-5.5"),
    ("CJS-5A.3", "CJS-5.4"),
    ("CJS-5A.2", "CJS-5.3"),
    ("CJS-5A.1", "CJS-5.2"),
)

ANCHOR_RENUMBER_MAP: tuple[tuple[str, str], ...] = tuple(
    (
        f"#cjs-{old.removeprefix('CJS-').lower().replace('.', '')}",
        f"#cjs-{new.removeprefix('CJS-').replace('.', '')}",
    )
    for old, new in CLUSTER_RENUMBER_MAP
)

FAMILY_HEADING_MAP: dict[str, str] = {
    "## CJS-5A: Authority, constraint, secrecy, and procedure": (
        "## Authority, constraint, secrecy, and procedure (CJS-5.2–CJS-5.7)"
    ),
    "## CJS-5B: Evidence, audit, and claim integrity": (
        "## Evidence, audit, and claim integrity (CJS-5.8–CJS-5.11)"
    ),
    "## CJS-5C: Participation, comprehension, and disclosure": (
        "## Participation, comprehension, and disclosure (CJS-5.12–CJS-5.15)"
    ),
    "## CJS-5D: Dependency, exit, and lifecycle integrity": (
        "## Dependency, exit, and lifecycle integrity (CJS-5.16–CJS-5.18)"
    ),
    "## CJS-5E: Failure, robustness, intervention, and correction": (
        "## Failure, robustness, intervention, and correction (CJS-5.19–CJS-5.23)"
    ),
}

FAMILY_RANGE_MAP: tuple[tuple[str, str], ...] = (
    ("CJS-5A", "CJS-5.2–CJS-5.7"),
    ("CJS-5B", "CJS-5.8–CJS-5.11"),
    ("CJS-5C", "CJS-5.12–CJS-5.15"),
    ("CJS-5D", "CJS-5.16–CJS-5.18"),
    ("CJS-5E", "CJS-5.19–CJS-5.23"),
)


def transform(text: str) -> str:
    temps: dict[str, str] = {}
    for idx, (old, new) in enumerate(CLUSTER_RENUMBER_MAP):
        token = f"__CJS5_RENUM_{idx}__"
        temps[token] = new
        text = text.replace(old, token)

    for token, new in temps.items():
        text = text.replace(token, new)

    for old_anchor, new_anchor in ANCHOR_RENUMBER_MAP:
        text = text.replace(old_anchor, new_anchor)

    for old_heading, new_heading in FAMILY_HEADING_MAP.items():
        text = text.replace(old_heading, new_heading)

    # Family shorthand after numbered clusters are migrated.
    for old_family, new_range in FAMILY_RANGE_MAP:
        text = text.replace(old_family, new_range)

    return text


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix not in EXTENSIONS:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name == "renumber_cjs5_numeric.py":
            continue
        yield path


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    root = root.resolve()
    changed: list[Path] = []
    for path in sorted(iter_files(root)):
        original = path.read_text(encoding="utf-8")
        updated = transform(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed.append(path)
    for path in changed:
        print(path.relative_to(root))
    print(f"Updated {len(changed)} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
