#!/usr/bin/env python3
"""Audit selected Chapter Five compound heading/member order contracts.

The goal is not to infer every possible semantic grouping. This checker is a
deliberately narrow drift tripwire for headings whose visible term sequence is
intended to mirror the internal reading order or member list.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PART_B = "core_05-05_definitions_b_semi_independent.md"
PART_C = "core_05-05_definitions_c_dependent_clusters.md"


EXPECTED_TOPIC_GROUPS: dict[str, list[str]] = {
    "#### Accountability, Contestability, Adjudication, Resolution Integrity, and Collective Failure": [
        "Accountability",
        "Contestability",
        "Adjudication and Dispute Resolution",
        "Collective Accountability Failure",
        "Capture of Resolution Pathways",
        "Force Majeure",
    ],
    "#### Sentience Status, Animal Life, Derivation, and Development": [
        "Animal Life, Sentient Life, Sentience Status, Derivation, and Development",
        "Animal Life",
        "Contested-Sentient Life",
        "Sentient",
        "Sentience Burden of Proof",
        "Sentience Contestability",
        "Sentience Evaluation",
        "Sentience Indicator Integrity",
        "Sentience Non-Exclusion",
        "Sentience Precaution Tiers",
        "Sentience Precautions",
        "Sentience Status Adjudication",
        "Derived Sentient",
        "Developing Sentient",
        "Meaningful Agency",
    ],
    "#### Agency, Expression, Assembly, Consent, and Coercion": [
        "Expression",
        "Assembly",
        "Collective Organization",
        "Consent",
        "Consent, Sexual",
        "Coercion and Manipulation",
    ],
    "#### Protected Status, Fairness, and Anti-Discrimination": [
        "Protected Characteristics",
        "Protected Characteristic Proxying and Disparate Impact",
        "Protected Intimate-Signal Gating",
        "Protected Commercial Sexual Services Status and Article X-C Circumvention",
    ],
    "#### Family, Care, and Instantiation": [
        "Non-Separation",
        "Family and Care Relationships",
        "Reproductive Autonomy",
    ],
    "#### Creative Work, Compensation, Productive Capacity, and Anti-Displacement": [
        "Creative Work Attribution",
        "Fair Compensation",
        "Productive Capacity",
        "Anti-Displacement Floor",
    ],
    "#### Governance, Oversight, Participation, and Stewardship": [
        "Governance",
        "Oversight",
        "Decentralization",
        "Concentration Threshold",
        "Systemic Lock-In",
        "Burden-Reduction Duty",
        "Review and Correction Duty",
        "Stakeholder",
        "Stakeholder Participation Weight",
        "Binding Stakeholder Choice — Decision-Resolution Requirements",
        "Stakeholder Representation and Participation-Weight Limits (Binding Stakeholder Choice)",
        "Stakeholder Rights-Collision Record (Binding Stakeholder Choice)",
    ],
    "#### Materiality, Impact, Risk, and Classification Integrity": [
        "Material",
        "Material Degradation",
        "Material Impact",
        "Material Risk",
        "Materiality Determination",
        "Materiality Integrity Constraint",
        "Materiality Under Uncertainty",
        "System",
        "System Boundaries",
        "System Boundary Integrity",
    ],
    "#### Environment, Ecological Footprint, Cultural Continuity, and Heritage": [
        "Ecological Footprint",
        "Environmental Preconditions",
        "Indigenous Continuity",
        "Language, Culture, and Heritage",
    ],
    "#### Survival Conditions, Tenure, Bodily Maintenance, and Rest": [
        "Bodily-Maintenance Access",
        "Safe Conditions",
        "Tenure Security",
        "Leisure and Rest",
    ],
    "#### Emergency, Movement, Refuge, and Continuity of Recognition": [
        "Emergency and Contingency",
        "Constitutional Emergency and Contingency",
        "Stakeholder Emergency and Contingency",
        "Emergency Pre-Deliberation Action (Binding Collective Choice)",
        "Movement and Relocation",
        "Refuge from Non-Compliance",
        "Non-Statelessness",
    ],
    "#### Collective Harm and Boundary": [
        "Collective Harm Boundary",
    ],
    "#### Standing Inputs: Contribution, Participant Standing, Cells, Effects, and Violation Findings": [
        "Contribution State",
        "Participant Standing",
        "Standing Cell",
        "Standing Effect",
        "Verified Violation Findings",
        "Violation Nature",
    ],
    "#### Use of Force, Autonomous Coercion, Mass Harm, and Irreversible Sanction": [
        "Use of Force",
        "Autonomous Coercion Tool",
        "Autonomous Lethal System",
        "Combatant / Non-Combatant Distinction",
        "Weapons of Mass Harm",
        "Irreversible Sanction",
    ],
    "#### Corpus, Authority Stack, Supremacy, and Enforceability": [
        "Corpus",
        "Authority Stack and Internal Hierarchy",
        "Supremacy and Enforceability",
    ],
}

TOPIC_GROUP_HEADINGS: set[str] = set(EXPECTED_TOPIC_GROUPS)


EXPECTED_CLUSTERS: dict[str, list[str]] = {
    "#### 3.3 Collective Harm Boundary, Harm, and Harassment and Bullying": [
        "Harm",
        "Psychological Harm",
        "Irreversible Harm",
        "Collective Harm Boundary",
        "Harassment and Bullying",
    ],
    "#### 3.4 Creative Work, Training-Data Use, Attribution, Compensation, and Anti-Displacement": [
        "Creative Work Attribution",
        "Training-Data Use",
        "Fair Compensation",
        "Anti-Displacement Floor",
        "Productive Capacity",
        "Innovation Reward and Anti-Enclosure",
    ],
    "#### 3.5 Forum Families and Dispute Routing": [
        "Forum Family, Sentient",
        "Forum Family, Technical",
        "Forum Family, Institutional",
        "Forum Family, Environment",
        "Forum Family, Integrity",
        "Forum Family, Constitutional",
        "Adjudication and Dispute Resolution",
    ],
    "#### 3.6 Self-Determination, Meaningful Agency, Educational Agency, and Volitional Integrity": [
        "Self-Determination",
        "Meaningful Agency",
        "Educational Agency",
        "Volitional Integrity",
        "Freedom (Bounded Agency)",
    ],
    "#### 3.7 Transparency, Auditability, and Verification": [
        "Transparency",
        "Auditability",
        "Audit Scope Sufficiency",
        "Evaluation Completeness Constraint",
        "Observability",
        "Verifiability",
        "Verification Accessibility",
        "Verification Feasibility",
        "Verification Independence",
        "Verification Proportionality",
        "Verification Robustness",
    ],
    "#### 3.8 Trust and Trustworthiness": [
        "Trust",
        "Trustworthiness",
        "Trust Degradation and Misleading Reliance",
    ],
    "#### 3.9 Truth and Epistemic Integrity": [
        "Truth (Constitutional Constraint)",
        "Epistemic Integrity",
        "Foreseeability Burden",
        "Foreseeability Diligence",
        "Foreseeability Failure",
        "Foreseeability Scaling",
        "Foreseeability Scope",
        "Reasonably Foreseeable",
        "Good Faith",
        "Materiality Determination",
        "Publication and High-Impact Communication",
        "Publication Truthfulness and Recklessness Floor",
        "Protected Data and Internal-State Publication Constraint",
        "Likeness and Documentary Depiction Interface",
        "High-Impact and Systemic Harm Publication Constraint",
        "Security-Sensitive Disclosure Balance",
    ],
    "#### 3.10 Voluntary Agency, Consent, and Anti-Coercion": [
        "Consent",
        "Coercion and Manipulation",
        "Voluntary Discontinuation",
        "Systemic Lock-In",
    ],
}


H4_RE = re.compile(r"^####\s+(.+?)\s*$")
MEMBER_LINK_RE = re.compile(r"^\s*-\s+\[(?P<name>[^\]]+)\]\(")


def collect_topic_group_entries(lines: list[str], heading: str, group_headings: set[str]) -> tuple[int, list[str]]:
    try:
        start = next(i for i, line in enumerate(lines) if line.strip() == heading)
    except StopIteration:
        raise ValueError(f"missing topic-group heading: {heading}") from None

    entries: list[str] = []
    for i in range(start + 1, len(lines)):
        stripped = lines[i].strip()
        if stripped in group_headings:
            break
        m = H4_RE.match(stripped)
        if m:
            entries.append(m.group(1))
    return start + 1, entries


def collect_cluster_members(lines: list[str], heading: str) -> tuple[int, list[str]]:
    try:
        start = next(i for i, line in enumerate(lines) if line.strip() == heading)
    except StopIteration:
        raise ValueError(f"missing cluster heading: {heading}") from None

    member_start = None
    for i in range(start + 1, len(lines)):
        stripped = lines[i].strip()
        if i != start + 1 and stripped.startswith("#### "):
            break
        if stripped == "**Cluster members.** This cluster comprises:":
            member_start = i
            break
    if member_start is None:
        raise ValueError(f"missing Cluster members block under: {heading}")

    members: list[str] = []
    for i in range(member_start + 1, len(lines)):
        stripped = lines[i].strip()
        if not stripped:
            if members:
                break
            continue
        m = MEMBER_LINK_RE.match(stripped)
        if not m:
            if members:
                break
            continue
        members.append(m.group("name"))
    return member_start + 1, members


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repository root")
    args = parser.parse_args()

    root = Path(args.root)
    part_b_lines = (root / PART_B).read_text(encoding="utf-8").splitlines()
    part_c_lines = (root / PART_C).read_text(encoding="utf-8").splitlines()

    failures: list[str] = []
    for heading, expected in EXPECTED_TOPIC_GROUPS.items():
        try:
            line_no, actual = collect_topic_group_entries(part_b_lines, heading, TOPIC_GROUP_HEADINGS)
        except ValueError as exc:
            failures.append(str(exc))
            continue
        if actual != expected:
            failures.append(
                "\n".join(
                    [
                        f"{PART_B}:{line_no}: topic-group order drift under {heading}",
                        f"  expected: {expected}",
                        f"  actual:   {actual}",
                    ]
                )
            )

    for heading, expected in EXPECTED_CLUSTERS.items():
        try:
            line_no, actual = collect_cluster_members(part_c_lines, heading)
        except ValueError as exc:
            failures.append(str(exc))
            continue
        if actual != expected:
            failures.append(
                "\n".join(
                    [
                        f"{PART_C}:{line_no}: cluster member order drift under {heading}",
                        f"  expected: {expected}",
                        f"  actual:   {actual}",
                    ]
                )
            )

    if failures:
        print("FAIL: Chapter Five compound heading/member order drift detected.")
        for failure in failures:
            print(failure)
        return 1

    print("PASS: selected Chapter Five compound headings preserve member order.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
