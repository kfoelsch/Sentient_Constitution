#!/usr/bin/env python3
"""Catch a bare "ground" where the text should say which kind of ground it is.

Rule ID: GROUND-QUALIFIED-01

In the corpus a *ground* is a stated reason that supports an outcome: a ground for
denial or revocation, for a stay, for an Interim Hold, for reopening. Written bare
("a ground", "the grounds", "that ground") the word leaves the reader to work out
which outcome and whose reason is meant, and two grounds on one page are easy to
mix up. The same trouble the bare "finding" had.

The audit reads each line (AUDIT-SCOPE-01). It flags the noun **ground** /
**grounds** when the word before it is a determiner or a modifier that does not say
what kind of ground it is (a, the, this, that, its, own, stated, lawful, only, ...).

A qualified form is accepted: *denial ground*, *revocation ground*, *readiness
ground*, *reopening ground*, *System ground*, *institutional ground*, *hold grounds*,
*protected grounds*.

Not matched: "ground for / of / against ..." and "grounds for / of / against ..."
(it says what the ground is for); the verb "ground" / "grounds" ("a rule that grounds
the duty", "may ground a denial"); "common ground", "ground truth", "on the ground", "ground level"; inline
code, link targets, fenced code, and `doc_architecture.md` (its dated move log keeps
the wording each move used).

Fix: name the kind: *denial ground*, *revocation ground*, *reopening ground*, and so
on, or say "ground for <outcome>". When two grounds are in play, name each.

Older uses sit in the shrink-only baseline
``tools/architecture/baselines/ground_qualified.json``: a new bare use anywhere
fails, and a baseline entry whose line was fixed also fails until it is removed
with ``--write-baseline``. ``--ignore-baseline`` lists the whole backlog.
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
RULE = "GROUND-QUALIFIED-01"
BASELINE_NAME = "ground_qualified"
EXEMPT = frozenset({"doc_architecture.md"})  # its dated move log keeps the wording each move used

_GROUND_WORD = re.compile(r"(?<![A-Za-z0-9-])(grounds?)(?![A-Za-z0-9-])", re.IGNORECASE)

# Words that leave "ground" unqualified: determiners, pronouns, numerals, prepositions, conjunctions,
# and modifiers that do not say what kind of ground it is.
_BARE_PRECEDERS = frozenset(
    """
    a an the this that these those each every any another its their his her our your my whose which what
    some no neither either both same other such own one two three first second third only sole main primary
    further additional separate listed named relevant stated verified lawful valid sufficient good real
    mislabeled unstated all more most few several many not or and but nor on of for in under by with from
    to at as when if where is are was were be may can will shall must does do did s
    """.split()
)

# "ground for denial", "grounds of sex": the ground says what it is for.
_NAMED_OBJECT = re.compile(r"\s+(?:for|of|against)\b", re.IGNORECASE)
# The verb: "a rule that grounds the duty".
_VERB_PRECEDERS = frozenset({"that", "which", "this", "it", "who", "and", "also", "then", "which"})
_VERB_FOLLOWERS = re.compile(
    r"\s+(?:the|a|an|its|their|this|that|each|every|any|no|all|both|those|these|his|her|our)\b",
    re.IGNORECASE,
)
# The base verb after a modal or "to": "none of those factors may ground a denial".
_MODAL_VERB_PRECEDERS = frozenset({"may", "can", "could", "will", "would", "shall", "should", "must", "might", "to"})
# Other senses of the word.
_OTHER_SENSE = re.compile(
    r"(?:common|firm|solid|level|high|middle)\s+ground\b|\bground\s+(?:truth|level|rules?|zero)\b|\bon\s+the\s+ground\b",
    re.IGNORECASE,
)

ADVICE = (
    "bare 'ground': say which kind (denial ground, revocation ground, reopening ground, "
    "System ground, institutional ground, ...) or 'ground for <outcome>'"
)


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    phrase: str
    text: str


def bare_ground_phrases(check_line: str) -> list[str]:
    """Return the bare 'ground' phrases on one masked line (empty when the line passes)."""
    phrases: list[str] = []
    for match in _GROUND_WORD.finditer(check_line):
        word = _pathway_preceding_word(check_line, match.start())
        if word not in _BARE_PRECEDERS:
            continue
        tail = check_line[match.end() :]
        if _NAMED_OBJECT.match(tail):
            continue
        if (
            match.group(1).lower() == "grounds"
            and word in _VERB_PRECEDERS
            and _VERB_FOLLOWERS.match(tail)
        ):
            continue
        if match.group(1).lower() == "ground" and word in _MODAL_VERB_PRECEDERS:
            continue
        window = check_line[max(0, match.start() - 14) : match.end() + 12]
        if _OTHER_SENSE.search(window):
            continue
        phrases.append(f"{word} {match.group(1)}")
    return phrases


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
        check_line = _mask_inline_code_and_link_targets(raw)
        phrases = bare_ground_phrases(check_line)
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
        print(f"PASS: {RULE} — no new bare 'ground'{extra}.")
        return 0
    print(f"FAIL: {RULE} — {len(findings)} bare 'ground' use(s), {len(stale)} stale baseline entr(ies).")
    for f in findings:
        print(f"  {f.file}:{f.line}: {RULE}: '{f.phrase}': {ADVICE}")
    for k in stale:
        print(f"  stale baseline entry (use fixed; remove it with --write-baseline): {k}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
