#!/usr/bin/env python3
"""Audit inbound local Markdown links to a selected source document."""

from __future__ import annotations

import argparse
import html
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

from corpus_paths import binding_corpus_scope


SOURCE_EXTRAS = ("CONSTITUTIONAL_REGRESSION_SCENARIOS.md",)
SOURCE_GLOBS = (
    "implementation/**/*.md",
    "doc_architecture/generated/**/*.md",
)
DEFAULT_TARGET = "core_09-09_standing_integration.md"
INLINE_LINK_RE = re.compile(
    r"!?\[[^\]\n]*\]\(\s*(?P<target><[^>\n]+>|[^)\s]+)"
    r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)
REFERENCE_LINK_RE = re.compile(
    r"^\s{0,3}\[[^\]\n]+\]:\s*(?P<target><[^>\n]+>|\S+)"
)
HTML_ANCHOR_RE = re.compile(
    r"<(?:a|[^>\s]+)\b[^>]*\b(?:id|name)\s*=\s*"
    r"(?:\"([^\"]+)\"|'([^']+)'|([^\s>]+))",
    re.IGNORECASE,
)
ATX_HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})(?:[ \t]+(.*?))[ \t]*$")
SETEXT_RE = re.compile(r"^\s{0,3}(?:=+|-+)\s*$")
FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
MARKDOWN_LINK_TEXT_RE = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
HTML_TAG_RE = re.compile(r"<[^>]+>")


@dataclass(frozen=True)
class Link:
    source: Path
    line: int
    raw_target: str


@dataclass(frozen=True)
class Finding:
    source: str
    line: int
    kind: str
    target: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument(
        "--target",
        default=DEFAULT_TARGET,
        help=(
            "Repository-relative Markdown file whose inbound links are checked "
            f"(default: {DEFAULT_TARGET})."
        ),
    )
    parser.add_argument(
        "--scope",
        nargs="+",
        default=None,
        help="Optional repository-relative Markdown source files to scan.",
    )
    return parser.parse_args()


def source_files(root: Path, scope: list[str] | None = None) -> list[Path]:
    if scope is not None:
        names = scope
    else:
        generated_extras = [
            path.relative_to(root).as_posix()
            for pattern in SOURCE_GLOBS
            for path in sorted(root.glob(pattern))
            if path.is_file()
        ]
        names = [
            *binding_corpus_scope(root, include_support_docs=True),
            *SOURCE_EXTRAS,
            *generated_extras,
        ]
    return [root / name for name in dict.fromkeys(names) if (root / name).is_file()]


def content_lines(text: str) -> list[tuple[int, str]]:
    """Return visible lines outside fenced code blocks and HTML comments."""
    result: list[tuple[int, str]] = []
    fence_char: str | None = None
    fence_length = 0
    in_comment = False
    for line_no, line in enumerate(text.splitlines(), start=1):
        fence = FENCE_RE.match(line)
        if fence:
            marker = fence.group(1)
            if fence_char is None:
                fence_char = marker[0]
                fence_length = len(marker)
                continue
            if marker[0] == fence_char and len(marker) >= fence_length:
                fence_char = None
                fence_length = 0
                continue
        if fence_char is None:
            visible: list[str] = []
            position = 0
            while position < len(line):
                if in_comment:
                    end = line.find("-->", position)
                    if end < 0:
                        position = len(line)
                        continue
                    in_comment = False
                    position = end + 3
                    continue
                start = line.find("<!--", position)
                if start < 0:
                    visible.append(line[position:])
                    break
                visible.append(line[position:start])
                in_comment = True
                position = start + 4
            result.append((line_no, "".join(visible)))
    return result


def links_in(path: Path, text: str) -> list[Link]:
    links: list[Link] = []
    lines = content_lines(text)
    visible_by_number = dict(lines)
    visible_text = "\n".join(
        visible_by_number.get(line_no, "")
        for line_no in range(1, len(text.splitlines()) + 1)
    )
    for match in INLINE_LINK_RE.finditer(visible_text):
        line_no = visible_text.count("\n", 0, match.start()) + 1
        links.append(Link(path, line_no, match.group("target").strip("<>")))
    for line_no, line in lines:
        reference = REFERENCE_LINK_RE.match(line)
        if reference:
            links.append(Link(path, line_no, reference.group("target").strip("<>")))
    return links


