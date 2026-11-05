#!/usr/bin/env python3
"""Catch a bare "record" where the text should say which kind of record it is.

Rule ID: RECORD-KIND-01

The corpus keeps several kinds of record: the **standing record** (with its
contribution, violation, operator and stakeholder forms), the **Forum Case Record**,
the **System Certification Record** and **Institutional Certification Record**, and
the named records of Chapters Five to Ten (classification, act, collision, incident,
and so on). Written bare ("the record", "a record", "that record", "its own record")
the word leaves the reader to work out which kind is meant, and a page that handles
two kinds (a standing record that rests on a Forum Case Record, say) reads two ways.
The same trouble the bare "ground" and the bare "finding" had.

The audit reads each line (AUDIT-SCOPE-01). It flags the noun **record** / **records**
when the word before it is a determiner or a modifier that does not say what kind of
record it is (a, the, this, that, its, own, same, one, single, new, official, verified,
reviewable, ...).

A qualified form is accepted: *official record* (Chapter Five's Record Integrity category), *standing record*, *contribution record*, *violation
record*, *Forum Case Record*, *System Certification Record*, *classification record*,
*incident record*, and any other word that names the kind.

Not matched: "record of ..." and "record for ..." (it says what is recorded); the
defined seat names *record custodian*, *record-opening authority*, *record seat*,
*record span*, *record holder*, *Record Version*, *record challenge path* and the other compounds in which "record" modifies a
following noun; the verb ("must record the reasons", "it records the determination");
"on record"; a sentence-initial "Records ..."; inline code, link targets, fenced code,
and `doc_architecture.md` (its dated move log keeps the wording each move used).

Fix: name the kind. Inside a chapter that is about one kind, say it each time the
word stands alone, for example *the standing record* throughout Chapter Eleven §5.
Where a line really means the general idea, use "a record of ..." and say what it
records, or a plural with its kind ("standing records").

Older uses sit in the shrink-only baseline
``tools/architecture/baselines/record_kind.json``: a new bare use anywhere fails, and
a baseline entry whose line was fixed also fails until it is removed with
``--write-baseline``. ``--ignore-baseline`` lists the whole backlog and ``--report``
counts it per file.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

import audit_baseline  # noqa: E402
from corpus_paths import binding_corpus_scope  # noqa: E402
from lexical_vocabulary_audit import (  # noqa: E402
    _mask_inline_code_and_link_targets,
    _pathway_preceding_word,
)

ROOT = Path(__file__).resolve().parents[1]
RULE = "RECORD-KIND-01"
BASELINE_NAME = "record_kind"
EXEMPT = frozenset({"doc_architecture.md"})  # its dated move log keeps the wording each move used

_RECORD_WORD = re.compile(r"(?<![A-Za-z0-9-])(records?)(?![A-Za-z0-9-])", re.IGNORECASE)

# Words that leave "record" unqualified: determiners, pronouns, numerals, quantifiers, and
# modifiers that describe the record without saying what kind of record it is.
_BARE_PRECEDERS = frozenset(
    """
    a an the this that these those each every any another its their his her our your whose which what
    some no same other such own one two three single whole entire all both separate prior earlier new
    current open completed linked related verified published reviewable auditable contestable
    attributable underlying duplicate required
    """.split()
)

# "record of the refusal", "records for review": the record says what it records.
_NAMED_OBJECT = re.compile(r"\s+(?:of|for)\b", re.IGNORECASE)
# Compounds in which "record" modifies the next noun (record custodian, record seat, record span, ...).
_COMPOUND_HEAD = re.compile(
    r"\s+(?:custodians?|opening|seats?|spans?|holders?|contents|keeping|integrity|duty|duties|"
    r"requirements?|paths?|versions?|challenges?|services?)\b",
    re.IGNORECASE,
)

ADVICE = (
    "bare 'record': say which kind (standing record, contribution record, violation record, "
    "Forum Case Record, System Certification Record, ...) or 'record of <what>'"
)


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    phrase: str
    text: str


# "a rule that records the reasons", "a result which records verified readiness": the verb.
_VERB_PRECEDERS = frozenset({"that", "which"})
_VERB_FOLLOWERS = re.compile(
    r"\s+(?:the|a|an|its|their|this|that|each|every|any|no|all|both|those|these|verified|how|why|what|whether|it|them)\b",
    re.IGNORECASE,
)


def bare_record_spans(check_line: str) -> list[tuple[int, int, str]]:
    """Return (start, end, preceding word) for each bare 'record' on one masked line."""
    spans: list[tuple[int, int, str]] = []
    for match in _RECORD_WORD.finditer(check_line):
        word = _pathway_preceding_word(check_line, match.start())
        if word not in _BARE_PRECEDERS:
            continue
        tail = check_line[match.end() :]
        if _NAMED_OBJECT.match(tail) or _COMPOUND_HEAD.match(tail):
            continue
        if word in _VERB_PRECEDERS and match.group(1).lower() == "records" and _VERB_FOLLOWERS.match(tail):
            continue
        spans.append((match.start(), match.end(), word))
    return spans


def bare_record_phrases(check_line: str) -> list[str]:
    """Return the bare 'record' phrases on one masked line (empty when the line passes)."""
    return [f"{word} {check_line[s:e]}" for s, e, word in bare_record_spans(check_line)]


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
    parser.add_argument("--paths", nargs="*", help="Scan only these corpus files (baseline not applied).")
    parser.add_argument("--ignore-baseline", action="store_true", help="List every bare use, baselined or not.")
    parser.add_argument(
        "--write-baseline",
        action="store_true",
        help="Rewrite the shrink-only baseline (AUDIT-SCOPE-01) from the current findings.",
    )
    parser.add_argument("--report", action="store_true", help="Print the count of bare uses per file.")
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

    if args.report:
        counts = Counter(f.file for f in findings)
        for name, n in counts.most_common():
            print(f"{n:4d}  {name}")
        print(f"{len(findings):4d}  total")
        return 0

    use_baseline = not args.paths and not args.ignore_baseline
    baselined = 0
    stale: list[str] = []
    if use_baseline:
        seen: Counter = Counter()
        keyed = [(audit_baseline.make_key(f.file, f.text, seen), f.text, f) for f in findings]
        if args.write_baseline:
            audit_baseline.write(root, BASELINE_NAME, RULE, [(k, t) for k, t, _f in keyed])
            print(f"WROTE baseline: {len(keyed)} entries")
            return 0
        new, stale = audit_baseline.split(root, BASELINE_NAME, keyed)
        baselined = len(findings) - len(new)
        findings = new

    if not findings and not stale:
        extra = f"; {baselined} older use(s) in the shrink-only baseline" if baselined else ""
        print(f"PASS: {RULE} — no new bare 'record'{extra}.")
        return 0
    print(f"FAIL: {RULE} — {len(findings)} bare 'record' use(s), {len(stale)} stale baseline entr(ies).")
    for f in findings:
        print(f"  {f.file}:{f.line}: {RULE}: '{f.phrase}': {ADVICE}")
    for k in stale:
        print(f"  stale baseline entry (use fixed; remove it with --write-baseline): {k}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
