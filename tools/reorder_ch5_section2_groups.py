#!/usr/bin/env python3
"""
Reorders Chapter Five section 2 (semi-independent definitions) into reader-facing
groups without changing definition text. Run from repo root:

  python3 tools/reorder_ch5_section2_groups.py

Writes ``core_05-05_definitions_b_semi_independent.md`` in place (backup recommended).

Primary anchors listed under ``GROUPS`` are emitted in reader-facing order.
By default, the script **fails** if Part B contains a primary anchor not listed
in ``GROUPS`` (or if ``GROUPS`` references a missing anchor). Pass
``--relax-unlisted`` to append unlisted anchors under an editorial heading
instead (with a stderr warning).

Extraction skips O/E/C widget anchors (-e / -c / -o) when finding the next entry
boundary so spans stay correct.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_PART_B  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]

# (non-operative group label, ordered list of primary anchor ids)
GROUPS: list[tuple[str, list[str]]] = [
    (
        "Accountability, Contestability, Adjudication, Resolution Integrity, and Collective Failure",
        [
            "accountability",
            "contestability",
            "adjudication-and-dispute-resolution-constitutional",
            "collective-accountability-failure",
            "capture-of-resolution-pathways",
            "force-majeure-constitutional",
        ],
    ),
    (
        "Sentience Status, Animal Life, Derivation, and Development",
        [
            "animal-life-sentient-life-and-sentience-status-cluster",
            "animal-life-constitutional",
            "contested-sentient-life-constitutional",
            "sentient",
            "sentience-non-exclusion",
            "sentience-status-adjudication-constitutional",
            "derived-sentient-constitutional",
            "developing-sentient-constitutional",
        ],
    ),
    (
        "Agency, Expression, Assembly, Consent, and Coercion",
        [
            "expression-constitutional",
            "assembly-constitutional",
            "collective-organization-constitutional",
            "consent-constitutional",
            "consent-sexual",
            "coercion-and-manipulation-constitutional",
        ],
    ),
    (
        "Protected Status, Fairness, and Anti-Discrimination",
        [
            "protected-characteristics-constitutional",
            "protected-characteristic-proxying-and-disparate-impact",
            "protected-intimate-signal-gating",
            "protected-commercial-sexual-services-status-and-article-x-c-circumvention",
        ],
    ),
    (
        "Family, Care, and Instantiation",
        [
            "best-interest-standard-constitutional",
            "instantiation-consent-constitutional",
            "graduated-capability-constitutional",
            "parent-system-relationship-constitutional",
            "non-separation-constitutional",
            "family-and-care-relationships-constitutional",
        ],
    ),
    (
        "Creative Work, Compensation, Productive Capacity, and Anti-Displacement",
        [
            "creative-work-attribution-constitutional",
            "fair-compensation-constitutional",
            "productive-capacity-constitutional",
            "anti-displacement-floor-constitutional",
        ],
    ),
    (
        "Governance, Oversight, Participation, and Stewardship",
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
        "Materiality, Impact, Risk, and Classification Integrity",
        [
            "material",
            "material-degradation",
            "material-impact",
            "material-risk",
            "materiality-determination",
            "materiality-integrity-constraint",
            "materiality-under-uncertainty",
            "system-system-boundaries-and-boundary-integrity-cluster",
            "system",
            "system-boundaries",
            "system-boundary-integrity",
        ],
    ),
    (
        "Environment, Ecological Footprint, Cultural Continuity, and Heritage",
        [
            "ecological-footprint",
            "environmental-preconditions-constitutional",
            "indigenous-continuity-constitutional",
            "language-culture-and-heritage-constitutional",
        ],
    ),
    (
        "Survival Conditions, Tenure, Bodily Maintenance, and Rest",
        [
            "bodily-maintenance-access-constitutional",
            "safe-conditions-constitutional",
            "tenure-security-constitutional",
            "leisure-and-rest-constitutional",
        ],
    ),
    (
        "Emergency, Movement, Refuge, and Continuity of Recognition",
        [
            "emergency-and-contingency-constitutional",
            "constitutional-emergency-and-contingency",
            "stakeholder-emergency-and-contingency",
            "emergency-pre-deliberation-action-binding-collective-choice",
            "movement-and-relocation-constitutional",
            "refuge-from-non-compliance-constitutional",
            "non-statelessness-constitutional",
        ],
    ),
    (
        "Collective Harm and Boundary",
        ["collective-harm-boundary"],
    ),
    (
        "Standing Inputs: Contribution, Participant Standing, Cells, Effects, and Violation Findings",
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
        "Use of Force, Autonomous Coercion, Mass Harm, and Irreversible Sanction",
        [
            "use-of-force-constitutional",
            "autonomous-coercion-tool-constitutional",
            "autonomous-lethal-system-constitutional",
            "combatant-non-combatant-distinction-constitutional",
            "weapons-of-mass-harm-constitutional",
            "irreversible-sanction-constitutional",
        ],
    ),
    (
        "Corpus, Authority Stack, Supremacy, and Enforceability",
        [
            "corpus",
            "authority-stack",
            "supremacy-and-enforceability",
        ],
    ),
]

GROUP_LABELS = frozenset(
    label
    for label, _ids in GROUPS
) | frozenset(
    {
        "Accountability, contestability, adjudication, collective failure, force majeure, and resolution-pathway capture",
        "Animal Life, Sentient Life, Sentience Status, Derivation, and Development",
        "Assembly, expression, and collective organization",
        "Assembly and collective organization",
        "Consent, sexual consent, and coercion / manipulation",
        "Protected characteristics, proxying, intimate-signal gating, and Article X-C status",
        "Collective Harm Boundary",
        "Corpus, authority stack, and supremacy / enforceability",
        "Creative Work, Compensation, Productive Capacity, and Anti-Displacement",
        "Derivation, care, family, and instantiation",
        "Care, family, and instantiation",
        "Ecological footprint (semi-independent surface)",
        "Emergency and contingency (constitutional, stakeholder-system, and pre-deliberation binding choice)",
        "Governance architecture, oversight, decentralization, concentration, lock-in, burdens, review, and stakeholder participation",
        "Safe conditions, bodily maintenance, tenure, environment, rest, and cultural / indigenous continuity",
        "Materiality, material impact, and material risk",
        "Movement, refuge, and non-statelessness",
        "Standing Inputs: Contribution, Participant Standing, Cells, Effects, and Violation Findings",
        "Force, autonomous weapons / coercion, combatant rules, mass harm, and irreversible sanction",
    }
)

# Paired / alias anchors on the same definition as another primary id; do not treat as separate entries.
NON_PRIMARY_ANCHOR_IDS = frozenset(
    {
        "internal-hierarchy",
        "movement-and-relocation",
        "sentient-composite",
    }
)

SECTION2_INTRO = """### 2. Semi-independent Definitions

