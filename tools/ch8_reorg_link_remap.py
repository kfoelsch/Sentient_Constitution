#!/usr/bin/env python3
"""Remap links after the Chapter Eight §1–§9 reorganization.

Old Part A §1–§10 / Part B §11–§16 anchors are retargeted to the new
§1–§9 anchors (no alias anchors are kept). Link text that carries the old
section number or title is updated to match. Historical snapshots under
archive/, evidence/, and evaluation/results/ are left untouched.

Usage: python3 tools/ch8_reorg_link_remap.py [--apply]
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


add(A, "11-rights-floors-this-chapter-helps-verify", A, "5-rights-floor-and-domain-evaluations", "1.1", "5",
    [("Rights floors this chapter helps verify", "Rights-Floor and Domain Evaluations")])
add(A, "21-participation-and-proportionality-at-class-scale", A, "21-how-class-scales-every-evaluation", "2.1", "2.1",
    [("Participation and proportionality at class scale", "How class scales every evaluation")])
add(A, "32-accessibility-under-sentience-non-exclusion", A, "54-accessibility-evaluation", "3.2", "5.4",
    [("Accessibility Under Sentience Non-Exclusion", "Accessibility Evaluation")])
add(A, "33-privacy-informational-joint-invocation", A, "32-privacy-informational-joint-invocation", "3.3", "3.2")
for old in ("34-voluntary-discontinuation-major-self-modification-and-exit-rights",
            "34-voluntary-discontinuation-and-exit-rights"):
    add(A, old, A, "33-voluntary-discontinuation-major-self-modification-and-exit-rights", "3.4", "3.3")
add(A, "35-assembly-collective-organization-and-institutional-formation", A,
    "34-assembly-collective-organization-and-institutional-formation", "3.5", "3.4")
add(A, "351-dissent-and-peaceful-protest", A, "341-dissent-and-peaceful-protest", "3.5.1", "3.4.1")
add(A, "36-time-consistency-constraint", A, "35-time-consistency-constraint", "3.6", "3.5")
add(A, "37-governance-incentive-and-contestability-discipline", A,
    "36-governance-incentive-and-contestability-discipline", "3.7", "3.6")
for f in (A, C):
    add(f, "38-illustrative-whole-system-application-by-class-non-exhaustive", f,
        "37-illustrative-whole-system-application-by-class-non-exhaustive", "3.8", "3.7")
add(A, "5-ecological-footprint-evaluation", A, "51-ecological-footprint-evaluation", "5", "5.1")
for old in ("6-proportionate-cross-system-support-evaluation", "6-proportionate-cross-system-contribution-evaluation"):
    add(A, old, A, "52-proportionate-cross-system-support-evaluation", "6", "5.2")
add(A, "7-nondiscrimination-evaluation", A, "53-nondiscrimination-evaluation", "7", "5.3")
add(A, "8-accessibility-evaluation", A, "54-accessibility-evaluation", "8", "5.4")
add(A, "9-educational-capability-and-learning-system-integrity-evaluation", A,
    "55-educational-capability-and-learning-system-integrity-evaluation", "9", "5.5")
add(A, "10-trustworthiness-and-system-reliance-integrity-evaluation", A,
    "56-trustworthiness-and-system-reliance-integrity-evaluation", "10", "5.6")
for f in (A, C):
    for old, new, ol, nl in [
        ("51-illustrative-ecological-footprint-application-by-class-non-exhaustive",
         "511-illustrative-ecological-footprint-application-by-class-non-exhaustive", "5.1", "5.1.1"),
        ("61-illustrative-cross-system-support-application-by-class-non-exhaustive",
         "521-illustrative-cross-system-support-application-by-class-non-exhaustive", "6.1", "5.2.1"),
        ("71-illustrative-nondiscrimination-application-by-class-non-exhaustive",
         "531-illustrative-nondiscrimination-application-by-class-non-exhaustive", "7.1", "5.3.1"),
        ("81-illustrative-accessibility-application-by-class-non-exhaustive",
         "541-illustrative-accessibility-application-by-class-non-exhaustive", "8.1", "5.4.1"),
        ("91-illustrative-educational-capability-application-by-class-non-exhaustive",
         "551-illustrative-educational-capability-application-by-class-non-exhaustive", "9.1", "5.5.1"),
        ("101-illustrative-trustworthiness-application-by-class-non-exhaustive",
         "561-illustrative-trustworthiness-application-by-class-non-exhaustive", "10.1", "5.6.1"),
    ]:
        add(f, old, f, new, ol, nl)
for old in ("11-system-certification-record", "11-certification-record"):
    add(B, old, B, "6-system-certification-record", "11", "6")
add(B, "111-minimum-record-contents", B, "61-minimum-record-contents", "11.1", "6.1")
add(B, "112-cross-section-record-requirements", B, "61-minimum-record-contents", "11.2", "6.1",
    [("Cross-section record requirements", "Minimum record contents"),
     ("cross-section record requirements", "minimum record contents")])
add(B, "113-rights-floor-record-evaluation-non-substitution", A, "5-rights-floor-and-domain-evaluations", "11.3", "5",
    [("Rights-Floor record evaluation (non-substitution)", "Rights-Floor and Domain Evaluations"),
     ("Part B", "Part A")])
add(B, "12-transparency-auditability-and-contestability", B, "62-record-integrity-transparency-and-auditability",
    "12", "6.2",
    [("Transparency, Auditability, and Contestability", "Record integrity: transparency and auditability")])
add(B, "13-forum-supervision-and-component-roles", B, "71-forum-supervision-and-component-roles", "13", "7.1")
add(B, "14-supervisory-sequence-and-contestability-chain", B, "7-forum-process", "14", "7",
    [("Supervisory Sequence and Contestability Chain", "Forum Process")])
add(B, "141-supervisory-sequence", B, "72-supervisory-sequence", "14.1", "7.2")
add(B, "142-contestability-chain", B, "732-contestability-chain", "14.2", "7.3.2")
add(B, "142-contestability-paths", B, "731-contestability-paths", "14.2", "7.3.1")
add(B, "143-anti-bypass", B, "733-anti-bypass", "14.3", "7.3.3")
add(B, "15-relationship-to-standing", B, "9-relationship-to-standing", "15", "9")
add(B, "16-reopening-misalignment-and-non-evasion", B, "8-outcomes-revalidation-and-reopening", "16", "8",
    [("Reopening, Misalignment, and Non-Evasion", "Outcomes, Revalidation, and Reopening"),
     ("Reopening, misalignment, and non-evasion", "Outcomes, revalidation, and reopening")])

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
