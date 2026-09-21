#!/usr/bin/env python3
"""Rewrite Chapter Five path references after core_05_* rename.

Historical map (already applied on live corpus):
  core_05_definitions_home.md → core_05__definitions_home.md
  core_05apex_*               → core_05_apex_*
  core_05defs_*               → core_05_band_*

Skips archive/ and .git/. Safe to re-run (identity on already-migrated text).
"""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Longest / most specific first. Keep OLD names on the left for re-entry from
# mixed checkouts; already-migrated trees are no-ops.
REPLACEMENTS: list[tuple[str, str]] = [
    ("core_05_definitions_home.md", "core_05__definitions_home.md"),
    ("core_05apex_flourishing_aim.md", "core_05_apex_flourishing_aim.md"),
    ("core_05apex_continuity_aim.md", "core_05_apex_continuity_aim.md"),
    ("core_05apex_accountability_leg.md", "core_05_apex_accountability_leg.md"),
    ("core_05apex_oversight_leg.md", "core_05_apex_oversight_leg.md"),
    ("core_05apex_participation_leg.md", "core_05_apex_participation_leg.md"),
    ("core_05apex_timeliness_leg.md", "core_05_apex_timeliness_leg.md"),
    ("core_05defs_oversight.md", "core_05_band_oversight.md"),
    ("core_05defs_participation.md", "core_05_band_participation.md"),
    ("core_05defs_accountability.md", "core_05_band_accountability.md"),
    ("core_05defs_continuity.md", "core_05_band_continuity.md"),
    ("core_05defs_integrative.md", "core_05_band_integrative.md"),
    ("core_05defs_performance.md", "core_05_band_performance.md"),
    ("core_05apex_*", "core_05_apex_*"),
    ("core_05defs_*", "core_05_band_*"),
    ("`core_05apex_`", "`core_05_apex_`"),
    ("`core_05defs_`", "`core_05_band_`"),
]

SKIP_DIR_PARTS = {
    ".git",
    "archive",
    "node_modules",
}

TEXT_SUFFIXES = {
    ".md",
    ".py",
    ".json",
    ".yml",
    ".yaml",
    ".txt",
    ".csv",
    ".toml",
}


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIR_PARTS for part in path.parts)


def iter_files(root: Path) -> list[Path]:
    out: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file() or should_skip(path):
            continue
        if path.name == "Makefile" or path.suffix in TEXT_SUFFIXES:
            out.append(path)
    makefile = root / "Makefile"
    if makefile.is_file() and makefile not in out:
        out.append(makefile)
    return out


def rewrite(text: str) -> str:
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--root", default=str(ROOT))
    args = parser.parse_args()
    root = Path(args.root).resolve()

    changed: list[Path] = []
    for path in iter_files(root):
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        updated = rewrite(original)
        if updated == original:
            continue
        changed.append(path.relative_to(root))
        if not args.dry_run:
            path.write_text(updated, encoding="utf-8")

    prefix = "DRY-RUN would update" if args.dry_run else "Updated"
    print(f"{prefix} {len(changed)} files")
    for rel in changed[:40]:
        print(f"  - {rel}")
    if len(changed) > 40:
        print(f"  ... and {len(changed) - 40} more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
