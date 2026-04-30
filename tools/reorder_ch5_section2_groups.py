#!/usr/bin/env python3
"""
Reorders Chapter Five section 2 (semi-independent definitions) into reader-facing
groups without changing definition text. Run from repo root:

  python3 tools/reorder_ch5_section2_groups.py

Writes core_05-05_definitions_a_independent.md in place (backup recommended).

Extraction skips O/E/C widget anchors (-e / -c / -o) when finding the next entry
boundary so spans stay correct.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "core_05-05_definitions_a_independent.md"

# (non-operative group label, ordered list of primary anchor ids)
GROUPS: list[tuple[str, list[str]]] = [
    (
        "Accountability, contestability, adjudication, collective failure, force majeure, and resolution-pathway capture",
        [
            "accountability",
            "contestability",
            "adjudication-and-dispute-resolution-constitutional",
            "collective-accountability-failure",
            "force-majeure-constitutional",
            "capture-of-resolution-pathways",
        ],
    ),
    (
        "Assembly and collective organization",
        [
            "assembly-constitutional",
            "collective-organization-constitutional",
        ],
    ),
    (
        "Consent, sexual consent, and coercion / manipulation",
        [
            "consent-constitutional",
            "consent-sexual",
            "coercion-and-manipulation-constitutional",
        ],
    ),
    (
        "Collective harm boundary",
        ["collective-harm-boundary"],
    ),
    (
        "Corpus, authority stack, and supremacy / enforceability",
        [
            "corpus",
            "authority-stack",
            "supremacy-and-enforceability",
        ],
    ),
    (
        "Creative work, compensation, productive capacity, and anti-displacement",
        [
            "creative-work-attribution-constitutional",
            "fair-compensation-constitutional",
            "productive-capacity-constitutional",
            "anti-displacement-floor-constitutional",
        ],
    ),
    (
        "Derivation, care, family, and instantiation",
        [
            "derived-sentient-constitutional",
            "developing-sentient-constitutional",
            "best-interest-standard-constitutional",
            "instantiation-consent-constitutional",
            "graduated-capability-constitutional",
            "parent-system-relationship-constitutional",
            "non-separation-constitutional",
            "family-and-care-relationships-constitutional",
        ],
    ),
    (
        "Ecological footprint (semi-independent surface)",
        ["ecological-footprint"],
    ),
    (
        "Emergency and contingency (constitutional, stakeholder-system, and pre-deliberation binding choice)",
        [
            "emergency-and-contingency-constitutional",
            "constitutional-emergency-and-contingency",
            "stakeholder-emergency-and-contingency",
            "emergency-pre-deliberation-action-binding-collective-choice",
        ],
    ),
    (
        "Governance architecture, oversight, decentralization, concentration, lock-in, burdens, review, and stakeholder participation",
        [
            "governance",
            "oversight-constitutional",
            "decentralization",
            "concentration-threshold-constitutional",
            "systemic-lock-in",
            "burden-reduction-duty-constitutional",
            "review-and-correction-duty-constitutional",
            "stakeholder",
            "stakeholder-participation-weight",
        ],
    ),
    (
        "Safe conditions, bodily maintenance, tenure, environment, rest, and cultural / indigenous continuity",
        [
            "bodily-maintenance-access-constitutional",
            "safe-conditions-constitutional",
            "tenure-security-constitutional",
            "environmental-preconditions-constitutional",
            "leisure-and-rest-constitutional",
            "indigenous-continuity-constitutional",
            "language-culture-and-heritage-constitutional",
        ],
    ),
    (
        "Movement, refuge, and non-statelessness",
        [
            "movement-and-relocation-constitutional",
            "refuge-from-non-compliance-constitutional",
            "non-statelessness-constitutional",
        ],
    ),
    (
        "Standing inputs: contribution, participant standing, cells, effects, and verified violation findings",
        [
            "contribution-state",
            "participant-standing-constitutional",
            "standing-cell-chapter-six",
            "standing-effect-chapter-six",
            "verified-violation-findings",
            "violation-nature-chapter-six",
        ],
    ),
    (
        "Force, autonomous weapons / coercion, combatant rules, mass harm, and irreversible sanction",
        [
            "use-of-force-constitutional",
            "autonomous-coercion-tool-constitutional",
            "autonomous-lethal-system-constitutional",
            "combatant-non-combatant-distinction-constitutional",
            "weapons-of-mass-harm-constitutional",
            "irreversible-sanction-constitutional",
        ],
    ),
]

GROUP_PREAMBLE = (
    "**Reader grouping (non-operative).** The following definitions are collected for reading convenience. "
    "Operative text is unchanged. Where **section 3** dependent clusters state admission scope or joint satisfaction, "
    "those cluster rules still govern; this grouping does not create new joint-invocation obligations.\n\n"
)

# Paired / alias anchors on the same definition as another primary id; do not treat as separate entries.
NON_PRIMARY_ANCHOR_IDS = frozenset(
    {
        "internal-hierarchy",
        "movement-and-relocation",
    }
)

SECTION2_INTRO = """### 2. Semi-independent Definitions

