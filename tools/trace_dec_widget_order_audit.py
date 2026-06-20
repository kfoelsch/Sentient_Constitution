#!/usr/bin/env python3
"""Audit Trace → D/E/C widget placement under owning headings.

Rule: NAV-DEC-12-ORDER in tools/architecture/rule_registry.json.

When a ``####`` or ``#####`` unit (or a ``###`` unit whose Trace block carries
Chapter Five ``· [O]`` read-with links) opens with a Trace ``<details>`` widget,
the next substantive block after ``</details>`` must be either:

1. a **Definitions · Evaluation · Compliance** ``<details>`` widget, or
2. a single-concept inline ``<strong>…Definition:</strong>`` line.

Only blank lines may appear between Trace close and that definition carrier.
``<br>``, *In plain terms*, anchor tags, or operative prose must not intervene.

Sections whose Trace blocks carry no Chapter Five ``· [O]`` read-with links are
exempt from the requirement (structural / routing-only traces).
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
    "Definitions · Evaluation · Compliance</span></strong></summary>"
)
INLINE_DEFINITION_RE = re.compile(
    r"<strong><span style=\"color: #2563eb;\">Definition:</span></strong>"
)
OEC_READ_WITH_RE = re.compile(r"· \[O\]\(")
HEADING_RE = re.compile(r"^(#{1,6})\s+")
PLAIN_TERMS_RE = re.compile(r"^\*In plain terms:")


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
                f"followed immediately by a D/E/C widget or inline Definition "
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
        print("Trace → D/E/C widget order audit failures:", file=sys.stderr)
        for item in findings:
            print(f"  - {item}", file=sys.stderr)
        print(f"Total: {len(findings)}", file=sys.stderr)
        return 1

    print("Trace → D/E/C widget order audit OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
