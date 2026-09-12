#!/usr/bin/env python3
"""
Planet-first Chapter Seven article renumber (old Roman -> new Roman).

Mapping: implementation/CH7_ARTICLE_RENUMBER_PLANET_FIRST_2026.md

Run from repo root:
  python3 tools/ch7_execute_planet_first_renumber.py

Uses placeholders for collision safety; expands old canonical ranges for
Articles R1–R2; handles common comma lists; rewrites bold **VI-A**-style refs.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

OLD_ORDER = "I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI XVII XVIII XIX XX XXI XXII XXIII".split()

OLD_TO_NEW: dict[str, str] = {
    "VI": "I",
    "VII": "II",
    "V": "III",
    "XX": "IV",
    "I": "V",
    "X": "VI",
    "II": "VII",
    "III": "VIII",
    "IV": "IX",
    "XIX": "X",
    "IX": "XI",
    "VIII": "XII",
    "XII": "XIII",
    "XI": "XIV",
    "XIII": "XV",
    "XIV": "XVI",
    "XVI": "XVII",
    "XVIII": "XVIII",
    "XXI": "XIX",
    "XXII": "XX",
    "XV": "XXI",
    "XVII": "XXII",
    "XXIII": "XXIII",
}

_ROMANS_LONGEST_FIRST = sorted(OLD_TO_NEW.keys(), key=len, reverse=True)
_ROMAN_ALT = "|".join(re.escape(r) for r in _ROMANS_LONGEST_FIRST)


def old_rank(r: str) -> int:
    return OLD_ORDER.index(r)


def new_rank(r: str) -> int:
    return OLD_ORDER.index(r)


def expand_old_range(a: str, b: str) -> list[str]:
    i, j = old_rank(a), old_rank(b)
    if i > j:
        i, j = j, i
    return OLD_ORDER[i : j + 1]


def format_articles_list(new_romans: list[str]) -> str:
    s = sorted(set(new_romans), key=new_rank)
    if not s:
        return "Articles"
    runs: list[tuple[str, str]] = []
    start = end = s[0]
    for r in s[1:]:
        if new_rank(r) == new_rank(end) + 1:
            end = r
        else:
            runs.append((start, end))
            start = end = r
    runs.append((start, end))
    parts: list[str] = []
    for a, b in runs:
        parts.append(a if a == b else f"{a}–{b}")
    if len(parts) == 1:
        return f"Articles {parts[0]}"
    return "Articles " + ", ".join(parts[:-1]) + ", and " + parts[-1]


def remap_old_list(olds: list[str]) -> str:
    news = [OLD_TO_NEW[o] for o in olds]
    return format_articles_list(news)


def sub_articles_range(m: re.Match[str]) -> str:
    a, b = m.group(1), m.group(2)
    if a not in OLD_TO_NEW or b not in OLD_TO_NEW:
        return m.group(0)
    olds = expand_old_range(a, b)
    return remap_old_list(olds)


# Articles R1–R2 (en dash, hyphen, em dash) in *old* canonical order
_RANGE_RE = re.compile(
    rf"\bArticles\s+({_ROMAN_ALT})\s*[–—-]\s*({_ROMAN_ALT})\b"
)


def sub_articles_comma_clause(m: re.Match[str]) -> str:
    inner = m.group(1)
    found = re.findall(rf"\b({_ROMAN_ALT})\b", inner)
    if len(found) < 2:
        return m.group(0)
    for o in found:
        if o not in OLD_TO_NEW:
            return m.group(0)
    return remap_old_list(found)


# Two or more old Romans after "Articles " with commas / Oxford "and"
_COMMA_LIST_RE = re.compile(
    rf"\bArticles\s+({_ROMAN_ALT}(?:(?:\s*,\s*(?:and\s+)?{_ROMAN_ALT})+))\b"
)


def sub_bold_subsection(m: re.Match[str]) -> str:
    old_r, suf = m.group(1), m.group(2)
    if old_r not in OLD_TO_NEW:
        return m.group(0)
    new_r = OLD_TO_NEW[old_r]
    return f"**{new_r}{suf}**"


_BOLD_SUB_RE = re.compile(rf"\*\*((?:{_ROMAN_ALT}))(-[A-Za-z][A-Za-z\-]*)\*\*")


def sub_singular_article(m: re.Match[str]) -> str:
    prefix, old_r, suf = m.group(1), m.group(2), m.group(3) or ""
    if old_r not in OLD_TO_NEW:
        return m.group(0)
    new_r = OLD_TO_NEW[old_r]
    return f"{prefix} {new_r}{suf}"


_SINGULAR_RE = re.compile(
    rf"\b(Article|article|Articles|articles)\s+({_ROMAN_ALT})(-[A-Za-z][A-Za-z\-]*)?\b"
)

# "Articles I and V–VII" — expand as I + range(V,VII)
_AND_RANGE_RE = re.compile(
    rf"\bArticles\s+({_ROMAN_ALT})\s+and\s+({_ROMAN_ALT})\s*[–—-]\s*({_ROMAN_ALT})\b"
)


def sub_and_range(m: re.Match[str]) -> str:
    r0, r1, r2 = m.group(1), m.group(2), m.group(3)
    if not all(x in OLD_TO_NEW for x in (r0, r1, r2)):
        return m.group(0)
    olds = [r0] + expand_old_range(r1, r2)
    return remap_old_list(olds)


# Optional fourth roman: "Articles I, IV, and XVII" style already covered by comma list if we fix regex
# "Articles XVI–XVII" range covered by _RANGE_RE

# Non-range compounds (apply before range/comma automation; longest first)
EXACT_OLD_TO_NEW_LITERAL: list[tuple[str, str]] = [
    ("**Articles I and V–VII**", "**Articles I–III and V**"),
    ("Articles I and V–VII", "Articles I–III and V"),
    ("**Articles I and V**", "**Articles III and V**"),
    ("Articles I and V", "Articles III and V"),
]


def renumber_text(text: str) -> str:
    # Longest explicit old phrases first (some overlap handled by order)
    for old, new in sorted(EXACT_OLD_TO_NEW_LITERAL, key=lambda x: -len(x[0])):
        text = text.replace(old, new)

    text = _AND_RANGE_RE.sub(sub_and_range, text)
    text = _RANGE_RE.sub(sub_articles_range, text)
    # Comma lists (may double-hit already replaced; OK if no OLD romans left)
    text = _COMMA_LIST_RE.sub(sub_articles_comma_clause, text)
    text = _BOLD_SUB_RE.sub(sub_bold_subsection, text)
    text = _SINGULAR_RE.sub(sub_singular_article, text)
    return text


FILES_CORE = [
    "core_constitution.md",
    "core_02-04_definition_mechanics.md",
    "core_05-05_definitions_a_independent.md",
    "core_amendment.md",
    "corpus_joint_structure.md",
    "corpus_systems.md",
    "corpus_institutions.md",
    "doc_architecture.md",
    "architecture_primer.md",
    "README.md",
    "CONSTITUTIONAL_REGRESSION_SCENARIOS.md",
    "TODO.md",
    "TRUST_UNDER_ATTACK_DELTA_REPORT.md",
    "MEMLOG.md",
]


def collect_paths() -> list[Path]:
    paths = [ROOT / f for f in FILES_CORE]
    impl = ROOT / "implementation"
    if impl.is_dir():
        paths.extend(sorted(p for p in impl.glob("*.md") if p.is_file()))
    ev = ROOT / "evidence"
    if ev.is_dir():
        paths.extend(sorted(ev.rglob("*.md")))
    arch = ROOT / "archive"
    if arch.is_dir():
        paths.extend(sorted(arch.rglob("*.md")))
    tools = ROOT / "tools"
    for p in tools.glob("*.py"):
        if p.name != Path(__file__).name:
            paths.append(p)
    return paths


def main() -> None:
    for path in collect_paths():
        if not path.is_file():
            continue
        try:
            raw = path.read_text(encoding="utf-8")
        except OSError:
            continue
        out = renumber_text(raw)
        if out != raw:
            path.write_text(out, encoding="utf-8", newline="\n")
            print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
