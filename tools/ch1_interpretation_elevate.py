#!/usr/bin/env python3
"""Elevate Chapter One interpretive front matter to §1; renumber §1–§10 → §2–§11."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Apply deepest-first so 6.1.1 does not become 7.1.1 then 8.1.1.
HEADER_RENUMBER: list[tuple[str, str]] = [
    ("##### 7.2.5 ", "##### 8.2.5 "),
    ("##### 7.2.4 ", "##### 8.2.4 "),
    ("##### 7.2.3 ", "##### 8.2.3 "),
    ("##### 7.2.2 ", "##### 8.2.2 "),
    ("##### 7.2.1 ", "##### 8.2.1 "),
    ("##### 7.1.5 ", "##### 8.1.5 "),
    ("##### 7.1.4 ", "##### 8.1.4 "),
    ("##### 7.1.3 ", "##### 8.1.3 "),
    ("##### 7.1.2 ", "##### 8.1.2 "),
    ("##### 7.1.1 ", "##### 8.1.1 "),
    ("##### 6.4.2 ", "##### 7.4.2 "),
    ("##### 6.4.1 ", "##### 7.4.1 "),
    ("##### 6.3.2 ", "##### 7.3.2 "),
    ("##### 6.3.1 ", "##### 7.3.1 "),
    ("##### 6.2.2 ", "##### 7.2.2 "),
    ("##### 6.2.1 ", "##### 7.2.1 "),
    ("##### 6.1.4 ", "##### 7.1.4 "),
    ("##### 6.1.3 ", "##### 7.1.3 "),
    ("##### 6.1.2 ", "##### 7.1.2 "),
    ("##### 6.1.1 ", "##### 7.1.1 "),
    ("##### 5.2.5 ", "##### 6.2.5 "),
    ("##### 5.2.4 ", "##### 6.2.4 "),
    ("##### 5.2.3 ", "##### 6.2.3 "),
    ("##### 5.2.2 ", "##### 6.2.2 "),
    ("##### 5.2.1 ", "##### 6.2.1 "),
    ("##### 5.1.5 ", "##### 6.1.5 "),
    ("##### 5.1.4 ", "##### 6.1.4 "),
    ("##### 5.1.3 ", "##### 6.1.3 "),
    ("##### 5.1.2 ", "##### 6.1.2 "),
    ("##### 5.1.1 ", "##### 6.1.1 "),
    ("#### 7.2 ", "#### 8.2 "),
    ("#### 7.1 ", "#### 8.1 "),
    ("#### 6.4 ", "#### 7.4 "),
    ("#### 6.3 ", "#### 7.3 "),
    ("#### 6.2 ", "#### 7.2 "),
    ("#### 6.1 ", "#### 7.1 "),
    ("#### 5.2 ", "#### 6.2 "),
    ("#### 5.1 ", "#### 6.1 "),
    ("#### 4.1 ", "#### 5.1 "),
    ("#### 3.4 ", "#### 4.4 "),
    ("#### 3.3 ", "#### 4.3 "),
    ("#### 3.2 ", "#### 4.2 "),
    ("#### 3.1 ", "#### 4.1 "),
    ("#### 2.2 ", "#### 3.2 "),
    ("#### 2.1 ", "#### 3.1 "),
    ("### 11. Integrated Application", "### 11. Integrated Application"),
    ("### 9. Prohibition on Absolute Override", "### 10. Prohibition on Absolute Override"),
    ("### 8. Freedom (Bounded Agency)", "### 9. Freedom (Bounded Agency)"),
    ("### 7. Systemic Evaluation Requirement", "### 8. Systemic Evaluation Requirement"),
    ("### 6. Interaction and Conflict Resolution", "### 7. Interaction and Conflict Resolution"),
    ("### 5. Shared-System Capacity and Stewardship", "### 6. Shared-System Capacity and Stewardship"),
    ("### 4. System Stability Enabler: Trust (Coordination Integrity)", "### 5. System Stability Enabler: Trust (Coordination Integrity)"),
    ("### 3. Non-Negotiable Constraints: Safety and Truth", "### 4. Non-Negotiable Constraints: Safety and Truth"),
    ("### 2. Foundational Objective: Wellbeing", "### 3. Foundational Objective: Wellbeing"),
    ("### 1. Purpose and Role", "### 2. Purpose and Role"),
]

# Anchor slug rewrites inside core_00-01_principles.md links (deepest first).
ANCHOR_MAP: list[tuple[str, str]] = [
    ("#825-contingent-claims-games-of-chance-and-event-contract-markets", "#825-contingent-claims-games-of-chance-and-event-contract-markets"),
    ("#824-misalignment-correction-and-capture-response", "#824-misalignment-correction-and-capture-response"),
    ("#823-role-depth-and-material-responsibility-pathways", "#823-role-depth-and-material-responsibility-pathways"),
    ("#822-stewardship-and-operator-incentive-alignment", "#822-stewardship-and-operator-incentive-alignment"),
    ("#821-alignment-requirement", "#821-alignment-requirement"),
    ("#815-assembly-collective-organization-and-institutional-formation", "#815-assembly-collective-organization-and-institutional-formation"),
    ("#814-voluntary-discontinuation-and-exit-rights", "#814-voluntary-discontinuation-and-exit-rights"),
    ("#813-privacy-informational-joint-invocation", "#813-privacy-informational-joint-invocation"),
    ("#812-accessibility-under-sentience-non-exclusion", "#812-accessibility-under-sentience-non-exclusion"),
    ("#811-systemic-scope-and-risk-factors", "#811-systemic-scope-and-risk-factors"),
    ("#742-proxy-divergence-invalidation", "#742-proxy-divergence-invalidation"),
    ("#741-rights-collision-decision-test", "#741-rights-collision-decision-test"),
    ("#732-time-consistency-constraint", "#732-time-consistency-constraint"),
    ("#731-constraint-on-freedom", "#731-constraint-on-freedom"),
    ("#722-trust-truth-alignment", "#722-trust-truth-alignment"),
    ("#721-preservation-of-epistemic-integrity", "#721-preservation-of-epistemic-integrity"),
    ("#714-minimization-of-avoidable-burden", "#714-minimization-of-avoidable-burden"),
    ("#713-minimization-of-harm", "#713-minimization-of-harm"),
    ("#712-necessity", "#712-necessity"),
    ("#711-proportionality", "#711-proportionality"),
    ("#625-bounds-and-rights-floor-disclaimer", "#625-bounds-and-rights-floor-disclaimer"),
    ("#624-openness-aspiration", "#624-openness-aspiration"),
    ("#623-institutional-development", "#623-institutional-development"),
    ("#622-distributed-understanding", "#622-distributed-understanding"),
    ("#621-stewardship", "#621-stewardship"),
    ("#615-consolidation-ceiling", "#615-consolidation-ceiling"),
    ("#614-pro-competition-and-anti-domination", "#614-pro-competition-and-anti-domination"),
    ("#613-concentration-threshold-mechanism-adopter-tunable", "#613-concentration-threshold-mechanism-adopter-tunable"),
    ("#612-constitutional-efficiency", "#612-constitutional-efficiency"),
    ("#611-productive-capacity-instrumental-good", "#611-productive-capacity-instrumental-good"),
    ("#11-integrated-application", "#11-integrated-application"),
    ("#10-prohibition-on-absolute-override", "#10-prohibition-on-absolute-override"),
    ("#9-freedom-bounded-agency", "#9-freedom-bounded-agency"),
    ("#8-systemic-evaluation-requirement", "#8-systemic-evaluation-requirement"),
    ("#82-incentive-alignment-and-system-capture", "#82-incentive-alignment-and-system-capture"),
    ("#81-required-evaluation-factors", "#81-required-evaluation-factors"),
    ("#7-interaction-and-conflict-resolution", "#7-interaction-and-conflict-resolution"),
    ("#73-freedom-limitation-constraints", "#73-freedom-limitation-constraints"),
    ("#72-epistemic-disclosure-constraints", "#72-epistemic-disclosure-constraints"),
    ("#71-core-tradeoff-principles", "#71-core-tradeoff-principles"),
    ("#74-rights-collision-procedure", "#74-rights-collision-procedure"),
    ("#6-shared-system-capacity-and-stewardship", "#6-shared-system-capacity-and-stewardship"),
    ("#62-stewardship-and-distributed-understanding", "#62-stewardship-and-distributed-understanding"),
    ("#61-shared-system-capacity", "#61-shared-system-capacity"),
    ("#5-system-stability-enabler-trust-coordination-integrity", "#5-system-stability-enabler-trust-coordination-integrity"),
    ("#51-resilience-and-self-healing-design", "#51-resilience-and-self-healing-design"),
    ("#4-non-negotiable-constraints-safety-and-truth", "#4-non-negotiable-constraints-safety-and-truth"),
    ("#44-plain-language-accessibility-stewardship-duty", "#44-plain-language-accessibility-stewardship-duty"),
    ("#43-science-informed-inquiry-and-decision-support", "#43-science-informed-inquiry-and-decision-support"),
    ("#42-truth-epistemic-integrity-constraint", "#42-truth-epistemic-integrity-constraint"),
    ("#41-safety-harm-constraint", "#41-safety-harm-constraint"),
    ("#3-foundational-objective-wellbeing", "#3-foundational-objective-wellbeing"),
    ("#32-recognition-reinforcement-and-aspiration", "#32-recognition-reinforcement-and-aspiration"),
    ("#31-fairness", "#31-fairness"),
    ("#2-purpose-and-role", "#2-purpose-and-role"),
    ("#12-canonical-conflict-resolution-procedure", "#12-canonical-conflict-resolution-procedure"),
    ("#1-constitutional-interpretation", "#1-constitutional-interpretation"),
]

# Display labels in link text and prose (order: longest / most specific first).
LABEL_MAP: list[tuple[str, str]] = [
    ("[11. Integrated Application]", "[11. Integrated Application]"),
    ("11. Integrated Application", "11. Integrated Application"),
    ("[10. Prohibition on Absolute Override]", "[10. Prohibition on Absolute Override]"),
    ("[9. Freedom (Bounded Agency)]", "[9. Freedom (Bounded Agency)]"),
    ("[9. Freedom]", "[9. Freedom]"),
    ("§9 Freedom", "§9 Freedom"),
    ("[8. Systemic Evaluation Requirement]", "[8. Systemic Evaluation Requirement]"),
    ("[8.1 Required Evaluation Factors]", "[8.1 Required Evaluation Factors]"),
    ("[8.2 Incentive Alignment and System Capture]", "[8.2 Incentive Alignment and System Capture]"),
    ("[7. Interaction and Conflict Resolution]", "[7. Interaction and Conflict Resolution]"),
    ("[7.4 Rights-Collision Procedure]", "[7.4 Rights-Collision Procedure]"),
    ("[7.4.1 Rights-Collision Decision Test]", "[7.4.1 Rights-Collision Decision Test]"),
    ("[7.3 Freedom-Limitation Constraints]", "[7.3 Freedom-Limitation Constraints]"),
    ("[7.2 Epistemic Disclosure Constraints]", "[7.2 Epistemic Disclosure Constraints]"),
    ("[7.1 Core Tradeoff Principles]", "[7.1 Core Tradeoff Principles]"),
    ("[7.1.1 Proportionality]", "[7.1.1 Proportionality]"),
    ("[7.1.2 Necessity]", "[7.1.2 Necessity]"),
    ("[7.1.4 Minimization of Avoidable Burden]", "[7.1.4 Minimization of Avoidable Burden]"),
    ("[6. Shared-System Capacity and Stewardship]", "[6. Shared-System Capacity and Stewardship]"),
    ("[§6.2 Stewardship and Distributed Understanding]", "[§6.2 Stewardship and Distributed Understanding]"),
    ("§6.2 Stewardship", "§6.2 Stewardship"),
    ("[§6.1 Shared-System Capacity]", "[§6.1 Shared-System Capacity]"),
    ("[§6.1.1 Productive Capacity (Instrumental Good)]", "[§6.1.1 Productive Capacity (Instrumental Good)]"),
    ("[5. System Stability Enabler: Trust]", "[5. System Stability Enabler: Trust]"),
    ("[5. Trust]", "[5. Trust]"),
    ("[4. Non-Negotiable Constraints: Safety and Truth]", "[4. Non-Negotiable Constraints: Safety and Truth]"),
    ("[4.2 Truth]", "[4.2 Truth]"),
    ("[4.1 Safety]", "[4.1 Safety]"),
    ("[3. Foundational Objective: Wellbeing]", "[3. Foundational Objective: Wellbeing]"),
    ("[§3.2 Recognition, Reinforcement, and Aspiration]", "[§3.2 Recognition, Reinforcement, and Aspiration]"),
    ("[3.1 Fairness]", "[3.1 Fairness]"),
    ("[2. Purpose and Role]", "[2. Purpose and Role]"),
    ("Chapter One — §1 Constitutional Interpretation", "Chapter One — §1 Constitutional Interpretation"),
    ("[1. Constitutional Interpretation]", "[1. Constitutional Interpretation]"),
    ("§1 Constitutional Interpretation", "§1 Constitutional Interpretation"),
    ("**§1 Constitutional Interpretation**", "**§1 Constitutional Interpretation**"),
]

SECTION_PROSE: list[tuple[str, str]] = [
    ("Chapter One, section 21", "Chapter One, section 21"),
    ("Chapter One, section 20", "Chapter One, section 21"),
    ("Chapter One, section 9", "Chapter One, section 20"),
    ("Chapter One, section 8", "Chapter One, section 9"),
    ("Chapter One, section 7", "Chapter One, section 8"),
    ("Chapter One, section 6", "Chapter One, section 7"),
    ("Chapter One, section 5", "Chapter One, section 6"),
    ("Chapter One, section 4", "Chapter One, section 5"),
    ("Chapter One, section 3", "Chapter One, section 4"),
    ("Chapter One, section 2", "Chapter One, section 3"),
    ("Chapter One §11", "Chapter One §11"),
    ("Chapter One §10", "Chapter One §11"),
    ("Chapter One §9", "Chapter One §10"),
    ("Chapter One §8", "Chapter One §9"),
    ("Chapter One §7", "Chapter One §8"),
    ("Chapter One §6", "Chapter One §7"),
    ("Chapter One §5", "Chapter One §6"),
    ("Chapter One §4", "Chapter One §5"),
    ("Chapter One §3", "Chapter One §4"),
    ("section 11 —", "section 11 —"),
    ("section 10 —", "section 11 —"),
    ("section 9 —", "section 10 —"),
    ("section 8 —", "section 9 —"),
    ("section 7.4.2", "section 7.4.2"),
    ("section 7.4.1", "section 7.4.1"),
    ("section 7.4", "section 7.4"),
    ("section 7.3", "section 7.3"),
    ("section 7.2", "section 7.2"),
    ("section 7.1.4", "section 7.1.4"),
    ("section 7.1", "section 7.1"),
    ("section 7 —", "section 8 —"),
    ("section 6.2", "section 7.2"),
    ("section 6.1", "section 7.1"),
    ("section 6 —", "section 7 —"),
    ("Section 8 answers", "Section 8 answers"),
    ("Section 7 tells", "Section 7 tells"),
    ("Section 8.", "Section 8."),
    ("Section 8.", "Section 8."),
    ("**§6.2**", "**§6.2**"),
    ("**§6.1**", "**§6.1**"),
    ("§6.2.1", "§6.2.1"),
    ("§6.2", "§6.2"),
    ("§6.1.5", "§6.1.5"),
    ("§6.1", "§6.1"),
    ("§3.2", "§3.2"),
]

NEW_SECTION_ONE = '''### 1. Constitutional Interpretation
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [Chapter 00 — Constitutional Triad](#constitutional-triad); [material stake](#material-stake) scaling applies chapter-wide through section traces.
- Downstream: [2. Purpose and Role](#2-purpose-and-role) through [11. Integrated Application](#11-integrated-application); [7. Interaction and Conflict Resolution](#7-interaction-and-conflict-resolution) for value-collision procedure; [Chapter Ten: Foundational Rights](core_10-10_rights_part_a.md#chapter-ten-foundational-rights) non-contraction default.
- Read with: [Chapters Two through Four](core_02-04_definition_mechanics.md) and [Chapter Five](core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) — interpretive and evidentiary layer for every term in this chapter.
- Read with: [Chapter Fifteen §2](core_15-15_incorporation.md#2-authority-stack-and-invocation) (*Conflict order* / strictest-applicable incorporated text).
- Read with: [Article XXII: Constitutional Interpretation, Review, and Anti-Capture Safeguards](core_10-10_rights_part_c.md#article-xxii-constitutional-interpretation-review-and-anti-capture-safeguards) for institutional interpretation safeguards (not a substitute for this section).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definitions · Evaluation · Compliance</span></strong></summary>

- [Corpus](core_05-05_definitions_c_dependent_clusters.md#corpus) · [O](core_05-05_definitions_c_dependent_clusters.md#corpus) · [E](core_05-05_definitions_c_dependent_clusters.md#corpus-e) · [C](core_05-05_definitions_c_dependent_clusters.md#corpus-c)
- [Authority Stack and Internal Hierarchy](core_05-05_definitions_c_dependent_clusters.md#authority-stack) · [O](core_05-05_definitions_c_dependent_clusters.md#authority-stack) · [E](core_05-05_definitions_c_dependent_clusters.md#authority-stack-e) · [C](core_05-05_definitions_c_dependent_clusters.md#authority-stack-c)
- [Supremacy and Enforceability](core_05-05_definitions_c_dependent_clusters.md#supremacy-and-enforceability) · [O](core_05-05_definitions_c_dependent_clusters.md#supremacy-and-enforceability) · [E](core_05-05_definitions_c_dependent_clusters.md#supremacy-and-enforceability-e) · [C](core_05-05_definitions_c_dependent_clusters.md#supremacy-and-enforceability-c)
- [Proportionality](core_05-05_definitions_a_independent.md#proportionality) · [O](core_05-05_definitions_a_independent.md#proportionality) · [E](core_05-05_definitions_a_independent.md#proportionality-e) · [C](core_05-05_definitions_a_independent.md#proportionality-c)
- [Necessity](core_05-05_definitions_a_independent.md#necessity) · [O](core_05-05_definitions_a_independent.md#necessity) · [E](core_05-05_definitions_a_independent.md#necessity-e) · [C](core_05-05_definitions_a_independent.md#necessity-c)

</details>

<br>

*In plain terms: read this Constitution as one whole. Chapter One states values and limits, but those words only count when read with the definition and evidence rules in Chapters Two through Five. If a passage could be read more than one way, choose the reading that best protects sentients and the Constitution as a whole — favoring stability, minimized irreversible harm, truthful understanding, and meaningful agency — not the reading that is merely strictest or most restrictive on paper. Rights in Chapter Ten may not be narrowed unless this Constitution clearly allows it.*

#### 1.1 Integrated reading and ambiguity

**Chapters Two through Five** govern the meaning, evaluation, and satisfaction conditions of all terms and constraints used in Chapter One. They operate as the **interpretive and evidentiary layer**; they do **not** operate as a competing substantive layer.

No interpretation of Chapter One is valid outside the definitions and evaluation constraints established in **Chapters Two through Five**. Every application must also preserve and apply:
- **proportionality**, **necessity**, and **systemic evaluation**
- **Chapter Four** evidentiary and traceability requirements
- **Chapter Three** anti-evasion discipline
- **Chapter One**, section 8 — Interaction and Conflict Resolution, including rights-collision handling under section 7.4 where materially relevant

Where Chapter One is ambiguous, interpreters must choose the reading that best preserves two things at once: the Constitution's **fullest protective effect as an integrated whole**, and its constitutional objective of aligning shared systems with sentient wellbeing. They must not resolve ambiguity by preferring **maximal restriction** or **abstract strictness** in isolation. Where **Chapter Ten** rights are implicated, interpreters must **not** resolve ambiguity by readings that **contract** those protections, except where **Chapter One** interaction rules and applicable definitions **expressly** permit.

Where ambiguity remains after integrated reading, interpretation must also favor:
- preservation of systemic stability
- minimization of irreversible harm
- maintenance of truthfulness and reliable understanding
- protection of meaningful agency consistent with system conditions

**Internal hierarchy (last-resort rule).** Within the binding constitutional source, **Chapter One principles** govern high-level constitutional direction. **Article-level obligations and Rights Floors** govern specific operative requirements. The canonical statement of this rule — including its boundary with source-layer authority and its application to adopters under **Chapter Twelve §3.1** — lives in the [Authority Stack and Internal Hierarchy](core_05-05_definitions_c_dependent_clusters.md#authority-stack) cluster in Chapter Five.

If a genuine incompatibility remains after reading the Constitution as an integrated whole:
- principles control over articles
- articles control over definitions read as independent substantive glosses
- canonical definitions continue to govern the meaning of the terms used at each level

This hierarchy is an interpretive rule of last resort and does not license:
- abstract-strictness preferences
- rights contraction outside expressly permitted interaction rules
- substitution of one layer for another under ordinary operation

Each principle in this chapter applies together with the [Constitutional Triad](#constitutional-triad) established in [Chapter 00](#chapter-00-preamble--foundational-requirements). Section traces identify which leg or legs are materially implicated and whether duties scale with [material stake](#material-stake).

#### 1.2 Canonical conflict resolution procedure

This subsection is the **single canonical procedure** for resolving interpretive tension **within the binding constitutional source** (the integrated `core_*` instrument) and for reading **strictest** / **stricter** language in **[Chapter Fifteen](core_15-15_incorporation.md#2-authority-stack-and-invocation)** section 2 (*Conflict order*).

**Constitutional instrument.** For the numbered Sentient Constitution chapters read as one instrument, apply the interpretive rules in **§1.1 Integrated reading and ambiguity**: **Chapters Two through Five** as interpretive and evidentiary layer; the **ambiguity** rule (fullest **protective** effect as an integrated whole and alignment with sentient wellbeing; **not** **maximal restriction** or **abstract strictness** in isolation; **Chapter Ten** non-contraction except where **Chapter One** interaction rules and applicable definitions **expressly** permit); and the **Internal hierarchy (last-resort rule)** with its non-licensing limits.

**Incorporation layer ([Chapter Fifteen](core_15-15_incorporation.md#2-authority-stack-and-invocation) §2).** Where that section (*Conflict order*) calls for the **strictest applicable** incorporated **text** or a **stricter clearly adopted baseline** when **edition identifiers or custody records** are missing, contradictory, or materially unreliable, **strictest** and **stricter** carry the same **protective, integrated-reading** meaning as the **ambiguity** rule:
- **Strictest applicable** means the incorporated **text** that preserves the **strongest protective, safety, accountability, and traceability** requirements for the same materially scoped obligation among alternatives that remain coherent with the constitutional reading produced under the **Chapter Fifteen** stack — in the same sense as the Constitution's **fullest protective effect as an integrated whole**, and **not** **maximal restriction** or **abstract strictness** in isolation.
- **Stricter clearly adopted baseline** means the **adoption-traceable** incorporated edition or **baseline** the adoption chain **clearly supports** when records are unreliable (custody discipline and anti-drift), **not** substantive constitutional ambiguity resolution by preference for **abstract strictness**.

'''

NEW_SECTION_ELEVEN_TAIL = '''*In plain terms: every later chapter, every institutional design, and every system is read and evaluated through the principles in this chapter. Reading rules and ambiguity defaults live in [§1 Constitutional Interpretation](#1-constitutional-interpretation); value collisions live in [§7 Interaction and Conflict Resolution](#7-interaction-and-conflict-resolution). These principles must hold even under adversarial pressure, capture attempts, or misaligned incentives.*

This chapter governs interpretation, application, and enforcement of all subsequent chapters and provisions. Institutional interpretation safeguards in **Chapter Ten** Article XXII implement — they do not replace — this chapter's integrated-value framework.

All foundational principles in this chapter:
- are binding and govern interpretation, application, and enforcement of all subsequent provisions
- must be implemented through enforceable classification, governance requirements, and accountability mechanisms defined here

They must remain enforceable under conditions of adversarial behavior, system capture, and misaligned incentives.

'''


def apply_maps(text: str, *, ch1_only_labels: bool = False) -> str:
    for old, new in ANCHOR_MAP:
        text = text.replace(f"core_00-01_principles.md{old}", f"core_00-01_principles.md{new}")
        text = text.replace(old, new)
    if not ch1_only_labels:
        for old, new in LABEL_MAP:
            text = text.replace(old, new)
        for old, new in SECTION_PROSE:
            text = text.replace(old, new)
    return text


def transform_ch1(text: str) -> str:
    start = text.index("### §1 Constitutional Interpretation")
    end = text.index("### 1. Purpose and Role")
    text = text[:start] + NEW_SECTION_ONE + text[end:]

    for old, new in HEADER_RENUMBER:
        text = text.replace(old, new)

  # Replace old §10 body with slimmed §11.
    marker = "### 11. Integrated Application"
    idx = text.index(marker)
    plain_idx = text.index("*In plain terms: every later chapter", idx)
    end_idx = text.index("---\n\n**Next file:**", idx)
    text = text[:plain_idx] + NEW_SECTION_ELEVEN_TAIL + text[end_idx:]

    text = apply_maps(text, ch1_only_labels=True)

    # Fix internal references introduced before SECTION_PROSE pass.
    for old, new in SECTION_PROSE:
        text = text.replace(old, new)
    for old, new in LABEL_MAP:
        text = text.replace(old, new)

    return text


def iter_target_files() -> list[Path]:
    patterns = [
        "core_*.md",
        "tools/**/*.py",
        "tools/**/*.json",
        "implementation/**/*.md",
        "implementation/**/*.py",
        "ai_corpus/indexes/*.json",
        "doc_architecture.md",
        "plans/*.md",
        "evidence/**/*.md",
    ]
    files: list[Path] = []
    for pat in patterns:
        files.extend(ROOT.glob(pat))
    return sorted({p for p in files if p.is_file() and "archive/" not in str(p)})


def main() -> int:
    ch1_path = ROOT / "core_00-01_principles.md"
    ch1_path.write_text(transform_ch1(ch1_path.read_text(encoding="utf-8")), encoding="utf-8")

    for path in iter_target_files():
        if path == ch1_path:
            continue
        original = path.read_text(encoding="utf-8")
        updated = apply_maps(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(f"updated {path.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
