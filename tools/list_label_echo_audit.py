#!/usr/bin/env python3
"""Flag list items whose bold label is merely restated by their own body.

A list item written ``- **Label:** body`` spends its label on one idea and its
body on the detail. When the body says nothing the label did not —

    - **Is invalid:** The seat is invalid.

— the reader gets the same words twice. The fix is to fold the item into its
neighbour, or to write a label that names a distinct idea.

Scope: a list item (any indent) that opens with a bold label, outside fenced
code, HTML comments, and ``<details>`` (Trace) blocks. It is flagged when

* every content word of the label reappears in the body, in the same order,
* the body adds at most ``MAX_EXTRA`` content word the label lacks, and
* the whole body is at most ``MAX_BODY_WORDS`` words.

Out of scope, to keep false positives low: bodies that open with ``—`` or
``(`` or contain ``§`` (cross-reference rows and pointers), and bodies that
end with ``:`` (a lead-in to a nested list, which carries the content).

Rule ID: MD-LABEL-ECHO-01 (blocking; part of ``make regression``; ``--advisory`` reports without failing).
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
RULE = "MD-LABEL-ECHO-01"

MAX_EXTRA = 1
MAX_BODY_WORDS = 12

FENCE_RE = re.compile(r"^(```|~~~)")
DETAILS_OPEN_RE = re.compile(r"<details\b", re.I)
DETAILS_CLOSE_RE = re.compile(r"</details>", re.I)
ITEM_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\*\*(?P<label>[^*]+?)\*\*(?P<body>.*)$")
LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
WORD_RE = re.compile(r"[a-z][a-z'-]*")

STOPWORDS = frozenset(
    "a an and are as at be been by can for from has have in is it its may "
    "must no not of on or shall should so than that the their then there "
    "these this to was were which will with would".split()
)


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    label: str
    body: str

    def format(self) -> str:
        preview = self.body if len(self.body) <= 80 else self.body[:77] + "..."
        return (
            f"{self.file}:{self.line}: {RULE}: bullet label '{self.label}' is "
            f"restated by its own body: {preview!r}"
        )


def plain(text: str) -> str:
    text = LINK_RE.sub(r"\1", text)
    return re.sub(r"[*_`]", "", text).strip()


def stem(word: str) -> str:
    for suffix in ("ing", "ed", "es", "s"):
        if word.endswith(suffix) and len(word) - len(suffix) >= 3:
            return word[: -len(suffix)]
    return word


def content_tokens(text: str) -> list[str]:
    return [stem(w) for w in WORD_RE.findall(plain(text).lower()) if w not in STOPWORDS]


def is_subsequence(needle: list[str], haystack: list[str]) -> bool:
    remaining = iter(haystack)
    return all(token in remaining for token in needle)


def clean_label(label: str) -> str:
    return plain(label).strip().rstrip(":.—- ").strip()


def clean_body(body: str) -> str:
    """Drop the label's own ``:`` / ``.`` separator; keep a leading ``—`` (a dash opens an index row)."""
    return body.strip().lstrip(":. ").strip()


def echoes(label: str, body: str) -> bool:
    if not label or not body:
        return False
    if body.startswith(("—", "(")) or "§" in body or body.endswith(":"):
        return False
    if len(WORD_RE.findall(plain(body).lower())) > MAX_BODY_WORDS:
        return False
    label_tokens = content_tokens(label)
    if not label_tokens:
        return False
    body_tokens = content_tokens(body)
    extra = set(body_tokens) - set(label_tokens)
    return is_subsequence(label_tokens, body_tokens) and len(extra) <= MAX_EXTRA


def scan_text(rel_path: str, text: str) -> list[Finding]:
    findings: list[Finding] = []
    details_depth = 0
    in_fence = False
    in_comment = False
    for idx, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if in_comment:
            if "-->" in stripped:
                in_comment = False
            continue
        if stripped.startswith("<!--") and "-->" not in stripped:
            in_comment = True
            continue
        if FENCE_RE.match(stripped):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        was_depth = details_depth
        details_depth += len(DETAILS_OPEN_RE.findall(raw))
        details_depth = max(0, details_depth - len(DETAILS_CLOSE_RE.findall(raw)))
        if was_depth > 0 or details_depth > 0:
            continue
        match = ITEM_RE.match(raw)
        if not match:
            continue
        label = clean_label(match.group("label"))
        body = clean_body(match.group("body"))
        if echoes(label, body):
            findings.append(Finding(rel_path, idx, label, plain(body)))
    return findings


def scan_file(root: Path, rel_path: str) -> list[Finding]:
    path = root / rel_path
    if not path.is_file():
        return []
    return scan_text(rel_path, path.read_text(encoding="utf-8"))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument(
        "--paths", nargs="*", help="Specific repository-relative Markdown paths to scan."
    )
    parser.add_argument(
        "--advisory", action="store_true", help="Report findings but exit 0."
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
        print(f"PASS: {RULE} — no bullet label is restated by its own body.")
        return 0
    status = "ADVISORY" if args.advisory else "FAIL"
    print(f"{status}: {RULE} — {len(findings)} bullet label(s) restated by their body.")
    for finding in findings:
        print(f"  {finding.format()}")
    return 0 if args.advisory else 1


if __name__ == "__main__":
    sys.exit(main())
