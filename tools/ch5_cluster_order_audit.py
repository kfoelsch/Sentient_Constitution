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


from ch5_paths import CH5_BANDS, CH5_INDEX


EXPECTED_TOPIC_GROUPS: dict[str, list[str]] = {
    "#### Accountability, Contestability, and Redress Pathways": [
        # Accountability and Timeliness leg heads live in core_05.005_apex_accountability_leg.md
        "Attributable Action",
        "Attribution Integrity",
        "Record Integrity",
        "Contestability",
        "Adjudication and Dispute Resolution",
        "Due Process",
        "Timely Resolution",
        "Merits Determination",
        "Stay",
        "Under Challenge",
        "Interim Hold",
        "Formation Check",
        "Negligence",
        "Collective Accountability Failure",
        "Redress and Remediation",
        "Remediation Readiness",
        "Remedy System",
        "Restorative Justice",
        "Force Majeure",
    ],
    "#### Assembly, Collective Organization, and Institutional Formation": [
        "Assembly",
        "Collective Organization",
        "System Creation",
        "Business Creation",
        "Commercial Compliance",
    ],
    "#### Constitutional Efficiency, Productive Capacity, Avoidable Burden, and Burden-Reduction Duty": [
        "Shared-System Capacity",
        "Constitutional Efficiency",
        "Productive Capacity",
        "Avoidable Burden",
        "Burden-Reduction Duty",
    ],
    "#### Agency, Consent, and Anti-Coercion": [
        "Meaningful Agency",
        "Consent",
        "Consent, Sexual",
        "Coercion and Manipulation",
    ],
    "#### Emergency and Contingency Cluster": [
        "Emergency and Contingency",
        "Constitutional Emergency and Contingency",
        "Stakeholder Emergency and Contingency",
        "Emergency Pre-Deliberation Action (Binding Collective Choice)",
    ],
    "#### Movement, Refuge, and Non-Statelessness": [
        "Movement and Relocation",
        "Refuge from Non-Compliance",
        "Non-Statelessness",
    ],
    "#### Governance Architecture, Decentralization, and Concentration": [
        "Governance",
        "Material Control Line",
        "Interested Party",
        "Independence",
        "Initiating Seat",
        "Verify-or-Authorize Seat",
        "Record-Opening Authority",
        "Record Seat",
        "Record Custodian",
        "Contest Seat",
        "Materially Binding Act",
        "Materially Binding Act Record",
        "Decentralization",
        "Standardization",
        "Market Structure",
        "Market Concentration Threshold",
    ],
    "#### Systemic Effects and Capture": [
        "Systemic",
        "Systemic Materiality",
        "System Capture",
        "Anti-Capture",
    ],
}

TOPIC_GROUP_HEADINGS: set[str] = set(EXPECTED_TOPIC_GROUPS) | {
    "#### Protected Reporting and Anti-Retaliation",
    "#### Fairness, Protected Characteristics, and Nondiscrimination",
    "#### Family, Care, Reproductive Autonomy, and Instantiation",
    "#### Ecological Integrity, Footprint, and Sustainability",
    "#### System Boundaries, Integrity, and Exit",
    "#### Stakeholder Status and Weight",
    "#### Survival-floor continuity: bodily maintenance, tenure, and environment",
    "#### Community-Anchored Continuity: Indigenous, Language, Culture, and Heritage",
    "#### Materiality, Impact, Risk, and Proxy Integrity",
    "#### Dependency and Cross-System Support",
}


