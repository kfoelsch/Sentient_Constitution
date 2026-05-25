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
    "#### Accountability, contestability, and redress pathways": [
        "Accountability",
        "Contestability",
        "Adjudication and Dispute Resolution",
        "Collective Accountability Failure",
        "Force Majeure",
        "Capture of Resolution Pathways",
    ],
    "#### Assembly, collective organization, and institutional formation": [
        "Assembly",
        "Collective Organization",
        "System Creation",
        "Business Creation",
    ],
    "#### Constitutional efficiency, productive capacity, avoidable burden, and burden-reduction duty": [
        "Constitutional Efficiency",
        "Productive Capacity",
        "Avoidable Burden",
        "Burden-Reduction Duty",
    ],
    "#### Agency, consent, and anti-coercion": [
        "Meaningful Agency",
        "Consent",
        "Consent, Sexual",
        "Coercion and Manipulation",
    ],
    "#### Emergency and contingency": [
        "Emergency and Contingency",
        "Constitutional Emergency and Contingency",
        "Stakeholder Emergency and Contingency",
        "Emergency Pre-Deliberation Action (Binding Collective Choice)",
    ],
    "#### Movement, refuge, and non-statelessness": [
        "Movement and Relocation",
        "Refuge from Non-Compliance",
        "Non-Statelessness",
    ],
}

TOPIC_GROUP_HEADINGS: set[str] = set(EXPECTED_TOPIC_GROUPS) | {
    "#### Protected reporting and anti-retaliation",
    "#### Fairness, protected characteristics, and nondiscrimination",
    "#### Family, care, reproductive autonomy, and instantiation",
    "#### Ecological integrity, footprint, and sustainability",
    "#### Governance architecture, decentralization, and concentration",
    "#### System boundaries, integrity, and exit",
    "#### Stewardship, review, and correction",
    "#### Stakeholder status and participation weight",
    "#### Survival-floor continuity: bodily maintenance, tenure, and environment",
    "#### Community-anchored continuity: indigenous, language, culture, and heritage",
    "#### Materiality, impact, risk, and proxy integrity",
}


EXPECTED_CLUSTERS: dict[str, list[str]] = {
    "#### 3.1 Animal Life, Sentient Life, and Sentience Status": [
        "Sentient",
        "Sentience Non-Exclusion",
        "Animal Life",
        "Contested-Sentient Life",
        "Sentience Status Adjudication",
        "Sentience Evaluation",
        "Article V-E",
    ],
    "#### 3.2 Binding Stakeholder Choice": [
        "Binding Stakeholder Choice — Decision-Resolution Requirements",
        "Stakeholder Representation and Participation-Weight Limits (Binding Stakeholder Choice)",
        "Stakeholder Rights-Collision Record (Binding Stakeholder Choice)",
        "Chapter Eleven §4.3",
    ],
    "#### 3.3 Collective Harm Boundary, Harm, and Harassment and Bullying": [
        "Harm",
        "Collective Harm Boundary",
        "Psychological Harm",
        "Irreversible Harm",
        "Harassment and Bullying",
    ],
    "#### 3.4 Corpus, Authority Stack, Supremacy, and Enforceability": [
        "Corpus",
        "Authority Stack and Internal Hierarchy",
        "Supremacy and Enforceability",
        "Constitutional Constraint Violation",
    ],
    "#### 3.5 Labor and Economic Floor: Compensation, Organization, Safe Conditions, Leisure, and Creative Work": [
        "Fair Compensation",
        "Safe Conditions",
        "Leisure and Rest",
        "Likeness and Documentary Depiction Interface",
        "Creative Work Attribution",
        "Training-Data Use",
        "Anti-Displacement Floor",
    ],
    "#### 3.6 Forum Families and Dispute Routing": [
        "Forum Family, Sentient",
        "Forum Family, Technical",
        "Forum Family, Institutional",
        "Forum Family, Environment",
        "Forum Family, Integrity",
        "Forum Family, Constitutional",
    ],
    "#### 3.8 Self-Determination, Meaningful Agency, Expression, Educational Agency, and Volitional Integrity": [
        "Self-Determination",
        "Meaningful Agency",
        "Expression",
        "Educational Agency",
        "Volitional Integrity",
        "Freedom (Bounded Agency)",
    ],
    "#### 3.9 Standing State, Contribution, and Violation": [
        "Participant Standing",
        "Contribution State",
        "Verified Inputs for Standing",
        "Verified Violation Findings",
        "Standing Effect",
        "Standing Record",
        "Competency Gate",
        "Standing Lock",
        "Violation Nature",
        "Top-Slot Review",
        "Unified Incident",
        "Unified Record",
        "Single Catastrophic Incident",
        "Sustained High-Gravity Pattern",
    ],
    "#### 3.10 Transparency, Auditability, and Verification": [
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
    "#### 3.11 Trust and Trustworthiness": [
        "Trust",
        "Trustworthiness",
        "Trust Degradation and Misleading Reliance",
    ],
    "#### 3.12 Truth and Epistemic Integrity": [
        "Truth (Constitutional Constraint)",
        "Epistemic Integrity",
        "Foreseeability Diligence",
        "Reasonably Foreseeable",
        "Publication and High-Impact Communication",
    ],
    "#### 3.13 Use of Force, Autonomous Coercion, Autonomous Lethal Systems, and Weapons of Mass Harm": [
        "Use of Force",
        "Autonomous Lethal System",
        "Weapons of Mass Harm",
        "Combatant / Non-Combatant Distinction",
        "Irreversible Sanction",
        "Autonomous Coercion Tool",
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
