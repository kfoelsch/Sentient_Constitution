#!/usr/bin/env python3
"""Smooth Chapter One Part A numbering (decided 2026-10-01).

  Flourishing Aim: Introduction  -> §2   (now numbered)
  old §3 Non-Negotiable ...      -> §2.1 (shared Safety/Truth framing, moved ahead of Wellbeing)
  old §2 Wellbeing (+2.1-2.3)    -> §3   (+3.1-3.3)
  old §3.1 Safety                -> §4
  old §3.2 Truth                 -> §5   (old 3.3 -> 5.1, old 3.4(.x) -> 5.2(.x))
  old §4 Trust                   -> §6   old §5 Freedom -> §7
  Continuity Aim: Introduction   -> §8   (now numbered)
  old §§6-9                      -> §§9-12
  old §§10-12 (Part B)           -> §§13-15
  old §§13-17 (Part C)           -> §§16-20

Rewrites headings, explicit anchors, link targets and labels, title-glossed cites, "Chapter One §N" cites and raw
`core_01_x.md#frag` mentions. Part-level prose and mermaid chart text are hand-edited afterwards.
Dry run by default; use --write to apply.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from local_markdown_fragment_audit import github_slug  # noqa: E402

FA = "core_01_a_values_principles.md"
FB = "core_01_b_interaction_interpretation.md"
FC = "core_01_c_stewardship_capacity_principles.md"
CH1 = [FA, FB, FC]

TOP = {1: 1, 2: 3, 4: 6, 5: 7, 6: 9, 7: 10, 8: 11, 9: 12, 10: 13, 11: 14, 12: 15,
       13: 16, 14: 17, 15: 18, 16: 19, 17: 20}
SPECIAL = {"F": "2", "C": "8", "3": "2.1", "3.1": "4", "3.2": "5", "3.3": "5.1", "3.4": "5.2"}
NEW_HASHES = {"3": "####", "3.1": "###", "3.2": "###"}
MOVE_TO_A: set = set()
RETITLE: dict = {}
UNNUM = {"Flourishing Aim: Introduction": "F", "Continuity Aim: Introduction": "C"}
ALIAS = {  # id: (new id, file, old number, new number)
    "13-limits": ("16-limits", FC, "13", "16"),
    "13-pillar-2-proactive-stewardship": ("16-pillar-2-proactive-stewardship", FC, "13", "16"),
    "13-scope-priority-and-limits": ("16-scope-priority-and-limits", FC, "13", "16"),
    "143-role-scoped-observability": ("173-role-scoped-observability", FC, "14.3", "17.3"),
    "1015-rights-collision-decision-test": ("1315-rights-collision-decision-test", FB, "10.1.5", "13.1.5"),
}
# Live data/tool files that hard-code Chapter One anchors or heading text
# (dated cut lists and the older relocation scripts are historical record).
EXTRA_FILES = [
    "implementation/steward_owner_clock_index.json",
    "tools/steward_door_lockstep_audit.py",
    "tools/generate_reader_accessibility.py",
    "tools/architecture/ch1_dac_order.json",
]
SKIP_PREFIXES = (
    "archive/", "evidence/", "evaluation/results/", "doc_architecture/generated/",
    "ai_corpus/indexes/", "ai_corpus/visualization/", "translations/", "_pages_site/", ".git/",
    "implementation/CH1_",  # dated cut lists are historical record
)

HEAD = re.compile(r"^(#{3,6}) (\d+(?:\.\d+)*)(\.?) (.+?)\s*$")
UNNUM_HEAD = re.compile(r"^(###) (Flourishing Aim: Introduction|Continuity Aim: Introduction)\s*$")
ANCH_LINE = re.compile(r'^<a id="[^"]+"></a>\s*$')
ANCH = re.compile(r'<a id="([^"]+)"></a>')
LINK = re.compile(r'\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s]+)((?:\s+"[^"]*")?)\)')
RAW_REF = re.compile(r"(?P<path>(?:[\w./-]*/)?core_01_[abc]_\w+\.md)#(?P<frag>[\w-]+)")


def new_num(old: str) -> str:
    if old in SPECIAL:
        return SPECIAL[old]
    for k in ("3.4",):
        if old.startswith(k + "."):
            return SPECIAL[k] + old[len(k):]
    parts = old.split(".")
    return ".".join([str(TOP[int(parts[0])])] + parts[1:])


@dataclass
class Sec:
    file: str
    idx: int
    hashes: str
    old: str
    dot: str
    title: str
    new: str = ""
    new_hashes: str = ""
    new_title: str = ""
    old_slug: str = ""
    new_slug: str = ""
    new_file: str = ""

    def new_heading(self) -> str:
        nd = "." if "." not in self.new else ""
        return f"{self.new_hashes} {self.new}{nd} {self.new_title}"


def block_start(lines: list[str], heading_idx: int) -> int:
    j = heading_idx
    while j - 1 >= 0 and ANCH_LINE.match(lines[j - 1]):
        j -= 1
    return j


def collect(orig: dict[str, list[str]]):
    secs: list[Sec] = []
    for f in CH1:
        in_fence = False
        for i, line in enumerate(orig[f]):
            if line.startswith("```"):
                in_fence = not in_fence
            if in_fence:
                continue
            m = HEAD.match(line)
            u = UNNUM_HEAD.match(line)
            if u:
                s = Sec(f, i, u.group(1), UNNUM[u.group(2)], "", u.group(2))
                s.new = new_num(s.old)
                s.new_hashes = "###"
                s.new_title = s.title
                s.new_file = f
                s.old_slug = github_slug(s.title)
                s.new_slug = github_slug(f"{s.new}. {s.new_title}")
                secs.append(s)
                continue
            if not m:
                continue
            s = Sec(f, i, m.group(1), m.group(2), m.group(3), m.group(4))
            s.new = new_num(s.old)
            s.new_hashes = NEW_HASHES.get(s.old, s.hashes)
            top = int(s.old.split(".")[0])
            s.new_title = RETITLE.get(s.old, s.title)
            s.new_file = f
            s.old_slug = github_slug(f"{s.old}{s.dot} {s.title}")
            nd = "." if "." not in s.new else ""
            s.new_slug = github_slug(f"{s.new}{nd} {s.new_title}")
            secs.append(s)
    return secs


class Rewriter:
    def __init__(self, secs: list[Sec]):
        self.secs = secs
        self.slugmap = {s.old_slug: s for s in secs}
        by_num: dict[str, Sec] = {}
        for s in secs:
            by_num[s.old] = s
        self.by_num = by_num
        self.by_title = {(s.old, s.title.lower()): s for s in secs}
        # longest titles first so a short title never shadows a longer one
        self.changed = sorted((s for s in secs if s.old != s.new and s.old not in ("F", "C")), key=lambda s: -len(s.title))
        self.stats: dict[str, int] = {}
        self.review: list[dict] = []

    def bump(self, key: str):
        self.stats[key] = self.stats.get(key, 0) + 1

    # ---- links -------------------------------------------------------
    def relabel(self, label: str, old: str, new: str) -> str:
        if old == new or old in ("F", "C"):
            return label
        # The label may cite the section itself ("§6.1.5") or an ancestor of it ("§6.1");
        # either way the cited number moves with the section.
        for m in re.finditer(r"(?<![\w.])(\d+(?:\.\d+)*)(?![\w]|\.\d)", label):
            tok = m.group(1)
            before = label[: m.start()]
            if before.strip("*§ ") != "" and not before.rstrip().endswith("§"):
                return label  # number not in citation position
            if tok == old:
                repl = new
            elif old.startswith(tok + "."):
                repl = new_num(tok)
                if not (new.startswith(repl + ".") or new == repl):
                    self.review.append({"kind": "ancestor label no longer ancestor", "label": label[:100], "old": old, "new": new})
                    return label
            else:
                continue
            self.bump("label")
            return label[: m.start()] + repl + label[m.end():]
        return label

    def target_of(self, path: str, frag: str, orig_file: str | None):
        base = path.rsplit("/", 1)[-1] if path else ""
        if path:
            if base not in CH1:
                return None
            tfile = base
        else:
            if orig_file not in CH1:
                return None
            tfile = orig_file
        if frag in self.slugmap:
            s = self.slugmap[frag]
            return s.new_slug, s.new_file, s
        if frag in ALIAS:
            a = ALIAS[frag]
            return a[0], a[1], Sec(tfile, -1, "", a[2], "", "", new=a[3])
        return ("", tfile, None)

    def link(self, m: re.Match, orig_file: str | None, dest_file: str | None, lineno: int) -> str:
        label, target, title = m.group(1), m.group(2), m.group(3)
        if target.startswith("<") or "://" in target or target.startswith("mailto:"):
            return m.group(0)
        path, _, frag = target.partition("#")
        res = self.target_of(path, frag, orig_file)
        if res is None or not frag:
            return m.group(0)
        new_slug, new_file, sec = res
        if not new_slug:  # fragment not a mapped section anchor
            if not path and orig_file != dest_file and dest_file is not None:
                self.review.append({"kind": "frag-only link moved files", "file": dest_file, "line": lineno, "text": m.group(0)[:140]})
            return m.group(0)
        if dest_file is not None and new_file == dest_file:
            new_target = f"#{new_slug}"
        else:
            prefix = path.rsplit("/", 1)[0] + "/" if "/" in path else ""
            new_target = f"{prefix}{new_file}#{new_slug}"
        if sec is not None:
            label = self.relabel(label, sec.old, sec.new)
        if new_target != target:
            self.bump("link-target")
        return f"[{label}]({new_target}{title})"

    # ---- prose -------------------------------------------------------
    GLOSS = re.compile(r"(§§?\s?)(\d+(?:\.\d+)*)(\*\*)?(\s*\(\*)([^*)]+)(\*\))")
    CHAPTER = re.compile(r"(Chapter (?:One|1)\b(?:,? Part [ABC],?)?(?:\*\*)?\s+(?:\*\*)?§)(\d+(?:\.\d+)*)")

    def prose(self, seg: str) -> str:
        def gloss(m):
            sec = self.by_title.get((m.group(2), m.group(5).strip().lower()))
            if not sec or sec.old == sec.new:
                return m.group(0)
            self.bump("gloss-cite")
            return f"{m.group(1)}{sec.new}{m.group(3) or ''}{m.group(4)}{m.group(5)}{m.group(6)}"

        def chap(m):
            n = m.group(2)
            if n not in self.by_num:
                return m.group(0)
            nn = new_num(n)
            if nn != n:
                self.bump("chapter-cite")
            return m.group(1) + nn

        def raw(m):
            frag = m.group("frag")
            if frag in self.slugmap:
                s = self.slugmap[frag]
                path = m.group("path")
                prefix = path.rsplit("/", 1)[0] + "/" if "/" in path else ""
                self.bump("raw-ref")
                return f"{prefix}{s.new_file}#{s.new_slug}"
            if frag in ALIAS:
                path = m.group("path")
                prefix = path.rsplit("/", 1)[0] + "/" if "/" in path else ""
                return f"{prefix}{ALIAS[frag][1]}#{ALIAS[frag][0]}"
            return m.group(0)

        if "§" in seg:
            for sec in self.changed:
                pat = "§" + sec.old + " " + sec.title
                if pat in seg:
                    seg = re.sub(re.escape(pat) + r"(?![\w])", "§" + sec.new + " " + sec.title, seg)
                    self.bump("number-title-cite")
        seg = self.GLOSS.sub(gloss, seg)
        seg = self.CHAPTER.sub(chap, seg)
        seg = RAW_REF.sub(raw, seg)
        return seg

    def anchors(self, line: str) -> str:
        def a(m):
            aid = m.group(1)
            if aid in self.slugmap:
                self.bump("anchor")
                return f'<a id="{self.slugmap[aid].new_slug}"></a>'
            if aid in ALIAS:
                self.bump("anchor")
                return f'<a id="{ALIAS[aid][0]}"></a>'
            return m.group(0)
        return ANCH.sub(a, line)

    def line(self, line: str, orig_file: str | None, dest_file: str | None, lineno: int) -> str:
        if orig_file in CH1 and ANCH.search(line):
            line = self.anchors(line)
        out, pos = [], 0
        for m in LINK.finditer(line):
            out.append(self.prose(line[pos: m.start()]))
            out.append(self.link(m, orig_file, dest_file, lineno))
            pos = m.end()
        out.append(self.prose(line[pos:]))
        return "".join(out)


def tidy_block(block: list[str]) -> list[str]:
    while block and block[-1].strip() == "":
        block = block[:-1]
    return block + [""]


def run(root: Path, write: bool) -> int:
    global ROOT
    ROOT = root
    orig = {f: (root / f).read_text(encoding="utf-8").split("\n") for f in CH1}
    secs = collect(orig)
    rw = Rewriter(secs)

    h2, h3, h31 = rw.by_num["2"], rw.by_num["3"], rw.by_num["3.1"]
    a_lines = orig[FA]
    s2, s3, s31 = block_start(a_lines, h2.idx), block_start(a_lines, h3.idx), block_start(a_lines, h31.idx)
    assert s2 < s3 < s31

    head_by_line = {(s.file, s.idx): s for s in secs}
    new_lines: dict[str, list[str]] = {}
    for f in CH1:
        res = []
        for i, line in enumerate(orig[f]):
            h = head_by_line.get((f, i))
            if h is not None:
                res.append(h.new_heading())
                continue
            res.append(rw.line(line, f, f, i + 1))
        new_lines[f] = res

    A = new_lines[FA]
    newA = A[:s2] + tidy_block(A[s3:s31]) + A[s2:s3] + A[s31:]
    outputs = {FA: "\n".join(newA), FB: "\n".join(new_lines[FB]), FC: "\n".join(new_lines[FC])}

    # Other live files: links + prose cites only.
    changed_other = []
    for p in sorted(root.rglob("*.md")):
        rel = p.relative_to(root).as_posix()
        if rel in CH1 or rel.startswith(SKIP_PREFIXES):
            continue
        text = p.read_text(encoding="utf-8")
        if "core_01_" not in text and "Chapter One" not in text and "Chapter 1" not in text and "(*" not in text:
            continue
        new = "\n".join(rw.line(l, rel, None, i + 1) for i, l in enumerate(text.split("\n")))
        if new != text:
            outputs[rel] = new
            changed_other.append(rel)

    # Live data/tool files with hard-coded anchors or heading text.
    for rel in EXTRA_FILES:
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
                new = re.sub(r"(?<=[#\"'])" + re.escape(old_slug) + r"(?![\w-])", sec.new_slug, new)
        if new != text:
            outputs[rel] = new
            changed_other.append(rel)

    # Review: leftover unlinked section cites in the three Ch1 files.
    for f, txt in ((FA, outputs[FA]), (FB, outputs[FB]), (FC, outputs[FC])):
        for i, l in enumerate(txt.split("\n")):
            s = LINK.sub("", l)
            if re.search(r"§§?\s?\d", s):
                rw.review.append({"kind": "unlinked § cite", "file": f, "line": i + 1, "text": s.strip()[:150]})

    print("sections parsed:", len(secs))
    print("moved block (old §3 shared text):", s31 - s3, "lines ahead of old §2")
    print("stats:", json.dumps(rw.stats, sort_keys=True))
    print("other files changed:", len(changed_other))
    print("review items:", len(rw.review))
    report = {"stats": rw.stats, "files_changed": sorted(outputs), "review": rw.review,
              "slug_map": {s.old_slug: s.new_slug for s in secs if s.old_slug != s.new_slug},
              "file_moves": {s.old_slug: s.new_file for s in secs if s.new_file != s.file}}
    if write:
        ev = root / "evidence" / "2026-10-01"
        ev.mkdir(parents=True, exist_ok=True)
        (ev / "ch1_numbering_smoothing_report_2026-10-01.json").write_text(
            json.dumps(report, indent=1, ensure_ascii=False), encoding="utf-8")
        for rel, text in outputs.items():
            (root / rel).write_text(text, encoding="utf-8")
        print("written:", len(outputs), "files")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    sys.exit(run(Path(args.root).resolve(), args.write))
