#!/usr/bin/env python3
"""Migrate Chapter Six extended Axis I (former §§3.5–3.9) and extended Axis II
(former §§4.5–4.13) into new top-level §§5–6; renumber former §5–§9 to §§7–§11.

Does not globally rewrite §6.1 (would collide with new Civil Violation §6.1).
Uses explicit link and phrase replacements after structural splice.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "core_06-06_standing_assessment.md"


def main() -> None:
    raise SystemExit(
        "Disabled: Chapter Six is split. Edit core_06-06_standing_assessment.md and "
        "core_07-07_standing_integration.md directly; this one-shot migrator targets the "
        "pre-split layout only."
    )
    text = SRC.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    def idx_startswith(prefix: str) -> int:
        for i, ln in enumerate(lines):
            if ln.startswith(prefix):
                return i
        raise SystemExit(f"start not found: {prefix!r}")

    def idx_exact(strip_prefix: str) -> int:
        for i, ln in enumerate(lines):
            if ln.rstrip("\n") == strip_prefix:
                return i
        raise SystemExit(f"exact line not found: {strip_prefix!r}")

    i_35 = idx_startswith("#### 3.5 Positive Standing Recognition")
    i_4 = idx_startswith("### 4. Violation Nature")
    i_ext = idx_exact(
        "#### Extended Axis II categories (legal, hybrid, duty, and diffusion — §§4.5–4.12)"
    )
    i_s5 = idx_startswith("### 5. Shared domain lenses")

    block_35_39 = lines[i_35:i_4]
    block_4_core = lines[i_4:i_ext]
    block_ext_413 = lines[i_ext:i_s5]
    tail = lines[i_s5:]

    b1 = "".join(block_35_39)
    for old, new in [
        ("#### 3.5 ", "#### 5.1 "),
        ("#### 3.6 ", "#### 5.2 "),
        ("#### 3.7 ", "#### 5.3 "),
        ("#### 3.8 ", "#### 5.4 "),
        ("#### 3.9 ", "#### 5.5 "),
    ]:
        b1 = b1.replace(old, new)

    b2_raw = "".join(block_ext_413)
    b2_raw = b2_raw.replace(
        "#### Extended Axis II categories (legal, hybrid, duty, and diffusion — §§4.5–4.12)\n\n"
        "**Sections 4.5 through 4.12** state **additional Axis II categories** (civil, criminal, and constitutional violation characterization; concurrency; constitutional floor rule; collective and duty-shaped violation nature; negligence and neglect) read with the **E-row** pairing in [**§1.1**](#11-two-axis-overview-reference). **How** those categories **combine** with **contribution state** and with **non-compliance ladder** severity is **not** restated here; it is stated in [**§6.1**](#38-standing-integration-contribution-and-violation-nature) and [**§6.2**](#62-joint-assessment-escalation-constraints-and-scrutiny).\n",
        "#### Extended Axis II categories (legal, hybrid, duty, and diffusion — §§6.1–6.8)\n\n"
        "**Sections 6.1 through 6.8** state **additional Axis II categories** (civil, criminal, and constitutional violation characterization; concurrency; constitutional floor rule; collective and duty-shaped violation nature; negligence and neglect) read with the **E-row** pairing in [**§1.1**](#11-two-axis-overview-reference). **How** those categories **combine** with **contribution state** and with **non-compliance ladder** severity is **not** restated here; it is stated in [**§8.1**](#38-standing-integration-contribution-and-violation-nature) and [**§8.2**](#62-joint-assessment-escalation-constraints-and-scrutiny).\n",
        1,
    )
    for old, new in [
        ("#### 4.13 ", "#### 6.9 "),
        ("#### 4.12 ", "#### 6.8 "),
        ("#### 4.11 ", "#### 6.7 "),
        ("#### 4.10 ", "#### 6.6 "),
        ("#### 4.9 ", "#### 6.5 "),
        ("#### 4.8 ", "#### 6.4 "),
        ("#### 4.7 ", "#### 6.3 "),
        ("#### 4.6 ", "#### 6.2 "),
        ("#### 4.5 ", "#### 6.1 "),
    ]:
        b2_raw = b2_raw.replace(old, new)

    sec5_hdr = (
        '<a id="5-extended-axis-i-standing-hooks-and-supplements"></a>\n'
        '<a id="5-axis-i-extended"></a>\n\n'
        "### 5. Extended Axis I — standing hooks and stackable contribution supplements\n"
        "<details>\n"
        '<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>\n\n'
        "- Upstream: [§3](#3-axis-i-contribution-state-and-standing-effect) (*primary Axis I — **§§3.0–3.4***); "
        "[§4](#4-axis-ii-violation-nature-legal-constitutional-type) (*primary Axis II — **§§4.0–4.4***); "
        "[§1.1](#11-two-axis-overview-reference).\n"
        "- Downstream: [§6](#6-extended-axis-ii-legal-hybrid-duty-and-harm-descriptors) (*extended Axis II — **§§6.1–6.9***); "
        "[§7](#7-shared-domain-lenses-cross-axis-vocabulary); "
        "[§8](#8-cross-axis-coupling-and-escalation-constraints) (*§§8.1–8.2*).\n"
        "- Read with: [§2](#2-standing-effect-verified-inputs-forums).\n\n"
        "</details>\n\n"
        "<br>\n\n"
        "*In plain terms: **trust-, role-, and recognition-eligibility** hooks and **stackable prosocial descriptors** live here — still **Axis I**, but separated from the four **primary** contribution bands in **section 3**.*\n\n"
    )

    sec6_hdr = (
        '<a id="6-extended-axis-ii-legal-hybrid-duty-and-harm-descriptors"></a>\n'
        '<a id="6-axis-ii-extended"></a>\n\n'
        "### 6. Extended Axis II — legal characterization, hybrid rules, and stackable harm descriptors\n"
        "<details>\n"
        '<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>\n\n'
        "- Upstream: [§4](#4-axis-ii-violation-nature-legal-constitutional-type) (*scope and ladder — **§§4.0–4.4***); "
        "[§5](#5-extended-axis-i-standing-hooks-and-supplements) (*paired **E-row** — **§§5.1–5.4***); "
        "[§1.1](#11-two-axis-overview-reference).\n"
        "- Downstream: [§7](#7-shared-domain-lenses-cross-axis-vocabulary) (*non-operative lens table*); "
        "[§8](#8-cross-axis-coupling-and-escalation-constraints) (*§§8.1–8.2*); "
        "[Chapter Eight](core_08-08_misconduct.md#chapter-seven-axis-ii-grand-anti-constitutional-misconduct).\n"
        "- Read with: [§2](#2-standing-effect-verified-inputs-forums).\n\n"
        "</details>\n\n"
        "<br>\n\n"
        "*In plain terms: **civil / criminal / constitutional** typing, **hybrid** concurrency, **duty** and **diffusion** rules, and **stackable harm-route** descriptors — separated from the **severity ladder** in **section 4**.*\n\n"
    )

    new_body = (
        "".join(lines[:i_35])
        + sec5_hdr
        + b1
        + "".join(block_4_core)
        + sec6_hdr
        + b2_raw
        + "".join(tail)
    )

    # Tail: §5→§7 through §9→§11
    new_body = new_body.replace(
        '<a id="5-shared-domain-lenses-cross-axis-vocabulary"></a>',
        '<a id="7-shared-domain-lenses-cross-axis-vocabulary"></a>\n<a id="5-shared-domain-lenses-cross-axis-vocabulary"></a>',
        1,
    )
    new_body = new_body.replace(
        "### 5. Shared domain lenses (cross-axis vocabulary)",
        "### 7. Shared domain lenses (cross-axis vocabulary)",
        1,
    )
    new_body = new_body.replace(
        '<a id="6-cross-axis-coupling-and-escalation-constraints"></a>',
        '<a id="8-cross-axis-coupling-and-escalation-constraints"></a>\n<a id="6-cross-axis-coupling-and-escalation-constraints"></a>',
        1,
    )
    new_body = new_body.replace(
        "### 6. Coupling Between Contribution State and Violation Nature — Escalation Constraints",
        "### 8. Coupling Between Contribution State and Violation Nature — Escalation Constraints",
        1,
    )
    new_body = new_body.replace(
        "#### 6.1 Standing integration — contribution and violation nature",
        "#### 8.1 Standing integration — contribution and violation nature",
        1,
    )
    new_body = new_body.replace(
        "#### 6.2 Joint assessment, escalation constraints, and scrutiny",
        "#### 8.2 Joint assessment, escalation constraints, and scrutiny",
        1,
    )
    new_body = new_body.replace(
        '<a id="7-additive-and-non-substitution-rule"></a>',
        '<a id="9-additive-and-non-substitution-rule"></a>\n<a id="7-additive-and-non-substitution-rule"></a>',
        1,
    )
    new_body = new_body.replace(
        "### 7. Additive and Non-Substitution Rule",
        "### 9. Additive and Non-Substitution Rule",
        1,
    )
    new_body = new_body.replace(
        '<a id="8-enforcement-realism-anchors"></a>',
        '<a id="10-enforcement-realism-anchors"></a>\n<a id="8-enforcement-realism-anchors"></a>',
        1,
    )
    new_body = new_body.replace(
        "### 8. Enforcement Realism Anchors",
        "### 10. Enforcement Realism Anchors",
        1,
    )
    new_body = new_body.replace(
        '<a id="9-tiered-anti-constitutional-misconduct-authoritative-location"></a>',
        '<a id="11-tiered-anti-constitutional-misconduct-authoritative-location"></a>\n<a id="9-tiered-anti-constitutional-misconduct-authoritative-location"></a>',
        1,
    )
    new_body = new_body.replace(
        "### 9. Tiered anti-constitutional misconduct — authoritative location",
        "### 11. Tiered anti-constitutional misconduct — authoritative location",
        1,
    )

    # --- Explicit markdown link display renumbering (anchors unchanged) ---
    link_fixes = [
        ("[§3.5](#35-positive-standing-recognition)", "[§5.1](#35-positive-standing-recognition)"),
        ("[§3.6](#36-restrictive-standing-effects)", "[§5.2](#36-restrictive-standing-effects)"),
        ("[§3.7](#37-reinstatement-review-and-non-entrenchment)", "[§5.3](#37-reinstatement-review-and-non-entrenchment)"),
        ("[§3.8](#38-standing-integration-category-hook)", "[§5.4](#38-standing-integration-category-hook)"),
        ("[§3.9](#39-stackable-benefit-and-stewardship-descriptors-axis-i-supplement)", "[§5.5](#39-stackable-benefit-and-stewardship-descriptors-axis-i-supplement)"),
        ("[§4.5](#45-civil-violation)", "[§6.1](#45-civil-violation)"),
        ("[§4.6](#46-criminal-violation)", "[§6.2](#46-criminal-violation)"),
        ("[§4.7](#47-constitutional-violation)", "[§6.3](#47-constitutional-violation)"),
        ("[§4.8](#48-concurrent-and-hybrid-violations)", "[§6.4](#48-concurrent-and-hybrid-violations)"),
        ("[§4.9](#49-constitutional-floor-rule)", "[§6.5](#49-constitutional-floor-rule)"),
        ("[§4.10](#410-collective-accountability-and-acquiescent-participation)", "[§6.6](#410-collective-accountability-and-acquiescent-participation)"),
        ("[§4.11](#411-duty-to-resist-unlawful-or-unconstitutional-instructions)", "[§6.7](#411-duty-to-resist-unlawful-or-unconstitutional-instructions)"),
        ("[§4.12](#412-negligence-and-neglect-as-violation-nature)", "[§6.8](#412-negligence-and-neglect-as-violation-nature)"),
        ("[§4.13](#413-non-exclusive-harm-and-conduct-descriptors)", "[§6.9](#413-non-exclusive-harm-and-conduct-descriptors)"),
        # Standing mechanics links only (by anchor id)
        (
            "[§6.1](#38-standing-integration-contribution-and-violation-nature)",
            "[§8.1](#38-standing-integration-contribution-and-violation-nature)",
        ),
        (
            "[§6.2](#62-joint-assessment-escalation-constraints-and-scrutiny)",
            "[§8.2](#62-joint-assessment-escalation-constraints-and-scrutiny)",
        ),
        ("[§6.1](#38-standing-integration-contribution-and-violation-nature)", "[§8.1](#38-standing-integration-contribution-and-violation-nature)"),
        ("[**§6.1**](#38-standing-integration-contribution-and-violation-nature)", "[**§8.1**](#38-standing-integration-contribution-and-violation-nature)"),
        ("[§5](#5-shared-domain-lenses-cross-axis-vocabulary)", "[§7](#7-shared-domain-lenses-cross-axis-vocabulary)"),
        ("[§6](#6-cross-axis-coupling-and-escalation-constraints)", "[§8](#8-cross-axis-coupling-and-escalation-constraints)"),
        ("[§7](#7-additive-and-non-substitution-rule)", "[§9](#9-additive-and-non-substitution-rule)"),
        ("[§8](#8-enforcement-realism-anchors)", "[§10](#10-enforcement-realism-anchors)"),
        ("[§9](#9-tiered-anti-constitutional-misconduct-authoritative-location)", "[§11](#11-tiered-anti-constitutional-misconduct-authoritative-location)"),
    ]
    for o, n in link_fixes:
        new_body = new_body.replace(o, n)

    # Range links in §1.1 table
    new_body = new_body.replace(
        "| E–1 | [§3.5](#35-positive-standing-recognition) Positive standing recognition | [§4.5](#45-civil-violation) Civil violation · [§4.6](#46-criminal-violation) Criminal violation · [§4.7](#47-constitutional-violation) Constitutional violation |",
        "| E–1 | [§5.1](#35-positive-standing-recognition) Positive standing recognition | [§6.1](#45-civil-violation) Civil violation · [§6.2](#46-criminal-violation) Criminal violation · [§6.3](#47-constitutional-violation) Constitutional violation |",
    )
    new_body = new_body.replace(
        "| E–2 | [§3.6](#36-restrictive-standing-effects) Restrictive standing effects | [§4.8](#48-concurrent-and-hybrid-violations) Concurrent and hybrid violations · [§4.9](#49-constitutional-floor-rule) Constitutional floor rule |",
        "| E–2 | [§5.2](#36-restrictive-standing-effects) Restrictive standing effects | [§6.4](#48-concurrent-and-hybrid-violations) Concurrent and hybrid violations · [§6.5](#49-constitutional-floor-rule) Constitutional floor rule |",
    )
    new_body = new_body.replace(
        "| E–3 | [§3.7](#37-reinstatement-review-and-non-entrenchment) Reinstatement, review, and non-entrenchment | [§4.10](#410-collective-accountability-and-acquiescent-participation) Collective accountability and acquiescent participation |",
        "| E–3 | [§5.3](#37-reinstatement-review-and-non-entrenchment) Reinstatement, review, and non-entrenchment | [§6.6](#410-collective-accountability-and-acquiescent-participation) Collective accountability and acquiescent participation |",
    )
    new_body = new_body.replace(
        "| E–4 | [§3.8](#38-standing-integration-category-hook) Standing integration — category hook · [§6.1](#38-standing-integration-contribution-and-violation-nature) Standing integration — mechanics | [§4.11](#411-duty-to-resist-unlawful-or-unconstitutional-instructions) Duty to resist unlawful or unconstitutional instructions · [§4.12](#412-negligence-and-neglect-as-violation-nature) Negligence and neglect as violation nature |",
        "| E–4 | [§5.4](#38-standing-integration-category-hook) Standing integration — category hook · [§8.1](#38-standing-integration-contribution-and-violation-nature) Standing integration — mechanics | [§6.7](#411-duty-to-resist-unlawful-or-unconstitutional-instructions) Duty to resist unlawful or unconstitutional instructions · [§6.8](#412-negligence-and-neglect-as-violation-nature) Negligence and neglect as violation nature |",
    )
    new_body = new_body.replace(
        "| X–1 | [§3.9](#39-stackable-benefit-and-stewardship-descriptors-axis-i-supplement) Stackable benefit-and-stewardship descriptors | [§4.13](#413-non-exclusive-harm-and-conduct-descriptors) Stackable harm-and-conduct descriptors |",
        "| X–1 | [§5.5](#39-stackable-benefit-and-stewardship-descriptors-axis-i-supplement) Stackable benefit-and-stewardship descriptors | [§6.9](#413-non-exclusive-harm-and-conduct-descriptors) Stackable harm-and-conduct descriptors |",
    )

    SRC.write_text(new_body, encoding="utf-8")
    print("Wrote structural migration to", SRC)
    print("Run manual / follow-up pass for prose § references and reader guidance.")


if __name__ == "__main__":
    main()
