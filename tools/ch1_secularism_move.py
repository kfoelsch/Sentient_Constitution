#!/usr/bin/env python3
"""Reorder Chapter One §7 and move Institutional Secularism into §18 (decided 2026-10-02).

  §7.2 Voluntary Discontinuation and Exit Rights  -> §7.4 (closes the Freedom section)
  §7.3 Assembly, Collective Organization, ...     -> §7.2   (7.3.x -> 7.2.x)
  §7.4 Dissent and Peaceful Protest               -> §7.3
  §7.5 Institutional Secularism and Worldview ... -> §18.2  (moves core_01_a -> core_01_c)
  §18.2 .. §18.5                                  -> §18.3 .. §18.6

Reuses the Rewriter from ch1_numbering_smoothing.py (headings, anchors, link targets and labels,
number-title cites, "Chapter One §N" cites, raw `core_01_x.md#frag` refs). Part-level prose and
mermaid chart text are hand-edited afterwards. Dry run by default; use --write to apply.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("sm", HERE / "ch1_numbering_smoothing.py")
sm = importlib.util.module_from_spec(spec)
sys.modules["sm"] = sm
spec.loader.exec_module(sm)

FA, FB, FC, CH1 = sm.FA, sm.FB, sm.FC, sm.CH1
MAP = {"7.2": "7.4", "7.3": "7.2", "7.4": "7.3", "7.5": "18.2",
       "18.2": "18.3", "18.3": "18.4", "18.4": "18.5", "18.5": "18.6"}
FILE_MOVE = {"7.5": FC}


def new_num(old: str) -> str:
    if old in MAP:
        return MAP[old]
    for k, v in MAP.items():
        if old.startswith(k + "."):
            return v + old[len(k):]
    return old


sm.new_num = new_num
sm.NEW_HASHES = {}
sm.ALIAS = {}
sm.UNNUM = {}
sm.RETITLE = {}


def run(root: Path, write: bool) -> int:
    orig = {f: (root / f).read_text(encoding="utf-8").split("\n") for f in CH1}
    secs = sm.collect(orig)
    for s in secs:
        s.new_file = FILE_MOVE.get(s.old, s.file) if s.file == FA or s.old in FILE_MOVE else s.file
    rw = sm.Rewriter(secs)
    by = rw.by_num
    A, C = orig[FA], orig[FC]
    bs = sm.block_start
    s71, s72, s73, s74, s75 = (bs(A, by[n].idx) for n in ("7.1", "7.2", "7.3", "7.4", "7.5"))
    s8 = bs(A, by["8"].idx)
    assert s71 < s72 < s73 < s74 < s75 < s8
    c182 = bs(C, by["18.2"].idx)

    head_by_line = {(s.file, s.idx): s for s in secs}
    new_lines: dict[str, list[str]] = {}
    for f in CH1:
        res = []
        for i, line in enumerate(orig[f]):
            h = head_by_line.get((f, i))
            if h is not None:
                res.append(h.new_heading())
                continue
            dest = FC if (f == FA and s75 <= i < s8) else f
            res.append(rw.line(line, f, dest, i + 1))
        new_lines[f] = res

    nA, nC = new_lines[FA], new_lines[FC]
    t = sm.tidy_block
    b71, b72, b73, b74, b75 = (t(nA[a:b]) for a, b in
                               ((s71, s72), (s72, s73), (s73, s74), (s74, s75), (s75, s8)))
    outA = nA[:s71] + b71 + b73 + b74 + b72 + nA[s8:]
    outC = nC[:c182] + b75 + nC[c182:]
    outputs = {FA: "\n".join(outA), FB: "\n".join(new_lines[FB]), FC: "\n".join(outC)}

    changed_other = []
    for p in sorted(root.rglob("*.md")):
        rel = p.relative_to(root).as_posix()
        if rel in CH1 or rel.startswith(sm.SKIP_PREFIXES):
            continue
        text = p.read_text(encoding="utf-8")
        if "core_01_" not in text and "Chapter One" not in text and "Chapter 1" not in text and "(*" not in text:
            continue
        new = "\n".join(rw.line(l, rel, None, i + 1) for i, l in enumerate(text.split("\n")))
        if new != text:
            outputs[rel] = new
            changed_other.append(rel)

    for rel in sm.EXTRA_FILES:
        p = root / rel
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        new = "\n".join(rw.prose(l) for l in text.split("\n"))
        for sec in secs:
            lit = f'"{sec.hashes} {sec.old}{sec.dot} {sec.title}"'
            if lit in new and sec.old != sec.new:
                new = new.replace(lit, f'"{sec.new_heading()}"')
                rw.bump("heading-literal")
        for old_slug, sec in rw.slugmap.items():
            if sec.old_slug != sec.new_slug:
                import re
                new = re.sub(r"(?<=[#\"'])" + re.escape(old_slug) + r"(?![\w-])", sec.new_slug, new)
        if new != text:
            outputs[rel] = new
            changed_other.append(rel)

    print("stats:", json.dumps(rw.stats, sort_keys=True))
    print("files changed:", len(outputs), "| review items:", len(rw.review))
    for r in rw.review:
        if r.get("kind") != "unlinked § cite":
            print("  REVIEW", json.dumps(r, ensure_ascii=False)[:240])
    report = {"stats": rw.stats, "files_changed": sorted(outputs), "review": rw.review,
              "slug_map": {s.old_slug: s.new_slug for s in secs if s.old_slug != s.new_slug}}
    if write:
        ev = root / "evidence" / "2026-10-02"
        ev.mkdir(parents=True, exist_ok=True)
        (ev / "ch1_secularism_move_report_2026-10-02.json").write_text(
            json.dumps(report, indent=1, ensure_ascii=False), encoding="utf-8")
        for rel, text in outputs.items():
            (root / rel).write_text(text, encoding="utf-8")
        print("written:", len(outputs), "files")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(HERE.parent))
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    sys.exit(run(Path(a.root).resolve(), a.write))
