#!/usr/bin/env python3
"""Advisory audit for jargon-heavy guidance prose in repository markdown files."""

from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import sys
from dataclasses import dataclass


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
WORD_RE = re.compile(r"[A-Za-z]+(?:-[A-Za-z]+)?")
CODE_SPAN_RE = re.compile(r"`[^`]+`")
LINK_RE = re.compile(r"\[[^\]]+\]\([^)]+\)")

NAVIGATION_VERBS = {
    "read",
    "see",
    "use",
}

META_TERMS = {
    "context",
    "explanation",
    "explanatory",
    "framing",
    "guidance",
    "note",
    "non-binding",
    "non-operative",
    "operative",
    "orientation",
    "overview",
    "reader",
}

ABSTRACT_TERMS = {
    "allocation",
    "architecture",
    "context",
    "explanatory",
    "extended",
    "framing",
    "guidance",
    "integrated",
    "interpretive",
    "jurisdiction",
    "materially",
    "narrative",
    "non-binding",
    "non-operative",
    "operative",
    "orientation",
}

ABSTRACT_SUFFIXES = ("tion", "sion", "ment", "ance", "ence", "ity")


@dataclass(frozen=True)
class PhraseRule:
    name: str
    pattern: re.Pattern[str]
    suggestion: str


PHRASE_RULES: tuple[PhraseRule, ...] = (
    PhraseRule(
        name="extended-narrative-context",
        pattern=re.compile(r"\bextended narrative context\b", re.IGNORECASE),
        suggestion="Prefer a simpler phrase such as 'longer explanation'.",
    ),
    PhraseRule(
        name="non-operative-explanatory-framing",
        pattern=re.compile(r"\bnon-operative explanatory framing\b", re.IGNORECASE),
        suggestion="Prefer a simpler phrase such as 'non-binding explanation'.",
    ),
)


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    rule: str
    detail: str
    text: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default=".",
        help="Workspace root path.",
    )
    parser.add_argument(
        "--include-glob",
        default=DEFAULT_INCLUDE_GLOB,
        help="Glob for markdown files to scan.",
    )
    parser.add_argument(
        "--scope",
        nargs="*",
        default=[],
        help="Optional explicit list of files to scan (overrides glob discovery).",
    )
    parser.add_argument(
        "--dense-sentence-words",
        type=int,
        default=12,
        help="Minimum words before dense guidance heuristic applies.",
    )
    parser.add_argument(
        "--dense-abstract-terms",
        type=int,
        default=4,
        help="Minimum abstract/jargon terms before dense guidance heuristic applies.",
    )
    parser.add_argument(
        "--write-evidence",
        action="store_true",
        help="Write a dated report under evidence/<date>/.",
    )
    parser.add_argument(
        "--date",
        default=dt.date.today().isoformat(),
        help="Date for evidence path (YYYY-MM-DD).",
    )
    return parser.parse_args()


def should_exclude(rel_path: pathlib.PurePath) -> bool:
    return (
        any(part in DEFAULT_EXCLUDE_DIRS for part in rel_path.parts)
        or rel_path.name in DEFAULT_EXCLUDE_FILES
    )


def discover_markdown_files(root: pathlib.Path, include_glob: str) -> list[pathlib.Path]:
    candidates: list[pathlib.Path] = []
    for path in root.glob(include_glob):
        if not path.is_file():
            continue
        if should_exclude(path.relative_to(root)):
            continue
        candidates.append(path)
    return sorted(candidates)


def load_text(path: pathlib.Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"Missing required file: {path}")


def normalize_sentence(text: str) -> str:
    cleaned = CODE_SPAN_RE.sub("", text)
    cleaned = LINK_RE.sub("", cleaned)
    cleaned = re.sub(r"<[^>]+>", "", cleaned)
    return cleaned.strip()


def iter_sentences(text: str) -> list[tuple[int, str]]:
    results: list[tuple[int, str]] = []
    in_fence = False

    for line_no, raw_line in enumerate(text.splitlines(), start=1):
        stripped = raw_line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not stripped:
            continue
        if stripped.startswith(("#", "|", ">")):
            continue

        working = re.sub(r"^[-*]\s+", "", stripped)
        working = re.sub(r"^\d+\.\s+", "", working)
        if not working:
            continue

        for sentence in SENTENCE_SPLIT_RE.split(working):
            sentence = normalize_sentence(sentence)
            if sentence:
                results.append((line_no, sentence))

    return results


def sentence_words(sentence: str) -> list[str]:
    return WORD_RE.findall(sentence)


