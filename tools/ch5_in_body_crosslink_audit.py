#!/usr/bin/env python3
"""Verify Chapter Five has at least one required in-body cross-definition link.

This audit is intentionally narrow. It proves a specific regression-sensitive case:
the ``Accountability`` definition must contain Markdown links to ``Auditability`` and
``Contestability`` in its O/E/C body, not only inside the preceding trace/details block.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys


ACCOUNTABILITY_BLOCK = re.compile(
    r"(?ms)^#### Accountability\s*\n(?P<after_heading>.*?)(?=^#### |\Z)"
)
DETAILS_BLOCK = re.compile(r"(?ms)^<details>\n.*?^</details>\s*\n")


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

    match = ACCOUNTABILITY_BLOCK.search(text)
    if not match:
        print("Missing expected '#### Accountability' definition block.", file=sys.stderr)
        return 1

    block_start = match.start()
    block_text = match.group("after_heading")
    body_text = DETAILS_BLOCK.sub("", block_text, count=1)

    missing = []
    for expected in (
        "[Auditability](#auditability)",
        "[Contestability](#contestability)",
    ):
        if expected not in body_text:
            missing.append(expected)

    if missing:
        start_line = line_number(text, block_start)
        print(
            f"{path}:{start_line}: Accountability must include in-body links after the trace block: "
            + ", ".join(missing),
            file=sys.stderr,
        )
        return 1

    print("PASS: Accountability contains required in-body cross-links after the trace block.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
