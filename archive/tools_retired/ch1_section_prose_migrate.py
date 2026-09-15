#!/usr/bin/env python3
"""Fix stale Chapter One Part B section labels after split/renumber (2026-06)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Order matters: more specific patterns first.
REPLACEMENTS: list[tuple[str, str]] = [
    # Evaluation factors: old §9.1 → new §10.1 (not tradeoff §9.1).
    (
        r"9\.1 Required Evaluation Factors",
        "10.1 Required Evaluation Factors",
    ),
    (
        r"§9\.1 Required Evaluation Factors",
        "§10.1 Required Evaluation Factors",
    ),
    (
        r"Chapter One §9\.1 Required",
        "Chapter One §10.1 Required",
    ),
    (
        r"Chapter One §9\.1\)",
        "Chapter One §10.1)",
    ),
    (
        r"Chapter One §9\.1 tradeoff",
        "Chapter One §9 tradeoff",
    ),
    (
        r"Chapter One §9\.1\.4",
        "Chapter One §9.1.4",
    ),
    (
        r"Chapter One §9\.3\.2",
        "Chapter One §9.3.2",
    ),
    (
        r"Chapter One §9\.4\.1",
        "Chapter One §9.4.1",
    ),
    (
        r"Chapter One §9\.4\.2",
        "Chapter One §9.4.2",
    ),
    # Governance incentive block: old §9.2.x → new §7.x.
    (
        r"9\.2\.2 Stewardship and Operator Incentive Alignment",
        "§7.4 Stewardship and Operator Incentive Alignment",
    ),
    (
        r"9\.2 Incentive Alignment and System Capture",
        "§7 Governance Under Stewardship Discipline",
    ),
    (
        r"§9\.2\.4 Misalignment Correction and Capture Response",
        "§7.6 Misalignment Correction and Capture Response",
    ),
    (
        r"§9\.2\.1\]",
        "§7.3]",
    ),
    (
        r"§9\.2\.1 ",
        "§7.3 ",
    ),
    (
        r"§9\.2\.2 ",
        "§7.4 ",
    ),
    (
        r"§9\.2\.3 ",
        "§7.5 ",
    ),
    (
        r"§9\.2\.4 ",
        "§7.6 ",
    ),
    (
        r"§§9\.2\.1",
        "§§7.3",
    ),
    (
        r"through \[§9\.2\.4",
        "through [§7.6",
    ),
    # Stewardship section: old §7 → new §6.
    (
        r"§7 Stewardship and Distributed Understanding",
        "§6 Stewardship and Distributed Understanding",
    ),
    # Capacity: old §6 productive → new §8.x.
    (
        r"§6\.2 Constitutional Efficiency",
        "§8.2 Constitutional Efficiency",
    ),
    (
        r"§6 Productive Capacity \(Instrumental Good\)",
        "§8.1 Productive Capacity (Instrumental Good)",
    ),
    (
        r"§6\.3 Concentration Threshold",
        "§8.3 Concentration Threshold",
    ),
    (
        r"§6\.4 Pro-Competition",
        "§8.4 Pro-Competition",
    ),
    (
        r"§6\.5 Consolidation",
        "§8.5 Consolidation",
    ),
    (
        r"Chapter One §6\.3\]",
        "Chapter One §8.3]",
    ),
    (
        r"Chapter One §6\.4\]",
        "Chapter One §8.4]",
    ),
    (
        r"Chapter One §6\.5\]",
        "Chapter One §8.5]",
    ),
    (
        r"Chapter One §6\]",
        "Chapter One §8]",
    ),
    # Tradeoff / avoidable burden labels under new §9.
    (
        r"8\.1\.4 Minimization of Avoidable Burden",
        "9.1.4 Minimization of Avoidable Burden",
    ),
    (
        r"8\.1 Core Tradeoff Principles",
        "9.1 Core Tradeoff Principles",
    ),
    (
        r"8\.4\.1 Rights-Collision Decision Test",
        "9.4.1 Rights-Collision Decision Test",
    ),
    (
        r"6\.4\.2 Proxy-Divergence",
        "9.4.2 Proxy-Divergence",
    ),
    (
        r"§6\.4\.2",
        "§9.4.2",
    ),
    # Interaction section label.
    (
        r"8\. Interaction and Conflict Resolution",
        "9. Interaction and Conflict Resolution",
    ),
    # Evaluation factor subsections mislabeled.
    (
        r"§§9\.1\.3–9\.1\.5\]",
        "§§10.1.3–10.1.5]",
    ),
    (
        r"Chapter One §10\.2\.2",
        "Chapter One §7.4",
    ),
    # Fix broken evaluation anchor labels (prose only; href already correct).
    (
        r"\[10\.1 Required Evaluation Factors\]\(#91-required-evaluation-factors\)",
        "[10.1 Required Evaluation Factors](#101-required-evaluation-factors)",
    ),
    (
        r"\[9\.1 Required Evaluation Factors\]\(#91-required-evaluation-factors\)",
        "[10.1 Required Evaluation Factors](#101-required-evaluation-factors)",
    ),
    (
        r"8\.2 Epistemic Disclosure Constraints",
        "9.2 Epistemic Disclosure Constraints",
    ),
    (
        r"8\.4 Rights-Collision Procedure",
        "9.4 Rights-Collision Procedure",
    ),
    (
        r"8\.3 Freedom-Limitation Constraints",
        "9.3 Freedom-Limitation Constraints",
    ),
    (
        r"§7\.2 Distributed Understanding",
        "§6.2 Distributed Understanding",
    ),
    (
        r"#82-epistemic-disclosure-constraints",
        "#92-epistemic-disclosure-constraints",
    ),
    (
        r"11\. Prohibition on Absolute Override",
        "12. Prohibition on Absolute Override",
    ),
    (
        r"12\. Integrated Application",
        "13. Integrated Application",
    ),
    (
        r"§9\.2\]",
        "§7]",
    ),
    (
        r"\[9\.1 Required Evaluation Factors\]\(#101-required-evaluation-factors\)",
        "[10.1 Required Evaluation Factors](#101-required-evaluation-factors)",
    ),
]


def migrate_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    original = text
    for pattern, repl in REPLACEMENTS:
        text = re.sub(pattern, repl, text)
    if text != original:
        path.write_text(text, encoding="utf-8")
        return 1
    return 0


def main() -> int:
    changed = 0
    for path in sorted(ROOT.glob("core_*.md")):
        changed += migrate_file(path)
    print(f"Updated {changed} core file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
