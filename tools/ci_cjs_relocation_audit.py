#!/usr/bin/env python3
"""Audit CI material that may belong in the CJS joint-structure layer.

This is an evidence-producing editorial audit. It does not fail the build by
default because a relocation candidate still needs human placement judgment.

Usage:
  python tools/ci_cjs_relocation_audit.py --root . --output-dir evidence/2026-06-12
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterable


CI_DIR = "corpus_institutions"
CJS_DIR = "corpus_joint_structure"


DESTINATION_RULES: tuple[tuple[str, tuple[str, ...], tuple[str, ...]], ...] = (
    (
        "CJS-5A / CJS-4.1 / CJS-4.7",
        (
            "authority",
            "delegation",
            "delegated",
            "procedure",
            "procedural",
            "panel",
            "recusal",
            "burden",
            "constraint",
            "secrecy",
            "override",
        ),
        ("authority/procedure", "shared procedural abstraction"),
    ),
    (
        "CJS-5B",
        (
            "audit",
            "evidence",
            "verification",
            "verified",
            "claim",
            "record",
            "assurance",
            "monitor",
            "reconstruct",
            "publication",
        ),
        ("evidence/audit", "claim integrity"),
    ),
    (
        "CJS-5C",
        (
            "participation",
            "notice",
            "notification",
            "disclosure",
            "accessibility",
            "accessible",
            "comprehension",
            "stakeholder",
            "salience",
        ),
        ("participation/disclosure", "comprehension/accessibility"),
    ),
    (
        "CJS-5D",
        (
            "dependency",
            "exit",
            "portability",
            "interoperability",
            "retention",
            "lifecycle",
            "continuity",
            "transition",
        ),
        ("dependency/exit", "lifecycle integrity"),
    ),
    (
        "CJS-5E",
        (
            "failure",
            "emergency",
            "intervention",
            "containment",
            "correction",
            "robustness",
            "resilience",
            "abuse",
            "restoration",
        ),
        ("failure/robustness", "intervention/correction"),
    ),
    (
        "CJS-4.4",
        ("trust", "trustworthiness", "misleading reliance", "proxy metric", "integrity"),
        ("cross-implementation trust",),
    ),
    (
        "CJS-3 / CJS-4",
        (
            "joint",
            "cross-implementation",
            "cross-domain",
            "interlock",
            "interface",
            "routing",
            "read with",
            "stricter-wins",
            "coordination",
            "escalation",
            "shared",
        ),
        ("joint obligation/interface",),
    ),
)


RELOCATION_SIGNALS: tuple[tuple[str, tuple[str, ...], int], ...] = (
    ("joint-interface", ("joint", "cross-implementation", "cross-domain", "shared", "interlock"), 3),
    ("multi-owner-routing", ("corpus_systems.md", "corpus_forum.md", " cjs-", " cs ", " cf "), 3),
    ("routing-read-with", ("read with", "routing", "interface", "stricter-wins", "owner", "stable id"), 2),
    ("cjs-cluster", ("cjs-5a", "cjs-5b", "cjs-5c", "cjs-5d", "cjs-5e", "operational cluster"), 3),
    ("shared-procedure", ("burden", "constraint", "procedure", "procedural", "verification", "audit"), 1),
    ("dependency-failure", ("dependency", "exit", "lifecycle", "failure", "intervention", "robustness"), 1),
    ("forum-system-touch", ("forum", "system", "classification", "steward", "chapter s2", "chapter s3"), 1),
)


KEEP_SIGNALS: tuple[str, ...] = (
    "institution-specific",
    "appointment",
    "rotation",
    "removal",
    "public revenue",
    "fees",
    "billing",
    "dissolution",
    "institutional lifecycle",
    "institutional formation",
    "local procedure",
)


ACTION_BY_SCORE = (
    (10, "split-CI-and-CJS"),
    (7, "replace-with-pointer"),
    (5, "needs-human-review"),
)


@dataclass
class Section:
    file: str
    section_id: str
    title: str
    start_line: int
    end_line: int
    body: str


@dataclass
class Candidate:
    section: Section
    score: int
    confidence: str
    action: str
    destinations: list[str] = field(default_factory=list)
    signals: list[str] = field(default_factory=list)
    router_rows: list[str] = field(default_factory=list)
    similar_cjs: list[dict[str, object]] = field(default_factory=list)
    keep_notes: list[str] = field(default_factory=list)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument(
        "--output-dir",
        default=None,
        help="Evidence directory. Defaults to evidence/<today>.",
    )
    parser.add_argument(
        "--min-score",
        type=int,
        default=5,
        help="Minimum relocation score to include. Defaults to 5.",
    )
    return parser.parse_args()


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"Missing required path: {path}")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def strip_details(text: str) -> str:
    text = re.sub(r"<details>.*?</details>", "", text, flags=re.S)
    text = re.sub(r"</?br\s*/?>", " ", text, flags=re.I)
    text = re.sub(r"</?[^>]+>", " ", text)
    return text


def strip_constitutional_index(text: str) -> str:
    """Remove standard CI routing boilerplate before relocation scoring."""

    return re.sub(
        r"\n?\*\*Constitutional index \(abridged\)\*\*.*?(?=\n\n\S|\Z)",
        "\n",
        text,
        flags=re.S,
    )


def strip_navigation_and_alignment(text: str) -> str:
    """Remove footer/navigation metadata before relocation scoring."""

    text = re.sub(r"\n?\*Corpus alignment:\*.*?(?=\n\n|\Z)", "\n", text, flags=re.S)
    text = re.sub(r"(?m)^.*\*\*(Previous|Next) file:\*\*[^\n]*$", "", text)
    text = re.sub(r"\n?## Implementation notes\b.*?(?=\n---|\Z)", "\n", text, flags=re.S)
    return text


def strip_inst_proto_registry(text: str) -> str:
    """Remove local INST-PROTO registry lists before relocation scoring."""

    return re.sub(
        r"\n?Core registry:\n(?:- `INST-PROTO-[^`\n]+`:[^\n]*\n)+",
        "\n",
        text,
    )


def strip_local_owner_application(text: str) -> str:
    """Remove accepted local owner-map and read-with routing paragraphs.

  After relocation, CI sections often retain only a CJS pointer plus compact
  owner-file naming and cross-CI interface reads. Those paragraphs are not
  fresh shared-doctrine candidates.
    """

    owner_map_re = re.compile(
        r"^(?:\*\*[^*]+\*\*\s+)?(?:Name the|Read \*\*CI-|Read \*\*Chapter|Read \*\*Protocol|"
        r"\*\*Local\b|role map\b|where applicable\b)",
        flags=re.I | re.M,
    )
    institutional_scope_re = re.compile(
        r"(use the highest `corpus_systems\.md`|apply to each delegated subunit|"
        r"through \*\*CI-\d+(?:\.\d+)*\*\* state only|"
        r"disclosure and cure file|grave breach and contingent claims|"
        r"institutional exception route|substitute capture-safeguard)",
        flags=re.I,
    )
    paragraph_kept: list[str] = []
    for paragraph in re.split(r"\n\s*\n", text):
        stripped = paragraph.strip()
        if not stripped:
            continue
        if owner_map_re.search(stripped):
            continue
        if institutional_scope_re.search(stripped):
            continue
        paragraph_kept.append(paragraph)
    return "\n\n".join(paragraph_kept)


def strip_cjs_pointer_sentences(text: str) -> str:
    """Remove explicit CJS pointer sentences before scoring relocation pressure.

    A short "apply/read CJS-X" pointer is the desired replacement form after a
    relocation. Counting those references as fresh cross-layer content would
    make the audit punish successful deduplication.
    """

    text = strip_navigation_and_alignment(strip_inst_proto_registry(strip_constitutional_index(text)))
    paragraph_kept: list[str] = []
    cjs_ref_re = re.compile(r"(corpus_joint_structure\.md|CJS-\d|CJS-5[A-E]?)", flags=re.I)
    post_relocation_re = re.compile(
        r"(this subsection states the institutional|this section states the institutional|"
        r"this section records the institutional|this subsection records the institutional|"
        r"this section supplies (?:only )?the institutional|"
        r"this section supplies the local|this subsection supplies the local|"
        r"CI-\d+(?:\.\d+)*\b.{0,160}states the institutional|"
        r"CI-\d+(?:\.\d+)*\b.{0,160}states only|"
        r"CI-\d+(?:\.\d+)*\b.{0,160}supplies (?:only )?the institutional|"
        r"institutional owner duties|institution-specific|it keeps the institution-specific|"
        r"local institutional|CI-\d+(?:\.\d+)* adds the institutional|"
        r"institutional publication duty|institutional custody duty|"
        r"institutional record duty|publication owner)",
        flags=re.I,
    )
    for paragraph in re.split(r"\n\s*\n", text):
        if cjs_ref_re.search(paragraph) and post_relocation_re.search(paragraph):
            continue
        paragraph_kept.append(paragraph)
    text = "\n\n".join(paragraph_kept)

    chunks = re.split(r"(?<=[.!?])\s+|\n\s*\n", text)
    kept: list[str] = []
    pointer_re = re.compile(
        r"(\bapply\b|\bread\b|\bsee\b|\bunder\b|\bgoverned by\b|\bremain(?:s)?\b|"
        r"\bshared\b|\bpointer\b|\brouter\b|\bowner map\b|\bjoint-obligation\b).{0,260}"
        r"(corpus_joint_structure\.md|CJS-\d|CJS-5[A-E]?)",
        flags=re.I | re.S,
    )
    for chunk in chunks:
        if pointer_re.search(chunk):
            continue
        kept.append(chunk)
    return strip_local_owner_application(" ".join(kept))


def words(text: str) -> set[str]:
    return set(re.findall(r"[a-z][a-z0-9-]{2,}", normalize(text)))


def short_summary(text: str, max_chars: int = 260) -> str:
    stripped = re.sub(
        r"\s+",
        " ",
        strip_navigation_and_alignment(strip_constitutional_index(strip_details(text))),
    ).strip()
    if len(stripped) <= max_chars:
        return stripped
    return stripped[: max_chars - 3].rstrip() + "..."


def extract_sections(path: Path, root: Path) -> list[Section]:
    rel = path.relative_to(root).as_posix()
    lines = read_text(path).splitlines()
    starts: list[tuple[int, str, str]] = []
    heading_re = re.compile(r"^(#{2,3})\s+(CI-\d+(?:\.\d+)*):?\s+(.+)$")
    for idx, line in enumerate(lines):
        match = heading_re.match(line)
        if match:
            starts.append((idx, match.group(2), match.group(3).strip()))

    sections: list[Section] = []
    for pos, (start_idx, section_id, title) in enumerate(starts):
        end_idx = starts[pos + 1][0] if pos + 1 < len(starts) else len(lines)
        body = "\n".join(lines[start_idx + 1 : end_idx])
        sections.append(
            Section(
                file=rel,
                section_id=section_id,
                title=title,
                start_line=start_idx + 1,
                end_line=end_idx,
                body=body,
            )
        )
    return sections


def extract_cjs_paragraphs(root: Path) -> list[dict[str, object]]:
    paragraphs: list[dict[str, object]] = []
    for path in sorted((root / CJS_DIR).glob("*.md")):
        rel = path.relative_to(root).as_posix()
        current_heading = ""
        buffer: list[str] = []
        start_line = 1
        in_details = False
        for idx, line in enumerate(read_text(path).splitlines(), start=1):
            if line.startswith("<details>"):
                in_details = True
            if line.startswith("</details>"):
                in_details = False
                continue
            if in_details:
                continue
            if line.startswith("#"):
                current_heading = line.lstrip("# ").strip()
                continue
            if line.startswith("*Corpus alignment:*"):
                continue
            if not line.strip() or line.strip() == "---":
                if buffer:
                    text = "\n".join(buffer).strip()
                    if len(words(text)) >= 8:
                        paragraphs.append(
                            {
                                "file": rel,
                                "line": start_line,
                                "heading": current_heading,
                                "text": text,
                                "words": words(text),
                            }
                        )
                    buffer = []
                continue
            if not buffer:
                start_line = idx
            buffer.append(line)
    return paragraphs


def extract_router_rows(root: Path) -> list[dict[str, str]]:
    path = root / CJS_DIR / "cjs_02_implementation_integration_map.md"
    rows: list[dict[str, str]] = []
    row_re = re.compile(r"^\|\s+\*\*(CJS-R[^*]+)\*\*\s+\|\s+([^|]+)\|\s+([^|]+)\|\s+([^|]+)\|")
    for line in read_text(path).splitlines():
        match = row_re.match(line)
        if match:
            rows.append(
                {
                    "id": match.group(1).strip(),
                    "topic": re.sub(r"\s+", " ", match.group(2)).strip(),
                    "owner": re.sub(r"\s+", " ", match.group(3)).strip(),
                    "read_with": re.sub(r"\s+", " ", match.group(4)).strip(),
                }
            )
    return rows


def count_occurrences(text: str, needles: Iterable[str]) -> int:
    haystack = normalize(text)
    return sum(haystack.count(needle.lower()) for needle in needles)


def choose_action(score: int, similar_count: int) -> str:
    if similar_count:
        return "replace-with-pointer"
    for threshold, action in ACTION_BY_SCORE:
        if score >= threshold:
            return action
    return "needs-human-review"


def confidence(score: int, similar_count: int) -> str:
    if score >= 12 or (score >= 8 and similar_count):
        return "high"
    if score >= 7:
        return "medium"
    return "low"


def destinations_for(text: str) -> list[str]:
    hits: list[tuple[int, str]] = []
    for destination, keywords, _reasons in DESTINATION_RULES:
        count = count_occurrences(text, keywords)
        if count:
            hits.append((count, destination))
    hits.sort(reverse=True)
    return [destination for _count, destination in hits[:3]]


def router_matches(section: Section, rows: list[dict[str, str]]) -> list[str]:
    text = normalize(f"{section.section_id} {section.title} {section.body}")
    tokens = words(f"{section.title} {section.body}")
    matches: list[tuple[int, str]] = []
    for row in rows:
        row_text = normalize(" ".join(row.values()))
        score = 0
        if section.section_id in row_text:
            score += 5
        score += len(tokens & words(f"{row['topic']} {row['owner']} {row['read_with']}")) // 4
        if any(term in text and term in row_text for term in ("forum", "system", "classification", "delegated", "trust", "audit", "coordination")):
            score += 1
        if score:
            matches.append((score, f"{row['id']} — {row['topic']}"))
    matches.sort(reverse=True)
    return [label for _score, label in matches[:3]]


def similar_cjs_paragraphs(section: Section, cjs_paragraphs: list[dict[str, object]]) -> list[dict[str, object]]:
    section_paragraphs = [
        strip_cjs_pointer_sentences(strip_details(para)).strip()
        for para in re.split(r"\n\s*\n", section.body)
        if len(words(para)) >= 8 and "<details>" not in para
    ]
    matches: list[dict[str, object]] = []
    for paragraph in section_paragraphs:
        paragraph_words = words(paragraph)
        for cjs in cjs_paragraphs:
            cjs_words = cjs["words"]
            assert isinstance(cjs_words, set)
            union = paragraph_words | cjs_words
            if not union:
                continue
            overlap = len(paragraph_words & cjs_words) / len(union)
            if overlap >= 0.32:
                matches.append(
                    {
                        "score": round(overlap, 2),
                        "file": cjs["file"],
                        "line": cjs["line"],
                        "heading": cjs["heading"],
                        "summary": short_summary(str(cjs["text"]), 140),
                    }
                )
    matches.sort(key=lambda item: item["score"], reverse=True)
    deduped: list[dict[str, object]] = []
    seen: set[tuple[str, object]] = set()
    for match in matches:
        key = (str(match["file"]), match["line"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(match)
        if len(deduped) == 3:
            break
    return deduped


def evaluate_section(section: Section, router_rows: list[dict[str, str]], cjs_paragraphs: list[dict[str, object]]) -> Candidate:
    operative_body = strip_cjs_pointer_sentences(strip_details(section.body))
    # Score only operative body text. Section IDs and headings are useful for
    # routing context, but relocation pressure should come from repeated rules,
    # not stable CI titles such as "interface" or "system".
    text = operative_body
    context_text = f"{section.section_id} {section.title}\n{operative_body}"
    score = 0
    signals: list[str] = []
    for label, needles, weight in RELOCATION_SIGNALS:
        count = count_occurrences(text, needles)
        if count:
            score += min(count, 4) * weight
            signals.append(f"{label}({count})")

    keep_notes: list[str] = []
    for needle in KEEP_SIGNALS:
        if needle in normalize(text):
            keep_notes.append(needle)
    if keep_notes and score < 9:
        score -= min(len(keep_notes), 2)

    similar = similar_cjs_paragraphs(section, cjs_paragraphs)
    if similar:
        score += 2
        signals.append(f"near-duplicate({len(similar)})")

    score = max(score, 0)
    if len(words(text)) < 8:
        score = 0
        signals.append("accepted-pointer-residual")
    return Candidate(
        section=section,
        score=score,
        confidence=confidence(score, len(similar)),
        action=choose_action(score, len(similar)),
        destinations=destinations_for(context_text),
        signals=signals,
        router_rows=router_matches(section, router_rows),
        similar_cjs=similar,
        keep_notes=keep_notes,
    )


def render_markdown(candidates: list[Candidate], root: Path, min_score: int) -> str:
    generated = datetime.now().strftime("%Y-%m-%d")
    high = sum(1 for c in candidates if c.confidence == "high")
    medium = sum(1 for c in candidates if c.confidence == "medium")
    low = sum(1 for c in candidates if c.confidence == "low")
    lines = [
        "# CI to CJS Relocation Candidate Audit",
        "",
        f"Generated: {generated}",
        "",
        "Scope: `corpus_institutions/*.md` compared against `corpus_joint_structure/*.md` and the CJS-2.2 topic router.",
        "",
        "This is an editorial exposure audit. It identifies candidate passages for relocation, pointer replacement, or split ownership; it does not apply moves.",
        "",
        "## Summary",
        "",
        f"- Candidate threshold: relocation score >= {min_score}",
        f"- Candidates: {len(candidates)}",
        f"- Confidence: high {high}, medium {medium}, low {low}",
        "",
        "## Classification rules",
        "",
        "- `split-CI-and-CJS`: likely shared rule should move to CJS while CI keeps institution-specific application.",
        "- `replace-with-pointer`: CI appears to restate existing or near-existing CJS text; replace local repetition with a short CJS pointer after review.",
        "- `needs-human-review`: cross-layer signals exist, but ownership is ambiguous or mixed.",
        "",
        "## Candidates",
        "",
    ]
    for idx, candidate in enumerate(candidates, start=1):
        section = candidate.section
        link = f"{section.file}:{section.start_line}"
        lines.extend(
            [
                f"### {idx}. {section.section_id}: {section.title}",
                "",
                f"- Source: `{link}`",
                f"- Score / confidence: {candidate.score} / {candidate.confidence}",
                f"- Suggested action: `{candidate.action}`",
                f"- Proposed CJS destination: {', '.join(candidate.destinations) if candidate.destinations else 'needs placement review'}",
                f"- Signals: {', '.join(candidate.signals) if candidate.signals else 'none'}",
                f"- Router matches: {'; '.join(candidate.router_rows) if candidate.router_rows else 'none'}",
            ]
        )
        if candidate.keep_notes:
            lines.append(f"- Keep-in-CI cautions: {', '.join(candidate.keep_notes)}")
        lines.extend(["", f"Summary: {short_summary(section.body)}", ""])
        if candidate.similar_cjs:
            lines.append("Near CJS matches:")
            for match in candidate.similar_cjs:
                lines.append(
                    f"- {match['score']}: `{match['file']}:{match['line']}` ({match['heading']}) — {match['summary']}"
                )
            lines.append("")
    lines.extend(
        [
            "## Recommended next pass",
            "",
            "1. Review high-confidence `split-CI-and-CJS` candidates first.",
            "2. For each accepted move, relocate only the shared operational rule to CJS and leave CI with a one-line pointer plus institution-specific application.",
            "3. Run `make reference-audit` after any actual relocation.",
        ]
    )
    return "\n".join(lines) + "\n"


def write_outputs(candidates: list[Candidate], output_dir: Path, root: Path, min_score: int) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    report_path = output_dir / "ci_to_cjs_relocation_audit.md"
    report_path.write_text(render_markdown(candidates, root, min_score), encoding="utf-8")

    csv_path = output_dir / "ci_to_cjs_relocation_candidates.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            lineterminator="\n",
            fieldnames=[
                "file",
                "section_id",
                "title",
                "start_line",
                "end_line",
                "score",
                "confidence",
                "action",
                "destinations",
                "signals",
                "router_rows",
                "summary",
            ],
        )
        writer.writeheader()
        for candidate in candidates:
            section = candidate.section
            writer.writerow(
                {
                    "file": section.file,
                    "section_id": section.section_id,
                    "title": section.title,
                    "start_line": section.start_line,
                    "end_line": section.end_line,
                    "score": candidate.score,
                    "confidence": candidate.confidence,
                    "action": candidate.action,
                    "destinations": "; ".join(candidate.destinations),
                    "signals": "; ".join(candidate.signals),
                    "router_rows": "; ".join(candidate.router_rows),
                    "summary": short_summary(section.body),
                }
            )

    json_path = output_dir / "ci_to_cjs_relocation_audit_log.json"
    json_path.write_text(
        json.dumps(
            [
                {
                    "file": c.section.file,
                    "section_id": c.section.section_id,
                    "title": c.section.title,
                    "start_line": c.section.start_line,
                    "end_line": c.section.end_line,
                    "score": c.score,
                    "confidence": c.confidence,
                    "action": c.action,
                    "destinations": c.destinations,
                    "signals": c.signals,
                    "router_rows": c.router_rows,
                    "similar_cjs": c.similar_cjs,
                    "keep_notes": c.keep_notes,
                    "summary": short_summary(c.section.body),
                }
                for c in candidates
            ],
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"Wrote {report_path}")
    print(f"Wrote {csv_path}")
    print(f"Wrote {json_path}")


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    output_dir = Path(args.output_dir) if args.output_dir else root / "evidence" / datetime.now().strftime("%Y-%m-%d")
    if not output_dir.is_absolute():
        output_dir = root / output_dir

    ci_paths = sorted((root / CI_DIR).glob("*.md"))
    if not ci_paths:
        raise SystemExit(f"No CI files found under {root / CI_DIR}")

    sections = [section for path in ci_paths for section in extract_sections(path, root)]
    router_rows = extract_router_rows(root)
    cjs_paragraphs = extract_cjs_paragraphs(root)

    candidates = [
        candidate
        for candidate in (evaluate_section(section, router_rows, cjs_paragraphs) for section in sections)
        if candidate.score >= args.min_score
    ]
    candidates.sort(
        key=lambda candidate: (
            {"high": 3, "medium": 2, "low": 1}[candidate.confidence],
            candidate.score,
            candidate.section.file,
            candidate.section.start_line,
        ),
        reverse=True,
    )

    write_outputs(candidates, output_dir, root, args.min_score)
    print(f"Candidates: {len(candidates)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
