#!/usr/bin/env python3
"""Chapter Five anchor-presence and D/E/C widget row-shape integrity audit.

This audit supersedes the one-off ``tools/verify_dec_anchors.py`` check by
running as a blocking regression gate alongside the other ``make regression``
audits. It enforces two invariants:

1. **Chapter Five anchor presence.** Every ``####`` and ``#####`` definition
   entry in ``core_05-05_definitions_a_independent.md`` that owns ``- O:`` /
   ``- E:`` / ``- C:`` bullets carries the canonical anchor trio:

   - the entry-level slug (either from an explicit ``<a id="SLUG"></a>`` tag
     above the heading or from the heading's auto-slug),
   - ``SLUG-e`` for the E bullet,
   - ``SLUG-c`` for the C bullet.

   Entries listed under the documented exception sets are handled as
   described below:

   - **Cluster heads** (``CLUSTERED_HEADS``) — headings that are organizational
     parents for sub-entries and intentionally carry no ``- O:`` / ``- E:`` /
     ``- C:`` body bullets. No ``-e`` / ``-c`` anchors required.
   - **Content gaps** (``MISSING_C``) — entries that have an ``- E:`` bullet
     but deliberately lack a top-level ``- C:`` bullet (pending future
     authoring). The ``-c`` anchor requirement is relaxed; D/E/C widget rows
     pointing at those entries fall back to the entry heading anchor for the
     C link.

2. **D/E/C widget row-shape and anchor resolution.** Across the consumer core
   files (``core_00-01_principles.md``, ``core_02-04_definition_mechanics.md``,
   the four Chapter Nine parts), every line inside a D/E/C widget that appears
   to be a widget row must match the canonical shape:

       - [Name](core_05-05_definitions_a_independent.md#slug) · [O](...) · [E](...) · [C](...)

   and every anchor in that row must resolve to a live Chapter Five anchor.
   The single-concept inline form is also recognized:

       <strong><span style="color: #2563eb;">Definition:</span></strong> [Name](...) · [O](...) · [E](...) · [C](...)

   Mis-shaped rows (missing separators, wrong arity, dead anchors) are
   reported with file/line/slug detail.

Run from the repository root:

    make ch5-dec-widget-audit

or directly:

    python3 tools/ch5_dec_widget_audit.py --root .

Exits 0 on PASS, non-zero on any violation.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_ALL, CH5_PART_A, CH5_PART_B, CH5_PART_C

CH5_FILENAME = CH5_PART_A

# Longest first so ``substantive-fairness-constitutional-e`` matches
# ``…-constitutional`` base when present, not ``substantive-fairness``.
_WIDGET_SLUG_SUFFIXES = (
    "-constitutional-e",
    "-constitutional-c",
    "-constitutional",
    "-o",
    "-e",
    "-c",
)

# Files that host D/E/C widgets or inline Definition: lines. Chapter Five
# itself does not host widgets (definitions live there), but its own heading
# anchors must still resolve — so Chapter Five is the canonical anchor source
# rather than a consumer.
CONSUMERS = [
    "core_00-01_principles.md",
    "core_02-04_definition_mechanics.md",
    "core_08-08_misconduct.md",
    "core_10-10_rights_part_a.md",
    "core_10-10_rights_part_b.md",
    "core_10-10_rights_part_c.md",
    "core_10-10_rights_part_d.md",
]

# Headings that are cluster parents without direct O/E/C body. The audit does
# not require -e / -c anchors for these. Keep in sync with
# ``tools/convert_definitions_to_dec_widget.py::CLUSTERED_HEADS`` (slug form).
CLUSTERED_HEADS: set[str] = {
    "accountability-contestability-and-collective-accountability-failure-cluster",
    "incentive-alignment",
    "innovation-reward-and-anti-enclosure",
    "trust-degradation-and-misleading-reliance-constitutional",
    "trust-degradation-and-misleading-reliance",
}

# Entries with an O and E but no authored C bullet. Widget rows may fall back
# the C link to the heading anchor. Keep in sync with
# ``tools/convert_definitions_to_dec_widget.py::MISSING_C``.
MISSING_C: set[str] = set()

# Structural Chapter Five headings that should never be treated as definition
# entries even if the heuristic-body-probe would otherwise pick them up. These
# are the section/chapter framing headings under Chapter Five itself.
STRUCTURAL_HEADINGS: set[str] = {
    "canonical-home-and-non-duplication-rule",
    "independent-definitions-a-z",
    "semi-independent-definitions-a-z",
    "dependent-clusters-a-z",
    "all-definitions-and-clusters-a-z",
    "definitions-a-z-unified",
    "definitions-a-z",
    "clusters-a-z",
    "1-independent-definitions",
    "1-interdependent-definitions",
    "2-semi-independent-definitions",
    "section-2-semi-independent-definitions",
    "3-dependent-clusters-clustered-definitions",
    "section-3-dependent-clusters-clustered-definitions",
    "31-joint-invocation-and-satisfaction",
    "32-standalone-definitions-interaction-and-full-context",
}


H4_RE = re.compile(r"^####\s+(.+?)\s*$")
H5_RE = re.compile(r"^#####\s+(.+?)\s*$")
ANCHOR_TAG_RE = re.compile(r'^<a id="([^"]+)"></a>\s*$')
INLINE_ANCHOR_TAG_RE = re.compile(r'<a id="([^"]+)"></a>')

DEC_SUMMARY_RE = re.compile(
    r'<summary><strong><span style="color: #2563eb;">'
    r"Definitions · Evaluation · Compliance</span></strong></summary>"
)
TRACE_SUMMARY_RE = re.compile(
    r'<summary><strong><span style="color: #2563eb;">'
    r"Trace</span></strong></summary>"
)
DETAILS_OPEN_RE = re.compile(r"^\s*<details>\s*$")
DETAILS_CLOSE_RE = re.compile(r"^\s*</details>\s*$")

# Canonical widget-row shape inside a D/E/C widget block. The separator is
# middle-dot with single spaces. Each href must point into Chapter Five.
#
# Example:
#   - [Wellbeing](core_05-05_definitions_a_independent.md#wellbeing) · [O](core_05-05_definitions_a_independent.md#wellbeing) · [E](core_05-05_definitions_a_independent.md#wellbeing-e) · [C](core_05-05_definitions_a_independent.md#wellbeing-c)
ROW_RE = re.compile(
    r"^\s*-\s+"
    r"\[(?P<name>[^\]]+)\]\((?P<link>[^)]+)\)"
    r"\s+·\s+\[O\]\((?P<o>[^)]+)\)"
    r"\s+·\s+\[E\]\((?P<e>[^)]+)\)"
    r"\s+·\s+\[C\]\((?P<c>[^)]+)\)"
    r"\s*$"
)

# Inline "Definition:" single-concept form.
INLINE_RE = re.compile(
    r'^<strong><span style="color: #2563eb;">Definition:</span></strong>'
    r"\s+\[(?P<name>[^\]]+)\]\((?P<link>[^)]+)\)"
    r"\s+·\s+\[O\]\((?P<o>[^)]+)\)"
    r"\s+·\s+\[E\]\((?P<e>[^)]+)\)"
    r"\s+·\s+\[C\]\((?P<c>[^)]+)\)"
    r"\s*$"
)

# A loose "row-like" detector for catching mis-shaped rows inside a D/E/C
# widget. We treat any line starting with a list bullet followed by a markdown
# link as a candidate, so we can flag shape violations that ROW_RE does not
# match.
ROW_LIKE_RE = re.compile(r"^\s*-\s+\[[^\]]+\]\(")


def auto_slug(heading: str) -> str:
    """Match the GitHub-flavored-markdown auto-slug GitHub renders for a
    heading. Mirrors the convention used across the corpus: lower-case,
    punctuation stripped, whitespace collapsed to hyphens.
    """
    s = heading.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def collect_ch5_anchors(ch5_text: str) -> set[str]:
    """Return the set of live anchor slugs in Chapter Five.

    Sources:
    - Explicit ``<a id="..."></a>`` tags anywhere in the file (line-start or
      inline).
    - Auto-slugs of ``###``, ``####``, and ``#####`` headings.
    """
    anchors: set[str] = set()
    for m in INLINE_ANCHOR_TAG_RE.finditer(ch5_text):
        anchors.add(m.group(1))
    for line in ch5_text.splitlines():
        for pat in (re.compile(r"^###\s+(.+?)\s*$"), H4_RE, H5_RE):
            m = pat.match(line)
            if m:
                anchors.add(auto_slug(m.group(1)))
    return anchors


def collect_all_ch5_anchors(root: Path) -> set[str]:
    merged: set[str] = set()
    for name in CH5_ALL:
        p = root / name
        if p.exists():
            merged |= collect_ch5_anchors(p.read_text(encoding="utf-8"))
    merged |= directory_slugs_from_part_a(root)
    return merged


def directory_slugs_from_part_a(root: Path) -> set[str]:
    """Anchor fragments declared by the Chapter Five A-Z directory."""
    path = root / CH5_PART_A
    if not path.exists():
        return set()
    part_a = path.read_text(encoding="utf-8")
    unified_heading = "#### All definitions and clusters (A–Z)"
    definitions_heading = "#### Definitions A-Z"
    directory_end_marker = "\n</details>"
    semi_marker = '<a id="semi-independent-definitions-a-z"></a>'
    dep_marker = '<a id="dependent-clusters-a-z"></a>'
    indep_marker = '<a id="independent-definitions-a-z"></a>'
    out: set[str] = set()

    def scan_directory_block(block: str) -> None:
        for line in block.splitlines():
            s = line.strip()
            m = re.match(r"^-\s\[[^\]]+\]\(#([^)]+)\)\s*$", s)
            if m:
                out.add(m.group(1))
                continue
            m = re.match(
                r"^-\s\[[^\]]+\]\(" + re.escape(CH5_PART_B) + r"#([^)]+)\)\s*$",
                s,
            )
            if m:
                out.add(m.group(1))
                continue
            m = re.match(
                r"^-\s\[[^\]]+\]\(" + re.escape(CH5_PART_C) + r"#([^)]+)\)\s*$",
                s,
            )
            if m:
                out.add(m.group(1))

    if unified_heading in part_a:
        _, rest = part_a.split(unified_heading, 1)
        block = rest.split(directory_end_marker, 1)[0]
        scan_directory_block(block)
        return out

    if definitions_heading in part_a:
        _, rest = part_a.split(definitions_heading, 1)
        block = rest.split(directory_end_marker, 1)[0]
        scan_directory_block(block)
        return out

    if semi_marker not in part_a or dep_marker not in part_a:
        return set()
    before_semi, semi_and_rest = part_a.split(semi_marker, 1)
    _, indep_section = before_semi.split(indep_marker, 1)
    semi_section, dep_and_rest = semi_and_rest.split(dep_marker, 1)
    dep_section = dep_and_rest.split(directory_end_marker, 1)[0]
    scan_directory_block(indep_section)
    scan_directory_block(semi_section)
    scan_directory_block(dep_section)

    return out


def anchor_resolves_for_widget(slug: str, anchors: set[str]) -> bool:
    if slug in anchors:
        return True
    for suf in _WIDGET_SLUG_SUFFIXES:
        if slug.endswith(suf):
            base = slug[: -len(suf)]
            if base in anchors:
                return True
    return False


def resolve_entry_slug(lines: list[str], heading_idx: int) -> str:
    """Return the canonical slug for the heading at ``lines[heading_idx]``.

    Explicit ``<a id="..."></a>`` immediately above (allowing blank lines)
    wins; otherwise auto-slug the heading text.
    """
    m = H4_RE.match(lines[heading_idx]) or H5_RE.match(lines[heading_idx])
    assert m is not None
    heading = m.group(1)

    j = heading_idx - 1
    while j >= 0 and lines[j].strip() == "":
        j -= 1
    # Editorial separator (horizontal rule) may sit between the explicit
    # entry anchor and the #### heading — skip it when resolving the slug.
    while j >= 0 and lines[j].strip() == "---":
        j -= 1
        while j >= 0 and lines[j].strip() == "":
            j -= 1
    if j >= 0:
        m_anchor = ANCHOR_TAG_RE.match(lines[j])
        if m_anchor:
            return m_anchor.group(1)

    return auto_slug(heading)


def scan_entry_body(lines: list[str], heading_idx: int) -> dict[str, object]:
    """Probe the body of the Chapter Five entry starting at ``heading_idx``.

    Returns a dict with:
        - ``has_o``, ``has_e``, ``has_c`` — whether a top-level ``- O:``,
          ``- E:``, or ``- C:`` bullet appears in the entry body.
        - ``inline_anchors`` — set of slugs from ``<a id="...">`` tags found
          in the entry body (used to verify the -e / -c anchors).
        - ``anchor_line`` — dict slug -> 1-based line number for each inline
          anchor (for accurate failure reporting).
    """
    has_o = has_e = has_c = False
    inline_anchors: set[str] = set()
    anchor_line: dict[str, int] = {}

    i = heading_idx + 1
    n = len(lines)
    while i < n:
        stripped = lines[i].strip()
        # Stop at the next H4/H5/H3/H2/H1 heading (new entry or section).
        if (
            stripped.startswith("#### ")
            or stripped.startswith("##### ")
            or stripped.startswith("### ")
            or stripped.startswith("## ")
            or stripped.startswith("# ")
        ):
            break
        if stripped.startswith("- O:"):
            has_o = True
        elif stripped.startswith("- E:"):
            has_e = True
        elif stripped.startswith("- C:"):
            has_c = True
        for m in INLINE_ANCHOR_TAG_RE.finditer(lines[i]):
            slug = m.group(1)
            inline_anchors.add(slug)
            anchor_line.setdefault(slug, i + 1)
        i += 1
    return {
        "has_o": has_o,
        "has_e": has_e,
        "has_c": has_c,
        "inline_anchors": inline_anchors,
        "anchor_line": anchor_line,
        "end_idx": i,
    }


def audit_chapter_five(ch5_path: Path) -> list[str]:
    """Return a list of violation strings for Chapter Five anchor presence.

    Scope: only ``####`` (H4) definition entries. ``#####`` (H5) component
    entries exist only as cluster sub-components (Incentive Alignment,
    Innovation Reward, Privacy, Trust Degradation, Trustworthiness, Harm /
    Materiality / Verifiability / Foreseeability clusters, etc.) and carry
    intentionally partial bullet shapes (for example, ``- O:`` only as a
    scope-of-sub-rule). Enforcing the full O/E/C anchor trio on them would
    misread cluster structure. The auto-slug of each H4 heading is still
    added to the live-anchor set in ``collect_ch5_anchors`` so H5-targeted
    widget rows remain resolvable.
    """
    text = ch5_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    violations: list[str] = []

    for idx, line in enumerate(lines):
        m = H4_RE.match(line)
        if not m:
            continue
        slug = resolve_entry_slug(lines, idx)
        if slug in STRUCTURAL_HEADINGS:
            continue
        if slug in CLUSTERED_HEADS:
            # Cluster heads intentionally carry no direct O/E/C body; skip.
            continue

        body = scan_entry_body(lines, idx)

        # Entries that do not assert O/E/C are out of scope (for example,
        # Chapter Five §2 structural sub-heads that happen to be H4 but carry
        # only explanatory prose).
        if not body["has_o"]:
            continue

        lineno = idx + 1
        inline_anchors = body["inline_anchors"]

        # An entry with - O: should also have - E: and - C: (unless MISSING_C).
        if not body["has_e"]:
            violations.append(
                f"{ch5_path}:{lineno}: Chapter Five entry '{slug}' has '- O:' "
                f"but is missing a top-level '- E:' bullet"
            )
        if slug not in MISSING_C and not body["has_c"]:
            violations.append(
                f"{ch5_path}:{lineno}: Chapter Five entry '{slug}' has '- O:' "
                f"but is missing a top-level '- C:' bullet (and is not in the "
                f"MISSING_C exception set)"
            )

        # -e anchor is required when - E: is present.
        if body["has_e"] and f"{slug}-e" not in inline_anchors:
            violations.append(
                f"{ch5_path}:{lineno}: Chapter Five entry '{slug}' is "
                f"missing expected anchor <a id=\"{slug}-e\"></a> above the "
                f"'- E:' bullet"
            )
        # -c anchor is required when - C: is present and not in MISSING_C.
        if (
            body["has_c"]
            and slug not in MISSING_C
            and f"{slug}-c" not in inline_anchors
        ):
            violations.append(
                f"{ch5_path}:{lineno}: Chapter Five entry '{slug}' is "
                f"missing expected anchor <a id=\"{slug}-c\"></a> above the "
                f"'- C:' bullet"
            )

    return violations


def slug_from_ch5_href(href: str) -> str | None:
    """Return the slug if ``href`` points into Chapter Five, else None."""
    for fname in CH5_ALL:
        prefix = f"{fname}#"
        if href.startswith(prefix):
            return href[len(prefix) :]
    return None


def audit_widgets_in_file(
    path: Path, anchors: set[str]
) -> list[str]:
    """Scan ``path`` for D/E/C widget blocks and inline Definition: lines,
    returning violation strings.

    Checks:
    - Widget blocks must contain only widget-shape rows (plus blank lines)
      between summary and ``</details>``.
    - Every row must match ``ROW_RE`` exactly.
    - Every href in every row must point into Chapter Five and resolve to a
      live anchor.
    - Inline ``Definition:`` single-concept lines must match ``INLINE_RE`` and
      resolve.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    violations: list[str] = []

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        # Detect a D/E/C widget: <details> followed by the DEC summary.
        if DETAILS_OPEN_RE.match(line):
            # Peek next non-blank line.
            j = i + 1
            while j < n and lines[j].strip() == "":
                j += 1
            if j < n and DEC_SUMMARY_RE.search(lines[j]):
                # This is a D/E/C widget block. Walk until </details>.
                block_start = i + 1
                k = j + 1
                while k < n and not DETAILS_CLOSE_RE.match(lines[k]):
                    raw = lines[k]
                    stripped = raw.strip()
                    # Permissible: blank line.
                    if stripped == "":
                        k += 1
                        continue
                    # Permissible: a row matching ROW_RE.
                    if ROW_RE.match(raw):
                        m = ROW_RE.match(raw)
                        assert m is not None
                        row_violations = validate_row(
                            path, k + 1, m, anchors
                        )
                        violations.extend(row_violations)
                        k += 1
                        continue
                    # Mis-shaped row-like line.
                    if ROW_LIKE_RE.match(raw):
                        violations.append(
                            f"{path}:{k + 1}: D/E/C widget row does not "
                            f"match canonical shape "
                            f"'- [Name](...) · [O](...) · [E](...) · [C](...)': "
                            f"{stripped}"
                        )
                        k += 1
                        continue
                    # Other non-empty content inside a D/E/C widget is a
                    # shape violation.
                    violations.append(
                        f"{path}:{k + 1}: unexpected non-row content inside "
                        f"D/E/C widget block (started line {block_start}): "
                        f"{stripped}"
                    )
                    k += 1
                if k >= n:
                    violations.append(
                        f"{path}:{block_start}: unterminated D/E/C widget "
                        f"<details> block"
                    )
                    i = n
                    continue
                i = k + 1
                continue
        # Detect an inline Definition: single-concept line.
        if INLINE_RE.match(line):
            m = INLINE_RE.match(line)
            assert m is not None
            violations.extend(validate_row(path, i + 1, m, anchors))
        elif line.lstrip().startswith(
            '<strong><span style="color: #2563eb;">Definition:'
        ):
            # Shape looks like an inline D/E/C line but didn't match INLINE_RE.
            violations.append(
                f"{path}:{i + 1}: inline 'Definition:' line does not match "
                f"canonical shape "
                f"'<strong>...Definition:</strong> [Name](...) · [O](...) · "
                f"[E](...) · [C](...)'"
            )
        i += 1

    return violations


