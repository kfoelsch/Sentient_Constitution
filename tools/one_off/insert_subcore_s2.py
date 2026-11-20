#!/usr/bin/env python3
"""Insert a reviewed §2 into numbered subcore files and renumber (one-off, 2026-11-20).

For each file: optionally move a block of §1 to a new section, insert the §2 text after
§1, renumber headings, numbered bold paragraph labels and their numeric `<a id>`s, then
rewrite every link (fragment and label) and every plain "Subcore X-Y §N" cite in the
live tree. Archive, evidence, translations and dated project files are left as they are.
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

HEAD_RE = re.compile(r"^(#{3,6}) (\d+(?:\.\d+)*)(\.?) (.*)$")
LABEL_RE = re.compile(r"^(\s*(?:[-*] )?\*\*)(\d+(?:\.\d+)+)\.")
AID_RE = re.compile(r'<a id="([^"]+)"></a>')
LINK_RE = re.compile(r"(\[(?:[^\[\]]|\[[^\]]*\])*\])\(([^)\s]+)\)")
SKIP = ("archive/", "evidence/", "translations/", "project/", "doc_architecture/generated/")


def slugs(lines):
    seen, out = {}, {}
    for i, l in enumerate(lines):
        m = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", l)
        if not m:
            continue
        b = github_slug(m.group(1))
        n = seen.get(b, 0)
        seen[b] = n + 1
        out[i] = b if n == 0 else f"{b}-{n}"
    return out


def process(spec):
    f = spec["file"]
    lines = (ROOT / f).read_text(encoding="utf-8").split("\n")
    old_slugs = slugs(lines)
    # tag each line with its object id so we can find it after moves
    tagged = [(i, l) for i, l in enumerate(lines)]
    top_of = {}
    cur = None
    for i, l in tagged:
        m = HEAD_RE.match(l)
        if m and len(m.group(1)) == 3:
            cur = int(m.group(2))
        top_of[i] = cur
    move = spec.get("move")  # {"start_id": ..., "before_top": 8, "heading": "...", "new_top": 9}
    moved_idx = set()
    if move:
        s = next(i for i, l in tagged if f'<a id="{move["start_id"]}"></a>' in l)
        e = next(i for i, l in tagged if i > s and HEAD_RE.match(l) and len(HEAD_RE.match(l).group(1)) == 3)
        while not tagged[e - 1][1].strip():
            e -= 1
        moved_idx = set(range(s, e))
    def newnum(num, idx):
        parts = num.split(".")
        top = int(parts[0])
        if (idx in moved_idx and top == 1) or (idx == -2 and move and any(num == x or num.startswith(x + ".") for x in move["nums"])):
            parts[0] = str(move["new_top"])
        else:
            parts[0] = str(spec["map"].get(str(top), top))
        return ".".join(parts)
    out = []
    id_map = {}
    num_of_old_anchor = {}
    for i, l in tagged:
        m = HEAD_RE.match(l)
        if m:
            nn = newnum(m.group(2), i)
            num_of_old_anchor[old_slugs[i]] = (m.group(2), nn)
            l = f"{m.group(1)} {nn}{m.group(3)} {m.group(4)}"
        lm = LABEL_RE.match(l)
        if lm:
            l = lm.group(1) + newnum(lm.group(2), i) + "." + l[lm.end():]
        def rid(mm, i=i):
            a = mm.group(1)
            t = top_of[i]
            if t is None:
                return mm.group(0)
            dm = re.match(r"^(\d+)(.*)$", a)
            if not dm or not dm.group(1).startswith(str(t)):
                return mm.group(0)
            nt = newnum(str(t), i).split(".")[0]
            na = nt + dm.group(1)[len(str(t)):] + dm.group(2)
            id_map[a] = na
            return f'<a id="{na}"></a>'
        l = AID_RE.sub(rid, l)
        out.append((i, l))
    # numbers for custom ids (bold labels)
    for k, (i, l) in enumerate(out):
        for a in AID_RE.findall(l):
            for j in range(k + 1, min(k + 3, len(out))):
                lm = LABEL_RE.match(out[j][1])
                if lm:
                    old = [x for x, y in id_map.items() if y == a]
                    if old:
                        num_of_old_anchor[old[0]] = (None, lm.group(2))
                    break
    # move block
    if move:
        block = [x for x in out if x[0] in moved_idx]
        rest = [x for x in out if x[0] not in moved_idx]
        pos = next(k for k, (i, l) in enumerate(rest) if HEAD_RE.match(l) and len(HEAD_RE.match(l).group(1)) == 3 and top_of[i] == move["before_top"])
        ins = [(-1, move["heading"]), (-1, ""), (-1, move["plain"]), (-1, "")] + block + [(-1, "")]
        out = rest[:pos] + ins + rest[pos:]
    # insert §2 before the heading that was old §2
    pos = next(k for k, (i, l) in enumerate(out) if i >= 0 and HEAD_RE.match(lines[i]) and len(HEAD_RE.match(lines[i]).group(1)) == 3 and top_of[i] == 2)
    s2 = spec["s2"].rstrip("\n").split("\n")
    out = out[:pos] + [(-1, x) for x in s2] + [(-1, "")] + out[pos:]
    new_lines = [l for _, l in out]
    new_slugs = slugs(new_lines)
    # map old anchors -> new anchors via original line index
    pos_of = {i: k for k, (i, _) in enumerate(out) if i >= 0}
    amap = {}
    for i, s in old_slugs.items():
        if i in pos_of and pos_of[i] in new_slugs:
            amap[s] = new_slugs[pos_of[i]]
    amap.update(id_map)
    nummap = {}
    for a, (o, n) in num_of_old_anchor.items():
        pass
    (ROOT / f).write_text("\n".join(new_lines), encoding="utf-8")
    return amap, newnum


def main():
    specs = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    maps = {}
    for sp in specs:
        amap, nn = process(sp)
        maps[sp["file"]] = (amap, nn, sp)
    files = subprocess.run(["git", "ls-files", "*.md"], cwd=ROOT, capture_output=True, text=True).stdout.split()
    label_by_file = {sp["file"]: sp["label"] for sp in specs}
    def mapnum_str(numstr, nn):
        return re.sub(r"\d+(?:\.\d+)*", lambda m: nn(m.group(0), -2), numstr)
    changed = []
    for rel in files:
        if rel.startswith(SKIP):
            continue
        p = ROOT / rel
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        orig = text
        def fix(m):
            label, target = m.group(1), m.group(2)
            if re.match(r"^(https?:|mailto:)", target):
                return m.group(0)
            path, _, frag = target.partition("#")
            tgt = os.path.relpath((p.parent / path).resolve() if path else p.resolve(), ROOT)
            if tgt not in maps:
                return m.group(0)
            amap, nn, sp = maps[tgt]
            if frag and frag in amap:
                frag = amap[frag]
            # map § numbers in the label (old numbering)
            label = re.sub(r"(section )(\d+)(?=\b)", lambda mm: mm.group(1) + nn(mm.group(2), -2), label) if label.startswith("[" + sp["label"]) else label
            label = re.sub(r"(§§?\s?)(\d+(?:\.\d+)*(?:\s?[–-]\s?\d+(?:\.\d+)*)?)", lambda mm: mm.group(1) + mapnum_str(mm.group(2), nn), label)
            return f"{label}({path}{'#' + frag if frag else ''})"
        # plain cites outside links
        segs = []
        last = 0
        for m in LINK_RE.finditer(text):
            segs.append(("t", text[last:m.start()]))
            segs.append(("l", m))
            last = m.end()
        segs.append(("t", text[last:]))
        res = []
        for kind, v in segs:
            if kind == "l":
                res.append(fix(v))
                continue
            for tf, (amap, nn, sp) in maps.items():
                lab = re.escape(sp["label"])
                v = re.sub(rf"({lab},? §§?\s?)(\d+(?:\.\d+)*(?:\s?[–-]\s?\d+(?:\.\d+)*)?)", lambda mm: mm.group(1) + mapnum_str(mm.group(2), nn), v)
                v = re.sub(rf"({lab}, section )(\d+)", lambda mm: mm.group(1) + nn(mm.group(2), -2), v)
                if rel == tf:
                    v = re.sub(r"(\*\*§)(\d+(?:\.\d+)*)(\*\*)", lambda mm: mm.group(1) + nn(mm.group(2), -2) + mm.group(3), v)
            res.append(v)
        text = "".join(res)
        if text != orig:
            p.write_text(text, encoding="utf-8")
            changed.append(rel)
    print(json.dumps({"changed": len(changed)}))


if __name__ == "__main__":
    main()
