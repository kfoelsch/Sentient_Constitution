#!/usr/bin/env python3
"""Move whole `##` sections out of corpus files into a new subcore file.

One-off tool for plan step 9 of the core reorganization (2026-11-20). It:

1. cuts the named `##` sections (with any `<a id>` lines directly above them)
   out of their source files, in the order given, and numbers them 1, 2, ...
   in the new subcore file (headings demoted one level: `## CS-8.310 §9 X`
   becomes `### 7. X`, `### 9.1 Y` becomes `#### 7.1 Y`);
2. leaves a one-line pointer where each run of sections was cut, or deletes the
   source file when nothing but its header is left;
3. rewrites every link in the repository that pointed at a moved heading or
   `<a id>` so it points at the new file and heading slug, rebases relative links
   inside the moved text, and renames bare file links of deleted sources;
4. rewrites textual cites (`CS-8.310 §9.6`, `Part A §4` in link text to a moved
   target) to `Subcore N-X §M`.

Translations, archive/, evidence/ and dated project drafts are left as they are.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from local_markdown_fragment_audit import github_slug  # noqa: E402

HEAD_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
AID_RE = re.compile(r'<a id="([^"]+)"></a>')
LINK_RE = re.compile(r"(\[(?:[^\[\]]|\[[^\]]*\])*\])\(([^)\s]+)\)")
SKIP = ("archive/", "evidence/", "translations/", "project/translation_drafts/")


def slugs_with_lines(lines: list[str]) -> list[tuple[int, str]]:
    seen: dict[str, int] = {}
    out = []
    in_code = False
    for i, line in enumerate(lines):
        if line.startswith("```"):
            in_code = not in_code
        if in_code:
            continue
        m = HEAD_RE.match(line)
        if not m:
            continue
        base = github_slug(m.group(2))
        n = seen.get(base, 0)
        seen[base] = n + 1
        out.append((i, base if n == 0 else f"{base}-{n}"))
    return out


SEC_PREFIX = re.compile(r"^(?:[A-Z]{2,4}-\d+\.\d+\s+)?(?:Part [A-Z]\s+)?§?\s*(\d+)((?:\.\d+)*)[.:]?\s+(.*)$")


def new_heading(level: int, text: str, newnum: int, oldnum_holder: dict) -> str:
    m = SEC_PREFIX.match(text)
    if m:
        old_top, rest, title = m.group(1), m.group(2), m.group(3)
        if level == 2:
            oldnum_holder["top"] = old_top
            return f"{'#' * (level + 1)} {newnum}. {title}"
        if old_top == oldnum_holder.get("top"):
            return f"{'#' * (level + 1)} {newnum}{rest} {title}"
    return f"{'#' * (level + 1)} {text}"


def tracked_text_files() -> list[str]:
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout.split()
    return [f for f in out if f.endswith((".md", ".json", ".py", ".mmd", ".txt")) and not f.startswith(SKIP)]


def run(spec: dict) -> dict:
    new_file = spec["new_file"]
    label = spec["label"]  # e.g. "Subcore 8-A"
    moved_text: list[str] = []
    anchor_map: dict[tuple[str, str], str] = {}  # (src, old anchor) -> new anchor (in new_file)
    secnum_map: dict[str, dict[str, str]] = {}  # src cite prefix -> {old "9.1": new "7.1"}
    deleted: list[str] = []
    newnum = 0
    new_lines_all: list[str] = []
    line_src: list[str] = []
    per_src: dict[str, list[str]] = {}
    for src, titles in spec["sections"]:
        per_src.setdefault(src, []).extend(titles)
    for src, titles in spec["sections"]:
        lines = (ROOT / src).read_text(encoding="utf-8").split("\n")
        slugs = dict(slugs_with_lines(lines))
        cite = spec["cites"][src]
        secnum_map.setdefault(cite, {})
        cuts = []
        for title in titles:
            start = next(i for i, l in enumerate(lines) if l.rstrip() == title)
            s0 = start
            while s0 > 0 and (AID_RE.fullmatch(lines[s0 - 1].strip() or "x") or not lines[s0 - 1].strip()):
                s0 -= 1
            while s0 < start and not lines[s0].strip():
                s0 += 1
            end = start + 1
            while end < len(lines) and not (lines[end].startswith("## ") or lines[end].startswith("# ")):
                end += 1
            # trailing anchors belong to the next section
            e0 = end
            while e0 > start and (not lines[e0 - 1].strip() or AID_RE.fullmatch(lines[e0 - 1].strip()) or lines[e0 - 1].strip() == "---"):
                e0 -= 1
            newnum += 1
            holder: dict = {}
            block = []
            for i in range(s0, e0):
                line = lines[i]
                for a in AID_RE.findall(line):
                    anchor_map[(src, a)] = a
                m = HEAD_RE.match(line) if not line.startswith("####### ") else None
                if m and i in slugs:
                    lvl = len(m.group(1))
                    nh = new_heading(lvl, m.group(2), newnum, holder)
                    nm = SEC_PREFIX.match(m.group(2))
                    if nm and (lvl == 2 or nm.group(1) == holder.get("top")):
                        secnum_map[cite][nm.group(1) + nm.group(2)] = str(newnum) + (nm.group(2) if lvl > 2 else "")
                    block.append(nh)
                    anchor_map[(src, slugs[i])] = ("__H__", len(new_lines_all) + len(block) - 1)
                else:
                    block.append(line)
            new_lines_all.extend(block + [""])
            line_src.extend([src] * (len(block) + 1))
            cuts.append((s0, e0, newnum))
        for s0, e0, n in sorted(cuts, reverse=True):
            lines[s0:e0] = [f"__CUT__{n}"]
        (ROOT / src).write_text("\n".join(lines), encoding="utf-8")
    # compute new slugs in the new file body
    body = new_lines_all
    newslugs = dict(slugs_with_lines(body))
    for k, v in list(anchor_map.items()):
        if isinstance(v, tuple):
            anchor_map[k] = newslugs[v[1]]
    # pointer text in sources
    for src in per_src:
        text = (ROOT / src).read_text(encoding="utf-8")
        cuts = re.findall(r"__CUT__(\d+)", text)
        nums = [int(c) for c in cuts]
        rel = os.path.relpath(ROOT / new_file, (ROOT / src).parent)
        # collapse consecutive cut markers
        text = re.sub(r"(__CUT__\d+)(\n+__CUT__\d+)+", lambda m: m.group(1), text)
        if nums:
            first, last = min(nums), max(nums)
            span = f"§{first}" if first == last else f"§§{first}–{last}"
            text = re.sub(r"__CUT__\d+", f"*Moved on 2026-11-20 to [{label} {span}]({rel}#{spec['anchor']}), part of the Sentient Constitution.*", text, count=1)
            text = re.sub(r"\n?__CUT__\d+\n?", "\n", text)
        remaining = [l for l in text.split("\n") if l.startswith("## ")]
        if not remaining and spec.get("delete_if_empty", {}).get(src):
            (ROOT / src).unlink()
            subprocess.run(["git", "rm", "-q", "--cached", src], cwd=ROOT)
            deleted.append(src)
        else:
            (ROOT / src).write_text(text, encoding="utf-8")
    # rebase relative links inside moved text (sources live in subdirectories)
    out_lines = []
    src_dir_of_line = None
    def rebase(target: str, from_dir: Path) -> str:
        if re.match(r"^(https?:|mailto:)", target):
            return target
        path, _, frag = target.partition("#")
        if not path:
            return target
        absp = (from_dir / path).resolve()
        return os.path.relpath(absp, ROOT) + ("#" + frag if frag else "")
    # all moved text came from per_src files; they share a directory per spec
    src_dirs = {(ROOT / s).parent for s in per_src}
    assert len(src_dirs) == 1, "sources must share one directory"
    src_dir = src_dirs.pop()
    for line, lsrc in zip(body, line_src):
        def fix(m, lsrc=lsrc):
            t = m.group(2)
            if t.startswith("#"):
                frag = t[1:]
                if (lsrc, frag) in anchor_map:
                    return f"{m.group(1)}(#{anchor_map[(lsrc, frag)]})"
                return f"{m.group(1)}({lsrc}#{frag})"
            return f"{m.group(1)}({rebase(t, src_dir)})"
        out_lines.append(LINK_RE.sub(fix, line))
    header = spec["header"].rstrip("\n") + "\n\n"
    footer = spec.get("footer", "")
    (ROOT / new_file).write_text(header + "\n".join(out_lines).rstrip("\n") + "\n" + footer, encoding="utf-8")
    subprocess.run(["git", "add", "-N", new_file], cwd=ROOT)
    # rewrite links across the repo
    moved_srcs = {s for s, _ in anchor_map}
    cite_res = []
    for cite, mp in secnum_map.items():
        cite_res.append((cite, mp))
    def map_cite_text(s: str) -> str:
        for cite, mp in cite_res:
            esc = re.escape(cite)
            def r(m):
                num = m.group(2)
                if num in mp:
                    return f"{label} §{mp[num]}"
                top = num.split(".")[0]
                if top in mp and "." in num:
                    return f"{label} §{mp[top]}{num[len(top):]}"
                return m.group(0)
            s = re.sub(rf"({esc}),? §(\d+(?:\.\d+)*)", r, s)
        return s
    changed = 0
    for f in tracked_text_files() + [new_file]:
        p = ROOT / f
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        orig = text
        base = p.parent
        def fix(m):
            linktext, target = m.group(1), m.group(2)
            if re.match(r"^(https?:|mailto:)", target):
                return m.group(0)
            path, _, frag = target.partition("#")
            tgt = (base / path).resolve() if path else p.resolve()
            try:
                rel = os.path.relpath(tgt, ROOT)
            except ValueError:
                return m.group(0)
            if rel in moved_srcs and frag and (rel, frag) in anchor_map:
                newt = os.path.relpath(ROOT / new_file, base) + "#" + anchor_map[(rel, frag)]
                if f == new_file:
                    newt = "#" + anchor_map[(rel, frag)]
                lt = re.sub(r"(Part [A-Z]|[A-Z]{2,4}-\d+\.\d+)(?:, Part [A-Z])? §(\d+(?:\.\d+)*)",
                            lambda mm: map_cite_text(f"{spec['cites'][rel]} §{mm.group(2)}") if mm.group(2).split('.')[0] in secnum_map[spec['cites'][rel]] or mm.group(2) in secnum_map[spec['cites'][rel]] else mm.group(0), linktext)
                return f"{lt}({newt})"
            if rel in deleted:
                return f"{linktext}({os.path.relpath(ROOT / new_file, base)}{'#' + frag if frag else ''})"
            return m.group(0)
        text = LINK_RE.sub(fix, text)
        if f.endswith(".md"):
            text = map_cite_text(text)
        if text != orig:
            p.write_text(text, encoding="utf-8")
            changed += 1
    return {"changed_files": changed, "deleted": deleted, "secnum_map": secnum_map, "anchors": len(anchor_map)}


if __name__ == "__main__":
    spec = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps(run(spec), indent=1))
