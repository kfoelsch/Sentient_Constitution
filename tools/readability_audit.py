#!/usr/bin/env python3
"""Deterministic readability audit for constitutional project markdown files."""

from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import sys
from dataclasses import dataclass

_TOOLS = pathlib.Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from subarticle_gloss_audit import subarticle_gloss_errors  # noqa: E402


DEFAULT_INCLUDE_GLOB = "**/*.md"
DEFAULT_EXCLUDE_DIRS = {
    ".git",
    ".cursor",
    "archive",
    "evidence",
    "agent-transcripts",
    "__pycache__",
}
DEFAULT_EXCLUDE_FILES = {
    "MEMLOG.md",
    "TODO.md",
}

SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
SYLLABLE_GROUP_RE = re.compile(r"[aeiouy]+", re.IGNORECASE)

# Common dense/abstract governance terms that often increase reading load when stacked.
DENSE_TERMS = {
    "posture",
    "constitutional",
    "legitimacy",
    "stewardship",
    "governance",
    "ratification",
    "adoption",
    "regressive",
    "classification",
    "enforceability",
    "contestability",
    "traceability",
}


@dataclass(frozen=True)
class SentenceFinding:
    file: str
    line: int
    kind: str
    detail: str
    sentence: str


@dataclass(frozen=True)
class FileStats:
    file: str
    sentence_count: int
    word_count: int
    syllable_count: int
    grade_level: float
    long_sentences: int
    findings_count: int


@dataclass(frozen=True)
class Candidate:
    file: str
    line: int
    score: int
    primary_kind: str
    sentence: str
    recommendation: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default=".",
        help="Workspace root path. Defaults to current directory.",
    )
    parser.add_argument(
        "--include-glob",
        default=DEFAULT_INCLUDE_GLOB,
        help="Glob for files to include in the audit.",
    )
    parser.add_argument(
        "--scope",
        nargs="*",
        default=[],
        help="Optional explicit list of files to scan (overrides glob discovery).",
    )
    parser.add_argument(
        "--max-grade",
        type=float,
        default=15.0,
        help="Target maximum Flesch-Kincaid grade level.",
    )
    parser.add_argument(
        "--long-sentence-words",
        type=int,
        default=25,
        help="Word threshold for long sentence warnings.",
    )
    parser.add_argument(
        "--very-long-sentence-words",
        type=int,
        default=35,
        help="Word threshold for very long sentence warnings.",
    )
    parser.add_argument(
        "--write-evidence",
        action="store_true",
        help="Write a dated audit artifact under evidence/<date>/.",
    )
    parser.add_argument(
        "--date",
        default=dt.date.today().isoformat(),
        help="Date used in evidence path and report header (YYYY-MM-DD).",
    )
    parser.add_argument(
        "--top-candidates",
        type=int,
        default=0,
        help="If >0, print a ranked top-N rewrite candidate list and exit.",
    )
    parser.add_argument(
        "--write-candidates-evidence",
        action="store_true",
        help="Write a dated top-candidates report under evidence/<date>/.",
    )
    parser.add_argument(
        "--with-subarticle-gloss",
        action="store_true",
        help=(
            "After the readability scan, run the Chapter Nine sub-article plain-terms "
            "gate (same logic as tools/subarticle_gloss_audit.py) and append results."
        ),
    )
    return parser.parse_args()


def discover_markdown_files(root: pathlib.Path, include_glob: str) -> list[pathlib.Path]:
    candidates: list[pathlib.Path] = []
    for path in root.glob(include_glob):
        if not path.is_file():
            continue
        if should_exclude(path.relative_to(root)):
            continue
        candidates.append(path)
    return sorted(candidates)


def should_exclude(rel_path: pathlib.PurePath) -> bool:
    return (
        any(part in DEFAULT_EXCLUDE_DIRS for part in rel_path.parts)
        or rel_path.name in DEFAULT_EXCLUDE_FILES
    )


def count_syllables(word: str) -> int:
    lowered = word.lower()
    groups = SYLLABLE_GROUP_RE.findall(lowered)
    if not groups:
        return 1
    count = len(groups)
    if lowered.endswith("e") and count > 1 and not lowered.endswith(("le", "ye")):
        count -= 1
    return max(1, count)


