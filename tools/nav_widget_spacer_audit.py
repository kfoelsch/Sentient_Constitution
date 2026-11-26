#!/usr/bin/env python3
"""Audit widget stack spacing and Markdown list boundaries in O/M/A/C widgets.

Rules: NAV-DAC-12-SPACER and NAV-DAC-12-MARKDOWN in tools/architecture/rule_registry.json.
One <br> follows the last widget of a stack, none separates stacked widgets, and
O/M/A/C list content is separated from its summary and closing HTML tag by blank lines.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from corpus_paths import binding_corpus_scope  # noqa: E402  (AUDIT-SCOPE-01: the whole corpus)

TRACE_SUMMARY = '<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>'
DEC_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">Definitions (O · M · A · C)</span></strong></summary>'
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
DEC_SUMMARY_LINE = DEC_SUMMARY



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


def definition_widget_markdown_findings(
    lines: list[str], open_idx: int, rel: str
) -> list[str]:
    """Require blank lines around Markdown list content inside an O/M/A/C widget."""
    depth = 0
    close_idx = None
    for idx in range(open_idx, len(lines)):
        stripped = lines[idx].strip()
        if stripped == "<details>":
            depth += 1
        elif stripped == DETAILS_CLOSE:
            depth -= 1
            if depth == 0:
                close_idx = idx
                break
    if close_idx is None:
        return []  # Other audits report unclosed details blocks.

    summary_idx = next(
        (idx for idx in range(open_idx + 1, close_idx) if lines[idx].strip() == DEC_SUMMARY_LINE),
        None,
    )
    if summary_idx is None:
        return []

    findings: list[str] = []
    first_content = next(
        (idx for idx in range(summary_idx + 1, close_idx) if lines[idx].strip()),
        None,
    )
    if first_content is not None and first_content == summary_idx + 1:
        findings.append(
            f"{rel}:{first_content + 1}: add a blank line after the O/M/A/C summary so its Markdown rows render"
        )

    last_content = next(
        (idx for idx in range(close_idx - 1, summary_idx, -1) if lines[idx].strip()),
        None,
    )
    if last_content is not None and last_content == close_idx - 1:
        findings.append(
            f"{rel}:{close_idx + 1}: add a blank line before </details> to close the O/M/A/C Markdown list"
        )
    return findings


def audit_file(path: Path, root: Path) -> list[str]:
    rel = path.relative_to(root).as_posix()
    if rel.startswith("core_05-05_definitions_"):
        return []

    lines = path.read_text(encoding="utf-8").splitlines()
    findings: list[str] = []

    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == "<details>":
            findings.extend(definition_widget_markdown_findings(lines, i, rel))
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
            after_br = next_nonempty(lines, nxt_idx + 1)
            if after_br and after_br[1].strip() == "<details>":
                findings.append(
                    f"{rel}:{nxt_idx + 1}: remove <br> between stacked widgets; put one <br> only after the last widget"
                )
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
    for rel in binding_corpus_scope(root, include_support_docs=True):
        path = root / rel
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
