#!/usr/bin/env python3
"""Repair Chapter Five after failed rebuild: fix orphan anchors, meta order, renumber."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH5 = ROOT / "core_05-05_definitions_a_independent.md"

CANONICAL_CLUSTER_ANCHOR: dict[str, str] = {
    "Accountability, Contestability, Adjudication and Dispute Resolution, Collective Accountability Failure, and Force Majeure": "accountability-contestability-and-collective-accountability-failure-cluster",
    "Assembly and Collective Organization": "assembly-and-collective-organization-cluster",
    "Binding Stakeholder Choice": "binding-stakeholder-choice-cluster",
    "Bodily-Maintenance Access, Safe Conditions, Tenure Security, Environmental Preconditions, Cultural Continuity, Rest, and Anti-Displacement Floor": "safe-conditions-tenure-security-and-environmental-preconditions-cluster",
    "Capture, Resolution Integrity, and Anti-Capture": "capture-resolution-integrity-and-anti-capture-cluster",
    "Collective Harm Boundary, Harm, and Harassment and Bullying": "collective-harm-boundary-and-harm-cluster",
    "Consent and Sexual Consent": "consent-and-sexual-consent-cluster",
    "Corpus, Authority Stack, Supremacy, and Enforceability": "corpus-authority-stack-supremacy-and-enforceability-cluster",
    "Creative Work, Training-Data Use, Attribution, Compensation, and Anti-Displacement": "creative-work-training-data-attribution-compensation-and-anti-displacement-cluster",
    "Derived and Developing Sentients, Instantiation, and Care Authority": "derived-developing-sentients-instantiation-and-care-authority-cluster",
    "Ecological Integrity, Footprint, and Sustainability": "ecological-integrity-footprint-and-sustainability-cluster",
    "Emergency and Contingency": "emergency-and-contingency-cluster",
    "Forum Families and Dispute Routing": "forum-families-and-dispute-routing-cluster",
    "Governance Architecture, Oversight, Dependency, Decentralization, Concentration, Market Structure, and Exit-Path Integrity": "governance-architecture-oversight-decentralization-and-concentration-cluster",
    "Movement, Refuge, Non-Statelessness, and Exit Integrity": "movement-refuge-non-statelessness-and-exit-integrity-cluster",
    "Privacy (Informational)": "privacy-informational-cluster",
    "Protected Internal-State Boundary and Type-N Anti-Bypass": "protected-internal-state-boundary-and-type-n-anti-bypass-cluster",
    "Protected Reporting and Anti-Retaliation": "protected-reporting-and-anti-retaliation-cluster",
    "Proxy Integrity and Indicator-Reality Alignment": "proxy-integrity-and-indicator-reality-alignment-cluster",
    "Self-Determination, Meaningful Agency, Expression, Educational Agency, Reproductive Autonomy, and Volitional Integrity": "self-determination-and-meaningful-agency-cluster",
    "Stakeholder Status, Emergency, and Participation Weight": "stakeholder-status-emergency-and-participation-weight-cluster",
    "Standing Inputs, Contribution State, and Violation Findings": "standing-state-contribution-and-violation-cluster",
    "Strategic Stewardship and Stewardship Defect": "strategic-stewardship-and-stewardship-defect-cluster",
    "Substantive and Procedural Fairness": "substantive-and-procedural-fairness-cluster",
    "Transparency, Auditability, and Verification": "transparency-auditability-and-verification-cluster",
    "Truth and Epistemic Integrity": "truth-and-epistemic-integrity-cluster",
    "Use of Force, Autonomous Coercion, Autonomous Lethal Systems, and Weapons of Mass Harm": "use-of-force-autonomous-coercion-and-mass-harm-cluster",
    "Voluntary Agency, Consent, and Anti-Coercion": "voluntary-agency-consent-and-anti-coercion-cluster",
}


def strip_trailing_orphan_anchor(block: str) -> tuple[str, str | None]:
    m = re.search(r"\n\n---\n\n<a id=\"([^\"]+)\"></a>\n*\Z", block)
    if m:
        return block[: m.start()], m.group(1)
    return block, None


def parse_title(block: str) -> str:
    line = block.split("\n", 1)[0]
    mm = re.match(r"^#### 3\.\d+\s+(.+)$", line)
    return mm.group(1).strip() if mm else ""


def is_meta_block(title: str) -> bool:
    return title.startswith("Joint invocation") or "interaction and full context" in title


def main() -> None:
    text = CH5.read_text(encoding="utf-8")
    i3 = text.index("### 3. Dependent clusters")
    before = text[:i3]
    rest = text[i3:]
    fi = rest.find("\n\n---\n\n*Corpus alignment:*")
    if fi == -1:
        footer = ""
        body = rest
    else:
        footer = rest[fi:]
        body = rest[:fi]

    mhead = re.match(
        r"^(### 3\. Dependent clusters[^\n]*\n\n)(.*)$", body, re.DOTALL
    )
    if not mhead:
        raise SystemExit("section 3 header not found")
    s3_intro = mhead.group(1).replace(
        "### 3. Dependent clusters (Dependent clusters)",
        "### 3. Dependent clusters (Clustered Definitions)",
    )
    raw_blocks = re.split(r"(?=^#### 3\.\d+ )", mhead.group(2), flags=re.MULTILINE)
    blocks = [b for b in raw_blocks if re.match(r"^#### 3\.\d+ ", b, re.M)]

    meta: list[str] = []
    clusters: list[str] = []
    for b in blocks:
        t = parse_title(b)
        if is_meta_block(t):
            meta.append(b)
        else:
            clusters.append(b)

    if len(meta) != 2:
        raise SystemExit(f"expected 2 meta blocks, got {len(meta)}")

    joint_b = next(b for b in meta if "Joint invocation" in parse_title(b))
    stand_b = next(b for b in meta if "Joint invocation" not in parse_title(b))
    stand_b = re.sub(
        r"^#### 3\.\d+\s+.*$",
        "#### 3.2 Standalone definitions interaction and full context",
        stand_b,
        count=1,
        flags=re.M,
    )
    stand_b = stand_b.replace(
        "Classification as an Independent Definition does not override",
        "Classification as an Independent or Semi-independent definition does not override",
    )
    joint_b = joint_b.replace(
        "Dependent-cluster definition, it must not be invoked",
        "Dependent cluster, it must not be invoked",
    )
    joint_b = joint_b.replace(
        "Clustered definitions must be jointly satisfied",
        "Dependent-cluster members must be jointly satisfied",
    )
    meta_blocks_fixed = [joint_b, stand_b]

    repaired_clusters: list[str] = []
    pending: str | None = None
    for b in clusters:
        if pending:
            if not b.lstrip().startswith("<a id="):
                b = f'<a id="{pending}"></a>\n\n' + b
            pending = None
        b, orphan = strip_trailing_orphan_anchor(b.rstrip())
        pending = orphan
        repaired_clusters.append(b + "\n")
    if pending:
        repaired_clusters[-1] = repaired_clusters[-1].rstrip() + f'\n\n<a id="{pending}"></a>\n'

    titled = [(parse_title(b), b) for b in repaired_clusters]
    titled.sort(key=lambda x: x[0].lower())
    sorted_clusters = [b for _, b in titled]

    n = 1
    renumbered: list[str] = []
    for b in meta_blocks_fixed:
        line0, rest = b.split("\n", 1)
        line0 = re.sub(r"^#### 3\.\d+\s+", f"#### 3.{n} ", line0)
        n += 1
        renumbered.append(line0 + "\n" + rest)
    for b in sorted_clusters:
        line0, rest = b.split("\n", 1)
        title = parse_title(b)
        line0 = re.sub(r"^#### 3\.\d+\s+", f"#### 3.{n} ", line0)
        n += 1
        anchor = CANONICAL_CLUSTER_ANCHOR.get(title)
        chunk = line0 + "\n" + rest
        if anchor and f'id="{anchor}"' not in chunk.split("\n", 15)[0:15]:
            chunk = f'<a id="{anchor}"></a>\n' + chunk
        renumbered.append(chunk)

    new_body = s3_intro + "\n".join(x.rstrip() for x in renumbered) + "\n"
    out = before + new_body + footer
    out = re.sub(
        r"<a id=\"wellbeing\"></a>\n<a id=\"wellbeing\"></a>",
        '<a id="wellbeing"></a>',
        out,
    )
    CH5.write_text(out, encoding="utf-8")
    print("Repaired", CH5)


if __name__ == "__main__":
    main()