def split_sentences_with_lines(text: str) -> list[tuple[int, str]]:
    results: list[tuple[int, str]] = []
    for line_no, raw_line in enumerate(text.splitlines(), start=1):
        stripped = raw_line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        stripped = re.sub(r"^[-*]\s+", "", stripped)
        stripped = re.sub(r"^\d+\.\s+", "", stripped)
        sentences = SENTENCE_SPLIT_RE.split(stripped)
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence:
                results.append((line_no, sentence))
    return results


def word_list(text: str) -> list[str]:
    return WORD_RE.findall(text)


def fk_grade_level(words: int, sentences: int, syllables: int) -> float:
    if words == 0 or sentences == 0:
        return 0.0
    return (0.39 * (words / sentences)) + (11.8 * (syllables / words)) - 15.59


def detect_sentence_findings(
    rel_path: str,
    line: int,
    sentence: str,
    long_sentence_words: int,
    very_long_sentence_words: int,
) -> list[SentenceFinding]:
    findings: list[SentenceFinding] = []
    words = word_list(sentence)
    word_count = len(words)
    if word_count >= very_long_sentence_words:
        findings.append(
            SentenceFinding(
                file=rel_path,
                line=line,
                kind="very-long-sentence",
                detail=f"{word_count} words; split into 2-4 shorter sentences.",
                sentence=sentence,
            )
        )
    elif word_count >= long_sentence_words:
        findings.append(
            SentenceFinding(
                file=rel_path,
                line=line,
                kind="long-sentence",
                detail=f"{word_count} words; consider splitting into shorter sentences.",
                sentence=sentence,
            )
        )

    semicolon_count = sentence.count(";")
    if semicolon_count >= 2:
        findings.append(
            SentenceFinding(
                file=rel_path,
                line=line,
                kind="clause-chain",
                detail=f"{semicolon_count} semicolons; convert to a list or separate sentences.",
                sentence=sentence,
            )
        )

    # Front-loaded abstraction patterns often reduce readability.
    if ":" in sentence:
        left, right = sentence.split(":", 1)
        left_words = word_list(left)
        right_words = word_list(right)
        abstract_lead = len(left_words) >= 8 and any(
            term in left.lower() for term in ("defines", "establishes", "sets", "requires")
        )
        concrete_tail = any(
            marker in right.lower() for marker in ("who", "what", "when", "where", "how")
        )
        if abstract_lead and concrete_tail and len(right_words) >= 6:
            findings.append(
                SentenceFinding(
                    file=rel_path,
                    line=line,
                    kind="abstraction-first",
                    detail=(
                        "Definition appears before concrete explanation; invert order "
                        "or use a short lead sentence plus list."
                    ),
                    sentence=sentence,
                )
            )

    dense_terms = sum(1 for w in words if w.lower() in DENSE_TERMS)
    if word_count >= 18 and dense_terms >= 4:
        findings.append(
            SentenceFinding(
                file=rel_path,
                line=line,
                kind="jargon-density",
                detail=f"{dense_terms} dense terms in one sentence; simplify wording or split.",
                sentence=sentence,
            )
        )

    return findings


def analyze_file(
    root: pathlib.Path,
    path: pathlib.Path,
    long_sentence_words: int,
    very_long_sentence_words: int,
) -> tuple[FileStats, list[SentenceFinding]]:
    text = path.read_text(encoding="utf-8")
    rel_path = str(path.relative_to(root))
    sentences = split_sentences_with_lines(text)

    all_words = word_list(text)
    total_words = len(all_words)
    total_syllables = sum(count_syllables(word) for word in all_words)

    findings: list[SentenceFinding] = []
    long_sentences = 0
    for line_no, sentence in sentences:
        sentence_words = len(word_list(sentence))
        if sentence_words >= long_sentence_words:
            long_sentences += 1
        findings.extend(
            detect_sentence_findings(
                rel_path=rel_path,
                line=line_no,
                sentence=sentence,
                long_sentence_words=long_sentence_words,
                very_long_sentence_words=very_long_sentence_words,
            )
        )

    stats = FileStats(
        file=rel_path,
        sentence_count=max(1, len(sentences)),
        word_count=total_words,
        syllable_count=total_syllables,
        grade_level=fk_grade_level(total_words, max(1, len(sentences)), total_syllables),
        long_sentences=long_sentences,
        findings_count=len(findings),
    )
    return stats, findings


