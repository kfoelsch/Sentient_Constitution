#!/usr/bin/env python3
"""Chapter Eight: split Phase II (Evaluate) into sub-phases IIa / IIb / IIc.

  Part A §3.1–§3.4 (Always)            stay §3.1–§3.4            (IIa)
  Part A §3.5–§3.7 (When implicated)   become §4.1–§4.3          (IIb)
  Part A §3.8      (When triggered)    becomes §5, §5.1–§5.6     (IIc)
  Part C §3.8.N.1                      become §5.N.1
  Part B §4–§8                         become §6–§10

One simultaneous pass from a single old->new table (no sequential renumbering, so
Part B's old §4 cannot collide with the new Part A §4). Remaps link anchors,
link labels that carry the old number, explicit <a id> anchors, and heading numbers
in Parts A, B, and C. Plain-text cites outside links are NOT touched here; they are
edited by hand and checked by the audits.

Usage: python3 tools/ch8_phase2_split_remap.py [--apply]
"""
from __future__ import annotations
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
A = "core_09_a_system_alignment_certification_evaluation.md"
B = "core_09_b_system_alignment_certification_record_process.md"
C = "core_09_c_system_alignment_certification_illustrations.md"

M: dict[tuple[str, str], tuple] = {}
def add(f, old, new, ol, nl):
    M[(f, old)] = (new, ol, nl)

# ---- Part A: IIb and IIc --------------------------------------------------
for old, new, ol, nl in [
    ("35-privacy-informational-joint-invocation", "41-privacy-informational-joint-invocation", "3.5", "4.1"),
    ("36-voluntary-discontinuation-major-self-modification-and-exit-rights", "42-voluntary-discontinuation-major-self-modification-and-exit-rights", "3.6", "4.2"),
    ("37-assembly-collective-organization-and-institutional-formation", "43-assembly-collective-organization-and-institutional-formation", "3.7", "4.3"),
    ("371-dissent-and-peaceful-protest", "431-dissent-and-peaceful-protest", "3.7.1", "4.3.1"),
    ("38-rights-floor-and-domain-evaluations", "5-rights-floor-and-domain-evaluations", "3.8", "5"),
    ("381-ecological-footprint-evaluation", "51-ecological-footprint-evaluation", "3.8.1", "5.1"),
    ("382-educational-capability-and-learning-system-integrity-evaluation", "52-educational-capability-and-learning-system-integrity-evaluation", "3.8.2", "5.2"),
    ("383-proportionate-cross-system-support-evaluation", "53-proportionate-cross-system-support-evaluation", "3.8.3", "5.3"),
    ("384-nondiscrimination-evaluation", "54-nondiscrimination-evaluation", "3.8.4", "5.4"),
    ("385-accessibility-evaluation", "55-accessibility-evaluation", "3.8.5", "5.5"),
    ("386-trustworthiness-and-system-reliance-integrity-evaluation", "56-trustworthiness-and-system-reliance-integrity-evaluation", "3.8.6", "5.6"),
]:
    add(A, old, new, ol, nl)
# ---- Part C illustrations (also linked from A) -----------------------------
for i, slug in enumerate(["ecological-footprint", "educational-capability", "cross-system-support",
                          "nondiscrimination", "accessibility", "trustworthiness"], 1):
    for f in (A, C):
        add(f, f"38{i}1-illustrative-{slug}-application-by-class-non-exhaustive",
            f"5{i}1-illustrative-{slug}-application-by-class-non-exhaustive", f"3.8.{i}.1", f"5.{i}.1")
# ---- Part B: +2 ---------------------------------------------------------------
for old, new, ol, nl in [
    ("4-forum-process", "6-forum-process", "4", "6"),
    ("41-forum-supervision-and-component-roles", "61-forum-supervision-and-component-roles", "4.1", "6.1"),
    ("42-supervisory-sequence", "62-supervisory-sequence", "4.2", "6.2"),
    ("43-contestability-chain", "63-contestability-chain", "4.3", "6.3"),
    ("44-anti-bypass", "64-anti-bypass", "4.4", "6.4"),
    ("5-certification-outcomes", "7-certification-outcomes", "5", "7"),
    ("6-system-certification-record", "8-system-certification-record", "6", "8"),
    ("61-minimum-record-contents", "81-minimum-record-contents", "6.1", "8.1"),
    ("62-record-integrity-transparency-and-auditability", "82-record-integrity-transparency-and-auditability", "6.2", "8.2"),
    ("7-recertification-and-reopening", "9-recertification-and-reopening", "7", "9"),
    ("71-challenging-a-certification", "91-challenging-a-certification", "7.1", "9.1"),
    ("711-contestability-paths", "911-contestability-paths", "7.1.1", "9.1.1"),
    ("72-provisional-and-full-certification", "92-provisional-and-full-certification", "7.2", "9.2"),
    ("73-non-evasion", "93-non-evasion", "7.3", "9.3"),
    ("8-relationship-to-standing", "10-relationship-to-standing", "8", "10"),
]:
    add(B, old, new, ol, nl)