def github_slug(heading: str) -> str:
    """Return the GitHub-style base slug for a Markdown heading."""
    value = html.unescape(heading)
    value = re.sub(r"\s+#+\s*$", "", value)
    value = MARKDOWN_LINK_TEXT_RE.sub(r"\1", value)
    value = HTML_TAG_RE.sub("", value)
    value = value.replace("`", "").replace("*", "").replace("_", "_")
    value = value.strip().lower()
    value = "".join(char for char in value if char.isalnum() or char in " _-\t")
    return re.sub(r"\s", "-", value)


def anchors_in(text: str) -> set[str]:
    lines = content_lines(text)
    anchors: set[str] = set()
    heading_bases: list[str] = []

    for _, line in lines:
        for match in HTML_ANCHOR_RE.finditer(line):
            anchors.add(html.unescape(next(group for group in match.groups() if group)))

    for index, (_, line) in enumerate(lines):
        atx = ATX_HEADING_RE.match(line)
        if atx and atx.group(2) is not None:
            heading_bases.append(github_slug(atx.group(2)))
            continue
        if index + 1 < len(lines):
            next_no, next_line = lines[index + 1]
            if (
                next_no == lines[index][0] + 1
                and line.strip()
                and SETEXT_RE.match(next_line)
            ):
                heading_bases.append(github_slug(line.strip()))

    used: set[str] = set()
    next_suffix: dict[str, int] = {}
    for base in heading_bases:
        slug = base
        suffix = next_suffix.get(base, 1)
        while slug in used:
            slug = f"{base}-{suffix}"
            suffix += 1
        used.add(slug)
        next_suffix[base] = suffix
        anchors.add(slug)
    return anchors


def resolve_link(root: Path, link: Link) -> tuple[Path, str | None] | None:
    target = link.raw_target
    if not target or target.startswith("//"):
        return None
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None

    decoded_path = unquote(parsed.path)
    if decoded_path and Path(decoded_path).suffix.lower() != ".md":
        return None
    if not decoded_path and not parsed.fragment:
        return None

    target_path = link.source if not decoded_path else link.source.parent / decoded_path
    resolved = target_path.resolve()
    fragment = unquote(parsed.fragment) if parsed.fragment else None
    try:
        resolved.relative_to(root)
    except ValueError:
        return resolved, fragment
    return resolved, fragment


def audit(root: Path, paths: list[Path], selected_target: Path) -> list[Finding]:
    root = root.resolve()
    findings: list[Finding] = []
    anchor_cache: dict[Path, set[str]] = {}

    for source_path in paths:
        source = source_path.resolve()
        source_text = source.read_text(encoding="utf-8")
        for link in links_in(source, source_text):
            resolved = resolve_link(root, link)
            if resolved is None:
                continue
            target_path, fragment = resolved
            if target_path != selected_target:
                continue
            source_rel = source.relative_to(root).as_posix()
            try:
                target_rel = target_path.relative_to(root).as_posix()
            except ValueError:
                findings.append(
                    Finding(
                        source_rel,
                        link.line,
                        "unsafe-target",
                        link.raw_target,
                        "local Markdown target resolves outside the repository",
                    )
                )
                continue
            if not target_path.is_file():
                findings.append(
                    Finding(
                        source_rel,
                        link.line,
                        "missing-file",
                        link.raw_target,
                        f"target file does not exist: {target_rel}",
                    )
                )
                continue
            if fragment is None:
                continue
            if target_path not in anchor_cache:
                anchor_cache[target_path] = anchors_in(
                    target_path.read_text(encoding="utf-8")
                )
            if fragment not in anchor_cache[target_path]:
                findings.append(
                    Finding(
                        source_rel,
                        link.line,
                        "missing-fragment",
                        link.raw_target,
                        f"fragment #{fragment} is absent from {target_rel}",
                    )
                )
    return findings


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    paths = source_files(root, args.scope)
    selected_target = (root / args.target).resolve()
    findings = audit(root, paths, selected_target)

    if findings:
        print(
            f"local-markdown-fragment-audit: FAIL ({len(findings)} finding(s))",
            file=sys.stderr,
        )
        for finding in findings:
            print(
                f"  {finding.source}:{finding.line} — "
                f"{finding.kind}: {finding.detail} ({finding.target})",
                file=sys.stderr,
            )
        return 1

    print(
        f"local-markdown-fragment-audit: PASS "
        f"({len(paths)} source file(s) scanned; target: {args.target})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
