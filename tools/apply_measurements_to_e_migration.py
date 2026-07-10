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
  * ``- O:`` / ``- **O:**`` line (concept, usually duplicated in In scope) + In scope / Out of scope.
  * Optional ``**Depends on:**`` sub-bullet under O.
  * ``*Measurements:*`` header block of ``**Primary:**`` / ``**Secondary:**`` /
    ``**Tertiary:**`` bullets between O and the ``-a`` / ``-e`` anchor.
  * ``- A:`` / ``- E:`` either inline prose (primary-only terms) or tier assessment bullets.
  * ``- C:`` either inline prose, ``Non-compliant:`` header + list, or failure sublabels.

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

LABEL_O = r"(?:\*\*O:\*\*|(?:\*\*)?O(?:\*\*)?:)"
LABEL_AE = r"(?:\*\*[AE]:\*\*|(?:\*\*)?[AE](?:\*\*)?:)"
LABEL_C = r"(?:\*\*C:\*\*|(?:\*\*)?C(?:\*\*)?:)"
O_LINE_RE = re.compile(rf"^- {LABEL_O}\s*(.*)$")
WHAT_IT_IS_RE = re.compile(r"^- \*\*What it is\*\*\s*$")
ASSESS_MARKER_RE = re.compile(
    rf'^(?:<a id="[^"]*-(?:a|e)"></a>|- {LABEL_AE}(\s|$))'
)
C_MARKER_RE = re.compile(rf'^(?:<a id="[^"]*-c"></a>|- {LABEL_C}(\s|$))')
C_LINE_RE = re.compile(rf"^- {LABEL_C}\s*(.*)$")
IN_SCOPE_RE = re.compile(
    r"^(\s*)- \*{0,2}(In scope(?:\s*—\s*[^:*]+|\s*:))\*{0,2}\s*(.*)$"
)
OUT_SCOPE_RE = re.compile(r"^(\s*)- \*{0,2}(Out of scope:)\*{0,2}\s*(.*)$")
DEPENDS_RE = re.compile(r"^(\s*)- \*{0,2}(Depends on:)\*{0,2}\s*(.*)$")
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

CONTINUATION_RE = re.compile(r"^\s+(?:-\s+|\d+\.\s+)\S")
ASSESS_AT_COL0_RE = re.compile(rf"^- {LABEL_AE}(\s|$)")
ASSESS_LINE_RE = re.compile(rf"^- {LABEL_AE}\s*(.*)$")
C_AT_COL0_RE = re.compile(rf"^- {LABEL_C}(\s|$)")
ASSESS_ANCHOR_SUFFIX_RE = re.compile(r"-(a|e)$")
C_ANCHOR_SUFFIX_RE = re.compile(r"-c$")
MEASUREMENTS_ANCHOR_SUFFIX_RE = re.compile(r"-measurements$")

TIER_ORDER = ("Primary", "Secondary", "Tertiary")


def _content_lines(block: list[str]) -> list[str]:
    """Non-blank, non-standalone-anchor lines of a block."""
    return [r for r in block if r.strip() and not ANCHOR_LINE_RE.match(r.strip())]


def assess_block_is_clean(assess_block: list[str]) -> bool:
    """Migratable A/E block: inline prose (+ optional sub-list) or tier bullets only."""
    body = _content_lines(assess_block)
    if not body:
        return False
    m = ASSESS_LINE_RE.match(body[0])
    if not m:
        return False
    inline = m.group(1).strip()
    rest = body[1:]
    if inline and not inline.startswith("**"):
        return all(CONTINUATION_RE.match(r) for r in rest)
    if inline:
        return False
    return len(rest) > 0 and all(ASSESS_BULLET_RE.match(r) for r in rest)


def e_block_is_clean(e_block: list[str]) -> bool:
    return assess_block_is_clean(e_block)


def c_block_is_clean(c_block: list[str], c_line_idx: int) -> bool:
    """True only for migratable C shapes:

    * a single ``- C: <inline prose>`` and nothing else, or
    * ``- C:`` (empty) followed by failure bullets (with an optional leading
      non-failure satisfaction bullet).
    """
    inline = C_LINE_RE.match(c_block[c_line_idx]).group(1).strip()
    rest = _content_lines(c_block[c_line_idx + 1:])
    if inline:
        remainder = NONCOMPLIANT_PREFIX_RE.sub("", inline).strip()
        if remainder == "":
            if not any(LIST_ITEM_RE.match(r) for r in rest):
                return False
            for raw in rest:
                if FAILURE_BULLET_RE.match(raw) or LIST_ITEM_RE.match(raw):
                    continue
                if raw.strip():
                    continue
                return False
            return True
        if not inline.startswith("**"):
            return len(rest) == 0
        return False
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