**Semi-independent Definitions** use the same O/E/C discipline as **section 1**. Where related semi-independent definitions must be read together, their reader-facing family context, admission scope, and joint-invocation / anti-bypass rule live in this section beside the relevant entries.

Each **semi-independent** definition has its single canonical O/E/C home in **section 2** only (Part B). **Dependent-cluster** definitions—canonical full O/E/C for cluster-owned members—live **only** in **section 3** (Part C). Where **section 3** joint-invocation applies, satisfy those clusters together with applicable **section 1** and **section 2** definitions as each cluster routes by pointer; semi-independent canonical bodies are **not** relocated into section 3.

Below, entries are **grouped by topic** for reading convenience (non-operative only). The alphabetical directory in [core_05-05_definitions_a_independent.md](core_05-05_definitions_a_independent.md#chapter-five-foundational-definitions) still lists every semi-independent term in A–Z order."""


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
    lines = b.rstrip().splitlines()
    while lines:
        while lines and not lines[-1].strip():
            lines.pop()
        if lines and lines[-1].strip() == "---":
            lines.pop()
            continue
        if lines and lines[-1].startswith("#### "):
            label = lines[-1].removeprefix("#### ").strip()
            if label in GROUP_LABELS:
                lines.pop()
                continue
        break
    return "\n".join(lines).rstrip() + "\n"


def reorder_section2_groups(
    root: Path | None = None, *, strict: bool = True
) -> int:
    """Rewrite Part B section 2 into reader-facing groups. Returns 0 on success.

    When ``strict`` is True (default), require every Part B primary anchor to
    appear exactly in ``GROUPS`` and every ``GROUPS`` id to exist in the file.
    When ``strict`` is False, anchors missing from ``GROUPS`` are appended after
    grouped content with a stderr warning.
    """
    base = root if root is not None else ROOT
    path = base / CH5_PART_B
    text = path.read_text(encoding="utf-8")
    m2 = text.find("### 2. Semi-independent Definitions\n")
    m3 = text.find("\n### 3. Dependent clusters", m2)
    if m2 < 0:
        print("Could not locate section 2 boundary", file=sys.stderr)
        return 1
    if m3 < 0:
        m3 = len(text)

    head = text[:m2]
    s2_full = text[m2:m3]
    tail = text[m3:]

    blocks = extract_all_primary_blocks(s2_full)
    ordered_ids: list[str] = []
    for _label, ids in GROUPS:
        ordered_ids.extend(ids)

    missing = set(ordered_ids) - set(blocks.keys())
    extra = sorted(set(blocks.keys()) - set(ordered_ids))
    if missing:
        print(
            f"Missing primary blocks for ids: {sorted(missing)}", file=sys.stderr
        )
        return 1
    if extra and strict:
        print(
            "Section 2 has primary anchors not listed in GROUPS "
            f"(update GROUPS or investigate): {extra}",
            file=sys.stderr,
        )
        return 1
    if extra:
        print(
            f"Warning: appending {len(extra)} Part B primary anchor(s) not listed in "
            "GROUPS under an editorial heading; tighten GROUPS when convenient.",
            file=sys.stderr,
        )

    out_parts: list[str] = [SECTION2_INTRO.rstrip(), "\n\n---\n\n"]
    for gi, (label, ids) in enumerate(GROUPS):
        if gi:
            out_parts.append("\n---\n\n")
        out_parts.append(f"#### {label}\n\n")
        # Separator before the first entry in each group (ch5_entry_format_audit trace rule).
        out_parts.append("---\n\n")
        for i, aid in enumerate(ids):
            out_parts.append(norm_block(blocks[aid]))
            if i < len(ids) - 1:
                out_parts.append("\n---\n\n")

    if extra:
        out_parts.append("\n---\n\n")
        out_parts.append(
            "#### Ungrouped semi-independent entries (non-operative placement)\n\n"
        )
        out_parts.append("---\n\n")
        for i, aid in enumerate(extra):
            out_parts.append(norm_block(blocks[aid]))
            if i < len(extra) - 1:
                out_parts.append("\n---\n\n")

    new_s2 = "".join(out_parts)
    tail = re.sub(
        r'^\s*<a id="wellbeing"></a>\s*\n+',
        "\n",
        tail,
        count=1,
    )

    path.write_text(head + new_s2 + tail, encoding="utf-8")
    detail = f"{len(ordered_ids)} grouped"
    if extra:
        detail += f", {len(extra)} ungrouped"
    print(f"Wrote section 2 ({detail} entries; {len(GROUPS)} reader groups).")
    return 0


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--relax-unlisted",
        action="store_true",
        help="Append Part B primary anchors not listed in GROUPS (stderr warning) "
        "instead of failing.",
    )
    args = p.parse_args()
    raise SystemExit(reorder_section2_groups(ROOT, strict=not args.relax_unlisted))


if __name__ == "__main__":
    main()
