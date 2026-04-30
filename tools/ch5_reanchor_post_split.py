#!/usr/bin/env python3
"""Rebuild merged Chapter Five anchor→file map and rewrite fragment + corpus links.

Run from repo root after split: python3 tools/ch5_reanchor_post_split.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

_ROOT_TOOLS = Path(__file__).resolve().parent
if str(_ROOT_TOOLS) not in sys.path:
    sys.path.insert(0, str(_ROOT_TOOLS))

from ch5_paths import CH5_PART_A, CH5_PART_B, CH5_PART_C

ROOT = Path(__file__).resolve().parents[1]

ANCHOR_RE = re.compile(r'<a id="([^"]+)"></a>')
FRAG_LINK_RE = re.compile(r"\]\(#([^)]+)\)")
CORPUS_CH5_RE = re.compile(re.escape(CH5_PART_A) + r"#([A-Za-z0-9_\-]+)")


def collect_anchors(text: str) -> set[str]:
    return set(ANCHOR_RE.findall(text))


def directory_supplement_map(part_a: str) -> dict[str, str]:
    """Anchors listed in the alphabetical directory but missing explicit <a id> in body."""
    extra: dict[str, str] = {}
    reader_marker = "#### Reader-friendly additions to consider"
    unified_heading = "#### All definitions and clusters (A–Z)"
    semi_marker = '<a id="semi-independent-definitions-a-z"></a>'
    dep_marker = '<a id="dependent-clusters-a-z"></a>'
    indep_marker = '<a id="independent-definitions-a-z"></a>'

    def ingest_block(block: str) -> None:
        for line in block.splitlines():
            s = line.strip()
            m = re.match(r"^-\s\[[^\]]+\]\(#([^)]+)\)\s*$", s)
            if m:
                extra[m.group(1)] = CH5_PART_A
                continue
            m = re.match(
                r"^-\s\[[^\]]+\]\(" + re.escape(CH5_PART_B) + r"#([^)]+)\)\s*$",
                s,
            )
            if m:
                extra[m.group(1)] = CH5_PART_B
                continue
            m = re.match(
                r"^-\s\[[^\]]+\]\(" + re.escape(CH5_PART_C) + r"#([^)]+)\)\s*$",
                s,
            )
            if m:
                extra[m.group(1)] = CH5_PART_C

    if unified_heading in part_a and reader_marker in part_a:
        _, rest = part_a.split(unified_heading, 1)
        block, _ = rest.split(reader_marker, 1)
        ingest_block(block)
        return extra

    if semi_marker not in part_a or dep_marker not in part_a:
        return extra
    before_semi, semi_and_rest = part_a.split(semi_marker, 1)
    _, indep_section = before_semi.split(indep_marker, 1)
    semi_section, dep_and_rest = semi_and_rest.split(dep_marker, 1)
    dep_section, _ = dep_and_rest.split(reader_marker, 1)
    ingest_block(indep_section)
    ingest_block(semi_section)
    ingest_block(dep_section)

    return extra


def merged_anchor_home(part_a: str, part_b: str, part_c: str) -> dict[str, str]:
    """Explicit <a id> wins; directory fills gaps (historical heading-only targets)."""
    home: dict[str, str] = {}
    for a in collect_anchors(part_a):
        home[a] = CH5_PART_A
    for a in collect_anchors(part_b):
        home[a] = CH5_PART_B
    for a in collect_anchors(part_c):
        home[a] = CH5_PART_C
    for anchor, fil in directory_supplement_map(part_a).items():
        home.setdefault(anchor, fil)
    return home


def rewrite_fragments(body: str, current: str, anchor_home: dict[str, str]) -> str:
    def repl(m: re.Match[str]) -> str:
        anchor = m.group(1)
        dest = anchor_home.get(anchor)
        if dest is None or dest == current:
            return m.group(0)
        return f"]({dest}#{anchor})"

    return FRAG_LINK_RE.sub(repl, body)


def file_for_ch5_anchor(anchor: str, anchor_home: dict[str, str]) -> str:
    if anchor in anchor_home:
        return anchor_home[anchor]
    for suf in ("-e", "-c"):
        if anchor.endswith(suf) and len(anchor) > len(suf):
            base = anchor[: -len(suf)]
            if base in anchor_home:
                return anchor_home[base]
    return CH5_PART_A


def corpus_rewrite_file(path: Path, anchor_home: dict[str, str]) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text

    def repl(m: re.Match[str]) -> str:
        anchor = m.group(1)
        home = file_for_ch5_anchor(anchor, anchor_home)
        return f"{home}#{anchor}"

    text = CORPUS_CH5_RE.sub(repl, text)
    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    pa = (ROOT / CH5_PART_A).read_text(encoding="utf-8")
    pb = (ROOT / CH5_PART_B).read_text(encoding="utf-8")
    pc = (ROOT / CH5_PART_C).read_text(encoding="utf-8")
    home = merged_anchor_home(pa, pb, pc)

    (ROOT / CH5_PART_A).write_text(
        rewrite_fragments(pa, CH5_PART_A, home), encoding="utf-8"
    )
    (ROOT / CH5_PART_B).write_text(
        rewrite_fragments(pb, CH5_PART_B, home), encoding="utf-8"
    )
    (ROOT / CH5_PART_C).write_text(
        rewrite_fragments(pc, CH5_PART_C, home), encoding="utf-8"
    )

    skip_dirs = {"archive", ".git", "node_modules"}
    for p in ROOT.rglob("*"):
        if not p.is_file() or skip_dirs & set(p.parts):
            continue
        if p.suffix not in {".md", ".mdc", ".py"}:
            continue
        if p.name in {"split_ch5_apply.py", "ch5_reanchor_post_split.py", "ch5_paths.py"}:
            continue
        corpus_rewrite_file(p, home)

    print("Re-anchored; anchor_home size", len(home))


if __name__ == "__main__":
    main()
