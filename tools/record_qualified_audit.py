#!/usr/bin/env python3
"""Catch a bare "the record" where a line names two kinds of certification record.

Rule ID: RECORD-QUALIFIED-01

Chapter Nine's "the record" is the System Certification Record; Chapter Ten reads it
as the Institutional Certification Record ("reading Institution for System"). On a
line that names one kind of record and also speaks of the other kind's owner (a
System Certification Record and an Institution, or an Institutional Certification
Record and a System), a bare "the record", "this record" or "that record" can
point to either. The reader should not have to work out which.

The audit reads each line (AUDIT-SCOPE-01). It flags "the record", "this record" or
"that record" when the same line (a) names a System record (*System Certification
Record*, *the System's record*) and speaks of an Institution, or (b) names an
Institution's record (*Institutional Certification Record*, *the Institution's
record*) and speaks of a System.

Not matched: a line that names only one kind of record, "the record seat" and
"record-keeping" (other nouns), inline code, link targets, fenced code, and
`doc_architecture.md` (its dated move log keeps the wording each move used).

Fix: name the record: *the Institutional Certification Record*, *the System
Certification Record*, or "that System's record".
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope  # noqa: E402
from lexical_vocabulary_audit import _mask_inline_code_and_link_targets  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RULE = "RECORD-QUALIFIED-01"
EXEMPT = frozenset({"doc_architecture.md"})  # its dated move log keeps the wording each move used

# "the record", "this record", "that record" as a bare noun. Other nouns that start with
# "record" (record seat, record-keeping, record span) and a possessive are not matched.
_BARE_RECORD = re.compile(
    r"(?<![A-Za-z0-9-])(?P<det>the|this|that)\s+record"
    r"(?![A-Za-z0-9'’-])(?!\s+(?:seat|seats|holder|custodian|span|contents|versions?|keeping))",
    re.IGNORECASE,
)
_SYSTEM_RECORD = re.compile(
    r"System Certification Records?|\bSystems?['’]s? records?\b|\bSystem records?\b", re.IGNORECASE
)
_INSTITUTION_RECORD = re.compile(
    r"Institutional Certification Records?|\bInstitution['’]s records?\b|\bInstitutional records?\b|"
    r"\bInstitution records?\b",
    re.IGNORECASE,
)
_SYSTEM_WORD = re.compile(r"\bSystems?\b|\bSystem['’]s\b")
_INSTITUTION_WORD = re.compile(r"\bInstitutions?\b|\bInstitution['’]s\b|\bInstitutional\b")

ADVICE = (
    "bare record on a line that names both a System and an Institution: say "
    "'the Institutional Certification Record' or 'the System Certification Record'"
)


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    phrase: str
    text: str


def mixed_record_line(check_line: str) -> bool:
    """True when the masked line names one kind of record and speaks of the other kind's owner."""
    if not _BARE_RECORD.search(check_line):
        return False
    without_inst = _INSTITUTION_RECORD.sub(" ", check_line)
    without_sys = _SYSTEM_RECORD.sub(" ", check_line)
    names_system = bool(_SYSTEM_RECORD.search(check_line))
    names_inst = bool(_INSTITUTION_RECORD.search(check_line))
    if names_inst and _SYSTEM_WORD.search(without_inst):
        return True
    if names_system and _INSTITUTION_WORD.search(without_sys):
        return True
    return False


def bare_record_phrases(check_line: str) -> list[str]:
    """Return the bare record phrases on one masked line when the line is a mixed-record line."""
    if not mixed_record_line(check_line):
        return []
    return [f"{m.group('det').lower()} record" for m in _BARE_RECORD.finditer(check_line)]


def scan_text(rel_path: str, text: str) -> list[Finding]:
    if rel_path in EXEMPT:
        return []
    findings: list[Finding] = []
    in_fence = False
    for idx, raw in enumerate(text.splitlines(), start=1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        phrases = bare_record_phrases(_mask_inline_code_and_link_targets(raw))
        if phrases:
            findings.append(Finding(file=rel_path, line=idx, phrase=phrases[0], text=raw.strip()))
    return findings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--paths", nargs="*", help="Scan only these corpus files.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    scope = list(binding_corpus_scope(root, include_support_docs=True))
    if args.paths:
        scope = [p for p in args.paths if p in set(scope)]
    findings: list[Finding] = []
    for rel_path in scope:
        path = root / rel_path
        if path.is_file():
            findings.extend(scan_text(rel_path, path.read_text(encoding="utf-8")))
    if not findings:
        print(f"PASS: {RULE} — no bare record on a line that names both a System and an Institution.")
        return 0
    print(f"FAIL: {RULE} — {len(findings)} bare record use(s) on mixed System/Institution lines.")
    for f in findings:
        print(f"  {f.file}:{f.line}: {RULE}: '{f.phrase}': {ADVICE}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
