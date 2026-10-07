#!/usr/bin/env python3
"""Chapter Eight process-order reorder (CH8-PROCESS-ORDER-01).

Reorders Chapter Eight so section order follows the certification process:

  Phase I   Frame               §1 Purpose and Role, §2 System Class Evaluation,
                                §3 Challenging a Certification  (was Part B §5.3 + §5.3.1)
  Phase II  Evaluate            §4 Whole-System Certification Evaluation  (was §3)
  Phase III Review              §5 Forum Process                          (§5.3.2/§5.3.3 -> §5.3/§5.4)
  Phase IV  Record              §6 System Certification Record            (was §4)
  Phase V   Decide, keep current §7 Outcomes, Recertification, and Reopening (was §6),
                                §8 Relationship to Standing                (was §7)

Inside the evaluation section the subsections are grouped by when they apply:
always (4.1-4.4), when implicated (4.5-4.7), when triggered (4.8).

What the script does, in order:
  1. Expand same-file fragment links in Parts A-C to explicit file links.
  2. Rewrite every link to a Chapter Eight anchor (file and fragment), the section number
     and (where retitled) the title in the link text, and bare section-number cites.
  3. Recompose Parts A and B (move blocks, renumber headings, rename anchors).
  4. Normalise explicit same-file links back to bare fragments.

It changes no operative wording; only labels, order, and link targets move.
Use --dry-run to print the report without writing.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

A = "core_08_a_system_alignment_certification_evaluation.md"
B = "core_08_b_system_alignment_certification_record_process.md"
C = "core_08_c_system_alignment_certification_illustrations.md"
HUB = "core_08_system_alignment_certification.md"
CH8 = {A, B, C}

# ---------------------------------------------------------------- number map
NUM: dict[str, str] = {
    # Part A (old) -> Part A (new)
    "1": "1", "1.1": "1.1", "1.2": "1.2", "2": "2", "2.1": "2.1",
    "3": "4",
    "3.1": "4.1",
    "3.5": "4.2",
    "3.6": "4.3",
    "3.7": "4.4",
    "3.2": "4.5",
    "3.3": "4.6",
    "3.4": "4.7",
    "3.4.1": "4.7.1",
    "3.8": "4.8",
    # Part B (old) -> new
    "4": "6", "4.1": "6.1", "4.2": "6.2",
    "5": "5", "5.1": "5.1", "5.2": "5.2",
    "5.3": "3",          # moves to Part A
    "5.3.1": "3.1",      # moves to Part A
    "5.3.2": "5.3",
    "5.3.3": "5.4",
    "6": "7", "6.1": "7.1", "6.2": "7.2", "6.2.1": "7.2.1", "6.3": "7.3",
    "7": "8",
    # Part C (old) -> new
    "3.7.1": "4.4.1",
}
for k in range(1, 7):
    NUM[f"3.8.{k}"] = f"4.8.{k}"
    NUM[f"3.8.{k}.1"] = f"4.8.{k}.1"

# Retitled headings (old number -> new title). Everything else keeps its title.
RETITLE = {
    "5.3": "Challenging a Certification",  # was "Challenging a certification" at ####
}

# Heading level change for moved blocks (old number -> new level, number of #).
RELEVEL = {
    "5.3": 3,
    "5.3.1": 4,
    "5.3.2": 4,
    "5.3.3": 4,
}

HISTORICAL_PREFIXES = (
    "archive/",
    "evidence/",
    "evaluation/results/",
    "evaluation/external_audit_2026-08/",
    "evaluation/two_party/results/",
    "doc_architecture/generated/",
    "ai_corpus/",
    "_pages_site/",
    "tools/ch8_",
    "tools/__pycache__/",
)

FOREIGN_BEFORE = re.compile(
    r"(Chapter\s+(?:One|Two|Three|Four|Five|Six|Seven|Nine|Ten|Eleven|Twelve|Thirteen|Fourteen|Fifteen|Sixteen|Seventeen|\d+)"
    r"|Preamble|CS-\d+[A-Za-z]?|CJS-\d+[A-Za-z]?|CI-\d+[A-Za-z]?|CF-\d+[A-Za-z]?|CH?-\d+|Article\s+[IVXLC]+(?:-[A-Z])?|Def\.\w+)"
    r"[^§\n]{0,40}$"
)


def slugify(text: str) -> str:
    t = text.lower()
    t = re.sub(r"[^\w\s-]", "", t)
    t = re.sub(r"\s", "-", t)
    return t


HEADING_RE = re.compile(r"^(#{1,6}) (\d+(?:\.\d+)*)\.? (.+?)\s*$")
ANCHOR_RE = re.compile(r'^<a id="([^"]+)"></a>\s*$')


def parse_headings(text: str):
    """Return list of dicts for numbered headings with their anchors."""
    lines = text.split("\n")
    out = []
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line)
        if not m:
            continue
        hashes, num, title = m.groups()
        j = i - 1
        anchors = []
        while j >= 0 and (lines[j].strip() == "" or ANCHOR_RE.match(lines[j])):
            am = ANCHOR_RE.match(lines[j])
            if am:
                anchors.append(am.group(1))
            j -= 1
        start = j + 1
        while start < i and lines[start].strip() == "":
            start += 1
        out.append(
            {"line": i, "start": start, "level": len(hashes), "num": num, "title": title, "anchors": anchors[::-1]}
        )
    return out


def build_anchor_map(files: dict[str, str]):
    """(basename, old_anchor) -> (new_basename, new_anchor, old_num, new_num, old_title, new_title)."""
    amap = {}
    for base, text in files.items():
        for h in parse_headings(text):
            old = h["num"]
            if old not in NUM:
                raise SystemExit(f"{base}: heading {old} {h['title']} has no mapping")
            new = NUM[old]
            title = RETITLE.get(old, h["title"])
            if old in ("5.3", "5.3.1", "5.3.2", "5.3.3"):
                new_base = A if old in ("5.3", "5.3.1") else B
            else:
                new_base = base
            # the heading's own anchor is the slug of "<num> <title>"
            old_slug = slugify(f"{old} {h['title']}")
            if old_slug not in h["anchors"]:
                raise SystemExit(f"{base}: expected anchor {old_slug} for {old}; has {h['anchors']}")
            new_slug = slugify(f"{new} {title}")
            for a in h["anchors"]:
                if a == old_slug:
                    amap[(base, a)] = (new_base, new_slug, old, new, h["title"], title)
                # other (legacy) anchors on numbered headings are not expected
    return amap


LINK_RE = re.compile(r"\[((?:[^\[\]]|\[[^\]]*\])*)\]\(([^)\s]+)\)")
SEC_TOKEN = re.compile(r"§(\d+(?:\.\d+)*)")


def split_target(target: str):
    if "#" in target:
        path, frag = target.split("#", 1)
        return path, frag
    return target, ""


class Remapper:
    def __init__(self, amap):
        self.amap = amap
        self.report = {"links": 0, "text_nums": 0, "titles": 0, "unresolved": [], "bare": [], "ranges": []}

    # -- links ---------------------------------------------------------------
    def rewrite_links(self, text: str, relpath: str) -> str:
        fdir = Path(relpath).parent

        def repl(m: re.Match) -> str:
            label, target = m.group(1), m.group(2)
            path, frag = split_target(target)
            if not frag:
                return m.group(0)
            base = Path(path).name if path else Path(relpath).name
            if base not in CH8:
                return m.group(0)
            key = (base, frag)
            if key not in self.amap:
                # unnumbered anchors (chapter, class profiles ...) stay put
                return m.group(0)
            nb, nfrag, onum, nnum, otitle, ntitle = self.amap[key]
            new_label = label
            # number in link text
            def tok(mm):
                if mm.group(1) == onum:
                    self.report["text_nums"] += 1
                    return "§" + nnum
                return mm.group(0)

            new_label = SEC_TOKEN.sub(tok, new_label)
            if otitle != ntitle and otitle.lower() in new_label.lower():
                new_label = re.sub(re.escape(otitle), ntitle, new_label, flags=re.I)
                self.report["titles"] += 1
            # leftover section tokens that do not match the target's number are suspicious
            for mm in SEC_TOKEN.finditer(new_label):
                if mm.group(1) != nnum and mm.group(1) in NUM and "through" not in new_label and "–" not in new_label:
                    # e.g. a link whose text cites a different section than its target
                    self.report["ranges"].append((relpath, label, target))
            # target
            if path:
                new_path = str(Path(path).parent / nb) if str(Path(path).parent) != "." else nb
                if path.startswith("./"):
                    new_path = "./" + new_path
            else:
                new_path = ""
            self.report["links"] += 1
            return f"[{new_label}]({new_path}#{nfrag})"

        return LINK_RE.sub(repl, text)

    # -- bare cites -----------------------------------------------------------
    def rewrite_bare(self, text: str, relpath: str, in_ch8: bool) -> str:
        """Rewrite §-tokens that are not inside a markdown link."""
        out = []
        pos = 0
        for lm in LINK_RE.finditer(text):
            out.append(self._bare_segment(text[pos:lm.start()], text, pos, relpath, in_ch8))
            out.append(lm.group(0))
            pos = lm.end()
        out.append(self._bare_segment(text[pos:], text, pos, relpath, in_ch8))
        return "".join(out)

    def _bare_segment(self, seg: str, full: str, offset: int, relpath: str, in_ch8: bool) -> str:
        def repl(m: re.Match) -> str:
            num = m.group(1)
            before = full[max(0, offset + m.start() - 70): offset + m.start()]
            line_start = before.rfind("\n")
            before_line = before[line_start + 1:]
            marker_ch8 = re.search(r"(Chapter Eight|Ch\.? ?8)[^§\n]{0,25}$", before_line) or re.search(
                r"Part [ABC](?:,|\s)\s*$", before_line
            )
            foreign = FOREIGN_BEFORE.search(before_line)
            part_foreign = re.search(r"(CS-\d+|CJS-\d+|CI-\d+|CF-\d+)[^§\n]{0,12}Part [ABC]\s*$", before_line)
            if part_foreign:
                foreign = part_foreign
            if marker_ch8 and not part_foreign:
                decision = "ch8"
            elif in_ch8 and not foreign:
                decision = "ch8?"  # unmarked inside Chapter Eight: assume ours, list for review
            else:
                decision = "skip"
            ctx = (before_line + m.group(0) + full[offset + m.end(): offset + m.end() + 40]).replace("\n", " ")
            if decision != "skip":
                self.report["bare"].append((relpath, decision, num, ctx))
            if decision in ("ch8", "ch8?") and num in NUM:
                self.report["text_nums"] += 1
                return "§" + NUM[num]
            return m.group(0)

        return SEC_TOKEN.sub(repl, seg)


def git_files() -> list[str]:
    out = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).decode()
    return [p for p in out.split("\0") if p]


def processable(relpath: str) -> bool:
    if relpath.startswith(HISTORICAL_PREFIXES):
        return False
    return relpath.endswith((".md", ".json", ".csv", ".py", ".yml", ".yaml", ".txt"))


# ------------------------------------------------------------------ recompose
def split_blocks(text: str):
    """Split a part file into (prefix, blocks, tail) by numbered headings."""
    heads = parse_headings(text)
    lines = text.split("\n")
    starts = [h["start"] for h in heads]
    prefix = "\n".join(lines[: starts[0]])
    blocks = {}
    for idx, h in enumerate(heads):
        end = starts[idx + 1] if idx + 1 < len(heads) else len(lines)
        blocks[h["num"]] = {"head": h, "text": "\n".join(lines[h["start"]:end])}
    return prefix, heads, blocks


def renumber_block(block: dict, old: str) -> str:
    """Rewrite the heading line and its anchors for a block under the NUM map."""
    h = block["head"]
    new = NUM[old]
    title = RETITLE.get(old, h["title"])
    level = RELEVEL.get(old, h["level"])
    old_slug = slugify(f"{old} {h['title']}")
    new_slug = slugify(f"{new} {title}")
    text = block["text"]
    text = text.replace(f'<a id="{old_slug}"></a>', f'<a id="{new_slug}"></a>', 1)
    old_head = f"{'#' * h['level']} {old}. {h['title']}" if f"{'#' * h['level']} {old}. " in text else f"{'#' * h['level']} {old} {h['title']}"
    sep = "." if f"{'#' * h['level']} {old}. " in text else ""
    new_head = f"{'#' * level} {new}{sep} {title}"
    if old_head not in text:
        raise SystemExit(f"cannot find heading '{old_head}'")
    text = text.replace(old_head, new_head, 1)
    return text


def trim(s: str) -> str:
    return s.strip("\n") + "\n"


def compose(a_text: str, b_text: str):
    a_prefix, a_heads, a_blocks = split_blocks(a_text)
    b_prefix, b_heads, b_blocks = split_blocks(b_text)

    # Part A tail (after 3.8.6) is the "Continue to ..." footer; detach it.
    last = a_blocks["3.8.6"]["text"]
    cut = last.find("\n<br>\n\n*Continue to record")
    if cut == -1:
        raise SystemExit("cannot find Part A tail")
    a_tail = last[cut:]
    a_blocks["3.8.6"]["text"] = last[:cut]

    # Part B tail (closing note and footer) follows the last paragraph of §7.
    last_b = b_blocks["7"]["text"]
    cut_b = last_b.find("\n*Closing note:*")
    if cut_b == -1:
        raise SystemExit("cannot find Part B closing note")
    b_tail = last_b[cut_b:]
    b_blocks["7"]["text"] = last_b[:cut_b]

    def rb(blocks, old):
        return renumber_block(blocks[old], old)

    a_order = ["1", "1.1", "1.2", "2", "2.1"]
    a_parts = [a_prefix.rstrip("\n") + "\n"]
    for n in a_order:
        a_parts.append(rb(a_blocks, n))
    # new §3 (from Part B §5.3 and §5.3.1)
    a_parts.append(rb(b_blocks, "5.3"))
    a_parts.append(rb(b_blocks, "5.3.1"))
    for n in ["3", "3.1", "3.5", "3.6", "3.7", "3.2", "3.3", "3.4", "3.4.1", "3.8",
              "3.8.1", "3.8.2", "3.8.3", "3.8.4", "3.8.5", "3.8.6"]:
        a_parts.append(rb(a_blocks, n))

    b_parts = [b_prefix.rstrip("\n") + "\n"]
    for n in ["5", "5.1", "5.2", "5.3.2", "5.3.3", "4", "4.1", "4.2", "6", "6.1", "6.2", "6.2.1", "6.3", "7"]:
        b_parts.append(rb(b_blocks, n))

    new_a = "\n".join(trim(p) if i else p for i, p in enumerate(a_parts)) + a_tail
    new_b = "\n".join(trim(p) if i else p for i, p in enumerate(b_parts)) + b_tail

    # Part C: renumber headings only
    return new_a, new_b


def recompose_c(c_text: str) -> str:
    prefix, heads, blocks = split_blocks(c_text)
    for old, blk in blocks.items():
        c_text = c_text.replace(blk["text"], renumber_block(blk, old), 1)
    return c_text


# ---------------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", type=Path, help="write the bare-cite report here")
    ap.add_argument("--skip-compose", action="store_true", help="only remap references")
    args = ap.parse_args()

    old = {n: (ROOT / n).read_text(encoding="utf-8") for n in (A, B, C)}
    amap = build_anchor_map(old)
    rm = Remapper(amap)

    # 1. expand same-file fragment links in Parts A-C
    def expand(text: str, base: str) -> str:
        def repl(m):
            label, target = m.group(1), m.group(2)
            if target.startswith("#"):
                return f"[{label}]({base}{target})"
            return m.group(0)
        return LINK_RE.sub(repl, text)

    texts = {n: expand(t, n) for n, t in old.items()}

    # 2. rewrite references everywhere
    changed = 0
    results: dict[str, str] = {}
    for rel in git_files():
        if not processable(rel):
            continue
        if rel in (A, B, C):
            src = texts[rel]
        else:
            p = ROOT / rel
            try:
                src = p.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
        if "core_08_" not in src and rel not in CH8 and "Chapter Eight" not in src:
            continue
        in_ch8 = rel in CH8 or rel == HUB
        dst = rm.rewrite_links(src, rel)
        dst = rm.rewrite_bare(dst, rel, in_ch8)
        if dst != (texts[rel] if rel in CH8 else src):
            results[rel] = dst
            changed += 1
        elif rel in CH8:
            results[rel] = dst

    # 3. recompose
    if not args.skip_compose:
        new_a, new_b = compose(results[A], results[B])
        new_c = recompose_c(results[C])
        results[A], results[B], results[C] = new_a, new_b, new_c

    # 4. normalise same-file explicit links in Parts A-C
    def normalise(text: str, base: str) -> str:
        def repl(m):
            label, target = m.group(1), m.group(2)
            path, frag = split_target(target)
            if frag and path == base:
                return f"[{label}](#{frag})"
            return m.group(0)
        return LINK_RE.sub(repl, text)

    for n in (A, B, C):
        results[n] = normalise(results[n], n)

    print(f"files changed: {len(results)}  links rewritten: {rm.report['links']}  "
          f"numbers rewritten: {rm.report['text_nums']}  titles: {rm.report['titles']}")
    if rm.report["unresolved"]:
        print("UNRESOLVED:", rm.report["unresolved"][:10])
    if rm.report["ranges"]:
        print(f"link texts citing a different section than their target: {len(rm.report['ranges'])}")
        for r in rm.report["ranges"][:20]:
            print("  ", r)
    if args.report:
        lines = []
        for rel, dec, num, ctx in rm.report["bare"]:
            lines.append(f"{dec}\t{rel}\t§{num}\t{ctx}")
        args.report.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"bare cite report: {len(lines)} rows -> {args.report}")
    if args.dry_run:
        return 0
    for rel, text in results.items():
        (ROOT / rel).write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
