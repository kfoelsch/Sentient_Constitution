#!/usr/bin/env python3
"""Migrate Chapter Five definitions to constitutional Triad / Aims band organization.

Renumbers §3.1–§3.15 dependent clusters into band-aligned ranges, distributes §1
Independent and §2 Semi-independent content across five band files, writes the
Chapter Five compass in Part A, and updates corpus-wide references.

  python3 tools/ch5_constitutional_migration.py [--dry-run]
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PART_A = "core_05-05_definitions_a_independent.md"
OLD_PART_B = "core_05-05_definitions_b_semi_independent.md"
OLD_PART_C = "core_05-05_definitions_c_dependent_clusters.md"

BAND_FILES = {
    "o": "core_05o_oversight_definitions.md",
    "p": "core_05p_participation_definitions.md",
    "a": "core_05a_accountability_definitions.md",
    "c": "core_05c_continuity_definitions.md",
    "i": "core_05i_integrative_definitions.md",
}

BAND_ORDER = ("o", "p", "a", "c", "i")

BAND_LABELS = {
    "o": "Oversight",
    "p": "Participation",
    "a": "Accountability",
    "c": "Continuity",
    "i": "Integrative",
}

SKIP_DIRS = {"archive", ".git", "__pycache__", "node_modules", "ai_corpus", "tools", "evidence"}
EXTENSIONS = {".md", ".py", ".json", ".csv", ".mmd"}

# old §3 cluster number -> new §3 cluster number
CLUSTER_RENUMBER: dict[str, str] = {
    "3.12": "3.2",
    "3.14": "3.3",
    "3.1": "3.5",
    "3.2": "3.6",
    "3.8": "3.7",
    "3.3": "3.8",
    "3.6": "3.9",
    "3.9": "3.10",
    "3.15": "3.11",
    "3.5": "3.12",
    "3.10": "3.13",
    "3.7": "3.14",
    "3.13": "3.15",
    "3.4": "3.16",
}

CLUSTER_TITLES: dict[str, str] = {
    "3.1": "Animal Life, Sentient Life, and Sentience Status",
    "3.2": "Binding Stakeholder Choice",
    "3.3": "Collective Harm Boundary, Harm, and Harassment and Bullying",
    "3.4": "Corpus, Authority Stack, Supremacy, and Enforceability",
    "3.5": "Labor and Economic Floor: Compensation, Organization, Safe Conditions, Leisure, and Creative Work",
    "3.6": "Forum Families and Dispute Routing",
    "3.7": "Privacy (Informational) — peer-level cluster head",
    "3.8": "Self-Determination, Meaningful Agency, Expression, Educational Agency, and Volitional Integrity",
    "3.9": "Standing State, Contribution, and Violation",
    "3.10": "Stewardship, Governance Discipline, and Shared-System Capacity",
    "3.12": "Transparency, Auditability, and Verification",
    "3.13": "Trust and Trustworthiness",
    "3.14": "Truth and Epistemic Integrity",
    "3.15": "Use of Force, Autonomous Coercion, Autonomous Lethal Systems, and Weapons of Mass Harm",
}

NEW_TO_OLD = {v: k for k, v in CLUSTER_RENUMBER.items()}

CLUSTER_META: dict[str, dict[str, str]] = {
    "3.2": {
        "title": "Transparency, Auditability, and Verification",
        "leg": "Oversight",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
        "basis": "§3.2, §4, §7.1, §7.2",
    },
    "3.3": {
        "title": "Truth and Epistemic Integrity",
        "leg": "Oversight",
        "aim": "Flourishing",
        "cross": "integrative with **Accountability** where contest and correction are implicated",
        "continuity_note": "",
        "basis": "§3.2, §3.3, §4, §7.1, §7.2",
    },
    "3.5": {
        "title": "Animal Life, Sentient Life, and Sentience Status",
        "leg": "Participation",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
        "basis": "§2.1, §4, §10",
    },
    "3.6": {
        "title": "Binding Stakeholder Choice",
        "leg": "Participation",
        "aim": "Flourishing",
        "cross": "integrative with **Accountability** procedural integrity",
        "continuity_note": "",
        "basis": "§2.1, §3.4, §6.4, §8, §10",
    },
    "3.7": {
        "title": "Self-Determination, Meaningful Agency, Expression, Educational Agency, and Volitional Integrity",
        "leg": "Participation",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
        "basis": "§10, §2.1, §4",
    },
    "3.8": {
        "title": "Collective Harm Boundary, Harm, and Harassment and Bullying",
        "leg": "Accountability",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
        "basis": "§3.1, §6.1, §7.1, §9",
    },
    "3.9": {
        "title": "Forum Families and Dispute Routing",
        "leg": "Accountability",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
        "basis": "§2.1, §3.4, §6.4, §8, §10",
    },
    "3.10": {
        "title": "Standing State, Contribution, and Violation",
        "leg": "Accountability",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
        "basis": "§6.1, §6.3, §6.4, §7.1, §8",
    },
    "3.11": {
        "title": "Use of Force, Autonomous Coercion, Autonomous Lethal Systems, and Weapons of Mass Harm",
        "leg": "Accountability",
        "aim": "Continuity",
        "cross": "integrative with **Continuity** where irreversible harm is implicated",
        "continuity_note": "Distinguish constitutional **Continuity** aim from operational force protocols.",
        "basis": "§3.1, §6.1, §7.1, §9",
    },
    "3.12": {
        "title": "Labor and Economic Floor: Compensation, Organization, Safe Conditions, Leisure, and Creative Work",
        "leg": "Continuity",
        "aim": "Continuity",
        "cross": "",
        "continuity_note": "Constitutional **Continuity** aim — survival-floor and economic continuity.",
        "basis": "§3.1, §4.1, §5.1, §7.1",
    },
    "3.13": {
        "title": "Stewardship, Governance Discipline, and Shared-System Capacity",
        "leg": "Continuity",
        "aim": "Continuity",
        "cross": "integrative with **Accountability** where review and correction duties apply",
        "continuity_note": "Constitutional **Continuity** aim — durable governance discipline.",
        "basis": "§5.1, §6.1, §7.1, §8",
    },
    "3.14": {
        "title": "Privacy (Informational) — peer-level cluster head",
        "leg": "Continuity",
        "aim": "Flourishing",
        "cross": "integrative with **Participation** and **Oversight**",
        "continuity_note": "",
        "basis": "§3.2, §4, §7.1, §7.2",
    },
    "3.15": {
        "title": "Trust and Trustworthiness",
        "leg": "Continuity",
        "aim": "Flourishing",
        "cross": "",
        "continuity_note": "",
        "basis": "§5, §7.1, §8",
    },
    "3.16": {
        "title": "Corpus, Authority Stack, Supremacy, and Enforceability",
        "leg": "Integrative",
        "aim": "Flourishing",
        "cross": "**Oversight**, **Accountability**, and **Participation** — authority stack spans all Triad legs",
        "continuity_note": "",
        "basis": "§2.1, §4, §5.2, §7.2, §10",
    },
}

CLUSTER_BAND: dict[str, str] = {
    "3.2": "o", "3.3": "o", "3.4": "o",
    "3.5": "p", "3.6": "p", "3.7": "p",
    "3.8": "a", "3.9": "a", "3.10": "a", "3.11": "a",
    "3.12": "c", "3.13": "c", "3.14": "c", "3.15": "c",
    "3.16": "i",
}

INDEPENDENT_BAND_MAP: dict[str, str] = {
    "Accessibility": "p",
    "Adversarial, Scaled, and Exploited Conditions": "o",
    "Capability Requirement": "o",
    "Cascading Failure": "c",
    "Classification-Scaled Governance": "o",
    "Constitutional Community": "p",
    "Constitutional Contract Layer": "i",
    "Contingent Claim": "a",
    "Dependency": "c",
    "Dignity and Equal Moral Standing": "p",
    "Essential-Environment Non-Commodification": "c",
    "Event-Contract Market": "a",
    "Existential Risk": "c",
    "Feasibility": "a",
    "Foundational Constitutional Choice": "i",
    "Freedom (Bounded Agency)": "p",
    "Game of Chance": "a",
    "Good Faith": "a",
    "Harm Minimization (Tradeoff Selection)": "a",
    "Incentive Alignment": "i",
    "Info-Sphere": "p",
    "Innovation Reward and Anti-Enclosure": "i",
    "Lifespan Equivalent Unit (LEQU)": "p",
    "Natural Systems Standing": "p",
    "Necessity": "a",
    "Negligence": "a",
    "Non-Imposition (Cooperative Interaction)": "p",
    "Oversight": "o",
    "Press and Journalistic Activity": "o",
    "Proportionality": "a",
    "Redress and Remediation": "a",
    "Residual Risk / Misalignment": "c",
    "Restorative Justice": "a",
    "Reversibility": "c",
    "Risk": "c",
    "Risk Evaluation and Disclosure": "o",
    "Safety (Constraint)": "c",
    "Self-Healing": "c",
    "System Capture": "c",
    "Systemic": "c",
    "Systemic Materiality": "c",
    "Voluntary Discontinuation": "c",
    "Wellbeing": "c",
}

TOPIC_GROUP_BAND_MAP: dict[str, str] = {
    "Accountability, contestability, and redress pathways": "a",
    "Protected reporting and anti-retaliation": "a",
    "Assembly, collective organization, and institutional formation": "p",
    "Constitutional efficiency, productive capacity, avoidable burden, and burden-reduction duty": "c",
    "Agency, consent, and anti-coercion": "p",
    "Fairness, protected characteristics, and nondiscrimination": "p",
    "Family, care, reproductive autonomy, and instantiation": "p",
    "Ecological integrity, footprint, and sustainability": "c",
    "Emergency and contingency": "c",
    "Governance architecture, decentralization, and concentration": "a",
    "System boundaries, integrity, and exit": "c",
    "Stewardship, governance discipline, review, and correction": "a",
    "Stakeholder status and participation weight": "p",
    "Survival-floor continuity: bodily maintenance, tenure, and environment": "c",
    "Community-anchored continuity: indigenous, language, culture, and heritage": "c",
    "Materiality, impact, risk, and proxy integrity": "o",
    "Movement, refuge, and non-statelessness": "p",
}

BAND_PREAMBLES: dict[str, str] = {
    "o": (
        "This band holds **Oversight**-leg definitions from the [Constitutional Triad]"
        "(../core_00_preamble.md#constitutional-triad): transparency, auditability, truth, "
        "materiality classification, and strategic stewardship oversight. Primary constitutional "
        "aim: [Flourishing](../core_01_a_values_principles.md#flourishing), with Continuity-scaled "
        "clusters where noted in the compass."
    ),
    "p": (
        "This band holds **Participation**-leg definitions: accessibility, agency, consent, "
        "assembly, stakeholder voice, self-determination, and comparable participation floors. "
        "Primary constitutional aim: [Flourishing](../core_01_a_values_principles.md#flourishing)."
    ),
    "a": (
        "This band holds **Accountability**-leg definitions: contestability, redress, governance "
        "architecture, procedural integrity, standing, collective harm, forum routing, and use-of-force "
        "constraints. Scales with [material stake](../core_00_preamble.md#material-stake)."
    ),
    "c": (
        "This band holds definitions under the constitutional [Continuity aim]"
        "(../core_01_a_values_principles.md#continuity): dependency, risk, survival-floor continuity, "
        "labor floors, stewardship discipline, privacy lifecycle, and trust. "
        "**Continuity disambiguation:** constitutional **Continuity aim** (Chapter One §1) is distinct "
        "from operational or protocol continuity elsewhere in the corpus."
    ),
    "i": (
        "This band holds **Integrative** cross-leg definitions that require simultaneous satisfaction "
        "across Triad legs and cannot be owned cleanly by one leg alone — notably the corpus authority "
        "stack, constitutional contract layer, and foundational authorization terms."
    ),
}

NEW_FILES_SPEC: dict[str, dict] = {
    "core_05o_oversight_definitions.md": {
        "band": "o",
        "family_title": "Oversight leg definitions (§3.2–§3.3 clusters)",
        "clusters": ["3.2", "3.3"],
    },
    "core_05p_participation_definitions.md": {
        "band": "p",
        "family_title": "Participation leg definitions (§3.5–§3.7 clusters)",
        "clusters": ["3.5", "3.6", "3.7"],
    },
    "core_05a_accountability_definitions.md": {
        "band": "a",
        "family_title": "Accountability leg definitions (§3.8–§3.11 clusters)",
        "clusters": ["3.8", "3.9", "3.10", "3.11"],
    },
    "core_05c_continuity_definitions.md": {
        "band": "c",
        "family_title": "Continuity aim definitions (§3.12–§3.15 clusters)",
        "clusters": ["3.12", "3.13", "3.14", "3.15"],
    },
    "core_05i_integrative_definitions.md": {
        "band": "i",
        "family_title": "Integrative cross-leg definitions (§3.16 cluster)",
        "clusters": ["3.16"],
    },
}

CLUSTER_ANCHORS: dict[str, str] = {
    "3.1": "animal-life-sentient-life-and-sentience-status-cluster",
    "3.2": "binding-stakeholder-choice-cluster",
    "3.3": "collective-harm-boundary-and-harm-cluster",
    "3.4": "corpus-authority-stack-supremacy-and-enforceability-cluster",
    "3.5": "labor-and-economic-floor-cluster",
    "3.6": "forum-families-and-dispute-routing-cluster",
    "3.7": "privacy-informational-cluster",
    "3.8": "self-determination-and-meaningful-agency-cluster",
    "3.9": "standing-state-contribution-and-violation-cluster",
    "3.10": "stewardship-governance-discipline-and-shared-system-capacity-cluster",
    "3.11": "strategic-stewardship-and-stewardship-defect-cluster",
    "3.12": "transparency-auditability-and-verification-cluster",
    "3.13": "trust-and-trustworthiness-cluster",
    "3.14": "truth-and-epistemic-integrity-cluster",
    "3.15": "use-of-force-autonomous-coercion-and-mass-harm-cluster",
}

REDIRECT_MAP = {
    OLD_PART_B: (
        "core_05a_accountability_definitions.md",
        "Semi-independent definitions are now distributed across constitutional band files.",
    ),
    OLD_PART_C: (
        "core_05i_integrative_definitions.md",
        "Dependent clusters are now distributed across constitutional band files.",
    ),
}

H4_RE = re.compile(r"^#### (.+)$", re.MULTILINE)
CLUSTER_H4_RE = re.compile(r"^#### (3\.\d+(?:\.\d+)?)\s+(.+)$", re.MULTILINE)
ANCHOR_RE = re.compile(r'<a id="([^"]+)"></a>')


def renumber_cluster_refs(text: str) -> str:
    """Renumber §3.N cluster references using temp tokens."""
    ordered = sorted(CLUSTER_RENUMBER.items(), key=lambda kv: len(kv[0]), reverse=True)
    temps: dict[str, str] = {}
    for idx, (old, new) in enumerate(ordered):
        if old == new:
            continue
        token = f"__CH5SEC{idx:02d}__"
        temps[token] = new
        for pattern in (
            rf"\b§{re.escape(old)}\b",
            rf"\bsection {re.escape(old)}\b",
            rf"\bSection {re.escape(old)}\b",
            rf"\*\*§{re.escape(old)}\b",
            rf"Chapter Five §{re.escape(old)}\b",
            rf"Chapter Five, section {re.escape(old)}\b",
            rf"#### {re.escape(old)}\s",
            rf"§{re.escape(old)}\s+\*",
        ):
            text = re.sub(pattern, lambda m, t=token: m.group(0).replace(old, t), text)
        text = re.sub(rf"\b{re.escape(old)}\b(?=\s+\*)", token, text)
    for token, new in temps.items():
        text = text.replace(token, new)
    return text


def peel_trailing_entry_preamble(buf: list[str]) -> tuple[list[str], list[str]]:
    """Move inter-entry ---/anchor separators from the prior block to the next preamble."""
    text = "\n".join(buf).rstrip()
    peeled: list[str] = []
    while text:
        m = re.search(r"\n<a id=\"[^\"]+\"></a>\s*$", text)
        if m:
            peeled = text[m.start() + 1 :].strip().splitlines() + peeled
            text = text[: m.start()].rstrip()
            continue
        m = re.search(r"\n---\s*$", text)
        if m:
            peeled = ["---"] + peeled
            text = text[: m.start()].rstrip()
            continue
        break
    if peeled:
        peeled.append("")
    return (text.splitlines() if text else []), peeled


def split_h4_blocks(text: str, skip_titles: set[str] | None = None) -> dict[str, str]:
    skip_titles = skip_titles or set()
    lines = text.splitlines()
    blocks: dict[str, str] = {}
    current: str | None = None
    buf: list[str] = []
    preamble: list[str] = []
    for line in lines:
        m = re.match(r"^#### (.+)$", line)
        if m:
            title = m.group(1).strip()
            if current and current not in skip_titles:
                body_lines, trailing = peel_trailing_entry_preamble(buf)
                blocks[current] = "\n".join(body_lines).rstrip()
                preamble = trailing
            if title in skip_titles:
                current = None
                buf = []
                preamble = []
            else:
                current = title
                buf = preamble + [line]
                preamble = []
        elif current is not None:
            buf.append(line)
        elif line.strip() or preamble:
            preamble.append(line)
    if current and current not in skip_titles:
        body_lines, _ = peel_trailing_entry_preamble(buf)
        blocks[current] = "\n".join(body_lines).rstrip()
    return blocks


def extract_independent_section(part_a: str) -> tuple[str, dict[str, str]]:
    marker = "### 1. Independent Definitions"
    idx = part_a.find(marker)
    if idx < 0:
        raise RuntimeError("§1 marker not found in Part A")
    pre = part_a[:idx].rstrip()
    rest = part_a[idx:]
    footer_idx = rest.find("**Previous file:**")
    if footer_idx >= 0:
        s1_body = rest[:footer_idx]
        footer = rest[footer_idx:]
    else:
        next_idx = rest.find("**Next file:**")
        s1_body = rest[:next_idx] if next_idx >= 0 else rest
        footer = rest[next_idx:] if next_idx >= 0 else ""
    blocks = split_h4_blocks(s1_body)
    return pre, blocks, footer


def extract_part_b_groups(part_b: str) -> dict[str, str]:
    idx = part_b.find("### 2. Semi-independent Definitions")
    body = part_b[idx:] if idx >= 0 else part_b
    footer_idx = body.find("**Previous file:**")
    if footer_idx >= 0:
        body = body[:footer_idx]
    lines = body.splitlines()
    groups: dict[str, str] = {}
    current_group: str | None = None
    buf: list[str] = []
    group_titles = set(TOPIC_GROUP_BAND_MAP.keys())

    def flush() -> None:
        nonlocal current_group, buf
        if current_group:
            groups[current_group] = "\n".join(buf).rstrip()
        buf = []

    for line in lines:
        m = re.match(r"^#### (.+)$", line)
        if m:
            title = m.group(1).strip()
            if title in group_titles:
                flush()
                current_group = title
                buf = [line]
            elif current_group:
                buf.append(line)
        elif current_group:
            buf.append(line)
    flush()
    return groups


def extract_clusters(part_c: str) -> tuple[str, dict[str, str]]:
    meta_end = part_c.find("---\n\n---\n\n<a id=")
    if meta_end < 0:
        meta_end = part_c.find("#### 3.1 ")
    meta = part_c[:meta_end].rstrip() if meta_end > 0 else ""
    cluster_text = part_c[meta_end:] if meta_end > 0 else part_c
    footer_idx = cluster_text.find("**Previous file:**")
    if footer_idx >= 0:
        cluster_text = cluster_text[:footer_idx]
    blocks: dict[str, str] = {}
    parts = re.split(r"(?=^#### 3\.\d+ )", cluster_text, flags=re.MULTILINE)
    for part in parts:
        m = CLUSTER_H4_RE.match(part)
        if m:
            blocks[m.group(1)] = part.rstrip()
    return meta, blocks


def constitutional_frame_lines(new_id: str) -> list[str]:
    meta = CLUSTER_META.get(new_id, {})
    if not meta:
        return []
    lines = [
        f"- Constitutional frame: **{meta['leg']}** leg; **{meta['aim']}** aim (primary); "
        "scales with [material stake](../core_00_preamble.md#material-stake) via "
        "[Materiality Determination](../core_05a_accountability_definitions.md#materiality-determination)."
    ]
    if meta.get("cross"):
        lines.append(f"- Cross-leg note: {meta['cross']}.")
    if meta.get("continuity_note"):
        lines.append(f"- Continuity disambiguation: {meta['continuity_note']}")
    if meta.get("basis"):
        lines.append(
            f"- Chapter One basis: {meta['basis']} (see "
            "[Chapter Five compass](../core_05-05_definitions_a_independent.md#chapter-five-compass-and-definition-map) map)."
        )
    return lines


def inject_constitutional_frame(block: str, new_id: str) -> str:
    frame = constitutional_frame_lines(new_id)
    if not frame:
        return block
    lines = block.splitlines()
    if not lines or not lines[0].startswith("#### 3."):
        return block
    head_chunk = "\n".join(lines[:20])
    if "Constitutional frame:" in head_chunk:
        return block
    insertion = "\n".join(frame)
    if "Trace</span>" in head_chunk:
        pattern = (
            r"(<details>\s*\n<summary><strong><span style=\"color: #2563eb;\">Trace</span></strong></summary>\s*\n"
            r"(?:- [^\n]+\n)*?)(\n</details>)"
        )
        return re.sub(
            r"(<details>\s*\n<summary><strong><span style=\"color: #2563eb;\">Trace</span></strong></summary>\s*\n"
            r"(?:- [^\n]+\n)*?)(\n</details>)",
            r"\1\n" + insertion + r"\2",
            block,
            count=1,
            flags=re.DOTALL,
        )
    trace_block = [
        lines[0],
        "",
        "<details>",
        '<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>',
        "",
        insertion,
        "",
        "</details>",
        "",
        "<br>",
        "",
    ]
    return "\n".join(trace_block + lines[1:])


def update_cluster_heading(block: str, old_id: str, new_id: str) -> str:
    meta = CLUSTER_META[new_id]
    old_title = CLUSTER_TITLES.get(old_id, "")
    new_heading = f"#### {new_id} {meta['leg']}: {meta['title']}"
    block = re.sub(
        rf"^#### {re.escape(old_id)}\s+{re.escape(old_title)}",
        new_heading,
        block,
        count=1,
        flags=re.MULTILINE,
    )
    if not block.startswith(f"#### {new_id}"):
        block = re.sub(rf"^#### {re.escape(old_id)}\s.+$", new_heading, block, count=1, flags=re.MULTILINE)
    return block


BAND_CHAIN = (
    BAND_FILES["o"],
    BAND_FILES["p"],
    BAND_FILES["a"],
    BAND_FILES["c"],
    BAND_FILES["i"],
)


def band_footer(filename: str) -> str:
    idx = BAND_CHAIN.index(filename)
    prev_file = BAND_CHAIN[idx - 1] if idx > 0 else "core_05-05_definitions_a_independent.md"
    next_file = "core_06-06_standing_assessment.md" if idx == len(BAND_CHAIN) - 1 else BAND_CHAIN[idx + 1]
    return (
        f"\n\n---\n\n"
        f"**Previous file:** [{prev_file}]({prev_file})\n\n"
        f"**Next file:** [{next_file}]({next_file})\n"
    )


def build_anchor_home_map(
    independent: dict[str, str],
    groups: dict[str, str],
    clusters: dict[str, str],
) -> dict[str, str]:
    anchor_home: dict[str, str] = {}
    for title, band in INDEPENDENT_BAND_MAP.items():
        for anchor in ANCHOR_RE.findall(independent.get(title, "")):
            anchor_home[anchor] = BAND_FILES[band]
    for gtitle, band in TOPIC_GROUP_BAND_MAP.items():
        for anchor in ANCHOR_RE.findall(groups.get(gtitle, "")):
            anchor_home[anchor] = BAND_FILES[band]
    for old_id, new_id in CLUSTER_RENUMBER.items():
        bf = BAND_FILES[CLUSTER_BAND[new_id]]
        for anchor in ANCHOR_RE.findall(clusters.get(old_id, "")):
            anchor_home[anchor] = bf
    for anchor in PART_A_ANCHORS:
        anchor_home[anchor] = PART_A
    return anchor_home


def rewrite_ch5_links(text: str, anchor_home: dict[str, str]) -> str:
    """Replace Part A/B/C link targets using anchor ownership map."""
    old_names = (OLD_PART_B, OLD_PART_C, PART_A)
    link_re = re.compile(
        r"\]\(((?:\.\./)*)(" + "|".join(re.escape(p) for p in old_names) + r"|"
        + "|".join(re.escape(p) for p in BAND_FILES.values())
        + r")(#[^)]+)?\)"
    )

    def repl(m: re.Match[str]) -> str:
        prefix = m.group(1) or ""
        path = m.group(2)
        frag = m.group(3) or ""
        if not frag:
            if path in (OLD_PART_B, OLD_PART_C):
                return f"]({prefix}{PART_A}#chapter-five-foundational-definitions)"
            return m.group(0)
        anchor = frag[1:]
        if anchor in PART_A_ANCHORS:
            return f"]({prefix}{PART_A}{frag})"
        home = anchor_home.get(anchor)
        if home:
            return f"]({prefix}{home}{frag})"
        if path == OLD_PART_B:
            return f"]({prefix}{BAND_FILES['a']}{frag})"
        if path == OLD_PART_C:
            return f"]({prefix}{BAND_FILES['i']}{frag})"
        if path == PART_A and anchor not in PART_A_ANCHORS:
            return f"]({prefix}{BAND_FILES['a']}{frag})"
        return m.group(0)

    return link_re.sub(repl, text)


def rewrite_fragment_links(text: str, anchor_home: dict[str, str]) -> str:
    """Rewrite same-file fragment links (#anchor) to band-qualified paths."""
    frag_re = re.compile(r"\]\(#([^)]+)\)")

    def repl(m: re.Match[str]) -> str:
        anchor = m.group(1)
        if anchor in PART_A_ANCHORS:
            return f"]({PART_A}#{anchor})"
        home = anchor_home.get(anchor)
        if home and home != PART_A:
            return f"]({home}#{anchor})"
        return m.group(0)

    return frag_re.sub(repl, text)


def build_band_file(
    filename: str,
    spec: dict,
    independent: dict[str, str],
    groups: dict[str, str],
    clusters: dict[str, str],
) -> str:
    band = spec["band"]
    leg = BAND_LABELS[band]
    parts = [
        f"# Constitutional definitions ({leg} band)",
        "",
        "This file is **part of the Sentient Constitution** and is **binding only together** "
        "with the other numbered `core_*` files read as one instrument. It contains "
        f"**Chapter Five, {leg} band** — Independent, Semi-independent, and Dependent cluster "
        f"definitions assigned to the **{leg}** constitutional band. "
        f"Reading order and the compass live in [{PART_A}]({PART_A}#chapter-five-foundational-definitions).",
        "",
        "---",
        "",
        f"## {spec['family_title']}",
        "",
        "<details>",
        '<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>',
        "",
        f"- Upstream: [Chapter Five compass]({PART_A}#chapter-five-compass-and-definition-map); "
        "[Constitutional Triad](../core_00_preamble.md#constitutional-triad); "
        "[Two Constitutional Aims](../core_01_a_values_principles.md#two-constitutional-aims).",
        f"- Downstream: {leg}-band canonical definition homes for Chapter Five.",
        f"- Read with: **{leg}** band definitions; mandatory cluster read-with where admission scope applies.",
        "",
        "</details>",
        "",
        "<br>",
        "",
        "",
        BAND_PREAMBLES[band],
        "",
        "| Cluster | Section |",
        "|---|---|",
    ]
    for cid in spec["clusters"]:
        parts.append(f"| **§{cid}** | {CLUSTER_META[cid]['title']} |")
    parts.extend(["", "---", ""])

    parts.extend([f"### {leg}: Independent terms", ""])
    for title, body in sorted(independent.items()):
        if INDEPENDENT_BAND_MAP.get(title) == band:
            parts.append(normalize_entry_block(body))
            parts.append("")
            parts.append("---")
            parts.append("")

    parts.extend([f"### {leg}: Semi-independent terms", ""])
    for gtitle, body in groups.items():
        if TOPIC_GROUP_BAND_MAP.get(gtitle) == band:
            parts.append(body)
            parts.append("")
            parts.append("---")
            parts.append("")

    parts.extend([f"### {leg}: Dependent clusters", ""])
    for new_id in spec["clusters"]:
        old_id = NEW_TO_OLD[new_id]
        block = clusters.get(old_id, "")
        if not block:
            raise RuntimeError(f"Missing cluster {old_id} for band {band}")
        block = renumber_cluster_refs(block)
        block = update_cluster_heading(block, old_id, new_id)
        block = inject_constitutional_frame(block, new_id)
        parts.append(block)
        parts.append("")
        parts.append("---")
        parts.append("")

    body = "\n".join(parts).rstrip()
    body = re.sub(r"\n---\s*$", "", body)
    body = collapse_duplicate_separators(body)
    return body + band_footer(filename)


def build_compass_section() -> str:
    rows = []
    for new_id in sorted(CLUSTER_META.keys(), key=lambda x: float(x.split(".")[1])):
        m = CLUSTER_META[new_id]
        bf = BAND_FILES[CLUSTER_BAND[new_id]]
        cross = m.get("cross", "") or "—"
        cont = m.get("continuity_note", "") or "—"
        rows.append(
            f"| **§{new_id}** | {m['title']} | {m['leg']} | {m['aim']} | {m.get('basis', '—')} | {cross} | {cont} | [{bf}]({bf}) |"
        )

    band_rows = []
    ranges = {
        "o": "§3.2–§3.3",
        "p": "§3.5–§3.7",
        "a": "§3.8–§3.11",
        "c": "§3.12–§3.15",
        "i": "§3.16",
    }
    for band in BAND_ORDER:
        bf = BAND_FILES[band]
        band_rows.append(
            f"| **{BAND_LABELS[band]} leg** | [{bf}]({bf}) | **{ranges[band]}** |"
        )

    return f"""---

### Chapter Five compass and definition map
<a id="chapter-five-compass-and-definition-map"></a>

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [Constitutional Triad](../core_00_preamble.md#constitutional-triad); [Two Constitutional Aims](../core_01_a_values_principles.md#two-constitutional-aims); [material stake](../core_00_preamble.md#material-stake).
- Downstream: constitutional orientation for all Chapter Five band definitions and §3 dependent clusters.
- Read with: [§3.0.1 Joint invocation](#joint-invocation-and-satisfaction) and [§3.0.2 Standalone interaction](#standalone-definitions-interaction-and-full-context) meta rules before applying any dependent cluster.

</details>

<br>

Use this compass before invoking any Chapter Five definition. Chapter Five supplies canonical O/E/C homes; it does not replace the [Constitutional Triad](../core_00_preamble.md#constitutional-triad), [Two Constitutional Aims](../core_01_a_values_principles.md#two-constitutional-aims), or [material stake](../core_00_preamble.md#material-stake) scaling required by [Chapter Two](../core_02-04_definition_mechanics.md).

**Reading order**

1. This compass and the constitutional bands below.
2. The band file for the relevant Triad leg, **Continuity** band, or **Integrative** band.
3. Individual definition O/E/C entries; dependent clusters per admission scope.
4. Where a finding is **non-compliant**, optional [Non-Compliance Finding Profile](core_05a_accountability_definitions.md#non-compliance-finding-profile) metadata per cluster map.

**Constitutional bands**

| Band | File | §3 cluster range |
|---|---|---|
{chr(10).join(band_rows)}

---

### Full cluster map (reader guidance)

<details>
<summary><strong><span style="color: #2563eb;">Reader guidance (non-operative): full cluster map</span></strong></summary>

> The following content is **reader guidance only**. Per-cluster constitutional framing lives in each cluster's Trace block.

| § ID | Title | Triad leg / band | Primary aim | Chapter One § basis | Cross-leg note | Continuity disambiguation | Home file |
|---|---|---|---|---|---|---|---|
{chr(10).join(rows)}

</details>

<br>
"""


PART_A_ANCHORS = {
    "chapter-five-foundational-definitions",
    "chapter-five-compass-and-definition-map",
    "definitions-a-z",
    "dependent-clusters-a-z",
    "semi-independent-definitions-a-z",
    "independent-definitions-a-z",
    "definitions-a-z-unified",
    "all-definitions-and-clusters-a-z",
    "joint-invocation-and-satisfaction",
    "standalone-definitions-interaction-and-full-context",
    "section-3-dependent-clusters-clustered-definitions",
    "section-2-semi-independent-definitions",
    "1-interdependent-definitions",
}


def normalize_entry_block(body: str) -> str:
    body = re.sub(r"^\s*---\s*\n+", "", body)
    body = re.sub(r"\n---\n\n---\n", "\n---\n\n", body)
    body = re.sub(r"(<a id=\"[^\"]+\"></a>)\n---\n", r"\1\n\n---\n", body)
    body = re.sub(r"\n---\s*$", "", body.rstrip())
    return body


def collapse_duplicate_separators(text: str) -> str:
    text = re.sub(r"(?:\n---\s*){2,}", "\n---\n\n", text)
    return text


def rebuild_clusters_directory(pre: str, root: Path) -> str:
    """Replace Clusters A-Z block using live band-file cluster inventory."""
    tools = root / "tools"
    if str(tools) not in sys.path:
        sys.path.insert(0, str(tools))
    from ch5_single_definition_audit import collect_entries_and_clusters, normalized_sort_key

    _, clusters = collect_entries_and_clusters(root)
    rows = sorted(
        [f"- [{c.label}]({c.href})" for c in clusters],
        key=lambda s: normalized_sort_key(re.search(r"\[([^\]]+)\]", s).group(1), cluster=True),
    )
    cluster_block = "#### Clusters A-Z\n\n" + "\n".join(rows)
    return re.sub(
        r"#### Clusters A-Z\n\n(?:- \[[^\]]+\]\([^)]+\)\n?)+",
        cluster_block + "\n",
        pre,
        count=1,
    )


def rebuild_definitions_directory(pre: str, root: Path) -> str:
    """Replace Definitions A-Z block using live band-file entry inventory."""
    tools = root / "tools"
    if str(tools) not in sys.path:
        sys.path.insert(0, str(tools))
    from ch5_single_definition_audit import collect_entries_and_clusters, normalized_sort_key

    entries, _ = collect_entries_and_clusters(root)
    rows = sorted(
        [f"- [{e.label}]({e.href})" for e in entries],
        key=lambda s: normalized_sort_key(re.search(r"\[([^\]]+)\]", s).group(1)),
    )
    defs_block = "#### Definitions A-Z\n\n" + "\n".join(rows)
    return re.sub(
        r"#### Definitions A-Z\n\n(?:- \[[^\]]+\]\([^)]+\)\n?)+",
        defs_block + "\n",
        pre,
        count=1,
    )


def build_part_a(pre: str, meta: str, footer: str, anchor_home: dict[str, str], root: Path) -> str:
    pre = rebuild_clusters_directory(pre, root)
    pre = rebuild_definitions_directory(pre, root)
    compass = build_compass_section()
    meta_section = ""
    if "#### 3.0.1" in meta:
        meta_section = meta[meta.find("### 3. Dependent"): meta.find("---", meta.find("#### 3.0.2") + 1)]
        meta_section = meta_section.strip()

    intro = (
        "\n\nThis file is the **Chapter Five index**: reader guidance, alphabetical directory, "
        "§3.0 joint-invocation meta rules, and the constitutional compass. "
        "Independent, semi-independent, and dependent definition bodies live in the five band files "
        f"([Oversight]({BAND_FILES['o']}), [Participation]({BAND_FILES['p']}), "
        f"[Accountability]({BAND_FILES['a']}), [Continuity]({BAND_FILES['c']}), "
        f"[Integrative]({BAND_FILES['i']}).\n"
    )
    pre_lines = pre.splitlines()
    for i, line in enumerate(pre_lines):
        if line.startswith("This file is **part of the Sentient Constitution**"):
            pre_lines[i] = (
                "This file is **part of the Sentient Constitution** and is **binding only together** "
                "with the other numbered `core_*` files read as one instrument. It contains "
                "**Chapter Five, Part A** — reader guidance, alphabetical directory, §3.0 meta rules, "
                "and the constitutional compass."
            )
            break
    pre = "\n".join(pre_lines)
    pre = re.sub(
        r"Part B.*?Part C.*?\.",
        intro.strip(),
        pre,
        count=1,
        flags=re.DOTALL,
    )

    footer = re.sub(
        r"\*\*Next file:\*\* \[core_05-05_definitions_b_semi_independent\.md\]\([^)]+\)",
        f"**Next file:** [{BAND_FILES['o']}]({BAND_FILES['o']})",
        footer,
    )
    return f"{pre.rstrip()}\n\n{compass}\n\n---\n\n{meta_section}\n\n---\n\n{footer.lstrip()}"




def build_redirect_stub(old_file: str, new_file: str, note: str) -> str:
    return f"""# Redirect — retired Chapter Five file

This file is **retired** after the Chapter Five constitutional band reorganization. {note}

**Read instead:** [{new_file}]({new_file})

See [archive/core_ch5_retired/README.md](../../archive/core_ch5_retired/README.md).
"""


def iter_corpus_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix not in EXTENSIONS:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in ("ch5_constitutional_migration.py", "cjs5_constitutional_migration.py"):
            continue
        yield path


def write_evidence(root: Path, dry_run: bool) -> None:
    today = date.today().isoformat()
    out_dir = root / "evidence" / today
    if dry_run:
        print(f"Would write evidence to {out_dir}")
        return
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for title, band in INDEPENDENT_BAND_MAP.items():
        rows.append({"kind": "independent", "name": title, "band": band, "file": BAND_FILES[band], "section": ""})
    for title, band in TOPIC_GROUP_BAND_MAP.items():
        rows.append({"kind": "topic_group", "name": title, "band": band, "file": BAND_FILES[band], "section": ""})
    for old, new in CLUSTER_RENUMBER.items():
        rows.append({
            "kind": "cluster",
            "name": CLUSTER_TITLES[old],
            "band": CLUSTER_BAND[new],
            "file": BAND_FILES[CLUSTER_BAND[new]],
            "section": f"{old}->{new}",
        })
    csv_path = out_dir / f"ch5_band_assignment_matrix_{today}.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["kind", "name", "band", "file", "section"])
        w.writeheader()
        w.writerows(rows)
    log = {"date": today, "clusters_renumbered": CLUSTER_RENUMBER, "band_files": BAND_FILES}
    (out_dir / f"ch5_constitutional_migration_log_{today}.json").write_text(
        json.dumps(log, indent=2), encoding="utf-8"
    )
    print(f"Wrote evidence to {out_dir}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    part_a_text = (ROOT / PART_A).read_text(encoding="utf-8")
    part_b_text = (ROOT / OLD_PART_B).read_text(encoding="utf-8")
    part_c_text = (ROOT / OLD_PART_C).read_text(encoding="utf-8")

    pre, independent_blocks, footer = extract_independent_section(part_a_text)
    groups = extract_part_b_groups(part_b_text)
    meta, cluster_blocks = extract_clusters(part_c_text)

    for title in INDEPENDENT_BAND_MAP:
        if title not in independent_blocks:
            raise RuntimeError(f"Missing independent term: {title}")
    for g in TOPIC_GROUP_BAND_MAP:
        if g not in groups:
            raise RuntimeError(f"Missing topic group: {g}")
    for old_id in CLUSTER_TITLES:
        if old_id not in cluster_blocks:
            raise RuntimeError(f"Missing cluster: {old_id}")

    anchor_home = build_anchor_home_map(independent_blocks, groups, cluster_blocks)

    band_contents: dict[str, str] = {}
    for filename, spec in NEW_FILES_SPEC.items():
        content = build_band_file(filename, spec, independent_blocks, groups, cluster_blocks)
        content = rewrite_ch5_links(content, anchor_home)
        content = rewrite_fragment_links(content, anchor_home)
        band_contents[filename] = content
        path = ROOT / filename
        if args.dry_run:
            print(f"Would write {path} ({len(content)} bytes)")
        else:
            path.write_text(content, encoding="utf-8")
            print(f"Wrote {path}")

    new_part_a = build_part_a(pre, meta, footer, anchor_home, ROOT)
    new_part_a = rewrite_ch5_links(new_part_a, anchor_home)
    new_part_a = rewrite_fragment_links(new_part_a, anchor_home)
    if args.dry_run:
        print(f"Would rewrite {ROOT / PART_A}")
    else:
        (ROOT / PART_A).write_text(new_part_a, encoding="utf-8")
        print(f"Rewrote {ROOT / PART_A}")

    archive_dir = ROOT / "archive" / "core_ch5_retired"
    if not args.dry_run:
        archive_dir.mkdir(parents=True, exist_ok=True)
    for old_file, (new_file, note) in REDIRECT_MAP.items():
        stub = build_redirect_stub(old_file, new_file, note)
        dest = archive_dir / old_file
        if args.dry_run:
            print(f"Would archive stub {dest}")
            print(f"Would remove live {ROOT / old_file}")
        else:
            dest.write_text(stub, encoding="utf-8")
            live = ROOT / old_file
            if live.exists():
                live.unlink()
            print(f"Archived stub {dest}; removed {live}")

    skip = set(NEW_FILES_SPEC) | {PART_A}
    changed = 0
    for path in iter_corpus_files(ROOT):
        if path.name in skip:
            continue
        original = path.read_text(encoding="utf-8")
        updated = renumber_cluster_refs(original)
        updated = rewrite_ch5_links(updated, anchor_home)
        if updated != original:
            changed += 1
            if not args.dry_run:
                path.write_text(updated, encoding="utf-8")
    print(f"{'Would update' if args.dry_run else 'Updated'} {changed} corpus files")

    if not args.dry_run:
        for filename, content in band_contents.items():
            fixed = rewrite_ch5_links(content, anchor_home)
            if fixed != content:
                (ROOT / filename).write_text(fixed, encoding="utf-8")

    write_evidence(ROOT, args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
