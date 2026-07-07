#!/usr/bin/env python3
"""Migrate Chapter Five leaf definitions to the guidepost O/M/E/C entry model.

Transforms a legacy definition into the reader-facing guidepost form used by the
2026-07 pilot terms:

    - **What it is**
      - **In scope:** {concept}
      - **Out of scope:** {exclusions}
    <a id="{slug}-e"></a>
    - **How to measure and assess**
      - **Primary measure:** ...

        **Primary assessment:** ...
      - **Secondary measure:** ...

        **Secondary assessment:** ...
    <a id="{slug}-c"></a>
    - **What must hold**
      - **Primary failure:** ...   (redundant "Non-compliant:" prefix stripped)

Legacy input shapes handled:
  * ``- O:`` line (concept, usually duplicated in In scope) + In scope / Out of scope.
  * ``*Measurements:*`` header block of ``**Primary:**`` / ``**Secondary:**`` /
    ``**Tertiary:**`` bullets between O and the ``-e`` anchor.
  * ``- E:`` either inline prose (primary-only terms) or ``**Primary assessment.**`` /
    ``**Secondary co-assessment.**`` / ``**Tertiary integrity check.**`` bullets.
  * ``- C:`` either inline prose or ``**Primary failure.**`` / ``**Secondary failure.**`` /
    ``**Tertiary failure.**`` sublabels.

The transform is deliberately conservative: any term it cannot confidently parse is
left untouched and reported on stderr (skipped). Always run ``--dry-run`` first.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

_TOOLS = pathlib.Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_measurement_tier_audit import HEADING_RE, find_term_body  # noqa: E402
from ch5_paths import CH5_ALL  # noqa: E402

O_LINE_RE = re.compile(r"^- (?:\*\*)?O(?:\*\*)?:\s*(.*)$")
E_MARKER_RE = re.compile(r'^(?:<a id="[^"]*-e"></a>|- (?:\*\*)?E(?:\*\*)?:)')
E_LINE_RE = re.compile(r"^- (?:\*\*)?E(?:\*\*)?:\s*(.*)$")
C_MARKER_RE = re.compile(r'^(?:<a id="[^"]*-c"></a>|- (?:\*\*)?C(?:\*\*)?:)')
C_LINE_RE = re.compile(r"^- (?:\*\*)?C(?:\*\*)?:\s*(.*)$")
IN_SCOPE_RE = re.compile(r"^(\s*)- (In scope.*?):\s*(.*)$")
OUT_SCOPE_RE = re.compile(r"^(\s*)- (Out of scope):\s*(.*)$")
MEAS_HEADER_RE = re.compile(r"^\s*-?\s*\*Measurements:\*\s*$")
MEAS_BULLET_RE = re.compile(r"^\s*-\s*\*\*(?:M-)?(Primary|Secondary|Tertiary):\*\*\s*(.*)$")
ASSESS_BULLET_RE = re.compile(
    r"^\s*-\s*\*\*(?:"
    r"(Primary) assessment\.|E-(Primary) Assessment:|"
    r"(Secondary) co-assessment\.|E-(Secondary) Assessment:|"
    r"(Tertiary) integrity check\.|E-(Tertiary) Integrity Check:"
    r")\*\*\s*(.*)$"
)
FAILURE_BULLET_RE = re.compile(
    r"^(\s*)-\s*\*\*(Primary|Secondary|Tertiary) failure[.:]\*\*\s*(?:Non-compliant:\s*)?(.*)$"
)
ANCHOR_LINE_RE = re.compile(r'^<a id="([^"]+)"></a>$')
NONCOMPLIANT_PREFIX_RE = re.compile(r"^Non-compliant:\s*")
LIST_ITEM_RE = re.compile(r"^\s+-\s+\S")

TIER_ORDER = ("Primary", "Secondary", "Tertiary")


def _content_lines(block: list[str]) -> list[str]:
    """Non-blank, non-standalone-anchor lines of a block."""
    return [r for r in block if r.strip() and not ANCHOR_LINE_RE.match(r.strip())]


def e_block_is_clean(e_block: list[str]) -> bool:
    """True only for the two shapes we can migrate without losing content:

    * primary-only: a single ``- E: <inline prose>`` line and nothing else, or
    * full tier: ``- E:`` (empty) followed only by tier assessment bullets.
    """
    body = _content_lines(e_block)
    if not body:
        return False
    m = E_LINE_RE.match(body[0])
    if not m:
        return False
    inline = m.group(1).strip()
    rest = body[1:]
    if inline and not inline.startswith("**"):
        # primary-only inline prose, optionally trailed by a continuation sub-list
        return all(LIST_ITEM_RE.match(r) for r in rest)
    if inline:
        return False
    return len(rest) > 0 and all(ASSESS_BULLET_RE.match(r) for r in rest)


def c_block_is_clean(c_block: list[str], c_line_idx: int) -> bool:
    """True only for migratable C shapes:

    * a single ``- C: <inline prose>`` and nothing else, or
    * ``- C:`` (empty) followed by failure bullets (with an optional leading
      non-failure satisfaction bullet).
    """
    inline = C_LINE_RE.match(c_block[c_line_idx]).group(1).strip()
    rest = _content_lines(c_block[c_line_idx + 1:])
    if inline:
        if NONCOMPLIANT_PREFIX_RE.sub("", inline).strip() == "":
            return False
        return len(rest) == 0
    if not rest:
        return False
    for i, raw in enumerate(rest):
        if FAILURE_BULLET_RE.match(raw):
            continue
        if i == 0 and raw.lstrip().startswith("- "):
            continue  # leading satisfaction sentence
        return False
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Workspace root.")
    parser.add_argument("--terms", nargs="+", help="Definition terms (exact heading titles).")
    parser.add_argument("--file", help="Migrate every definition in this Chapter Five file.")
    parser.add_argument("--dry-run", action="store_true", help="Report without writing.")
    return parser.parse_args()


def _norm(text: str) -> str:
    """Normalize prose for duplicate detection: drop anchors/link URLs, collapse ws."""
    text = re.sub(r'<a id="[^"]*"></a>', "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\s+", " ", text).strip().rstrip(".").lower()
    return text


def entry_bounds(lines: list[str], heading_idx: int) -> tuple[int, int]:
    """Body of a single entry: up to the next H4/H5 heading (children excluded).

    Trailing inter-entry lines (blank lines, ``---`` separators, and the *next*
    entry's leading ``<a id="...">`` anchors) are trimmed off so they stay
    outside the transformed section.
    """
    end = len(lines)
    for i in range(heading_idx + 1, len(lines)):
        stripped = lines[i].strip()
        if re.match(r"#{1,6}\s", stripped):
            end = i
            break
    while end > heading_idx + 1:
        stripped = lines[end - 1].strip()
        if stripped == "" or stripped == "---" or ANCHOR_LINE_RE.match(stripped):
            end -= 1
        else:
            break
    return heading_idx + 1, end


def transform_section(section: list[str], term: str) -> tuple[list[str] | None, str]:
    o_start = e_start = c_start = None
    for i, raw in enumerate(section):
        if o_start is None and O_LINE_RE.match(raw):
            o_start = i
        elif o_start is not None and e_start is None and E_MARKER_RE.match(raw):
            e_start = i
        elif e_start is not None and c_start is None and C_MARKER_RE.match(raw):
            c_start = i
            break
    if o_start is None or e_start is None or c_start is None:
        return None, "missing O/E/C markers"

    pre = section[:o_start]
    o_block = section[o_start:e_start]
    e_block = section[e_start:c_start]
    c_block = section[c_start:]

    # Content after the first `---` separator belongs between entries (e.g. a
    # relocated-aim note); keep it verbatim as a tail rather than folding it into C.
    hr_idx = next((i for i, raw in enumerate(c_block) if raw.strip() == "---"), None)
    if hr_idx is not None:
        tail = ["", *c_block[hr_idx:]]
        c_block = c_block[:hr_idx]
    else:
        tail = []

    # Guard: only the -e / -c anchors may be standalone anchor lines. Anything
    # else (for example a *-measurements anchor) is left for manual handling.
    for raw in o_block + e_block + c_block:
        m = ANCHOR_LINE_RE.match(raw.strip())
        if m and not (m.group(1).endswith("-e") or m.group(1).endswith("-c")):
            return None, f"unexpected standalone anchor #{m.group(1)}"

    # ---- O: relabel In scope / Out of scope, drop the duplicated concept line. ----
    o_concept = O_LINE_RE.match(o_block[0]).group(1).strip()
    scope_lines: list[str] = []
    in_scope_texts: list[str] = []
    for raw in o_block[1:]:
        if MEAS_HEADER_RE.match(raw) or MEAS_BULLET_RE.match(raw) or not raw.strip():
            continue
        mi = IN_SCOPE_RE.match(raw)
        if mi:
            indent, label, text = mi.group(1), mi.group(2).strip(), mi.group(3).strip()
            scope_lines.append(f"{indent}- **{label}:** {text}".rstrip())
            in_scope_texts.append(text)
            continue
        mo = OUT_SCOPE_RE.match(raw)
        if mo:
            indent, label, text = mo.group(1), mo.group(2).strip(), mo.group(3).strip()
            scope_lines.append(f"{indent}- **{label}:** {text}".rstrip())
            continue
        scope_lines.append(raw)  # continuation sub-bullet (kept verbatim)

    if not in_scope_texts:
        if not o_concept:
            return None, "no concept and no In scope to build O"
        scope_lines.insert(0, f"  - **In scope:** {o_concept}")
    elif o_concept and len(in_scope_texts) == 1 and _norm(o_concept) != _norm(in_scope_texts[0]):
        return None, "O-line concept diverges from In scope (manual review)"

    if not any(OUT_SCOPE_RE.match(raw) for raw in o_block[1:]):
        scope_lines.append(
            "  - **Out of scope:** formal-label-only or nominal treatment without "
            "functional effect on the constitutionally governed subject matter."
        )

    new_o = ["- **What it is**", *scope_lines]

    # Only migrate E/C shapes we can transform without losing content.
    if not e_block_is_clean(e_block):
        return None, "E block has irregular content (manual review)"
    c_line_idx_probe = next((i for i, raw in enumerate(c_block) if C_LINE_RE.match(raw)), None)
    if c_line_idx_probe is None:
        return None, "no C marker line"
    if not c_block_is_clean(c_block, c_line_idx_probe):
        return None, "C block has irregular content (manual review)"

    # ---- Measures (from O block, where the *Measurements:* block lives) and E block. ----
    measures: dict[str, str] = {}
    for raw in o_block + e_block:
        m = MEAS_BULLET_RE.match(raw)
        if m:
            measures.setdefault(m.group(1), m.group(2).strip())
    if "Primary" not in measures:
        return None, "no Primary measurement bullet found"

    # ---- Assessments: tier bullets, or inline E prose as the primary assessment. ----
    assessments: dict[str, str] = {}
    for raw in e_block:
        m = ASSESS_BULLET_RE.match(raw)
        if m:
            tier = next(g for g in m.groups()[:6] if g)
            assessments[tier] = m.group(7).strip()
    e_body = _content_lines(e_block)
    e_inline = E_LINE_RE.match(e_body[0]) if e_body else None
    inline_text = e_inline.group(1).strip() if e_inline else ""
    # A continuation sub-list under an inline `- E:` lead nests under the assessment.
    primary_sublist: list[str] = []
    if inline_text and not inline_text.startswith("**"):
        if "Primary" not in assessments:
            assessments["Primary"] = inline_text
        primary_sublist = ["    " + raw for raw in e_body[1:] if LIST_ITEM_RE.match(raw)]

    # Guidepost pairs each assessment with a measure of the same tier. If an
    # assessment tier has no matching measure, pairing is ambiguous and emitting
    # would drop content — leave such terms for manual review.
    extra_assess = [t for t in TIER_ORDER if t in assessments and t not in measures]
    if extra_assess:
        return None, f"assessment tier(s) {extra_assess} without matching measure (manual review)"

    # Anchors may sit in either block (a `-c` anchor is sometimes indented inside
    # the legacy E block). Route each by its slug suffix and normalize to column 0.
    anchor_ids = [
        m.group(1)
        for raw in e_block + c_block
        if (m := ANCHOR_LINE_RE.match(raw.strip()))
    ]
    e_anchor = [f'<a id="{a}"></a>' for a in anchor_ids if a.endswith("-e")]
    c_anchor = [f'<a id="{a}"></a>' for a in anchor_ids if a.endswith("-c")]

    new_e: list[str] = [*e_anchor, "- **How to measure and assess**"]
    for tier in TIER_ORDER:
        if tier in measures:
            new_e.append(f"  - **{tier} measure:** {measures[tier]}")
            if tier in assessments:
                new_e.append("")
                new_e.append(f"    **{tier} assessment:** {assessments[tier]}")
                if tier == "Primary":
                    new_e.extend(primary_sublist)

    # ---- C: relabel failure sublabels, strip redundant "Non-compliant:" prefixes. ----
    c_line_idx = next((i for i, raw in enumerate(c_block) if C_LINE_RE.match(raw)), None)
    if c_line_idx is None:
        return None, "no C marker line"
    c_inline = C_LINE_RE.match(c_block[c_line_idx]).group(1).strip()

    new_c: list[str] = [*c_anchor, "- **What must hold**"]
    if c_inline:
        new_c.append("  - " + NONCOMPLIANT_PREFIX_RE.sub("", c_inline))
    for raw in c_block[c_line_idx + 1:]:
        if ANCHOR_LINE_RE.match(raw.strip()):
            continue
        mf = FAILURE_BULLET_RE.match(raw)
        if mf:
            indent, tier, rest = mf.group(1), mf.group(2), mf.group(3).strip()
            new_c.append(f"{indent}- **{tier} failure:** {rest}")
        else:
            new_c.append(raw)
    while new_c and not new_c[-1].strip():
        new_c.pop()

    rebuilt = [*pre, *new_o, *new_e, *new_c, *tail]
    return rebuilt, ""


def migrate_text(text: str, only_terms: set[str] | None) -> tuple[str, list[str], list[str]]:
    lines = text.splitlines()
    heads: list[tuple[int, str]] = []
    for i, raw in enumerate(lines):
        m = HEADING_RE.match(raw.strip())
        if m:
            heads.append((i, m.group(1).strip()))

    migrated: list[str] = []
    skipped: list[str] = []
    for idx, term in reversed(heads):
        if only_terms is not None and term not in only_terms:
            continue
        start, end = entry_bounds(lines, idx)
        rebuilt, reason = transform_section(lines[start:end], term)
        if rebuilt is None:
            skipped.append(f"{term}: {reason}")
            continue
        lines[start:end] = rebuilt
        migrated.append(term)

    migrated.reverse()
    return "\n".join(lines) + ("\n" if text.endswith("\n") else ""), migrated, skipped


def locate_file(root: pathlib.Path, term: str) -> pathlib.Path | None:
    registry_path = root / "ai_corpus/indexes/definition_registry.json"
    registry: dict = {"definitions": []}
    if registry_path.is_file():
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
    located = find_term_body(root, term, registry)
    if located:
        return root / located[0]
    for file_name in CH5_ALL:
        path = root / file_name
        if path.is_file() and f"#### {term}" in path.read_text(encoding="utf-8"):
            return path
    return None


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve()
    migrated: list[str] = []
    skipped: list[str] = []

    if args.file:
        path = root / args.file
        text = path.read_text(encoding="utf-8")
        updated, mig, skip = migrate_text(text, only_terms=None)
        migrated.extend(mig)
        skipped.extend(skip)
        if not args.dry_run:
            path.write_text(updated, encoding="utf-8")
    elif args.terms:
        cache: dict[pathlib.Path, str] = {}
        by_file: dict[pathlib.Path, set[str]] = {}
        for term in args.terms:
            path = locate_file(root, term)
            if path is None:
                skipped.append(f"{term}: source not found")
                continue
            by_file.setdefault(path, set()).add(term)
            cache.setdefault(path, path.read_text(encoding="utf-8"))
        for path, terms in by_file.items():
            updated, mig, skip = migrate_text(cache[path], only_terms=terms)
            migrated.extend(mig)
            skipped.extend(skip)
            cache[path] = updated
        if not args.dry_run:
            for path, content in cache.items():
                path.write_text(content, encoding="utf-8")
    else:
        print("error: pass --file or --terms", file=sys.stderr)
        return 2

    print(f"apply-measurements-to-e: migrated {len(migrated)} definition(s)")
    for term in migrated:
        print(f"  + {term}")
    for line in skipped:
        print(f"  - {line}", file=sys.stderr)
    if args.dry_run and migrated:
        print("(dry run — no files written)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
