#!/usr/bin/env python3
"""Catch a bare "finding" where a violation finding is meant.

Rule ID: VIOLATION-FINDING-01

"Finding" is used in two families in the corpus. Evaluation and certification
findings (component findings, risk findings, cause findings, restoration
findings) are always qualified. A *violation finding* is the verified finding
that someone violated the Constitution, which a standing lock, an Interim Hold,
a sanction, or a misconduct designation rests on. That one is often written
bare: "a lock attaches only to a verified finding", "the finding it rested on".
A reader of Chapter Twelve cannot tell from the word alone which family is meant.

The audit reads each line, not the file (AUDIT-SCOPE-01). It flags the noun
**finding** / **findings** when both hold:

* **Bare.** The word before it is a determiner or a bare modifier (a, the, this,
  that, each, any, no, its, verified, adverse, unresolved, ...). A qualified
  form (violation finding, component finding, non-compliance finding, cause
  finding, "Violation Axis s = 7 finding") is not matched.
* **Violation line.** The same line speaks of violations, standing locks,
  Interim Holds, misconduct, sanctions, wrongdoing, allegations, or a merits
  matter.

Not matched: "finding of violation / misconduct / harm / non-compliance / independent review" (it
says what the finding is of); "finding profile / authority / basis" (finding is
the qualifier there); a bare "finding" that follows a "violation
finding" earlier on the same line (it points back); inline code, link targets,
fenced code, and `doc_architecture.md` (its dated move log keeps the wording
each move used).

Fix: say **violation finding** (or **verified violation finding**) when a finding
of violation is meant. Where a different finding is meant, qualify that one
(component finding, cause finding, and so on).

Older uses sit in the shrink-only baseline
``tools/architecture/baselines/violation_finding.json``: a new bare use anywhere
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
RULE = "VIOLATION-FINDING-01"
BASELINE_NAME = "violation_finding"
EXEMPT = frozenset({"doc_architecture.md"})  # its dated move log keeps the wording each move used

_FINDING_WORD = re.compile(r"(?<![A-Za-z0-9-])(findings?)(?![A-Za-z0-9-])", re.IGNORECASE)

# Words that leave "finding" unqualified: determiners, and modifiers that do not say what the finding is of.
_BARE_PRECEDERS = frozenset(
    """
    a an the this that these those each every any another its their our same one no such
    verified adverse unresolved earlier later prior final published recorded formal underlying
    """.split()
)

# A line that speaks of violations, locks, holds, sanctions, or misconduct is a line where "finding" most often means a violation finding.
_VIOLATION_LINE_CUE = re.compile(
    r"violation|misconduct|wrongdoing|sanction|interim hold|\block(?:s|ed)?\b|standing (?:effect|record)"
    r"|allegation|accusation|set[- ]aside|\bmerits\b",
    re.IGNORECASE,
)

# "finding of violation" and its kin already say what the finding is of.
_NAMED_OBJECT = re.compile(
    r"\s+(?:of|about|that)\s+(?:an?\s+|the\s+)?(?:violations?|misconduct|harm|wrongdoing|non-?compliance|breach|independent review)\b",
    re.IGNORECASE,
)
_VIOLATION_FINDING = re.compile(r"violation[- ]findings?\b", re.IGNORECASE)
# "finding profile", "finding authority", "finding basis": here "finding" is itself the qualifier.
_USED_AS_MODIFIER = re.compile(r"\s+(?:profiles?|authorit(?:y|ies)|basis|steps?|records?|types?)\b", re.IGNORECASE)

ADVICE = (
    "bare 'finding' on a violation line: say 'violation finding' (or 'verified violation finding') "
    "if a finding of violation is meant, or qualify the other kind of finding"
)


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    phrase: str
    text: str


def bare_finding_phrases(check_line: str) -> list[str]:
    """Return the bare 'finding' phrases on one masked line (empty when the line passes)."""
    if not _VIOLATION_LINE_CUE.search(check_line):
        return []
    phrases: list[str] = []
    for match in _FINDING_WORD.finditer(check_line):
        word = _pathway_preceding_word(check_line, match.start())
        if word not in _BARE_PRECEDERS:
            continue
        if _NAMED_OBJECT.match(check_line[match.end() :]) or (
            match.group(1).lower() == "finding" and _USED_AS_MODIFIER.match(check_line[match.end() :])
        ):
            continue
        if _VIOLATION_FINDING.search(check_line[: match.start() + 1]):
            continue  # points back to a violation finding named earlier on the line
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
        phrases = bare_finding_phrases(check_line)
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
        print(f"PASS: {RULE} — no new bare 'finding' on a violation line{extra}.")
        return 0
    print(f"FAIL: {RULE} — {len(findings)} bare 'finding' use(s), {len(stale)} stale baseline entr(ies).")
    for f in findings:
        print(f"  {f.file}:{f.line}: {RULE}: '{f.phrase}': {ADVICE}")
    for k in stale:
        print(f"  stale baseline entry (use fixed; remove it with --write-baseline): {k}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
