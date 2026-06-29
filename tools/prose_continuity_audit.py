#!/usr/bin/env python3
"""Regression gate for prose continuity: malformed indents, stranded continuation lines, and Article IX nested lists."""

from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import sys
from dataclasses import dataclass

from corpus_paths import binding_corpus_scope

def _is_malformed_leading_indent(raw: str) -> bool:
    """True if the line uses leading spaces before prose (not a sublist or ordered item)."""
    if not raw.startswith(" ") or not raw.strip():
        return False
    rest = raw.lstrip(" \t")
    if rest.startswith(("- ", "* ")):
        return False
    if rest.startswith("#"):
        return False
    if re.match(r"^\d+\.\s", rest):
        return False
    return True

# Stranded one-line continuations that previously appeared split from their paragraph.
_ORPHAN_LINE_RES: tuple[re.Pattern[str], ...] = tuple(
    re.compile(p, re.IGNORECASE)
    for p in (
        r"^Failure to do so\b",
        r"^They may default\b",
        r"^They must comply\b",
        r"^Where the burden of proof is not satisfied\b",
        r"^That validation must\b",
        r"^Such risk does\b",
        r"^That preservation must\b",
        r"^That rule applies under\b",
        r"^It must preserve compliance\b",
        r"^That choice governs\b",
        r"^That violation is assessed\b",
        r"^That satisfaction must\b",
        r"^Partial satisfaction or selective application is non-compliant\.\s*$",
    )
)

_SENTENCE_END = frozenset(".!?…")

