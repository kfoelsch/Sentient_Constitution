#!/usr/bin/env python3
"""Catch a numbered anti-constitutional-misconduct criterion cited without its name.

Rule ID: CRITERION-NAMED-01

Chapter Fourteen §3.3 sets six criteria for anti-constitutional-misconduct designation,
and the corpus cites them by number ("criterion 3", "criteria 1 and 2", "criteria 1-4").
A bare number tells the reader nothing, and the reader has to leave the page to learn
what it means. Every numbered reference therefore carries the name of each criterion it
cites, in a parenthetical right after the number:

    criterion 3 (*Material rollback effect*)
    criteria 1 and 2 (*Willful deceptive intent* and *Knowing falsification or suppression*)
    criteria 1-4 (*Willful deceptive intent*; *Knowing falsification or suppression*;
        *Material rollback effect*; and *Causally significant conduct*)

The names are the ones Chapter Fourteen §3.3 gives:

    1 Willful deceptive intent
    2 Knowing falsification or suppression
    3 Material rollback effect
    4 Causally significant conduct
    5 Insurrection or material forcible subversion
    6 Operative nullification

The audit reads each line (AUDIT-SCOPE-01) of every corpus file. It finds "criterion" or
"criteria" followed by one or more digits (single, "and" / "or" / comma lists, ranges
such as 1-4 or "1 through 4", with or without bold markers) and checks that the text
right after the last number is a parenthetical naming every criterion the number group
covers (a range names each number in it). Italic markers inside the parenthetical are
ignored.

Accepted without a parenthetical: a list introduction that ends in a colon and is
followed within twelve lines by the numbered definition lines ("1. **Willful deceptive
intent:** ...") of every criterion it cites, which is how §3.3 itself introduces them.

Not matched: a number with no "criterion" or "criteria" word in front of it, the words
without a digit ("the section 3 criteria"), inline code, link targets, fenced code, and
`doc_architecture.md` (its dated move log keeps the wording each move used).

The audit also fails when Chapter Fourteen §3.3 no longer gives one of the six names
above, so the table here cannot drift from the source.

Fix: add the names, or run ``python3 tools/criterion_named_audit.py --fix`` to insert
them after every unnamed reference. A reference that already has a parenthetical without
the names is left for a hand edit. There is no baseline: every older use was named in
the move that added this rule, and a new unnamed number anywhere fails.
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

from corpus_paths import binding_corpus_scope  # noqa: E402
from lexical_vocabulary_audit import _mask_inline_code_and_link_targets  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RULE = "CRITERION-NAMED-01"
EXEMPT = frozenset({"doc_architecture.md"})  # its dated move log keeps the wording each move used
SOURCE_FILE = "core_14.000_misconduct_designation.md"

NAMES = {
    1: "Willful deceptive intent",
    2: "Knowing falsification or suppression",
    3: "Material rollback effect",
    4: "Causally significant conduct",
    5: "Insurrection or material forcible subversion",
    6: "Operative nullification",
}

_NUM = r"\*{0,2}\d(?:\s*[–—-]\s*\d)?\*{0,2}"
_SEP = r"(?:\s*,\s*(?:and\s+|or\s+)?|\s+(?:and|or)\s+|\s+\*{0,2}through\*{0,2}\s+)"
_REF = re.compile(
    rf"(?<![A-Za-z])criteri(?:on|a)\*{{0,2}}\s*(?P<nums>{_NUM}(?:{_SEP}{_NUM})*)",
    re.IGNORECASE,
)
_TOKEN = re.compile(r"\d|through|[–—-]", re.IGNORECASE)

ADVICE = (
    "numbered criterion without its name: add the name in a parenthetical right after the "
    "number, for example 'criterion 3 (*Material rollback effect*)' (names: Chapter Fourteen §3.3)"
)


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    phrase: str
    text: str
    fixable: bool


def numbers_in(nums: str) -> list[int]:
    """Return the criterion numbers a number group covers, expanding ranges, in order."""
    out: list[int] = []
    tokens = _TOKEN.findall(nums)
    i = 0
    while i < len(tokens):
        tok = tokens[i].lower()
        if tok.isdigit():
            out.append(int(tok))
        elif i > 0 and i + 1 < len(tokens) and tokens[i - 1].isdigit() and tokens[i + 1].isdigit():
            lo, hi = int(tokens[i - 1]), int(tokens[i + 1])
            for n in range(lo + 1, hi):
                out.append(n)
        i += 1
    seen: list[int] = []
    for n in out:
        if n not in seen:
            seen.append(n)
    return seen


def _balanced_parenthetical(tail: str) -> str | None:
    """Return the text inside a parenthetical that opens the tail, or None."""
    m = re.match(r"\s*\(", tail)
    if not m:
        return None
    depth = 0
    for idx in range(m.end() - 1, len(tail)):
        if tail[idx] == "(":
            depth += 1
        elif tail[idx] == ")":
            depth -= 1
            if depth == 0:
                return tail[m.end() : idx]
    return None


def names_missing(numbers: list[int], tail: str) -> list[int]:
    """Return the numbers whose names are not in the parenthetical that opens the tail."""
    inside = _balanced_parenthetical(tail)
    plain = (inside or "").replace("*", "").replace("_", "").lower()
    return [n for n in numbers if n in NAMES and NAMES[n].lower() not in plain]


def _definition_list_follows(numbers: list[int], following: list[str]) -> bool:
    window = following[:12]
    for n in numbers:
        if n not in NAMES:
            return False
        rx = re.compile(rf"^\s*(?:[-*]\s*)?{n}\.\s*\*\*{re.escape(NAMES[n])}", re.IGNORECASE)
        if not any(rx.match(line) for line in window):
            return False
    return True


def _in_italics(prefix: str) -> bool:
    """True when an unclosed single-asterisk italic span is open at the end of the prefix."""
    return prefix.replace("**", "").count("*") % 2 == 1


def name_text(numbers: list[int], nums_raw: str, italic_open: bool) -> str:
    """Build the parenthetical content that names the numbers."""
    names = [NAMES[n] for n in numbers if n in NAMES]
    marks = [n if italic_open else f"*{n}*" for n in names]
    if len(marks) == 1:
        return marks[0]
    joiner = "or" if re.search(r"\sor\s", nums_raw, re.IGNORECASE) else "and"
    if len(marks) == 2:
        return f"{marks[0]} {joiner} {marks[1]}"
    return "; ".join(marks[:-1]) + f"; {joiner} {marks[-1]}"


def refs_in_line(masked: str, following: list[str]) -> list[tuple[int, int, str, list[int], bool]]:
    """Return (start, end, phrase, numbers, fixable) for each unnamed numbered criterion on a line."""
    found = []
    for match in _REF.finditer(masked):
        numbers = numbers_in(match.group("nums"))
        if not numbers or any(n not in NAMES for n in numbers):
            continue
        tail = masked[match.end() :]
        if not names_missing(numbers, tail):
            continue
        if masked.rstrip().endswith(":") and _definition_list_follows(numbers, following):
            continue
        fixable = _balanced_parenthetical(tail) is None
        found.append((match.start(), match.end(), match.group(0).strip(), numbers, fixable))
    return found


def scan_text(rel_path: str, text: str) -> list[Finding]:
    if rel_path in EXEMPT:
        return []
    findings: list[Finding] = []
    lines = text.splitlines()
    in_fence = False
    for idx, raw in enumerate(lines):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        masked = _mask_inline_code_and_link_targets(raw)
        for _s, _e, phrase, _numbers, fixable in refs_in_line(masked, lines[idx + 1 :]):
            findings.append(Finding(rel_path, idx + 1, phrase, raw.strip(), fixable))
    return findings


def fix_text(rel_path: str, text: str) -> tuple[str, int]:
    """Insert the names after every fixable unnamed reference; return the new text and the count."""
    if rel_path in EXEMPT:
        return text, 0
    lines = text.splitlines(keepends=True)
    plain = [ln.rstrip("\r\n") for ln in lines]
    in_fence = False
    fixed = 0
    for idx, raw in enumerate(plain):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        masked = _mask_inline_code_and_link_targets(raw)
        refs = [r for r in refs_in_line(masked, plain[idx + 1 :]) if r[4]]
        if not refs:
            continue
        new = raw
        for start, end, _phrase, numbers, _fixable in sorted(refs, reverse=True):
            nums_raw = raw[start:end]
            italic_open = _in_italics(new[:end])
            content = name_text(numbers, nums_raw, italic_open)
            new = new[:end] + f" ({content})" + new[end:]
            fixed += 1
        eol = lines[idx][len(raw) :]
        lines[idx] = new + eol
    return "".join(lines), fixed


def source_lacks_names(root: Path) -> list[str]:
    """Return the names that Chapter Fourteen §3.3 no longer gives as numbered definition lines."""
    path = root / SOURCE_FILE
    if not path.is_file():
        return [f"{SOURCE_FILE} is missing"]
    text = path.read_text(encoding="utf-8")
    missing = []
    for n, name in NAMES.items():
        rx = re.compile(rf"^\s*(?:[-*]\s*)?{n}\.\s*\*\*{re.escape(name)}", re.IGNORECASE | re.MULTILINE)
        if not rx.search(text):
            missing.append(f"criterion {n}: '{name}'")
    return missing


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--paths", nargs="*", help="Scan only these corpus files.")
    parser.add_argument("--fix", action="store_true", help="Insert the names after every unnamed reference.")
    parser.add_argument("--report", action="store_true", help="Print the count of unnamed references per file.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    scope = list(binding_corpus_scope(root, include_support_docs=True))
    if args.paths:
        scope = [p for p in args.paths if p in set(scope)]

    if args.fix:
        total = 0
        for rel_path in scope:
            path = root / rel_path
            if not path.is_file():
                continue
            text = path.read_text(encoding="utf-8")
            new_text, n = fix_text(rel_path, text)
            if n:
                path.write_text(new_text, encoding="utf-8")
                print(f"fixed {n:3d}  {rel_path}")
                total += n
        print(f"fixed {total} reference(s)")
        return 0

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

    lacking = [] if args.paths else source_lacks_names(root)
    if not findings and not lacking:
        print(f"PASS: {RULE} — every numbered criterion carries its name.")
        return 0
    print(f"FAIL: {RULE} — {len(findings)} unnamed numbered criterion reference(s), {len(lacking)} missing source name(s).")
    for f in findings:
        hand = "" if f.fixable else " (has a parenthetical without the names: edit by hand)"
        print(f"  {f.file}:{f.line}: {RULE}: '{f.phrase}': {ADVICE}{hand}")
    for item in lacking:
        print(f"  {SOURCE_FILE}: {RULE}: §3.3 no longer gives {item}; update NAMES in tools/criterion_named_audit.py")
    return 1


if __name__ == "__main__":
    sys.exit(main())
