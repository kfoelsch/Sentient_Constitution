#!/usr/bin/env python3
"""Sort / relocate Chapter Five full O/E/C definitions (``sort definitions``).

Moves definition *blocks* between Part A/B/C when they disagree with
cluster / family member routing (same rules as ``ch5_definition_location_audit``).

Default is **dry-run** (plan only). Pass ``--apply`` to rewrite the three Chapter
Five files in ``--root``. After moves, Part A alphabetical bullets that still
use fragment-only ``](#slug)`` links are rewritten when the slug's home is now
Part B or Part C.

After a successful ``--apply`` that adds, removes, or rewrites Part B content,
**section 2 is automatically regrouped** using ``reorder_ch5_section2_groups``
in **relaxed** mode (same as ``--relax-unlisted``): known ``GROUPS`` order
first, then any other Part B primary anchors under an editorial **Ungrouped**
heading. To fail fast when ``GROUPS`` is incomplete, run the reorder script
manually with default (strict) flags.

Does **not** fix: dependent-cluster context in the wrong file, duplicate O/E/C
slugs, §3 orphan definitions (not in any member list), or conflicts where one
entry maps to two different expected sections—resolve those manually first.

Examples::

  python3 tools/sort_ch5_definitions.py --root .
  python3 tools/sort_ch5_definitions.py --root . --apply

Makefile::

  make sort-ch5-definitions
  make sort-ch5-definitions ARGS=--apply
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_definition_location_audit import (  # noqa: E402
    ANCHOR_RE,
    DEF_HEADING_RE,
    CH5_SECTION_BY_FILE,
    DefinitionEntry,
    WrongSectionMove,
    audit,
    build_indexes,
    iter_wrong_section_moves,
)
from ch5_paths import CH5_ALL, CH5_PART_A, CH5_PART_B, CH5_PART_C  # noqa: E402
from reorder_ch5_section2_groups import reorder_section2_groups  # noqa: E402

FILE_FOR_SECTION: dict[str, str] = {v: k for k, v in CH5_SECTION_BY_FILE.items()}
FRAG_LINK_RE = re.compile(r"\]\(#([a-z0-9\-]+)\)")
DIR_BULLET_FRAG = re.compile(r"^(- \[[^\]]+\])\((#[a-z0-9\-]+)\)\s*$")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Repository root.")
    p.add_argument(
        "--apply",
        action="store_true",
        help="Perform moves (default: print plan only).",
    )
    return p.parse_args()


def _heading_depth(line: str) -> int | None:
    m = DEF_HEADING_RE.match(line)
    return len(m.group(1)) if m else None


def extract_block_span(lines: list[str], entry: DefinitionEntry) -> tuple[int, int]:
    """Return [start, end) line indices for the definition block containing entry."""
    h = entry.line - 1
    depth = _heading_depth(lines[h])
    if depth is None:
        raise SystemExit(f"expected a ####/##### title line at {entry.location}")

    lo = h
    i = h - 1
    while i >= 0:
        s = lines[i].strip()
        if s in ("", "<br>"):
            lo = i
            i -= 1
            continue
        if ANCHOR_RE.match(s):
            lo = i
            i -= 1
            continue
        if s == "---":
            lo = i
            break
        break
    start = lo

    end = len(lines)
    for j in range(h + 1, len(lines)):
        m = DEF_HEADING_RE.match(lines[j])
        if m and len(m.group(1)) <= depth and not m.group(
            2
        ).startswith("In plain terms:"):
            k = j - 1
            while k > h and lines[k].strip() == "":
                k -= 1
            if k > h and lines[k].strip() == "---":
                end = k + 1
            else:
                end = j
            break
    return start, end


def build_anchor_home_from_texts(text_by_file: dict[str, str]) -> dict[str, str]:
    home: dict[str, str] = {}
    for fname in (CH5_PART_A, CH5_PART_B, CH5_PART_C):
        text = text_by_file.get(fname, "")
        for line in text.splitlines():
            m = ANCHOR_RE.match(line.strip())
            if m:
                home[m.group(1)] = fname
    return home


def adjusted_anchor_home(
    initial: dict[str, str],
    moves: list[WrongSectionMove],
) -> dict[str, str]:
    out = dict(initial)
    for m in moves:
        tgt = FILE_FOR_SECTION[m.expected_section]
        for s in m.entry.slugs:
            out[s] = tgt
    return out


def rewrite_fragment_links(block: str, target_file: str, home: dict[str, str]) -> str:
    def repl(m: re.Match[str]) -> str:
        slug = m.group(1)
        h = home.get(slug)
        if h is None or h == target_file:
            return m.group(0)
        return f"]({h}#{slug})"

    return FRAG_LINK_RE.sub(repl, block)


def repair_part_a_directory(text: str, home: dict[str, str]) -> str:
    had_trailing_nl = text.endswith("\n")
    out_lines: list[str] = []
    for line in text.splitlines():
        m = DIR_BULLET_FRAG.match(line.strip())
        if m:
            slug = m.group(2)[1:]
            h = home.get(slug)
            if h and h != CH5_PART_A:
                out_lines.append(f"{m.group(1)}({h}#{slug})")
                continue
        out_lines.append(line)
    result = "\n".join(out_lines)
    if had_trailing_nl:
        result += "\n"
    return result


def dedupe_moves(
    raw: list[WrongSectionMove],
) -> tuple[list[WrongSectionMove], list[str]]:
    by_key: dict[tuple[str, int], WrongSectionMove] = {}
    errors: list[str] = []
    for m in raw:
        k = (m.entry.file, m.entry.line)
        prev = by_key.get(k)
        if prev is None:
            by_key[k] = m
        elif prev.expected_section != m.expected_section:
            errors.append(
                f"{m.entry.location}: conflicting relocation targets "
                f"§{prev.expected_section} (member #{prev.member_slug}) vs "
                f"§{m.expected_section} (member #{m.member_slug}); fix manually."
            )
    return sorted(
        by_key.values(), key=lambda m: (m.entry.title.lower(), m.entry.line)
    ), errors


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    missing = [n for n in CH5_ALL if not (root / n).is_file()]
    if missing:
        print(f"Missing Chapter Five file(s): {', '.join(missing)}", file=sys.stderr)
        return 2

    entries, members = build_indexes(root)
    blocking = audit(entries, members)
    raw_moves = list(iter_wrong_section_moves(entries, members))
    moves, conflicts = dedupe_moves(raw_moves)

    def is_wrong_section_line(msg: str) -> bool:
        return (
            "cluster member #" in msg
            and "full O/E/C home is only elsewhere" in msg
        )

    other_errs = [e for e in blocking if not is_wrong_section_line(e)]

    if not args.apply:
        if conflicts:
            for c in conflicts:
                print(c, file=sys.stderr)
            return 1
        if other_errs:
            print(
                "\nOther definition-location issues (not auto-fixed by this tool):",
                file=sys.stderr,
            )
            for e in other_errs:
                print(f"  {e}", file=sys.stderr)
            return 1
        if moves:
            print("Planned relocations (cluster / family routing):")
            for m in moves:
                dest = FILE_FOR_SECTION[m.expected_section]
                print(
                    f"  §{m.entry.section} {m.entry.location} → §{m.expected_section} "
                    f"{dest}  (member #{m.member_slug}; {m.entry.title!r})"
                )
            part_b_touched = any(
                m.entry.file == CH5_PART_B
                or FILE_FOR_SECTION[m.expected_section] == CH5_PART_B
                for m in moves
            )
            if part_b_touched:
                print(
                    "\nWith --apply: Part B section 2 would be regrouped "
                    "(reorder_section2_groups, relaxed / --relax-unlisted)."
                )
            print("\nDry-run only. Re-run with --apply to write files.")
        else:
            print("PASS: nothing to sort; definition-location audit is clean.")
        return 0

    if conflicts:
        for c in conflicts:
            print(c, file=sys.stderr)
        return 1
    if other_errs:
        print("Refusing --apply: fix these first:", file=sys.stderr)
        for e in other_errs:
            print(f"  {e}", file=sys.stderr)
        return 1
    if not moves:
        print("Nothing to apply.")
        return 0

    text_by: dict[str, str] = {}
    for fname in CH5_ALL:
        text_by[fname] = (root / fname).read_text(encoding="utf-8")

    initial_home = build_anchor_home_from_texts(text_by)
    post_home = adjusted_anchor_home(initial_home, moves)
    lines_map: dict[str, list[str]] = {f: text_by[f].split("\n") for f in CH5_ALL}
    extracted: list[tuple[str, str]] = []

    for m in sorted(moves, key=lambda x: (x.entry.file, -x.entry.line)):
        fname = m.entry.file
        lines = lines_map[fname]
        start, end = extract_block_span(lines, m.entry)
        block_raw = "\n".join(lines[start:end])
        dest = FILE_FOR_SECTION[m.expected_section]
        block = rewrite_fragment_links(block_raw, dest, post_home)
        lines_map[fname] = lines[:start] + lines[end:]
        extracted.append((dest, block))

    by_dest: dict[str, list[str]] = {CH5_PART_A: [], CH5_PART_B: [], CH5_PART_C: []}
    for dest_file, block in extracted:
        by_dest[dest_file].append(block)
    for dest in (CH5_PART_A, CH5_PART_B, CH5_PART_C):
        blocks = by_dest[dest]
        if not blocks:
            continue
        blocks.sort(key=lambda b: b.lower())
        body = "\n\n".join(blocks)
        cur = "\n".join(lines_map[dest])
        if cur and not cur.endswith("\n"):
            cur += "\n"
        lines_map[dest] = (cur + "\n\n" + body).split("\n")

    final_text: dict[str, str] = {}
    for fname in CH5_ALL:
        new_text = "\n".join(lines_map[fname])
        if not new_text.endswith("\n"):
            new_text += "\n"
        final_text[fname] = new_text

    final_home = build_anchor_home_from_texts(final_text)
    final_text[CH5_PART_A] = repair_part_a_directory(
        final_text[CH5_PART_A], final_home
    )

    for fname in CH5_ALL:
        (root / fname).write_text(final_text[fname], encoding="utf-8")

    entries2, members2 = build_indexes(root)
    remaining = audit(entries2, members2)
    if remaining:
        for e in remaining:
            print(e, file=sys.stderr)
        print(
            f"\nFAIL: {len(remaining)} issue(s) after --apply; files were written.",
            file=sys.stderr,
        )
        return 1

    part_b_touched = any(
        m.entry.file == CH5_PART_B
        or FILE_FOR_SECTION[m.expected_section] == CH5_PART_B
        for m in moves
    )
    if part_b_touched:
        regroup_rc = reorder_section2_groups(root, strict=False)
        if regroup_rc != 0:
            print(
                "FAIL: section 2 regrouping failed (e.g. missing GROUPS id).",
                file=sys.stderr,
            )
            return regroup_rc

    print(
        f"Applied {len(moves)} relocation(s). PASS: Chapter Five definition locations."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
