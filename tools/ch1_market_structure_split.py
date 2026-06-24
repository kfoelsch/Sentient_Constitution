#!/usr/bin/env python3
"""Split Chapter One §8.3–§8.5 into new §9 Market Structure; renumber §9–§13 → §10–§14."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PART_B = ROOT / "core_01_b_stewardship_capacity_principles.md"

# Anchor migrations: old → new (apply longest keys first in corpus pass)
ANCHOR_MIGRATIONS = [
    ("#852-ceiling-discipline-adopter-requirements", "#932-ceiling-discipline-adopter-requirements"),
    ("#851-consolidation-risk-pre-lock-in-impairment", "#931-consolidation-risk-pre-lock-in-impairment"),
    ("#842-proxy-divergence-invalidation", "#1042-proxy-divergence-invalidation"),
    ("#841-rights-collision-decision-test", "#1041-rights-collision-decision-test"),
    ("#822-trust-truth-alignment", "#1022-trust-truth-alignment"),
    ("#821-preservation-of-epistemic-integrity", "#1021-preservation-of-epistemic-integrity"),
    ("#814-minimization-of-avoidable-burden", "#1014-minimization-of-avoidable-burden"),
    ("#813-minimization-of-harm", "#1013-minimization-of-harm"),
    ("#812-necessity", "#1012-necessity"),
    ("#811-proportionality", "#1011-proportionality"),
    ("#102-read-with-governance-and-incentive-discipline", "#112-read-with-governance-and-incentive-discipline"),
    ("#101-required-evaluation-factors", "#111-required-evaluation-factors"),
    ("#83-concentration-threshold-mechanism-adopter-tunable", "#91-concentration-threshold-mechanism-adopter-tunable"),
    ("#84-pro-competition-and-anti-domination", "#92-pro-competition-and-anti-domination"),
    ("#85-consolidation-ceiling", "#93-consolidation-ceiling"),
    ("#82-epistemic-disclosure-constraints", "#102-epistemic-disclosure-constraints"),
    ("#81-core-tradeoff-principles", "#101-core-tradeoff-principles"),
    ("#13-integrated-application", "#14-integrated-application"),
    ("#12-prohibition-on-absolute-override", "#13-prohibition-on-absolute-override"),
    ("#11-freedom-bounded-agency", "#12-freedom-bounded-agency"),
    ("#10-systemic-evaluation-requirement", "#11-systemic-evaluation-requirement"),
    ("#9-interaction-and-conflict-resolution", "#10-interaction-and-conflict-resolution"),
    ("#82-constitutional-efficiency", "#82-constitutional-efficiency"),  # no-op guard
]

MARKET_STRUCTURE_INTRO = """<a id="9-market-structure"></a>
### 9. Market Structure
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Read with: [Constitutional Tetrad](core_00_preamble.md#constitutional-tetrad) — participation, oversight, accountability, and timeliness where concentration or domination defeats voice, scrutiny, answerability, or timely correction; [material stake](core_00_preamble.md#material-stake) scaling (especially [§9.2 Pro-Competition and Anti-Domination](#92-pro-competition-and-anti-domination)).
- Read with: [Two Constitutional Aims](core_00_preamble.md#two-constitutional-aims) — **Continuity** aim (contestable, durable productive conditions); **Flourishing** aim (fair access to livelihood, agency, and innovation pathways).
- Upstream: Principles: [§8 Shared-System Capacity](#8-shared-system-capacity) — productive-capacity and efficiency claims fail where concentration or domination hollows them; [7. Governance Under Stewardship Discipline](#7-governance-under-stewardship-discipline).
- Downstream: [Chapter Eight §6](core_08-08_misconduct.md#61-concentration-based-subversion-criteria-interaction) (concentration-based subversion); [10. Interaction and Conflict Resolution](#10-interaction-and-conflict-resolution) ([§10.4.2 Proxy-Divergence Invalidation](#1042-proxy-divergence-invalidation)).
- Downstream: Shapes the rights surface for resource allocation, fair compensation, collective organization, interoperability, exit, and anti-capture review; especially [Article III-D: Labor and Economic Floor](core_10-10_rights_part_a.md#article-iii-d-labor-and-economic-floor), [Article IV: Resource Allocation, Dependencies, and Ecosystem Funding](core_10-10_rights_part_a.md#article-iv-resource-allocation-dependencies-and-ecosystem-funding), and [Article XIX: Interoperability, Portability, and Exit Integrity](core_10-10_rights_part_c.md#article-xix-interoperability-portability-and-exit-integrity).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Evaluation · Compliance</span></strong></summary>

- [Market Structure](core_05a_accountability_definitions.md#market-structure-constitutional) · [O](core_05a_accountability_definitions.md#market-structure-constitutional) · [E](core_05a_accountability_definitions.md#market-structure-constitutional-e) · [C](core_05a_accountability_definitions.md#market-structure-constitutional-c)
- [Concentration Threshold](core_05a_accountability_definitions.md#concentration-threshold-constitutional) · [O](core_05a_accountability_definitions.md#concentration-threshold-constitutional) · [E](core_05a_accountability_definitions.md#concentration-threshold-constitutional-e) · [C](core_05a_accountability_definitions.md#concentration-threshold-constitutional-c)
- [Contestability](core_05a_accountability_definitions.md#contestability) · [O](core_05a_accountability_definitions.md#contestability) · [E](core_05a_accountability_definitions.md#contestability-e) · [C](core_05a_accountability_definitions.md#contestability-c)
- [Proxy Divergence](core_05o_oversight_definitions.md#proxy-divergence) · [O](core_05o_oversight_definitions.md#proxy-divergence) · [E](core_05o_oversight_definitions.md#proxy-divergence-e) · [C](core_05o_oversight_definitions.md#proxy-divergence-c)
- [Dependency](core_05c_continuity_definitions.md#dependency) · [O](core_05c_continuity_definitions.md#dependency) · [E](core_05c_continuity_definitions.md#dependency-e) · [C](core_05c_continuity_definitions.md#dependency-c)
- [Meaningful Agency](core_05p_participation_definitions.md#meaningful-agency) · [O](core_05a_accountability_definitions.md#meaningful-agency-o) · [E](core_05p_participation_definitions.md#meaningful-agency-e) · [C](core_05p_participation_definitions.md#meaningful-agency-c)

</details>

<br>

*In plain terms: **Market Structure** is the constitutional discipline for keeping productive life contestable — markets, platforms, labor arrangements, infrastructure, data, compute, credentials, and comparable dependencies must not become durable chokepoints that lock people in, block rivals, or capture accountability. Scale and innovation are allowed; domination is not. **§9.1–§9.3** carry concentration thresholds, anti-domination rules, and consolidation ceilings that must bite before lock-in.*

**Market structure** governs how sentients and shared systems experience contestable participation in productive life — not only commercial exchange, but also platforms, labor-demand markets, supplier and resource-control systems, credentialing pathways, capital-access channels, and information-sphere gatekeeping where dependency is material.

Productive-capacity and constitutional-efficiency claims under **§8** fail where market structure permits concentration, domination, or consolidation that predictably degrades wellbeing, meaningful agency, dignity, ecological integrity, or constitutional review.

This section advances the [Two Constitutional Aims](core_00_preamble.md#two-constitutional-aims) — **Flourishing** through fair access to livelihood and innovation, and **Continuity** through durable, contestable systems — and carries the [Constitutional Tetrad](core_00_preamble.md#constitutional-tetrad) where concentration or domination defeats voice, scrutiny, answerability, or timely correction, scaled to [material stake](core_00_preamble.md#material-stake).

"""

LEGACY_ANCHORS = """
<a id="83-concentration-threshold-mechanism-adopter-tunable"></a>
<a id="84-pro-competition-and-anti-domination"></a>
<a id="85-consolidation-ceiling"></a>
<a id="851-consolidation-risk-pre-lock-in-impairment"></a>
<a id="852-ceiling-discipline-adopter-requirements"></a>
<a id="8-interaction-and-conflict-resolution"></a>
<a id="81-core-tradeoff-principles"></a>
<a id="811-proportionality"></a>
<a id="812-necessity"></a>
<a id="813-minimization-of-harm"></a>
<a id="814-minimization-of-avoidable-burden"></a>
<a id="82-epistemic-disclosure-constraints"></a>
<a id="821-preservation-of-epistemic-integrity"></a>
<a id="822-trust-truth-alignment"></a>
<a id="841-rights-collision-decision-test"></a>
<a id="842-proxy-divergence-invalidation"></a>
<a id="9-interaction-and-conflict-resolution"></a>
<a id="9-systemic-evaluation-requirement"></a>
<a id="10-freedom-bounded-agency"></a>
<a id="11-prohibition-on-absolute-override"></a>
<a id="12-integrated-application"></a>
<a id="13-integrated-application"></a>
"""


def split_part_b(text: str) -> str:
    start_marker = "#### 8.3 Concentration Threshold Mechanism (Adopter-Tunable)"
    end_marker = "### 9. Interaction and Conflict Resolution"
    start = text.index(start_marker)
    end = text.index(end_marker)
    market_block = text[start:end]
    before = text[:start]
    after = text[end:]

    # Trim §8 intro references to market-structure content
    before = before.replace(
        "**§8.3–§8.5** carry the anti-concentration discipline: harmful pile-ups of control trigger review, durable domination is barred, and consolidation ceilings must bite before lock-in.",
        "Anti-concentration discipline for contestable productive conditions appears in **[§9 Market Structure](#9-market-structure)**.",
    )
    before = before.replace(
        "- Read with: [Constitutional Tetrad](core_00_preamble.md#constitutional-tetrad) — participation, oversight, accountability, and timeliness where concentration or domination defeats voice, scrutiny, answerability, or timely correction; [material stake](core_00_preamble.md#material-stake) scaling (especially [§8.4 Pro-Competition and Anti-Domination](#84-pro-competition-and-anti-domination)).\n",
        "",
    )
    before = before.replace(
        "- [Concentration Threshold](core_05a_accountability_definitions.md#concentration-threshold-constitutional) · [O](core_05a_accountability_definitions.md#concentration-threshold-constitutional) · [E](core_05a_accountability_definitions.md#concentration-threshold-constitutional-e) · [C](core_05a_accountability_definitions.md#concentration-threshold-constitutional-c)\n",
        "",
    )
    before = before.replace(
        "**Concentration Threshold** supplies adopter-tunable triggers for heightened review where concentration threatens those outcomes.\n\n",
        "",
    )
    before = before.replace(
        "and carries the [Constitutional Tetrad](core_00_preamble.md#constitutional-tetrad) where concentration or domination defeats voice, scrutiny, answerability, or timely correction, scaled to [material stake](core_00_preamble.md#material-stake).\n",
        ".\n",
    )

    # Renumber market block headings 8.3→9.1 etc.
    market_block = market_block.replace("#### 8.3 ", "#### 9.1 ")
    market_block = market_block.replace("#### 8.4 ", "#### 9.2 ")
    market_block = market_block.replace("#### 8.5 ", "#### 9.3 ")
    market_block = market_block.replace("##### 8.5.1 ", "##### 9.3.1 ")
    market_block = market_block.replace("##### 8.5.2 ", "##### 9.3.2 ")

    # Internal §8 refs inside market block → §9
    market_block = re.sub(r"\*\*§8\*\*", "**§9**", market_block)
    market_block = market_block.replace("**§8.3**", "**§9.1**")
    market_block = market_block.replace("**§8.4**", "**§9.2**")
    market_block = market_block.replace("**§8.5**", "**§9.3**")
    market_block = market_block.replace("[§8.4.2 Proxy-Divergence Invalidation](#842-proxy-divergence-invalidation)", "[§10.4.2 Proxy-Divergence Invalidation](#1042-proxy-divergence-invalidation)")
    market_block = market_block.replace("above the **§8** floor", "above the **§9** floor")
    market_block = market_block.replace("the **§8** non-concentration discipline", "the **§9** non-concentration discipline")
    market_block = market_block.replace("The non-concentration discipline in **§8**", "The non-concentration discipline in **§9**")
    market_block = market_block.replace("non-concentration discipline in **§8**", "non-concentration discipline in **§9**")
    market_block = market_block.replace("nullify the **§8** floor, the **§8.3** threshold mechanism, or **§8.4** anti-domination discipline", "nullify the **§9** floor, the **§9.1** threshold mechanism, or **§9.2** anti-domination discipline")
    market_block = market_block.replace("under the **§8** non-concentration discipline and **§8.4** anti-domination rules", "under the **§9** non-concentration discipline and **§9.2** anti-domination rules")
    market_block = market_block.replace("the **§8.3** threshold mechanism, or **§8.4** anti-domination discipline", "the **§9.1** threshold mechanism, or **§9.2** anti-domination discipline")
    market_block = market_block.replace("does not narrow Article III-D, Article IV, Article XIX, **§8.5**, or Chapter Eight", "does not narrow Article III-D, Article IV, Article XIX, **§9.3**, or Chapter Eight")

    # Update anchors in market block
    market_block = market_block.replace(
        '<a id="511-concentration-threshold-mechanism-adopter-tunable"></a>\n#### 9.1',
        '<a id="91-concentration-threshold-mechanism-adopter-tunable"></a>\n#### 9.1',
    )
    market_block = market_block.replace(
        '<a id="85-consolidation-ceiling"></a>\n#### 9.3',
        '<a id="93-consolidation-ceiling"></a>\n#### 9.3',
    )
    market_block = market_block.replace(
        '<a id="851-consolidation-risk-pre-lock-in-impairment"></a>',
        '<a id="931-consolidation-risk-pre-lock-in-impairment"></a>',
    )
    market_block = market_block.replace(
        '<a id="852-ceiling-discipline-adopter-requirements"></a>',
        '<a id="932-ceiling-discipline-adopter-requirements"></a>',
    )
    if '<a id="92-pro-competition-and-anti-domination"></a>' not in market_block:
        market_block = market_block.replace(
            "#### 9.2 Pro-Competition and Anti-Domination",
            '<a id="92-pro-competition-and-anti-domination"></a>\n#### 9.2 Pro-Competition and Anti-Domination',
        )

    text = before + MARKET_STRUCTURE_INTRO + market_block + after

    # Renumber old §9–§13 → §10–§14 (headings only, high to low)
    for old, new in [
        ("### 13. Integrated Application", "### 14. Integrated Application"),
        ("### 12. Prohibition on Absolute Override", "### 13. Prohibition on Absolute Override"),
        ("### 11. Freedom (Bounded Agency)", "### 12. Freedom (Bounded Agency)"),
        ("### 10. Systemic Evaluation Requirement", "### 11. Systemic Evaluation Requirement"),
        ("### 9. Interaction and Conflict Resolution", "### 10. Interaction and Conflict Resolution"),
        ("#### 9.4 Rights-Collision Procedure", "#### 10.4 Rights-Collision Procedure"),
        ("#### 9.3 Freedom-Limitation Constraints", "#### 10.3 Freedom-Limitation Constraints"),
        ("#### 9.2 Epistemic Disclosure Constraints", "#### 10.2 Epistemic Disclosure Constraints"),
        ("#### 9.1 Core Tradeoff Principles", "#### 10.1 Core Tradeoff Principles"),
        ("##### 9.4.2 Proxy-Divergence Invalidation", "##### 10.4.2 Proxy-Divergence Invalidation"),
        ("##### 9.4.1 Rights-Collision Decision Test", "##### 10.4.1 Rights-Collision Decision Test"),
        ("##### 9.3.2 Time-Consistency Constraint", "##### 10.3.2 Time-Consistency Constraint"),
        ("##### 9.3.1 Constraint on Freedom", "##### 10.3.1 Constraint on Freedom"),
        ("##### 9.2.2 Trust-Truth Alignment", "##### 10.2.2 Trust-Truth Alignment"),
        ("##### 9.2.1 Preservation of Epistemic Integrity", "##### 10.2.1 Preservation of Epistemic Integrity"),
        ("##### 9.1.4 Minimization of Avoidable Burden", "##### 10.1.4 Minimization of Avoidable Burden"),
        ("##### 9.1.3 Minimization of Harm", "##### 10.1.3 Minimization of Harm"),
        ("##### 9.1.2 Necessity", "##### 10.1.2 Necessity"),
        ("##### 9.1.1 Proportionality", "##### 10.1.1 Proportionality"),
        ("#### 10.2 Read-with: Governance and Incentive Discipline", "#### 11.2 Read-with: Governance and Incentive Discipline"),
        ("#### 10.1 Required Evaluation Factors", "#### 11.1 Required Evaluation Factors"),
        ("##### 10.1.5 Assembly, Collective Organization, and Institutional Formation", "##### 11.1.5 Assembly, Collective Organization, and Institutional Formation"),
        ("##### 10.1.4 Voluntary Discontinuation and Exit Rights", "##### 11.1.4 Voluntary Discontinuation and Exit Rights"),
        ("##### 10.1.3 Privacy (Informational) Joint Invocation", "##### 11.1.3 Privacy (Informational) Joint Invocation"),
        ("##### 10.1.2 Accessibility Under Sentience Non-Exclusion", "##### 11.1.2 Accessibility Under Sentience Non-Exclusion"),
        ("##### 10.1.1 Systemic Scope and Risk Factors", "##### 11.1.1 Systemic Scope and Risk Factors"),
    ]:
        text = text.replace(old, new)

    # Insert legacy anchors before legacy block end
    legacy_insert = "<a id=\"12-integrated-application\"></a>\n"
    if legacy_insert in text and "id=\"83-concentration" not in text.split("Legacy Chapter One")[1][:500]:
        text = text.replace(
            "<!-- Legacy Chapter One anchor redirects",
            LEGACY_ANCHORS + "<!-- Legacy Chapter One anchor redirects",
            1,
        )

    # File metadata
    text = text.replace(
        "It contains **Chapter One, Part B** (§§6–13).",
        "It contains **Chapter One, Part B** (§§6–14).",
    )
    text = text.replace(
        "**Reading arc:** §6 stewardship → §7 governance discipline → §8 capacity → §9 tradeoffs → §10 whole-system evaluation → §§11–13 agency, integration, and override limits.",
        "**Reading arc:** §6 stewardship → §7 governance discipline → §8 capacity → §9 market structure → §10 tradeoffs → §11 whole-system evaluation → §§12–14 agency, integration, and override limits.",
    )

    # Update anchors in tradeoff/system sections
    text = text.replace(
        '<a id="81-core-tradeoff-principles"></a>\n#### 10.1',
        '<a id="101-core-tradeoff-principles"></a>\n#### 10.1',
    )
    text = text.replace('<a id="811-proportionality"></a>', '<a id="1011-proportionality"></a>')
    text = text.replace('<a id="812-necessity"></a>', '<a id="1012-necessity"></a>')
    text = text.replace('<a id="813-minimization-of-harm"></a>', '<a id="1013-minimization-of-harm"></a>')
    text = text.replace('<a id="814-minimization-of-avoidable-burden"></a>', '<a id="1014-minimization-of-avoidable-burden"></a>')
    text = text.replace('<a id="82-epistemic-disclosure-constraints"></a>', '<a id="102-epistemic-disclosure-constraints"></a>')
    text = text.replace('<a id="821-preservation-of-epistemic-integrity"></a>', '<a id="1021-preservation-of-epistemic-integrity"></a>')
    text = text.replace('<a id="822-trust-truth-alignment"></a>', '<a id="1022-trust-truth-alignment"></a>')
    text = text.replace('<a id="841-rights-collision-decision-test"></a>', '<a id="1041-rights-collision-decision-test"></a>')
    text = text.replace(
        '<a id="102-read-with-governance-and-incentive-discipline"></a>',
        '<a id="112-read-with-governance-and-incentive-discipline"></a>',
    )

    # Add section anchor for §10
    if '<a id="10-interaction-and-conflict-resolution"></a>' not in text:
        text = text.replace(
            "### 10. Interaction and Conflict Resolution",
            '<a id="10-interaction-and-conflict-resolution"></a>\n### 10. Interaction and Conflict Resolution',
            1,
        )

    return renumber_internal_refs(text)


def renumber_internal_refs(text: str) -> str:
    """Update § and # internal references in Part B after structural renumber."""

    # §13 → §14 ... §9 → §10 (section level, avoid subsections)
    section_refs = [
        (r"§13\b", "§14"),
        (r"§12\b", "§13"),
        (r"§11\b", "§12"),
        (r"§10\b", "§11"),
        (r"§9\b", "§10"),
    ]
    # Apply to tradeoff block only after market structure inserted - whole file pass with subsection first

    subsection_pairs = [
        ("§9.4.2", "§10.4.2"),
        ("§9.4.1", "§10.4.1"),
        ("§9.4", "§10.4"),
        ("§9.3.2", "§10.3.2"),
        ("§9.3.1", "§10.3.1"),
        ("§9.3", "§10.3"),
        ("§9.2.2", "§10.2.2"),
        ("§9.2.1", "§10.2.1"),
        ("§9.2", "§10.2"),
        ("§9.1.4", "§10.1.4"),
        ("§9.1.3", "§10.1.3"),
        ("§9.1.2", "§10.1.2"),
        ("§9.1.1", "§10.1.1"),
        ("§9.1", "§10.1"),
        ("§8.5.2", "§9.3.2"),
        ("§8.5.1", "§9.3.1"),
        ("§8.5", "§9.3"),
        ("§8.4.2", "§10.4.2"),
        ("§8.4", "§9.2"),
        ("§8.3", "§9.1"),
        ("§13.", "§14."),
        ("§12.", "§13."),
        ("§11.", "§12."),
        ("§10.2 ", "§11.2 "),
        ("§10.1.", "§11.1."),
        ("§10.1 ", "§11.1 "),
        ("§10 ", "§11 "),
    ]
    for old, new in subsection_pairs:
        text = text.replace(old, new)

    # Fix double-bumps where §9 market structure became §10
    text = text.replace("§10 Market Structure", "§9 Market Structure")
    text = text.replace("§10.1 Concentration", "§9.1 Concentration")
    text = text.replace("§10.2 Pro-Competition", "§9.2 Pro-Competition")
    text = text.replace("§10.3 Consolidation", "§9.3 Consolidation")
    text = text.replace("§10.3.1 ", "§9.3.1 ")
    text = text.replace("§10.3.2 ", "§9.3.2 ")

    # Hash link bumps for tradeoffs/evaluation
    hash_pairs = [
        ("#914-minimization-of-avoidable-burden", "#1014-minimization-of-avoidable-burden"),
        ("#913-minimization-of-harm", "#1013-minimization-of-harm"),
        ("#912-necessity", "#1012-necessity"),
        ("#911-proportionality", "#1011-proportionality"),
        ("#942-proxy-divergence-invalidation", "#1042-proxy-divergence-invalidation"),
        ("#941-rights-collision-decision-test", "#1041-rights-collision-decision-test"),
        ("#932-time-consistency-constraint", "#1032-time-consistency-constraint"),
        ("#931-constraint-on-freedom", "#1031-constraint-on-freedom"),
        ("#922-trust-truth-alignment", "#1022-trust-truth-alignment"),
        ("#921-preservation-of-epistemic-integrity", "#1021-preservation-of-epistemic-integrity"),
        ("#92-epistemic-disclosure-constraints", "#102-epistemic-disclosure-constraints"),
        ("#101-required-evaluation-factors", "#111-required-evaluation-factors"),
        ("#1011-systemic-scope-and-risk-factors", "#1111-systemic-scope-and-risk-factors"),
        ("#1012-accessibility-under-sentience-non-exclusion", "#1112-accessibility-under-sentience-non-exclusion"),
        ("#1013-privacy-informational-joint-invocation", "#1113-privacy-informational-joint-invocation"),
        ("#1014-voluntary-discontinuation-and-exit-rights", "#1114-voluntary-discontinuation-and-exit-rights"),
        ("#1015-assembly-collective-organization-and-institutional-formation", "#1115-assembly-collective-organization-and-institutional-formation"),
        ("#9-interaction-and-conflict-resolution", "#10-interaction-and-conflict-resolution"),
        ("#10-systemic-evaluation-requirement", "#11-systemic-evaluation-requirement"),
        ("#11-freedom-bounded-agency", "#12-freedom-bounded-agency"),
        ("#12-prohibition-on-absolute-override", "#13-prohibition-on-absolute-override"),
        ("#13-integrated-application", "#14-integrated-application"),
    ]
    for old, new in hash_pairs:
        text = text.replace(old, new)

    # Restore market-structure hash links if bumped
    text = text.replace("#102-pro-competition-and-anti-domination", "#92-pro-competition-and-anti-domination")
    text = text.replace("#101-concentration-threshold-mechanism-adopter-tunable", "#91-concentration-threshold-mechanism-adopter-tunable")

    # Section references in prose
    text = text.replace("**§§6–10**", "**§§6–11**")
    text = text.replace("**Section 10**", "**Section 11**")
    text = text.replace("**§10.1 Required Evaluation Factors**", "**§11.1 Required Evaluation Factors**")
    text = text.replace("[§9 Interaction and Conflict Resolution]", "[§10 Interaction and Conflict Resolution]")
    text = text.replace("[9. Interaction and Conflict Resolution](#9-interaction-and-conflict-resolution)", "[10. Interaction and Conflict Resolution](#10-interaction-and-conflict-resolution)")
    text = text.replace("[§8.4.2 Proxy-Divergence Invalidation](#842-proxy-divergence-invalidation)", "[§10.4.2 Proxy-Divergence Invalidation](#1042-proxy-divergence-invalidation)")
    text = text.replace("§8.1.1–§8.1.3", "§10.1.1–§10.1.3")
    text = text.replace("[§8.3 Concentration Threshold Mechanism](#83-concentration-threshold-mechanism-adopter-tunable)", "[§9.1 Concentration Threshold Mechanism](#91-concentration-threshold-mechanism-adopter-tunable)")
    text = text.replace("[§8.4 Pro-Competition and Anti-Domination](#84-pro-competition-and-anti-domination)", "[§9.2 Pro-Competition and Anti-Domination](#92-pro-competition-and-anti-domination)")

    return text


def migrate_corpus_file(path: Path, content: str) -> str:
    if path.name == "ch1_market_structure_split.py":
        return content
    original = content
    for old, new in ANCHOR_MIGRATIONS:
        if old == new:
            continue
        content = content.replace(old, new)

    # Section reference replacements (order matters)
    ref_pairs = [
        ("Chapter One §8.5", "Chapter One §9.3"),
        ("Chapter One §8.4", "Chapter One §9.2"),
        ("Chapter One §8.3", "Chapter One §9.1"),
        ("§8.5", "§9.3"),
        ("§8.4", "§9.2"),
        ("§8.3", "§9.1"),
        ("§9.4.2", "§10.4.2"),
        ("§9.4.1", "§10.4.1"),
        ("§9.4", "§10.4"),
        ("§9.3.2", "§10.3.2"),
        ("§9.3.1", "§10.3.1"),
        ("§9.3 Freedom", "§10.3 Freedom"),
        ("§9.2 Epistemic", "§10.2 Epistemic"),
        ("§9.1.4", "§10.1.4"),
        ("§9.1.3", "§10.1.3"),
        ("§9.1.2", "§10.1.2"),
        ("§9.1.1", "§10.1.1"),
        ("§9.1 Core", "§10.1 Core"),
        ("§9 Interaction", "§10 Interaction"),
        ("§10.1 Required", "§11.1 Required"),
        ("§10.2 Read-with", "§11.2 Read-with"),
        ("§10 Systemic", "§11 Systemic"),
        ("§11 Freedom", "§12 Freedom"),
        ("§12 Prohibition", "§13 Prohibition"),
        ("§13 Integrated", "§14 Integrated"),
        ("#914-minimization-of-avoidable-burden", "#1014-minimization-of-avoidable-burden"),
        ("#913-minimization-of-harm", "#1013-minimization-of-harm"),
        ("#912-necessity", "#1012-necessity"),
        ("#911-proportionality", "#1011-proportionality"),
        ("#942-proxy-divergence-invalidation", "#1042-proxy-divergence-invalidation"),
        ("#941-rights-collision-decision-test", "#1041-rights-collision-decision-test"),
        ("#932-time-consistency-constraint", "#1032-time-consistency-constraint"),
        ("#931-constraint-on-freedom", "#1031-constraint-on-freedom"),
        ("#922-trust-truth-alignment", "#1022-trust-truth-alignment"),
        ("#921-preservation-of-epistemic-integrity", "#1021-preservation-of-epistemic-integrity"),
        ("#92-epistemic-disclosure-constraints", "#102-epistemic-disclosure-constraints"),
        ("#101-required-evaluation-factors", "#111-required-evaluation-factors"),
        ("#9-interaction-and-conflict-resolution", "#10-interaction-and-conflict-resolution"),
        ("#10-systemic-evaluation-requirement", "#11-systemic-evaluation-requirement"),
        ("#11-freedom-bounded-agency", "#12-freedom-bounded-agency"),
        ("#12-prohibition-on-absolute-override", "#13-prohibition-on-absolute-override"),
        ("#13-integrated-application", "#14-integrated-application"),
        ("#83-concentration-threshold-mechanism-adopter-tunable", "#91-concentration-threshold-mechanism-adopter-tunable"),
        ("#84-pro-competition-and-anti-domination", "#92-pro-competition-and-anti-domination"),
        ("#85-consolidation-ceiling", "#93-consolidation-ceiling"),
        ("#851-consolidation-risk-pre-lock-in-impairment", "#931-consolidation-risk-pre-lock-in-impairment"),
        ("#852-ceiling-discipline-adopter-requirements", "#932-ceiling-discipline-adopter-requirements"),
        ("#81-core-tradeoff-principles", "#101-core-tradeoff-principles"),
        ("#82-epistemic-disclosure-constraints", "#102-epistemic-disclosure-constraints"),
        ("Chapter One §9.4.2", "Chapter One §10.4.2"),
        ("Chapter One §9.4.1", "Chapter One §10.4.1"),
        ("Chapter One §9.4", "Chapter One §10.4"),
        ("Chapter One §9.3.2", "Chapter One §10.3.2"),
        ("Chapter One §9.3.1", "Chapter One §10.3.1"),
        ("Chapter One §9.3", "Chapter One §10.3"),
        ("Chapter One §9.2 Constitutional Efficiency", "Chapter One §8.2 Constitutional Efficiency"),
        ("Chapter One §9.2 Epistemic", "Chapter One §10.2 Epistemic"),
        ("Chapter One §9.1.4", "Chapter One §10.1.4"),
        ("Chapter One §9.1.3", "Chapter One §10.1.3"),
        ("Chapter One §9.1.2", "Chapter One §10.1.2"),
        ("Chapter One §9.1.1", "Chapter One §10.1.1"),
        ("Chapter One §9.1 Core", "Chapter One §10.1 Core"),
        ("Chapter One §9 Interaction", "Chapter One §10 Interaction"),
        ("Chapter One §10.1 Required", "Chapter One §11.1 Required"),
        ("Chapter One §10 Systemic", "Chapter One §11 Systemic"),
        ("Chapter One §11 Freedom", "Chapter One §12 Freedom"),
        ("Chapter One §12 Prohibition", "Chapter One §13 Prohibition"),
        ("Chapter One §13 Integrated", "Chapter One §14 Integrated"),
        ("Chapter One §6 non-concentration", "Chapter One §9 non-concentration"),
        ("Chapter One §6.4", "Chapter One §9.2"),
        ("Chapter One §6.5", "Chapter One §9.3"),
        ("**§6** non-concentration", "**§9** non-concentration"),
        ("**§6.4**", "**§9.2**"),
        ("**§6.5**", "**§9.3**"),
    ]
    for old, new in ref_pairs:
        content = content.replace(old, new)

    # Fix over-replacement of §9 market structure references in files that got §10
    if path != PART_B:
        content = content.replace("Chapter One §10.1 Concentration", "Chapter One §9.1 Concentration")
        content = content.replace("Chapter One §10.2 Pro-Competition", "Chapter One §9.2 Pro-Competition")
        content = content.replace("Chapter One §10.3 Consolidation", "Chapter One §9.3 Consolidation")

    return content if content != original else content


def main() -> int:
    part_b = PART_B.read_text(encoding="utf-8")
    PART_B.write_text(split_part_b(part_b), encoding="utf-8")
    print(f"Updated {PART_B}")

    skip_dirs = {".git", "archive", "evidence", "node_modules", "__pycache__"}
    extensions = {".md", ".json", ".py"}
    for path in ROOT.rglob("*"):
        if path == PART_B or path.name == "ch1_market_structure_split.py":
            continue
        if any(p in skip_dirs for p in path.parts):
            continue
        if path.suffix not in extensions:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        new_text = migrate_corpus_file(path, text)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            print(f"Updated {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
