#!/usr/bin/env python3
"""Audit Chapter Five section 1 alphabetical order.

Checks the section 1 Independent Definitions headings in
core_05-05_definitions_a_independent.md.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
import sys
from ch5_paths import CH5_PART_A

CH5_FILE_PATTERN = re.compile(r"^core_05-05_definitions_.*\.md$")
SECTION1_HEADING = "### 1. Independent Definitions"
HEADING_RE = re.compile(r"^####\s+(.+)$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Workspace root (default: .)")
    parser.add_argument(
        "--file",
        default=CH5_PART_A,
        help="Chapter Five Markdown file under --root.",
    )
    parser.add_argument(
        "--only-if-ch5-changed",
        action="store_true",
        help="Skip the audit unless a Chapter Five file has changed in git.",
    )
    return parser.parse_args()


def git_changed_files(root: pathlib.Path) -> set[str]:
    changed: set[str] = set()

    def run_git(args: list[str]) -> list[str]:
        try:
            proc = subprocess.run(
                ["git"] + args,
                cwd=root,
                capture_output=True,
                text=True,
                check=False,
            )
        except FileNotFoundError:
            return []
        if proc.returncode != 0:
            return []
        return [line.strip() for line in proc.stdout.splitlines() if line.strip()]

    changed.update(run_git(["diff", "--name-only", "HEAD"]))
    changed.update(run_git(["diff", "--name-only", "--cached", "HEAD"]))
    return changed


def normalize_key(label: str) -> str:
    return label.casefold()


def collect_section1_headings(lines: list[str]) -> list[tuple[int, str]]:
    try:
        start = next(i for i, line in enumerate(lines) if line.strip() == SECTION1_HEADING)
    except StopIteration:
        raise ValueError(f"Missing section 1 heading: {SECTION1_HEADING}")

    headings: list[tuple[int, str]] = []
    for i in range(start + 1, len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        match = HEADING_RE.match(line)
        if match:
            headings.append((i + 1, match.group(1).strip()))
    if not headings:
        raise ValueError("Unable to parse any section 1 headings after the section heading.")
    return headings


def find_order_violations(items: list[tuple[int, str]]) -> list[str]:
    violations: list[str] = []
    prev_key: str | None = None
    prev_label = ""
    for lineno, label in items:
        key = normalize_key(label)
        if prev_key is not None and key < prev_key:
            violations.append(
                f"line {lineno}: '{label}' should come before '{prev_label}' in alphabetical order"
            )
        prev_key = key
        prev_label = label
    return violations


def audit_file(path: pathlib.Path) -> list[str]:
    raw = path.read_text(encoding="utf-8")
    lines = raw.splitlines()

    violations: list[str] = []
    try:
        section1_headings = collect_section1_headings(lines)
    except ValueError as exc:
        violations.append(str(exc))
    else:
        for violation in find_order_violations(section1_headings):
            violations.append(f"{path}:{violation}")

    return violations


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root)
    path = root / args.file
    if args.only_if_ch5_changed:
        changed = git_changed_files(root)
        if not any(CH5_FILE_PATTERN.match(name) for name in changed):
            print("SKIP: no Chapter Five file changes detected.")
            return 0

    if not path.exists():
        print(f"Missing required file: {path}", file=sys.stderr)
        return 1

    violations = audit_file(path)
    if violations:
        print("FAIL: Chapter Five alphabetical order audit detected issues:")
        for violation in violations:
            print(violation)
        return 1

    print("PASS: Chapter Five section 1 headings are alphabetically ordered.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
