#!/usr/bin/env python3
"""Flag bold run-in labels that merely restate their own section heading.

After Trace / D/A/C widgets, ``<br>`` spacers, and the ``*In plain terms*``
gloss, the first operative line of a section must carry content. A bold
run-in label that repeats the heading it sits under —

    #### 11.1 Governance as Authorized Structure

    **Governance as authorized structure.** At principle layer, ...

— spends the reader's first line on a word the heading already said. The
fix is to drop the label and let the sentence (or the list) start, or to
replace it with a label that says something the heading does not.

Scope: the first body line of a section, when that line opens with a bold
run-in in label form (``**Label:**`` / ``**Label.**`` / a bold label alone
on its line). A bold term used as the subject of a real sentence
(``**Market Structure** governs whether ...``) is not a label and is out of
scope, as are labels that add a distinct idea (``**What this subsection
does:**``, ``**Plural detection and review:**``).

MD-HEADING-TOPIC-01 covers the neighboring case: a first line that restates
the heading as a numbered ``§`` self-cite or a self-fragment link.

Rule ID: MD-HEADING-RUNIN-01
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
from heading_echo_topic_audit import (  # noqa: E402
    DETAILS_CLOSE_RE,
    DETAILS_OPEN_RE,
    FENCE_RE,
    HEADING_LINE_RE,
    ID_RE,
    MARKDOWN_LINK_RE,
    is_file_chrome,
)

ROOT = Path(__file__).resolve().parents[1]
RULE = "MD-HEADING-RUNIN-01"

LIST_PREFIX_RE = re.compile(r"^(?:[-*] |\d+\. )")
RUNIN_RE = re.compile(r"^\*\*(?P<label>[^*]+?)\*\*(?P<after>.*)$")

STOPWORDS = frozenset(
    {
        "a",
        "an",
        "and",
        "are",
        "as",
        "at",
        "by",
        "for",
        "in",
        "is",
        "its",
        "not",
        "of",
        "on",
        "or",
        "over",
        "that",
        "the",
        "this",
        "to",
        "under",
        "with",
    }
)


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    heading: str
    label: str

    def format(self) -> str:
        where = f"§{self.heading}" if self.heading else "section"
        return (
            f"{self.file}:{self.line}: {RULE}: {where} opens with a bold "
            f"run-in that restates the heading: **{self.label}**"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--paths",
        nargs="*",
        help="Specific repository-relative Markdown paths to scan.",
    )
    return parser.parse_args()


def plain_text(text: str) -> str:
    text = MARKDOWN_LINK_RE.sub(r"\1", text)
    text = re.sub(r"[*_`]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def singular(token: str) -> str:
    if len(token) > 3 and token.endswith("s") and not token.endswith("ss"):
        return token[:-1]
    return token


def content_tokens(text: str) -> set[str]:
    words = re.findall(r"[a-z0-9]+", plain_text(text).casefold())
    return {singular(word) for word in words if word not in STOPWORDS}


def runin_label(line: str) -> str | None:
    """Return the bold label if this line opens with a run-in label."""
    stripped = LIST_PREFIX_RE.sub("", line.strip())
    match = RUNIN_RE.match(stripped)
    if match is None:
        return None
    label = match.group("label").strip()
    after = match.group("after").strip()
    ends_label = label.endswith((":", ".", "—", "-"))
    if not after or after.startswith((":", ".", "—")) or ends_label:
        return label.rstrip(":.—- ")
    return None


def echoes_heading(label: str, heading_title: str) -> bool:
    label_tokens = content_tokens(label)
    heading_tokens = content_tokens(heading_title)
    if not label_tokens or not heading_tokens:
        return False
    if label_tokens == heading_tokens:
        return True
    smaller, larger = sorted((label_tokens, heading_tokens), key=len)
    return len(smaller) >= 2 and smaller < larger


def scan_text(rel_path: str, text: str) -> list[Finding]:
    findings: list[Finding] = []
    details_depth = 0
    in_fence = False
    heading_num: str | None = None
    heading_title = ""
    seen_body = False
    for idx, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if FENCE_RE.match(stripped):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        details_depth += len(DETAILS_OPEN_RE.findall(raw))
        details_depth = max(0, details_depth - len(DETAILS_CLOSE_RE.findall(raw)))
        if details_depth == 0:
            if ID_RE.fullmatch(stripped):
                continue
            heading = HEADING_LINE_RE.match(stripped)
            if heading:
                heading_num = heading.group(2)
                heading_title = heading.group(3).strip()
                seen_body = False
                continue
        if heading_num is None:
            continue
        if is_section_chrome(stripped, details_depth) or is_file_chrome(stripped):
            continue
        if seen_body:
            continue
        seen_body = True
        label = runin_label(raw)
        if label and echoes_heading(label, heading_title):
            findings.append(Finding(rel_path, idx, heading_num, plain_text(label)))
    return findings


def scan_file(root: Path, rel_path: str) -> list[Finding]:
    path = root / rel_path
    if not path.is_file():
        return []
    return scan_text(rel_path, path.read_text(encoding="utf-8"))


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
        finding for rel_path in scope for finding in scan_file(root, rel_path)
    ]
    if not findings:
        print(
            f"PASS: {RULE} — no section opens with a bold run-in that "
            "restates its heading."
        )
        return 0
    print(f"FAIL: {RULE} — {len(findings)} heading-echo run-in label(s).")
    for finding in findings:
        print(f"  {finding.format()}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
