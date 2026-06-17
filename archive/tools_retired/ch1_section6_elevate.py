#!/usr/bin/env python3
"""Promote Chapter One §6.1 → §6, §6.2 → §7; bump former §7–§11 → §8–§12."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# --- core_00-01_principles.md heading rewrites (deepest / most specific first) ---

HEADER_RENUMBER: list[tuple[str, str]] = [
    # Former §8 → §9
    ("##### 8.2.5 ", "##### 9.2.5 "),
    ("##### 8.2.4 ", "##### 9.2.4 "),
    ("##### 8.2.3 ", "##### 9.2.3 "),
    ("##### 8.2.2 ", "##### 9.2.2 "),
    ("##### 8.2.1 ", "##### 9.2.1 "),
    ("##### 8.1.5 ", "##### 9.1.5 "),
    ("##### 8.1.4 ", "##### 9.1.4 "),
    ("##### 8.1.3 ", "##### 9.1.3 "),
    ("##### 8.1.2 ", "##### 9.1.2 "),
    ("##### 8.1.1 ", "##### 9.1.1 "),
    ("#### 8.2 ", "#### 9.2 "),
    ("#### 8.1 ", "#### 9.1 "),
    ("### 8. Systemic Evaluation Requirement", "### 9. Systemic Evaluation Requirement"),
    # Former §7 → §8
    ("##### 7.4.2 ", "##### 8.4.2 "),
    ("##### 7.4.1 ", "##### 8.4.1 "),
    ("##### 7.3.2 ", "##### 8.3.2 "),
    ("##### 7.3.1 ", "##### 8.3.1 "),
    ("##### 7.2.2 ", "##### 8.2.2 "),
    ("##### 7.2.1 ", "##### 8.2.1 "),
    ("##### 7.1.4 ", "##### 8.1.4 "),
    ("##### 7.1.3 ", "##### 8.1.3 "),
    ("##### 7.1.2 ", "##### 8.1.2 "),
    ("##### 7.1.1 ", "##### 8.1.1 "),
    ("#### 7.4 ", "#### 8.4 "),
    ("#### 7.3 ", "#### 8.3 "),
    ("#### 7.2 ", "#### 8.2 "),
    ("#### 7.1 ", "#### 8.1 "),
    ("### 7. Interaction and Conflict Resolution", "### 8. Interaction and Conflict Resolution"),
    # Former §6.2 → §7
    ("##### 6.2.5 ", "#### 7.5 "),
    ("##### 6.2.4 ", "#### 7.4 "),
    ("##### 6.2.3 ", "#### 7.3 "),
    ("##### 6.2.2 ", "#### 7.2 "),
    ("##### 6.2.1 ", "#### 7.1 "),
    ("#### 6.2 Stewardship and Distributed Understanding", "### 7. Stewardship and Distributed Understanding"),
    # Former §6.1 → §6
    ("##### 6.1.5 ", "#### 6.5 "),
    ("##### 6.1.4 ", "#### 6.4 "),
    ("##### 6.1.3 ", "#### 6.3 "),
    ("##### 6.1.2 ", "#### 6.2 "),
    ("##### 6.1.1 ", "#### 6.1 "),
    ("#### 6.1 Shared-System Capacity", "### 6. Shared-System Capacity"),
    # Former §9–§11 → §10–§12
    ("### 11. Integrated Application", "### 12. Integrated Application"),
    ("### 10. Prohibition on Absolute Override", "### 11. Prohibition on Absolute Override"),
    ("### 9. Freedom (Bounded Agency)", "### 10. Freedom (Bounded Agency)"),
]

ANCHOR_MAP: list[tuple[str, str]] = [
    ("#825-contingent-claims-games-of-chance-and-event-contract-markets", "#925-contingent-claims-games-of-chance-and-event-contract-markets"),
    ("#824-misalignment-correction-and-capture-response", "#924-misalignment-correction-and-capture-response"),
    ("#823-role-depth-and-material-responsibility-pathways", "#923-role-depth-and-material-responsibility-pathways"),
    ("#822-stewardship-and-operator-incentive-alignment", "#922-stewardship-and-operator-incentive-alignment"),
    ("#821-alignment-requirement", "#921-alignment-requirement"),
    ("#815-assembly-collective-organization-and-institutional-formation", "#915-assembly-collective-organization-and-institutional-formation"),
    ("#814-voluntary-discontinuation-and-exit-rights", "#914-voluntary-discontinuation-and-exit-rights"),
    ("#813-privacy-informational-joint-invocation", "#913-privacy-informational-joint-invocation"),
    ("#812-accessibility-under-sentience-non-exclusion", "#912-accessibility-under-sentience-non-exclusion"),
    ("#811-systemic-scope-and-risk-factors", "#911-systemic-scope-and-risk-factors"),
    ("#82-incentive-alignment-and-system-capture", "#92-incentive-alignment-and-system-capture"),
    ("#81-required-evaluation-factors", "#91-required-evaluation-factors"),
    ("#8-systemic-evaluation-requirement", "#9-systemic-evaluation-requirement"),
    ("#742-proxy-divergence-invalidation", "#842-proxy-divergence-invalidation"),
    ("#741-rights-collision-decision-test", "#841-rights-collision-decision-test"),
    ("#74-rights-collision-procedure", "#84-rights-collision-procedure"),
    ("#732-time-consistency-constraint", "#832-time-consistency-constraint"),
    ("#731-constraint-on-freedom", "#831-constraint-on-freedom"),
    ("#73-freedom-limitation-constraints", "#83-freedom-limitation-constraints"),
    ("#722-trust-truth-alignment", "#822-trust-truth-alignment"),
    ("#721-preservation-of-epistemic-integrity", "#821-preservation-of-epistemic-integrity"),
    ("#72-epistemic-disclosure-constraints", "#82-epistemic-disclosure-constraints"),
    ("#714-minimization-of-avoidable-burden", "#814-minimization-of-avoidable-burden"),
    ("#713-minimization-of-harm", "#813-minimization-of-harm"),
    ("#712-necessity", "#812-necessity"),
    ("#711-proportionality", "#811-proportionality"),
    ("#71-core-tradeoff-principles", "#81-core-tradeoff-principles"),
    ("#7-interaction-and-conflict-resolution", "#8-interaction-and-conflict-resolution"),
    ("#625-bounds-and-rights-floor-disclaimer", "#75-bounds-and-rights-floor-disclaimer"),
    ("#624-openness-aspiration", "#74-openness-aspiration"),
    ("#623-institutional-development", "#73-institutional-development"),
    ("#622-distributed-understanding", "#72-distributed-understanding"),
    ("#621-stewardship", "#71-stewardship"),
    ("#62-stewardship-and-distributed-understanding", "#7-stewardship-and-distributed-understanding"),
    ("#615-consolidation-ceiling", "#65-consolidation-ceiling"),
    ("#614-pro-competition-and-anti-domination", "#64-pro-competition-and-anti-domination"),
    ("#613-concentration-threshold-mechanism-adopter-tunable", "#63-concentration-threshold-mechanism-adopter-tunable"),
    ("#612-constitutional-efficiency", "#62-constitutional-efficiency"),
    ("#611-productive-capacity-instrumental-good", "#61-productive-capacity-instrumental-good"),
    ("#61-shared-system-capacity", "#6-shared-system-capacity"),
    ("#11-integrated-application", "#12-integrated-application"),
    ("#10-prohibition-on-absolute-override", "#11-prohibition-on-absolute-override"),
    ("#9-freedom-bounded-agency", "#10-freedom-bounded-agency"),
]

# §-symbol prose: tuples of (pattern, replacement) applied with re.sub in order.
SECTION_RE: list[tuple[str, str]] = [
    (r"§11\b", "§§TEMP12§§"),
    (r"§10\b", "§§TEMP11§§"),
    (r"§9\b", "§§TEMP10§§"),
    (r"§8\.2\.5", "§9.2.5"),
    (r"§8\.2\.4", "§9.2.4"),
    (r"§8\.2\.3", "§9.2.3"),
    (r"§8\.2\.2", "§9.2.2"),
    (r"§8\.2\.1", "§9.2.1"),
    (r"§8\.1\.5", "§9.1.5"),
    (r"§8\.1\.4", "§9.1.4"),
    (r"§8\.1\.3", "§9.1.3"),
    (r"§8\.1\.2", "§9.1.2"),
    (r"§8\.1\.1", "§9.1.1"),
    (r"§8\.2\b", "§9.2"),
    (r"§8\.1\b", "§9.1"),
    (r"§8\b", "§9"),
    (r"§7\.4\.2", "§8.4.2"),
    (r"§7\.4\.1", "§8.4.1"),
    (r"§7\.3\.2", "§8.3.2"),
    (r"§7\.3\.1", "§8.3.1"),
    (r"§7\.2\.2", "§8.2.2"),
    (r"§7\.2\.1", "§8.2.1"),
    (r"§7\.1\.4", "§8.1.4"),
    (r"§7\.1\.3", "§8.1.3"),
    (r"§7\.1\.2", "§8.1.2"),
    (r"§7\.1\.1", "§8.1.1"),
    (r"§7\.4\b", "§8.4"),
    (r"§7\.3\b", "§8.3"),
    (r"§7\.2\b", "§8.2"),
    (r"§7\.1\b", "§8.1"),
    (r"§7\b", "§8"),
    (r"§6\.2\.5", "§7.5"),
    (r"§6\.2\.4", "§7.4"),
    (r"§6\.2\.3", "§7.3"),
    (r"§6\.2\.2", "§7.2"),
    (r"§6\.2\.1", "§7.1"),
    (r"§6\.2\b", "§7"),
    (r"§6\.1\.5", "§6.5"),
    (r"§6\.1\.4", "§6.4"),
    (r"§6\.1\.3–§6\.1\.5", "§6.3–§6.5"),
    (r"§6\.1\.3", "§6.3"),
    (r"§6\.1\.2", "§6.2"),
    (r"§6\.1\.1", "§6.1"),
    (r"§6\.1\b", "§6"),
    (r"§§TEMP12§§", "§12"),
    (r"§§TEMP11§§", "§11"),
    (r"§§TEMP10§§", "§10"),
]

LABEL_MAP: list[tuple[str, str]] = [
    ("[12. Integrated Application]", "[12. Integrated Application]"),
    ("[11. Integrated Application]", "[12. Integrated Application]"),
    ("11. Integrated Application", "12. Integrated Application"),
    ("[11. Prohibition on Absolute Override]", "[11. Prohibition on Absolute Override]"),
    ("[10. Prohibition on Absolute Override]", "[11. Prohibition on Absolute Override]"),
    ("10. Prohibition on Absolute Override", "11. Prohibition on Absolute Override"),
    ("[10. Freedom (Bounded Agency)]", "[10. Freedom (Bounded Agency)]"),
    ("[9. Freedom (Bounded Agency)]", "[10. Freedom (Bounded Agency)]"),
    ("§9 Freedom", "§10 Freedom"),
    ("[9. Systemic Evaluation Requirement]", "[9. Systemic Evaluation Requirement]"),
    ("[8. Systemic Evaluation Requirement]", "[9. Systemic Evaluation Requirement]"),
    ("8. Systemic Evaluation Requirement", "9. Systemic Evaluation Requirement"),
    ("[8.2 Incentive Alignment and System Capture]", "[9.2 Incentive Alignment and System Capture]"),
    ("[8.1 Required Evaluation Factors]", "[9.1 Required Evaluation Factors]"),
    ("[8. Interaction and Conflict Resolution]", "[8. Interaction and Conflict Resolution]"),
    ("[7. Interaction and Conflict Resolution]", "[8. Interaction and Conflict Resolution]"),
    ("7. Interaction and Conflict Resolution", "8. Interaction and Conflict Resolution"),
    ("[7.4 Rights-Collision Procedure]", "[8.4 Rights-Collision Procedure]"),
    ("[7.4.1 Rights-Collision Decision Test]", "[8.4.1 Rights-Collision Decision Test]"),
    ("[7.3 Freedom-Limitation Constraints]", "[8.3 Freedom-Limitation Constraints]"),
    ("[7.2 Epistemic Disclosure Constraints]", "[8.2 Epistemic Disclosure Constraints]"),
    ("[7.1 Core Tradeoff Principles]", "[8.1 Core Tradeoff Principles]"),
    ("[7.1.4 Minimization of Avoidable Burden]", "[8.1.4 Minimization of Avoidable Burden]"),
    ("[7.1.1 Proportionality]", "[8.1.1 Proportionality]"),
    ("[7.1.2 Necessity]", "[8.1.2 Necessity]"),
    ("[§7 Stewardship and Distributed Understanding]", "[§7 Stewardship and Distributed Understanding]"),
    ("[§6.2 Stewardship and Distributed Understanding]", "[§7 Stewardship and Distributed Understanding]"),
    ("§6.2 Stewardship", "§7 Stewardship"),
    ("[§6 Shared-System Capacity]", "[§6 Shared-System Capacity]"),
    ("[§6.1 Shared-System Capacity]", "[§6 Shared-System Capacity]"),
    ("[§6.1.1 Productive Capacity (Instrumental Good)]", "[§6.1 Productive Capacity (Instrumental Good)]"),
    ("[§6.1.3 Concentration Threshold Mechanism (Adopter-Tunable)]", "[§6.3 Concentration Threshold Mechanism (Adopter-Tunable)]"),
    ("[§6.1.4 Pro-Competition and Anti-Domination]", "[§6.4 Pro-Competition and Anti-Domination]"),
    ("[§6.1.5 Consolidation Ceiling]", "[§6.5 Consolidation Ceiling]"),
    ("[6. Shared-System Capacity and Stewardship]", "[6. Shared-System Capacity]"),
    ("6. Shared-System Capacity and Stewardship", "6. Shared-System Capacity"),
]

SECTION_PROSE: list[tuple[str, str]] = [
    ("Chapter One, section 11", "Chapter One, section 12"),
    ("Chapter One, section 10", "Chapter One, section 11"),
    ("Chapter One, section 9", "Chapter One, section 10"),
    ("Chapter One, section 8", "Chapter One, section 9"),
    ("Chapter One, section 7", "Chapter One, section 8"),
    ("Chapter One §11", "Chapter One §12"),
    ("Chapter One §10", "Chapter One §11"),
    ("Chapter One §9", "Chapter One §10"),
    ("Chapter One §8", "Chapter One §9"),
    ("Chapter One §7", "Chapter One §8"),
    ("section 11 —", "section 12 —"),
    ("section 10 —", "section 11 —"),
    ("section 9 —", "section 10 —"),
    ("section 8 —", "section 9 —"),
    ("section 7 —", "section 8 —"),
    ("§§6–8", "§§6–9"),
    ("§§6–8)", "§§6–9)"),
]

LEGACY_ANCHORS = '''<!-- Legacy §6/§7 redirect anchors (2026-06 section elevation); do not remove without link migration. -->
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

'''

OLD_SECTION_SIX_WRAPPER = re.compile(
    r"### 6\. Shared-System Capacity and Stewardship\n\n"
    r"\*In plain terms:.*?\n\n"
    r"This section sets the capacity.*?scaled to \[material stake\]\(#material-stake\)\.\n\n"
    r"This section has two major parts:\n"
    r"- \[§6\.1 Shared-System Capacity\].*?\n"
    r"- \[§6\.2 Stewardship and Distributed Understanding\].*?\n\n"
    r"Read together with the sections that follow, \*\*§§6–8\*\* form a sequence:\n"
    r"- \*\*§6\*\* — capacity and stewardship substrate\n"
    r"- \*\*§7\*\* — conflict-resolution and tradeoff procedure among values, rights, and constraints\n"
    r"- \*\*§8\*\* — whole-system validation before classification, governance, limitation, or compliance claims can stand\n\n",
    re.DOTALL,
)

NEW_SECTION_SIX_INTRO = '''*In plain terms: shared systems must keep building real productive capacity — without letting wealth, power, or control pile up in a few hands. **§6.1–§6.5** carry productive-capacity discipline, anti-concentration triggers, pro-competition rules, and consolidation ceilings that must bite before lock-in.*

Read together with the sections that follow, **§§6–9** form a sequence:
- **§6** — shared-system capacity, contestability, and anti-concentration discipline
- **§7** — stewardship, distributed understanding, and institutional learning
- **§8** — conflict-resolution and tradeoff procedure among values, rights, and constraints
- **§9** — whole-system validation before classification, governance, limitation, or compliance claims can stand

'''


def apply_section_re(text: str) -> str:
    for pattern, repl in SECTION_RE:
        text = re.sub(pattern, repl, text)
    return text


def apply_maps(text: str) -> str:
    for old, new in ANCHOR_MAP:
        text = text.replace(f"core_00-01_principles.md{old}", f"core_00-01_principles.md{new}")
    for old, new in ANCHOR_MAP:
        text = text.replace(old, new)
    for old, new in LABEL_MAP:
        text = text.replace(old, new)
    for old, new in SECTION_PROSE:
        text = text.replace(old, new)
    return apply_section_re(text)


def transform_ch1(text: str) -> str:
    if "### 6. Shared-System Capacity\n" in text or "### 6. Shared-System Capacity\r" in text:
        print("Chapter One already elevated; skipping structural transform", file=sys.stderr)
        return apply_maps(text)

    # Legacy mislabels: §6.1.4 was used for Minimization of Avoidable Burden (owner: §7.1.4 → §8.1.4).
    text = text.replace(
        "[§6.1.4 Minimization of Avoidable Burden](#714-minimization-of-avoidable-burden)",
        "[§8.1.4 Minimization of Avoidable Burden](#814-minimization-of-avoidable-burden)",
    )
    text = text.replace(
        "[§6.1.4](#714-minimization-of-avoidable-burden)",
        "[§8.1.4](#814-minimization-of-avoidable-burden)",
    )
    text = text.replace(
        "**framing** under section **6.1.4**.",
        "**framing** under section **8.1.4**.",
    )

    text = OLD_SECTION_SIX_WRAPPER.sub("", text)

    for old, new in HEADER_RENUMBER:
        text = text.replace(old, new)

    text = text.replace(
        '<a id="52-distributed-understanding-and-stewardship"></a>\n### 7. Stewardship and Distributed Understanding',
        '<a id="52-distributed-understanding-and-stewardship"></a>\n<a id="7-stewardship-and-distributed-understanding"></a>\n### 7. Stewardship and Distributed Understanding',
    )

    # Stewardship section intro: update cross-refs from §6.1 to §6
    text = text.replace(
        "Upstream: Principles: [3. Foundational Objective: Wellbeing](#3-foundational-objective-wellbeing); [4.2 Truth](#42-truth-epistemic-integrity-constraint); [5. Trust](#5-system-stability-enabler-trust-coordination-integrity); and [§6.1 Shared-System Capacity](#61-shared-system-capacity).",
        "Upstream: Principles: [3. Foundational Objective: Wellbeing](#3-foundational-objective-wellbeing); [4.2 Truth](#42-truth-epistemic-integrity-constraint); [5. Trust](#5-system-stability-enabler-trust-coordination-integrity); and [§6 Shared-System Capacity](#6-shared-system-capacity).",
    )

    # Insert §6 sequence intro before productive-capacity anchor
    marker = '<a id="51-productive-capacity-instrumental-good"></a>\n### 6. Shared-System Capacity'
    if marker in text:
        text = text.replace(
            marker,
            LEGACY_ANCHORS + NEW_SECTION_SIX_INTRO + '<a id="6-shared-system-capacity"></a>\n' + marker,
        )

    # §7 stewardship plain-terms / upstream fixes inside file
    text = text.replace(
        "**§6.1** states what must be preserved and improved; **§6.2** states how that capacity stays legitimate over time.",
        "**§6** states what must be preserved and improved; **§7** states how that capacity stays legitimate over time.",
    )

    text = apply_maps(text)

    # Heading-based markdown links like [7. Interaction...](#7-interaction...)
    text = text.replace("[11. Integrated Application](#11-integrated-application)", "[12. Integrated Application](#12-integrated-application)")
    text = text.replace("[10. Prohibition on Absolute Override](#10-prohibition-on-absolute-override)", "[11. Prohibition on Absolute Override](#11-prohibition-on-absolute-override)")
    text = text.replace("[9. Freedom (Bounded Agency)](#9-freedom-bounded-agency)", "[10. Freedom (Bounded Agency)](#10-freedom-bounded-agency)")
    text = text.replace(
        "value collisions live in [§7 Interaction and Conflict Resolution](#7-interaction-and-conflict-resolution)",
        "value collisions live in [§8 Interaction and Conflict Resolution](#8-interaction-and-conflict-resolution)",
    )

    return text


def iter_target_files() -> list[Path]:
    patterns = [
        "core_*.md",
        "tools/**/*.py",
        "tools/**/*.json",
        "implementation/**/*.md",
        "doc_architecture.md",
        "corpus_*.md",
        "README.md",
    ]
    files: list[Path] = []
    for pat in patterns:
        files.extend(ROOT.glob(pat))
    return sorted(
        p for p in files
        if p.is_file() and "archive/" not in str(p) and p.name != "ch1_section6_elevate.py"
    )


def update_ch1_dec_order(path: Path) -> None:
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    replacements = [
        ('"#### 6.1 Shared-System Capacity"', '"### 6. Shared-System Capacity"'),
        ('"#### 6.2 Stewardship and Distributed Understanding"', '"### 7. Stewardship and Distributed Understanding"'),
        ('"##### 6.2.1 Stewardship"', '"#### 7.1 Stewardship"'),
        ('"##### 6.2.2 Distributed Understanding"', '"#### 7.2 Distributed Understanding"'),
        ('"### 9. Freedom (Bounded Agency)"', '"### 10. Freedom (Bounded Agency)"'),
        ('"##### 7.4.1 Rights-Collision Decision Test"', '"##### 8.4.1 Rights-Collision Decision Test"'),
        ('"#### 8.1 Required Evaluation Factors"', '"#### 9.1 Required Evaluation Factors"'),
        ('"##### 8.2.2 Stewardship and Operator Incentive Alignment"', '"##### 9.2.2 Stewardship and Operator Incentive Alignment"'),
        ('"### 11. Integrated Application"', '"### 12. Integrated Application"'),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    ch1_path = ROOT / "core_00-01_principles.md"
    ch1_path.write_text(
        transform_ch1(ch1_path.read_text(encoding="utf-8")),
        encoding="utf-8",
    )
    print(f"updated {ch1_path.relative_to(ROOT)}")

    for path in iter_target_files():
        if path == ch1_path:
            continue
        original = path.read_text(encoding="utf-8")
        updated = apply_maps(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(f"updated {path.relative_to(ROOT)}")

    update_ch1_dec_order(ROOT / "tools/architecture/ch1_dec_order.json")
    print("updated tools/architecture/ch1_dec_order.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