LINK = re.compile(r"\[(?P<text>[^\]\n]*)\]\((?P<path>[^)#\s]*)#(?P<anchor>[A-Za-z0-9_-]+)\)")
SKIP_PREFIXES = ("archive/", "evidence/", "evaluation/", ".git/", "node_modules/", "translations/",
                 "doc_architecture/generated/", "ai_corpus/indexes/", "_pages_site/")
SKIP_FILES = {"MEMLOG.md"}   # historical log; tools/ch8_* migration scripts are left as history

def relabel(text, ol, nl):
    return re.sub(r"§" + re.escape(ol) + r"(?![0-9])(?!\.[0-9])", "§" + nl, text)

def remap_links(text, cur, stats):
    def sub(m):
        path, anchor, label = m.group("path"), m.group("anchor"), m.group("text")
        target = Path(path).name if path else cur
        if (target, anchor) not in M:
            return m.group(0)
        new, ol, nl = M[(target, anchor)]
        stats["links"] = stats.get("links", 0) + 1
        return f"[{relabel(label, ol, nl)}]({path}#{new})"
    return LINK.sub(sub, text)

def remap_anchor_ids(text, cur, stats):
    def sub(m):
        key = (cur, m.group(1))
        if key not in M: return m.group(0)
        stats["ids"] = stats.get("ids", 0) + 1
        return f'<a id="{M[key][0]}"></a>'
    return re.sub(r'<a id="([A-Za-z0-9_-]+)"></a>', sub, text)

def a_num(n):                      # Part A / Part C numbering
    p = n.split(".")
    if p[0] != "3" or len(p) < 2 or p[1] not in "5678": return None
    if p[1] == "5": return "4.1" + "".join("." + x for x in p[2:])
    if p[1] == "6": return "4.2" + "".join("." + x for x in p[2:])
    if p[1] == "7": return "4.3" + "".join("." + x for x in p[2:])
    return "5" + "".join("." + x for x in p[2:])

def remap_headings(text, cur, stats):
    out = []
    for line in text.split("\n"):
        m = re.match(r"^(#{3,6}) (\d+(?:\.\d+)*)(\.?) (.*)$", line)
        if m and cur in (A, C, B):
            hashes, n, dot, rest = m.groups()
            new = None
            if cur == B and n.split(".")[0] in "45678" and len(n.split(".")[0]) == 1:
                p = n.split("."); p[0] = str(int(p[0]) + 2); new = ".".join(p)
            elif cur in (A, C):
                new = a_num(n)
                if cur == A and n == "3.8": hashes = "###"
                elif cur == A and n.startswith("3.8."): hashes = hashes[:-1]
            if new:
                line = f"{hashes} {new}{dot} {rest}"; stats["heads"] = stats.get("heads", 0) + 1
        out.append(line)
    return "\n".join(out)

def main():
    apply = "--apply" in sys.argv
    if "### 4. Evaluations Where Implicated" in (ROOT / A).read_text(encoding="utf-8"):
        sys.exit("Already applied: Part A has the new §4. This script renumbers once and is not idempotent.")
    changed, tot = [], {}
    for p in sorted(ROOT.rglob("*.md")):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(SKIP_PREFIXES) or p.name in SKIP_FILES: continue
        try: text = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError): continue
        st = {}
        new = remap_links(text, p.name, st)
        new = remap_anchor_ids(new, p.name, st)
        new = remap_headings(new, p.name, st)
        if new != text:
            changed.append((rel, st))
            for k, v in st.items(): tot[k] = tot.get(k, 0) + v
            if apply: p.write_text(new, encoding="utf-8")
    for rel, st in changed:
        print(f"{st.get('links',0):5d} links {st.get('ids',0):3d} ids {st.get('heads',0):3d} heads  {rel}")
    print(f"files: {len(changed)}; {tot}; applied: {apply}")

if __name__ == "__main__":
    main()
