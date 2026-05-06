"""One-shot helper: convert legacy ``Definitions: ...`` lines inside Trace
widgets into standalone **Definitions · Evaluation · Compliance (D/E/C)**
widgets (or the single-concept ``Definition:`` inline line when exactly one
concept is invoked).

Scope (per ``doc_architecture.md`` rule 12, 2026-04-16 D/E/C split):
- Operates only on consuming files — principles and rights parts. Runs are
  idempotent; already-converted sections are skipped.
- Does **not** add widgets to sections that never carried a ``Definitions:``
  line. That expansion is author-by-hand invocation analysis and is out of
  scope for this mechanical pass.
- Leaves ``core_05-05_definitions_a_independent.md`` alone.

Input ``Definitions:`` formats handled:

1. Inline bare-text: ``- Definitions: Wellbeing; Materiality; Foreseeability.``
2. Inline linked: ``- Definitions: [A](url#slug); [B](url#slug).``
3. Multi-line linked: ``- Definitions:`` followed by indented ``  - [A](url)`` rows.

Concept-name qualifiers (for example, ``Proxy Divergence where claimed wellbeing
rests on substitute metrics``) are stripped — the widget row uses the concept
name and its canonical Chapter Five slug. Any concept name that cannot be
resolved against the Chapter Five slug table is reported on stderr and the
section is **not** converted (manual intervention required).

Run from the repository root:

    python3 tools/convert_definitions_to_dec_widget.py

Targets (hard-coded): the five consumer files that currently carry
``Definitions:`` lines. Edit ``TARGETS`` to extend.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


CH5 = Path("core_05-05_definitions_a_independent.md")
CH5_PATH = "core_05-05_definitions_a_independent.md"
CH5C_PATH = "core_05-05_definitions_c_dependent_clusters.md"


def ch5_href_base(slug: str) -> str:
    """Trust and Trustworthiness (and trustworthiness sub-anchors) live in Part C."""
    if slug == "trust" or slug == "trustworthiness" or slug.startswith(
        "trustworthiness-"
    ):
        return CH5C_PATH
    return CH5_PATH

TARGETS = [
    Path("core_00-01_principles.md"),
    Path("core_09-09_rights_part_a.md"),
    Path("core_09-09_rights_part_b.md"),
    Path("core_09-09_rights_part_c.md"),
    Path("core_09-09_rights_part_d.md"),
]

TRACE_SUMMARY_RE = re.compile(
    r'^<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>\s*$'
)
DETAILS_OPEN_RE = re.compile(r"^<details>\s*$")
DETAILS_CLOSE_RE = re.compile(r"^</details>\s*$")

DEFINITIONS_INLINE_RE = re.compile(r"^- Definitions:\s*(.+?)\s*$")
DEFINITIONS_BLOCK_HEADER_RE = re.compile(r"^- Definitions:\s*$")
DEFINITIONS_SUBBULLET_RE = re.compile(r"^\s{2,}-\s+(.+?)\s*$")

MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
DEC_SUMMARY_STR = (
    '<summary><strong><span style="color: #2563eb;">'
    "Definitions · Evaluation · Compliance</span></strong></summary>"
)


# Concepts that are clustered heads in Chapter Five and therefore do not carry
# -e / -c anchors. Widget rows for these point all three letters to the
# heading.
CLUSTERED_HEADS = {
    "accountability-contestability-and-collective-accountability-failure-cluster",
    "incentive-alignment",
    "innovation-reward-and-anti-enclosure",
    "trust-degradation-and-misleading-reliance-constitutional",
    "trust-degradation-and-misleading-reliance",
}

# Concepts that have an O and E but no direct C bullet in Chapter Five. Widget
# rows for these keep the E link but fall back the C link to the heading so
# the reader still lands somewhere sensible. Content gaps tracked separately.
#
# Note (2026-04-17): ``trustworthiness`` and ``sentience-non-exclusion`` were
# pruned from this set once their top-level ``- C:`` bullets were authored in
# Chapter Five (they also received a ``-c`` anchor). The set is intentionally
# left in place so that any future concept that develops the same content gap
# can be re-added here without reshaping the converter.
MISSING_C: set[str] = set()

# Title anchor remains an alphabetical stub; O/E/C bullets live under the
# Self-Determination / Meaningful Agency / Educational Agency cluster.
STUB_CLUSTER_OEC: frozenset[str] = frozenset(
    {
        "educational-agency",
        "meaningful-agency",
        "self-determination-constitutional",
    }
)

# Known pre-existing slug corrections: consumer files occasionally carried a
# Chapter Five href whose slug did not actually exist (the heading is defined
# under a different slug). Map bad -> good here so the converter emits the
# canonical anchor regardless of what the source had. Keys and values are
# slugs (no ``#`` prefix).
SLUG_CORRECTIONS = {
    "coercion-and-manipulation": "coercion-and-manipulation-constitutional",
}


def build_ch5_slug_table() -> dict[str, str]:
    """Walk Chapter Five and build a name -> slug table, plus known aliases.

    The table keys are lower-case concept-display names as they commonly appear
    in consumer `Definitions:` lines. Where a concept's display name and its
    explicit anchor slug differ (for example, `Coercion and Manipulation` whose
    slug is `coercion-and-manipulation-constitutional`), both forms are
    captured through the canonical slug.
    """

    text = CH5.read_text(encoding="utf-8").splitlines()
    table: dict[str, str] = {}

    i = 0
    while i < len(text):
        line = text[i]
        m_h = re.match(r"^####\s+(.+?)\s*$", line)
        if not m_h:
            i += 1
            continue
        heading = m_h.group(1)

        # Explicit anchor is the last non-blank line above.
        slug: str | None = None
        j = i - 1
        while j >= 0 and text[j].strip() == "":
            j -= 1
        if j >= 0:
            m_a = re.match(r'^<a id="([^"]+)"></a>\s*$', text[j])
            if m_a:
                slug = m_a.group(1)
        if slug is None:
            # Auto-slug the heading.
            s = heading.lower()
            s = re.sub(r"[^\w\s-]", "", s)
            s = re.sub(r"\s+", "-", s)
            s = re.sub(r"-+", "-", s).strip("-")
            slug = s

        table[heading.lower()] = slug

        # Common stripped-parenthetical aliases ("Safety (Constraint)" -> "safety").
        no_parens = re.sub(r"\s*\([^)]*\)\s*", "", heading).strip()
        if no_parens and no_parens.lower() not in table:
            table[no_parens.lower()] = slug

        i += 1

    # Manual aliases for concepts that appear in consumer Definitions lines but
    # are not an exact heading match at the ``####`` level in Chapter Five, or
    # whose display name in a consumer file differs slightly from the Chapter
    # Five heading. Slugs are the **actual** anchors present in Chapter Five
    # (verified against the anchor-insertion pass); do not invent slugs.
    manual_aliases = {
        # Simple name-is-slug concepts.
        "harm": "harm",
        "risk": "risk",
        "dependency": "dependency",
        "wellbeing": "wellbeing",
        "epistemic integrity": "epistemic-integrity",
        "trust": "trust",
        "trustworthiness": "trustworthiness",
        "feasibility": "feasibility",
        "necessity": "necessity",
        "proportionality": "proportionality",
        "meaningful agency": "meaningful-agency",
        "avoidable burden": "avoidable-burden",
        "constitutional efficiency": "constitutional-efficiency",
        "proxy divergence": "proxy-divergence",
        "existential risk": "existential-risk",
        "governance": "governance",
        "stakeholder": "stakeholder",
        "good faith": "good-faith",
        "surveillance boundary": "surveillance-boundary",
        # Bare-text names whose Chapter Five anchor has a suffix.
        "foreseeability": "foreseeability-diligence",
        "safety": "safety-constraint",
        "truth": "truth-constitutional-constraint",
        "truth (constitutional constraint)": "truth-constitutional-constraint",
        "productive capacity": "productive-capacity-constitutional",
        "productive capacity (constitutional)": "productive-capacity-constitutional",
        "coercion and manipulation": "coercion-and-manipulation-constitutional",
        "coercion and manipulation (constitutional)": "coercion-and-manipulation-constitutional",
        "procedural fairness": "procedural-fairness-constitutional",
        "reversibility": "reversibility-constitutional",
        "participant standing": "participant-standing-constitutional",
        "participant standing (constitutional)": "participant-standing-constitutional",
        "oversight": "oversight-constitutional",
        "oversight (constitutional)": "oversight-constitutional",
        "privacy": "privacy-informational",
        "privacy (informational)": "privacy-informational",
        "protected characteristics": "protected-characteristics-constitutional",
        "protected internal-state boundary": "protected-internal-state-boundary-constitutional",
        "redress and remediation": "redress-and-remediation-constitutional",
        "self-determination": "self-determination-constitutional",
        "substantive fairness": "substantive-fairness-constitutional",
        "force majeure": "force-majeure-constitutional",
        "emergency and contingency": "emergency-and-contingency-constitutional",
        "intergenerational responsibility": "intergenerational-responsibility-constitutional",
        "consent": "consent-constitutional",
        "consent and sexual consent": "consent-and-sexual-consent-cluster",
        "freedom": "freedom-bounded-agency",
        "freedom (bounded agency)": "freedom-bounded-agency",
        "harm minimization (tradeoff selection)": "harm-minimization-tradeoff-selection",
        "ecological integrity": "ecological-integrity-constitutional",
        "non-imposition (cooperative interaction)": "non-imposition-cooperative-interaction",
        "environmental preconditions": "environmental-preconditions-constitutional",
        "adjudication and dispute resolution": "adjudication-and-dispute-resolution-constitutional",
        # Cluster heads and cluster-component concepts (level-5 entries).
        "materiality": "materiality-determination",
        "materiality determination": "materiality-determination",
        "material impact": "material-impact",
        "material risk": "material-risk",
        "irreversible harm": "irreversible-harm",
        "psychological harm": "psychological-harm",
        "system capture": "system-capture",
        "system boundaries": "system-boundaries",
        "system boundary integrity": "system-boundary-integrity",
        "sentience (non-exclusion)": "sentience-non-exclusion",
        # Incentive Alignment and Innovation Reward: cluster heads without
        # direct O/E/C bullets. Listed in CLUSTERED_HEADS below so rows point
        # all three letters to the heading.
        "incentive alignment": "incentive-alignment",
        "incentive alignment (constitutional)": "incentive-alignment",
        "innovation reward and anti-enclosure": "innovation-reward-and-anti-enclosure",
        # Trust Degradation cluster: its top-level anchor in Chapter Five is
        # explicit; map the constitutional-suffixed alias variants.
        "trust degradation and misleading reliance": "trust-degradation-and-misleading-reliance-constitutional",
        "trust degradation and misleading reliance (constitutional)": "trust-degradation-and-misleading-reliance-constitutional",
        # Compound aliases observed in consumer Definitions lines.
        "educational agency": "educational-agency",
        "classification-scaled governance": "classification-scaled-governance",
        "cascading failure": "cascading-failure",
        "ecological footprint": "ecological-footprint",
        "ecological integrity, footprint, and sustainability": "ecological-integrity-footprint-and-sustainability-cluster",
        "ecological integrity and sustainability": "ecological-integrity-and-sustainability-cluster",
        "stakeholder participation weight": "stakeholder-participation-weight",
        "standing state, contribution, and violation": "standing-state-contribution-and-violation-cluster",
        "contribution state": "contribution-state",
        "participant standing": "participant-standing-constitutional",
        "participant standing (constitutional)": "participant-standing-constitutional",
        "standing cell": "standing-cell-chapter-six",
        "standing effect": "standing-effect-chapter-six",
        "verified violation findings": "verified-violation-findings",
        "violation nature": "violation-nature-chapter-six",
        "sentience status, subclasses, and evaluation": "sentience-status-subclasses-and-evaluation-cluster",
        "sentience status and evaluation": "sentience-status-and-evaluation-cluster",
        "derived sentient": "derived-sentient-constitutional",
        "derived sentient (constitutional)": "derived-sentient-constitutional",
        "developing sentient": "developing-sentient-constitutional",
        "developing sentient (constitutional)": "developing-sentient-constitutional",
        "collective accountability failure": "collective-accountability-failure",
        "accountability, contestability, and collective accountability failure": "accountability-contestability-and-collective-accountability-failure-cluster",
        "accountability, contestability, adjudication and dispute resolution, and collective accountability failure": "accountability-contestability-and-collective-accountability-failure-cluster",
        "accountability and collective accountability failure": "accountability-and-collective-accountability-failure-cluster",
        "systemic lock-in": "systemic-lock-in",
        "protected reporting (whistleblowing)": "protected-reporting-whistleblowing",
        "innovation reward": "innovation-reward-and-anti-enclosure",
        "transparency": "transparency",
        "auditability": "auditability",
        "contestability": "contestability",
        "accountability": "accountability",
        "dignity and equal moral standing": "dignity-and-equal-moral-standing",
        "corpus": "corpus",
        "authority stack": "authority-stack",
        "corpus, authority stack, supremacy, and enforceability": "corpus-authority-stack-supremacy-and-enforceability-cluster",
        "source authority, supremacy, and enforceability": "source-authority-supremacy-and-enforceability-cluster",
        "forum family, sentient": "forum-family-sentient",
        "forum family, technical": "forum-family-technical",
        "technical forum domains": "technical-forum-domains",
        "forum family, institutional": "forum-family-institutional",
        "forum family, environment": "forum-family-environment",
        "forum family, integrity": "forum-family-integrity",
        "forum family, constitutional": "forum-family-constitutional",
        "constitutional forums": "constitutional-forums",
        "constitutional review body": "constitutional-forums",
    }
    for alias, slug in manual_aliases.items():
        table.setdefault(alias, slug)

    return table


def parse_concept_item(raw: str, slug_table: dict[str, str]) -> tuple[str, str] | None:
    """Extract (display_name, slug) from a single `Definitions:` item.

    Handles three shapes:
    - Markdown link: ``[Name](path#slug)`` (optionally with trailing qualifier).
    - Bare text: ``Name`` or ``Name followed by where-clause qualifier``.

    Returns None if the concept cannot be resolved.
    """

    item = raw.strip().rstrip(".").strip()
    if not item:
        return None

    # Markdown link first.
    m = MD_LINK_RE.search(item)
    if m:
        name = m.group(1).strip()
        href = m.group(2).strip()
        if "#" in href:
            slug = href.split("#", 1)[1]
        else:
            # Fall back to table.
            slug = slug_table.get(name.lower())
            if slug is None:
                return None
        # Apply known pre-existing slug corrections.
        slug = SLUG_CORRECTIONS.get(slug, slug)
        return name, slug

    # Bare text. Match the longest known concept name from the table as a
    # prefix of the item.
    lower = item.lower()
    best_name: str | None = None
    best_len = 0
    for key in slug_table:
        if lower.startswith(key):
            # Require a word boundary after the match so "harm" doesn't
            # swallow "harm minimization".
            after = item[len(key) : len(key) + 1]
            if after and after not in (" ", ",", ";", ".", ")", ":"):
                continue
            if len(key) > best_len:
                best_name = key
                best_len = len(key)
    if best_name is None:
        return None

    display = item[: best_len]
    # Normalize display-name casing to match whatever is in the slug table key,
    # but prefer the original capitalization from the source item when the
    # source is already TitleCased.
    if display.strip().islower():
        display = display.title()
    slug = slug_table[best_name]
    return display.strip(), slug


def _targets(slug: str) -> tuple[str, str, str]:
    """Return (O, E, C) anchor URLs for the given concept slug, honoring
    CLUSTERED_HEADS (all three to the heading) and MISSING_C (C falls back to
    the heading)."""

    file_base = ch5_href_base(slug)
    base = f"{file_base}#{slug}"
    if slug in CLUSTERED_HEADS:
        return base, base, base
    if slug in STUB_CLUSTER_OEC:
        return (
            f"{file_base}#{slug}-o",
            f"{file_base}#{slug}-e",
            f"{file_base}#{slug}-c",
        )
    e = f"{file_base}#{slug}-e"
    if slug in MISSING_C:
        return base, e, base
    c = f"{file_base}#{slug}-c"
    return base, e, c


def format_row(name: str, slug: str) -> str:
    """Return the widget-row Markdown for a single concept."""

    base = f"{ch5_href_base(slug)}#{slug}"
    o, e, c = _targets(slug)
    return f"- [{name}]({base}) · [O]({o}) · [E]({e}) · [C]({c})"


def format_inline_line(name: str, slug: str) -> str:
    """Return the single-concept inline line, including bold-blue prefix."""

    base = f"{ch5_href_base(slug)}#{slug}"
    o, e, c = _targets(slug)
    prefix = '<strong><span style="color: #2563eb;">Definition:</span></strong>'
    return f"{prefix} [{name}]({base}) · [O]({o}) · [E]({e}) · [C]({c})"


def build_widget(
    concepts: list[tuple[str, str]],
    indent_prefix: str,
) -> list[str]:
    """Return the lines of a <details> D/E/C widget. indent_prefix is applied
    to every emitted line."""

    lines = [
        f"{indent_prefix}<details>",
        f"{indent_prefix}{DEC_SUMMARY_STR}",
        f"{indent_prefix}",
    ]
    for name, slug in concepts:
        lines.append(f"{indent_prefix}{format_row(name, slug)}")
    lines.extend([f"{indent_prefix}", f"{indent_prefix}</details>"])
    return lines


def convert_file(path: Path, slug_table: dict[str, str]) -> tuple[int, list[str]]:
    """Return (conversion_count, warnings) for the given file."""

    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()

    out: list[str] = []
    warnings: list[str] = []
    conversions = 0

    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        # Detect the opening of a Trace <details> block.
        if DETAILS_OPEN_RE.match(line.strip()) and i + 1 < n and TRACE_SUMMARY_RE.match(lines[i + 1]):
            # Collect the whole Trace block through </details>.
            block_start = i
            block_lines: list[str] = []
            i += 1  # Currently at line after <details>
            while i < n and not DETAILS_CLOSE_RE.match(lines[i].strip()):
                block_lines.append(lines[i])
                i += 1
            if i >= n:
                warnings.append(
                    f"{path}: unterminated <details> beginning near line {block_start + 1}"
                )
                # Emit original back unchanged.
                out.append(lines[block_start])
                out.extend(block_lines)
                continue
            # lines[i] is the </details> close.
            block_close_line = lines[i]
            i += 1  # Advance past </details>

            # Determine whether the block contains a Definitions: line.
            # Find it.
            def_start_idx: int | None = None
            def_end_idx: int | None = None  # inclusive index within block_lines
            multi_line = False
            for j, bline in enumerate(block_lines):
                if DEFINITIONS_INLINE_RE.match(bline):
                    def_start_idx = j
                    def_end_idx = j
                    multi_line = False
                    break
                if DEFINITIONS_BLOCK_HEADER_RE.match(bline):
                    def_start_idx = j
                    # Consume indented sub-bullets.
                    k = j + 1
                    while k < len(block_lines) and DEFINITIONS_SUBBULLET_RE.match(
                        block_lines[k]
                    ):
                        k += 1
                    def_end_idx = k - 1
                    multi_line = True
                    break

            if def_start_idx is None:
                # No Definitions line in this Trace. Emit unchanged.
                out.append(lines[block_start])
                out.extend(block_lines)
                out.append(block_close_line)
                continue

            # Parse concepts from the Definitions block.
            concepts: list[tuple[str, str]] = []
            if multi_line:
                for bl in block_lines[def_start_idx + 1 : def_end_idx + 1]:
                    sub = DEFINITIONS_SUBBULLET_RE.match(bl)
                    if not sub:
                        continue
                    parsed = parse_concept_item(sub.group(1), slug_table)
                    if parsed:
                        concepts.append(parsed)
                    else:
                        warnings.append(
                            f"{path}:{block_start + 1 + def_start_idx}: "
                            f"unparseable concept in multi-line Definitions: {sub.group(1)!r}"
                        )
            else:
                content = DEFINITIONS_INLINE_RE.match(block_lines[def_start_idx]).group(1)
                # Split on `;` and also handle a trailing period.
                items = [p.strip() for p in content.split(";") if p.strip()]
                for item in items:
                    parsed = parse_concept_item(item, slug_table)
                    if parsed:
                        concepts.append(parsed)
                    else:
                        warnings.append(
                            f"{path}:{block_start + 1 + def_start_idx}: "
                            f"unparseable concept in Definitions: {item!r}"
                        )

            if not concepts:
                # Parse failure -- leave block untouched; warnings already raised.
                out.append(lines[block_start])
                out.extend(block_lines)
                out.append(block_close_line)
                continue

            # De-duplicate while preserving order.
            seen: set[str] = set()
            unique: list[tuple[str, str]] = []
            for name, slug in concepts:
                if slug in seen:
                    continue
                seen.add(slug)
                unique.append((name, slug))
            concepts = unique

            # Remove the Definitions line(s) from block_lines.
            remaining_block = (
                block_lines[:def_start_idx] + block_lines[def_end_idx + 1 :]
            )
            # Tidy: strip trailing blank lines inside the block.
            while remaining_block and remaining_block[-1].strip() == "":
                remaining_block.pop()
            # Also strip leading blank lines.
            while remaining_block and remaining_block[0].strip() == "":
                remaining_block.pop(0)
            # Re-add one leading blank line to preserve the summary -> blank -> body
            # visual spacing used across the corpus, IF remaining_block has content
            # beyond the summary line.
            # The block_lines list starts with the summary line.
            if remaining_block:
                # remaining_block[0] is the summary line; ensure one blank after.
                tidy: list[str] = [remaining_block[0], ""]
                for bl in remaining_block[1:]:
                    if bl.strip() == "" and tidy and tidy[-1].strip() == "":
                        continue
                    tidy.append(bl)
                # trailing blank to match original style
                if tidy and tidy[-1].strip() != "":
                    tidy.append("")
                remaining_block = tidy

            # Decide whether to keep the Trace block at all.
            # Count content bullets (anything that starts with "- ").
            has_content = any(
                re.match(r"^\s*-\s+", bl) for bl in remaining_block
            )

            if has_content:
                out.append(lines[block_start])  # <details>
                out.extend(remaining_block)
                out.append(block_close_line)  # </details>
                # Emit the D/E/C widget directly after.
                if len(concepts) == 1:
                    out.append("")
                    out.append(format_inline_line(*concepts[0]))
                else:
                    out.append("")
                    out.extend(build_widget(concepts, indent_prefix=""))
            else:
                # Trace had only a Definitions line; drop Trace entirely and
                # replace with the D/E/C widget (or inline line).
                if len(concepts) == 1:
                    out.append(format_inline_line(*concepts[0]))
                else:
                    out.extend(build_widget(concepts, indent_prefix=""))

            conversions += 1
            continue

        out.append(line)
        i += 1

    # Preserve original trailing newline.
    new_text = "\n".join(out)
    if original.endswith("\n") and not new_text.endswith("\n"):
        new_text += "\n"

    if new_text != original:
        path.write_text(new_text, encoding="utf-8")

    return conversions, warnings


def main() -> int:
    slug_table = build_ch5_slug_table()

    total = 0
    all_warnings: list[str] = []
    for target in TARGETS:
        if not target.exists():
            all_warnings.append(f"{target}: file not found, skipped")
            continue
        count, warnings = convert_file(target, slug_table)
        total += count
        all_warnings.extend(warnings)
        print(f"{target}: converted {count} Definitions line(s)")

    if all_warnings:
        print("\nWarnings:", file=sys.stderr)
        for w in all_warnings:
            print(f"  {w}", file=sys.stderr)
    print(f"\nTotal conversions: {total}")
    return 0 if not all_warnings else 1


if __name__ == "__main__":
    raise SystemExit(main())
