#!/usr/bin/env python3
"""Flag prose that lists a definition's components but leaves out Measurement (M).

Every constitutional definition has four parts that are met together:
Ontological (O), Measurement (M), Assessment (A), and Compliance (C)
(Subcore 3-A §3). A sentence in the binding corpus that names two or more of
the O, A, and C parts by their tagged names, or speaks of a definition's
"semantic, assessment, and compliance scope", must also name Measurement.
Otherwise it reads as if measurement were outside the protected scope.

Scope: ``core_*.md``, ``subcore_*.md``, the four corpus wrappers, and their
``corpus_*/`` subfiles.

Rule ID: OMAC-LIST-01 (blocking; part of ``make regression``).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULE = "OMAC-LIST-01"

TAGGED = (
    re.compile(r"\bOntological\s*\(O\)"),
    re.compile(r"\bAssessment\s*\(A\)"),
    re.compile(r"\bCompliance\s*\(C\)"),
)
SCOPE_PHRASE = re.compile(r"\bsemantic,\s*assessment,?\s*and\s*compliance\b", re.I)
LETTERS = re.compile(r"\bO,\s*A,?\s*and\s*C\b|\bO/A/C\b")
HAS_M = re.compile(r"\bMeasurement\s*\(M\)|\bmeasurement\b|\bO/M/A/C\b|\bO,\s*M,", re.I)
SENTENCE_SPLIT = re.compile(r"(?<=[.;])\s+")
FENCE_RE = re.compile(r"^(```|~~~)")


def corpus_files(root: Path) -> list[Path]:
    pats = ("core_*.md", "subcore_*.md", "corpus_*.md", "corpus_*/*.md")
    return sorted({p for pat in pats for p in root.glob(pat) if p.is_file()})


def scan_text(rel: str, text: str) -> list[str]:
    findings: list[str] = []
    in_fence = False
    for number, line in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for sentence in SENTENCE_SPLIT.split(line):
            tagged = sum(bool(rx.search(sentence)) for rx in TAGGED)
            listed = tagged >= 2 or SCOPE_PHRASE.search(sentence) or LETTERS.search(sentence)
            if listed and not HAS_M.search(sentence):
                snippet = sentence.strip()
                snippet = snippet if len(snippet) <= 90 else snippet[:87] + "..."
                findings.append(
                    f"{rel}:{number}: {RULE}: lists definition components without "
                    f"Measurement (M): {snippet}"
                )
    return findings


def audit(root: Path) -> list[str]:
    findings: list[str] = []
    for path in corpus_files(root):
        rel = path.relative_to(root).as_posix()
        findings += scan_text(rel, path.read_text(encoding="utf-8"))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    findings = audit(root)
    if findings:
        print(f"FAIL: {RULE} — {len(findings)} component list(s) leave out Measurement (M).")
        for line in findings:
            print(f"  {line}")
        return 2
    print(f"PASS: {RULE} — every O/A/C component list in {len(corpus_files(root))} corpus files names Measurement (M).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
