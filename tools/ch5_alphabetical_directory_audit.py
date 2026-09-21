#!/usr/bin/env python3
"""Audit Chapter Five alphabetical directory and section 1 order.

Checks the non-operative Definitions A-Z / Clusters A-Z directory in
``core_05__definitions_home.md`` and preserves the older section 1
Independent Definitions heading-order check.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
import sys
from ch5_paths import CH5_PART_A
from ch5_single_definition_audit import (
    collect_entries_and_clusters,
    parse_directory,
    sorted_violations,
)

CH5_FILE_PATTERN = re.compile(
    r"^core_05(?:-05_definitions_a_independent|_apex_[a-z_]+|_band_[a-z]+|__definitions_home)\.md$"
)
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
        # Stop at the next H3 (section 2+); do not scan the alphabetical directory.
        if line.startswith("### ") and not line.startswith("#### "):
            break
        match = HEADING_RE.match(line)
        if match:
            headings.append((i + 1, match.group(1).strip()))
    # Section 1 may be meta-only (no #### children); directory order is audited separately.
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
    if SECTION1_HEADING in raw:
        try:
            section1_headings = collect_section1_headings(lines)
        except ValueError as exc:
            violations.append(str(exc))
        else:
            for violation in find_order_violations(section1_headings):
                violations.append(f"{path}:{violation}")

    return violations


def audit_directory(root: pathlib.Path) -> list[str]:
    violations: list[str] = []
    rows, parse_violations = parse_directory(root)
    violations.extend(parse_violations)
    if not rows:
        return violations

    directory_labels: dict[str, list[str]] = {}
    for row in rows:
        directory_labels.setdefault(row.label, []).append(
            f"line {row.line} ({row.list_name})"
        )
    for label, locations in sorted(directory_labels.items()):
        if len(locations) > 1:
            violations.append(
                f"{root / CH5_PART_A}: duplicate directory display label "
                f"'{label}': {', '.join(locations)}"
            )
    violations.extend(sorted_violations(rows))

    entries, clusters = collect_entries_and_clusters(root)
    expected_defs = {(entry.label, entry.href) for entry in entries}
    actual_defs = {
        (row.label, row.href) for row in rows if row.list_name == "Definitions A-Z"
    }
    from ch5_paths import CH5_APEX

    apex_prefix = tuple(f"{name}#" for name in CH5_APEX)
    actual_defs_leaves = {
        (label, href)
        for label, href in actual_defs
        if not href.startswith(apex_prefix)
    }
    expected_clusters = {(cluster.label, cluster.href) for cluster in clusters}
    actual_clusters = {
        (row.label, row.href) for row in rows if row.list_name == "Clusters A-Z"
    }
    for label, href in sorted(expected_defs - actual_defs):
        violations.append(f"{root / CH5_PART_A}: missing definition directory row [{label}]({href})")
    for label, href in sorted(actual_defs_leaves - expected_defs):
        violations.append(f"{root / CH5_PART_A}: extra definition directory row [{label}]({href})")
    for label, href in sorted(expected_clusters - actual_clusters):
        violations.append(f"{root / CH5_PART_A}: missing cluster directory row [{label}]({href})")
    for label, href in sorted(actual_clusters - expected_clusters):
        violations.append(f"{root / CH5_PART_A}: extra cluster directory row [{label}]({href})")
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

    violations = audit_directory(root)
    violations.extend(audit_file(path))
    if violations:
        print("FAIL: Chapter Five alphabetical directory audit detected issues:")
        for violation in violations:
            print(violation)
        return 1

    print("PASS: Chapter Five directory rows and section 1 headings are alphabetically ordered.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