EXPECTED_CLUSTERS: dict[str, list[str]] = {
    "#### Def.P1 Animal Life, Sentient Life, and Sentience Status": [
        "Substrate Class",
        "Sentience Non-Exclusion",
        "Animal Life",
        "Elevated Communicative Life",
        "Contested-Sentient Life",
        "Sentience Status Adjudication",
        "Sentience-Status Adjudication Record",
        "Sentient",
        "Sentience Evaluation",
        "Article VI-B",
    ],
    "#### Def.P2 Binding Stakeholder Choice": [
        "Binding Stakeholder Choice — Decision-Resolution Requirements",
        "Stakeholder Representation and Weight Limits (Binding Stakeholder Choice)",
        "Stakeholder Rights-Collision Record (Binding Stakeholder Choice)",
        "Chapter Sixteen §4.3 Decision-Resolution Requirements for Binding Stakeholder Choice",
    ],
    "#### Def.A1 Collective Harm Boundary, Harm, and Harassment and Bullying": [
        "Harm",
        "Psychological Harm",
        "Irreversible Harm",
        "Cruelty",
        "Animal Cruelty",
        "Harassment and Bullying",
        "Collective Harm Boundary",
    ],
    "#### Def.I1 Corpus and Authority Stack": [
        "Corpus",
        "Authority Stack and Internal Hierarchy",
    ],
    "#### Def.C1 Labor and Economic Floor: Compensation, Organization, Safe Conditions, Leisure, and Creative Work": [
        "Fair Compensation",
        "Safe Conditions",
        "Leisure and Rest",
        "Likeness and Documentary Depiction Interface",
        "Creative Work Attribution",
        "Training-Data Use",
        "Anti-Displacement Floor",
    ],
    "#### Def.A2 Forum Families and Dispute Routing": [
        "Forum Family, Sentient",
        "Forum Family, Technical",
        "Forum Family, Institutional",
        "Forum Family, Environment",
        "Forum Family, Integrity",
        "Forum Family, Constitutional",
        "Jurisdiction",
        "Primary-Stakes Routing",
        "Forum Case Record",
    ],
    "#### Def.P3 Self-Determination, Meaningful Agency, Expression, Educational Agency, and Volitional Integrity": [
        "Self-Determination",
        "Meaningful Agency",
        "Expression",
        "Hard Content",
        "Educational Agency",
        "Volitional Integrity",
        "Freedom (Bounded Agency)",
    ],
    "#### Def.P4 Developing Sentient, Best-Interest Standard, and Graduated Capability": [
        "Developing Sentient",
        "Best-Interest Standard",
        "Graduated Capability",
        "Article VIII-D",
    ],
    "#### Def.A3 Standing State, Contribution, and Violation": [
        "Participant Standing",
        "Verified Inputs for Standing",
        "Contribution Nature",
        "Violation Nature",
        "Standing Effect",
        "Standing Record",
        "Gated Pathway",
        "Influence Pathway",
        "Competency Bar",
        "Competency Clearance",
        "Standing Lock",
        "Anti-Constitutional Misconduct Review",
        "Unified Incident",
        "Unified Incident Record",
        "Single Catastrophic Incident",
        "Sustained High-Gravity Pattern",
    ],
    "#### Def.C2 Stewardship, Governance Discipline, and Shared-System Capacity": [
        "Stewardship",
        "Distributed Understanding",
        "Institutional Development",
        "Openness Aspiration",
        "Strategic Stewardship Obligation",
        "Short-Horizon Governance Defect",
        "Stewardship Defect",
        "Review and Correction Duty",
    ],
    "#### Def.O1 Transparency, Auditability, and Verification": [
        "Transparency",
        "Public Oversight Baseline Disclosure",
        "Risk Disclosure",
        "Auditability",
        "Evidence Preservation",
        "Evaluation Completeness Constraint",
        "Verifiability",
    ],
    "#### Def.C4 Trust and Trustworthiness": [
        "Trust",
        "Trustworthiness",
        "Trust Degradation and Misleading Reliance",
    ],
    "#### Def.O2 Truth and Epistemic Integrity": [
        "Truth (Constitutional Constraint)",
        "Epistemic Integrity",
        "Foreseeability and Reasonably Foreseeable",
        "Publication and High-Impact Communication",
    ],
    "#### Def.A4 Use of Force, Autonomous Coercion, Autonomous Lethal Systems, and Weapons of Mass Harm": [
        "Use of Force",
        "Autonomous Lethal System",
        "Weapons of Mass Harm",
        "Combatant / Non-Combatant Distinction",
        "Irreversible Deprivation Measure",
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
        if re.match(r"^#### Def\.[OPACI]\d+", stripped):
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


def find_lines_for_heading(all_lines: dict[str, list[str]], heading: str) -> tuple[str, list[str], int]:
    prefix = heading[:20]
    for fname, lines in all_lines.items():
        for i, line in enumerate(lines):
            if line.strip() == heading or line.strip().startswith(prefix):
                if line.strip().startswith("#### 3.") and heading.startswith("#### 3."):
                    if line.strip() == heading:
                        return fname, lines, i
                elif line.strip() == heading:
                    return fname, lines, i
    raise ValueError(f"missing heading: {heading}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repository root")
    args = parser.parse_args()

    root = Path(args.root)
    ch5_files = [CH5_INDEX, *CH5_BANDS]
    all_lines = {name: (root / name).read_text(encoding="utf-8").splitlines() for name in ch5_files}

    failures: list[str] = []
    for heading, expected in EXPECTED_TOPIC_GROUPS.items():
        try:
            fname, lines, start_idx = find_lines_for_heading(all_lines, heading)
            line_no, actual = collect_topic_group_entries(lines, heading, TOPIC_GROUP_HEADINGS)
        except ValueError as exc:
            failures.append(str(exc))
            continue
        if actual != expected:
            failures.append(
                "\n".join(
                    [
                        f"{fname}:{line_no}: topic-group order drift under {heading}",
                        f"  expected: {expected}",
                        f"  actual:   {actual}",
                    ]
                )
            )

    for heading, expected in EXPECTED_CLUSTERS.items():
        try:
            fname, lines, _ = find_lines_for_heading(all_lines, heading)
            line_no, actual = collect_cluster_members(lines, heading)
        except ValueError as exc:
            failures.append(str(exc))
            continue
        if actual != expected:
            failures.append(
                "\n".join(
                    [
                        f"{fname}:{line_no}: cluster member order drift under {heading}",
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
