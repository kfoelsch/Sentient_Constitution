#!/usr/bin/env python3
"""Audit Chapter Five cross-link navigation metadata placement.

This check enforces the Chapter Five authoring rule that navigation metadata such
as ``Read with:`` and cluster ``**Read-with definitions.**`` lines belong inside
a local ``Trace`` / ``<details>`` block rather than as standalone prose in the
operative definition body.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from ch5_paths import CH5_ALL

READ_WITH_LINE_RE = re.compile(r"^(- )?Read with:", re.IGNORECASE)
READ_WITH_DEFINITIONS_RE = re.compile(r"\*\*Read-with definitions\.\*\*", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Workspace root (default: .).")
    return parser.parse_args()


def audit_file(path: Path) -> list[tuple[int, str, str]]:
    text = path.read_text(encoding="utf-8")
    violations: list[tuple[int, str, str]] = []
    in_details = 0
    in_fence = False

    for lineno, raw_line in enumerate(text.splitlines(), start=1):
        stripped = raw_line.strip()

        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        if stripped == "<details>":
            in_details += 1
            continue
        if stripped == "</details>":
            in_details = max(0, in_details - 1)
            continue

        if in_details:
            continue

        if READ_WITH_LINE_RE.match(stripped):
            violations.append((lineno, "Read with:", raw_line))
            continue
        if READ_WITH_DEFINITIONS_RE.search(stripped):
            violations.append((lineno, "Read-with definitions", raw_line))

    return violations


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    all_violations: list[tuple[str, int, str, str]] = []

    for rel in CH5_ALL:
        path = root / rel
        if not path.is_file():
            print(f"Missing required file: {path}", file=sys.stderr)
            return 1
        for lineno, kind, raw_line in audit_file(path):
            all_violations.append((rel, lineno, kind, raw_line))

    if all_violations:
        for rel, lineno, kind, raw_line in all_violations:
            print(
                f"{rel}:{lineno}: '{kind}' must appear inside the local Trace/details block, "
                f"not as standalone body prose: {raw_line.strip()}",
                file=sys.stderr,
            )
        return 1

    print("PASS: Chapter Five cross-link metadata stays inside Trace/details blocks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