# Chapter Six, Article IX (`core_06-06_rights_part_b.md`): lead bullets ending with these must be
# followed by nested `-` items (e.g. `  - `), not additional top-level `- ` siblings (regression for flattened sub-lists).
_ARTICLE_IX_TOP_HEADING = re.compile(r"^### Article IX:")
_TOP_LEVEL_ARTICLE_HEADING = re.compile(r"^### Article [IVXLCDM]+:")
_COLON_INTRO_PARENT = re.compile(
    r"^-\s+.+\b("
    r"including:"
    r"|have the right to:"
    r"|This includes:"
    r"|must be:"
    r")\s*$"
)


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    kind: str
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
        "--scope",
        nargs="+",
        default=None,
        help="Markdown files to scan.",
    )
    parser.add_argument(
        "--no-orphan-lines",
        action="store_true",
        help="Disable stranded continuation-line detection (indent check only).",
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


def load_text(path: pathlib.Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"Missing required file: {path}")


def is_structural_line(stripped: str) -> bool:
    if not stripped:
        return True
    if stripped.startswith("#"):
        return True
    if stripped.startswith("---"):
        return True
    if stripped.startswith("|"):
        return True
    if stripped.startswith("- ") or stripped.startswith("* "):
        return True
    if stripped.startswith("```"):
        return True
    if stripped.startswith("<"):
        return True
    return False


def _is_trivial_markdown_bullet_starter(stripped: str) -> bool:
    """A real list marker line (``- ``, ``* ```) — not a ``**`` bold run."""
    return stripped.startswith(("- ", "* "))


def _line_is_indented_list_continuation(
    raw: str, lines: list[str], idx0: int
) -> bool:
    """True for intentionally indented follow-on prose under list items.

    Covers: nested ``  - `` runs, top-level ``- `` items, chained continuations,
    and **bold** continuation paragraphs (``**`` must not be treated as ``*`` bullets).
    """
    if not _is_malformed_leading_indent(raw) or not raw.strip():
        return False
    rest = raw.lstrip(" \t")
    if _is_trivial_markdown_bullet_starter(rest):
        return True
    prev: str | None = None
    for j in range(idx0 - 1, -1, -1):
        t = lines[j]
        if t.strip():
            prev = t
            break
    if prev is None:
        return False
    pls = prev.lstrip(" \t")
    if prev.startswith(("\t", " ")) and _is_trivial_markdown_bullet_starter(pls):
        return True
    if not prev.startswith(("\t", " ")) and _is_trivial_markdown_bullet_starter(
        pls
    ) and (prev.lstrip() == pls):
        return True
    if _is_malformed_leading_indent(prev) and not _is_trivial_markdown_bullet_starter(
        pls
    ) and not pls.startswith(("<", "#", "|", "---")):
        return True
    return False


def _is_top_level_markdown_bullet(raw: str) -> bool:
    """True if line is a `- ` list item at column 0 (not indented)."""
    if raw.startswith(("\t", " ")):
        return False
    return raw.startswith("- ")


def _is_nested_markdown_bullet(raw: str) -> bool:
    """True if line is an indented `- ` or `* ` list item."""
    if not raw.startswith(("\t", " ")):
        return False
    stripped_lead = raw.lstrip(" \t")
    return stripped_lead.startswith(("- ", "* "))


def scan_article_ix_colon_intro_lists(rel_path: str, lines: list[str]) -> list[Finding]:
    """Enforce nested sub-bullets under Article IX colon introducers in the Chapter Six Part B file."""
    if rel_path != "core_06-06_rights_part_b.md":
        return []

    findings: list[Finding] = []
    in_region = False
    in_fence = False

    for idx, raw in enumerate(lines, start=1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        stripped = raw.strip()
        if _ARTICLE_IX_TOP_HEADING.match(stripped):
            in_region = True
            continue
        if in_region and _TOP_LEVEL_ARTICLE_HEADING.match(stripped) and not _ARTICLE_IX_TOP_HEADING.match(
            stripped
        ):
            in_region = False
            continue
        if not in_region:
            continue

        if not _COLON_INTRO_PARENT.match(raw.rstrip()):
            continue

        # Scan forward for the first non-blank, non-fence line after this introducer.
        j = idx
        inner_fence = False
        while j < len(lines):
            j += 1
            if j > len(lines):
                break
            nxt = lines[j - 1]
            if nxt.strip().startswith("```"):
                inner_fence = not inner_fence
                continue
            if inner_fence:
                continue
            if not nxt.strip():
                continue
            if nxt.lstrip().startswith("#"):
                break
            if _is_nested_markdown_bullet(nxt):
                break
            if _is_top_level_markdown_bullet(nxt):
                findings.append(
                    Finding(
                        file=rel_path,
                        line=j,
                        kind="article-ix-nested-list",
                        detail="Sub-bullets after a colon introducer (including:/have the right to:/This includes:/must be:) must be indented under the parent (e.g. `  - `), not top-level `- `",
                        text=nxt.strip()[:200],
                    ),
                )
            break

    return findings


def scan_file(
    rel_path: str,
    text: str,
    *,
    orphan_lines: bool,
) -> list[Finding]:
    findings: list[Finding] = []
    lines = text.splitlines()
    in_fence = False

    for idx, raw in enumerate(lines, start=1):
        if raw.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        stripped = raw.strip()
        if not stripped:
            continue

        if _is_malformed_leading_indent(raw) and not is_structural_line(stripped):
            if _line_is_indented_list_continuation(raw, lines, idx - 1):
                pass
            else:
                findings.append(
                    Finding(
                        file=rel_path,
                        line=idx,
                        kind="malformed-indent",
                        detail="Line uses leading space(s) before prose; merge into the prior line or convert to a proper list item",
                        text=stripped[:200],
                    )
                )

    if orphan_lines:
        in_fence = False
        prev_idx = 0
        prev_stripped = ""
        blank_run = False
        for idx, raw in enumerate(lines, start=1):
            if raw.strip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue

            stripped = raw.strip()
            if not stripped:
                blank_run = True
                continue

            if blank_run and prev_stripped and not is_structural_line(prev_stripped):
                last = prev_stripped[-1]
                if (
                    last in _SENTENCE_END
                    and len(stripped.split()) <= 40
                    and not stripped.rstrip().endswith(":")
                ):
                    for pat in _ORPHAN_LINE_RES:
                        if pat.search(stripped):
                            findings.append(
                                Finding(
                                    file=rel_path,
                                    line=idx,
                                    kind="stranded-continuation",
                                    detail="Line matches a known continuation fragment; join with the previous paragraph",
                                    text=stripped[:200],
                                )
                            )
                            break

            prev_idx = idx
            prev_stripped = stripped
            blank_run = False

    findings.extend(scan_article_ix_colon_intro_lists(rel_path, lines))

    return findings


def report_markdown(run_date: str, scope: list[str], findings: list[Finding]) -> str:
    out: list[str] = []
    out.append(f"# Prose Continuity Audit - {run_date}")
    out.append("")
    out.append("## Scope")
    for p in scope:
        out.append(f"- `{p}`")
    out.append("")
    out.append("## Findings")
    if findings:
        out.append("| File | Line | Type | Detail |")
        out.append("|---:|---:|---|---|")
        for f in findings:
            out.append(
                f"| `{f.file}` | {f.line} | `{f.kind}` | {f.detail} |"
            )
        out.append("")
        for f in findings:
            out.append(f"- `{f.file}:{f.line}` — {f.text}")
    else:
        out.append("- No issues detected.")
    out.append("")
    out.append("## Result")
    out.append("- `PASS`" if not findings else "- `FAIL`")
    out.append("")
    return "\n".join(out)


def write_evidence(root: pathlib.Path, run_date: str, report: str) -> pathlib.Path:
    evidence_dir = root / "evidence" / run_date
    evidence_dir.mkdir(parents=True, exist_ok=True)
    path = evidence_dir / f"PROSE_CONTINUITY_AUDIT_{run_date}.md"
    path.write_text(report, encoding="utf-8")
    return path


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve()
    scope = args.scope or binding_corpus_scope(root)
    orphan = not args.no_orphan_lines

    all_findings: list[Finding] = []
    for rel in scope:
        path = root / rel
        text = load_text(path)
        all_findings.extend(
            scan_file(rel, text, orphan_lines=orphan),
        )

    report = report_markdown(args.date, scope, all_findings)
    if args.write_evidence:
        ep = write_evidence(root, args.date, report)
        print(f"Wrote evidence report: {ep}")
    else:
        print(report)

    return 1 if all_findings else 0


if __name__ == "__main__":
    sys.exit(main())