def make_report(
    run_date: str,
    max_grade: float,
    stats: list[FileStats],
    findings: list[SentenceFinding],
) -> str:
    total_words = sum(item.word_count for item in stats)
    total_sentences = sum(item.sentence_count for item in stats)
    total_syllables = sum(item.syllable_count for item in stats)
    overall_grade = fk_grade_level(total_words, max(1, total_sentences), total_syllables)
    files_over_grade = [item for item in stats if item.grade_level > max_grade]
    high_signal_findings = sorted(
        findings,
        key=lambda f: (severity_rank(f.kind), f.file, f.line),
    )

    lines: list[str] = []
    lines.append(f"# Readability Audit - {run_date}")
    lines.append("")
    lines.append("## Targets")
    lines.append(f"- Maximum grade target: `{max_grade:.1f}`")
    lines.append(f"- Files scanned: `{len(stats)}`")
    lines.append(f"- Overall estimated grade: `{overall_grade:.2f}`")
    lines.append(f"- Files over target: `{len(files_over_grade)}`")
    lines.append("")
    lines.append("## File Scores")
    lines.append("| File | Grade | Long Sentences | Findings |")
    lines.append("|---|---:|---:|---:|")
    for item in sorted(stats, key=lambda x: x.grade_level, reverse=True):
        lines.append(
            f"| `{item.file}` | {item.grade_level:.2f} | {item.long_sentences} | {item.findings_count} |"
        )
    lines.append("")
    lines.append("## High-Signal Findings")

    if high_signal_findings:
        lines.append("| File | Line | Type | Detail |")
        lines.append("|---|---:|---|---|")
        for finding in high_signal_findings:
            lines.append(
                f"| `{finding.file}` | {finding.line} | `{finding.kind}` | {finding.detail} |"
            )
        lines.append("")
        lines.append("## Context Snippets")
        for finding in high_signal_findings[:150]:
            lines.append(
                f"- `{finding.file}:{finding.line}` `{finding.kind}` - {finding.sentence}"
            )
    else:
        lines.append("- No readability findings triggered by current thresholds.")

    lines.append("")
    lines.append("## Result")
    passed = (overall_grade <= max_grade) and (len(files_over_grade) == 0) and (len(findings) == 0)
    lines.append("- `PASS`" if passed else "- `FAIL`")
    return "\n".join(lines) + "\n"


def severity_points(kind: str) -> int:
    if kind == "very-long-sentence":
        return 8
    if kind == "abstraction-first":
        return 7
    if kind == "clause-chain":
        return 6
    if kind == "jargon-density":
        return 4
    if kind == "long-sentence":
        return 2
    return 1


def recommendation_for_kind(kind: str) -> str:
    if kind == "very-long-sentence":
        return "Split into 2-4 short sentences (target 12-20 words each)."
    if kind == "abstraction-first":
        return "Start with concrete who/what/how, then define terms."
    if kind == "clause-chain":
        return "Convert semicolon chain into a bulleted list."
    if kind == "jargon-density":
        return "Replace dense terms with plain language and examples."
    if kind == "long-sentence":
        return "Trim qualifiers and split into two shorter sentences."
    return "Simplify wording and shorten sentence length."


