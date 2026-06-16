#!/usr/bin/env python3
"""Split core_00-01_principles.md into three Chapter One files and renumber Part B.

See implementation/CH1_SPLIT_RENUMBER_CUT_LIST_2026-06-16.md.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "core_00-01_principles.md"

PREAMBLE_HEADER = """# Sentient Constitution — Preamble

This file is **part of the Sentient Constitution** and is **binding only together** with the other numbered `core_*` files read as one instrument. It contains **Chapter 00** (preamble / foundational requirements). Reading order and edition metadata are maintained in [README.md](README.md).

**Next:** [core_01_values_principles.md](core_01_values_principles.md) (Chapter One, Part A — Values Principles).

---
"""

VALUES_HEADER = """# Sentient Constitution — Values Principles (Chapter One, Part A)

This file is **part of the Sentient Constitution** and is **binding only together** with the other numbered `core_*` files read as one instrument. It contains **Chapter One, Part A** (§§1–5: interpretation, aims, wellbeing, Safety and Truth, Trust).

**Upstream:** [core_00_preamble.md](core_00_preamble.md)  
**Next:** [core_01_stewardship_capacity_principles.md](core_01_stewardship_capacity_principles.md) (Chapter One, Part B).

---
"""

PART_B_HEADER = """# Sentient Constitution — Stewardship, Capacity, and Constitutional Safeguards (Chapter One, Part B)

This file is **part of the Sentient Constitution** and is **binding only together** with the other numbered `core_*` files read as one instrument. It contains **Chapter One, Part B** (§§6–13).

**Upstream:** [core_01_values_principles.md](core_01_values_principles.md) (Chapter One, Part A)  
**Next:** [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md)

---
<a id="chapter-01-part-b-stewardship-capacity-and-constitutional-safeguards"></a>
## CHAPTER 01, PART B: STEWARDSHIP, CAPACITY, AND CONSTITUTIONAL SAFEGUARDS

**Principle hierarchy (Part B).** At principle layer:

