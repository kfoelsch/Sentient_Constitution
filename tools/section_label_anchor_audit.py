#!/usr/bin/env python3
"""Map prose section labels to resolved anchors and flag numbering divergences.

When a Markdown link's text contains a section label (``§5.4``,
``Chapter Nine §5.4 Duty to resist``), the resolved heading must carry a
current-numbering id whose prefix matches that heading's current number
(dots stripped, e.g. ``54-...``, or dots as hyphens, e.g. ``4-3-...``).
Stable / legacy ids may remain beside that alias. A citation whose fragment
still uses the fossil prefix is fine once the current-numbering alias exists
on the same heading.

Rule ID: SECTION-LABEL-ANCHOR-01
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope
from local_markdown_fragment_audit import links_in, resolve_link

ROOT = Path(__file__).resolve().parents[1]
RULE = "SECTION-LABEL-ANCHOR-01"

ANCHOR_RE = re.compile(r'<a id="([^"]+)"></a>')
ATX_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
NUM_RE = re.compile(r"^(\d+(?:\.\d+)*)\.?(?:\s+|$)")
BOLD_NUM_RE = re.compile(r"^\*\*(\d+(?:\.\d+)*)\.?\s+")
ID_NUM_RE = re.compile(r"^(\d+(?:-\d+)*)-")
SECTION_IN_TEXT_RE = re.compile(
    r"(?:Chapter\s+(?:One|Two|Three|Four|Five|Six|Seven|Eight|Nine|"
    r"Ten|Eleven|Twelve|Thirteen|Fourteen|Fifteen|Sixteen|\d+)\s+)?"
    r"§+\s*(\d+(?:\.\d+)*)",
    re.I,
)
SKIP_CONSUMERS = (
    "<details",
    "<summary",
    "<!--",
    "<div",
    "<span",
    "<br",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    return parser.parse_args()


def compact(num: str) -> str:
    return num.replace(".", "").replace("-", "")


def hyphenated(dotted: str) -> str:
    return dotted.replace(".", "-")


def id_matches_current(anchor_id: str, current_dotted: str) -> bool:
    match = ID_NUM_RE.match(anchor_id)
    if not match:
        return False
    prefix = match.group(1)
    return prefix == compact(current_dotted) or prefix == hyphenated(
        current_dotted
    )


def dotted_related(prose: str, current: str) -> bool:
    return (
        prose == current
        or current.startswith(prose + ".")
        or prose.startswith(current + ".")
    )


def source_paths(root: Path) -> list[Path]:
    names = list(binding_corpus_scope(root, include_support_docs=True))
    for pattern in ("implementation/**/*.md", "evaluation/**/*.md"):
        names.extend(
            path.relative_to(root).as_posix()
            for path in sorted(root.glob(pattern))
            if path.is_file()
        )
    out: list[Path] = []
    seen: set[str] = set()
    for name in names:
        if name.startswith(("archive/", "ai_corpus/", "evidence/")):
            continue
        if name in seen:
            continue
        seen.add(name)
        path = root / name
        if path.is_file():
            out.append(path)
    return out


def _plain_title(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return re.sub(r"^\*\*|\*\*$", "", text).strip()


def parse_clusters(text: str) -> dict[str, dict]:
    """Map each explicit id to its heading cluster (sibling ids + current number)."""
    lines = text.splitlines()
    numbered_stack: list[tuple[int, str]] = []
    pending: list[str] = []
    clusters: dict[str, dict] = {}

    def consume(title_plain: str, atx_level: int | None, lineno: int) -> None:
        nonlocal pending
        if not pending:
            return
        if atx_level is not None:
            while numbered_stack and numbered_stack[-1][0] >= atx_level:
                numbered_stack.pop()
            numbered = NUM_RE.match(title_plain)
            current = (
                numbered.group(1)
                if numbered
                else (numbered_stack[-1][1] if numbered_stack else None)
            )
            if numbered:
                numbered_stack.append((atx_level, numbered.group(1)))
        else:
            bold = BOLD_NUM_RE.match("**" + title_plain)
            if title_plain and not title_plain.startswith("**"):
                bold = BOLD_NUM_RE.match(f"**{title_plain}")
            current = (
                bold.group(1)
                if bold
                else (numbered_stack[-1][1] if numbered_stack else None)
            )
        info = {
            "ids": list(pending),
            "lineno": lineno,
            "title": title_plain[:90],
            "current": current,
        }
        for anchor_id in pending:
            clusters[anchor_id] = info
        pending = []

    for index, line in enumerate(lines, start=1):
        stripped = line.strip()
        anchor = ANCHOR_RE.match(stripped)
        if anchor:
            pending.append(anchor.group(1))
            continue
        atx = ATX_RE.match(stripped)
        if atx and not pending:
            level = len(atx.group(1))
            title = _plain_title(atx.group(2))
            while numbered_stack and numbered_stack[-1][0] >= level:
                numbered_stack.pop()
            numbered = NUM_RE.match(title)
            if numbered:
                numbered_stack.append((level, numbered.group(1)))
            continue
        if not pending:
            continue
        if not stripped or stripped.lower().startswith(SKIP_CONSUMERS):
            continue
        if atx:
            consume(_plain_title(atx.group(2)), len(atx.group(1)), index)
            continue
        bold = BOLD_NUM_RE.match(stripped)
        if bold or stripped.startswith("**"):
            consume(_plain_title(stripped), None, index)
            continue
        consume(_plain_title(stripped), None, index)
    return clusters


def cluster_cache_for(path: Path, cache: dict[Path, dict[str, dict]]) -> dict[str, dict]:
    if path not in cache:
        cache[path] = parse_clusters(path.read_text(encoding="utf-8"))
    return cache[path]


def audit(root: Path) -> list[str]:
    errors: list[str] = []
    cache: dict[Path, dict[str, dict]] = {}
    root_resolved = root.resolve()
    for source in source_paths(root):
        text = source.read_text(encoding="utf-8")
        rel = source.relative_to(root).as_posix()
        for link in links_in(source, text):
            resolved = resolve_link(root_resolved, link)
            if resolved is None:
                continue
            target_path, fragment = resolved
            if fragment is None or not ID_NUM_RE.match(fragment):
                continue
            try:
                target_rel = target_path.relative_to(root_resolved).as_posix()
            except ValueError:
                continue
            if not target_path.is_file():
                continue
            # Recover the link text from the source line for the section label.
            line = text.splitlines()[link.line - 1] if link.line <= len(text.splitlines()) else ""
            labels = [
                match.group(1)
                for match in re.finditer(r"\[([^\]]+)\]\([^)]+\)", line)
                if fragment in match.group(0)
            ]
            if not labels:
                # Multi-line or wrapped; search a small window.
                lines = text.splitlines()
                window = "\n".join(
                    lines[max(0, link.line - 3) : min(len(lines), link.line + 2)]
                )
                labels = [
                    match.group(1)
                    for match in re.finditer(r"\[([^\]]+)\]\([^)]+\)", window)
                    if fragment in match.group(0)
                ]
            if not labels:
                continue
            prose_match = SECTION_IN_TEXT_RE.search(labels[0])
            if not prose_match:
                continue
            prose = prose_match.group(1)
            info = cluster_cache_for(target_path, cache).get(fragment)
            if not info or not info.get("current"):
                continue
            current = info["current"]
            if not dotted_related(prose, current):
                continue
            if any(id_matches_current(anchor_id, current) for anchor_id in info["ids"]):
                continue
            errors.append(
                f"{rel}:{link.line}: prose §{prose} resolves to {target_rel}#"
                f"{fragment} (heading §{current} {info['title']!r}) with no "
                f"current-numbering alias (expected prefix {compact(current)}- "
                f"or {hyphenated(current)}-) ({RULE})"
            )
    return errors


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    errors = audit(root)
    if errors:
        print(f"FAIL: {len(errors)} section-label/anchor divergence(s)")
        for err in errors:
            print(err)
        return 1
    print(
        "PASS: prose section labels resolve to headings that carry a "
        "current-numbering alias beside any stable/legacy id."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
