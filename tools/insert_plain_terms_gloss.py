#!/usr/bin/env python3
"""Insert ``*In plain terms:*`` glosses into companion subfiles.

A file-level gloss lands after the file-top widget stack and immediately
before the first operative paragraph, matching where the numbered ``core_*``
files put theirs. Glosses are non-operative: they restate, and never extend,
the rules below them.

Reads a JSON mapping whose keys are either a relative path (file-level gloss)
or ``path#Heading text`` (section-level gloss, inserted under that heading).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_PREFIXES = ("#", "<", "---", "*Non-operative", "This file is the")


def insertion_point(lines: list[str]) -> int | None:
    """Index of the first operative prose line under the file-top stack."""
    depth = 0
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if "<details>" in stripped:
            depth += 1
            continue
        if "</details>" in stripped:
            depth = max(0, depth - 1)
            continue
        if depth or not stripped:
            continue
        if stripped.startswith("*In plain terms"):
            return None  # already glossed
        if stripped.startswith(SKIP_PREFIXES):
            continue
        return idx
    return None


def section_insertion_point(lines: list[str], heading: str) -> int | None:
    """Index of the first operative line inside the named section."""
    start = None
    for idx, line in enumerate(lines):
        if line.startswith("#") and line.lstrip("#").strip().startswith(heading):
            start = idx + 1
            break
    if start is None:
        return None

    depth = 0
    for idx in range(start, len(lines)):
        stripped = lines[idx].strip()
        if lines[idx].startswith("#") and not depth:
            # Section opens straight into a subheading: gloss the parent above it.
            return idx
        if "<details>" in stripped:
            depth += 1
            continue
        if "</details>" in stripped:
            depth = max(0, depth - 1)
            continue
        if depth or not stripped:
            continue
        if stripped.startswith("*In plain terms"):
            return None
        if stripped in {"<br>"}:
            continue
        return idx
    return None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--glosses", required=True, help="JSON mapping file.")
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    mapping = json.loads(Path(args.glosses).read_text(encoding="utf-8"))

    applied = skipped = 0
    for key, gloss in mapping.items():
        rel, _, heading = key.partition("#")
        path = root / rel
        if not path.is_file():
            print(f"missing: {rel}", file=sys.stderr)
            return 2
        lines = path.read_text(encoding="utf-8").splitlines()
        idx = (
            section_insertion_point(lines, heading)
            if heading
            else insertion_point(lines)
        )
        if idx is None:
            print(f"skip (already glossed or no prose): {key}")
            skipped += 1
            continue
        text = gloss.strip()
        if not text.startswith("*In plain terms"):
            text = f"*In plain terms: {text}*"
        lines[idx:idx] = [text, ""]
        applied += 1
        print(f"{'wrote' if args.write else 'would insert'} {key}")
        if args.write:
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"\n{applied} inserted, {skipped} skipped")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
