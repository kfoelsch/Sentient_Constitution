#!/usr/bin/env python3
"""
Split Chapter Five into Independent / Semi-independent / Dependent clusters,
alphabetize, renumber §3. Run from repo root:
  python3 tools/rebuild_chapter_five.py
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "core_05-05_definitions_a_independent.md"
MAP_OUT = ROOT / "implementation" / "CHAPTER_FIVE_OLD_TO_NEW_MAP.md"


def parse_directory_classification(text: str) -> tuple[dict[str, str], dict[str, str]]:
    """Returns (anchor -> kind, title_lower -> anchor)."""
    m = re.search(
        r"#### Interdependent Definitions A-Z.*?\n\n(.*?)\n\n#### Clustered Definitions A-Z",
        text,
        re.DOTALL,
    )
    if not m:
        raise SystemExit("Directory block not found")
    result: dict[str, str] = {}
    title_to_anchor: dict[str, str] = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        mm = re.match(r"- \[([^\]]*)\]\(#([^)]+)\)(.*)", line)
        if not mm:
            continue
        title = mm.group(1).strip()
        anchor = mm.group(2)
        rest = mm.group(3)
        result[anchor] = "semi" if "cluster component" in rest else "independent"
        title_to_anchor[title.lower()] = anchor
    return result, title_to_anchor


def entry_title_from_block(block: str) -> str:
    for line in block.split("\n"):
        if line.startswith("#### "):
            return line[5:].strip()
    return ""


def primary_anchor_from_block(
    block: str, cls: dict[str, str], title_to_anchor: dict[str, str]
) -> str | None:
    title = entry_title_from_block(block)
    if title.lower() in title_to_anchor:
        return title_to_anchor[title.lower()]
    head = block.split("#####", 1)[0]
    ids = re.findall(r'<a id="([^"]+)"></a>', head)
    for i in ids:
        if i in cls:
            return i
    for i in ids:
        if not i.endswith(("-e", "-c")):
            return i
    return ids[0] if ids else None


def cluster_stable_anchor(block: str) -> str:
    mm = re.search(r'<a id="([^"]+-cluster[^"]*)"></a>', block)
    if mm:
        return mm.group(1)
    mm = re.search(r'<a id="([^"]+)"></a>', block)
    return mm.group(1) if mm else ""


def split_section1_entries(body: str) -> tuple[str, list[tuple[str, str]]]:
    parts = re.split(r"(?=^#### )", body, flags=re.MULTILINE)
    intro = parts[0].strip()
    entries = []
    for p in parts[1:]:
        if p.strip():
            entries.append((p.split("\n", 1)[0], p.rstrip()))
    return intro, entries


def split_section2_clusters(s2_body: str) -> tuple[str, list[tuple[str, str, str]]]:
    """s2_body = content after '### 2. Clustered Definitions\\n'. Returns (meta, clusters)."""
    cluster_pat = re.compile(r"^#### (2\.\d+[A-Z]?)\s+(.*)$", re.MULTILINE)
    matches = list(cluster_pat.finditer(s2_body))
    if not matches:
        raise SystemExit("No §2 numbered clusters")
    meta = s2_body[: matches[0].start()].strip()
    clusters = []
    for i, m in enumerate(matches):
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(s2_body)
        clusters.append((m.group(1), m.group(2).strip(), s2_body[start:end].rstrip()))
    return meta, clusters


def sort_key_title(title_line: str) -> str:
    return re.sub(r"^####\s+", "", title_line).strip().lower()


def renumber_cluster(block: str, new_num: str) -> str:
    return re.sub(
        r"^#### 2\.\d+[A-Z]?\s+",
        f"#### {new_num} ",
        block,
        count=1,
        flags=re.MULTILINE,
    )


def replace_directory(preamble: str, new_middle: str) -> str:
    pat = r"#### Interdependent Definitions A-Z\n\n.*?(?=\n</details>)"
    if not re.search(pat, preamble, flags=re.DOTALL):
        raise SystemExit("Could not find directory to replace in preamble")
    return re.sub(pat, new_middle.rstrip() + "\n", preamble, count=1, flags=re.DOTALL)


def global_post(s: str) -> str:
    s = re.sub(r"§2\.1\b", "§3.1", s)
    s = s.replace(
        "supporting Independent Definitions without importing",
        "supporting Independent Definitions without importing",
    )
    s = re.sub(
        r"\bsection 2 — Clustered Definitions\b",
        "section 3 — Dependent clusters",
        s,
    )
    s = re.sub(r"\bChapter Five §2\b(?!\.)", "Chapter Five §3", s)
    s = re.sub(r"\bClustered Definition\b", "Dependent-cluster definition", s)
    s = re.sub(r"\bClustered Definitions\b", "Dependent clusters", s)
    s = re.sub(r"\bInterdependent Definitions\b", "Independent Definitions", s)
    s = re.sub(r"\bInterdependent Definition\b", "Independent Definition", s)
    s = s.replace(
        "have their canonical O/E/C home, or an additional joint-satisfaction component, in Chapter Five §2.",
        "have their canonical O/E/C home, or an additional joint-satisfaction component, in Chapter Five §3.",
    )
    return s


def format_dep_directory(clusters_sorted: list[tuple[str, str, str]]) -> str:
    lines = []
    for _old, title, block in clusters_sorted:
        aid = cluster_stable_anchor(block)
        if aid:
            lines.append(f"- [{title}](#{aid})")
        else:
            lines.append(f"- {title}")
    return "\n".join(lines)


def format_s12_directory(
    entries: list[tuple[str, str]],
    cls: dict[str, str],
    title_to_anchor: dict[str, str],
) -> str:
    lines = []
    for title_line, block in entries:
        mm = re.match(r"^#### (.+)$", title_line)
        title = mm.group(1).strip() if mm else title_line
        aid = primary_anchor_from_block(block, cls, title_to_anchor)
        lines.append(f"- [{title}](#{aid})" if aid else f"- {title}")
    return "\n".join(lines)


def main() -> None:
    text = SOURCE.read_text(encoding="utf-8")
    cls, title_to_anchor = parse_directory_classification(text)

    i1 = text.index("### 1. Interdependent Definitions\n")
    i2 = text.index("### 2. Clustered Definitions\n")
    preamble = text[:i1]
    s1_raw = text[i1 + len("### 1. Interdependent Definitions\n") : i2]
    s2_all = text[i2 + len("### 2. Clustered Definitions\n") :]

    fi = s2_all.find("\n\n---\n\n*Corpus alignment:*")
    if fi == -1:
        footer = ""
        s2_body = s2_all
    else:
        footer = s2_all[fi:]
        s2_body = s2_all[:fi]

    intro_s1, entries = split_section1_entries(s1_raw)
    missing = []
    classified = []
    for tl, blk in entries:
        aid = primary_anchor_from_block(blk, cls, title_to_anchor)
        k = cls.get(aid) if aid else None
        if k is None:
            missing.append(f"{tl!r} anchor={aid!r}")
        classified.append((k or "independent", tl, blk))
    if missing:
        print("\n".join(missing))
        raise SystemExit(f"{len(missing)} unclassified §1 entries")

    indep = [(t, b) for k, t, b in classified if k == "independent"]
    semi = [(t, b) for k, t, b in classified if k == "semi"]
    indep.sort(key=lambda x: sort_key_title(x[0]))
    semi.sort(key=lambda x: sort_key_title(x[0]))

    meta, clusters = split_section2_clusters(s2_body)
    clusters_sorted = sorted(clusters, key=lambda x: x[1].lower())

    new_dir_middle = f"""Entries in **section 1** do not carry a `cluster component` pointer. Entries in **section 2** do; joint-satisfaction rules are in **section 3**.

