#!/usr/bin/env python3
"""Catch a sentence copied from Chapter Nine into its parallel Chapter Ten.

Rule ID: CH10-DUPLICATION-01

Chapter Ten (Institutional Alignment Certification) runs the same process as Chapter Nine
(System Alignment Certification) for an Institution. Its header says "Reuse, not repetition":
where the meaning is the same, Chapter Ten summarizes and points to Chapter Nine and sets out
only what differs for an Institution. Hand-kept copies drift (the first comparison found
copies that had already diverged), so this audit finds them.

It reads every sentence of eight or more words in Chapter Ten and looks for a near-verbatim
match in Chapter Nine Parts A, B and C. Both sides are normalized first, so that a plain
noun swap does not hide a copy: "Institution", "Institutional", "System", "operator" and
"governing authority" all count as the same word, and links, emphasis and list markers are
dropped. Two sentences are near-verbatim when their word sequences are 85% alike or closer.

Not read: Trace, reader-guide and other collapsed ``<details>`` widgets, fenced code, anchors,
link targets, and sentences under eight words. Plain-terms lines match on purpose, because
they are the parallel the reader sees; they sit in the baseline like any other accepted copy.

Fix: replace the copied sentence with a short summary and a pointer ("Chapter Nine Part C
§9.3.2 applies, reading Institution for System") and keep only what differs for an
Institution. Where a copy is intended, rewrite the baseline with ``--write-baseline``.

Older copies sit in the shrink-only baseline
``tools/architecture/baselines/ch10_duplication.json``: a new near-verbatim sentence fails, and
a baseline entry whose sentence was rewritten or removed also fails until it is deleted with
``--write-baseline``. ``--ignore-baseline`` lists every near-copy. ``--report`` prints the share
of near-verbatim sentences in each Chapter Ten section and always exits 0.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

import audit_baseline  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RULE = "CH10-DUPLICATION-01"
BASELINE_NAME = "ch10_duplication"
TARGET = "core_10.000_institutional_alignment_certification.md"
SOURCES = {
    "A": "core_09.000_system_alignment_certification_evaluation.md",
    "B": "core_09.005_system_alignment_certification_record_process.md",
    "C": "core_09.010_system_alignment_certification_record_recertification.md",
}
MIN_WORDS = 8
THRESHOLD = 0.85
SHINGLE = 3  # word run used to find candidate pairs quickly

ADVICE = (
    "near-verbatim copy of Chapter Nine; say it once there and point to it, or summarize it and keep only "
    "what differs for an Institution (CH10-DUPLICATION-01)"
)

_HEADING = re.compile(r"^(#{3,6})\s+(\d+(?:\.\d+)*)\.?\s")
_SUBSTITUTIONS = (
    (re.compile(r"\binstitutions\b"), "x"),
    (re.compile(r"\binstitutional\b"), "x"),
    (re.compile(r"\binstitution\b"), "x"),
    (re.compile(r"\bsystems\b"), "x"),
    (re.compile(r"\bsystem\b"), "x"),
    (re.compile(r"\boperators\b"), "x"),
    (re.compile(r"\boperator\b"), "x"),
    (re.compile(r"\bgoverning authority\b"), "x"),
    (re.compile(r"\bchapter (?:nine|ten)(?: part [abc])?\b"), "ch"),
)


@dataclass(frozen=True)
class Sentence:
    file: str
    line: int
    section: str
    text: str
    tokens: tuple[str, ...]


@dataclass(frozen=True)
class Match:
    target: Sentence
    source: Sentence
    ratio: float


def normalize(text: str) -> tuple[str, ...]:
    s = text.lower()
    for pattern, repl in _SUBSTITUTIONS:
        s = pattern.sub(repl, s)
    s = s.replace("\u2019s", "").replace("'s", "")
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    tokens: list[str] = []
    for word in s.split():
        word = "a" if word == "an" else word
        if word == "x" and tokens and tokens[-1] == "x":
            continue  # "system operator", "Institution's governing authority" read as one noun
        tokens.append(word)
    return tuple(tokens)


def _clean(line: str) -> str:
    line = re.sub(r'<a id="[^"]*"></a>', "", line)
    line = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line)
    line = re.sub(r"[*_`>|]+", "", line)
    return line.strip(" -0123456789.\t")


def extract_sentences(rel_path: str, text: str) -> list[Sentence]:
    """Sentences of MIN_WORDS words or more, outside collapsed widgets and code fences."""
    out: list[Sentence] = []
    in_details = False
    in_code = False
    section = ""
    for number, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if stripped.startswith("<details"):
            in_details = True
            continue
        if stripped.startswith("</details"):
            in_details = False
            continue
        if in_details:
            continue
        match = _HEADING.match(raw)
        if match:
            section = match.group(2)
            continue
        cleaned = _clean(raw)
        if not cleaned:
            continue
        for piece in re.split(r"(?<=[.;:])\s+", cleaned):
            if len(piece.split()) >= MIN_WORDS:
                tokens = normalize(piece)
                if len(tokens) >= SHINGLE:
                    out.append(Sentence(rel_path, number, section, piece.strip(), tokens))
    return out


def _shingles(tokens: tuple[str, ...]) -> set[tuple[str, ...]]:
    return {tokens[i : i + SHINGLE] for i in range(len(tokens) - SHINGLE + 1)}


def near_copies(targets: list[Sentence], sources: list[Sentence], threshold: float = THRESHOLD) -> list[Match]:
    """Each target sentence with its closest source sentence at or above the threshold."""
    index: dict[tuple[str, ...], list[int]] = defaultdict(list)
    source_shingles = []
    for i, s in enumerate(sources):
        sh = _shingles(s.tokens)
        source_shingles.append(sh)
        for g in sh:
            index[g].append(i)
    found: list[Match] = []
    for t in targets:
        t_sh = _shingles(t.tokens)
        shared: Counter = Counter()
        for g in t_sh:
            for i in index.get(g, ()):
                shared[i] += 1
        need = max(1, int(0.3 * len(t_sh)))
        best_ratio, best = 0.0, None
        for i, count in shared.items():
            if count < need:
                continue
            ratio = difflib.SequenceMatcher(None, t.tokens, sources[i].tokens, autojunk=False).ratio()
            if ratio > best_ratio:
                best_ratio, best = ratio, sources[i]
        if best is not None and best_ratio >= threshold:
            found.append(Match(t, best, best_ratio))
    return found


def load_sentences(root: Path) -> tuple[list[Sentence], list[Sentence]]:
    target_path = root / TARGET
    targets = extract_sentences(TARGET, target_path.read_text(encoding="utf-8")) if target_path.is_file() else []
    sources: list[Sentence] = []
    for part, name in SOURCES.items():
        path = root / name
        if path.is_file():
            for s in extract_sentences(name, path.read_text(encoding="utf-8")):
                sources.append(Sentence(f"Chapter Nine Part {part}", s.line, s.section, s.text, s.tokens))
    return targets, sources


def _top(section: str) -> str:
    return section.split(".")[0] if section else "-"


def report(targets: list[Sentence], matches: list[Match]) -> None:
    totals: Counter = Counter(_top(t.section) for t in targets)
    copied: Counter = Counter(_top(m.target.section) for m in matches)
    print(f"{RULE}: share of Chapter Ten sentences (>= {MIN_WORDS} words) that are near-verbatim to Chapter Nine")
    print("  §   sentences  near-verbatim  share")
    for sec in sorted(totals, key=lambda x: (not x.isdigit(), int(x) if x.isdigit() else 0)):
        n, c = totals[sec], copied[sec]
        print(f"  {sec:>2}  {n:>9}  {c:>13}  {100 * c / max(n, 1):>4.0f}%")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--ignore-baseline", action="store_true", help="List every near-copy, baselined or not.")
    parser.add_argument("--report", action="store_true", help="Print the share per Chapter Ten section; exit 0.")
    parser.add_argument(
        "--write-baseline",
        action="store_true",
        help="Rewrite the shrink-only baseline (AUDIT-SCOPE-01) from the current near-copies.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    targets, sources = load_sentences(root)
    matches = near_copies(targets, sources)
    if args.report:
        report(targets, matches)
        return 0

    findings = matches
    baselined = 0
    stale: list[str] = []
    if not args.ignore_baseline:
        seen: Counter = Counter()
        keyed = [(audit_baseline.make_key(m.target.file, m.target.text, seen), m.target.text, m) for m in matches]
        if args.write_baseline:
            audit_baseline.write(root, BASELINE_NAME, RULE, [(k, t) for k, t, _m in keyed])
            print(f"WROTE baseline: {len(keyed)} entries")
            return 0
        new, stale = audit_baseline.split(root, BASELINE_NAME, keyed)
        baselined = len(matches) - len(new)
        findings = new

    if not findings and not stale:
        extra = f"; {baselined} older near-copy sentence(s) in the shrink-only baseline" if baselined else ""
        print(f"PASS: {RULE} — no new near-verbatim copy of Chapter Nine in Chapter Ten{extra}.")
        return 0
    print(f"FAIL: {RULE} — {len(findings)} new near-verbatim copy sentence(s), {len(stale)} stale baseline entr(ies).")
    for m in findings:
        t, s = m.target, m.source
        print(f"  {t.file}:{t.line}: {RULE}: §{t.section} matches {s.file} §{s.section} line {s.line} at {m.ratio:.0%}: {ADVICE}")
        print(f"    {t.text[:160]}")
    for k in stale:
        print(f"  stale baseline entry (sentence rewritten or removed; delete it with --write-baseline): {k}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