def build_top_candidates(findings: list[SentenceFinding], limit: int) -> list[Candidate]:
    sentence_map: dict[tuple[str, int, str], list[str]] = {}
    for finding in findings:
        key = (finding.file, finding.line, finding.sentence)
        sentence_map.setdefault(key, []).append(finding.kind)

    candidates: list[Candidate] = []
    for (file, line, sentence), kinds in sentence_map.items():
        points = sum(severity_points(kind) for kind in kinds)
        points += min(len(word_list(sentence)) // 10, 8)
        primary_kind = sorted(kinds, key=lambda kind: severity_rank(kind))[0]
        candidates.append(
            Candidate(
                file=file,
                line=line,
                score=points,
                primary_kind=primary_kind,
                sentence=sentence,
                recommendation=recommendation_for_kind(primary_kind),
            )
        )

    ranked = sorted(
        candidates,
        key=lambda item: (-item.score, item.file, item.line),
    )
    return ranked[:limit]


def candidates_report(run_date: str, candidates: list[Candidate], limit: int) -> str:
    lines: list[str] = []
    lines.append(f"# Readability Top Candidates - {run_date}")
    lines.append("")
    lines.append(f"## Ranked Rewrite Queue (Top {limit})")
    if not candidates:
        lines.append("- No candidates found.")
        return "\n".join(lines) + "\n"
    lines.append("| Rank | File | Line | Score | Trigger | Recommendation |")
    lines.append("|---:|---|---:|---:|---|---|")
    for idx, item in enumerate(candidates, start=1):
        lines.append(
            f"| {idx} | `{item.file}` | {item.line} | {item.score} | `{item.primary_kind}` | {item.recommendation} |"
        )
    lines.append("")
    lines.append("## Sentence Context")
    for idx, item in enumerate(candidates, start=1):
        lines.append(f"- `{idx}. {item.file}:{item.line}` - {item.sentence}")
    lines.append("")
    return "\n".join(lines) + "\n"


def severity_rank(kind: str) -> int:
    if kind == "very-long-sentence":
        return 0
    if kind == "abstraction-first":
        return 1
    if kind == "clause-chain":
        return 2
    if kind == "jargon-density":
        return 3
    return 4


def write_evidence(root: pathlib.Path, run_date: str, report: str) -> pathlib.Path:
    evidence_dir = root / "evidence" / run_date
    evidence_dir.mkdir(parents=True, exist_ok=True)
    evidence_file = evidence_dir / f"READABILITY_AUDIT_{run_date}.md"
    evidence_file.write_text(report, encoding="utf-8")
    return evidence_file


def write_candidates_evidence(root: pathlib.Path, run_date: str, report: str) -> pathlib.Path:
    evidence_dir = root / "evidence" / run_date
    evidence_dir.mkdir(parents=True, exist_ok=True)
    evidence_file = evidence_dir / f"READABILITY_TOP_CANDIDATES_{run_date}.md"
    evidence_file.write_text(report, encoding="utf-8")
    return evidence_file


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve()

    if args.scope:
        files = [root / rel for rel in args.scope]
    else:
        files = discover_markdown_files(root, args.include_glob)

    missing = [str(path) for path in files if not path.exists()]
    if missing:
        raise SystemExit(f"Missing required files in scope: {', '.join(missing)}")
    if not files:
        raise SystemExit("No markdown files found for readability audit.")

    all_stats: list[FileStats] = []
    all_findings: list[SentenceFinding] = []
    for file_path in files:
        stats, findings = analyze_file(
            root=root,
            path=file_path,
            long_sentence_words=args.long_sentence_words,
            very_long_sentence_words=args.very_long_sentence_words,
        )
        all_stats.append(stats)
        all_findings.extend(findings)

    report = make_report(
        run_date=args.date,
        max_grade=args.max_grade,
        stats=all_stats,
        findings=all_findings,
    )

    gloss_errors: list[str] = []
    if args.with_subarticle_gloss and args.top_candidates <= 0:
        gloss_errors = subarticle_gloss_errors(root)
        gloss_lines = ["", "## Subarticle gloss audit (Chapter Nine, bundled)", ""]
        if gloss_errors:
            gloss_lines.append("- Result: `FAIL`")
            gloss_lines.extend(f"  - {e}" for e in gloss_errors)
        else:
            gloss_lines.append("- Result: `PASS`")
        report = report.rstrip() + "\n" + "\n".join(gloss_lines) + "\n"

    if args.top_candidates > 0:
        candidates = build_top_candidates(all_findings, args.top_candidates)
        candidate_text = candidates_report(args.date, candidates, args.top_candidates)
        if args.write_candidates_evidence:
            evidence_path = write_candidates_evidence(root, args.date, candidate_text)
            print(f"Wrote top-candidates report: {evidence_path}")
        else:
            print(candidate_text)
        return 1 if candidates else 0

    if args.write_evidence:
        evidence_path = write_evidence(root, args.date, report)
        print(f"Wrote evidence report: {evidence_path}")
    else:
        print(report)

    total_words = sum(item.word_count for item in all_stats)
    total_sentences = sum(item.sentence_count for item in all_stats)
    total_syllables = sum(item.syllable_count for item in all_stats)
    overall_grade = fk_grade_level(total_words, max(1, total_sentences), total_syllables)
    files_over_grade = any(item.grade_level > args.max_grade for item in all_stats)
    hard_findings = any(
        f.kind in {"very-long-sentence", "abstraction-first", "clause-chain"}
        for f in all_findings
    )
    readability_fail = overall_grade > args.max_grade or files_over_grade or hard_findings
    gloss_fail = bool(gloss_errors)
    return 1 if (readability_fail or gloss_fail) else 0


if __name__ == "__main__":
    sys.exit(main())
