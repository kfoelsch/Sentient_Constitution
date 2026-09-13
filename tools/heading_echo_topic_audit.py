#!/usr/bin/env python3
"""Flag numbered sections whose first body-prose line restates the heading.

After Trace / D/A/C widgets, ``<br>``, and ``*In plain terms*`` gloss, the
first operative line must not repeat the current numbered heading as a
topic sentence — a self-cite such as ``§13.2 Title:`` or a markdown link
to the heading's own fragment.

Unnumbered heading-echo run-ins (``**Symmetric costly constraints:**``)
remain MD-LIST-INTRO-01's colon rule and are out of scope here.
Cross-chapter cites that happen to share a number (``Chapter Nine §4.3``
under Chapter Ten §4.3) are out of scope.

Rule ID: MD-HEADING-TOPIC-01
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_markdown_audit import is_section_chrome  # noqa: E402
from corpus_paths import binding_corpus_scope  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RULE = "MD-HEADING-TOPIC-01"

HEADING_LINE_RE = re.compile(r"^(#{2,6})\s+(\d+(?:\.\d+)*)\.?\s+(.+)$")
ID_RE = re.compile(r'<a id="([^"]+)"></a>', re.I)
FENCE_RE = re.compile(r"^```")
DETAILS_OPEN_RE = re.compile(r"<details\b", re.I)
DETAILS_CLOSE_RE = re.compile(r"</details>", re.I)
LIST_PREFIX_RE = re.compile(r"^(?:[-*] |\d+\. )")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
LEADING_CITE_RE = re.compile(
    r"^(?:(?P<preamble>Preamble)\s+|"
    r"(?:Chapter\s+(?P<chapter>One|Two|Three|Four|Five|Six|Seven|Eight|"
    r"Nine|Ten|Eleven|Twelve|Thirteen|Fourteen|Fifteen|Sixteen|\d+)\s+))?"
    r"§+\s*(?P<num>\d+(?:\.\d+)*)\b",
    re.I,
)
FILE_CHAPTER_RE = re.compile(r"^core_(\d{2})")
CHAPTER_NAME_TO_CODE = {
    "preamble": "00",
    "one": "01",
    "two": "02",
    "three": "03",
    "four": "04",
    "five": "05",
    "six": "06",
    "seven": "07",
    "eight": "08",
    "nine": "09",
    "ten": "10",
    "eleven": "11",
    "twelve": "12",
    "thirteen": "13",
    "fourteen": "14",
    "fifteen": "15",
    "sixteen": "16",
}


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    heading: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--paths",
        nargs="*",
        help="Specific repository-relative Markdown paths to scan.",
    )
    return parser.parse_args()


def file_chapter_code(rel_path: str) -> str | None:
    match = FILE_CHAPTER_RE.match(Path(rel_path).name)
    return match.group(1) if match else None


def cite_chapter_code(preamble: str | None, chapter: str | None) -> str | None:
    if preamble:
        return "00"
    if not chapter:
        return None
    if chapter.isdigit():
        return f"{int(chapter):02d}"
    return CHAPTER_NAME_TO_CODE.get(chapter.casefold())


def visible_text(line: str) -> str:
    text = LIST_PREFIX_RE.sub("", line.strip())
    text = MARKDOWN_LINK_RE.sub(r"\1", text)
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def normalize_title(text: str) -> str:
    text = MARKDOWN_LINK_RE.sub(r"\1", text)
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"^§+\s*", "", text)
    text = re.sub(r"^\d+(?:\.\d+)*\.?\s+", "", text)
    text = re.sub(r"\s+", " ", text).strip().casefold()
    return text.rstrip(".:")


def href_is_self_fragment(href: str, rel_path: str, heading_ids: set[str]) -> bool:
    if "#" not in href:
        return False
    file_part, frag = href.split("#", 1)
    file_part = file_part.strip()
    if file_part:
        href_name = Path(file_part).name
        if href_name != Path(rel_path).name:
            return False
    return frag in heading_ids


def is_file_chrome(stripped: str) -> bool:
    if stripped in {"---", "<br>", "<br/>", "<br />"}:
        return True
    if stripped.startswith(("**Previous file:**", "**Next file:**", "<!--")):
        return True
    if stripped.startswith("|"):
        return True
    return False


def first_body_finding(
    rel_path: str,
    line_number: int,
    line: str,
    heading_num: str,
    heading_title: str,
    heading_ids: set[str],
) -> Finding | None:
    visible = visible_text(line)
    if not visible:
        return None
    cite = LEADING_CITE_RE.match(visible)
    if cite and cite.group("num") == heading_num:
        cite_chapter = cite_chapter_code(cite.group("preamble"), cite.group("chapter"))
        file_chapter = file_chapter_code(rel_path)
        if cite_chapter is None or cite_chapter == file_chapter:
            return Finding(
                rel_path,
                line_number,
                heading_num,
                "first body line restates this heading as a numbered § cite",
            )
    link = MARKDOWN_LINK_RE.search(line)
    if link and href_is_self_fragment(link.group(2), rel_path, heading_ids):
        link_title = normalize_title(link.group(1))
        if link_title and link_title == normalize_title(heading_title):
            return Finding(
                rel_path,
                line_number,
                heading_num,
                "first body line restates this heading via a self-fragment link",
            )
    return None


def scan_text(rel_path: str, text: str) -> list[Finding]:
    findings: list[Finding] = []
    details_depth = 0
    in_fence = False
    pending_ids: list[str] = []
    heading_num: str | None = None
    heading_title = ""
    heading_ids: set[str] = set()
    seen_body = False
    for idx, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if FENCE_RE.match(stripped):
            in_fence = not in_fence
            if heading_num is None and stripped:
                pending_ids.clear()
            continue
        if in_fence:
            continue
        opens = len(DETAILS_OPEN_RE.findall(raw))
        closes = len(DETAILS_CLOSE_RE.findall(raw))
        if opens:
            details_depth += opens
        if closes:
            details_depth = max(0, details_depth - closes)
        if details_depth == 0:
            id_match = ID_RE.fullmatch(stripped)
            if id_match:
                pending_ids.append(id_match.group(1))
                continue
            heading = HEADING_LINE_RE.match(stripped)
            if heading:
                heading_num = heading.group(2)
                heading_title = heading.group(3).strip()
                heading_ids = set(pending_ids)
                pending_ids = []
                seen_body = False
                continue
        if heading_num is None:
            if stripped and details_depth == 0:
                pending_ids.clear()
            continue
        if is_section_chrome(stripped, details_depth) or is_file_chrome(stripped):
            continue
        if seen_body:
            continue
        seen_body = True
        finding = first_body_finding(
            rel_path, idx, raw, heading_num, heading_title, heading_ids
        )
        if finding is not None:
            findings.append(finding)
    return findings


def scan_file(root: Path, rel_path: str) -> list[Finding]:
    path = root / rel_path
    if not path.is_file():
        return []
    return scan_text(rel_path, path.read_text(encoding="utf-8"))


def format_finding(finding: Finding) -> str:
    return (
        f"{finding.file}:{finding.line}: {RULE}: §{finding.heading} "
        f"{finding.detail}"
    )


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    full_scope = binding_corpus_scope(root, include_support_docs=False)
    if args.paths:
        allowed = set(full_scope)
        scope = [path for path in args.paths if path in allowed]
    else:
        scope = full_scope
    findings = [
        finding
        for rel_path in scope
        for finding in scan_file(root, rel_path)
    ]
    if not findings:
        print(
            f"PASS: {RULE} — numbered sections do not restate the heading "
            "as the first topic sentence."
        )
        return 0
    print(
        f"FAIL: {RULE} — {len(findings)} heading-echo topic sentence(s)."
    )
    for finding in findings:
        print(f"  {format_finding(finding)}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
