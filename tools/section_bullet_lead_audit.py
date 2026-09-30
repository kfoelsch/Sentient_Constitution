#!/usr/bin/env python3
"""Flag sections whose body opens with a list item instead of lead-in prose.

After a heading's Trace / D/A/C widgets, ``<br>`` spacers, anchor lines, and
``*In plain terms*`` gloss, the first operative line of a section should be
prose that introduces what follows — not a bare ``- `` / ``* `` / ``1. `` list
item. A section whose first content is a child heading is a container and is
out of scope.

Carve-out: Chapter Five definition files (``core_05_*.md``) are excluded —
their entries open with O / E / C bullets by design (see
``ch5_entry_format_audit.py``).

Rule ID: MD-SECTION-LEAD-01 (blocking; part of ``make regression``).
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
RULE = "MD-SECTION-LEAD-01"

HEADING_RE = re.compile(r"^(#{2,6})\s+(.+?)\s*#*\s*$")
FENCE_RE = re.compile(r"^(```|~~~)")
DETAILS_OPEN_RE = re.compile(r"<details\b", re.I)
DETAILS_CLOSE_RE = re.compile(r"</details>", re.I)
LIST_ITEM_RE = re.compile(r"^(?:[-*+]|\d+[.)])\s+\S")
CARVE_OUT_RE = re.compile(r"^core_05_")


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    heading_line: int
    heading: str
    preview: str


def is_carved_out(rel_path: str) -> bool:
    """Chapter Five definition files are exempt from this rule."""
    return bool(CARVE_OUT_RE.match(Path(rel_path).name))


def is_file_chrome(stripped: str) -> bool:
    if stripped in {"---", "***", "___"}:
        return True
    if stripped.startswith(("**Previous file:**", "**Next file:**", "<!--")):
        return True
    return False


def scan_text(rel_path: str, text: str) -> list[Finding]:
    """Return one finding per section whose first body line is a list item."""
    findings: list[Finding] = []
    details_depth = 0
    in_fence = False
    in_comment = False
    heading: str | None = None
    heading_line = 0
    for idx, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if in_comment:
            if "-->" in stripped:
                in_comment = False
            continue
        if FENCE_RE.match(stripped):
            in_fence = not in_fence
            if heading is not None and details_depth == 0:
                heading = None  # a code block opens the body: not a list
            continue
        if in_fence:
            continue
        if stripped.startswith("<!--") and "-->" not in stripped:
            in_comment = True
            continue
        was_depth = details_depth
        details_depth += len(DETAILS_OPEN_RE.findall(raw))
        details_depth = max(0, details_depth - len(DETAILS_CLOSE_RE.findall(raw)))
        if was_depth == 0 and details_depth == 0:
            match = HEADING_RE.match(stripped)
            if match and not raw.startswith((" ", "\t")):
                heading = match.group(2).strip()
                heading_line = idx
                continue
        if heading is None:
            continue
        if was_depth > 0 or is_section_chrome(stripped, details_depth):
            continue
        if is_file_chrome(stripped):
            continue
        if LIST_ITEM_RE.match(stripped) and not raw.startswith((" ", "\t")):
            preview = stripped if len(stripped) <= 90 else stripped[:87] + "..."
            findings.append(Finding(rel_path, idx, heading_line, heading, preview))
        heading = None
    return findings


def scan_file(root: Path, rel_path: str) -> list[Finding]:
    path = root / rel_path
    if not path.is_file() or is_carved_out(rel_path):
        return []
    return scan_text(rel_path, path.read_text(encoding="utf-8"))


def format_finding(finding: Finding) -> str:
    return (
        f"{finding.file}:{finding.line}: {RULE}: section "
        f"'{finding.heading}' (line {finding.heading_line}) opens with a list "
        f"item, not lead-in prose: {finding.preview!r}"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--paths",
        nargs="*",
        help="Specific repository-relative Markdown paths to scan.",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Print per-file counts instead of every finding.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    full_scope = binding_corpus_scope(root, include_support_docs=False)
    if args.paths:
        allowed = set(full_scope)
        scope = [path for path in args.paths if path in allowed]
    else:
        scope = full_scope
    findings = [f for rel_path in scope for f in scan_file(root, rel_path)]
    if not findings:
        print(
            f"PASS: {RULE} — sections open with lead-in prose, not a list item "
            "(Chapter Five definition files exempt)."
        )
        return 0
    print(
        f"FAIL: {RULE} — {len(findings)} section(s) open with a list item "
        "(Chapter Five definition files exempt)."
    )
    if args.summary:
        counts: dict[str, int] = {}
        for finding in findings:
            counts[finding.file] = counts.get(finding.file, 0) + 1
        for rel_path, count in counts.items():
            print(f"  {rel_path}: {count}")
    else:
        for finding in findings:
            print(f"  {format_finding(finding)}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
