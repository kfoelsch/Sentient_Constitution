#!/usr/bin/env python3
"""Audit Chapter Five cross-link navigation metadata placement.

This check enforces the Chapter Five authoring rule that navigation metadata such
as ``Read with:`` belongs inside a local ``Trace`` / ``<details>`` block rather
than as standalone prose in the operative definition body.
"""

from __future__ import annotations

import argparse
import pathlib
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Workspace root (default: .).")
    parser.add_argument(
        "--file",
        default="core_05-05_definitions_a_independent.md",
        help="Chapter Five Markdown file under --root.",
    )
    return parser.parse_args()


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def main() -> int:
    args = parse_args()
    path = pathlib.Path(args.root) / args.file

    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Missing required file: {path}", file=sys.stderr)
        return 1

    in_details = False
    violations: list[tuple[int, str]] = []

    for lineno, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if line == "<details>":
            in_details = True
            continue
        if line == "</details>":
            in_details = False
            continue
        if line.startswith("Read with:") and not in_details:
            violations.append((lineno, raw_line))

    if violations:
        for lineno, raw_line in violations:
            print(
                f"{path}:{lineno}: 'Read with:' must appear inside the local Trace/details block, "
                f"not as standalone body prose: {raw_line.strip()}",
                file=sys.stderr,
            )
        return 1

    print("PASS: Chapter Five cross-link metadata stays inside Trace/details blocks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