def count_abstract_terms(words: list[str]) -> int:
    total = 0
    for word in words:
        lowered = word.lower()
        if lowered in ABSTRACT_TERMS:
            total += 1
            continue
        if lowered.endswith(ABSTRACT_SUFFIXES) and len(lowered) >= 8:
            total += 1
    return total


def meta_term_count(words: list[str]) -> int:
    return sum(1 for word in words if word.lower() in META_TERMS)


def navigation_verb_count(words: list[str]) -> int:
    return sum(1 for word in words if word.lower() in NAVIGATION_VERBS)


def scan_phrase_rules(rel_path: str, text: str) -> list[Finding]:
    findings: list[Finding] = []
    in_fence = False

    for idx, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not stripped:
            continue

        check_line = normalize_sentence(raw)

        for rule in PHRASE_RULES:
            if rule.pattern.search(check_line):
                findings.append(
                    Finding(
                        file=rel_path,
                        line=idx,
                        rule=rule.name,
                        detail=rule.suggestion,
                        text=stripped,
                    )
                )

    return findings


def scan_dense_guidance_sentences(
    rel_path: str,
    text: str,
    *,
    dense_sentence_words: int,
    dense_abstract_terms: int,
) -> list[Finding]:
    findings: list[Finding] = []

    for line_no, sentence in iter_sentences(text):
        words = sentence_words(sentence)
        if len(words) < dense_sentence_words:
            continue
        meta_count = meta_term_count(words)
        verb_count = navigation_verb_count(words)
        if meta_count < 2 and not (meta_count >= 1 and verb_count >= 1):
            continue

        abstract_count = count_abstract_terms(words)
        if abstract_count < dense_abstract_terms:
            continue

        findings.append(
            Finding(
                file=rel_path,
                line=line_no,
                rule="dense-guidance-sentence",
                detail=(
                    f"{len(words)} words and {abstract_count} abstract terms; "
                    "rewrite as a shorter note with everyday language."
                ),
                text=sentence,
            )
        )

    return findings


def report_markdown(run_date: str, scope: list[str], findings: list[Finding]) -> str:
    lines: list[str] = [
        f"# Plain language audit — {run_date}",
        "",
        "Rules:",
        "- **`extended-narrative-context`:** prefer a simpler pointer such as **longer explanation**.",
        "- **`non-operative-explanatory-framing`:** prefer **non-binding explanation**.",
        "- **`dense-guidance-sentence`:** flags meta/guidance sentences that stack abstract terms instead of plain words.",
        "",
        "## Scope",
    ]
    for file_path in scope:
        lines.append(f"- `{file_path}`")
    lines.extend(["", "## Findings"])
    if findings:
        lines.append("| File | Line | Rule | Detail | Snippet |")
        lines.append("|---:|---:|---|---|---|")
        for item in findings:
            detail = item.detail.replace("|", "\\|")
            snippet = item.text.replace("|", "\\|")
            if len(snippet) > 120:
                snippet = snippet[:117] + "..."
            lines.append(
                f"| `{item.file}` | {item.line} | `{item.rule}` | {detail} | {snippet} |"
            )
        lines.append("")
        lines.append("## Result")
        lines.append("- `FAIL`")
    else:
        lines.append("- No plain-language issues detected.")
        lines.append("")
        lines.append("## Result")
        lines.append("- `PASS`")
    lines.append("")
    return "\n".join(lines)


def write_evidence(root: pathlib.Path, run_date: str, report: str) -> pathlib.Path:
    evidence_dir = root / "evidence" / run_date
    evidence_dir.mkdir(parents=True, exist_ok=True)
    evidence_file = evidence_dir / f"PLAIN_LANGUAGE_AUDIT_{run_date}.md"
    evidence_file.write_text(report, encoding="utf-8")
    return evidence_file


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve()

    if args.scope:
        paths = [root / rel_path for rel_path in args.scope]
    else:
        paths = discover_markdown_files(root, args.include_glob)

    findings: list[Finding] = []
    scope: list[str] = []
    for path in paths:
        rel_path = path.relative_to(root).as_posix()
        scope.append(rel_path)
        text = load_text(path)
        findings.extend(scan_phrase_rules(rel_path, text))
        findings.extend(
            scan_dense_guidance_sentences(
                rel_path,
                text,
                dense_sentence_words=args.dense_sentence_words,
                dense_abstract_terms=args.dense_abstract_terms,
            )
        )

    report = report_markdown(args.date, scope, findings)
    if args.write_evidence:
        evidence_path = write_evidence(root, args.date, report)
        print(f"Wrote evidence report: {evidence_path}")
    else:
        print(report)

    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
