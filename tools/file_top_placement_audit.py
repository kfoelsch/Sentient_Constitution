#!/usr/bin/env python3
"""Audit file-top Corpus placement widget discipline.

Rule: NAV-PLACEMENT-01 in tools/architecture/rule_registry.json.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PLACEMENT_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">Corpus placement '
    "(non-operative): file structure and reading rules</span></strong></summary>"
)
BINDING_OUTSIDE = re.compile(
    r"^This file is \*\*part of the Sentient Constitution\*\* and is \*\*binding only together\*\*"
)
CORPUS_EDITION_VISIBLE = re.compile(r"^\*\*Corpus edition:\*\*")
QUICK_ORIENTATION_VISIBLE = re.compile(r"^\*\*Quick orientation\*\*")
APPLICATION_BASELINE = re.compile(r"^\*\*Application baseline\.\*\*")

CORE_GLOB = "core_*.md"
REGISTRY_GLOBS = (
    "corpus_joint_structure/*_00_registry_and_reading_rules.md",
    "corpus_systems/*_00_registry_and_reading_rules.md",
    "corpus_institutions/*_00_registry_and_reading_rules.md",
    "corpus_forum/*_00_registry_and_reading_rules.md",
)
# There are no live redirect stubs in the normalized CJS family.
PLACEMENT_EXEMPT: set[str] = set()
COMPANION_GLOBS = (
    "corpus_joint_structure/*.md",
    "corpus_systems/*.md",
    "corpus_institutions/*.md",
    "corpus_forum/*.md",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--include-companions",
        action="store_true",
        help=(
            "Apply placement-widget discipline to every companion subfile, not "
            "only the *_00 registry annexes."
        ),
    )
    return parser.parse_args()


HEADING_RE = re.compile(r"^#{1,6} ")


def file_top_region(lines: list[str]) -> list[str]:
    """File-top block: the leading title heading plus the widgets beneath it.

    The block runs from the start of the file through the leading ``#`` title
    and any Corpus placement / reader-guidance widgets, stopping at the first
    section heading that follows the title. This supports files whose single
    visible title is the chapter heading itself (``# CHAPTER …``) with body
    sections at ``###`` and no intervening ``##``.
    """
    region: list[str] = []
    seen_title = False
    for line in lines:
        if HEADING_RE.match(line):
            if not seen_title:
                seen_title = True
                region.append(line)
                continue
            break
        region.append(line)
    return region


def placement_widget_count(region: list[str]) -> int:
    count = 0
    in_placement = False
    for line in region:
        if PLACEMENT_SUMMARY in line:
            in_placement = True
            count += 1
        elif in_placement and line.strip() == "</details>":
            in_placement = False
    return count


def visible_file_top_prose_lines(region: list[str]) -> list[tuple[int, str]]:
    """Non-operative prose lines visible before the first ## heading."""
    allowed_prefixes = ("#", "<", "---", "")
    findings: list[tuple[int, str]] = []
    in_details = False
    for idx, line in enumerate(region, start=1):
        stripped = line.strip()
        if PLACEMENT_SUMMARY in line:
            in_details = True
            continue
        if in_details:
            if stripped == "</details>":
                in_details = False
            continue
        if stripped in {"", "<br>", "---"}:
            continue
        if stripped.startswith("*Non-operative subtitle:*"):
            continue
        if stripped.startswith(allowed_prefixes):
            continue
        findings.append((idx, stripped[:80]))
    return findings


def audit_core(path: Path, root: Path) -> list[str]:
    rel = path.relative_to(root).as_posix()
    if rel.startswith("archive/"):
        return []

    lines = path.read_text(encoding="utf-8").splitlines()
    region = file_top_region(lines)
    findings: list[str] = []

    if placement_widget_count(region) != 1:
        findings.append(
            f"{rel}: expected exactly one file-top Corpus placement widget "
            f"(found {placement_widget_count(region)})"
        )

    for idx, line in enumerate(region, start=1):
        if BINDING_OUTSIDE.match(line.strip()):
            findings.append(
                f"{rel}:{idx}: binding banner must be inside Corpus placement widget, not visible"
            )

    for idx, snippet in visible_file_top_prose_lines(region):
        findings.append(
            f"{rel}:{idx}: visible file-top prose must move into Corpus placement widget "
            f"(starts: {snippet!r})"
        )

    for idx, line in enumerate(lines, start=1):
        if APPLICATION_BASELINE.match(line.strip()):
            findings.append(
                f"{rel}:{idx}: Application baseline paragraphs are retired; "
                "move scope notes into Corpus placement or reader-guidance widgets"
            )

    return findings


def audit_registry(path: Path, root: Path) -> list[str]:
    rel = path.relative_to(root).as_posix()
    lines = path.read_text(encoding="utf-8").splitlines()
    region = file_top_region(lines)
    findings: list[str] = []

    if placement_widget_count(region) != 1:
        findings.append(
            f"{rel}: expected exactly one file-top Corpus placement widget "
            f"(found {placement_widget_count(region)})"
        )

    for idx, line in enumerate(region, start=1):
        stripped = line.strip()
        if CORPUS_EDITION_VISIBLE.match(stripped):
            findings.append(
                f"{rel}:{idx}: visible Corpus edition line must move inside placement widget"
            )
        if QUICK_ORIENTATION_VISIBLE.match(stripped):
            findings.append(
                f"{rel}:{idx}: visible Quick orientation must move inside placement widget"
            )

    # No extra file-top reader-guidance widgets before first ##.
    for idx, line in enumerate(region, start=1):
        if "Reader guidance (non-operative):" in line and PLACEMENT_SUMMARY not in line:
            findings.append(
                f"{rel}:{idx}: merge file-top Reader guidance into single Corpus placement widget"
            )

    return findings


def audit_companion(path: Path, root: Path) -> list[str]:
    """Placement discipline for substantive companion subfiles.

    Looser than the ``*_00`` registry annexes in two ways, matching how the
    numbered ``core_*`` files already read: a visible **Quick orientation**
    block is a reader aid rather than a competing front door, and a separate
    **Reader guidance** widget is permitted alongside Corpus placement
    (NAV-READER-06).
    """
    rel = path.relative_to(root).as_posix()
    if path.name in PLACEMENT_EXEMPT:
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    count = placement_widget_count(file_top_region(lines))
    if count != 1:
        return [
            f"{rel}: expected exactly one file-top Corpus placement widget (found {count})"
        ]
    return []


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    all_findings: list[str] = []

    for path in sorted(root.glob(CORE_GLOB)):
        if path.is_file():
            all_findings.extend(audit_core(path, root))

    registry_paths = {
        path
        for pattern in REGISTRY_GLOBS
        for path in root.glob(pattern)
        if path.is_file()
    }
    for path in sorted(registry_paths):
        all_findings.extend(audit_registry(path, root))

    if args.include_companions:
        for pattern in COMPANION_GLOBS:
            for path in sorted(root.glob(pattern)):
                if path.is_file() and path not in registry_paths:
                    all_findings.extend(audit_companion(path, root))

    if all_findings:
        print("File-top placement audit failures:", file=sys.stderr)
        for item in all_findings:
            print(f"  - {item}", file=sys.stderr)
        print(f"Total: {len(all_findings)}", file=sys.stderr)
        return 1

    print("File-top placement audit OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