def validate_row(
    path: Path,
    lineno: int,
    match: re.Match[str],
    anchors: set[str],
) -> list[str]:
    """Validate the O/E/C href resolution for a single widget/inline row."""
    violations: list[str] = []
    name = match.group("name")
    link_href = match.group("link")
    o_href = match.group("o")
    e_href = match.group("e")
    c_href = match.group("c")

    for label, href in (
        ("link", link_href),
        ("O", o_href),
        ("E", e_href),
        ("C", c_href),
    ):
        slug = slug_from_ch5_href(href)
        if slug is None:
            violations.append(
                f"{path}:{lineno}: D/E/C row [{name}] {label}-link does not "
                f"point into Chapter Five: {href}"
            )
            continue
        if not anchor_resolves_for_widget(slug, anchors):
            violations.append(
                f"{path}:{lineno}: D/E/C row [{name}] {label}-link anchor "
                f"#{slug} does not resolve in Chapter Five ({', '.join(CH5_ALL)})"
            )
    return violations


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default=".",
        help="Workspace root (default: current directory).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root)

    ch5_path = root / CH5_FILENAME
    if not ch5_path.exists():
        print(f"Missing required file: {ch5_path}", file=sys.stderr)
        return 2

    anchors = collect_all_ch5_anchors(root)

    violations: list[str] = []
    for fname in CH5_ALL:
        p = root / fname
        if p.exists():
            violations.extend(audit_chapter_five(p))

    for consumer_name in CONSUMERS:
        consumer = root / consumer_name
        if not consumer.exists():
            # Silent skip: consumer list is stable but tolerate file removals.
            continue
        violations.extend(audit_widgets_in_file(consumer, anchors))

    if violations:
        for v in violations:
            print(v, file=sys.stderr)
        print(
            f"\nFAIL: {len(violations)} Chapter Five anchor / D/E/C widget "
            f"integrity violation(s).",
            file=sys.stderr,
        )
        return 1

    print(
        "PASS: Chapter Five definition entries carry canonical anchors and "
        "all D/E/C widget rows resolve to live Chapter Five anchors."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
