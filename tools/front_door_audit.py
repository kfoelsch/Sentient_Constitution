#!/usr/bin/env python3
"""Keep the public front doors in step with the corpus they describe.

README.md and START_HERE.md (with AGENTS.md, llms.txt, docs/index.md,
CONTRIBUTING.md and the announcement copy) make claims that the corpus can
quietly stop supporting: an edition string, "Chapters 1-17", "28 articles", a
language list, a fit ranking, the wording of the Two Fundamental Questions, a
`make` target. Each check below derives the true value from the corpus itself
and compares it with what the front doors say, so a change in one place fails
loudly until the other is updated.

Section labels in link text (``Chapter One §17.1``) are checked against their
target headings by ``make section-label-anchor-audit``, which scans the same
front-door pages (see ``FRONT_DOOR_FILES`` there). This audit does not repeat
that check.

Rules:
  FRONT-DOOR-EDITION-01    one edition string and effective date everywhere:
                           README table = AGENTS = llms.txt = docs/index.md =
                           ANNOUNCEMENT = CONTRIBUTING = steward index pin
  FRONT-DOOR-EDITION-02    the edition label's date is the effective date
                           (SC-Corpus-2026.10.19 <-> 2026-10-12)
  FRONT-DOOR-EDITION-03    with --edition-tracks-date (until the announcement):
                           the edition is today's date; fix with `make edition-bump`
  FRONT-DOOR-STATUS-01     pages agree on whether the corpus is "pre-release"
  FRONT-DOOR-CHAPTERS-01   "Chapters 1-N" / "One through N" / "N chapters"
                           match the highest numbered core_NN file
  FRONT-DOOR-ARTICLES-01   "N articles" and "Articles I-X" match the Article
                           headings in the Rights Floor files
  FRONT-DOOR-COUNT-01      "more than N hundred" definitions is not above the
                           definition registry count
  FRONT-DOOR-LANG-01       README language bar = translations/*/README.md =
                           translations/README.md; the English-governs
                           statement is present
  FRONT-DOOR-QUESTIONS-01  README and ANNOUNCEMENT quote the Two Fundamental
                           Questions exactly as the Preamble words them
  FRONT-DOOR-MAKE-01       every backticked `make target` and tools/*.py path
                           the front doors name exists
  FRONT-DOOR-LINK-01       every relative link target (any file type) exists
  FRONT-DOOR-FIT-01        START_HERE's ranked situations and non-fits match
                           FIT_SITUATIONS.md one for one
  FRONT-DOOR-AUTHOR-01     authorship names in LICENSE appear in README,
                           docs/index.md and CONTRIBUTING.md
  FRONT-DOOR-POINTER-01    the doors point at each other (README <-> START_HERE,
                           AGENTS, llms.txt, docs/index.md, ANNOUNCEMENT)
  FRONT-DOOR-SECTIONS-01   the sections other pages rely on still exist
  FRONT-DOOR-DUP-01        no two bullets in one list link the same target
  FRONT-DOOR-GENERATED-01  generated reader files the README links are tracked
                           in git (and, with --freshness, are current)

Usage:
  front_door_audit.py --root .               # fast checks; exit 1 on findings
  front_door_audit.py --root . --freshness   # also run the generator -check targets
  front_door_audit.py --root . --edition-tracks-date   # edition must be today's date
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

README = "README.md"
START_HERE = "START_HERE.md"
ANNOUNCEMENT = "implementation/adoption/ANNOUNCEMENT.md"
FIT = "implementation/adoption/FIT_SITUATIONS.md"
PREAMBLE = "core_00_preamble.md"

# Pages that must carry the edition string.
EDITION_PAGES = (
    README,
    "AGENTS.md",
    "llms.txt",
    "docs/index.md",
    ANNOUNCEMENT,
    "CONTRIBUTING.md",
)
# Pages that state whether the corpus is pre-release.
STATUS_PAGES = (*EDITION_PAGES, START_HERE)
# Pages whose chapter, article and tool claims are checked.
CLAIM_PAGES = (README, START_HERE, "AGENTS.md", "docs/index.md", ANNOUNCEMENT, "CONTRIBUTING.md")
LINK_PAGES = (README, START_HERE, "AGENTS.md", "docs/index.md", ANNOUNCEMENT, "CONTRIBUTING.md")
POINTER_REQUIRED = {
    README: (START_HERE,),
    START_HERE: (README,),
    "AGENTS.md": (README, START_HERE),
    "llms.txt": (README, START_HERE),
    "docs/index.md": (README, START_HERE),
    ANNOUNCEMENT: (README, START_HERE),
}
# Anchors other pages (and the announcement) rely on.
REQUIRED_SECTIONS = {
    README: (
        "edition",
        "reading-paths",
        "quick-find",
        "the-full-text",
        "implementation-files",
        "is-this-in-effect",
        "binding-vs-support",
        "authorship",
        "license",
        "read-in-your-language",
    ),
    START_HERE: (
        "pre-release-status",
        "two-modes",
        "fit-tests",
        "ranked-situations",
        "honest-non-fits",
    ),
}
GENERATED_LINKED = (
    "doc_architecture/generated/rights_floor_sheet.md",
    "doc_architecture/generated/plain_terms_edition.md",
    "doc_architecture/generated/human_definition_lookup.md",
    "implementation/PRINT_PACK.md",
)
FRESHNESS_TARGETS = (
    "plain-terms-edition-check",
    "reader-accessibility-check",
    "print-pack-check",
    "pages-corpus-index-check",
)

EDITION_RE = re.compile(r"SC-Corpus-\d{4}\.\d{2}\.\d{2}(?:\.\d+)?")
README_EDITION_RE = re.compile(r"\*\*Corpus edition\*\*\s*\|\s*`?(SC-Corpus-[\d.]+)`?")
README_EFFECTIVE_RE = re.compile(r"\*\*Effective date\*\*\s*\|\s*(\d{4}-\d{2}-\d{2})")
README_STATUS_RE = re.compile(r"\*\*Status\*\*\s*\|\s*(.+)")
EFFECTIVE_IN_TEXT_RE = re.compile(r"effective\s+(\d{4}-\d{2}-\d{2})", re.I)

NUMBER_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20,
}
ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}


def read(root: Path, rel: str) -> str | None:
    path = root / rel
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def roman_to_int(value: str) -> int:
    total = 0
    for index, char in enumerate(value):
        current = ROMAN[char]
        nxt = ROMAN.get(value[index + 1], 0) if index + 1 < len(value) else 0
        total += -current if current < nxt else current
    return total


def to_number(token: str) -> int | None:
    token = token.strip().lower()
    if token.isdigit():
        return int(token)
    return NUMBER_WORDS.get(token)


def normalize(text: str) -> str:
    text = re.sub(r"[*_`“”\"]", "", text)
    text = text.replace("’", "'")
    return re.sub(r"\s+", " ", text).strip().lower()


def code_free(text: str) -> str:
    """Drop fenced code blocks (they hold sample copy, not live claims)."""
    return re.sub(r"```.*?```", "", text, flags=re.S)


# --- checks ---------------------------------------------------------------


def check_edition(root: Path, tracks_date: date | None = None) -> list[str]:
    errors: list[str] = []
    readme = read(root, README)
    if readme is None:
        return [f"{README}: missing (FRONT-DOOR-EDITION-01)"]
    edition_match = README_EDITION_RE.search(readme)
    effective_match = README_EFFECTIVE_RE.search(readme)
    if not edition_match or not effective_match:
        return [f"{README}: edition table lacks 'Corpus edition' or 'Effective date' (FRONT-DOOR-EDITION-01)"]
    edition, effective = edition_match.group(1), effective_match.group(1)
    label_date = re.fullmatch(r"SC-Corpus-(\d{4})\.(\d{2})\.(\d{2})", edition)
    if label_date and "-".join(label_date.groups()) != effective:
        errors.append(
            f"{README}: edition {edition} does not carry the effective date {effective} (FRONT-DOOR-EDITION-02)"
        )
    if tracks_date is not None and effective != tracks_date.isoformat():
        errors.append(
            f"{README}: until the announcement the edition is the current date ({tracks_date.isoformat()}), "
            f"but it is {edition} (effective {effective}); run `make edition-bump` (FRONT-DOOR-EDITION-03)"
        )
    for rel in EDITION_PAGES:
        text = read(root, rel)
        if text is None:
            errors.append(f"{rel}: missing (FRONT-DOOR-EDITION-01)")
            continue
        found = set(EDITION_RE.findall(text))
        if not found:
            errors.append(f"{rel}: does not state the edition {edition} (FRONT-DOOR-EDITION-01)")
        for value in sorted(found - {edition}):
            errors.append(f"{rel}: edition {value} differs from README {edition} (FRONT-DOOR-EDITION-01)")
        for date in sorted(set(EFFECTIVE_IN_TEXT_RE.findall(text)) - {effective}):
            errors.append(f"{rel}: effective date {date} differs from README {effective} (FRONT-DOOR-EDITION-01)")
    index_text = read(root, "implementation/steward_owner_clock_index.json")
    if index_text is not None:
        try:
            index = json.loads(index_text)
        except json.JSONDecodeError:
            index = {}
        pinned = index.get("pinned_to_edition")
        if pinned and pinned != edition:
            errors.append(
                f"implementation/steward_owner_clock_index.json: pinned_to_edition {pinned} "
                f"differs from README {edition} (FRONT-DOOR-EDITION-01)"
            )
        index_effective = index.get("edition_effective")
        if index_effective and index_effective != effective:
            errors.append(
                f"implementation/steward_owner_clock_index.json: edition_effective {index_effective} "
                f"differs from README {effective} (FRONT-DOOR-EDITION-01)"
            )
    return errors


def mentions_pre_release(text: str) -> bool:
    return bool(re.search(r"pre-?release", text, re.I))


def check_status(root: Path) -> list[str]:
    readme = read(root, README) or ""
    status = README_STATUS_RE.search(readme)
    readme_pre = bool(status and mentions_pre_release(status.group(1)))
    errors: list[str] = []
    for rel in STATUS_PAGES:
        text = read(root, rel)
        if text is None:
            continue
        if mentions_pre_release(text) != readme_pre:
            word = "does not mention" if readme_pre else "still mentions"
            errors.append(
                f"{rel}: {word} pre-release, but the README edition table "
                f"{'says' if readme_pre else 'does not say'} pre-release (FRONT-DOOR-STATUS-01)"
            )
    return errors


def core_chapter_count(root: Path) -> int:
    numbers = [
        int(m.group(1))
        for path in root.glob("core_*.md")
        if (m := re.match(r"core_(\d{2})_", path.name))
    ]
    return max(numbers) if numbers else 0


def check_chapters(root: Path) -> list[str]:
    count = core_chapter_count(root)
    if not count:
        return ["no core_NN_*.md files found (FRONT-DOOR-CHAPTERS-01)"]
    errors: list[str] = []
    words = "|".join(NUMBER_WORDS)
    range_re = re.compile(
        rf"Chapters?\s+(?:1|One)\s*(?:–|—|-|to|through)\s*(\d+|{words})\b", re.I
    )
    count_re = re.compile(rf"Preamble and ({words}|\d+) chapters", re.I)
    for rel in CLAIM_PAGES:
        text = read(root, rel)
        if text is None:
            continue
        text = re.sub(r"[ \t]*\n[ \t]*", " ", text)
        for match in range_re.finditer(text):
            upper = to_number(match.group(1))
            if upper != count:
                errors.append(
                    f"{rel}: '{match.group(0)}' but the core has {count} chapters "
                    f"(highest core_{count:02d}_*) (FRONT-DOOR-CHAPTERS-01)"
                )
        for match in count_re.finditer(text):
            if to_number(match.group(1)) != count:
                errors.append(
                    f"{rel}: '{match.group(0)}' but the core has {count} chapters (FRONT-DOOR-CHAPTERS-01)"
                )
    return errors


def article_numerals(root: Path) -> list[int]:
    found: set[int] = set()
    for path in sorted(root.glob("core_06_rights_part_*.md")):
        for match in re.finditer(r"^#{1,6}\s+Article\s+([IVXL]+)\b", path.read_text(encoding="utf-8"), re.M):
            found.add(roman_to_int(match.group(1)))
    return sorted(found)


def check_articles(root: Path) -> list[str]:
    numerals = article_numerals(root)
    if not numerals:
        return ["no Article headings found in core_06_rights_part_*.md (FRONT-DOOR-ARTICLES-01)"]
    errors: list[str] = []
    count, top = len(numerals), max(numerals)
    if numerals != list(range(1, top + 1)):
        missing = sorted(set(range(1, top + 1)) - set(numerals))
        errors.append(f"Rights Floor Article numerals are not consecutive; missing {missing} (FRONT-DOOR-ARTICLES-01)")
    count_re = re.compile(r"\b(\d+)\s+articles\b", re.I)
    range_re = re.compile(r"Articles?\s+I\s*(?:–|—|-|to|through)\s*([IVXL]+)\b")
    for rel in CLAIM_PAGES:
        text = read(root, rel)
        if text is None:
            continue
        text = re.sub(r"[ \t]*\n[ \t]*", " ", text)
        for match in count_re.finditer(text):
            if int(match.group(1)) != count:
                errors.append(
                    f"{rel}: '{match.group(0)}' but the Rights Floor has {count} Articles (FRONT-DOOR-ARTICLES-01)"
                )
        for match in range_re.finditer(text):
            if roman_to_int(match.group(1)) != top:
                errors.append(
                    f"{rel}: '{match.group(0)}' but the last Rights Floor Article is {top} (FRONT-DOOR-ARTICLES-01)"
                )
    return errors


def check_counts(root: Path) -> list[str]:
    registry_text = read(root, "ai_corpus/indexes/definition_registry.json")
    if registry_text is None:
        return []
    try:
        registry = json.loads(registry_text)
    except json.JSONDecodeError:
        return []
    total = registry.get("definition_count") or len(registry.get("definitions", []))
    if not total:
        return []
    errors: list[str] = []
    claim_re = re.compile(r"more than (\w+) hundred", re.I)
    for rel in CLAIM_PAGES:
        text = read(root, rel)
        if text is None:
            continue
        flat = re.sub(r"\s+", " ", text)
        for match in claim_re.finditer(flat):
            hundreds = to_number(match.group(1))
            if hundreds is not None and hundreds * 100 >= total:
                errors.append(
                    f"{rel}: '{match.group(0)}' definitions but the registry holds {total} (FRONT-DOOR-COUNT-01)"
                )
    return errors


def check_languages(root: Path) -> list[str]:
    errors: list[str] = []
    readme = read(root, README)
    if readme is None:
        return []
    trans = root / "translations"
    on_disk = (
        {p.name for p in trans.iterdir() if p.is_dir() and (p / "README.md").is_file()}
        if trans.is_dir()
        else set()
    )
    in_readme = set(re.findall(r"\]\(translations/([A-Za-z-]+)/README\.md\)", readme))
    for code in sorted(on_disk - in_readme):
        errors.append(f"{README}: language bar lacks translations/{code}/ (FRONT-DOOR-LANG-01)")
    for code in sorted(in_readme - on_disk):
        errors.append(f"{README}: language bar links translations/{code}/ which has no README.md (FRONT-DOOR-LANG-01)")
    index = read(root, "translations/README.md")
    if index is None:
        errors.append("translations/README.md: missing (FRONT-DOOR-LANG-01)")
    else:
        in_index = set(re.findall(r"\]\(([A-Za-z-]+)/README\.md\)", index))
        for code in sorted(on_disk - in_index):
            errors.append(f"translations/README.md: table lacks {code}/ (FRONT-DOOR-LANG-01)")
        for code in sorted(in_index - on_disk):
            errors.append(f"translations/README.md: table links {code}/ which has no README.md (FRONT-DOOR-LANG-01)")
    flat = normalize(readme)
    if "the english text is the one that counts" not in flat:
        errors.append(f"{README}: the 'English text is the one that counts' statement is missing (FRONT-DOOR-LANG-01)")
    return errors


def preamble_questions(root: Path) -> list[str]:
    text = read(root, PREAMBLE) or ""
    return [
        m.group(1).strip()
        for m in re.finditer(r"^\s*[12]\.\s+\*\*(Does it [^*\n]+\?)\*\*\s*$", text, re.M)
    ]


def check_questions(root: Path) -> list[str]:
    questions = preamble_questions(root)
    if len(questions) != 2:
        return [
            f"{PREAMBLE}: expected the two numbered '**Does it ...?**' questions, found {len(questions)}; "
            "update tools/front_door_audit.py if the Preamble layout changed on purpose (FRONT-DOOR-QUESTIONS-01)"
        ]
    errors: list[str] = []
    for rel in (README, ANNOUNCEMENT):
        text = read(root, rel)
        if text is None:
            continue
        flat = normalize(text)
        for number, question in enumerate(questions, start=1):
            if normalize(question) not in flat:
                errors.append(
                    f"{rel}: does not quote Question {number} exactly as the Preamble words it: "
                    f"'{question}' (FRONT-DOOR-QUESTIONS-01)"
                )
    return errors


def makefile_targets(root: Path) -> set[str]:
    text = read(root, "Makefile") or ""
    targets = set(re.findall(r"^([A-Za-z0-9_.-]+)\s*:(?!=)", text, re.M))
    for block in re.findall(r"^\.PHONY:(.*?)(?:\n\n|\Z)", text, re.M | re.S):
        targets.update(block.replace("\\\n", " ").split())
    return targets


def check_make(root: Path) -> list[str]:
    targets = makefile_targets(root)
    errors: list[str] = []
    make_re = re.compile(r"`make\s+([a-z0-9][a-z0-9_-]*(?:\s+[a-z0-9][a-z0-9_-]*)*)\s*`")
    tool_re = re.compile(r"\btools/[A-Za-z0-9_]+\.py\b")
    for rel in CLAIM_PAGES:
        text = read(root, rel)
        if text is None:
            continue
        for match in make_re.finditer(text):
            for target in match.group(1).split():
                if target not in targets:
                    errors.append(f"{rel}: names `make {target}` but the Makefile has no such target (FRONT-DOOR-MAKE-01)")
        for tool in sorted(set(tool_re.findall(text))):
            if not (root / tool).is_file():
                errors.append(f"{rel}: names {tool} which does not exist (FRONT-DOOR-MAKE-01)")
    return errors


LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def check_links(root: Path) -> list[str]:
    errors: list[str] = []
    for rel in LINK_PAGES:
        text = read(root, rel)
        if text is None:
            continue
        base = (root / rel).parent
        for lineno, line in enumerate(code_free(text).splitlines(), start=1):
            for match in LINK_RE.finditer(line):
                target = match.group(1)
                if target.startswith(("http://", "https://", "mailto:", "#", "//")):
                    continue
                path = unquote(target.split("#", 1)[0])
                if not path:
                    continue
                if not (base / path).exists():
                    errors.append(f"{rel}:{lineno}: link target {path} does not exist (FRONT-DOOR-LINK-01)")
    return errors


def section_text(text: str, heading_re: str) -> str:
    """Return the body under the first heading matching heading_re, up to the next same-or-higher heading."""
    match = re.search(rf"^(#{{1,6}})\s+{heading_re}.*$", text, re.M)
    if not match:
        return ""
    level = len(match.group(1))
    rest = text[match.end():]
    end = re.search(rf"^#{{1,{level}}}\s", rest, re.M)
    return rest[: end.start()] if end else rest


def check_fit(root: Path) -> list[str]:
    start = read(root, START_HERE)
    fit = read(root, FIT)
    if start is None or fit is None:
        return []
    errors: list[str] = []
    # Ranked situations: START_HERE item n must link FIT heading 4.n.
    fit_ids: dict[int, set[str]] = {}
    fit_lines = fit.splitlines()
    for index, line in enumerate(fit_lines):
        match = re.match(r"^###\s+4\.(\d+)\s+(.+?)\s*$", line)
        if not match:
            continue
        ids = {slugify(f"4.{match.group(1)} {match.group(2)}")}
        back = index - 1
        while back >= 0 and (not fit_lines[back].strip() or fit_lines[back].lstrip().startswith("<a id=")):
            ids.update(re.findall(r'<a id="([^"]+)"', fit_lines[back]))
            back -= 1
        fit_ids[int(match.group(1))] = ids
    fit_slugs = fit_ids
    ranked = section_text(start, r"\d+\.\s+Where it fits best")
    linked = re.findall(
        r"^\s*(\d+)\.\s+\[[^\]]*\]\(implementation/adoption/FIT_SITUATIONS\.md#([^)\s]+)\)", ranked, re.M
    )
    if not fit_slugs:
        errors.append(f"{FIT}: no '### 4.n' ranked-situation headings found (FRONT-DOOR-FIT-01)")
    else:
        if len(linked) != len(fit_slugs):
            errors.append(
                f"{START_HERE}: ranked list has {len(linked)} items but {FIT} §4 has {len(fit_slugs)} (FRONT-DOOR-FIT-01)"
            )
        for number, fragment in linked:
            expected = fit_slugs.get(int(number))
            if expected is None:
                errors.append(f"{START_HERE}: ranked item {number} has no §4.{number} in {FIT} (FRONT-DOOR-FIT-01)")
            elif fragment not in expected:
                errors.append(
                    f"{START_HERE}: ranked item {number} links #{fragment} but {FIT} §4.{number} is "
                    f"#{sorted(expected)[0]} (FRONT-DOOR-FIT-01)"
                )
    # Non-fits: same number of bullets.
    start_bullets = len(re.findall(r"^- ", section_text(start, r"\d+\.\s+Where it does not fit"), re.M))
    fit_bullets = len(re.findall(r"^- ", section_text(fit, r"5\.\s+Honest non-fits"), re.M))
    if start_bullets != fit_bullets:
        errors.append(
            f"{START_HERE}: 'Where it does not fit' has {start_bullets} bullets but {FIT} §5 has {fit_bullets} (FRONT-DOOR-FIT-01)"
        )
    return errors


def check_authors(root: Path) -> list[str]:
    license_text = read(root, "LICENSE")
    if license_text is None:
        return []
    match = re.search(r"Attribution:\s*(.+?)\s+and collaborating AI models\s*\(([^)]*)\)", license_text)
    if not match:
        return ["LICENSE: 'Attribution: <name> and collaborating AI models (<models>)' line not found (FRONT-DOOR-AUTHOR-01)"]
    names = [match.group(1).strip()] + [part.strip().split()[0] for part in match.group(2).split(",") if part.strip()]
    errors: list[str] = []
    # README and docs/index.md list everyone; CONTRIBUTING repeats only the
    # corpus-level attribution line, which names the author.
    for rel, required in ((README, names), ("docs/index.md", names), ("CONTRIBUTING.md", names[:1])):
        text = read(root, rel)
        if text is None:
            continue
        for name in required:
            if name.lower() not in text.lower():
                errors.append(f"{rel}: authorship omits '{name}', which LICENSE names (FRONT-DOOR-AUTHOR-01)")
    return errors


def check_pointers(root: Path) -> list[str]:
    errors: list[str] = []
    for rel, required in POINTER_REQUIRED.items():
        text = read(root, rel)
        if text is None:
            errors.append(f"{rel}: missing (FRONT-DOOR-POINTER-01)")
            continue
        for target in required:
            if target not in text and Path(target).name not in text:
                errors.append(f"{rel}: does not point to {target} (FRONT-DOOR-POINTER-01)")
    return errors


def slugify(title: str) -> str:
    title = re.sub(r"<[^>]+>", "", title)
    title = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", title)
    title = re.sub(r"[`*_]", "", title).lower()
    title = "".join(c for c in title if c.isalnum() or c in " -")
    return re.sub(r"\s", "-", title.strip())


def heading_slugs_and_ids(text: str) -> set[str]:
    found = set(re.findall(r'<a\s+id="([^"]+)"', text))
    for match in re.finditer(r"^#{1,6}\s+(.+?)\s*$", text, re.M):
        found.add(slugify(match.group(1)))
    return found


def check_sections(root: Path) -> list[str]:
    errors: list[str] = []
    for rel, anchors in REQUIRED_SECTIONS.items():
        text = read(root, rel)
        if text is None:
            continue
        present = heading_slugs_and_ids(text)
        for anchor in anchors:
            if anchor not in present:
                errors.append(f"{rel}: required section #{anchor} is gone; other pages link to it (FRONT-DOOR-SECTIONS-01)")
    return errors


def check_duplicates(root: Path) -> list[str]:
    errors: list[str] = []
    for rel in (README, START_HERE):
        text = read(root, rel)
        if text is None:
            continue
        lines = text.splitlines()
        block: dict[str, int] = {}
        for lineno, line in enumerate(lines, start=1):
            if re.match(r"^\s*[-*]\s", line):
                targets = {
                    m.group(1).split("#", 1)[0] + ("#" + m.group(1).split("#", 1)[1] if "#" in m.group(1) else "")
                    for m in LINK_RE.finditer(line)
                    if not m.group(1).startswith(("http", "mailto:"))
                }
                for target in targets:
                    if target in block:
                        errors.append(
                            f"{rel}:{lineno}: link to {target} repeats the bullet at line {block[target]} "
                            "in the same list (FRONT-DOOR-DUP-01)"
                        )
                    else:
                        block[target] = lineno
            elif not line.strip() or line.lstrip().startswith(("<", "|")):
                continue
            else:
                block = {}
    return errors


def git_tracked(root: Path, rel: str) -> bool | None:
    if not (root / ".git").exists():
        return None
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "--error-unmatch", rel],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def check_generated(root: Path) -> list[str]:
    errors: list[str] = []
    readme = read(root, README) or ""
    for rel in GENERATED_LINKED:
        if rel not in readme:
            errors.append(f"{README}: no longer links {rel} (FRONT-DOOR-GENERATED-01)")
        if not (root / rel).is_file():
            errors.append(f"{rel}: missing; the README links it (FRONT-DOOR-GENERATED-01)")
            continue
        tracked = git_tracked(root, rel)
        if tracked is False:
            errors.append(f"{rel}: linked from the README but not tracked in git (FRONT-DOOR-GENERATED-01)")
    return errors


def check_freshness(root: Path) -> list[str]:
    errors: list[str] = []
    for target in FRESHNESS_TARGETS:
        result = subprocess.run(["make", "-C", str(root), target], capture_output=True, text=True)
        if result.returncode != 0:
            tail = " ".join((result.stdout + result.stderr).strip().splitlines()[-3:])
            errors.append(f"make {target} failed: {tail} (FRONT-DOOR-GENERATED-01)")
    return errors


CHECKS = (
    check_edition,
    check_status,
    check_chapters,
    check_articles,
    check_counts,
    check_languages,
    check_questions,
    check_make,
    check_links,
    check_fit,
    check_authors,
    check_pointers,
    check_sections,
    check_duplicates,
    check_generated,
)


def audit(root: Path, freshness: bool = False, tracks_date: date | None = None) -> list[str]:
    errors: list[str] = []
    for check in CHECKS:
        errors.extend(check(root, tracks_date) if check is check_edition else check(root))
    if freshness:
        errors.extend(check_freshness(root))
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--freshness", action="store_true", help="also run the generated-file -check make targets")
    parser.add_argument(
        "--edition-tracks-date",
        action="store_true",
        help="require the edition to be today's date (until the announcement)",
    )
    parser.add_argument("--today", help="override today's date, YYYY-MM-DD (for tests)")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    tracks_date = None
    if args.edition_tracks_date:
        if args.today:
            tracks_date = date.fromisoformat(args.today)
        else:
            from bump_edition import today

            tracks_date = today()
    errors = audit(root, freshness=args.freshness, tracks_date=tracks_date)
    if errors:
        print(f"FAIL: {len(errors)} front-door divergence(s)")
        for error in errors:
            print(error)
        return 1
    print("PASS: the front doors match the corpus (edition, chapters, articles, languages, questions, targets, fit list, authorship).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
