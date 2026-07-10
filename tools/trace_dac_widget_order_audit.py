#!/usr/bin/env python3
"""Audit Trace → D/A/C widget placement under owning headings.

Rule: NAV-DAC-12-ORDER in tools/architecture/rule_registry.json.

When a ``####`` or ``#####`` unit (or a ``###`` unit whose Trace block carries
Chapter Five ``· [O]`` read-with links) opens with a Trace ``<details>`` widget,
the next substantive block after ``</details>`` must be either:

1. a **Definitions · Assessment · Compliance** ``<details>`` widget, or
2. a single-concept inline ``<strong>…Definition:</strong>`` line.

Only blank lines may appear between Trace close and that definition carrier.
``<br>``, *In plain terms*, anchor tags, or operative prose must not intervene.

Sections whose Trace blocks carry no Chapter Five ``· [O]`` read-with links are
exempt from the requirement (structural / routing-only traces).

Without Trace, the D/A/C widget must be the first substantive block under the
owning ``####`` or ``#####`` heading (before *In plain terms* or operative prose).

A ``###`` heading that carries a small roadmap-only D/A/C widget (two or fewer
O/E/C rows) must not also host ``####`` subsections with their own D/A/C widgets
(roadmap exclusion).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from corpus_paths import binding_corpus_scope

ROOT = Path(__file__).resolve().parents[1]

TRACE_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>'
)
DEC_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">'
    "Definitions · Assessment · Compliance</span></strong></summary>"
)
INLINE_DEFINITION_RE = re.compile(
    r"<strong><span style=\"color: #2563eb;\">Definition:</span></strong>"
)
OEC_READ_WITH_RE = re.compile(r"· \[O\]\(")
OEC_ROW_RE = re.compile(
    r"^\s*-\s+\[[^\]]+\]\([^)]+\)\s*·\s*\[O\]\([^)]+\)\s*·\s*\[A\]\([^)]+\)\s*·\s*\[C\]\([^)]+\)\s*$"
)
HEADING_RE = re.compile(r"^(#{1,6})\s+")
PLAIN_TERMS_RE = re.compile(r"^\*In plain terms:")
ANCHOR_RE = re.compile(r'^<a id="[^"]+"></a>$')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    return parser.parse_args()


def next_nonempty(lines: list[str], start: int) -> int | None:
    for idx in range(start, len(lines)):
        if lines[idx].strip():
            return idx
    return None


def heading_level(line: str) -> int | None:
    m = HEADING_RE.match(line.strip())
    return len(m.group(1)) if m else None


def nearest_heading(lines: list[str], before_idx: int) -> tuple[int, str, int] | None:
    for idx in range(before_idx, -1, -1):
        stripped = lines[idx].strip()
        level = heading_level(stripped)
        if level is not None:
            return idx, stripped, level
    return None


def trace_block_needs_definition(trace_lines: list[str]) -> bool:
    return any(OEC_READ_WITH_RE.search(line) for line in trace_lines)


def classify_definition_carrier(lines: list[str], idx: int) -> str | None:
    stripped = lines[idx].strip()
    if stripped == "<details>":
        summary_idx = next_nonempty(lines, idx + 1)
        if summary_idx is not None and lines[summary_idx].strip() == DEC_SUMMARY:
            return "dec-widget"
        return None
    if INLINE_DEFINITION_RE.search(stripped):
        return "inline-definition"
    return None


def section_end(lines: list[str], start: int, level: int) -> int:
    for idx in range(start + 1, len(lines)):
        next_level = heading_level(lines[idx])
        if next_level is not None and next_level <= level:
            return idx
    return len(lines)


def is_skippable_before_dec(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if ANCHOR_RE.match(stripped):
        return True
    return False


def is_substantive_before_dec(line: str) -> bool:
    stripped = line.strip()
    if not stripped or is_skippable_before_dec(line):
        return False
    if stripped == "<details>" or stripped == "</details>":
        return False
    if TRACE_SUMMARY in stripped or DEC_SUMMARY in stripped:
        return False
    return True


def find_dec_widget(lines: list[str], start: int, end: int) -> int | None:
    idx = start
    while idx < end:
        if lines[idx].strip() == "<details>":
            summary_idx = next_nonempty(lines, idx + 1)
            if (
                summary_idx is not None
                and summary_idx < end
                and lines[summary_idx].strip() == DEC_SUMMARY
            ):
                return idx
        idx += 1
    return None


def unit_has_trace(lines: list[str], start: int, end: int) -> bool:
    idx = start
    while idx < end:
        if lines[idx].strip() == "<details>":
            summary_idx = next_nonempty(lines, idx + 1)
            if (
                summary_idx is not None
                and summary_idx < end
                and lines[summary_idx].strip() == TRACE_SUMMARY
            ):
                return True
        idx += 1
    return False


def count_dec_rows(lines: list[str], dec_open_idx: int, end: int) -> int:
    count = 0
    idx = dec_open_idx + 1
    while idx < end and lines[idx].strip() != "</details>":
        if OEC_ROW_RE.match(lines[idx]):
            count += 1
        idx += 1
    return count


def audit_dec_without_trace_placement(
    lines: list[str], rel: str, start: int, end: int, heading_text: str, level: int
) -> list[str]:
    if level < 4 or unit_has_trace(lines, start, end):
        return []

    dec_idx = find_dec_widget(lines, start, end)
    if dec_idx is None:
        return []

    for idx in range(start + 1, dec_idx):
        if is_substantive_before_dec(lines[idx]):
            preview = lines[idx].strip()[:72]
            return [
                f"{rel}:{idx + 1}: D/A/C widget on {heading_text!r} must be the "
                f"first substantive block under the heading (found prose first: "
                f"{preview!r})"
            ]
    return []


def audit_roadmap_exclusion_parent_dec(
    lines: list[str], rel: str, start: int, end: int, heading_text: str, level: int
) -> list[str]:
    if level != 3 or not rel.startswith("core_01_"):
        return []

    first_child = end
    for idx in range(start + 1, end):
        if heading_level(lines[idx]) == 4:
            first_child = idx
            break

    parent_dec = find_dec_widget(lines, start, first_child)
    if parent_dec is None:
        return []

    row_count = count_dec_rows(lines, parent_dec, first_child)
    if row_count > 2:
        return []

    for idx in range(first_child, end):
        if heading_level(lines[idx]) != 4:
            continue
        child_end = section_end(lines, idx, 4)
        if find_dec_widget(lines, idx, child_end) is not None:
            return [
                f"{rel}:{parent_dec + 1}: remove roadmap-only parent D/A/C widget on "
                f"{heading_text!r} ({row_count} row(s)); subsection "
                f"{lines[idx].strip()!r} owns the operative definitions "
                f"(roadmap exclusion)"
            ]

    return []


def audit_heading_units(path: Path, root: Path) -> list[str]:
    rel = path.relative_to(root).as_posix()
    if rel.startswith("core_05-05_definitions_"):
        return []

    lines = path.read_text(encoding="utf-8").splitlines()
    findings: list[str] = []

    for idx, line in enumerate(lines):
        level = heading_level(line)
        if level is None or level < 3:
            continue
        end = section_end(lines, idx, level)
        heading_text = line.strip()
        findings.extend(
            audit_dec_without_trace_placement(
                lines, rel, idx, end, heading_text, level
            )
        )
        findings.extend(
            audit_roadmap_exclusion_parent_dec(
                lines, rel, idx, end, heading_text, level
            )
        )

    return findings


def audit_file(path: Path, root: Path) -> list[str]:
    rel = path.relative_to(root).as_posix()
    if rel.startswith("core_05-05_definitions_"):
        return []

    lines = path.read_text(encoding="utf-8").splitlines()
    findings: list[str] = []

    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if TRACE_SUMMARY not in line:
            idx += 1
            continue
        if idx == 0 or lines[idx - 1].strip() != "<details>":
            idx += 1
            continue

        heading_info = nearest_heading(lines, idx - 1)
        if heading_info is None:
            idx += 1
            continue
        _, heading_text, level = heading_info

        trace_start = idx - 1
        close_idx = idx + 1
        trace_body: list[str] = []
        while close_idx < len(lines) and lines[close_idx].strip() != "</details>":
            trace_body.append(lines[close_idx])
            close_idx += 1
        if close_idx >= len(lines):
            idx += 1
            continue

        needs_def = trace_block_needs_definition(trace_body)
        applies = needs_def and level >= 3  # ###, ####, and #####

        scan_idx = next_nonempty(lines, close_idx + 1)
        carrier = (
            classify_definition_carrier(lines, scan_idx)
            if scan_idx is not None
            else None
        )

        if applies and carrier is None:
            preview = lines[scan_idx].strip()[:72] if scan_idx is not None else "EOF"
            findings.append(
                f"{rel}:{close_idx + 1}: Trace on {heading_text!r} must be "
                f"followed immediately by a D/A/C widget or inline Definition "
                f"(next line {scan_idx + 1 if scan_idx is not None else '?'}: "
                f"{preview!r})"
            )
        elif carrier is not None:
            # Misplaced carrier: blank lines only between trace close and carrier.
            between = lines[close_idx + 1 : scan_idx]
            bad = [
                (close_idx + 1 + offset, row.strip())
                for offset, row in enumerate(between)
                if row.strip()
            ]
            if bad:
                ln, text = bad[0]
                findings.append(
                    f"{rel}:{ln}: remove intervening content between Trace close "
                    f"and definition carrier on {heading_text!r} ({text[:72]!r})"
                )

        idx = close_idx + 1

    findings.extend(audit_heading_units(path, root))
    return findings


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    findings: list[str] = []
    for rel in binding_corpus_scope(root):
        path = root / rel
        if path.is_file() and path.suffix == ".md":
            findings.extend(audit_file(path, root))

    if findings:
        print("Trace → D/A/C widget order audit failures:", file=sys.stderr)
        for item in findings:
            print(f"  - {item}", file=sys.stderr)
        print(f"Total: {len(findings)}", file=sys.stderr)
        return 1

    print("Trace → D/A/C widget order audit OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
