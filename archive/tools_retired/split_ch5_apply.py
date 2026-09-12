#!/usr/bin/env python3
"""Split core_05-05_definitions_a_independent.md into Part A/B/C; fix directory and links.

**Layout note:** this script expects the legacy directory split (independent /
semi-independent / dependent blocks between markers). After the **unified**
`#### All definitions and clusters (A–Z)` directory (see current Part A), run it
only on snapshots that still match the old structure, or update
`rewrite_directory_lists` accordingly.

Run from repo root: python3 tools/split_ch5_apply.py
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
SOURCE = ROOT / CH5_PART_A

ANCHOR_RE = re.compile(r'<a id="([^"]+)"></a>')
FRAG_LINK_RE = re.compile(r"\]\(#([^)]+)\)")

# Stable section anchors (explicit; do not rely on heading slug generators)
CH5_S2_ANCHOR = "section-2-semi-independent-definitions"
CH5_S3_ANCHOR = "section-3-dependent-clusters-clustered-definitions"


def collect_anchors(text: str) -> set[str]:
    return set(ANCHOR_RE.findall(text))


def rewrite_directory_lists(part_a: str) -> str:
    """Prefix semi-independent and dependent directory bullets with Part B / Part C paths."""
    semi_marker = '<a id="semi-independent-definitions-a-z"></a>'
    dep_marker = '<a id="dependent-clusters-a-z"></a>'
    directory_end_marker = "\n</details>"

    if semi_marker not in part_a or dep_marker not in part_a:
        raise SystemExit("directory markers not found in Part A")

    head, mid = part_a.split(semi_marker, 1)
    semi_block, tail = mid.split(dep_marker, 1)

    def prefix_bullets(block: str, fname: str) -> str:
        out_lines = []
        for line in block.splitlines():
            stripped = line.strip()
            m = re.match(r"^(- \[[^\]]+\])\(#([^)]+)\)$", stripped)
            if m:
                prefix, anchor = m.group(1), m.group(2)
                out_lines.append(f"{prefix}({fname}#{anchor})")
            else:
                out_lines.append(line)
        return "\n".join(out_lines)

    semi_fixed = prefix_bullets(semi_block, CH5_PART_B)
    if directory_end_marker in tail:
        dep_section, rest = tail.split(directory_end_marker, 1)
        dep_fixed = prefix_bullets(dep_section, CH5_PART_C)
        tail = dep_fixed + directory_end_marker + rest
    else:
        tail = prefix_bullets(tail, CH5_PART_C)

    return head + semi_marker + semi_fixed + dep_marker + tail


def rewrite_fragments(body: str, current: str, anchor_home: dict[str, str]) -> str:
    """Turn fragment-only links into file-qualified when target lives in another part."""

    def repl(m: re.Match[str]) -> str:
        anchor = m.group(1)
        home = anchor_home.get(anchor)
        if home is None or home == current:
            return m.group(0)
        return f"]({home}#{anchor})"

    return FRAG_LINK_RE.sub(repl, body)


def part_b_header() -> str:
    return f"""# Sentient Constitution — Constitutional definitions (Part B)

This file is **part of the Sentient Constitution** and is **binding only together** with the other numbered `core_*` files read as one instrument. It contains **Chapter Five, Part B** — Semi-independent Definitions; chapter numbering and cross-references match the integrated instrument. Reading order, the binding/support split, and corpus edition metadata are maintained in [README.md](README.md).

Upstream constitutional direction for this file's definitions begins in [core_00_preamble.md](core_00_preamble.md), [core_01_a_values_principles.md](core_01_a_values_principles.md), and [core_01_b_stewardship_capacity_principles.md](core_01_b_stewardship_capacity_principles.md), the definition-mechanics pipeline in [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md), and **Chapter Five, Part A** (Independent Definitions and the alphabetical directory) in [{CH5_PART_A}]({CH5_PART_A}#chapter-five-foundational-definitions). **Chapter Five, Part C** (Dependent clusters) continues in [{CH5_PART_C}]({CH5_PART_C}#{CH5_S3_ANCHOR}).

---

"""


def part_c_header() -> str:
    return f"""# Sentient Constitution — Constitutional definitions (Part C)

This file is **part of the Sentient Constitution** and is **binding only together** with the other numbered `core_*` files read as one instrument. It contains **Chapter Five, Part C** — Dependent clusters (Clustered Definitions); chapter numbering and cross-references match the integrated instrument. Reading order, the binding/support split, and corpus edition metadata are maintained in [README.md](README.md).

Upstream constitutional direction for this file's definitions begins in [core_00_preamble.md](core_00_preamble.md), [core_01_a_values_principles.md](core_01_a_values_principles.md), and [core_01_b_stewardship_capacity_principles.md](core_01_b_stewardship_capacity_principles.md), the definition-mechanics pipeline in [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md), **Chapter Five, Part A** in [{CH5_PART_A}]({CH5_PART_A}#chapter-five-foundational-definitions), and **Chapter Five, Part B** in [{CH5_PART_B}]({CH5_PART_B}#{CH5_S2_ANCHOR}).

---

"""


def part_a_intro_replace(part_a_head: str) -> str:
    old = """This file is **part of the Sentient Constitution** and is **binding only together** with the other numbered `core_*` files read as one instrument. It contains **Chapter Five**; chapter numbering and cross-references match the integrated instrument. Reading order, the binding/support split, and corpus edition metadata are maintained in [README.md](README.md).

