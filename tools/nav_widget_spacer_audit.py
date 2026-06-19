#!/usr/bin/env python3
"""Audit <br> spacer discipline after Trace, D/E/C, reader-guidance, and placement widgets.

Rule: NAV-DEC-12-SPACER in tools/architecture/rule_registry.json.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

TRACE_SUMMARY = '<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>'
DEC_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">Definitions · Evaluation · Compliance</span></strong></summary>'
)
READER_GUIDANCE_RE = re.compile(
    r'<summary><strong><span style="color: #2563eb;">Reader guidance \(non-operative\):'
)
PLACEMENT_RE = re.compile(
    r'<summary><strong><span style="color: #2563eb;">Corpus placement \(non-operative\):'
)
INLINE_DEFINITION_RE = re.compile(
    r'<strong><span style="color: #2563eb;">Definition:</span></strong>'
)
DETAILS_CLOSE = "</details>"

AUDIT_GLOBS = (
    "core_*.md",
    "corpus_joint_structure/*.md",
    "corpus_systems/*_00_registry_and_reading_rules.md",
    "corpus_institutions/*_00_registry_and_reading_rules.md",
    "corpus_forum/*_00_registry_and_reading_rules.md",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    return parser.parse_args()


def widget_kind(opening: str) -> str | None:
    if TRACE_SUMMARY in opening:
        return "trace"
    if DEC_SUMMARY in opening:
        return "dec"
    if READER_GUIDANCE_RE.search(opening):
        return "reader"
    if PLACEMENT_RE.search(opening):
        return "placement"
    return None


def next_nonempty(lines: list[str], start: int) -> tuple[int, str] | None:
    for j in range(start, len(lines)):
        if lines[j].strip():
            return j, lines[j]
    return None


def audit_file(path: Path, root: Path) -> list[str]:
    rel = path.relative_to(root).as_posix()
    if rel.startswith("core_05-05_definitions_"):
        return []

    lines = path.read_text(encoding="utf-8").splitlines()
    findings: list[str] = []

    i = 0
    while i < len(lines):
        line = lines[i]
        if INLINE_DEFINITION_RE.search(line):
            nxt = next_nonempty(lines, i + 1)
            if nxt and nxt[1].strip() == "<br>":
                findings.append(
                    f"{rel}:{nxt[0] + 1}: remove <br> after inline Definition: line (rule 12 spacer)"
                )
        if line.strip() != DETAILS_CLOSE:
            i += 1
            continue

        # Find matching <details> and classify widget.
        depth = 1
        start = i - 1
        opening_chunk = ""
        while start >= 0 and depth > 0:
            opening_chunk = lines[start] + "\n" + opening_chunk
            if lines[start].strip() == DETAILS_CLOSE:
                depth += 1
            if lines[start].strip() == "<details>":
                depth -= 1
            start -= 1
        kind = widget_kind(opening_chunk)

        nxt = next_nonempty(lines, i + 1)
        if nxt is None:
            i += 1
            continue

        nxt_idx, nxt_line = nxt
        nxt_stripped = nxt_line.strip()

        if nxt_stripped == "<details>":
            i += 1
            continue

        if INLINE_DEFINITION_RE.search(nxt_stripped):
            i += 1
            continue

        if nxt_stripped == "<br>":
            i += 1
            continue

        if nxt_stripped.startswith("**Next file:**") or nxt_stripped.startswith(
            "**Previous file:**"
        ):
            i += 1
            continue

        if nxt_stripped == "---":
            i += 1
            continue

        if kind in {"trace", "dec", "reader", "placement"}:
            if nxt_stripped.startswith("<a id="):
                i += 1
                continue
            findings.append(
                f"{rel}:{i + 1}: missing <br> after {kind} widget before operative content "
                f"(next line {nxt_idx + 1}: {nxt_stripped[:60]}...)"
            )
        i += 1

    return findings


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    all_findings: list[str] = []
    for pattern in AUDIT_GLOBS:
        for path in sorted(root.glob(pattern)):
            if path.is_file():
                all_findings.extend(audit_file(path, root))

    if all_findings:
        print("Nav widget spacer audit failures:", file=sys.stderr)
        for item in all_findings:
            print(f"  - {item}", file=sys.stderr)
        print(f"Total: {len(all_findings)}", file=sys.stderr)
        return 1

    print("Nav widget spacer audit OK.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