def _bold_scope_line(indent: str, label: str, text: str) -> str:
    label = label.strip()
    text = text.strip().lstrip(":").strip()
    if label.endswith(":"):
        return f"{indent}- **{label}** {text}".rstrip()
    return f"{indent}- **{label}:** {text}".rstrip()


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
    if any(raw.strip() == "- **How to measure and assess**" for raw in section):
        return None, "already guidepost M/A"

    o_start = e_start = c_start = None
    for i, raw in enumerate(section):
        if o_start is None and (O_LINE_RE.match(raw) or WHAT_IT_IS_RE.match(raw)):
            o_start = i
        elif o_start is not None and e_start is None:
            if ASSESS_AT_COL0_RE.match(raw):
                e_start = i
            elif ANCHOR_LINE_RE.match(raw.strip()):
                m = ANCHOR_LINE_RE.match(raw.strip())
                if m and ASSESS_ANCHOR_SUFFIX_RE.search(m.group(1)) and raw.lstrip().startswith("<a"):
                    e_start = i
        elif e_start is not None and c_start is None and C_AT_COL0_RE.match(raw):
            c_start = i
            break
    if o_start is None or e_start is None or c_start is None:
        return None, "missing O/A/C markers"

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

    # Guard: only assessment/compliance anchors may be standalone. Measurements
    # anchors and other legacy ids are skipped during O parsing.
    for raw in o_block + e_block + c_block:
        m = ANCHOR_LINE_RE.match(raw.strip())
        if not m:
            continue
        slug = m.group(1)
        if (
            ASSESS_ANCHOR_SUFFIX_RE.search(slug)
            or C_ANCHOR_SUFFIX_RE.search(slug)
            or MEASUREMENTS_ANCHOR_SUFFIX_RE.search(slug)
        ):
            continue
        return None, f"unexpected standalone anchor #{slug}"

    # ---- O: relabel In scope / Out of scope / Depends on; drop duplicated concept line. ----
    o_line = o_block[0]
    o_concept = ""
    if O_LINE_RE.match(o_line):
        o_concept = O_LINE_RE.match(o_line).group(1).strip()
    scope_lines: list[str] = []
    in_scope_texts: list[str] = []
    for raw in o_block[1:]:
        if MEAS_HEADER_RE.match(raw) or MEAS_BULLET_RE.match(raw) or not raw.strip():
            continue
        m_anchor = ANCHOR_LINE_RE.match(raw.strip())
        if m_anchor and MEASUREMENTS_ANCHOR_SUFFIX_RE.search(m_anchor.group(1)):
            continue
        if m_anchor:
            continue
        mi = IN_SCOPE_RE.match(raw)
        if mi:
            indent, label, text = mi.group(1), mi.group(2).strip(), mi.group(3).strip()
            scope_lines.append(_bold_scope_line(indent, label, text))
            in_scope_texts.append(text)
            continue
        mo = OUT_SCOPE_RE.match(raw)
        if mo:
            indent, label, text = mo.group(1), mo.group(2).strip(), mo.group(3).strip()
            scope_lines.append(_bold_scope_line(indent, label, text))
            continue
        md = DEPENDS_RE.match(raw)
        if md:
            indent, label, text = md.group(1), md.group(2).strip(), md.group(3).strip()
            if "**" in raw:
                scope_lines.append(raw.rstrip())
            else:
                scope_lines.append(_bold_scope_line(indent, label, text))
            continue
        scope_lines.append(raw)  # continuation sub-bullet (kept verbatim)

    if WHAT_IT_IS_RE.match(o_line):
        new_o = [o_line, *scope_lines]
    else:
        if o_concept and not WHAT_IT_IS_RE.match(o_line):
            if not in_scope_texts or all(_norm(o_concept) != _norm(t) for t in in_scope_texts):
                scope_lines.insert(0, f"  - **In scope:** {o_concept}")
        if not any(OUT_SCOPE_RE.match(raw) or "**Out of scope:**" in raw for raw in o_block[1:]):
            scope_lines.append(
                "  - **Out of scope:** formal-label-only or nominal treatment without "
                "functional effect on the constitutionally governed subject matter."
            )
        new_o = ["- **What it is**", *scope_lines]

    # Only migrate A/C shapes we can transform without losing content.
    if not assess_block_is_clean(e_block):
        return None, "A block has irregular content (manual review)"
    c_line_idx_probe = next(
        (i for i, raw in enumerate(c_block) if C_LINE_RE.match(raw.strip()) or C_LINE_RE.match(raw)),
        None,
    )
    if c_line_idx_probe is None:
        return None, "no C marker line"
    if not c_block_is_clean(c_block, c_line_idx_probe):
        return None, "C block has irregular content (manual review)"

    # ---- Measures (from O block) and A block. ----
    measures: dict[str, str] = {}
    for raw in o_block + e_block:
        m = MEAS_BULLET_RE.match(raw)
        if m:
            measures.setdefault(m.group(1), m.group(2).strip())
    if "Primary" not in measures:
        return None, "no Primary measurement bullet found"

    # ---- Assessments: tier bullets, or inline A prose as the primary assessment. ----
    assessments: dict[str, str] = {}
    for raw in e_block:
        m = ASSESS_BULLET_RE.match(raw)
        if m:
            tier = next(g for g in m.groups()[:6] if g)
            assessments[tier] = m.group(7).strip()
    e_body = _content_lines(e_block)
    e_inline = ASSESS_LINE_RE.match(e_body[0]) if e_body else None
    inline_text = e_inline.group(1).strip() if e_inline else ""
    primary_sublist: list[str] = []
    if inline_text and not inline_text.startswith("**"):
        if "Primary" not in assessments:
            assessments["Primary"] = inline_text
        primary_sublist = [
            "    " + raw.lstrip() for raw in e_body[1:] if CONTINUATION_RE.match(raw)
        ]

    extra_assess = [t for t in TIER_ORDER if t in assessments and t not in measures]
    if extra_assess:
        return None, f"assessment tier(s) {extra_assess} without matching measure (manual review)"

    seen: set[str] = set()
    e_anchor: list[str] = []
    for raw in section[o_start:c_start]:
        m = ANCHOR_LINE_RE.match(raw.strip())
        if m and ASSESS_ANCHOR_SUFFIX_RE.search(m.group(1)):
            line = f'<a id="{m.group(1)}"></a>'
            if line not in seen:
                seen.add(line)
                e_anchor.append(line)

    new_e: list[str] = [*e_anchor, "- **How to measure and assess**"]
    for tier in TIER_ORDER:
        if tier in measures:
            new_e.append(f"  - **{tier} measure:** {measures[tier]}")
            if tier in assessments:
                new_e.append("")
                new_e.append(f"    **{tier} assessment:** {assessments[tier]}")
                if tier == "Primary":
                    new_e.extend(primary_sublist)

    # ---- C: relabel failure sublabels; convert Non-compliant lists; strip redundant prefix. ----
    c_line_idx = c_line_idx_probe
    c_inline = C_LINE_RE.match(c_block[c_line_idx]).group(1).strip()
    c_rest = [r for r in c_block[c_line_idx + 1:] if r.strip() and not ANCHOR_LINE_RE.match(r.strip())]

    seen_c: set[str] = set()
    c_anchor: list[str] = []
    for raw in section[e_start:]:
        m = ANCHOR_LINE_RE.match(raw.strip())
        if m and C_ANCHOR_SUFFIX_RE.search(m.group(1)):
            line = f'<a id="{m.group(1)}"></a>'
            if line not in seen_c:
                seen_c.add(line)
                c_anchor.append(line)

    new_c: list[str] = [*c_anchor, "- **What must hold**"]
    handled_c_rest = False
    if c_inline:
        remainder = NONCOMPLIANT_PREFIX_RE.sub("", c_inline).strip()
        if remainder == "" and c_rest:
            handled_c_rest = True
            tiers = list(TIER_ORDER)
            ti = 0
            for raw in c_rest:
                if LIST_ITEM_RE.match(raw):
                    text = re.sub(r"^\s+-\s+", "", raw).strip()
                    tier = tiers[min(ti, 2)]
                    indent = re.match(r"^(\s*)", raw).group(1)
                    new_c.append(f"{indent}- **{tier} failure:** {text}")
                    ti += 1
                elif raw.strip():
                    new_c.append(f"  - {raw.strip()}")
        elif remainder:
            new_c.append(f"  - {remainder}")
    if not handled_c_rest:
        for raw in c_block[c_line_idx + 1:]:
            if ANCHOR_LINE_RE.match(raw.strip()):
                continue
            mf = FAILURE_BULLET_RE.match(raw)
            if mf:
                indent, tier, rest = mf.group(1), mf.group(2), mf.group(3).strip()
                new_c.append(f"{indent}- **{tier} failure:** {rest}")
            elif LIST_ITEM_RE.match(raw) and not c_inline:
                new_c.append(raw)
            elif raw.strip():
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
