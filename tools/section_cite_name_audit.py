#!/usr/bin/env python3
"""Require human-readable titles on § section-number cites in body prose.

Number-only links such as ``[§11.5](#…)`` and bare ranges such as
``**§§11.1–11.6**`` fail. A cite is named when the title is in the link
text (``[§11.5 Contingent Claims…](#…)``), immediately after an unlinked
token, or in a following ``(*Title*)`` gloss that starts with a capital letter.
A lowercase note such as ``(*remedy and correction*)`` describes a cite but does
not name it, so ``[§5](#…) (*remedy and correction*)`` fails; put the title in
the link text and keep the note after it.

Table rows are scanned like prose: a cite in a table cell needs its title
too. Table cites that were already unnamed when table rows came into scope
are listed in ``section_cite_name_table_baseline.json`` and do not block a full
scan; editing such a row changes its fingerprint, so the row must then be
named. Prose cites have no baseline. ``--write-baseline`` rewrites the file. ``<details>`` widgets, headings, HTML-only lines, blockquotes,
backticks, and fenced code are out of scope. ``--changed-only`` scans
added Markdown lines versus HEAD so existing unnamed cites do not block
until those lines are edited.

Rule ID: SECTION-CITE-NAME-01
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope  # noqa: E402
from chapter_insertion_diff import is_insertion_only_change  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RULE = "SECTION-CITE-NAME-01"
BASELINE_PATH = _TOOLS / "section_cite_name_table_baseline.json"

CHAPTER_PREFIX = (
    r"(?:Chapter\s+(?:One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|"
    r"Eleven|Twelve|Thirteen|Fourteen|Fifteen|Sixteen|Seventeen|Eighteen|Nineteen|Twenty-One|Twenty-Two|Twenty-Three|Twenty-Four|Twenty-Five|Twenty-Six|Twenty-Seven|Twenty-Eight|Twenty|\d+)\s+)?"
    r"(?:Preamble\s+)?"
)
SECTION_TOKEN_RE = re.compile(
    CHAPTER_PREFIX
    + r"§+\s*\d+(?:\.\d+)*(?:\s*[–-]\s*§*\s*\d+(?:\.\d+)*)?",
    re.I,
)
NUMBER_ONLY_RE = re.compile(
    r"^"
    + CHAPTER_PREFIX
    + r"§+\s*\d+(?:\.\d+)*(?:\s*[–-]\s*§*\s*\d+(?:\.\d+)*)?"
    r"$",
    re.I,
)
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
CODE_SPAN_RE = re.compile(r"`[^`]*`")
FENCE_RE = re.compile(r"^```")
GLOSS_AFTER_RE = re.compile(r"^\(\*[A-Z0-9][^*]*?\*\)")
TITLE_START_RE = re.compile(r"^[*_]*[A-Z]")
DETAILS_OPEN_RE = re.compile(r"<details\b", re.I)
DETAILS_CLOSE_RE = re.compile(r"</details>", re.I)
FAMILY_BEFORE_RE = re.compile(
    r"(?:CS|CI|CF|CJS)-\d+(?:\.\d+)*[A-Z]?"
    r"(?:\s*[—–-]\s+[^*\n§]+)?"
    r"[*_]*\s*$",
    re.I,
)


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    cite: str
    detail: str
    table: bool = False
    fingerprint: str = ""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--changed-only",
        action="store_true",
        help="Scan added Markdown lines changed relative to HEAD.",
    )
    parser.add_argument(
        "--write-baseline",
        action="store_true",
        help="Rewrite the table-cite baseline from a full scan of the binding corpus.",
    )
    parser.add_argument(
        "--paths",
        nargs="*",
        help="Specific repository-relative Markdown paths to scan.",
    )
    return parser.parse_args()


def visible_text(link_label: str) -> str:
    return re.sub(r"[*_]", "", link_label).strip()


def is_named_after(text_after: str) -> bool:
    rest = re.sub(r"^[*_]+", "", text_after).lstrip()
    if GLOSS_AFTER_RE.match(rest):
        return True
    link_close = re.match(r"\]\([^)]+\)", rest)
    if link_close:
        return is_named_after(rest[link_close.end() :])
    return bool(TITLE_START_RE.match(rest))


def is_family_section(line: str, start: int) -> bool:
    return bool(FAMILY_BEFORE_RE.search(line[:start]))


def is_exempt_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if stripped.startswith("#"):
        return True
    if stripped.startswith("<"):
        return True
    if stripped.startswith(">"):
        return True
    return False


def scan_line(rel_path: str, line_number: int, line: str) -> list[Finding]:
    if is_exempt_line(line):
        return []
    is_table = line.lstrip().startswith("|")
    fingerprint = hashlib.sha1(line.strip().encode("utf-8")).hexdigest()[:12]
    line = CODE_SPAN_RE.sub(" ", line)
    findings: list[Finding] = []
    for match in MARKDOWN_LINK_RE.finditer(line):
        if is_family_section(line, match.start()):
            continue
        visible = visible_text(match.group(1))
        if NUMBER_ONLY_RE.match(visible):
            after = line[match.end() :]
            if is_named_after(after):
                continue
            findings.append(
                Finding(
                    rel_path,
                    line_number,
                    visible,
                    "section-number link has no title in the link text "
                    "or a following capitalized (*Title*) gloss",
                    is_table,
                    fingerprint,
                )
            )
    stripped = MARKDOWN_LINK_RE.sub("", line)
    for match in SECTION_TOKEN_RE.finditer(stripped):
        if is_family_section(stripped, match.start()):
            continue
        token = re.sub(r"\s+", " ", match.group(0)).strip()
        if is_named_after(stripped[match.end() :]):
            continue
        findings.append(
            Finding(
                rel_path,
                line_number,
                token,
                "bare section number has no title immediately after it",
                is_table,
                fingerprint,
            )
        )
    return findings


def mask_details_and_fences(text: str) -> str:
    lines = text.splitlines()
    depth = 0
    in_fence = False
    out: list[str] = []
    for line in lines:
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            out.append("")
            continue
        if in_fence:
            out.append("")
            continue
        opens = len(DETAILS_OPEN_RE.findall(line))
        closes = len(DETAILS_CLOSE_RE.findall(line))
        if depth > 0 or opens:
            out.append("")
            depth += opens - closes
            if depth < 0:
                depth = 0
            continue
        out.append(line)
    return "\n".join(out)


def masked_line_numbers(text: str) -> set[int]:
    masked: set[int] = set()
    depth = 0
    in_fence = False
    for idx, line in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            masked.add(idx)
            continue
        if in_fence:
            masked.add(idx)
            continue
        opens = len(DETAILS_OPEN_RE.findall(line))
        closes = len(DETAILS_CLOSE_RE.findall(line))
        if depth > 0 or opens:
            masked.add(idx)
            depth += opens - closes
            if depth < 0:
                depth = 0
    return masked


def scan_text(rel_path: str, text: str) -> list[Finding]:
    findings: list[Finding] = []
    masked = mask_details_and_fences(text)
    for idx, line in enumerate(masked.splitlines(), start=1):
        findings.extend(scan_line(rel_path, idx, line))
    return findings


def scan_file(root: Path, rel_path: str) -> list[Finding]:
    path = root / rel_path
    if not path.is_file():
        return []
    return scan_text(rel_path, path.read_text(encoding="utf-8"))


def changed_markdown_findings(root: Path, allowed_scope: set[str]) -> list[Finding]:
    result = subprocess.run(
        [
            "git",
            "diff",
            "--unified=0",
            "--diff-filter=ACM",
            "HEAD",
            "--",
            *sorted(allowed_scope),
        ],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    findings: list[Finding] = []
    rel_path: str | None = None
    new_line = 0
    removed_lines: list[str] = []
    masked_by_file: dict[str, set[int]] = {}
    for line in result.stdout.splitlines():
        if line.startswith("+++ b/"):
            rel_path = line.removeprefix("+++ b/")
            continue
        if line.startswith("@@"):
            match = re.search(r"\+(\d+)(?:,\d+)?", line)
            new_line = int(match.group(1)) if match else 0
            removed_lines = []
            continue
        if rel_path is None or rel_path not in allowed_scope:
            continue
        if line.startswith("+") and not line.startswith("+++"):
            if is_insertion_only_change(removed_lines, line[1:]):
                new_line += 1
                continue
            if rel_path not in masked_by_file:
                path = root / rel_path
                masked_by_file[rel_path] = (
                    masked_line_numbers(path.read_text(encoding="utf-8"))
                    if path.is_file()
                    else set()
                )
            if new_line not in masked_by_file[rel_path]:
                findings.extend(scan_line(rel_path, new_line, line[1:]))
            new_line += 1
            continue
        if line.startswith("-") and not line.startswith("---"):
            removed_lines.append(line[1:])
            continue
        if not line.startswith("-"):
            new_line += 1
    return findings


def baseline_key(finding: Finding) -> tuple[str, str, str]:
    return (finding.file, finding.cite, finding.fingerprint)


def load_baseline(path: Path = BASELINE_PATH) -> Counter:
    if not path.is_file():
        return Counter()
    data = json.loads(path.read_text(encoding="utf-8"))
    return Counter(
        (entry["file"], entry["cite"], entry["line"]) for entry in data.get("entries", [])
    )


def apply_baseline(findings: list[Finding], baseline: Counter) -> tuple[list[Finding], int]:
    """Drop table findings already in the baseline; prose findings never drop."""
    remaining = Counter(baseline)
    kept: list[Finding] = []
    grandfathered = 0
    for finding in findings:
        key = baseline_key(finding)
        if finding.table and remaining[key] > 0:
            remaining[key] -= 1
            grandfathered += 1
            continue
        kept.append(finding)
    return kept, grandfathered


def write_baseline(findings: list[Finding], path: Path = BASELINE_PATH) -> int:
    entries = sorted(
        (
            {"file": f.file, "cite": f.cite, "line": f.fingerprint}
            for f in findings
            if f.table
        ),
        key=lambda e: (e["file"], e["cite"], e["line"]),
    )
    payload = {
        "rule": RULE,
        "note": (
            "Unnamed section-number cites in table rows that predate table rows "
            "coming into scope. Each entry is (file, cite, SHA-1 of the row text). "
            "Editing a row changes its fingerprint, so the row must then be named. "
            "Shrink this file by naming cites; never add to it by hand."
        ),
        "entries": entries,
    }
    path.write_text(json.dumps(payload, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return len(entries)


def format_finding(finding: Finding) -> str:
    return (
        f"{finding.file}:{finding.line}: {RULE}: unnamed {finding.cite}: "
        f"{finding.detail}"
    )


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    full_scope = binding_corpus_scope(root, include_support_docs=False)
    if args.write_baseline:
        scanned = [
            finding
            for rel_path in full_scope
            for finding in scan_file(root, rel_path)
        ]
        prose = [f for f in scanned if not f.table]
        if prose:
            print(f"FAIL: {RULE} — {len(prose)} unnamed prose cite(s); name them before writing a baseline.")
            for finding in prose:
                print(f"  {format_finding(finding)}")
            return 1
        count = write_baseline(scanned)
        print(f"Wrote {count} table-cite baseline entr{'y' if count == 1 else 'ies'} to {BASELINE_PATH.name}.")
        return 0
    grandfathered = 0
    if args.paths:
        allowed = set(full_scope)
        scope = [path for path in args.paths if path in allowed]
        findings = [
            finding
            for rel_path in scope
            for finding in scan_file(root, rel_path)
        ]
    elif args.changed_only:
        findings = changed_markdown_findings(root, set(full_scope))
    else:
        findings = [
            finding
            for rel_path in full_scope
            for finding in scan_file(root, rel_path)
        ]
    if not args.changed_only:
        findings, grandfathered = apply_baseline(findings, load_baseline())
    if not findings:
        mode = "changed-only" if args.changed_only else "full"
        note = (
            f" {grandfathered} older table cite(s) are in the baseline."
            if grandfathered
            else ""
        )
        print(f"PASS: {RULE} ({mode}) — section-number cites are named.{note}")
        return 0
    print(f"FAIL: {RULE} — {len(findings)} unnamed section-number cite(s).")
    for finding in findings:
        print(f"  {format_finding(finding)}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