1. **Stewardship** orients systems toward durable constitutional alignment over time, including the **Continuity** aim under the [Two Constitutional Aims](core_01_values_principles.md#two-constitutional-aims).
2. **Governance** structures authorized decision-making, participation, and accountability. Where governance and stewardship conflict, stewardship discipline controls at principle layer unless **Necessity** and **Proportionality** expressly justify a bounded, time-limited exception with correction paths. Operative authorization and contract-layer requirements remain owned by **Chapter Eleven**.
3. **Shared-System Capacity** is the durable, contestable ability those jointly produce — an **instrumental outcome**, not a freestanding trump value.

**Reading arc:** §6 stewardship → §7 governance discipline → §8 capacity → §9 tradeoffs → §10 whole-system evaluation → §§11–13 agency, integration, and override limits.

"""

PART_B_SEC7_FRAMING = """
<a id="7-governance-under-stewardship-discipline"></a>
### 7. Governance Under Stewardship Discipline

#### 7.1 Governance as Authorized Structure

*In plain terms: governance tells you who may decide and how — but only counts when it stays under stewardship discipline and does not eat the future for today's metrics.*

**Governance** at principle layer means the structures, rules, allocation of authority, and processes by which already-authorized systems and institutions are directed and held accountable — as defined in Chapter Five ([Governance](core_05-05_definitions_b_semi_independent.md#governance)) and operationalized under **Chapter Eleven** for the **Constitutional Contract Layer** and stakeholder participation layers stated in [Chapter 00](core_00_preamble.md#chapter-00-preamble--foundational-requirements).

Governance is **necessary** but **not sufficient**. It must remain subordinate to **Stewardship** where procedural regularity, short-horizon optimization, or institutional self-protection would otherwise defeat durable alignment, **Continuity**, or Rights-Floor integrity.

<a id="7-governance-as-authorized-structure"></a>

#### 7.2 Short-Horizon Governance Defect

*In plain terms: governance that keeps hitting quarterly targets while hollowing safety, truth, participation, or the future is not "working governance" — it is a defect this Constitution names and corrects.*

A **short-horizon governance defect** is a material pattern that optimizes immediate output, convenience, institutional self-protection, or transient stability at the foreseeable expense of medium- or long-horizon constitutional alignment.

Systems must detect, disclose, and correct such defects through **Review and Correction Duty**, contestable oversight, and the incentive and capture discipline in **§§7.3–7.7**.

<a id="72-short-horizon-governance-defect"></a>

"""

PART_B_SEC10_POINTER = """
#### 10.2 Read-with: Governance and Incentive Discipline

*In plain terms: checking the whole system is not done if you skip whether the incentives and governance structures will quietly undo the outcome you claim to protect.*

Whole-system evaluation under **§10.1** is incomplete if it omits whether incentives and governance structures will preserve constitutional outcomes. Apply **§7 Governance Under Stewardship Discipline** for that discipline; **§10.1** does not duplicate **§7**.

<a id="102-read-with-governance-and-incentive-discipline"></a>

"""

LEGACY_ANCHORS = """<!-- Legacy Chapter One anchor redirects (2026-06 split/renumber); do not remove without link migration. -->
<a id="6-shared-system-capacity-and-stewardship"></a>
<a id="61-shared-system-capacity"></a>
<a id="611-productive-capacity-instrumental-good"></a>
<a id="612-constitutional-efficiency"></a>
<a id="511-concentration-threshold-mechanism-adopter-tunable"></a>
<a id="613-concentration-threshold-mechanism-adopter-tunable"></a>
<a id="614-pro-competition-and-anti-domination"></a>
<a id="615-consolidation-ceiling"></a>
<a id="62-stewardship-and-distributed-understanding"></a>
<a id="521-distributed-understanding"></a>
<a id="522-stewardship"></a>
<a id="621-stewardship"></a>
<a id="7-interaction-and-conflict-resolution"></a>
<a id="71-core-tradeoff-principles"></a>
<a id="711-proportionality"></a>
<a id="714-minimization-of-avoidable-burden"></a>
<a id="722-trust-truth-alignment"></a>
<a id="741-rights-collision-decision-test"></a>
<a id="742-proxy-divergence-invalidation"></a>
<a id="822-stewardship-and-operator-incentive-alignment"></a>
<a id="81-required-evaluation-factors"></a>
<a id="8-systemic-evaluation-requirement"></a>
<a id="9-freedom-bounded-agency"></a>
<a id="10-prohibition-on-absolute-override"></a>
<a id="11-integrated-application"></a>
<a id="6-shared-system-capacity"></a>
<a id="51-productive-capacity-instrumental-good"></a>
<a id="52-distributed-understanding-and-stewardship"></a>
<a id="7-stewardship-and-distributed-understanding"></a>
<a id="8-interaction-and-conflict-resolution"></a>
<a id="92-incentive-alignment-and-system-capture"></a>
<a id="9-systemic-evaluation-requirement"></a>
<a id="10-freedom-bounded-agency"></a>
<a id="11-prohibition-on-absolute-override"></a>
<a id="12-integrated-application"></a>

"""

STUB_CONTENT = """# The Sentient Constitution — Chapter 00 and Chapter One (retired path)

This path is **retired**. Chapter 00 and Chapter One now live in:

1. [core_00_preamble.md](core_00_preamble.md) — **Chapter 00** (Preamble)
2. [core_01_values_principles.md](core_01_values_principles.md) — **Chapter One, Part A** (Values Principles, §§1–5)
3. [core_01_stewardship_capacity_principles.md](core_01_stewardship_capacity_principles.md) — **Chapter One, Part B** (§§6–13)

Read together with the other numbered `core_*` files as one instrument. Edition metadata: [README.md](README.md).

---
<a id="constitutional-triad"></a>
<a id="material-stake"></a>
<a id="material-family-orientation"></a>
<a id="two-constitutional-aims"></a>
<a id="flourishing"></a>
<a id="continuity"></a>

"""


def slice_lines(lines: list[str], start: int, end: int) -> str:
    """1-based inclusive start/end."""
    return "".join(lines[start - 1 : end])


def fix_preamble_links(text: str) -> str:
    text = text.replace(
        "[Chapter One, §2 Purpose and Role](#2-purpose-and-role)",
        "[Chapter One, §2 Purpose and Role](core_01_values_principles.md#2-purpose-and-role)",
    )
    text = text.replace(
        "[§3.2 Recognition, Reinforcement, and Aspiration](#32-recognition-reinforcement-and-aspiration)",
        "[§3.2 Recognition, Reinforcement, and Aspiration](core_01_values_principles.md#32-recognition-reinforcement-and-aspiration)",
    )
    text = text.replace(
        "stated in Chapter One.",
        "stated in [Chapter One, Part A](core_01_values_principles.md).",
    )
    return text


def fix_values_cross_links(text: str) -> str:
    """Point Part A traces at Part B / preamble files."""
    repl = [
        (r"\(#constitutional-triad\)", "(core_00_preamble.md#constitutional-triad)"),
        (r"\(#material-stake\)", "(core_00_preamble.md#material-stake)"),
        (r"\(#material-family-orientation\)", "(core_00_preamble.md#material-family-orientation)"),
        (r"\[Chapter 00\]\(#chapter-00-preamble--foundational-requirements\)",
         "[Chapter 00](core_00_preamble.md#chapter-00-preamble--foundational-requirements)"),
        (r"#7-stewardship-and-distributed-understanding",
         "core_01_stewardship_capacity_principles.md#6-stewardship-and-distributed-understanding"),
        (r"#6-shared-system-capacity",
         "core_01_stewardship_capacity_principles.md#8-shared-system-capacity"),
        (r"#814-minimization-of-avoidable-burden",
         "core_01_stewardship_capacity_principles.md#914-minimization-of-avoidable-burden"),
        (r"#91-required-evaluation-factors",
         "core_01_stewardship_capacity_principles.md#101-required-evaluation-factors"),
        (r"#92-incentive-alignment-and-system-capture",
         "core_01_stewardship_capacity_principles.md#7-governance-under-stewardship-discipline"),
        (r"#922-stewardship-and-operator-incentive-alignment",
         "core_01_stewardship_capacity_principles.md#74-stewardship-and-operator-incentive-alignment"),
        (r"#821-preservation-of-epistemic-integrity",
         "core_01_stewardship_capacity_principles.md#921-preservation-of-epistemic-integrity"),
        (r"#822-trust-truth-alignment",
         "core_01_stewardship_capacity_principles.md#922-trust-truth-alignment"),
        (r"#11-prohibition-on-absolute-override",
         "core_01_stewardship_capacity_principles.md#12-prohibition-on-absolute-override"),
        (r"#8-interaction-and-conflict-resolution",
         "core_01_stewardship_capacity_principles.md#9-interaction-and-conflict-resolution"),
        (r"#10-freedom-bounded-agency",
         "core_01_stewardship_capacity_principles.md#11-freedom-bounded-agency"),
    ]
    for old, new in repl:
        text = text.replace(old, new)
    text = text.replace(
        "## CHAPTER 01: PRINCIPLES AND CONSTRAINTS",
        "## CHAPTER 01, PART A: VALUES PRINCIPLES",
    )
    return text


def renumber_old_sec7_to_sec6(text: str) -> str:
    text = text.replace("### 7. Stewardship and Distributed Understanding", "### 6. Stewardship and Distributed Understanding")
    text = text.replace("#7-stewardship-and-distributed-understanding", "#6-stewardship-and-distributed-understanding")
    text = text.replace("<a id=\"7-stewardship-and-distributed-understanding\"></a>", "<a id=\"6-stewardship-and-distributed-understanding\"></a>")
    text = text.replace("#### 7.1 Stewardship", "#### 6.1 Stewardship")
    text = text.replace("#### 7.2 Distributed Understanding", "#### 6.2 Distributed Understanding")
    text = text.replace("#### 7.3 Institutional Development", "#### 6.3 Institutional Development")
    text = text.replace("#### 7.4 Openness Aspiration", "#### 6.4 Openness Aspiration")
    text = text.replace("#### 7.5 Bounds and Rights-Floor Disclaimer", "#### 6.5 Bounds and Rights-Floor Disclaimer")
    text = text.replace("#71-stewardship", "#61-stewardship")
    text = text.replace("#72-distributed-understanding", "#62-distributed-understanding")
    text = text.replace("#73-institutional-development", "#63-institutional-development")
    text = text.replace("#74-openness-aspiration", "#64-openness-aspiration")
    text = text.replace("#75-bounds-and-rights-floor-disclaimer", "#65-bounds-and-rights-floor-disclaimer")
    text = re.sub(r"\[§7 Stewardship", "[§6 Stewardship", text)
    text = re.sub(r"\*\*§7\*\*", "**§6**", text)
    text = re.sub(r"section \*\*7\*\*", "section **6**", text)
    text = re.sub(r"under section \*\*7\*\*", "under section **6**", text)
    text = re.sub(r"\[§7\.", "[§6.", text)
    text = re.sub(r"\*\*§7\.", "**§6.", text)
    text = text.replace("[§6 Shared-System Capacity](#6-shared-system-capacity)", "[§8 Shared-System Capacity](#8-shared-system-capacity)")
    text = text.replace("and [§6 Shared-System Capacity](#6-shared-system-capacity)", "and [§8 Shared-System Capacity](#8-shared-system-capacity)")
    text = text.replace("[8. Interaction and Conflict Resolution](#8-interaction-and-conflict-resolution)", "[9. Interaction and Conflict Resolution](#9-interaction-and-conflict-resolution)")
    text = text.replace("[9.1 Required Evaluation Factors](#91-required-evaluation-factors)", "[10.1 Required Evaluation Factors](#101-required-evaluation-factors)")
    text = text.replace("[10. Freedom (Bounded Agency)](#10-freedom-bounded-agency)", "[11. Freedom (Bounded Agency)](#11-freedom-bounded-agency)")
    text = text.replace("[8.1.4 Minimization of Avoidable Burden](#814-minimization-of-avoidable-burden)", "[9.1.4 Minimization of Avoidable Burden](#914-minimization-of-avoidable-burden)")
    text = text.replace("[7.2.3 Role Depth and Material Responsibility Pathways](#923-role-depth-and-material-responsibility-pathways)",
                        "[7.5 Role Depth and Material Responsibility Pathways](#75-role-depth-and-material-responsibility-pathways)")
    text = text.replace("[3. Foundational Objective: Wellbeing](#3-foundational-objective-wellbeing)",
                        "[3. Foundational Objective: Wellbeing](core_01_values_principles.md#3-foundational-objective-wellbeing)")
    text = text.replace("[4.2 Truth](#42-truth-epistemic-integrity-constraint)",
                        "[4.2 Truth](core_01_values_principles.md#42-truth-epistemic-integrity-constraint)")
    text = text.replace("[5. Trust](#5-system-stability-enabler-trust-coordination-integrity)",
                        "[5. Trust](core_01_values_principles.md#5-system-stability-enabler-trust-coordination-integrity)")
    return text


def renumber_old_sec6_to_sec8(text: str) -> str:
    intro = (
        "*In plain terms: shared systems must keep building real productive capacity — but capacity is something "
        "stewardship and lawful governance produce and preserve, not a license to concentrate power.*\n\n"
        "**§8** states **Shared-System Capacity** as an instrumental outcome downstream of **§6 Stewardship** "
        "and **§7 Governance Under Stewardship Discipline**. Capacity claims fail where they rest on domination, "
        "proxy divergence, irreversible lock-in, or governance that defeats the "
        "[Constitutional Triad](core_00_preamble.md#constitutional-triad).\n\n"
    )
    text = re.sub(
        r"\*In plain terms: shared systems must keep building real productive capacity.*?\n\n",
        intro,
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = text.replace("### 6. Shared-System Capacity", "### 8. Shared-System Capacity")
    text = text.replace("#6-shared-system-capacity", "#8-shared-system-capacity")
    text = text.replace("#### 6.1 Productive Capacity", "#### 8.1 Productive Capacity")
    text = text.replace("#### 6.2 Constitutional Efficiency", "#### 8.2 Constitutional Efficiency")
    text = text.replace("#### 6.3 Concentration Threshold", "#### 8.3 Concentration Threshold")
    text = text.replace("#### 6.4 Pro-Competition and Anti-Domination", "#### 8.4 Pro-Competition and Anti-Domination")
    text = text.replace("#### 6.5 Consolidation Ceiling", "#### 8.5 Consolidation Ceiling")
    text = text.replace("#61-productive-capacity-instrumental-good", "#81-productive-capacity-instrumental-good")
    text = text.replace("#62-constitutional-efficiency", "#82-constitutional-efficiency")
    text = text.replace("#63-concentration-threshold-mechanism-adopter-tunable", "#83-concentration-threshold-mechanism-adopter-tunable")
    text = text.replace("#64-pro-competition-and-anti-domination", "#84-pro-competition-and-anti-domination")
    text = text.replace("#65-consolidation-ceiling", "#85-consolidation-ceiling")
    text = re.sub(r"\*\*§6\*\*", "**§8**", text)
    text = re.sub(r"\[§6\.", "[§8.", text)
    text = re.sub(r"\*\*§6\.", "**§8.", text)
    text = re.sub(r"Chapter One §6\b", "Chapter One §8", text)
    text = re.sub(r"\[Chapter One §6\]", "[Chapter One §8]", text)
    text = text.replace("[8.1.4 Minimization of Avoidable Burden](#814-minimization-of-avoidable-burden)",
                        "[9.1.4 Minimization of Avoidable Burden](#914-minimization-of-avoidable-burden)")
    text = text.replace("[9.2 Incentive Alignment and System Capture](#92-incentive-alignment-and-system-capture)",
                        "[7. Governance Under Stewardship Discipline](#7-governance-under-stewardship-discipline)")
    text = text.replace("[9.2.2 Stewardship and Operator Incentive Alignment](#922-stewardship-and-operator-incentive-alignment)",
                        "[7.4 Stewardship and Operator Incentive Alignment](#74-stewardship-and-operator-incentive-alignment)")
    text = text.replace("[§8 Interaction and Conflict Resolution](#8-interaction-and-conflict-resolution)",
                        "[§9 Interaction and Conflict Resolution](#9-interaction-and-conflict-resolution)")
    text = text.replace("[2. Purpose and Role](#2-purpose-and-role)",
                        "[2. Purpose and Role](core_01_values_principles.md#2-purpose-and-role)")
    text = text.replace("[3. Foundational Objective: Wellbeing](#3-foundational-objective-wellbeing)",
                        "[3. Foundational Objective: Wellbeing](core_01_values_principles.md#3-foundational-objective-wellbeing)")
    text = text.replace("[5. Trust](#5-system-stability-enabler-trust-coordination-integrity)",
                        "[5. Trust](core_01_values_principles.md#5-system-stability-enabler-trust-coordination-integrity)")
    return text


def renumber_old_sec8_to_sec9(text: str) -> str:
    text = text.replace("### 8. Interaction and Conflict Resolution", "### 9. Interaction and Conflict Resolution")
    text = text.replace("#8-interaction-and-conflict-resolution", "#9-interaction-and-conflict-resolution")
    text = text.replace("#### 8.1 Core Tradeoff Principles", "#### 9.1 Core Tradeoff Principles")
    text = text.replace("#### 8.2 Epistemic Disclosure Constraints", "#### 9.2 Epistemic Disclosure Constraints")
    text = text.replace("#### 8.3 Freedom-Limitation Constraints", "#### 9.3 Freedom-Limitation Constraints")
    text = text.replace("#### 8.4 Rights-Collision Procedure", "#### 9.4 Rights-Collision Procedure")
    text = text.replace("#81-core-tradeoff-principles", "#91-core-tradeoff-principles")
    text = text.replace("#82-epistemic-disclosure-constraints", "#92-epistemic-disclosure-constraints")
    text = text.replace("#83-freedom-limitation-constraints", "#93-freedom-limitation-constraints")
    text = text.replace("#84-rights-collision-procedure", "#94-rights-collision-procedure")
    text = text.replace("##### 8.1.1 Proportionality", "##### 9.1.1 Proportionality")
    text = text.replace("##### 8.1.2 Necessity", "##### 9.1.2 Necessity")
    text = text.replace("##### 8.1.3 Minimization of Harm", "##### 9.1.3 Minimization of Harm")
    text = text.replace("##### 8.1.4 Minimization of Avoidable Burden", "##### 9.1.4 Minimization of Avoidable Burden")
    text = text.replace("##### 8.2.1 Preservation of Epistemic Integrity", "##### 9.2.1 Preservation of Epistemic Integrity")
    text = text.replace("##### 8.2.2 Trust-Truth Alignment", "##### 9.2.2 Trust-Truth Alignment")
    text = text.replace("##### 8.3.1 Constraint on Freedom", "##### 9.3.1 Constraint on Freedom")
    text = text.replace("##### 8.3.2 Time-Consistency Constraint", "##### 9.3.2 Time-Consistency Constraint")
    text = text.replace("##### 8.4.1 Rights-Collision Decision Test", "##### 9.4.1 Rights-Collision Decision Test")
    text = text.replace("##### 8.4.2 Proxy-Divergence Invalidation", "##### 9.4.2 Proxy-Divergence Invalidation")
    text = text.replace("#811-proportionality", "#911-proportionality")
    text = text.replace("#812-necessity", "#912-necessity")
    text = text.replace("#813-minimization-of-harm", "#913-minimization-of-harm")
    text = text.replace("#814-minimization-of-avoidable-burden", "#914-minimization-of-avoidable-burden")
    text = text.replace("#821-preservation-of-epistemic-integrity", "#921-preservation-of-epistemic-integrity")
    text = text.replace("#822-trust-truth-alignment", "#922-trust-truth-alignment")
    text = text.replace("#831-constraint-on-freedom", "#931-constraint-on-freedom")
    text = text.replace("#832-time-consistency-constraint", "#932-time-consistency-constraint")
    text = text.replace("#841-rights-collision-decision-test", "#941-rights-collision-decision-test")
    text = text.replace("#842-proxy-divergence-invalidation", "#942-proxy-divergence-invalidation")
    text = re.sub(r"\[§8\]", "[§9]", text)
    text = re.sub(r"\*\*§8\.", "**§9.", text)
    text = re.sub(r"\[§8\.", "[§9.", text)
    text = text.replace("[§7 Stewardship and Distributed Understanding](#7-stewardship-and-distributed-understanding)",
                        "[§6 Stewardship and Distributed Understanding](#6-stewardship-and-distributed-understanding)")
    text = text.replace("[9. Freedom](#10-freedom-bounded-agency)", "[11. Freedom](#11-freedom-bounded-agency)")
    text = text.replace("[11. Prohibition on Absolute Override](#11-prohibition-on-absolute-override)",
                        "[12. Prohibition on Absolute Override](#12-prohibition-on-absolute-override)")
    text = text.replace("[7.2.1 Preservation of Epistemic Integrity](#821-preservation-of-epistemic-integrity)",
                        "[9.2.1 Preservation of Epistemic Integrity](#921-preservation-of-epistemic-integrity)")
    text = text.replace("[§9.2.2 Stewardship and Operator Incentive Alignment](#922-stewardship-and-operator-incentive-alignment)",
                        "[§7.4 Stewardship and Operator Incentive Alignment](#74-stewardship-and-operator-incentive-alignment)")
    return text


def renumber_old_sec92_to_sec7(text: str) -> str:
    text = re.sub(r"^#### 9\.2 Incentive Alignment and System Capture\n", "", text, count=1, flags=re.MULTILINE)
    text = text.replace("##### 9.2.1 Alignment Requirement", "#### 7.3 Alignment Requirement")
    text = text.replace("##### 9.2.2 Stewardship and Operator Incentive Alignment", "#### 7.4 Stewardship and Operator Incentive Alignment")
    text = text.replace("##### 9.2.3 Role Depth and Material Responsibility Pathways", "#### 7.5 Role Depth and Material Responsibility Pathways")
    text = text.replace("##### 9.2.4 Misalignment Correction and Capture Response", "#### 7.6 Misalignment Correction and Capture Response")
    text = text.replace("##### 9.2.5 Contingent claims, games of chance, and event-contract markets",
                        "#### 7.7 Contingent claims, games of chance, and event-contract markets")
    text = text.replace("#921-alignment-requirement", "#73-alignment-requirement")
    text = text.replace("#922-stewardship-and-operator-incentive-alignment", "#74-stewardship-and-operator-incentive-alignment")
    text = text.replace("#923-role-depth-and-material-responsibility-pathways", "#75-role-depth-and-material-responsibility-pathways")
    text = text.replace("#924-misalignment-correction-and-capture-response", "#76-misalignment-correction-and-capture-response")
    text = text.replace("#925-contingent-claims-games-of-chance-and-event-contract-markets", "#77-contingent-claims-games-of-chance-and-event-contract-markets")
    text = text.replace("[§9.2.1](#921-alignment-requirement)", "[§7.3](#73-alignment-requirement)")
    text = text.replace("[§9.2.4](#924-misalignment-correction-and-capture-response)", "[§7.6](#76-misalignment-correction-and-capture-response)")
    text = text.replace("[§9.1 Required Evaluation Factors](#91-required-evaluation-factors)",
                        "[10.1 Required Evaluation Factors](#101-required-evaluation-factors)")
    text = text.replace("[§7 Stewardship and Distributed Understanding](#7-stewardship-and-distributed-understanding)",
                        "[§6 Stewardship and Distributed Understanding](#6-stewardship-and-distributed-understanding)")
    text = text.replace("[9. Freedom](#10-freedom-bounded-agency)", "[11. Freedom](#11-freedom-bounded-agency)")
    text = text.replace("[11. Prohibition on Absolute Override](#11-prohibition-on-absolute-override)",
                        "[12. Prohibition on Absolute Override](#12-prohibition-on-absolute-override)")
    text = text.replace("[§8.1.4 Minimization of Avoidable Burden](#814-minimization-of-avoidable-burden)",
                        "[§9.1.4 Minimization of Avoidable Burden](#914-minimization-of-avoidable-burden)")
    text = text.replace("**[§7 Stewardship and Distributed Understanding](#7-stewardship-and-distributed-understanding)**",
                        "**[§6 Stewardship and Distributed Understanding](#6-stewardship-and-distributed-understanding)**")
    text = text.replace("Chapter Eleven, section 6 —", "Chapter Eleven, section 5 —")
    return text


def renumber_old_sec91_to_sec10(text: str, sec9_intro: str) -> str:
    intro = sec9_intro
    intro = intro.replace("### 9. Systemic Evaluation Requirement", "### 10. Systemic Evaluation Requirement")
    intro = intro.replace("#9-systemic-evaluation-requirement", "#10-systemic-evaluation-requirement")
    intro = intro.replace("**Section 8**", "**Section 9**")
    intro = intro.replace("**Section 9**", "**Section 10**")
    intro = intro.replace("[§9.1 Required Evaluation Factors](#91-required-evaluation-factors)", "[§10.1 Required Evaluation Factors](#101-required-evaluation-factors)")
    intro = intro.replace("[§9.2 Incentive Alignment and System Capture](#92-incentive-alignment-and-system-capture)",
                          "[§7 Governance Under Stewardship Discipline](#7-governance-under-stewardship-discipline)")
    intro = intro.replace("**§§6–9**", "**§§6–10**")
    intro = intro.replace("under **§8**", "under **§9**")
    intro = intro.replace("fail **§9**", "fail **§10**")
    intro = intro.replace("**§9** verifies", "**§10** verifies")
    intro = re.sub(r"\*\*§9\.1–§9\.2\*\*.*?\n\n", "", intro, count=1, flags=re.DOTALL)

    body = text
    body = body.replace("#### 9.1 Required Evaluation Factors", "#### 10.1 Required Evaluation Factors")
    body = body.replace("#91-required-evaluation-factors", "#101-required-evaluation-factors")
    body = body.replace("##### 9.1.1 Systemic Scope", "##### 10.1.1 Systemic Scope")
    body = body.replace("##### 9.1.2 Accessibility Under Sentience Non-Exclusion", "##### 10.1.2 Accessibility Under Sentience Non-Exclusion")
    body = body.replace("##### 9.1.3 Privacy (Informational) Joint Invocation", "##### 10.1.3 Privacy (Informational) Joint Invocation")
    body = body.replace("##### 9.1.4 Voluntary Discontinuation and Exit Rights", "##### 10.1.4 Voluntary Discontinuation and Exit Rights")
    body = body.replace("##### 9.1.5 Assembly, Collective Organization, and Institutional Formation",
                        "##### 10.1.5 Assembly, Collective Organization, and Institutional Formation")
    body = body.replace("#911-systemic-scope-and-risk-factors", "#1011-systemic-scope-and-risk-factors")
    body = body.replace("#912-accessibility-under-sentience-non-exclusion", "#1012-accessibility-under-sentience-non-exclusion")
    body = body.replace("#913-privacy-informational-joint-invocation", "#1013-privacy-informational-joint-invocation")
    body = body.replace("#914-voluntary-discontinuation-and-exit-rights", "#1014-voluntary-discontinuation-and-exit-rights")
    body = body.replace("#915-assembly-collective-organization-and-institutional-formation", "#1015-assembly-collective-organization-and-institutional-formation")
    body = body.replace("[§7 Stewardship and Distributed Understanding](#7-stewardship-and-distributed-understanding)",
                        "[§6 Stewardship and Distributed Understanding](#6-stewardship-and-distributed-understanding)")
    body = body.replace("[8. Interaction and Conflict Resolution](#8-interaction-and-conflict-resolution)",
                        "[9. Interaction and Conflict Resolution](#9-interaction-and-conflict-resolution)")
    body = body.replace("[9.2 Incentive Alignment and System Capture](#92-incentive-alignment-and-system-capture)",
                        "[7. Governance Under Stewardship Discipline](#7-governance-under-stewardship-discipline)")
    body = body.replace("[9. Freedom](#10-freedom-bounded-agency)", "[11. Freedom](#11-freedom-bounded-agency)")
    body = body.replace("[11. Prohibition on Absolute Override](#11-prohibition-on-absolute-override)",
                        "[12. Prohibition on Absolute Override](#12-prohibition-on-absolute-override)")
    body = body.replace("[12. Integrated Application](#12-integrated-application)",
                        "[13. Integrated Application](#13-integrated-application)")
    body = re.sub(r"\[§9\.1\.", "[§10.1.", body)
    body = re.sub(r"#91([0-9])", r"#101\1", body)
    return intro + body + PART_B_SEC10_POINTER


def renumber_old_sec10_to_sec11(text: str) -> str:
    text = text.replace("### 10. Freedom (Bounded Agency)", "### 11. Freedom (Bounded Agency)")
    text = text.replace("#10-freedom-bounded-agency", "#11-freedom-bounded-agency")
    text = text.replace("[§6 Shared-System Capacity](#6-shared-system-capacity)", "[§8 Shared-System Capacity](#8-shared-system-capacity)")
    text = text.replace("[§7 Stewardship and Distributed Understanding](#7-stewardship-and-distributed-understanding)",
                        "[§6 Stewardship and Distributed Understanding](#6-stewardship-and-distributed-understanding)")
    text = text.replace("[8. Interaction and Conflict Resolution](#8-interaction-and-conflict-resolution)",
                        "[9. Interaction and Conflict Resolution](#9-interaction-and-conflict-resolution)")
    text = text.replace("[9. Systemic Evaluation Requirement](#9-systemic-evaluation-requirement)",
                        "[10. Systemic Evaluation Requirement](#10-systemic-evaluation-requirement)")
    text = text.replace("[11. Prohibition on Absolute Override](#11-prohibition-on-absolute-override)",
                        "[12. Prohibition on Absolute Override](#12-prohibition-on-absolute-override)")
    text = text.replace("[12. Integrated Application](#12-integrated-application)",
                        "[13. Integrated Application](#13-integrated-application)")
    text = text.replace("[8.4.1 Rights-Collision Decision Test](#841-rights-collision-decision-test)",
                        "[9.4.1 Rights-Collision Decision Test](#941-rights-collision-decision-test)")
    return text


def renumber_old_sec11_to_sec12(text: str) -> str:
    text = text.replace("### 11. Prohibition on Absolute Override", "### 12. Prohibition on Absolute Override")
    text = text.replace("#11-prohibition-on-absolute-override", "#12-prohibition-on-absolute-override")
    text = text.replace("[§7 Stewardship and Distributed Understanding](#7-stewardship-and-distributed-understanding)",
                        "[§6 Stewardship and Distributed Understanding](#6-stewardship-and-distributed-understanding)")
    text = text.replace("[8. Interaction and Conflict Resolution](#8-interaction-and-conflict-resolution)",
                        "[9. Interaction and Conflict Resolution](#9-interaction-and-conflict-resolution)")
    text = text.replace("[9. Freedom](#10-freedom-bounded-agency)", "[11. Freedom](#11-freedom-bounded-agency)")
    text = text.replace("[12. Integrated Application](#12-integrated-application)",
                        "[13. Integrated Application](#13-integrated-application)")
    return text


def renumber_old_sec12_to_sec13(text: str) -> str:
    text = text.replace("### 12. Integrated Application", "### 13. Integrated Application")
    text = text.replace("#12-integrated-application", "#13-integrated-application")
    text = text.replace("[§7 Stewardship and Distributed Understanding](#7-stewardship-and-distributed-understanding)",
                        "[§6 Stewardship and Distributed Understanding](#6-stewardship-and-distributed-understanding)")
    text = text.replace("[8. Interaction and Conflict Resolution](#8-interaction-and-conflict-resolution)",
                        "[9. Interaction and Conflict Resolution](#9-interaction-and-conflict-resolution)")
    text = text.replace("[9.1 Required Evaluation Factors](#91-required-evaluation-factors)",
                        "[10.1 Required Evaluation Factors](#101-required-evaluation-factors)")
    text = text.replace("[9. Freedom](#10-freedom-bounded-agency)", "[11. Freedom](#11-freedom-bounded-agency)")
    text = text.replace("[11. Prohibition on Absolute Override](#11-prohibition-on-absolute-override)",
                        "[12. Prohibition on Absolute Override](#12-prohibition-on-absolute-override)")
    text = text.replace("[1. Constitutional Interpretation](#1-constitutional-interpretation)",
                        "[1. Constitutional Interpretation](core_01_values_principles.md#1-constitutional-interpretation)")
    text = text.replace("[2. Purpose and Role](#2-purpose-and-role)",
                        "[2. Purpose and Role](core_01_values_principles.md#2-purpose-and-role)")
    text = text.replace("[Chapter 00](#chapter-00-preamble--foundational-requirements)",
                        "[Chapter 00](core_00_preamble.md#chapter-00-preamble--foundational-requirements)")
    text = text.replace("[§8 Interaction and Conflict Resolution](#8-interaction-and-conflict-resolution)",
                        "[§9 Interaction and Conflict Resolution](#9-interaction-and-conflict-resolution)")
    text = text.replace("**§§6–9**", "**§§6–10**")
    return text


def fix_part_b_global(text: str) -> str:
  text = text.replace("(#constitutional-triad)", "(core_00_preamble.md#constitutional-triad)")
  text = text.replace("(#material-stake)", "(core_00_preamble.md#material-stake)")
  text = text.replace("(#two-constitutional-aims)", "(core_01_values_principles.md#two-constitutional-aims)")
  text = text.replace("(#flourishing)", "(core_01_values_principles.md#flourishing)")
  text = text.replace("(#continuity)", "(core_01_values_principles.md#continuity)")
  text = text.replace(
      "[material stake](core_00_preamble.md#material-stake)",
      "[material stake](core_00_preamble.md#material-stake)",
  )
  text = text.replace(
      "[Constitutional Triad](core_00_preamble.md#constitutional-triad)",
      "[Constitutional Triad](core_00_preamble.md#constitutional-triad)",
  )
  text = text.replace(
      "[Two Constitutional Aims](core_01_values_principles.md#two-constitutional-aims)",
      "[Two Constitutional Aims](core_01_values_principles.md#two-constitutional-aims)",
  )
  return text


def build_part_b(lines: list[str]) -> str:
    sec_old_7 = slice_lines(lines, 874, 1068)
    sec_old_92 = slice_lines(lines, 1520, 1688)
    sec_old_6 = slice_lines(lines, 659, 871)  # includes arc paragraph + §6
    sec_old_8 = slice_lines(lines, 1070, 1411)
    sec_old_9_intro = slice_lines(lines, 1413, 1424)
    sec_old_91 = slice_lines(lines, 1425, 1518)
    sec_old_10 = slice_lines(lines, 1690, 1734)
    sec_old_11 = slice_lines(lines, 1736, 1767)
    sec_old_12 = slice_lines(lines, 1769, 1808)
    vocab = slice_lines(lines, 1810, 1830)

    # Remove duplicate arc from sec_old_6 (lines 659-665) - use Part B header arc instead
    sec_old_6 = re.sub(
        r"\*In plain terms: shared systems must keep building.*?\n\nRead together with the sections that follow.*?\n\n",
        "",
        sec_old_6,
        count=1,
        flags=re.DOTALL,
    )

    sec6 = renumber_old_sec7_to_sec6(sec_old_7)
    sec7 = PART_B_SEC7_FRAMING + renumber_old_sec92_to_sec7(sec_old_92)
    sec8 = renumber_old_sec6_to_sec8(sec_old_6)
    sec9 = renumber_old_sec8_to_sec9(sec_old_8)
    sec10 = renumber_old_sec91_to_sec10(sec_old_91, sec_old_9_intro)
    sec11 = renumber_old_sec10_to_sec11(sec_old_10)
    sec12 = renumber_old_sec11_to_sec12(sec_old_11)
    sec13 = renumber_old_sec12_to_sec13(sec_old_12)

    body = "\n".join([sec6, sec7, sec8, sec9, sec10, sec11, sec12, sec13, vocab])
    body = fix_part_b_global(body)
    body = body.replace(
        "**Next file:** [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md)",
        "",
    )
    return PART_B_HEADER + LEGACY_ANCHORS + "\n" + body + "\n---\n\n**Next file:** [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md)\n"


def main() -> int:
    if not SOURCE.exists():
        print(f"Missing source: {SOURCE}", file=sys.stderr)
        return 1

    lines = SOURCE.read_text(encoding="utf-8").splitlines(keepends=True)

    preamble = PREAMBLE_HEADER + fix_preamble_links(slice_lines(lines, 6, 45))
    values = VALUES_HEADER + fix_values_cross_links(slice_lines(lines, 48, 631))
    part_b = build_part_b(lines)

    (ROOT / "core_00_preamble.md").write_text(preamble, encoding="utf-8")
    (ROOT / "core_01_values_principles.md").write_text(values, encoding="utf-8")
    (ROOT / "core_01_stewardship_capacity_principles.md").write_text(part_b, encoding="utf-8")
    SOURCE.write_text(STUB_CONTENT, encoding="utf-8")

    print("Wrote core_00_preamble.md")
    print("Wrote core_01_values_principles.md")
    print("Wrote core_01_stewardship_capacity_principles.md")
    print("Replaced core_00-01_principles.md with redirect stub")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
