#!/usr/bin/env python3
"""Flag Mermaid chart boxes whose section number trails the title.

A reader scanning a chart should find where each box lives in the same place
every time: at the start. A box that cites the section it summarizes puts the
number first, before the title —

    H["§5 Publish the office-holder statement<br/><br/>Who holds the key offices"]

— not after it behind a dash (``Publish the office-holder statement — §5``),
and not as a trailing note on a content line (``... to start — §2``).

Scope: every node label and subgraph title in a Mermaid block (the quoted text
inside ``ID["..."]``, ``ID{"..."}``, ``ID[["..."]]``, and so on). Edge labels
(``-->|"... — §1"|``) are not boxes and are out of scope. Two checks:

* **Title line.** The first line of a label (the text before the first
  ``<br/>``) must start with ``§`` if it cites a section of this corpus.
* **Trailing cite.** No line of a label may end in a dash-led section cite
  (``... — §2``, ``... — §3–§5``, ``(... — §1)``).

A cite qualified by another document (``CS-14.305 §10``, ``Chapter Nine §3``) names
a section elsewhere and is not the box's own number. Inline cross-references
in running content (``carried downstream (§18, §19)``) are prose, not labels,
and are out of scope. Article numbers (``Article VI``) are not section numbers.

Rule ID: VIS-CHART-SECNUM-09
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

from corpus_paths import binding_corpus_scope  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RULE = "VIS-CHART-SECNUM-09"

# Files outside the binding corpus that carry reader charts.
EXTRA_SCOPE = (
    "CONTRIBUTING.md",
    "guides/*.md",
    "implementation/*.md",
)

FENCE_OPEN_RE = re.compile(r"^\s*```\s*mermaid\b", re.IGNORECASE)
FENCE_CLOSE_RE = re.compile(r"^\s*```\s*$")

# ID["label"], ID{"label"}, ID[["label"]], ID(("label")), subgraph ID["label"].
# An edge label sits between pipes (``-->|"label"|``) and is not matched.
NODE_LABEL_RE = re.compile(
    r"(?<![\w|\"])[A-Za-z_][\w-]*\s*(?:\[\[|\[|\{\{|\{|\(\(|\()\s*"
    r"\"(?P<label>(?:[^\"\\]|\\.)*)\""
)
BR_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)

SECTION_REF_RE = re.compile(r"§\d")
# A section cite qualified by the document it belongs to: ``CS-14.305 §10``,
# ``Chapter Nine §3``, ``Part D §14``, ``Article XI-E §2``.
QUALIFIER_BEFORE_RE = re.compile(
    r"(?:\b[A-Z]{1,3}-\d+(?:\.\d+)*|\bChapter [A-Z][a-z]+|\bPart [A-Z]"
    r"|\bArticle [IVXL]+(?:-[A-Z])?)\s*$"
)
LEADING_MARK_RE = re.compile(r"^(?:[\s•·*\-]|\*\*)+")
TRAILING_CITE_RE = re.compile(
    r"\s[—–]\s*§\d[\d.]*"
    r"(?:(?:\s*,\s*|\s*[–-]\s*|\s+to\s+|\s+and\s+)§?\d[\d.]*)*"
    r"\s*\)?\s*$"
)


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    kind: str  # "title" or "trailing"
    text: str

    def format(self) -> str:
        if self.kind == "title":
            why = "section number is not at the start of the title line"
        else:
            why = "line ends with a trailing section number; put it first"
        return f"{self.file}:{self.line}: {RULE}: {why}: {self.text!r}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--paths",
        nargs="*",
        help="Specific repository-relative Markdown paths to scan.",
    )
    return parser.parse_args()


def has_own_section_ref(line: str) -> bool:
    """True when ``line`` cites a section of this corpus (unqualified)."""
    for match in SECTION_REF_RE.finditer(line):
        if not QUALIFIER_BEFORE_RE.search(line[: match.start()]):
            return True
    return False


def label_findings(label: str) -> list[tuple[str, str]]:
    """Return (kind, line text) for each problem in one box label."""
    problems: list[tuple[str, str]] = []
    parts = [part.strip() for part in BR_RE.split(label)]
    first = next((i for i, part in enumerate(parts) if part), None)
    for index, part in enumerate(parts):
        if not part:
            continue
        body = LEADING_MARK_RE.sub("", part)
        if (
            index == first
            and has_own_section_ref(part)
            and not body.startswith("§")
        ):
            problems.append(("title", part))
        elif TRAILING_CITE_RE.search(part):
            problems.append(("trailing", part))
    return problems


def scan_text(rel_path: str, text: str) -> list[Finding]:
    findings: list[Finding] = []
    in_chart = False
    for idx, raw in enumerate(text.splitlines(), start=1):
        if not in_chart:
            if FENCE_OPEN_RE.match(raw):
                in_chart = True
            continue
        if FENCE_CLOSE_RE.match(raw):
            in_chart = False
            continue
        for match in NODE_LABEL_RE.finditer(raw):
            for kind, line_text in label_findings(match.group("label")):
                findings.append(Finding(rel_path, idx, kind, line_text))
    return findings


def scan_file(root: Path, rel_path: str) -> list[Finding]:
    path = root / rel_path
    if not path.is_file():
        return []
    return scan_text(rel_path, path.read_text(encoding="utf-8"))


def default_scope(root: Path) -> list[str]:
    scope = list(binding_corpus_scope(root, include_support_docs=False))
    for pattern in EXTRA_SCOPE:
        for path in sorted(root.glob(pattern)):
            rel = path.relative_to(root).as_posix()
            if path.is_file() and rel not in scope:
                scope.append(rel)
    return scope


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    full_scope = default_scope(root)
    if args.paths:
        allowed = set(full_scope)
        scope = [path for path in args.paths if path in allowed]
    else:
        scope = full_scope
    findings = [f for rel in scope for f in scan_file(root, rel)]
    if not findings:
        print(f"PASS: {RULE} — every chart box puts its section number first.")
        return 0
    print(
        f"FAIL: {RULE} — {len(findings)} chart line(s) with a section number "
        "that is not first."
    )
    for finding in findings:
        print(f"  {finding.format()}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
