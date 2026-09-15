#!/usr/bin/env python3
"""Generate the non-binding plain-terms edition of the core corpus.

Walks the numbered ``core_*`` files in footer-chain order and emits one
single-file gloss edition: for every heading, the heading text, the first
``*In plain terms: …*`` gloss in that section (if any), and one link back to
the authentic source span. Nothing else is copied.

The output is a derived locator, not constitutional text. It cannot narrow,
add to, or restate binding obligations; where a gloss and the source diverge,
the source binds (Chapter Fourteen supremacy; README *Binding vs support*).

Usage (from the repo root)::

    python3 tools/generate_plain_terms_edition.py --root . --write
    python3 tools/generate_plain_terms_edition.py --root . --check

``--check`` exits non-zero when the committed edition differs from what would
be generated now (advisory freshness gate; not in ``make regression``).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import CORE_FILES  # noqa: E402

DEFAULT_MD_OUT = "doc_architecture/generated/plain_terms_edition.md"
DEFAULT_JSON_OUT = "doc_architecture/generated/plain_terms_edition.json"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
ANCHOR_RE = re.compile(r'<a\s+id="([^"]+)"\s*>\s*</a>')
GLOSS_RE = re.compile(r"^\*In plain terms[:.]?\s*(.*?)\*?\s*$")
EDITION_RE = re.compile(r"\*\*Corpus edition\*\*\s*\|\s*`([^`]+)`")
EFFECTIVE_RE = re.compile(r"\*\*Effective date\*\*\s*\|\s*([0-9]{4}-[0-9]{2}-[0-9]{2})")
LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)\)")
FENCE_RE = re.compile(r"^(```|~~~)")


@dataclass
class Section:
    file: str
    level: int
    title: str
    anchor: str
    line: int
    gloss: str | None = None
    gloss_line: int | None = None

    def as_dict(self) -> dict:
        return {
            "file": self.file,
            "level": self.level,
            "title": self.title,
            "anchor": self.anchor,
            "line": self.line,
            "gloss": self.gloss,
            "gloss_line": self.gloss_line,
        }


@dataclass
class FileReport:
    file: str
    title: str
    sections: list[Section] = field(default_factory=list)

    @property
    def glossed(self) -> int:
        return sum(1 for s in self.sections if s.gloss)


def auto_slug(heading: str) -> str:
    """GitHub-flavored auto-slug used across the corpus for heading fragments."""
    text = re.sub(r"<[^>]+>", "", heading)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.replace("*", "").replace("`", "")
    s = text.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s", "-", s)
    return s.strip("-")


def clean_title(raw: str) -> str:
    text = re.sub(r"<a\s+id=\"[^\"]+\"\s*>\s*</a>", "", raw)
    text = re.sub(r"<[^>]+>", "", text)
    return text.strip()


def read_edition(root: Path) -> tuple[str, str]:
    readme = root / "README.md"
    if not readme.is_file():
        return "unknown", "unknown"
    text = readme.read_text(encoding="utf-8")
    edition = EDITION_RE.search(text)
    effective = EFFECTIVE_RE.search(text)
    return (
        edition.group(1) if edition else "unknown",
        effective.group(1) if effective else "unknown",
    )


def parse_file(root: Path, rel: str) -> FileReport:
    path = root / rel
    lines = path.read_text(encoding="utf-8").splitlines()
    report = FileReport(file=rel, title=rel)
    pending_anchor: str | None = None
    details_depth = 0
    in_fence = False
    current: Section | None = None
    seen_slugs: dict[str, int] = {}

    for idx, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n")
        stripped = line.strip()

        if FENCE_RE.match(stripped):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        # Anchors may sit on their own line directly above a heading.
        anchor_match = ANCHOR_RE.match(stripped)
        if anchor_match and stripped == anchor_match.group(0):
            # First explicit anchor above a heading wins (stable id);
            # later alias anchors are ignored for the link target.
            if pending_anchor is None:
                pending_anchor = anchor_match.group(1)
            continue

        # Track collapsible widget depth so headings inside <details>
        # (directory widgets) are not treated as sections.
        opens = stripped.count("<details")
        closes = stripped.count("</details>")

        heading = HEADING_RE.match(line)
        if heading and details_depth == 0:
            level = len(heading.group(1))
            title = clean_title(heading.group(2))
            anchor = pending_anchor
            if not anchor:
                base = auto_slug(title)
                n = seen_slugs.get(base, 0)
                seen_slugs[base] = n + 1
                anchor = base if n == 0 else f"{base}-{n}"
            current = Section(file=rel, level=level, title=title, anchor=anchor, line=idx)
            report.sections.append(current)
            if level == 1 and report.title == rel:
                report.title = title
            pending_anchor = None
            details_depth += opens - closes
            continue

        if stripped and not heading:
            pending_anchor = None

        details_depth += opens - closes
        if details_depth < 0:
            details_depth = 0

        if current is not None and current.gloss is None and details_depth == 0:
            gloss = GLOSS_RE.match(stripped)
            if gloss:
                current.gloss = gloss.group(1).strip()
                current.gloss_line = idx

    return report


def rewrite_links(text: str, source_file: str, prefix: str) -> str:
    """Point gloss links at the source tree relative to the generated file."""

    def repl(match: re.Match[str]) -> str:
        label, target = match.group(1), match.group(2)
        if target.startswith(("http://", "https://", "mailto:", "/")):
            return match.group(0)
        if target.startswith("#"):
            return f"[{label}]({prefix}{source_file}{target})"
        return f"[{label}]({prefix}{target})"

    return LINK_RE.sub(repl, text)


def render_markdown(reports: list[FileReport], edition: str, effective: str, prefix: str) -> str:
    total = sum(len(r.sections) for r in reports)
    glossed = sum(r.glossed for r in reports)
    pct = (100.0 * glossed / total) if total else 0.0

    out: list[str] = [
        "# Plain-terms edition (generated, non-binding)",
        "",
        "Auto-generated by `make plain-terms-edition` from the numbered `core_*` files. Do not edit by hand.",
        "",
        f"Corpus edition: `{edition}` · effective **{effective}**",
        "",
        "> **Reader guidance (non-operative).** This page lists every core heading, the section's *In plain terms* gloss where one exists, and one link to the authentic source span. It copies **nothing else**. Glosses are reading aids already present in the source; they do not add, remove, or narrow obligations. Where a gloss and the source differ, the source binds ([Chapter Fourteen](" + prefix + "core_14_expansion_supremacy.md); [README — Binding vs support](" + prefix + "README.md#binding-vs-support)). A heading without a gloss is listed with its link only.",
        "",
        f"Coverage: **{glossed}** of **{total}** headings carry a gloss ({pct:.0f}%).",
        "",
        "## Contents",
        "",
    ]
    for report in reports:
        out.append(f"- [{report.title}](#{auto_slug(report.title)}) — `{report.file}` ({report.glossed}/{len(report.sections)} glossed)")
    out.append("")

    for report in reports:
        out.append(f"## {report.title}")
        out.append("")
        out.append(f"Source file: [`{report.file}`]({prefix}{report.file}) · {report.glossed}/{len(report.sections)} headings glossed")
        out.append("")
        for section in report.sections:
            if section.level == 1:
                continue
            depth = min(section.level + 1, 6)
            hashes = "#" * depth
            link = f"{prefix}{section.file}#{section.anchor}"
            out.append(f"{hashes} {section.title}")
            out.append("")
            if section.gloss:
                out.append(rewrite_links(section.gloss, section.file, prefix))
            else:
                out.append("*(no plain-terms gloss in source)*")
            out.append("")
            out.append(f"[Source]({link})")
            out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def build_payload(reports: list[FileReport], edition: str, effective: str) -> dict:
    total = sum(len(r.sections) for r in reports)
    glossed = sum(r.glossed for r in reports)
    return {
        "edition": edition,
        "effective_date": effective,
        "status": "process_support_not_binding",
        "cannot_narrow_core": True,
        "heading_count": total,
        "glossed_count": glossed,
        "files": [
            {
                "file": r.file,
                "title": r.title,
                "heading_count": len(r.sections),
                "glossed_count": r.glossed,
                "sections": [s.as_dict() for s in r.sections],
            }
            for r in reports
        ],
    }


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=".", help="Repository root.")
    p.add_argument("--md-out", default=DEFAULT_MD_OUT, help="Markdown output path (relative to root).")
    p.add_argument("--json-out", default=DEFAULT_JSON_OUT, help="JSON output path (relative to root).")
    mode = p.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="Write the edition files (default).")
    mode.add_argument("--check", action="store_true", help="Fail if the committed edition is stale.")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    md_out = root / args.md_out
    json_out = root / args.json_out
    prefix = "../" * (len(md_out.relative_to(root).parts) - 1)

    edition, effective = read_edition(root)
    reports = [parse_file(root, rel) for rel in CORE_FILES if (root / rel).is_file()]
    markdown = render_markdown(reports, edition, effective, prefix)
    payload = build_payload(reports, edition, effective)
    payload_text = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"

    if args.check:
        stale: list[str] = []
        if not md_out.is_file() or md_out.read_text(encoding="utf-8") != markdown:
            stale.append(args.md_out)
        if not json_out.is_file() or json_out.read_text(encoding="utf-8") != payload_text:
            stale.append(args.json_out)
        if stale:
            print("plain-terms edition is stale; run `make plain-terms-edition`:")
            for rel in stale:
                print(f"  - {rel}")
            return 1
        print(
            f"plain-terms edition is current ({payload['glossed_count']}/{payload['heading_count']} headings glossed)."
        )
        return 0

    md_out.parent.mkdir(parents=True, exist_ok=True)
    md_out.write_text(markdown, encoding="utf-8")
    json_out.write_text(payload_text, encoding="utf-8")
    print(
        f"Wrote {payload['heading_count']} headings ({payload['glossed_count']} glossed) "
        f"to {md_out.relative_to(root)} and {json_out.relative_to(root)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