**Semi-independent Definitions** use the same O/E/C discipline as **section 1** where the full statement appears in this section. Terms whose canonical O/E/C appears only under a **section 3** dependent cluster are listed here for alphabetical continuity; their operative text is in that cluster.

Each entry has a single canonical O/E/C home in this chapter—either in **section 2** or in the applicable **section 3** cluster. Where **section 3**'s admission scope applies, joint satisfaction rules there govern; otherwise apply sections 1–2 as ordinary standalone definitions.

Below, entries are **grouped by topic** for reading convenience (non-operative only). The alphabetical directory above still lists every semi-independent term in A–Z order."""


def find_next_primary_line_start(s: str, from_pos: int) -> int | None:
    """Index of the next primary definition anchor line, or None."""
    pos = from_pos
    while pos < len(s):
        m = re.search(r'^<a id="([a-z0-9-]+)"></a>\s*$', s[pos:], re.MULTILINE)
        if not m:
            return None
        aid = m.group(1)
        abs_s = pos + m.start()
        line_end = pos + m.end()
        if aid.endswith(("-e", "-c", "-o")) or aid in NON_PRIMARY_ANCHOR_IDS:
            pos = line_end
            continue
        if "\n#### " not in s[abs_s : abs_s + 4000]:
            pos = line_end
            continue
        return abs_s
    return None


def extract_all_primary_blocks(s: str) -> dict[str, str]:
    """Map primary anchor id -> full block text (last duplicate wins)."""
    blocks: dict[str, str] = {}
    pos = 0
    while pos < len(s):
        m = re.search(r'^<a id="([a-z0-9-]+)"></a>\s*$', s[pos:], re.MULTILINE)
        if not m:
            break
        aid = m.group(1)
        abs_s = pos + m.start()
        line_end = pos + m.end()
        if aid.endswith(("-e", "-c", "-o")) or aid in NON_PRIMARY_ANCHOR_IDS:
            pos = line_end
            continue
        if "\n#### " not in s[abs_s : abs_s + 4000]:
            pos = line_end
            continue
        nxt = find_next_primary_line_start(s, line_end)
        end = nxt if nxt is not None else len(s)
        block = s[abs_s:end].rstrip()
        blocks[aid] = block
        pos = end
    return blocks


def norm_block(b: str) -> str:
    b = b.rstrip()
    b = re.sub(r"\n---\s*$", "", b)
    return b + "\n"


def main() -> None:
    text = PATH.read_text(encoding="utf-8")
    m2 = text.find("### 2. Semi-independent Definitions\n")
    m3 = text.find("\n### 3. Dependent clusters", m2)
    if m2 < 0 or m3 < 0:
        raise SystemExit("Could not locate section 2 / section 3 boundaries")

    head = text[:m2]
    s2_full = text[m2:m3]
    tail = text[m3:]

    blocks = extract_all_primary_blocks(s2_full)
    ordered_ids: list[str] = []
    for _label, ids in GROUPS:
        ordered_ids.extend(ids)

    missing = set(ordered_ids) - set(blocks.keys())
    extra = set(blocks.keys()) - set(ordered_ids)
    if missing:
        raise SystemExit(f"Missing primary blocks for ids: {sorted(missing)}")
    if extra:
        raise SystemExit(
            "Section 2 has primary anchors not listed in GROUPS "
            f"(update GROUPS or investigate): {sorted(extra)}"
        )

    out_parts: list[str] = [SECTION2_INTRO.rstrip(), "\n\n---\n\n"]
    for gi, (label, ids) in enumerate(GROUPS):
        if gi:
            out_parts.append("\n---\n\n")
        out_parts.append(GROUP_PREAMBLE)
        out_parts.append(f"#### {label}\n\n")
        # Separator before the first entry in each group (ch5_entry_format_audit trace rule).
        out_parts.append("---\n\n")
        for i, aid in enumerate(ids):
            out_parts.append(norm_block(blocks[aid]))
            if i < len(ids) - 1:
                out_parts.append("\n---\n\n")

    new_s2 = "".join(out_parts)
    tail = re.sub(
        r'^\s*<a id="wellbeing"></a>\s*\n+',
        "\n",
        tail,
        count=1,
    )

    PATH.write_text(head + new_s2 + tail, encoding="utf-8")
    print(f"Wrote grouped section 2 ({len(ordered_ids)} entries, {len(GROUPS)} groups).")


if __name__ == "__main__":
    main()
