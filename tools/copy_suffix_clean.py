#!/usr/bin/env python3
"""Find and remove copy-suffixed duplicate files (FILE-COPY-SUFFIX-01).

A file such as ``core_07.000_charters 2.md`` beside ``core_07.000_charters.md`` is a copy made by a
file manager or sync client. It is not corpus and may be deleted freely, provided the
original exists and git does not track the copy.

  python3 tools/copy_suffix_clean.py            # list candidates (dry run, exit 0)
  python3 tools/copy_suffix_clean.py --write    # delete them

A tracked file with this naming pattern, or a copy whose original is missing, is never
deleted; it is reported and needs a person. The list notes copies whose content differs
from the original, in case a change is worth porting by hand before deleting.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r"^(?P<stem>.+) (?P<n>\d+)(?P<ext>\.[^.]+)?$")
SKIP_DIRS = {".git", "node_modules", "_pages_site"}


def tracked(root: Path) -> set[str]:
    out = subprocess.run(["git", "ls-files", "-z"], cwd=root, capture_output=True, check=True).stdout
    return {p for p in out.decode("utf-8").split("\0") if p}


def find_copies(root: Path) -> list[Path]:
    found: list[Path] = []
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        if path.is_file() and PATTERN.match(path.name):
            found.append(path)
    return sorted(found)


def original_of(path: Path) -> Path:
    m = PATTERN.match(path.name)
    assert m
    return path.with_name(m.group("stem") + (m.group("ext") or ""))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--write", action="store_true", help="delete the removable copies")
    args = ap.parse_args(argv)
    root = Path(args.root).resolve()
    tr = tracked(root)

    removable: list[Path] = []
    for path in find_copies(root):
        rel = path.relative_to(root).as_posix()
        orig = original_of(path)
        if rel in tr:
            print(f"KEEP (tracked, filename-convention defect): {rel}")
        elif not orig.exists():
            print(f"KEEP (original missing): {rel}")
        else:
            try:
                differs = path.read_bytes() != orig.read_bytes()
            except OSError:
                # A sync-conflict copy can be locked or unreadable; fall back to comparing sizes.
                differs = path.stat().st_size != orig.stat().st_size
            print(f"{'REMOVE' if args.write else 'would remove'}{' (differs from original)' if differs else ''}: {rel}")
            removable.append(path)

    deleted = 0
    if args.write:
        for path in removable:
            try:
                path.unlink()
                deleted += 1
            except OSError as exc:
                print(f"COULD NOT DELETE ({exc.strerror}): {path.relative_to(root).as_posix()}")
    noun = "copy" if len(removable) == 1 else "copies"
    if args.write:
        print(f"copy-suffix-clean: {deleted} of {len(removable)} removable {noun} deleted")
    else:
        print(f"copy-suffix-clean: {len(removable)} removable {noun} found (dry run; use --write)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