#### Independent Definitions A-Z

{format_s12_directory(indep, cls, title_to_anchor)}

#### Semi-independent Definitions A-Z

{format_s12_directory(semi, cls, title_to_anchor)}

#### Dependent clusters A-Z

{format_dep_directory(clusters_sorted)}
"""
    preamble2 = replace_directory(preamble, new_dir_middle)

    intro_s1 = intro_s1.replace(
        "Interdependent Definitions are reusable",
        "Independent Definitions are reusable",
    )
    intro_s1 = intro_s1.replace(
        "any materially required Interdependent Definition",
        "any materially required Independent Definition",
    )
    intro_s1 = intro_s1.replace(
        "All Interdependent Definitions invoked",
        "All Independent Definitions invoked",
    )
    intro_s1 = intro_s1.replace(
        "each invoked Interdependent Definition",
        "each invoked Independent Definition",
    )
    intro_s1 = intro_s1.replace(
        "When an Interdependent Definition is invoked",
        "When an Independent Definition is invoked",
    )
    intro_s1 = intro_s1.replace(
        "Interdependent Definitions do not require joint satisfaction with other definitions unless a Clustered Definition explicitly requires it (**section 2** of this chapter).",
        "Independent and Semi-independent definitions do not require joint satisfaction with other definitions unless a Dependent-cluster definition explicitly requires it (**section 3** of this chapter).",
    )
    intro_s1 = intro_s1.replace(
        "applicable Interdependent Definitions (Chapter Five, section 1 — Interdependent Definitions).",
        "applicable Independent Definitions (Chapter Five, sections 1 and 2).",
    )
    intro_s1 = intro_s1.replace(
        "applicable Interdependent Definitions",
        "applicable Independent Definitions",
    )
    intro_s1 = intro_s1.replace(
        "Interdependent Definitions must not fragment",
        "Independent Definitions must not fragment",
    )
    intro_s1 += (
        "\n\n**Semi-independent Definitions** appear in **section 2**. They use the same O/E/C discipline as section 1, "
        "but the alphabetical directory marks a `cluster component` when **section 3** supplies joint-invocation context for materially in-scope matters.\n"
    )

    meta = re.sub(r"^#### 2\.1 ", "#### 3.1 ", meta, flags=re.MULTILINE)
    meta = re.sub(
        r"^#### 2\.2 Interdependent Definitions interaction and full context\s*$",
        "#### 3.2 Standalone definitions interaction and full context",
        meta,
        flags=re.MULTILINE,
    )
    meta = meta.replace(
        "Where a definition or definition component is designated as part of a Clustered Definition, it must not be invoked, satisfied, or evaluated independently of the cluster. Clustered definitions must be jointly satisfied where they describe components of a single functional requirement; partial satisfaction is not compliance.",
        "Where a definition or definition component is designated as part of a Dependent cluster, it must not be invoked, satisfied, or evaluated independently of the cluster. Dependent-cluster members must be jointly satisfied where they describe components of a single functional requirement; partial satisfaction is not compliance.",
    )
    meta = meta.replace(
        "Classification as an Interdependent Definition does not override or bypass cluster membership. Clustered Definitions must be satisfied jointly in full functional system context. No component may be isolated, reclassified, or applied independently in a manner that alters compliance determination.",
        "Classification as an Independent or Semi-independent definition does not override or bypass cluster membership. Dependent clusters must be satisfied jointly in full functional system context. No component may be isolated, reclassified, or applied independently in a manner that alters compliance determination.",
    )

    new_cluster_blocks = []
    map_rows = [
        "# Chapter Five: old §2 cluster label → new §3 label",
        "",
        "After alphabetical reorder, numeric labels changed. Prefer stable anchor links.",
        "",
        "| Old | New | Title | Anchor |",
        "|-----|-----|-------|--------|",
    ]
    n = 3
    for old_lbl, title, block in clusters_sorted:
        new_lbl = f"3.{n}"
        n += 1
        nb = renumber_cluster(block, new_lbl)
        new_cluster_blocks.append(nb)
        map_rows.append(
            f"| §{old_lbl} | §{new_lbl} | {title.replace('|', '\\|')[:70]} | `{cluster_stable_anchor(block)}` |"
        )

    section1 = (
        "### 1. Independent Definitions\n\n"
        + intro_s1
        + "\n\n"
        + "\n\n".join(b for _, b in indep)
    )
    section2 = (
        "### 2. Semi-independent Definitions\n\n"
        + "Each entry has a full O/E/C home here and may belong to a **Dependent cluster** in **section 3**. "
        "Where **section 3**’s admission scope applies, joint satisfaction rules there govern; otherwise apply sections 1–2 as ordinary standalone definitions.\n\n"
        + "\n\n".join(b for _, b in semi)
    )
    section3 = (
        "### 3. Dependent clusters (Clustered Definitions)\n\n"
        + "Joint invocation and satisfaction for definition sets that must be evaluated as a whole. "
        "Subsection numbers are editorial navigation aids; cluster **anchors** are the stable cross-reference targets.\n\n"
        + meta
        + "\n\n"
        + "\n\n".join(new_cluster_blocks)
    )

    out = preamble2 + section1 + "\n\n" + section2 + "\n\n" + section3 + footer
    out = global_post(out)

    MAP_OUT.parent.mkdir(parents=True, exist_ok=True)
    MAP_OUT.write_text("\n".join(map_rows) + "\n", encoding="utf-8")
    SOURCE.write_text(out, encoding="utf-8")
    print("Updated", SOURCE)
    print("Wrote", MAP_OUT)


if __name__ == "__main__":
    main()
