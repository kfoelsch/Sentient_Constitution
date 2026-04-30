#!/usr/bin/env python3
"""Audit Chapter One D/E/C widget row order for drift-sensitive sections.

This checker intentionally validates a small set of high-value widgets instead
of trying to infer semantic order everywhere. It protects the functional order
documented in doc_architecture.md and
implementation/CHAPTER_ONE_PRINCIPLE_DEFINITION_MATRIX_2026-04-29.md.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DEC_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">'
    "Definitions · Evaluation · Compliance</span></strong></summary>"
)
ROW_RE = re.compile(r"^\s*-\s+\[(?P<name>[^\]]+)\]\(")


EXPECTED: dict[str, list[str]] = {
    "#### 3.1 Safety (Harm Constraint)": [
        "Safety (Constraint)",
        "Harm",
        "Irreversible Harm",
        "Risk",
        "Materiality",
        "Dependency",
        "Foreseeability",
    ],
    "### 5. Governance Principle: Freedom (Bounded Agency)": [
        "Freedom (Bounded Agency)",
        "Meaningful Agency",
        "Feasibility",
        "Necessity",
        "Proportionality",
        "Harm Minimization (Tradeoff Selection)",
        "Dependency",
    ],
    "#### 5.1 Productive Capacity (Instrumental Good)": [
        "Productive Capacity",
        "Constitutional Efficiency",
        "Wellbeing",
        "Dignity and Equal Moral Standing",
        "Meaningful Agency",
        "Feasibility",
        "Necessity",
        "Proportionality",
        "Avoidable Burden",
        "Proxy Divergence",
        "Ecological Integrity",
        "Environmental Preconditions",
        "Intergenerational Responsibility",
    ],
    "#### 5.2 Distributed Understanding and Stewardship": [
        "Educational Agency",
        "Transparency",
        "Meaningful Agency",
        "Strategic Stewardship Obligation",
        "Contestability",
        "Auditability",
        "Materiality",
        "Dependency",
        "Accessibility",
        "Safety (Constraint)",
        "Truth (Constitutional Constraint)",
        "Necessity",
        "Proportionality",
        "Avoidable Burden",
        "Epistemic Integrity",
    ],
    "##### 5.2.1 Distributed Understanding": [
        "Transparency",
        "Materiality",
        "Dependency",
        "Accessibility",
        "Meaningful Agency",
        "Contestability",
    ],
    "##### 6.4.1 Rights-Collision Decision Test": [
        "Necessity",
        "Proportionality",
        "Feasibility",
        "Materiality",
        "Dependency",
        "Foreseeability",
        "Proxy Divergence",
        "Avoidable Burden",
    ],
    "#### 7.1 Required Evaluation Factors": [
        "Dependency",
        "Materiality",
        "Foreseeability",
        "Risk",
        "Systemic",
        "System Boundaries",
        "System Boundary Integrity",
        "Cascading Failure",
        "Residual Risk / Misalignment",
        "Existential Risk",
        "Incentive Alignment",
    ],
    "##### 7.2.2 Stewardship and Operator Incentive Alignment": [
        "Incentive Alignment",
        "Productive Capacity",
        "Constitutional Efficiency",
        "Avoidable Burden",
        "Proxy Divergence",
        "Auditability",
        "Safety (Constraint)",
        "Truth (Constitutional Constraint)",
        "System Capture",
    ],
    "### 9. Interpretive Role": [
        "Corpus",
        "Authority Stack and Internal Hierarchy",
        "Supremacy and Enforceability",
        "Irreversible Harm",
        "Truth (Constitutional Constraint)",
        "Meaningful Agency",
        "Accountability",
        "System Capture",
        "Incentive Alignment",
        "Governance",
    ],
}


def extract_widget_rows(lines: list[str], heading: str) -> tuple[int, list[str]]:
    try:
        start = next(i for i, line in enumerate(lines) if line.strip() == heading)
    except StopIteration:
        raise ValueError(f"missing heading: {heading}") from None

    dec_idx = None
    for i in range(start + 1, len(lines)):
        stripped = lines[i].strip()
        if i != start + 1 and re.match(r"^#{1,5}\s+", stripped):
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
        # ch5_dec_widget_audit owns row-shape failures. Here we keep the error
        # explicit so non-row labels cannot hide from this drift check either.
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
    path = root / "core_00-01_principles.md"
    lines = path.read_text(encoding="utf-8").splitlines()

    failures: list[str] = []
    for heading, expected in EXPECTED.items():
        try:
            line_no, actual = extract_widget_rows(lines, heading)
        except ValueError as exc:
            failures.append(str(exc))
            continue
        if actual != expected:
            failures.append(
                "\n".join(
                    [
                        f"{path}:{line_no}: D/E/C order drift under {heading}",
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
