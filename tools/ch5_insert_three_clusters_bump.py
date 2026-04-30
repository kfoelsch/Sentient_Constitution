#!/usr/bin/env python3
"""One-off: bump Chapter Five §3 citations for three cluster insertions (2026-04-29 batch).

Mapping for old cluster index k (18 <= k <= 39):
  fk = k + 1 + (1 if k >= 20 else 0) + (1 if k >= 21 else 0)

Inserts (final numbering): §3.18 Family… §3.21 Indigenous… §3.23 Materiality…
Run from repo root: python3 tools/ch5_insert_three_clusters_bump.py
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

FILES = [
    "core_00-01_principles.md",
    "core_02-04_definition_mechanics.md",
    "core_05-05_definitions_a_independent.md",
    "core_05-05_definitions_b_semi_independent.md",
    "core_05-05_definitions_c_dependent_clusters.md",
    "core_06-06_standing_classification.md",
    "core_06-06_standing_integration.md",
    "core_07-07_misconduct.md",
    "core_08-08_forum.md",
    "core_09-09_rights_part_a.md",
    "core_09-09_rights_part_b.md",
    "core_09-09_rights_part_c.md",
    "core_09-09_rights_part_d.md",
    "core_10-10_governance.md",
    "core_11-13_amendment.md",
    "core_14-14_incorporation.md",
    "corpus_systems.md",
    "corpus_institutions.md",
    "corpus_forum.md",
    "corpus_joint_structure.md",
    "doc_architecture.md",
    "implementation/TRANSITION_FRAMEWORK_2026.md",
]


def fk(k: int) -> int:
    if k < 18 or k > 39:
        return k
    return k + 1 + (1 if k >= 20 else 0) + (1 if k >= 21 else 0)


def sub_heading_line(line: str) -> str | None:
    m = re.match(r"^(#### )3\.(\d+)\s", line)
    if not m:
        return None
    k = int(m.group(2))
    if k < 18 or k > 39:
        return None
    return re.sub(r"^(#### )3\.\d+\s", f"#### 3.{fk(k)} ", line)


def sub_text(text: str) -> str:
    # #### 3.N (headings) — skip; handled in line walker for Part C file, or here globally:
    out = text
    for k in range(39, 17, -1):
        nk = fk(k)
        if nk == k:
            continue
        # §3.k word boundary (avoid §3.3 matching §3.39 — match longest first by descending k)
        out = re.sub(rf"§3\.{k}\b", f"§3.{nk}", out)
        out = re.sub(rf"section 3\.{k}\b", f"section 3.{nk}", out, flags=re.IGNORECASE)
        out = re.sub(rf"Section 3\.{k}\b", f"Section 3.{nk}", out)
        out = re.sub(rf"\*\*3\.{k}\*\*", f"**3.{nk}**", out)
    return out


def process_file(path: pathlib.Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    if path.name == "core_05-05_definitions_c_dependent_clusters.md":
        lines = raw.splitlines(keepends=True)
        out_lines: list[str] = []
        for line in lines:
            nl = sub_heading_line(line)
            out_lines.append(nl if nl is not None else line)
        raw2 = "".join(out_lines)
        raw3 = sub_text(raw2)
    else:
        raw3 = sub_text(raw)
    if raw3 != raw:
        path.write_text(raw3, encoding="utf-8")
        return True
    return False


def main() -> None:
    changed: list[str] = []
    for rel in FILES:
        p = ROOT / rel
        if not p.is_file():
            print(f"skip (missing): {rel}", file=sys.stderr)
            continue
        if process_file(p):
            changed.append(rel)
    print("Updated:", *changed, sep="\n  ")


if __name__ == "__main__":
    main()
