#!/usr/bin/env python3
"""Stage 2 of the Chapter Eight reorganization: nest §4–§5 under §3 (§3.8, §3.9)
and renumber Part B §6–§9 to §4–§7.

Old Part A §1–§10 / Part B §11–§16 anchors are retargeted to the new
§1–§9 anchors (no alias anchors are kept). Link text that carries the old
section number or title is updated to match. Historical snapshots under
archive/, evidence/, and evaluation/results/ are left untouched.

Usage: python3 tools/ch8_reorg_link_remap_stage2.py [--apply]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
A = "core_08_a_system_alignment_certification_evaluation.md"
B = "core_08_b_system_alignment_certification_record_process.md"
C = "core_08_c_system_alignment_certification_illustrations.md"

# (file, old anchor) -> (new file, new anchor, old label, new label, [(old title, new title), ...])
M: dict[tuple[str, str], tuple] = {}


def add(f, old, nf, new, ol=None, nl=None, titles=()):
    M[(f, old)] = (nf, new, ol, nl, list(titles))


# Stage 2: §4 and §5 become §3.8 and §3.9; Part B §6–§9 become §4–§7.
add(A, "4-data-types-and-handling-evaluation", A, "38-data-types-and-handling-evaluation", "4", "3.8")
add(A, "5-rights-floor-and-domain-evaluations", A, "39-rights-floor-and-domain-evaluations", "5", "3.9")
for old, new, ol, nl in [
    ("51-ecological-footprint-evaluation", "391-ecological-footprint-evaluation", "5.1", "3.9.1"),
    ("52-proportionate-cross-system-support-evaluation", "392-proportionate-cross-system-support-evaluation", "5.2", "3.9.2"),
    ("53-nondiscrimination-evaluation", "393-nondiscrimination-evaluation", "5.3", "3.9.3"),
    ("54-accessibility-evaluation", "394-accessibility-evaluation", "5.4", "3.9.4"),
    ("55-educational-capability-and-learning-system-integrity-evaluation",
     "395-educational-capability-and-learning-system-integrity-evaluation", "5.5", "3.9.5"),
    ("56-trustworthiness-and-system-reliance-integrity-evaluation",
     "396-trustworthiness-and-system-reliance-integrity-evaluation", "5.6", "3.9.6"),
]:
    add(A, old, A, new, ol, nl)
for f in (A, C):
    for old, new, ol, nl in [
        ("41-illustrative-data-handling-application-by-class-non-exhaustive",
         "381-illustrative-data-handling-application-by-class-non-exhaustive", "4.1", "3.8.1"),
        ("511-illustrative-ecological-footprint-application-by-class-non-exhaustive",
         "3911-illustrative-ecological-footprint-application-by-class-non-exhaustive", "5.1.1", "3.9.1.1"),
        ("521-illustrative-cross-system-support-application-by-class-non-exhaustive",
         "3921-illustrative-cross-system-support-application-by-class-non-exhaustive", "5.2.1", "3.9.2.1"),
        ("531-illustrative-nondiscrimination-application-by-class-non-exhaustive",
         "3931-illustrative-nondiscrimination-application-by-class-non-exhaustive", "5.3.1", "3.9.3.1"),
        ("541-illustrative-accessibility-application-by-class-non-exhaustive",
         "3941-illustrative-accessibility-application-by-class-non-exhaustive", "5.4.1", "3.9.4.1"),
        ("551-illustrative-educational-capability-application-by-class-non-exhaustive",
         "3951-illustrative-educational-capability-application-by-class-non-exhaustive", "5.5.1", "3.9.5.1"),
        ("561-illustrative-trustworthiness-application-by-class-non-exhaustive",
         "3961-illustrative-trustworthiness-application-by-class-non-exhaustive", "5.6.1", "3.9.6.1"),
    ]:
        add(f, old, f, new, ol, nl)
for old, new, ol, nl in [
    ("6-system-certification-record", "4-system-certification-record", "6", "4"),
    ("61-minimum-record-contents", "41-minimum-record-contents", "6.1", "4.1"),
    ("62-record-integrity-transparency-and-auditability", "42-record-integrity-transparency-and-auditability", "6.2", "4.2"),
    ("7-forum-process", "5-forum-process", "7", "5"),
    ("71-forum-supervision-and-component-roles", "51-forum-supervision-and-component-roles", "7.1", "5.1"),
    ("72-supervisory-sequence", "52-supervisory-sequence", "7.2", "5.2"),
    ("73-challenging-a-certification", "53-challenging-a-certification", "7.3", "5.3"),
    ("731-contestability-paths", "531-contestability-paths", "7.3.1", "5.3.1"),
    ("732-contestability-chain", "532-contestability-chain", "7.3.2", "5.3.2"),
    ("733-anti-bypass", "533-anti-bypass", "7.3.3", "5.3.3"),
    ("8-outcomes-revalidation-and-reopening", "6-outcomes-revalidation-and-reopening", "8", "6"),
    ("81-certification-outcomes", "61-certification-outcomes", "8.1", "6.1"),
    ("82-revalidation-and-reopening", "62-revalidation-and-reopening", "8.2", "6.2"),
    ("83-non-evasion", "63-non-evasion", "8.3", "6.3"),
    ("9-relationship-to-standing", "7-relationship-to-standing", "9", "7"),
]:
    add(B, old, B, new, ol, nl)

LINK = re.compile(r"\[(?P<text>[^\]\n]*)\]\((?P<path>[^)#\s]*)#(?P<anchor>[A-Za-z0-9_-]+)\)")
SKIP_PREFIXES = ("archive/", "evidence/", "evaluation/results/", ".git/", "node_modules/")


def relabel(text: str, ol: str | None, nl: str | None) -> str:
    if not ol or ol == nl:
        return text
    return re.sub(r"§" + re.escape(ol) + r"(?![0-9])(?!\.[0-9])", "§" + nl, text)


def remap(text: str, cur: str, stats: dict) -> str:
    def sub(m: re.Match) -> str:
        path, anchor, label = m.group("path"), m.group("anchor"), m.group("text")
        target = Path(path).name if path else cur
        key = (target, anchor)
        if key not in M:
            return m.group(0)
        nf, new, ol, nl, titles = M[key]
        if path:
            new_path = path[: len(path) - len(Path(path).name)] + nf if nf != target else path
        else:
            new_path = "" if nf == cur else nf
        label = relabel(label, ol, nl)
        for ot, nt in titles:
            label = label.replace(ot, nt)
        stats["links"] = stats.get("links", 0) + 1
        return f"[{label}]({new_path}#{new})"

    return LINK.sub(sub, text)


def main() -> int:
    apply = "--apply" in sys.argv
    changed = []
    total = {}
    for p in sorted(ROOT.rglob("*.md")):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith(SKIP_PREFIXES):
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        stats: dict = {}
        new = remap(text, p.name, stats)
        if new != text:
            changed.append((rel, stats.get("links", 0)))
            total["links"] = total.get("links", 0) + stats.get("links", 0)
            if apply:
                p.write_text(new, encoding="utf-8")
    for rel, n in changed:
        print(f"{n:5d}  {rel}")
    print(f"files changed: {len(changed)}; links remapped: {total.get('links', 0)}; applied: {apply}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
