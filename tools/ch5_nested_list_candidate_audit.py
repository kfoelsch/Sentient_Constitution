#!/usr/bin/env python3
"""Advisory ranking of packed list items for nested-bullet rewrites.

Chapter Five: In-scope / assessment / failure bullets (and unlabeled
assessment continuation lines). Chapter Six: labeled operative run-ins
(``**Label:**`` / ``**Label** —``) and packed covers/includes lists.
Chapter Seven: labeled walkthrough and record bullets (same packing
signals as Chapter Six). Chapter Eight: labeled record, custody, and
measurement bullets (same packing signals as Chapters Six and Seven).
Chapter Nine: labeled integration, lock, remedy, and routing bullets
(same packing signals as Chapters Six through Eight). Chapter Ten:
labeled designation, safeguard, and named-pattern bullets (same packing
signals as Chapters Six through Nine). Chapter Eleven: labeled routing,
forum-family, escalation, and support bullets (same packing signals as
Chapters Six through Ten). Chapter Twelve: labeled legitimacy,
stewardship, collective-choice, and role bullets (same packing signals as
Chapters Six through Eleven). Chapter Thirteen: labeled non-regression,
amendment-validity, anti-evasion, and layer-scope bullets (same packing
signals as Chapters Six through Twelve). The Preamble and Chapters One
through Four, Fourteen, Fifteen, and Sixteen use the same conservative
packing signals over their numbered source files.

Finds items that pack a parallel list into one sentence and have no nested
child bullets yet. Default is advisory: print ranked candidates and exit 0.
Use ``--strict`` only when an operator wants a non-zero exit on hits.

This is a candidate finder, not a duty. Existing nesting gates
(``corpus_markdown_audit.check_oec_intro_sublist_nesting``, Article IX in
``prose_continuity_audit``) still lock lists that are already nested.

Rules: CH0-NEST-CANDIDATE through CH16-NEST-CANDIDATE (by selected
chapter) in
tools/architecture/rule_registry.json.
Legacy chapter-specific names: CH5-NEST-CANDIDATE / CH6-NEST-CANDIDATE /
CH7-NEST-CANDIDATE / CH8-NEST-CANDIDATE / CH9-NEST-CANDIDATE /
CH10-NEST-CANDIDATE /
CH11-NEST-CANDIDATE / CH12-NEST-CANDIDATE /
CH13-NEST-CANDIDATE in

Run:

    make ch5-nested-list-candidates
    make ch6-nested-list-candidates
    make ch7-nested-list-candidates
    make ch8-nested-list-candidates
    make ch9-nested-list-candidates
    make ch10-nested-list-candidates
    make ch11-nested-list-candidates
    make ch12-nested-list-candidates
    make ch13-nested-list-candidates
    make ch14-nested-list-candidates
    make ch15-nested-list-candidates
    make ch16-nested-list-candidates
    python3 tools/ch5_nested_list_candidate_audit.py --root . --chapter 16
    python3 tools/ch5_nested_list_candidate_audit.py --root . --file core_05_band_accountability.md
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_APEX, CH5_DEFS  # noqa: E402

CH0_PARTS: tuple[str, ...] = ("core_00_preamble.md",)

CH1_PARTS: tuple[str, ...] = (
    "core_01_a_values_principles.md",
    "core_01_b_interaction_interpretation.md",
    "core_01_c_stewardship_capacity_principles.md",
)

CH2_PARTS: tuple[str, ...] = ("core_02_definition_structure.md",)

CH3_PARTS: tuple[str, ...] = ("core_03_definition_integrity.md",)

CH4_PARTS: tuple[str, ...] = ("core_04_burden_traceability_verification.md",)

CH6_RIGHTS: tuple[str, ...] = (
    "core_06_rights_part_a.md",
    "core_06_rights_part_b.md",
    "core_06_rights_part_c.md",
    "core_06_rights_part_d.md",
)

CH7_PARTS: tuple[str, ...] = (
    "core_07_a_system_alignment_certification_evaluation.md",
    "core_07_b_system_alignment_certification_record_process.md",
)

CH8_PARTS: tuple[str, ...] = ("core_08_standing_assessment.md",)

CH9_PARTS: tuple[str, ...] = ("core_09_standing_integration.md",)

CH10_PARTS: tuple[str, ...] = (
    "core_10_a_misconduct_designation.md",
    "core_10_b_misconduct_pattern_applications.md",
)

CH11_PARTS: tuple[str, ...] = ("core_11_forum.md",)

CH12_PARTS: tuple[str, ...] = ("core_12_governance.md",)

CH13_PARTS: tuple[str, ...] = ("core_13_non_regression.md",)

CH14_PARTS: tuple[str, ...] = ("core_14_expansion_supremacy.md",)

CH15_PARTS: tuple[str, ...] = ("core_15_amendment_ratification.md",)

CH16_PARTS: tuple[str, ...] = ("core_16_incorporation.md",)

SUPPORTED_CHAPTERS: tuple[int, ...] = tuple(range(17))
WORDS_ONLY_SKIP_CHAPTERS: frozenset[int] = frozenset(
    set(range(17)) - {5}
)

LIST_RE = re.compile(r"^([ \t]*)([-*]|\d+\.)\s+(.*)$")
HEADING_RE = re.compile(r"^(#{3,5})\s+(.+)$")
ASSESSMENT_LABEL_RE = re.compile(
    r"^([ \t]+)\*\*(Primary|Secondary|Tertiary) assessment:\*\*(.*)$"
)
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
HTML_ANCHOR_RE = re.compile(r"<a id=\"[^\"]+\"></a>")
CODE_SPAN_RE = re.compile(r"`[^`]+`")

GUIDEPOST_HEADERS = frozenset(
    {
        "**What it is**",
        "**How to measure and assess**",
        "**What must hold**",
    }
)

TARGET_ROLES = frozenset(
    {
        "in-scope",
        "primary-failure",
        "secondary-failure",
        "tertiary-failure",
        "primary-assessment",
        "secondary-assessment",
        "tertiary-assessment",
        "depends-on",
    }
)

COLON_INTRO_RE = re.compile(
    r"(?:"
    r"including:"
    r"|this includes:"
    r"|these include:"
    r"|examples include:"
    r"|causes include:"
    r"|covers:"
    r"|covering:"
    r"|that capacity supports:"
    r"|it is non-compliant to:"
    r"|it is also non-compliant to:"
    r"|non-compliant practices include:"
    r"|must include:"
    r"|may include:"
    r"|check:"
    r"|look for:"
    r"|apply:"
    r"|identify:"
    r"|separate:"
    r"|as follows:"
    r"|the following:"
    r"|must:"
    r")\s*$",
    re.IGNORECASE,
)

INCLUDING_LIST_RE = re.compile(
    r"\b(?:including|covers|covering|comprises|may include|this includes|"
    r"these include|must include|examples include|causes include|includes)\b"
    r"[^.\n]*,[^.\n]*,[^.\n]*\b(?:and|or)\b",
    re.IGNORECASE,
)

POINTER_RE = re.compile(
    r"^(?:Chapter Five pointer|canonical (?:owner|concept|mechanics)|"
    r"Axis mechanics:|operational requirements:)",
    re.IGNORECASE,
)

LABELED_RE = re.compile(
    r"^\*\*(?:([^*]+?)(?::|—)\*\*|([^*]+)\*\*\s*(?::|—)\s*)"
)
TETRAD_OR_AIM_ROLES = frozenset(
    {
        "flourishing",
        "continuity",
        "participation",
        "oversight",
        "accountability",
        "timeliness",
    }
)

ROLE_RES: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("in-scope", re.compile(r"^\*\*In scope(?:\s*—[^:]+)?:\*\*")),
    ("out-of-scope", re.compile(r"^\*\*Out of scope:\*\*")),
    ("depends-on", re.compile(r"^\*\*Depends on:\*\*")),
    ("primary-failure", re.compile(r"^\*\*Primary failure:\*\*")),
    ("secondary-failure", re.compile(r"^\*\*Secondary failure:\*\*")),
    ("tertiary-failure", re.compile(r"^\*\*Tertiary failure:\*\*")),
    ("primary-measure", re.compile(r"^\*\*Primary measure:\*\*")),
    ("secondary-measure", re.compile(r"^\*\*Secondary measure:\*\*")),
    ("tertiary-measure", re.compile(r"^\*\*Tertiary measure:\*\*")),
    ("primary-assessment", re.compile(r"^\*\*Primary assessment:\*\*")),
    ("secondary-assessment", re.compile(r"^\*\*Secondary assessment:\*\*")),
    ("tertiary-assessment", re.compile(r"^\*\*Tertiary assessment:\*\*")),
)

DEFAULT_MIN_SCORE = 8
PREVIEW_CHARS = 180


@dataclass(frozen=True)
class Candidate:
    file: str
    line: int
    heading: str
    role: str
    score: int
    kinds: tuple[str, ...]
    words: int
    recommendation: str
    preview: str


@dataclass
class ScanUnit:
    line: int
    indent: int
    heading: str
    body: str
    has_child: bool
    role: str = ""
    kinds: list[str] = field(default_factory=list)
    score: int = 0
    words: int = 0
    recommendation: str = ""


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument(
        "--file",
        action="append",
        default=[],
        help="Limit to one or more relative paths (repeatable).",
    )
    parser.add_argument(
        "--chapter",
        action="append",
        type=int,
        choices=SUPPORTED_CHAPTERS,
        default=[],
        help="Chapter to scan (repeatable: 0 through 16). Default 5 when --file is omitted.",
    )
    parser.add_argument(
        "--apex",
        action="store_true",
        help="Also scan Chapter Five aim and Tetrad-leg apex files (chapter 5 only).",
    )
    parser.add_argument(
        "--min-score",
        type=int,
        default=DEFAULT_MIN_SCORE,
        help=f"Minimum candidate score to print (default {DEFAULT_MIN_SCORE}).",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=0,
        help="If >0, print only the top N candidates.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Print candidates as JSON.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit 1 when any candidate meets --min-score. Default is advisory.",
    )
    return parser.parse_args(argv)


def visual_indent(prefix: str) -> int:
    return len(prefix.expandtabs(4))


def leading_indent(raw: str) -> int:
    match = re.match(r"^[ \t]*", raw)
    return visual_indent(match.group(0) if match else "")


def strip_md(text: str) -> str:
    text = LINK_RE.sub(r"\1", text)
    text = BOLD_RE.sub(r"\1", text)
    text = HTML_ANCHOR_RE.sub(" ", text)
    text = CODE_SPAN_RE.sub(" ", text)
    return text


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9']+", strip_md(text)))


def sentence_count(text: str) -> int:
    return len(re.findall(r"[.!?]", strip_md(text)))


def detect_role(body: str) -> str:
    stripped = body.lstrip()
    for role, pattern in ROLE_RES:
        if pattern.match(stripped):
            return role
    labeled = LABELED_RE.match(stripped)
    if labeled:
        raw_label = labeled.group(1) or labeled.group(2) or ""
        slug = re.sub(r"[^a-z0-9]+", "-", raw_label.strip().lower()).strip("-")
        return slug or "labeled"
    return "other"


def _is_packable_role(role: str) -> bool:
    if role in TARGET_ROLES:
        return True
    if role in {"other", "out-of-scope"} or role.endswith("-measure"):
        return False
    return True


def chapter_from_rel(rel: str) -> int | None:
    name = Path(rel).name if rel else ""
    if name.startswith("core_00_"):
        return 0
    if name.startswith("core_01_"):
        return 1
    if name.startswith("core_02_"):
        return 2
    if name.startswith("core_03_"):
        return 3
    if name.startswith("core_04_"):
        return 4
    if name.startswith("core_13_"):
        return 13
    if name.startswith("core_14_"):
        return 14
    if name.startswith("core_15_"):
        return 15
    if name.startswith("core_16_"):
        return 16
    if name.startswith("core_12_"):
        return 12
    if name.startswith("core_11_"):
        return 11
    if name.startswith("core_10_"):
        return 10
    if name.startswith("core_09_"):
        return 9
    if name.startswith("core_08_"):
        return 8
    if name.startswith("core_07_"):
        return 7
    if name.startswith("core_06_"):
        return 6
    if name.startswith("core_05_"):
        return 5
    return None


RULE_ID_BY_CHAPTER: dict[int, str] = {
    0: "CH0-NEST-CANDIDATE",
    1: "CH1-NEST-CANDIDATE",
    2: "CH2-NEST-CANDIDATE",
    3: "CH3-NEST-CANDIDATE",
    4: "CH4-NEST-CANDIDATE",
    5: "CH5-NEST-CANDIDATE",
    6: "CH6-NEST-CANDIDATE",
    7: "CH7-NEST-CANDIDATE",
    8: "CH8-NEST-CANDIDATE",
    9: "CH9-NEST-CANDIDATE",
    10: "CH10-NEST-CANDIDATE",
    11: "CH11-NEST-CANDIDATE",
    12: "CH12-NEST-CANDIDATE",
    13: "CH13-NEST-CANDIDATE",
    14: "CH14-NEST-CANDIDATE",
    15: "CH15-NEST-CANDIDATE",
    16: "CH16-NEST-CANDIDATE",
}


def rule_ids_for(paths: list[Path], chapters: list[int]) -> tuple[str, ...]:
    found: set[int] = set(chapters)
    for path in paths:
        chapter = chapter_from_rel(path.name)
        if chapter is not None:
            found.add(chapter)
    if not found:
        found.add(5)
    return tuple(
        RULE_ID_BY_CHAPTER[chapter]
        for chapter in SUPPORTED_CHAPTERS
        if chapter in found
    )


def is_guidepost_header(body: str) -> bool:
    return body.strip() in GUIDEPOST_HEADERS


def _skip_structural(stripped: str) -> bool:
    return stripped.startswith(
        ("#", "---", "</details>", "<details", "<a id=", "<summary", "</summary")
    )


def _collect_follow_on(
    lines: list[str],
    start: int,
    *,
    min_child_indent: int,
    min_continue_indent: int,
    stop_on_assessment: bool,
) -> tuple[list[str], bool, int]:
    """Return (continuation bodies, has_child, index of first unused line)."""
    continuations: list[str] = []
    has_child = False
    j = start
    while j < len(lines):
        raw = lines[j]
        stripped = raw.strip()
        if not stripped:
            j += 1
            continue
        if stripped.startswith("```"):
            break
        if _skip_structural(stripped):
            break
        if stop_on_assessment and ASSESSMENT_LABEL_RE.match(raw):
            break
        list_match = LIST_RE.match(raw)
        if list_match:
            child_indent = visual_indent(list_match.group(1))
            if child_indent >= min_child_indent:
                has_child = True
            break
        if leading_indent(raw) >= min_continue_indent:
            continuations.append(stripped)
            j += 1
            continue
        break
    return continuations, has_child, j


def iter_scan_units(lines: list[str]) -> list[ScanUnit]:
    units: list[ScanUnit] = []
    in_fence = False
    in_details = False
    heading = ""
    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            i += 1
            continue
        if in_fence:
            i += 1
            continue
        if stripped.startswith("<details"):
            in_details = True
            i += 1
            continue
        if stripped.startswith("</details"):
            in_details = False
            i += 1
            continue
        if in_details:
            i += 1
            continue
        heading_match = HEADING_RE.match(raw)
        if heading_match:
            heading = heading_match.group(2).strip()
            i += 1
            continue

        assessment_match = ASSESSMENT_LABEL_RE.match(raw)
        if assessment_match:
            indent = visual_indent(assessment_match.group(1))
            body = stripped
            continuations, has_child, _ = _collect_follow_on(
                lines,
                i + 1,
                min_child_indent=indent,
                min_continue_indent=indent,
                stop_on_assessment=False,
            )
            if continuations:
                body = " ".join([body, *continuations])
            units.append(
                ScanUnit(
                    line=i + 1,
                    indent=indent,
                    heading=heading,
                    body=body,
                    has_child=has_child,
                    role=detect_role(body),
                )
            )
            i += 1
            continue

        list_match = LIST_RE.match(raw)
        if list_match:
            indent = visual_indent(list_match.group(1))
            body = list_match.group(3)
            continuations, has_child, _ = _collect_follow_on(
                lines,
                i + 1,
                min_child_indent=indent + 1,
                min_continue_indent=indent + 1,
                stop_on_assessment=True,
            )
            if continuations:
                body = " ".join([body, *continuations])
            units.append(
                ScanUnit(
                    line=i + 1,
                    indent=indent,
                    heading=heading,
                    body=body,
                    has_child=has_child,
                    role=detect_role(body),
                )
            )
            i += 1
            continue
        i += 1
    return units


def _kinds_and_score(unit: ScanUnit) -> tuple[list[str], int, str]:
    body = unit.body.strip()
    plain = strip_md(body)
    kinds: list[str] = []
    score = 0

    if COLON_INTRO_RE.search(plain):
        kinds.append("colon-intro")
        score += 8

    semicolons = plain.count(";")
    if semicolons >= 2:
        kinds.append(f"semicolons:{semicolons}")
        score += semicolons * 3 if semicolons >= 3 else 4

    if INCLUDING_LIST_RE.search(plain):
        kinds.append("including-list")
        score += 8

    commas = plain.count(",")
    if (
        re.search(r"\bit is(?: also)? non-compliant to\b", plain, re.I)
        and re.search(r"\bor\b", plain, re.I)
        and (commas >= 3 or semicolons >= 2)
    ):
        kinds.append("or-chain")
        score += 6

    sentences = sentence_count(body)
    packable = _is_packable_role(unit.role)
    if sentences >= 3 and packable:
        kinds.append(f"sentences:{sentences}")
        score += (sentences - 2) * 2

    words = word_count(body)
    if packable and words >= 55:
        kinds.append(f"words:{words}")
        score += 3
    if words >= 80:
        if not any(k.startswith("words:") for k in kinds):
            kinds.append(f"words:{words}")
        score += 4
    if words >= 110:
        score += 4

    if "colon-intro" in kinds:
        recommendation = "Nest the list this line introduces."
    elif any(k.startswith("semicolons:") and int(k.split(":")[1]) >= 3 for k in kinds):
        recommendation = "Split the semicolon list into nested bullets."
    elif "including-list" in kinds:
        recommendation = "Lift the including-list into nested bullets."
    elif "or-chain" in kinds:
        recommendation = "Split the non-compliance modes into nested bullets."
    elif any(k.startswith("sentences:") for k in kinds):
        recommendation = "Split stacked duties into nested labeled children."
    else:
        recommendation = "Consider nested bullets if the items are parallel tests."

    return kinds, score, recommendation


def _should_skip(unit: ScanUnit) -> bool:
    if unit.has_child:
        return True
    if is_guidepost_header(unit.body):
        return True
    if unit.role.endswith("-measure"):
        return True
    if POINTER_RE.match(strip_md(unit.body).lstrip()):
        return True
    words = word_count(unit.body)
    if unit.role == "out-of-scope" and words < 50 and unit.body.count(";") < 3:
        return True
    if words < 12 and not COLON_INTRO_RE.search(strip_md(unit.body)):
        return True
    return False


def _mild_including_only(kinds: list[str]) -> bool:
    packing = [kind for kind in kinds if not kind.startswith("words:")]
    return packing == ["including-list"]


def score_units(
    units: list[ScanUnit], *, min_score: int, chapter: int | None = None
) -> list[Candidate]:
    candidates: list[Candidate] = []
    for unit in units:
        if _should_skip(unit):
            continue
        kinds, score, recommendation = _kinds_and_score(unit)
        unit.kinds = kinds
        unit.score = score
        unit.words = word_count(unit.body)
        unit.recommendation = recommendation
        if score < min_score or not kinds:
            continue
        packing = [kind for kind in kinds if not kind.startswith("words:")]
        if (
            chapter in WORDS_ONLY_SKIP_CHAPTERS
            and unit.role == "other"
            and not packing
        ):
            continue
        if (
            unit.role in TETRAD_OR_AIM_ROLES
            and _mild_including_only(kinds)
            and unit.words < 55
        ):
            continue
        preview = strip_md(unit.body).replace("\n", " ")
        if len(preview) > PREVIEW_CHARS:
            preview = preview[: PREVIEW_CHARS - 1].rstrip() + "…"
        candidates.append(
            Candidate(
                file="",
                line=unit.line,
                heading=unit.heading or "(file head)",
                role=unit.role,
                score=score,
                kinds=tuple(kinds),
                words=unit.words,
                recommendation=recommendation,
                preview=preview,
            )
        )
    candidates.sort(key=lambda item: (-item.score, item.line))
    return candidates


def scan_lines(
    lines: list[str],
    *,
    rel: str = "",
    min_score: int = DEFAULT_MIN_SCORE,
    chapter: int | None = None,
) -> list[Candidate]:
    units = iter_scan_units(lines)
    resolved_chapter = chapter if chapter is not None else chapter_from_rel(rel)
    candidates = score_units(units, min_score=min_score, chapter=resolved_chapter)
    if not rel:
        return candidates
    return [
        Candidate(
            file=rel,
            line=item.line,
            heading=item.heading,
            role=item.role,
            score=item.score,
            kinds=item.kinds,
            words=item.words,
            recommendation=item.recommendation,
            preview=item.preview,
        )
        for item in candidates
    ]


def scan_text(
    text: str,
    *,
    rel: str = "",
    min_score: int = DEFAULT_MIN_SCORE,
    chapter: int | None = None,
) -> list[Candidate]:
    return scan_lines(
        text.splitlines(), rel=rel, min_score=min_score, chapter=chapter
    )


def selected_chapters(args: argparse.Namespace) -> list[int]:
    if args.chapter:
        return list(dict.fromkeys(args.chapter))
    if args.file:
        found: list[int] = []
        for name in args.file:
            chapter = chapter_from_rel(name)
            if chapter is not None and chapter not in found:
                found.append(chapter)
        return found
    return [5]


def resolve_targets(root: Path, args: argparse.Namespace) -> list[Path]:
    if args.file:
        names = tuple(args.file)
    else:
        chapters = selected_chapters(args)
        names_list: list[str] = []
        chapter_parts = {
            0: CH0_PARTS,
            1: CH1_PARTS,
            2: CH2_PARTS,
            3: CH3_PARTS,
            4: CH4_PARTS,
            5: CH5_DEFS,
            6: CH6_RIGHTS,
            7: CH7_PARTS,
            8: CH8_PARTS,
            9: CH9_PARTS,
            10: CH10_PARTS,
            11: CH11_PARTS,
            12: CH12_PARTS,
            13: CH13_PARTS,
            14: CH14_PARTS,
            15: CH15_PARTS,
            16: CH16_PARTS,
        }
        for chapter in chapters:
            names_list.extend(chapter_parts.get(chapter, ()))
        if 5 in chapters and args.apex:
            names_list.extend(CH5_APEX)
        names = tuple(names_list)
    paths: list[Path] = []
    for name in names:
        path = root / name
        if path.is_file():
            paths.append(path)
        else:
            print(f"warning: missing {name}", file=sys.stderr)
    return paths


def format_text(
    candidates: list[Candidate],
    *,
    min_score: int,
    rule_ids: tuple[str, ...] = ("CH5-NEST-CANDIDATE",),
) -> str:
    rules = ", ".join(rule_ids) if rule_ids else "CH5-NEST-CANDIDATE"
    lines = [
        "Advisory nested-list candidates (not a regression gate).",
        f"Rule {rules}; min-score {min_score}.",
        "",
    ]
    if not candidates:
        lines.append(f"No nested-list candidates at or above min-score {min_score}.")
        return "\n".join(lines)
    for item in candidates:
        loc = f"{item.file}:{item.line}" if item.file else f"L{item.line}"
        kinds = ", ".join(item.kinds)
        lines.append(
            f"{loc}  score={item.score}  words={item.words}  "
            f"[{item.heading}]  {item.role}  ({kinds})"
        )
        lines.append(f"  {item.preview}")
        lines.append(f"  → {item.recommendation}")
        lines.append("")
    lines.append(f"{len(candidates)} candidate(s). Review by hand before nesting.")
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    paths = resolve_targets(root, args)
    if not paths:
        print("No nested-list candidate files found to scan.", file=sys.stderr)
        return 2

    candidates: list[Candidate] = []
    for path in paths:
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        candidates.extend(scan_text(text, rel=rel, min_score=args.min_score))

    candidates.sort(key=lambda item: (-item.score, item.file, item.line))
    if args.top > 0:
        candidates = candidates[: args.top]

    rule_ids = rule_ids_for(paths, selected_chapters(args))
    if args.as_json:
        print(json.dumps([asdict(item) for item in candidates], indent=2))
    else:
        print(
            format_text(candidates, min_score=args.min_score, rule_ids=rule_ids),
            end="",
        )

    if args.strict and candidates:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
