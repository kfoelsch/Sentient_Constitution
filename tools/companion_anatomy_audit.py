#!/usr/bin/env python3
"""Audit the reader-facing anatomy of companion implementation subfiles.

The CJS, CS, CI, and CF subfiles are expected to open the way the numbered
``core_*`` files do, so a reader lands on a title and a plain-language summary
rather than on collapsed routing widgets:

1. an ``#`` H1 title carrying the stable family ID;
2. a collapsed **Corpus placement** widget;
3. a one-line ``*In plain terms:*`` gloss before the first operative paragraph.

It also rejects the content-free Trace lines that accumulated across the
companion layers -- a ``Downstream:`` that only names the section it sits in, a
``Read with:`` that cites nothing but its own section, and an ``Upstream:``
repeated verbatim from the file-level Trace block.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from corpus_paths import COMPANION_SUBDIRS

ROOT = Path(__file__).resolve().parents[1]

PLACEMENT_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">Corpus placement '
    "(non-operative): file structure and reading rules</span></strong></summary>"
)
TRACE_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>'
)

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
H1_WITH_ID_RE = re.compile(r"^#\s+(?:CF|CI|CS|CJS)-\S+")
PLAIN_TERMS_RE = re.compile(r"^\*In plain terms[:,]")
# Part of the file-top stack, not the operative body.
OWNER_LINE_RE = re.compile(r"^(?:This file is the |\*?\*?(?:CF|CI|CS|CJS)-[\d.]+)")
SELF_DOWNSTREAM_RE = re.compile(
    r"^- Downstream: this section's local operational requirements", re.I
)
SELF_READ_WITH_RE = re.compile(r"^- Read with: \*\*(?:CF|CI|CS|CJS)-[\d.]+\*\*\.\s*$")

# Redirect stubs and retired family files carry no operative body.
EXEMPT_SUFFIXES = ("cjs_02_implementation_integration_map.md",)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Also require the H1 title to carry the stable family ID.",
    )
    return parser.parse_args()


def companion_paths(root: Path) -> list[Path]:
    paths: list[Path] = []
    for subdir in COMPANION_SUBDIRS:
        base = root / subdir
        if base.is_dir():
            paths.extend(sorted(base.glob("*.md")))
    return [p for p in paths if not p.name.endswith(EXEMPT_SUFFIXES)]


def first_heading(lines: list[str]) -> tuple[int, str, int] | None:
    for idx, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if match:
            return idx, match.group(2).strip(), len(match.group(1))
    return None


def file_level_upstream(lines: list[str]) -> str | None:
    """The ``Upstream:`` line of the first Trace block in the file."""
    in_trace = False
    for line in lines:
        if TRACE_SUMMARY in line:
            in_trace = True
            continue
        if in_trace:
            if line.strip() == "</details>":
                return None
            if line.startswith("- Upstream:"):
                return line.strip()
    return None


def has_gloss_before_prose(lines: list[str]) -> bool:
    """True when an *In plain terms* line precedes the first operative paragraph."""
    depth = 0
    for line in lines:
        stripped = line.strip()
        if "<details>" in stripped:
            depth += 1
            continue
        if "</details>" in stripped:
            depth = max(0, depth - 1)
            continue
        if depth or not stripped:
            continue
        if PLAIN_TERMS_RE.match(stripped):
            return True
        if stripped.startswith(("#", "<", "---", "*Non-operative")):
            continue
        if OWNER_LINE_RE.match(stripped):
            continue
        # First visible non-widget prose line, and no gloss reached it.
        return False
    return False


def audit_file(path: Path, root: Path, *, strict: bool) -> list[str]:
    rel = path.relative_to(root).as_posix()
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    findings: list[str] = []

    heading = first_heading(lines)
    if heading is None:
        findings.append(f"{rel}: file has no heading")
        return findings
    idx, title, level = heading
    if level != 1:
        findings.append(
            f"{rel}:{idx + 1}: file must open with an '#' H1 title "
            f"(found H{level}: {title[:60]!r})"
        )
    elif strict and not H1_WITH_ID_RE.match(lines[idx]):
        findings.append(
            f"{rel}:{idx + 1}: H1 title should carry the stable family ID "
            f"(found {title[:60]!r})"
        )

    if PLACEMENT_SUMMARY not in text:
        findings.append(f"{rel}: missing file-top Corpus placement widget")

    if not has_gloss_before_prose(lines):
        findings.append(
            f"{rel}: needs an '*In plain terms:*' gloss before the first "
            "operative paragraph"
        )

    top_upstream = file_level_upstream(lines)
    upstream_repeats: list[int] = []
    for number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if SELF_DOWNSTREAM_RE.match(stripped):
            findings.append(
                f"{rel}:{number}: self-referential Downstream line carries no routing"
            )
        if SELF_READ_WITH_RE.match(stripped):
            findings.append(f"{rel}:{number}: 'Read with' cites only its own section")
        if top_upstream and stripped == top_upstream:
            upstream_repeats.append(number)

    for number in upstream_repeats[1:]:
        findings.append(
            f"{rel}:{number}: Upstream line repeats the file-level Trace verbatim"
        )

    return findings


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    findings: list[str] = []
    paths = companion_paths(root)
    for path in paths:
        findings.extend(audit_file(path, root, strict=args.strict))

    if findings:
        print("Companion anatomy audit failures:", file=sys.stderr)
        for item in findings:
            print(f"  - {item}", file=sys.stderr)
        print(f"Total: {len(findings)} across {len(paths)} files", file=sys.stderr)
        return 1

    print(f"Companion anatomy audit OK ({len(paths)} files).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
