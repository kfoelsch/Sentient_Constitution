#!/usr/bin/env python3
"""Catch a bare "scope" where the text should say whose or which scope it is.

Rule ID: SCOPE-QUALIFIED-01

"Scope" is used for several different things in the corpus: the **chartered scope** a System
Charter or Institutional Charter states, a definition's **In scope** / **Out of scope**
fields, a dependent cluster's **admission scope**, a **release scope**, an
**enforceability scope**, the scope of an evaluation, and more. Written bare ("the scope",
"that scope", "its scope", "a scope") the word leaves the reader to work out which of them
is meant, and a line that mentions two of them reads two ways. The same trouble the bare
"ground", "finding" and "record" had.

The audit reads each line (AUDIT-SCOPE-01). It flags the noun **scope** / **scopes** when
the word before it is a determiner or a generic modifier that does not say whose or which
scope it is (a, the, this, that, its, their, own, same, whole, full, narrow, broader, ...).

Not matched, because the scope is named:

* a word before it that names the kind: *chartered scope*, *admission scope*, *release
  scope*, *enforceability scope*, *supervised scope*, ...;
* "scope of ..." and "scope for ..." (it says what the scope belongs to);
* a following relative clause or pointer: "the scope above", "the scope each cluster states",
  "the scope it is supervised under", "the scope that was actually adopted";
* compounds in which "scope" modifies the next noun: *scope document*, *scope cap*,
  *scope creep*;
* the field labels of Chapter Five and the corpus operations files: **In scope:**, **Out of
  scope:**, **Admission scope:** (the word before "scope" is "in", "out of" or a kind), so
  Chapter Five needs no exemption and a new bare use there still fails;
* "Class A scope" (the A is a class letter), emphasis markers around the word
  ("the **scope** of restriction"), the verb ("to scope a review"), inline code, link targets, fenced code, and
  `doc_architecture.md` (its dated move log keeps the wording each move used).

Fix: name the scope. Inside a chapter about one kind, say it each time the word stands
alone, for example *the chartered scope* in Chapter Seven. Where a line really means "what
this thing covers", write "scope of <thing>" or name the thing ("the system, institution,
or business the standing record concerns").

Older uses sit in the shrink-only baseline
``tools/architecture/baselines/scope_qualified.json``: a new bare use anywhere fails, and a
baseline entry whose line was fixed also fails until it is removed with
``--write-baseline``. ``--ignore-baseline`` lists the whole backlog and ``--report`` counts
it per file.
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
RULE = "SCOPE-QUALIFIED-01"
BASELINE_NAME = "scope_qualified"
EXEMPT = frozenset({"doc_architecture.md"})  # its dated move log keeps the wording each move used

_SCOPE_WORD = re.compile(r"(?<![A-Za-z0-9-])(scopes?)(?![A-Za-z0-9-])", re.IGNORECASE)

# Words that leave "scope" unqualified: determiners, pronouns, numerals, quantifiers, and
# modifiers that describe the scope without saying whose or which scope it is. Words that
# carry their own referent ("what", "which", "whose") are not listed.
_BARE_PRECEDERS = frozenset(
    """
    a an the this that these those each every any another its their his her our your some no
    same other such own one two three single whole entire all both separate prior earlier new
    current full narrow narrower broad broader wide wider larger smaller limited
    """.split()
)

# "scope of the Charter", "scope for review": the scope says what it belongs to.
_NAMED_OBJECT = re.compile(r"\s+(?:of|for)\b", re.IGNORECASE)
# "the scope above", "the scope each cluster states", "the scope it is supervised under".
_POINTER_TAIL = re.compile(
    r"\s+(?:above|below|that|which|it|its|each|their|his|her|whose|this|the|a|an|under|within|stated|named)\b",
    re.IGNORECASE,
)
# Compounds in which "scope" modifies the next noun (scope document, scope cap, scope creep, ...).
_COMPOUND_HEAD = re.compile(
    r"\s+(?:documents?|caps?|creep|statements?|labels?|fields?|lines?|contraction|map|notes?)\b",
    re.IGNORECASE,
)

# "Class A scope" (the capital A is a class letter) and emphasis markers around the word.
_CLASS_LETTER = re.compile(r"\bClass\s+A\s+$")
_EMPHASIS = re.compile(r"^[*_]+")

ADVICE = (
    "bare 'scope': say whose or which scope (chartered scope, admission scope, release scope, "
    "enforceability scope, ...) or 'scope of <thing>'"
)


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    phrase: str
    text: str


def bare_scope_spans(check_line: str) -> list[tuple[int, int, str]]:
    """Return (start, end, preceding word) for each bare 'scope' on one masked line."""
    spans: list[tuple[int, int, str]] = []
    for match in _SCOPE_WORD.finditer(check_line):
        word = _pathway_preceding_word(check_line, match.start())
        if word not in _BARE_PRECEDERS:
            continue
        # "Class A scope": the capital A is a class letter, not the article.
        if word == "a" and _CLASS_LETTER.search(check_line[: match.start()]):
            continue
        # "the **scope** of restriction": step over emphasis markers before reading the tail.
        tail = _EMPHASIS.sub("", check_line[match.end() :])
        if _NAMED_OBJECT.match(tail) or _POINTER_TAIL.match(tail) or _COMPOUND_HEAD.match(tail):
            continue
        spans.append((match.start(), match.end(), word))
    return spans


def bare_scope_phrases(check_line: str) -> list[str]:
    """Return the bare 'scope' phrases on one masked line (empty when the line passes)."""
    return [f"{word} {check_line[s:e]}" for s, e, word in bare_scope_spans(check_line)]


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
        phrases = bare_scope_phrases(_mask_inline_code_and_link_targets(raw))
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
        print(f"PASS: {RULE} — no new bare 'scope'{extra}.")
        return 0
    print(f"FAIL: {RULE} — {len(findings)} bare 'scope' use(s), {len(stale)} stale baseline entr(ies).")
    for f in findings:
        print(f"  {f.file}:{f.line}: {RULE}: '{f.phrase}': {ADVICE}")
    for k in stale:
        print(f"  stale baseline entry (use fixed; remove it with --write-baseline): {k}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