Upstream constitutional direction for this file's definitions begins in [core_00_preamble.md](core_00_preamble.md), [core_01_a_values_principles.md](core_01_a_values_principles.md), and [core_01_b_stewardship_capacity_principles.md](core_01_b_stewardship_capacity_principles.md) and the definition-mechanics pipeline in [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md)."""
    new = f"""This file is **part of the Sentient Constitution** and is **binding only together** with the other numbered `core_*` files read as one instrument. It contains **Chapter Five, Part A** — reader guidance, the canonical-home rule, the alphabetical directory, and **section 1 — Independent Definitions**; **Part B** (Semi-independent Definitions) is in [{CH5_PART_B}]({CH5_PART_B}#{CH5_S2_ANCHOR}); **Part C** (Dependent clusters) is in [{CH5_PART_C}]({CH5_PART_C}#{CH5_S3_ANCHOR}). Read **Chapter Five** as the three parts together. Chapter numbering and cross-references match the integrated instrument. Reading order, the binding/support split, and corpus edition metadata are maintained in [README.md](README.md).

Upstream constitutional direction for this file's definitions begins in [core_00_preamble.md](core_00_preamble.md), [core_01_a_values_principles.md](core_01_a_values_principles.md), and [core_01_b_stewardship_capacity_principles.md](core_01_b_stewardship_capacity_principles.md) and the definition-mechanics pipeline in [core_02-04_definition_mechanics.md](core_02-04_definition_mechanics.md)."""
    if old not in part_a_head:
        raise SystemExit("Part A intro paragraph not found (already migrated?)")
    return part_a_head.replace(old, new, 1)


def fix_part_b_directory_prose(body: str) -> str:
    return body.replace(
        "The alphabetical directory above still lists every semi-independent term in A–Z order.",
        f"The alphabetical directory in [{CH5_PART_A}]({CH5_PART_A}#chapter-five-foundational-definitions) still lists every semi-independent term in A–Z order.",
        1,
    )


def corpus_rewrite_file(path: Path, anchor_home: dict[str, str]) -> bool:
    text = path.read_text(encoding="utf-8")
    orig = text
    pattern = re.compile(re.escape(CH5_PART_A) + r"#([A-Za-z0-9_\-]+)")

    def repl(m: re.Match[str]) -> str:
        anchor = m.group(1)
        home = anchor_home.get(anchor, CH5_PART_A)
        return f"{home}#{anchor}"

    text = pattern.sub(repl, text)
    if text != orig:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    raw = SOURCE.read_text(encoding="utf-8")
    sep2 = "\n### 2. Semi-independent Definitions\n"
    sep3 = "\n### 3. Dependent clusters (Clustered Definitions)\n"
    if sep2 not in raw or sep3 not in raw:
        raise SystemExit("section separators not found")

    chunk_a, rest = raw.split(sep2, 1)
    chunk_b_mid, chunk_c_mid = rest.split(sep3, 1)

    chunk_b = (
        f'<a id="{CH5_S2_ANCHOR}"></a>\n\n### 2. Semi-independent Definitions\n' + chunk_b_mid
    )
    chunk_c = (
        f'<a id="{CH5_S3_ANCHOR}"></a>\n\n### 3. Dependent clusters (Clustered Definitions)\n'
        + chunk_c_mid
    )

    anchors_a = collect_anchors(chunk_a)
    anchors_b = collect_anchors(chunk_b)
    anchors_c = collect_anchors(chunk_c)
    overlap = (anchors_a & anchors_b) | (anchors_b & anchors_c) | (anchors_a & anchors_c)
    if overlap:
        raise SystemExit(f"duplicate anchors across parts: {sorted(overlap)[:30]}")

    anchor_home: dict[str, str] = {}
    for a in anchors_a:
        anchor_home[a] = CH5_PART_A
    for a in anchors_b:
        anchor_home[a] = CH5_PART_B
    for a in anchors_c:
        anchor_home[a] = CH5_PART_C

    chunk_a = part_a_intro_replace(chunk_a)
    chunk_a = rewrite_directory_lists(chunk_a)
    chunk_a = rewrite_fragments(chunk_a, CH5_PART_A, anchor_home)

    chunk_b = part_b_header() + fix_part_b_directory_prose(chunk_b)
    chunk_b = rewrite_fragments(chunk_b, CH5_PART_B, anchor_home)

    chunk_c = part_c_header() + chunk_c
    chunk_c = rewrite_fragments(chunk_c, CH5_PART_C, anchor_home)

    SOURCE.write_text(chunk_a, encoding="utf-8")
    (ROOT / CH5_PART_B).write_text(chunk_b, encoding="utf-8")
    (ROOT / CH5_PART_C).write_text(chunk_c, encoding="utf-8")

    skip_dirs = {"archive", ".git", "node_modules"}
    scan_suffixes = {".md", ".mdc", ".py"}
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        if set(p.parts) & skip_dirs:
            continue
        if p.suffix not in scan_suffixes:
            continue
        if p.name in {"split_ch5_apply.py", "ch5_paths.py"}:
            continue
        corpus_rewrite_file(p, anchor_home)

    print("Wrote", CH5_PART_A, CH5_PART_B, CH5_PART_C)
    print("Anchors:", len(anchor_home))


if __name__ == "__main__":
    main()
