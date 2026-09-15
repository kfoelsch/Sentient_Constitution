#!/usr/bin/env python3
"""Fix cascade damage from ch1_integration_relocation section-ref pass."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Longest-first explicit repairs
FIXUPS = [
    # Rights-collision / tradeoffs (Part A §5.4)
    ("Chapter One §14.4.2", "Chapter One §5.4.2"),
    ("Chapter One §14.4.1", "Chapter One §5.4.1"),
    ("Chapter One §14.4", "Chapter One §5.4"),
    ("§14.4.2", "§5.4.2"),
    ("§14.4.1", "§5.4.1"),
    # Plain language (Part A §3.4) — restore after blanket §14.4 fix
    ("Chapter One §5.4 — Plain-Language", "Chapter One §3.4 — Plain-Language"),
    ("Chapter One §5.4 plain-language", "Chapter One §3.4 plain-language"),
    ("Chapter One §5.4.", "Chapter One §3.4."),
    # Epistemic disclosure (Part A §5.2)
    ("Chapter One §12.2 (*Epistemic", "Chapter One §5.2 (*Epistemic"),
    ("Chapter One §12.2 Epistemic", "Chapter One §5.2 Epistemic"),
    ("[9.2 Epistemic Disclosure Constraints](#102-", "[5.2 Epistemic Disclosure Constraints](#52-"),
    ("[§5.2 Epistemic Disclosure Constraints](#102-", "[§5.2 Epistemic Disclosure Constraints](#52-"),
    ("#52-epistemic-disclosure-constraints", "#52-epistemic-disclosure-constraints"),
    ("#521-preservation-of-epistemic-integrity", "#521-preservation-of-epistemic-integrity"),
    ("#522-trust-truth-alignment", "#522-trust-truth-alignment"),
    # Evaluation (Part A §11.1)
    ("[§11.1 Required Evaluation Factors](#111-required", "[§11.1 Required Evaluation Factors](#61-required"),
    ("[11.1 Required Evaluation Factors](#111-required", "[6.1 Required Evaluation Factors](#61-required"),
    ("#61-required-evaluation-factors", "#61-required-evaluation-factors"),
    ("#1111-systemic-scope", "#611-systemic-scope"),
    ("#1112-accessibility-under", "#612-accessibility-under"),
    ("#1113-privacy-informational", "#613-privacy-informational"),
    ("#1114-voluntary-discontinuation", "#614-voluntary-discontinuation"),
    ("#1115-assembly-collective", "#615-assembly-collective"),
    ("#112-read-with-governance", "#62-read-with-governance"),
    # Tradeoffs / interaction (Part A §5)
    ("#514-minimization-of-avoidable-burden", "#514-minimization-of-avoidable-burden"),
    ("#541-rights-collision-decision-test", "#541-rights-collision-decision-test"),
    ("#542-proxy-divergence-invalidation", "#542-proxy-divergence-invalidation"),
    ("#5-interaction-and-conflict-resolution", "#5-interaction-and-conflict-resolution"),
    ("[§5 Interaction and Conflict Resolution](#10-interaction", "[§5 Interaction and Conflict Resolution](core_01_a_values_principles.md#5-interaction"),
    ("[10. Interaction and Conflict Resolution](core_01_a_values_principles.md#5-interaction", "[5. Interaction and Conflict Resolution](core_01_a_values_principles.md#5-interaction"),
    ("[10. Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#5-interaction", "[5. Interaction and Conflict Resolution](#5-interaction"),
    ("[10.4.1 Rights-Collision Decision Test](core_01_b_stewardship_capacity_principles.md#1041", "[5.4.1 Rights-Collision Decision Test](#541"),
    ("[10.4.1 Rights-Collision Decision Test](core_01_b_stewardship_capacity_principles.md#541", "[5.4.1 Rights-Collision Decision Test](#541"),
    ("[§5.4.1 Rights-Collision Decision Test](core_01_b_stewardship_capacity_principles.md#1041", "[§5.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541"),
    ("[§5.4.1 Rights-Collision Decision Test](core_01_b_stewardship_capacity_principles.md#541", "[§5.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541"),
    ("[§5 Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#1041", "[§5.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541"),
    ("core_01_b_stewardship_capacity_principles.md#54-rights-collision-procedure", "core_01_a_values_principles.md#54-rights-collision-procedure"),
    ("core_01_a_values_principles.md#541-", "core_01_a_values_principles.md#541-"),
    ("core_01_a_values_principles.md#514-", "core_01_a_values_principles.md#514-"),
    ("core_01_a_values_principles.md#61-", "core_01_a_values_principles.md#61-"),
    ("core_01_a_values_principles.md#52-", "core_01_a_values_principles.md#52-"),
    ("core_01_a_values_principles.md#5-interaction", "core_01_a_values_principles.md#5-interaction"),
    # Part B ops section refs
    ("#11-stewardship-and-distributed-understanding", "#11-stewardship-and-distributed-understanding"),
    ("#12-governance-under-stewardship-discipline", "#12-governance-under-stewardship-discipline"),
    ("#123-stewardship-and-operator-incentive-alignment", "#123-stewardship-and-operator-incentive-alignment"),
    ("[§11 Stewardship and Distributed Understanding](core_01_b_stewardship_capacity_principles.md#11-stewardship", "[§11 Stewardship and Distributed Understanding](core_01_b_stewardship_capacity_principles.md#11-stewardship"),
    ("[§12 Governance Under Stewardship Discipline](core_01_b_stewardship_capacity_principles.md#12-governance", "[§12 Governance Under Stewardship Discipline](core_01_b_stewardship_capacity_principles.md#12-governance"),
    ("[§12.2 Stewardship and Operator Incentive Alignment](core_01_b_stewardship_capacity_principles.md#124-", "[§12.2 Stewardship and Operator Incentive Alignment](core_01_b_stewardship_capacity_principles.md#124-"),
    ("[§13 Shared-System Capacity](core_01_b_stewardship_capacity_principles.md#8-shared", "[§13 Shared-System Capacity](core_01_b_stewardship_capacity_principles.md#13-shared"),
    ("[§11 Stewardship and Distributed Understanding](#6-stewardship", "[§11 Stewardship and Distributed Understanding](#11-stewardship"),
    ("[§12 Governance Under Stewardship Discipline](#7-governance", "[§12 Governance Under Stewardship Discipline](#12-governance"),
    ("[§11.1 Required Evaluation Factors](core_01_b_stewardship_capacity_principles.md#111-", "[§11.1 Required Evaluation Factors](core_01_a_values_principles.md#61-"),
    ("[11.1 Required Evaluation Factors](core_01_b_stewardship_capacity_principles.md#111-", "[6.1 Required Evaluation Factors](core_01_a_values_principles.md#61-"),
    ("[10.1.4 Minimization of Avoidable Burden](#1014", "[5.1.4 Minimization of Avoidable Burden](#514"),
    ("[10.1.4 Minimization of Avoidable Burden](core_01_b_stewardship_capacity_principles.md#1014", "[5.1.4 Minimization of Avoidable Burden](core_01_a_values_principles.md#514"),
    ("[§9.1.4 Minimization of Avoidable Burden](#1014", "[§9.1.4 Minimization of Avoidable Burden](#514"),
    ("[§9.1.4 Minimization of Avoidable Burden](core_01_b_stewardship_capacity_principles.md#1014", "[§9.1.4 Minimization of Avoidable Burden](core_01_a_values_principles.md#514"),
    ("[§5.4.2 Proxy-Divergence Invalidation](#1042", "[§5.4.2 Proxy-Divergence Invalidation](#542"),
    ("[§5.4.2 Proxy-Divergence Invalidation](core_01_b_stewardship_capacity_principles.md#1042", "[§5.4.2 Proxy-Divergence Invalidation](core_01_a_values_principles.md#542"),
    ("[§5.4.1 Rights-Collision Decision Test](#1041", "[§5.4.1 Rights-Collision Decision Test](#541"),
    ("[§5 Interaction and Conflict Resolution](#10-interaction", "[§5 Interaction and Conflict Resolution](#5-interaction"),
    ("[§5.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541-rights-collision-decision-test)"),
    ("[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[10.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)", "[5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    # Part A wellbeing trace stale headings
    ("[3. Foundational Objective: Wellbeing](#3-foundational", "[2. Foundational Objective: Wellbeing](#2-foundational"),
    ("[3.2 Recognition", "[2.2 Recognition"),
    ("[§9.2 Recognition", "[§9.2 Recognition"),
    ("[4.1 Safety](#41-", "[3.1 Safety](#31-"),
    ("[4.2 Truth](#42-", "[3.2 Truth](#32-"),
    ("[4.3 Science", "[3.3 Science"),
    ("[5. Trust](#5-system", "[4. Trust](#4-system"),
    ("[§9.1](#51-resilience", "[§9.1](#41-resilience"),
    ("[§11](#3-foundational", "[§3](#2-foundational"),
    ("[§4](#5-system", "[§2](#4-system"),
    # README / Ch5 cluster renumber damage
    ("§9 dependent clusters **§14.2–§14.16**", "§3 dependent clusters **§9.2–§9.16**"),
    ("§9.0 meta rules", "dependent-cluster meta rules"),
    ("§1/§9/§9 **§14.2–§14.3**", "§9.2–§3.3"),
    ("§1/§9/§9 **§9.5–§9.7**", "§3.5–§3.7"),
    ("§1/§9/§9 **§9.8–§14.11**", "§3.8–§9.11"),
    ("§§11–13", "§§11–14"),
    ("§§1–5", "§§1–10"),
    ("Part A (Values Principles, §§1–5)", "Part A (Values Principles, §§1–10)"),
    ("Part B (Stewardship and Governance, §§11–13)", "Part B (Stewardship and Governance, §§11–14)"),
    # Ch14 amendment internal anchors (not Chapter One)
    ("[§12.1](#111-notice", "[§12.1](#121-notice"),
    ("[§12.2](#112-recorded", "[§12.2](#122-recorded"),
    ("#111-notice-and-contest", "#121-notice-and-contest"),
    ("#112-recorded-effectiveness", "#122-recorded-effectiveness"),
    ("[§11.1](#101-deliberate", "[§11.1](#111-deliberate"),
    ("[§11.2](#102-instrument", "[§11.2](#112-instrument"),
    ("[§11.3](#103-joining", "[§11.3](#113-joining"),
    ("#101-deliberate-adoption", "#111-deliberate-adoption"),
    ("#102-instrument-of-adoption", "#112-instrument-of-adoption"),
    ("#103-joining-by-additional-parties", "#113-joining-by-additional-parties"),
    ("[§13](#5-test-3", "[§13](#9-test-3"),
    ("#5-test-3-authority", "#9-test-3-authority"),
    # §14.1 definitional layer in Part A
    ("**[§5 Interaction and Conflict Resolution](core_01_a_values_principles.md#541-rights-collision-decision-test)**", "**[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)**"),
    ("**[§5 Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#541-rights-collision-decision-test)**", "**[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)**"),
    ("[§5 Interaction and Conflict Resolution](core_01_a_values_principles.md#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5 Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[10.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)", "[5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5.4.1 Rights-Collision Decision Test](core_01_b_stewardship_capacity_principles.md#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5 Interaction and Conflict Resolution](core_01_a_values_principles.md#5-interaction-and-conflict-resolution)", "[§5 Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)"),
    ("[10. Interaction and Conflict Resolution](core_01_a_values_principles.md#5-interaction-and-conflict-resolution)", "[5. Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)"),
    ("[§5 Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#5-interaction-and-conflict-resolution)", "[§5 Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)"),
    ("[10. Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#5-interaction-and-conflict-resolution)", "[5. Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)"),
    ("[§5.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#1041", "[§5.4.1 Rights-Collision Decision Test](#541"),
    ("[10.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#1041", "[5.4.1 Rights-Collision Decision Test](#541"),
    ("[§5.4.1 Rights-Collision Decision Test](#1041", "[§5.4.1 Rights-Collision Decision Test](#541"),
    ("[10.4.1 Rights-Collision Decision Test](#1041", "[5.4.1 Rights-Collision Decision Test](#541"),
    ("[§5.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541", "[§5.4.1 Rights-Collision Decision Test](#541"),
    ("[10. Integrated Application](#10-integrated-application)", "[10. Integrated Application](#10-integrated-application)"),
    ("[13. Prohibition on Absolute Override](core_01_a_values_principles.md#8-prohibition", "[8. Prohibition on Absolute Override](#8-prohibition"),
    ("[13. Prohibition on Absolute Override](core_01_b_stewardship_capacity_principles.md#8-prohibition", "[8. Prohibition on Absolute Override](#8-prohibition"),
    ("[7.2.1 Preservation of Epistemic Integrity](core_01_b_stewardship_capacity_principles.md#1021", "[5.2.1 Preservation of Epistemic Integrity](#521"),
    ("[7.2.2 Trust-Truth Alignment](core_01_b_stewardship_capacity_principles.md#1022", "[5.2.2 Trust-Truth Alignment](#522"),
    ("[§13.2](core_01_b_stewardship_capacity_principles.md#12-governance", "[§12 Governance Under Stewardship Discipline](core_01_b_stewardship_capacity_principles.md#12-governance"),
    ("[3. Foundational Objective: Wellbeing](#3-foundational", "[2. Foundational Objective: Wellbeing](#2-foundational"),
    ("[§9.2 Recognition, Reinforcement, and Aspiration](#32-", "[§9.2 Recognition, Reinforcement, and Aspiration](#22-"),
    ("[4.1 Safety](#41-", "[3.1 Safety](#31-"),
    ("[4.2 Truth](#42-", "[3.2 Truth](#32-"),
    ("[5. Trust](#5-system", "[4. Trust](#4-system"),
    ("[§5](core_01_b_stewardship_capacity_principles.md#13-shared-system-capacity)", "[§13 Shared-System Capacity](core_01_b_stewardship_capacity_principles.md#13-shared-system-capacity)"),
    ("[§15](core_01_b_stewardship_capacity_principles.md#7-freedom", "[§7 Freedom](#7-freedom"),
    ("[§5 Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#5-interaction-and-conflict-resolution)", "[§5 Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)"),
    ("[10. Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#5-interaction-and-conflict-resolution)", "[5. Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)"),
    ("[§7 Freedom](core_01_b_stewardship_capacity_principles.md#7-freedom-bounded-agency)", "[§7 Freedom](#7-freedom-bounded-agency)"),
    ("[§7 Freedom](core_01_a_values_principles.md#7-freedom", "[§7 Freedom](#7-freedom-bounded-agency)"),
    ("[§5.4.1 Rights-Collision Decision Test](core_01_b_stewardship_capacity_principles.md#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[10.4.1 Rights-Collision Decision Test](core_01_b_stewardship_capacity_principles.md#541-rights-collision-decision-test)", "[5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[10.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541-rights-collision-decision-test)", "[5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5 Interaction and Conflict Resolution](core_01_a_values_principles.md#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5 Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[10.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541-rights-collision-decision-test)", "[5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[10.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541-rights-collision-decision-test)", "[5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[10.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)", "[5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5 Interaction and Conflict Resolution](core_01_a_values_principles.md#5-interaction-and-conflict-resolution)", "[§5 Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)"),
    ("[10. Interaction and Conflict Resolution](core_01_a_values_principles.md#5-interaction-and-conflict-resolution)", "[5. Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)"),
    ("[§5 Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#5-interaction-and-conflict-resolution)", "[§5 Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)"),
    ("[10. Interaction and Conflict Resolution](core_01_b_stewardship_capacity_principles.md#5-interaction-and-conflict-resolution)", "[5. Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)"),
    ("[§5 Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)", "[§5 Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)"),
    ("[10. Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)", "[5. Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)"),
    ("[§5 Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)", "[§5 Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)"),
    ("[10. Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)", "[5. Interaction and Conflict Resolution](#5-interaction-and-conflict-resolution)"),
    ("[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[10.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)", "[5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[10.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)", "[5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[10.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541-rights-collision-decision-test)", "[5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5.4.1 Rights-Collision Decision Test](core_01_b_stewardship_capacity_principles.md#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[10.4.1 Rights-Collision Decision Test](core_01_b_stewardship_capacity_principles.md#541-rights-collision-decision-test)", "[5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[10.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541-rights-collision-decision-test)", "[5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[10.4.1 Rights-Collision Decision Test](core_01_a_values_principles.md#541-rights-collision-decision-test)", "[5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[10.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)", "[5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)", "[§5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
    ("[10.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)", "[5.4.1 Rights-Collision Decision Test](#541-rights-collision-decision-test)"),
]

# Deduplicate longest-first
_seen: set[str] = set()
ORDERED = []
for old, new in sorted(FIXUPS, key=lambda x: len(x[0]), reverse=True):
    if old not in _seen and old != new:
        _seen.add(old)
        ORDERED.append((old, new))


def main() -> int:
    skip = {".git", "archive", "evidence", "node_modules", "__pycache__", ".cursor"}
    exts = {".md", ".json", ".py"}
    for path in ROOT.rglob("*"):
        if any(p in skip for p in path.parts):
            continue
        if path.suffix not in exts:
            continue
        if path.name in ("ch1_integration_relocation.py", "ch1_integration_fixup.py"):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        orig = text
        for old, new in ORDERED:
            text = text.replace(old, new)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print(f"Fixed {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
