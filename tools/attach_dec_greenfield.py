"""Attach **Definitions · Evaluation · Compliance (D/E/C) widgets** (or, where
exactly one concept is invoked, single-concept inline ``Definition:`` lines) to
consumer sections that did **not** previously carry a ``Definitions: …`` line
inside Trace.

Scope (per ``doc_architecture.md`` rule 12, 2026-04-16 D/E/C split):
- Operates only on the five existing consumer files (``core_00-01_principles.md``
  + ``core_10-10_rights_part_a..d.md``).
- Sections targeted are listed in ``ATTACHMENTS`` below: each entry pairs a
  unique heading-line text with the explicitly invoked Chapter Five concepts
  for that section. The list is the audit trail of this fan-out pass.
- "Owning unit" choice follows ``doc_architecture.md`` rule 9: subarticle for
  Chapter Ten, subsection elsewhere. Article-level openers in Chapter Ten
  appear here only where the opener carries shared opening doctrine that
  materially binds across the whole article.
- Concept threshold is "explicit only": each attributed concept is named in
  the section text (capitalized, bolded, italic Chapter Five cross-reference,
  or unambiguous noun-form). The script does **not** infer concepts the
  section does not name.

Placement rule (per rule 12):
- If the section already carries a Trace ``<details>`` block immediately
  under the heading, the new widget is inserted directly after Trace's
  closing ``</details>``, before the ``<br>`` and operative prose. If the
  payload is the single-concept inline ``Definition:`` line (one concept),
  the existing ``<br>`` spacer that followed Trace is dropped because the
  inline form takes no trailing ``<br>`` per rule 12 *Spacer rule*.
- Otherwise the widget is inserted directly under the heading, before the
  operative prose, with a ``<br>`` separator afterwards. The ``<br>`` is
  emitted only for the collapsible widget; the single-concept inline
  ``Definition:`` line stands alone with the standard inter-paragraph
  blank line and no ``<br>``.

Idempotent: if the script sees a ``Definitions · Evaluation · Compliance``
summary already present in the section (between the heading and the next
sibling heading), it leaves that section alone.

Single-concept degradation rule (per rule 12 (f)): one concept → inline line
prefixed by bold-blue ``Definition:`` (singular), with no collapsible widget.

Run from the repository root:

    python3 tools/attach_dec_greenfield.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


CH5_PATH = "core_05-05_definitions_a_independent.md"
CH5C_PATH = "core_05-05_definitions_c_dependent_clusters.md"


def ch5_href_base(slug: str) -> str:
    if slug in ("trust", "trustworthiness"):
        return CH5C_PATH
    return CH5_PATH

DEC_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">'
    "Definitions · Evaluation · Compliance</span></strong></summary>"
)
DEC_INLINE_PREFIX = (
    '<strong><span style="color: #2563eb;">Definition:</span></strong>'
)


CLUSTERED_HEADS = {
    "accountability-contestability-and-collective-accountability-failure-cluster",
    "incentive-alignment",
    "innovation-reward-and-anti-enclosure",
    "trust-degradation-and-misleading-reliance-constitutional",
    "trust-degradation-and-misleading-reliance",
}

MISSING_C = {
    "sentience-non-exclusion",
}

# These concepts use cluster-level O/E/C anchors rather than direct sibling
# anchors on every local sub-entry heading.
CLUSTER_OEC_FALLBACK = {
    "educational-agency",
    "meaningful-agency",
    "self-determination-constitutional",
}


# Canonical (display name -> Chapter Five anchor slug) lookup. The slugs match
# anchors verified by ``tools/verify_dec_anchors.py`` after the 2026-04-16
# anchor pass.
CONCEPTS = {
    "Wellbeing": "wellbeing",
    "Materiality": "materiality-determination",
    "Material Impact": "material-impact",
    "Dependency": "dependency",
    "Foreseeability": "foreseeability-diligence",
    "Proxy Divergence": "proxy-divergence",
    "Harm": "harm",
    "Irreversible Harm": "irreversible-harm",
    "Risk": "risk",
    "Existential Risk": "existential-risk",
    "Systemic Lock-In": "systemic-lock-in",
    "Reversibility": "reversibility-constitutional",
    "Epistemic Integrity": "epistemic-integrity",
    "Truth (Constitutional Constraint)": "truth-constitutional-constraint",
    "Safety (Constraint)": "safety-constraint",
    "Trust": "trust",
    "Trustworthiness": "trustworthiness",
    "Meaningful Agency": "meaningful-agency",
    "Feasibility": "feasibility",
    "Necessity": "necessity",
    "Proportionality": "proportionality",
    "Harm Minimization (Tradeoff Selection)": "harm-minimization-tradeoff-selection",
    "Freedom (Bounded Agency)": "freedom-bounded-agency",
    "Oversight (Constitutional)": "oversight-constitutional",
    "Auditability": "auditability",
    "Transparency": "transparency",
    "Contestability": "contestability",
    "Accountability": "accountability",
    "Governance": "governance",
    "Stakeholder": "stakeholder",
    "Stakeholder Participation Weight": "stakeholder-participation-weight",
    "Procedural Fairness (Constitutional)": "procedural-fairness-constitutional",
    "Productive Capacity (Constitutional)": "productive-capacity-constitutional",
    "Constitutional Efficiency": "constitutional-efficiency",
    "Avoidable Burden": "avoidable-burden",
    "System Capture": "system-capture",
    "Incentive Alignment (Constitutional)": "incentive-alignment",
    "Coercion and Manipulation (Constitutional)": "coercion-and-manipulation-constitutional",
    "Self-Determination (Constitutional)": "self-determination-constitutional",
    "Surveillance Boundary (Constitutional)": "surveillance-boundary",
    "Educational Agency": "educational-agency",
    "Protected Characteristics": "protected-characteristics-constitutional",
    "Constitutional Community": "constitutional-community",
    "Restorative Justice (Constitutional)": "restorative-justice",
    "Non-Imposition (Cooperative Interaction)": "non-imposition-cooperative-interaction",
    "Environmental Preconditions (Constitutional)": "environmental-preconditions-constitutional",
    "Ecological Footprint": "ecological-footprint",
    "Intergenerational Responsibility (Constitutional)": "intergenerational-responsibility-constitutional",
    "Adjudication and Dispute Resolution (Constitutional)": "adjudication-and-dispute-resolution-constitutional",
    "Participant Standing (Constitutional)": "participant-standing-constitutional",
    "Dignity and Equal Moral Standing": "dignity-and-equal-moral-standing",
    "Redress and Remediation": "redress-and-remediation-constitutional",
    "Authority Stack": "authority-stack",
    "Forum Family, Sentient": "forum-family-sentient",
    "Forum Family, Technical": "forum-family-technical",
    "Technical Forum Domains": "technical-forum-domains",
    "Forum Family, Institutional": "forum-family-institutional",
    "Forum Family, Environment": "forum-family-environment",
    "Forum Family, Integrity": "forum-family-integrity",
    "Forum Family, Constitutional": "forum-family-constitutional",
    "Constitutional Forums": "constitutional-forums",
    "Constitutional Review Body": "constitutional-forums",
}


def slug(name: str) -> str:
    if name not in CONCEPTS:
        raise KeyError(
            f"Unknown concept name (add to CONCEPTS): {name!r}"
        )
    return CONCEPTS[name]


def targets(name: str) -> tuple[str, str, str]:
    s = slug(name)
    fb = ch5_href_base(s)
    base = f"{fb}#{s}"
    if s in CLUSTERED_HEADS:
        return base, base, base
    if s in CLUSTER_OEC_FALLBACK:
        return f"{fb}#{s}-o", f"{fb}#{s}-e", f"{fb}#{s}-c"
    e = f"{fb}#{s}-e"
    if s in MISSING_C:
        return base, e, base
    c = f"{fb}#{s}-c"
    return base, e, c


def row(name: str) -> str:
    s = slug(name)
    base = f"{ch5_href_base(s)}#{s}"
    o, e, c = targets(name)
    return f"- [{name}]({base}) · [O]({o}) · [E]({e}) · [C]({c})"


def inline_line(name: str) -> str:
    s = slug(name)
    base = f"{ch5_href_base(s)}#{s}"
    o, e, c = targets(name)
    return (
        f"{DEC_INLINE_PREFIX} [{name}]({base}) · [O]({o}) · [E]({e}) · [C]({c})"
    )


def widget_block(concepts: list[str]) -> list[str]:
    out = ["<details>", DEC_SUMMARY, ""]
    for name in concepts:
        out.append(row(name))
    out.extend(["", "</details>"])
    return out


# Each entry: (file_path_str, heading_line, concepts).
# - heading_line is matched verbatim against a single line in the file. It
#   must be unique within the file; if not, the script aborts.
# - concepts: ordered list. >=2 -> widget, ==1 -> inline line.
ATTACHMENTS: list[tuple[str, str, list[str]]] = [
    # ---------------- core_00-01_principles.md ----------------
    (
        "core_00-01_principles.md",
        "### 1. Purpose and Role",
        [
            "Wellbeing",
            "Truth (Constitutional Constraint)",
            "Safety (Constraint)",
            "Trustworthiness",
            "Meaningful Agency",
            "Proportionality",
            "Necessity",
        ],
    ),
    (
        "core_00-01_principles.md",
        "##### 6.1.1 Proportionality",
        [
            "Proportionality",
            "Risk",
            "Irreversible Harm",
            "Existential Risk",
            "Systemic Lock-In",
            "Reversibility",
            "Dependency",
        ],
    ),
    (
        "core_00-01_principles.md",
        "##### 6.1.2 Necessity",
        ["Necessity"],
    ),
    (
        "core_00-01_principles.md",
        "##### 6.1.3 Minimization of Harm",
        [
            "Harm Minimization (Tradeoff Selection)",
            "Harm",
        ],
    ),
    (
        "core_00-01_principles.md",
        "##### 6.1.4 Minimization of Avoidable Burden",
        [
            "Avoidable Burden",
            "Proportionality",
            "Necessity",
            "Safety (Constraint)",
            "Truth (Constitutional Constraint)",
        ],
    ),
    (
        "core_00-01_principles.md",
        "##### 6.2.2 Trust-Truth Alignment",
        [
            "Trust",
            "Truth (Constitutional Constraint)",
            "Epistemic Integrity",
        ],
    ),
    (
        "core_00-01_principles.md",
        "##### 6.3.1 Constraint on Freedom",
        [
            "Freedom (Bounded Agency)",
            "Necessity",
            "Proportionality",
            "Harm",
            "Risk",
            "Reversibility",
            "Oversight (Constitutional)",
        ],
    ),
    (
        "core_00-01_principles.md",
        "##### 6.3.2 Time-Consistency Constraint",
        [
            "Safety (Constraint)",
            "Truth (Constitutional Constraint)",
            "Wellbeing",
            "Foreseeability",
        ],
    ),
    (
        "core_00-01_principles.md",
        "##### 6.4.2 Proxy-Divergence Invalidation",
        [
            "Proxy Divergence",
            "Materiality",
        ],
    ),
    (
        "core_00-01_principles.md",
        "##### 7.2.1 Alignment Requirement",
        [
            "Incentive Alignment (Constitutional)",
            "Safety (Constraint)",
            "Truth (Constitutional Constraint)",
            "Meaningful Agency",
        ],
    ),
    (
        "core_00-01_principles.md",
        "##### 7.2.2 Stewardship and Operator Incentive Posture",
        [
            "Productive Capacity (Constitutional)",
            "Constitutional Efficiency",
            "Avoidable Burden",
            "Proxy Divergence",
            "Incentive Alignment (Constitutional)",
            "Safety (Constraint)",
            "Truth (Constitutional Constraint)",
            "Auditability",
            "System Capture",
        ],
    ),
    (
        "core_00-01_principles.md",
        "##### 7.2.3 Role Depth and Material Responsibility Pathways",
        ["Meaningful Agency"],
    ),
    (
        "core_00-01_principles.md",
        "##### 7.2.4 Misalignment Correction and Capture Response",
        [
            "Incentive Alignment (Constitutional)",
            "System Capture",
            "Oversight (Constitutional)",
            "Accountability",
        ],
    ),
    (
        "core_00-01_principles.md",
        "##### 7.2.5 Contingent claims, games of chance, and event-contract markets",
        [
            "Incentive Alignment (Constitutional)",
            "Necessity",
            "Proportionality",
            "Truth (Constitutional Constraint)",
            "Contestability",
            "Dependency",
            "Coercion and Manipulation (Constitutional)",
        ],
    ),
    (
        "core_00-01_principles.md",
        "### 10. Interpretive Role",
        [
            "Irreversible Harm",
            "Truth (Constitutional Constraint)",
            "Meaningful Agency",
            "Accountability",
            "System Capture",
            "Incentive Alignment (Constitutional)",
            "Governance",
        ],
    ),
    # ---------------- core_10-10_rights_part_a.md ----------------
    (
        "core_10-10_rights_part_a.md",
        "### Article I: Environmental Survival",
        ["Environmental Preconditions (Constitutional)"],
    ),
    (
        "core_10-10_rights_part_a.md",
        "### Article II: Material Stewardship and Durable-Use Integrity",
        [
            "Ecological Footprint",
            "Intergenerational Responsibility (Constitutional)",
            "Materiality",
        ],
    ),
    # ---------------- core_10-10_rights_part_b.md ----------------
    (
        "core_10-10_rights_part_b.md",
        "### Article VI: Right to Sentient-Centered Education",
        [
            "Educational Agency",
            "Meaningful Agency",
            "Self-Determination (Constitutional)",
            "Protected Characteristics",
        ],
    ),
    (
        "core_10-10_rights_part_b.md",
        "### Article IX: Self-Determination and Agency",
        [
            "Self-Determination (Constitutional)",
            "Surveillance Boundary (Constitutional)",
            "Safety (Constraint)",
            "Epistemic Integrity",
        ],
    ),
    (
        "core_10-10_rights_part_b.md",
        "### Article X: Cooperative Interaction",
        [
            "Constitutional Community",
            "Non-Imposition (Cooperative Interaction)",
            "Restorative Justice (Constitutional)",
        ],
    ),
    (
        "core_10-10_rights_part_b.md",
        "### Article XI: Stakeholder System Participation, Representation, and Due Process",
        [
            "Stakeholder",
            "Material Impact",
            "Dependency",
            "Proportionality",
            "Procedural Fairness (Constitutional)",
        ],
    ),
    # ---------------- core_10-10_rights_part_c.md ----------------
    (
        "core_10-10_rights_part_c.md",
        "### Article XII: Right to Reliable and Trustworthy Systems",
        [
            "Trustworthiness",
            "Trust",
            "Wellbeing",
            "Dependency",
        ],
    ),
    (
        "core_10-10_rights_part_c.md",
        "### Article XIII: Info-Sphere Integrity",
        [
            "Epistemic Integrity",
            "Self-Determination (Constitutional)",
            "Contestability",
        ],
    ),
    (
        "core_10-10_rights_part_c.md",
        "### Article XIV: Audit, Transparency, and Independent Verification",
        [
            "Auditability",
            "Transparency",
            "Materiality",
            "Dependency",
            "Risk",
        ],
    ),
    (
        "core_10-10_rights_part_c.md",
        "### Article XV: System Lifecycle, Environments, and Reversibility",
        [
            "Risk",
            "Materiality",
            "Dependency",
            "Reversibility",
            "Safety (Constraint)",
            "Epistemic Integrity",
            "Contestability",
        ],
    ),
    (
        "core_10-10_rights_part_c.md",
        "### Article XVII: Standing, Reputation, and Participation Status",
        [
            "Participant Standing (Constitutional)",
            "Stakeholder",
            "Material Impact",
            "Dignity and Equal Moral Standing",
            "Redress and Remediation",
            "Contestability",
        ],
    ),
    (
        "core_10-10_rights_part_c.md",
        "### Article XIX: Interoperability, Portability, and Exit Integrity",
        ["Systemic Lock-In"],
    ),
    (
        "core_10-10_rights_part_c.md",
        "### Article XIX: Comprehensibility and Complexity Stewardship",
        [
            "Productive Capacity (Constitutional)",
            "Constitutional Efficiency",
            "Avoidable Burden",
            "Safety (Constraint)",
            "Truth (Constitutional Constraint)",
            "Materiality",
            "Meaningful Agency",
            "Auditability",
            "Contestability",
        ],
    ),
    (
        "core_10-10_rights_part_c.md",
        "### Article XX: Root Cause Analysis and Adaptive Response",
        [
            "Materiality",
            "System Capture",
            "Auditability",
            "Contestability",
        ],
    ),
    (
        "core_10-10_rights_part_c.md",
        "### Article XXII: Constitutional Interpretation, Review, and Anti-Capture Safeguards",
        [
            "Authority Stack",
            "Forum Family, Constitutional",
            "Auditability",
            "Contestability",
        ],
    ),
    # ---------------- core_10-10_rights_part_d.md ----------------
    (
        "core_10-10_rights_part_d.md",
        "### Article XXII: Conflict Resolution, Escalation, and Emergency Proportionality",
        [
            "Adjudication and Dispute Resolution (Constitutional)",
            "Procedural Fairness (Constitutional)",
            "Contestability",
            "Transparency",
        ],
    ),
    (
        "core_10-10_rights_part_d.md",
        "### Article XXIII: Constitutional Evolution and Non-Entrenchment",
        ["Governance"],
    ),
    (
        "core_10-10_rights_part_d.md",
        "### Article XXIV: Transition Governance, Continuity, and Re-Baselining",
        ["Governance"],
    ),
]


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TRACE_OPEN_LINE = "<details>"
TRACE_SUMMARY_LINE = (
    '<summary><strong><span style="color: #2563eb;">'
    "Trace</span></strong></summary>"
)
DETAILS_CLOSE_LINE = "</details>"


def attach_one(
    lines: list[str],
    heading_line: str,
    concepts: list[str],
) -> tuple[list[str], str]:
    """Return (new_lines, status_message). Idempotent."""

    # Find the unique heading line.
    matches = [i for i, l in enumerate(lines) if l == heading_line]
    if len(matches) == 0:
        return lines, f"NOT FOUND: {heading_line!r}"
    if len(matches) > 1:
        return lines, f"AMBIGUOUS ({len(matches)}x): {heading_line!r}"
    h_idx = matches[0]

    # Find the next sibling-or-higher heading to bound the section.
    h_match = HEADING_RE.match(heading_line)
    h_depth = len(h_match.group(1))
    end_idx = len(lines)
    for j in range(h_idx + 1, len(lines)):
        m = HEADING_RE.match(lines[j])
        if m and len(m.group(1)) <= h_depth:
            end_idx = j
            break

    # Find the opener preamble: from heading down to the first deeper-level
    # child heading (or the next sibling-or-higher heading already bounded by
    # end_idx). For an article-level opener like ``### Article XII: ...``, the
    # preamble ends at the first ``#### Article XII-A: ...``. For sections
    # without children, preamble == section.
    preamble_end = end_idx
    for j in range(h_idx + 1, end_idx):
        m = HEADING_RE.match(lines[j])
        if m and len(m.group(1)) > h_depth:
            preamble_end = j
            break

    preamble = lines[h_idx + 1 : preamble_end]

    # Idempotence check: if a D/E/C summary or inline Definition: line is
    # already present in the preamble, leave it alone.
    for sl in preamble:
        if DEC_SUMMARY in sl or DEC_INLINE_PREFIX in sl:
            return lines, f"SKIP (already present): {heading_line!r}"

    # Decide payload.
    if len(concepts) == 1:
        payload = [inline_line(concepts[0])]
    else:
        payload = widget_block(concepts)

    # Locate insertion point. Bound everything by preamble_end so an
    # article-level opener does not scan into subarticle widgets.
    j = h_idx + 1
    while j < preamble_end and lines[j].strip() == "":
        j += 1

    # Case A: opener begins with a Trace <details> block.
    has_trace = (
        j < preamble_end
        and lines[j].strip() == TRACE_OPEN_LINE
        and j + 1 < preamble_end
        and lines[j + 1].strip() == TRACE_SUMMARY_LINE
    )

    if has_trace:
        # Find the closing </details> for this Trace block.
        k = j + 1
        depth = 1
        while k < preamble_end and depth > 0:
            k += 1
            if k >= preamble_end:
                break
            stripped = lines[k].strip()
            if stripped == TRACE_OPEN_LINE:
                depth += 1
            elif stripped == DETAILS_CLOSE_LINE:
                depth -= 1
        if depth != 0:
            return lines, f"ERROR: unterminated Trace under {heading_line!r}"
        # k is the index of the closing </details>. Insert payload after the
        # blank line that follows </details>.
        insert_at = k + 1
        if insert_at < preamble_end and lines[insert_at].strip() == "":
            insert_at += 1
        new_block = list(payload) + [""]
        new_lines = lines[:insert_at] + new_block + lines[insert_at:]
        # Per rule 12 *Spacer rule*: the single-concept inline Definition:
        # line takes no trailing <br>. When Trace is already present, the
        # existing <br> that followed Trace would now sit directly under the
        # newly inserted inline line and act as its trailing spacer; drop it
        # (and the blank that pads it) so the inline line goes straight into
        # the operative prose. The collapsible widget keeps the existing <br>.
        if len(concepts) == 1:
            after_payload = insert_at + len(new_block)
            if (
                after_payload < len(new_lines)
                and new_lines[after_payload].strip() == "<br>"
            ):
                drop_end = after_payload + 1
                if (
                    drop_end < len(new_lines)
                    and new_lines[drop_end].strip() == ""
                ):
                    drop_end += 1
                new_lines = new_lines[:after_payload] + new_lines[drop_end:]
        return new_lines, f"OK (after Trace): {heading_line!r}"

    # Case B: greenfield -- no Trace in the opener preamble. Insert directly
    # under the heading.
    #
    # Multi-concept widget (collapsible <details>):
    #   {heading}
    #   <blank>
    #   {payload}
    #   <blank>
    #   <br>
    #   <blank>
    #   {existing body...}
    #
    # Single-concept inline Definition: line (no trailing <br> per rule 12
    # *Spacer rule*; the inline line is a one-line styled paragraph and
    # the standard inter-paragraph blank already produces correct spacing):
    #   {heading}
    #   <blank>
    #   {payload}
    #   <blank>
    #   {existing body...}
    insert_at = h_idx + 1
    if len(concepts) == 1:
        new_block = ["", *payload, ""]
        if insert_at < preamble_end and lines[insert_at].strip() == "":
            new_block = [*payload, ""]
    else:
        new_block = ["", *payload, "", "<br>", ""]
        if insert_at < preamble_end and lines[insert_at].strip() == "":
            new_block = [*payload, "", "<br>", ""]
    new_lines = lines[:insert_at] + new_block + lines[insert_at:]
    return new_lines, f"OK (greenfield): {heading_line!r}"


def main() -> int:
    # Group by file for one read/write per file.
    by_file: dict[str, list[tuple[str, list[str]]]] = {}
    for path_str, heading, concepts in ATTACHMENTS:
        by_file.setdefault(path_str, []).append((heading, concepts))

    overall_errors: list[str] = []
    overall_changes = 0

    for path_str, items in by_file.items():
        path = Path(path_str)
        if not path.exists():
            overall_errors.append(f"FILE NOT FOUND: {path_str}")
            continue
        original = path.read_text(encoding="utf-8")
        # Preserve trailing newline.
        had_trailing_nl = original.endswith("\n")
        lines = original.splitlines()

        file_changes = 0
        for heading, concepts in items:
            new_lines, status = attach_one(lines, heading, concepts)
            print(f"  {path_str}: {status}")
            if status.startswith("OK"):
                lines = new_lines
                file_changes += 1
            elif status.startswith("SKIP"):
                pass
            else:
                overall_errors.append(f"{path_str}: {status}")

        if file_changes > 0:
            new_text = "\n".join(lines)
            if had_trailing_nl and not new_text.endswith("\n"):
                new_text += "\n"
            path.write_text(new_text, encoding="utf-8")
            overall_changes += file_changes
            print(f"{path_str}: wrote {file_changes} change(s)")
        else:
            print(f"{path_str}: no changes")

    print(f"\nTotal changes: {overall_changes}")
    if overall_errors:
        print("\nErrors:", file=sys.stderr)
        for e in overall_errors:
            print(f"  {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
