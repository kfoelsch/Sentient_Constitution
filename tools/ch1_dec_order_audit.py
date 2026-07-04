#!/usr/bin/env python3
"""Audit Chapter One D/E/C widget row order for drift-sensitive sections.

This checker intentionally validates a small set of high-value widgets instead
of trying to infer semantic order everywhere. Expected order lives in
tools/architecture/ch1_dec_order.json (rule NAV-DEC-CH1-ORDER).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from architecture.load_config import ch1_dec_order_expected  # noqa: E402

DEC_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">'
    "Definitions · Evaluation · Compliance</span></strong></summary>"
)
ROW_RE = re.compile(r"^\s*-\s+\[(?P<name>[^\]]+)\]\(")
ANNOTATION_ROW_RE = re.compile(r"^\s*-\s+\*[^*]+\*")
PROSE_ANNOTATION_RE = re.compile(r"^\*[^*]+\*")


def extract_widget_rows(lines: list[str], heading: str) -> tuple[int, list[str]]:
    try:
        start = next(i for i, line in enumerate(lines) if line.strip() == heading)
    except StopIteration:
        raise ValueError(f"missing heading: {heading}") from None

    dec_idx = None
    for i in range(start + 1, len(lines)):
        stripped = lines[i].strip()
        if i != start + 1 and re.match(r"^#{1,6}\s+", stripped):
            break
        if stripped == DEC_SUMMARY:
            dec_idx = i
            break
    if dec_idx is None:
        raise ValueError(f"missing D/E/C widget after heading: {heading}")

    rows: list[str] = []
    for i in range(dec_idx + 1, len(lines)):
        stripped = lines[i].strip()
        if stripped == "</details>":
            return dec_idx + 1, rows
        if not stripped:
            continue
        m = ROW_RE.match(lines[i])
        if m:
            rows.append(m.group("name"))
            continue
        if ANNOTATION_ROW_RE.match(lines[i]):
            continue
        if PROSE_ANNOTATION_RE.match(stripped):
            continue
        raise ValueError(
            f"unexpected non-row content in D/E/C widget for {heading} "
            f"at line {i + 1}: {stripped}"
        )

    raise ValueError(f"unterminated D/E/C widget after heading: {heading}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repository root")
    args = parser.parse_args()

    root = Path(args.root)
    failures: list[str] = []
    ch1_files = (
        root / "core_01_a_values_principles.md",
        root / "core_01_b_interaction_interpretation.md",
        root / "core_01_c_stewardship_capacity_principles.md",
    )
    lines: list[str] = []
    for path in ch1_files:
        if not path.exists():
            failures.append(f"missing Chapter One file: {path.name}")
            continue
        lines.extend(path.read_text(encoding="utf-8").splitlines())
    if not lines:
        print("FAIL: Chapter One D/E/C order audit — no Chapter One content found.")
        return 1
    expected_map = ch1_dec_order_expected()

    for heading, expected in expected_map.items():
        try:
            line_no, actual = extract_widget_rows(lines, heading)
        except ValueError as exc:
            failures.append(str(exc))
            continue
        if actual != expected:
            failures.append(
                "\n".join(
                    [
                        f"Chapter One:{line_no}: D/E/C order drift under {heading}",
                        f"  expected: {expected}",
                        f"  actual:   {actual}",
                    ]
                )
            )

    if failures:
        print("FAIL: Chapter One D/E/C order drift detected.")
        for failure in failures:
            print(failure)
        return 1

    print("PASS: Chapter One D/E/C widgets preserve expected functional order.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
