#!/usr/bin/env python3
"""Report possible missing Chapter One principle references in selected core files.

This is an advisory keyword search, not a compliance audit. It extracts the
numbered section headings in Chapter One as the initial principle inventory,
then reports paragraphs in selected sections that use distinctive heading
terms where that section has no Chapter One source link. Review every result in
context; a match does not establish that a reference is required.

Examples:

    python3 tools/principle_check.py --chapter-range 2-9
    python3 tools/principle_check.py --chapter-range 2-9 --through-file core_09.005_system_alignment_certification_record_process.md
    python3 tools/principle_check.py --file core_08.000_functional_independence_separation_of_duties.md --file core_09.000_system_alignment_certification_evaluation.md
    python3 tools/principle_check.py --list-principles
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

CH1_FILES = (
    "core_01.000_values_principles.md",
    "core_01.005_interaction_interpretation.md",
    "core_01.010_stewardship_capacity_principles.md",
)
CORE_FILE_RE = re.compile(r"^core_(\d{2})\.")
HEADING_RE = re.compile(r"^#{3,5}\s+(\d+(?:\.\d+)*)(?:\.)?\s+(.+?)\s*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HTML_TAG_RE = re.compile(r"<[^>]+>")
WORD_RE = re.compile(r"[a-z][a-z0-9-]*", re.IGNORECASE)
STOP_WORDS = frozenset(
    "a about above after against all also an and any are as at be because been before "
    "being below between both but by can could did do does doing down during each either "
    "else few for from further had has have having he her here hers herself him himself "
    "his how i if in into is it its itself just may me might more most must my myself "
    "neither no nor not of off on once only or other our ours ourselves out over own same "
    "she should so some such than that the their theirs them themselves then there these "
    "they this those through to too under until up very was we were what when where which "
    "while who whom why will with would you your yours yourself yourselves".split()
)
GENERIC_TERMS = frozenset(
    "alignment aligned constitutional constitution system systems principle principles "
    "section role layer process requirement requirements standard standards rule rules "
    "scope application integrated integration design effect effects basis level levels "
    "part parts structure outcome outcomes control controls measure measures term terms "
    "definition definitions implementation information responsibility discipline duty duties "
    "rights major good depth line".split()
)
TERM_FAMILIES = {
    "stewardship": "steward",
    "trustworthiness": "trust",
    "proxies": "proxy",
    "systemic": "system",
    "systems": "system",
    "aligned": "align",
    "alignment": "align",
    "accessible": "access",
    "accessibility": "access",
    "governance": "govern",
    "governed": "govern",
    "governing": "govern",
    "assessment": "assess",
    "evaluations": "evaluate",
    "evaluation": "evaluate",
}
NON_PRINCIPLE_HEADINGS = frozenset({"1", "2", "8", "13", "15", "20"})
PRINCIPLE_ALIASES: dict[str, tuple[str, ...]] = {
    "2.1": ("safety and truth", "non-negotiable constraints"),
    "3": ("lived wellbeing", "flourishing outcomes"),
    "4": ("harm prevention", "material harm", "systemic risk"),
    "5": ("epistemic integrity", "evidence integrity", "selective reporting"),
    "6": ("justified reliance", "system reliance", "reliance integrity"),
    "7": ("meaningful agency", "self-determination", "exit rights"),
    "9": (
        "shared infrastructure", "shared foundations", "dependency and resource flows",
        "productive capacity", "shared system capacity",
    ),
    "10": ("self-healing recovery", "failure recovery", "degraded operation"),
    "11": ("market concentration", "market power", "anti-concentration", "anti-domination"),
    "12": ("whole-system evaluation", "systemic scope"),
    "15.1": ("bypass by label", "requirements follow the act", "substance over labels"),
    "15.1.1": ("anti-segmentation", "joint assessment", "fragmented assessment"),
    "16": ("distributed understanding", "document at action", "stewardship capacity"),
    "17": ("material stewardship", "stewardship role", "consequential stewardship"),
    "18": ("authorized governance", "governance structure", "authority and answerability"),
    "19": ("incentive alignment", "system capture", "misalignment correction"),
    "19.2": ("proxy divergence", "proxy-based decisions", "convenient proxies"),
    "19.4": ("misalignment correction", "capture response", "system capture response"),
}


@dataclass(frozen=True)
class Principle:
    section: str
    title: str
    filename: str
    terms: tuple[str, ...]
    aliases: tuple[str, ...]


def distinct_concepts(words: list[str]) -> set[str]:
    return {TERM_FAMILIES.get(word, word) for word in words}


def principle_inventory(root: Path) -> list[Principle]:
    inventory: list[Principle] = []
    for filename in CH1_FILES:
        path = root / filename
        for line in path.read_text(encoding="utf-8").splitlines():
            heading = HEADING_RE.match(line)
            if not heading:
                continue
            section, title = heading.groups()
            # Introductory, organizational, and integration headings are not
            # independently searchable principles in this first pass.
            if section in NON_PRINCIPLE_HEADINGS or section.count(".") > 1:
                continue
            words = [word.lower() for word in WORD_RE.findall(title)]
            terms = tuple(
                dict.fromkeys(
                    word for word in words
                    if word not in STOP_WORDS and word not in GENERIC_TERMS and len(word) > 2
                )
            )
            if terms:
                inventory.append(
                    Principle(section, title, filename, terms, PRINCIPLE_ALIASES.get(section, ()))
                )
    return inventory


def markdown_paragraphs(text: str):
    """Yield (starting line, paragraph, nearest heading) outside code/HTML."""
    lines = text.splitlines()
    chunk: list[str] = []
    start = 1
    section = "(before first heading)"
    in_fence = False
    in_html = False

    def emit():
        nonlocal chunk
        if chunk:
            result = (start, "\n".join(chunk), section)
            chunk = []
            return result
        return None

    for number, line in enumerate(lines, 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if "<details" in line or "<summary" in line:
            in_html = True
        if in_html:
            if "</details>" in line:
                in_html = False
            continue
        heading = re.match(r"^\s*#{1,6}\s+(.+?)\s*$", line)
        if heading:
            result = emit()
            if result:
                yield result
            section = heading.group(1)
            continue
        if line.strip():
            if not chunk:
                start = number
            chunk.append(line)
        elif chunk:
            result = emit()
            if result:
                yield result
    result = emit()
    if result:
        yield result


def sections_with_ch1_references(text: str) -> set[str]:
    """Count Chapter One citations in each section, including collapsed widgets."""
    section = "(before first heading)"
    referenced: set[str] = set()
    for line in text.splitlines():
        heading = re.match(r"^\s*#{1,6}\s+(.+?)\s*$", line)
        if heading:
            section = heading.group(1)
        if any("core_01." in target for target in LINK_RE.findall(line)) or re.search(
            r"\bChapter One\s+(?:§{1,2}|section\s+)\d", line, re.IGNORECASE
        ):
            referenced.add(section)
    return referenced


def selected_files(root: Path, args: argparse.Namespace) -> list[Path]:
    core_files = sorted(
        path for path in root.glob("core_*.md") if CORE_FILE_RE.match(path.name)
    )
    if args.file:
        missing = [name for name in args.file if not (root / name).is_file()]
        if missing:
            raise ValueError("file(s) not found: " + ", ".join(missing))
        return [root / name for name in args.file]

    if args.chapter_range:
        first, last = args.chapter_range
        selected = [
            path for path in core_files
            if first <= int(CORE_FILE_RE.match(path.name).group(1)) <= last
        ]
    else:
        selected = [path for path in core_files if int(CORE_FILE_RE.match(path.name).group(1)) != 1]

    if args.through_file:
        through = root / args.through_file
        if through not in core_files:
            raise ValueError(f"--through-file is not a numbered core file: {args.through_file}")
        selected = [path for path in selected if path.name <= through.name]
    return selected


def parse_range(value: str) -> tuple[int, int]:
    match = re.fullmatch(r"(\d+)(?:-(\d+))?", value)
    if not match:
        raise argparse.ArgumentTypeError("expected a chapter number or inclusive range such as 2-9")
    first = int(match.group(1))
    last = int(match.group(2) or first)
    if first > last:
        raise argparse.ArgumentTypeError("range start must not exceed range end")
    return first, last


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--chapter-range", type=parse_range, help="inclusive chapter range, e.g. 2-9")
    parser.add_argument("--file", action="append", help="specific core filename; repeat to select several")
    parser.add_argument("--through-file", help="with --chapter-range, stop at this file, inclusive")
    parser.add_argument("--list-principles", action="store_true", help="print the extracted Chapter One inventory")
    args = parser.parse_args()
    root = args.root.resolve()

    try:
        inventory = principle_inventory(root)
        if args.list_principles:
            for item in inventory:
                print(f"§{item.section}  {item.title} [{item.filename}]")
            print(f"{len(inventory)} Chapter One headings in the initial search inventory")
            return 0
        files = selected_files(root, args)
    except (OSError, ValueError) as error:
        parser.error(str(error))

    hits = 0
    print("Advisory only: keyword matches are review candidates, not findings.")
    print(f"Principle headings: {len(inventory)} | files checked: {len(files)}")
    for path in files:
        text = path.read_text(encoding="utf-8")
        paragraphs = list(markdown_paragraphs(text))
        sections_with_principle_refs = sections_with_ch1_references(text)
        for line_number, paragraph, section in paragraphs:
            if path.name in CH1_FILES:
                continue
            # A section that already points to Chapter One may still omit a
            # second relevant principle, but detecting that reliably requires
            # more context than this first-pass keyword check has.
            if section in sections_with_principle_refs:
                continue
            paragraph_lines = paragraph.splitlines()
            if all(line.lstrip().startswith("|") for line in paragraph_lines):
                continue
            if any(re.match(r"\s*#{1,6}\s", line) for line in paragraph_lines):
                continue
            clean = HTML_TAG_RE.sub(" ", LINK_RE.sub(" ", paragraph))
            lowered = clean.lower()
            paragraph_candidates: list[str] = []
            for principle in inventory:
                matched = [term for term in principle.terms if re.search(rf"\b{re.escape(term)}\b", lowered)]
                phrase_words = [word.lower() for word in WORD_RE.findall(principle.title)]
                phrase = " ".join(phrase_words)
                meaningful_phrase = [
                    word for word in phrase_words
                    if word not in STOP_WORDS and word not in GENERIC_TERMS and len(word) > 2
                ]
                title_phrase_match = len(meaningful_phrase) >= 2 and phrase in lowered
                matched_aliases = [alias for alias in principle.aliases if alias in lowered]
                # A full heading phrase is a strong signal. Otherwise require
                # at least two distinctive title words to avoid broad hits.
                if title_phrase_match or matched_aliases or len(distinct_concepts(matched)) >= 2:
                    evidence_parts = matched_aliases or matched
                    evidence = ", ".join(evidence_parts) if evidence_parts else "title phrase"
                    label = f"§{principle.section} {principle.title} [{evidence}]"
                    if label not in paragraph_candidates:
                        paragraph_candidates.append(label)
            if paragraph_candidates:
                excerpt = re.sub(r"\s+", " ", paragraph)
                if len(excerpt) > 240:
                    excerpt = excerpt[:237].rstrip() + "..."
                print(
                    f"{path.name}:{line_number}: possible references: "
                    f"{'; '.join(paragraph_candidates)}: {excerpt}"
                )
                hits += 1
    print(f"Candidate matches: {hits}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
