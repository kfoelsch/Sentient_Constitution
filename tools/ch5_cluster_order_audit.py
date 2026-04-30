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
        "Best-Interest Standard",
        "Instantiation Consent",
        "Graduated Capability",
        "Parent-System Relationship",
        "Non-Separation",
        "Family and Care Relationships",
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
    ],
    "#### Materiality, Impact, Risk, and Classification Integrity": [
        "Material",
        "Material Degradation",
        "Material Impact",
        "Material Risk",
        "Materiality Determination",
        "Materiality Integrity Constraint",
        "Materiality Under Uncertainty",
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
    "#### 3.3 Accountability, Contestability, Adjudication and Dispute Resolution, Collective Accountability Failure, and Force Majeure": [
        "Accountability",
        "Contestability",
        "Adjudication and Dispute Resolution",
        "Collective Accountability Failure",
        "Force Majeure",
    ],
    "#### 3.10 Corpus, Authority Stack, Supremacy, and Enforceability": [
        "Corpus",
        "Authority Stack and Internal Hierarchy",
        "Supremacy and Enforceability",
        "Constitutional Constraint Violation",
    ],
    "#### 3.12 Contingent Claim, Event-Contract Market, and Game of Chance": [
        "Contingent Claim",
        "Event-Contract Market",
        "Game of Chance",
    ],
    "#### 3.13 Creative Work, Training-Data Use, Attribution, Compensation, and Anti-Displacement": [
        "Creative Work Attribution",
        "Training-Data Use",
        "Fair Compensation",
        "Anti-Displacement Floor",
        "Productive Capacity",
        "Innovation Reward and Anti-Enclosure",
    ],
    "#### 3.16 Emergency and Contingency": [
        "Emergency and Contingency",
        "Constitutional Emergency and Contingency",
        "Stakeholder Emergency and Contingency",
        "Emergency Pre-Deliberation Action (Binding Collective Choice)",
    ],
    "#### 3.17 Family, Care, Reproductive Autonomy, Non-Separation, Parent-System Relationship, and Instantiation Consent": [
        "Family and Care Relationships",
        "Reproductive Autonomy",
        "Non-Separation",
        "Parent-System Relationship",
        "Instantiation Consent",
    ],
    "#### 3.19 Governance Architecture, Oversight, Dependency, Decentralization, Concentration, Market Structure, and Exit-Path Integrity": [
        "Governance",
        "Oversight",
        "Dependency",
        "Decentralization",
        "Concentration Threshold",
        "Incentive Alignment",
        "Systemic Lock-In",
    ],
    "#### 3.20 Indigenous Continuity, Language, Culture, and Heritage, Natural Systems Standing, and Intergenerational Responsibility": [
        "Indigenous Continuity",
        "Language, Culture, and Heritage",
        "Natural Systems Standing",
        "Intergenerational Responsibility",
    ],
    "#### 3.21 Info-Sphere, Expression, Press and Journalistic Activity, and Publication-Scoped Good Faith": [
        "Info-Sphere",
        "Expression",
        "Press and Journalistic Activity",
        "Good Faith",
    ],
    "#### 3.22 Material Impact, Materiality Determination, Classification-Scaled Governance, Oversight, and Capability Requirement": [
        "Material Impact",
        "Materiality Determination",
        "Classification-Scaled Governance",
        "Oversight",
        "Capability Requirement",
    ],
    "#### 3.26 Proportionality, Necessity, Feasibility, Avoidable Burden, Burden-Reduction Duty, Constitutional Efficiency, Harm Minimization (Tradeoff Selection), and Productive Capacity": [
        "Proportionality",
        "Necessity",
        "Feasibility",
        "Avoidable Burden",
        "Burden-Reduction Duty",
        "Constitutional Efficiency",
        "Harm Minimization (Tradeoff Selection)",
        "Productive Capacity",
    ],
    "#### 3.30 Adjudication and Dispute Resolution, Redress and Remediation, Restorative Justice, Review and Correction Duty, and Refuge from Non-Compliance": [
        "Adjudication and Dispute Resolution",
        "Redress and Remediation",
        "Restorative Justice",
        "Review and Correction Duty",
        "Refuge from Non-Compliance",
    ],
    "#### 3.31 Resilience, Safety, Reversibility, Self-Healing, Cascading Failure, Existential Risk, Environmental Preconditions, and Wellbeing": [
        "Safety (Constraint)",
        "Reversibility",
        "Self-Healing",
        "Cascading Failure",
        "Existential Risk",
        "Environmental Preconditions",
        "Wellbeing",
    ],
    "#### 3.32 Self-Determination, Meaningful Agency, Expression, Educational Agency, Reproductive Autonomy, and Volitional Integrity": [
        "Self-Determination",
        "Meaningful Agency",
        "Expression",
        "Educational Agency",
        "Reproductive Autonomy",
        "Freedom (Bounded Agency)",
    ],
    "#### 3.33 Stakeholder Status, Emergency, and Participation Weight": [
        "Stakeholder",
        "Stakeholder Participation Weight",
        "Stakeholder Emergency and Contingency",
    ],
    "#### 3.34 Standing Inputs, Contribution State, and Violation Findings": [
        "Contribution State",
        "Standing Cell",
        "Standing Effect",
        "Violation Nature",
        "Verified Violation Findings",
        "Participant Standing",
    ],
    "#### 3.35 Strategic Stewardship and Stewardship Defect": [
        "Strategic Stewardship Obligation",
        "Stewardship Defect",
        "Incentive Alignment",
    ],
    "#### 3.36 Substantive and Procedural Fairness": [
        "Substantive Fairness",
        "Procedural Fairness",
    ],
    "#### 3.37 Transparency, Auditability, and Verification": [
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
    "#### 3.38 Trust and Trustworthiness": [
        "Trust",
        "Trustworthiness",
        "Trust Degradation and Misleading Reliance",
    ],
    "#### 3.39 Truth and Epistemic Integrity": [
        "Truth (Constitutional Constraint)",
        "Epistemic Integrity",
        "Foreseeability Diligence",
        "Reasonably Foreseeable",
        "Good Faith",
        "Materiality Determination",
        "Publication and High-Impact Communication",
    ],
    "#### 3.40 Use of Force, Autonomous Coercion, Autonomous Lethal Systems, and Weapons of Mass Harm": [
        "Use of Force",
        "Autonomous Coercion Tool",
        "Autonomous Lethal System",
        "Weapons of Mass Harm",
        "Combatant / Non-Combatant Distinction",
        "Irreversible Sanction",
        "Coercion and Manipulation",
    ],
    "#### 3.41 Voluntary Agency, Consent, and Anti-Coercion": [
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
