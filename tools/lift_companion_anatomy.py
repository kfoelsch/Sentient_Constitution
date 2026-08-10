#!/usr/bin/env python3
"""Lift companion implementation subfiles onto the core-file reading anatomy.

Each file gains the opening a reader gets from a numbered ``core_*`` file:

1. an ``#`` H1 title;
2. a collapsed **Corpus placement** widget stating layer, binding status, and
   where to start;
3. a one-line statement of what the file owns.

Heading depth is promoted only where a file has a single top-level section, so
band files that carry several sibling clusters keep their existing structure
under a new umbrella title. Anchors are unaffected: markdown slugs derive from
heading text, not depth.

Where a file has one top-level section, its per-section **Definitions ·
Assessment · Compliance** widgets are merged into a single file-level widget
holding the union of their rows, so no Chapter Five jump link is lost.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PLACEMENT_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">Corpus placement '
    "(non-operative): file structure and reading rules</span></strong></summary>"
)
TRACE_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>'
)
DAC_SUMMARY = (
    '<summary><strong><span style="color: #2563eb;">'
    "Definitions · Assessment · Compliance</span></strong></summary>"
)

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
ID_RE = re.compile(r"^((?:CF|CI|CS|CJS)-[0-9]+(?:\.[0-9]+)*[A-Z]?)\b")

LAYERS = {
    "corpus_joint_structure": {
        "wrapper": "corpus_joint_structure.md",
        "wrapper_label": "Joint structure landing page",
        "registry": "cjs_00_registry_and_reading_rules.md",
        "registry_label": "joint-structure registry",
        "descriptor": "joint-structure",
    },
    "corpus_systems": {
        "wrapper": "corpus_systems.md",
        "wrapper_label": "Systems and data landing page",
        "registry": "cs_00_registry_and_reading_rules.md",
        "registry_label": "systems registry",
        "descriptor": "systems",
    },
    "corpus_institutions": {
        "wrapper": "corpus_institutions.md",
        "wrapper_label": "Institutions landing page",
        "registry": "ci_00_registry_and_reading_rules.md",
        "registry_label": "institutions registry",
        "descriptor": "institutional",
    },
    "corpus_forum": {
        "wrapper": "corpus_forum.md",
        "wrapper_label": "Forums landing page",
        "registry": "cf_00_registry_and_reading_rules.md",
        "registry_label": "forums registry",
        "descriptor": "forum",
    },
}

SKIP_NAMES = {
    "cjs_00_registry_and_reading_rules.md",
    "cs_00_registry_and_reading_rules.md",
    "ci_00_registry_and_reading_rules.md",
    "cf_00_registry_and_reading_rules.md",
}


def headings(lines: list[str]) -> list[tuple[int, int, str]]:
    found = []
    fenced = False
    for idx, line in enumerate(lines):
        if line.startswith("```"):
            fenced = not fenced
        if fenced:
            continue
        match = HEADING_RE.match(line)
        if match:
            found.append((idx, len(match.group(1)), match.group(2).strip()))
    return found


def find_blocks(lines: list[str], summary: str) -> list[tuple[int, int]]:
    spans = []
    start = None
    matched = False
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "<details>":
            start = idx
            matched = False
            continue
        if start is not None:
            if summary in line:
                matched = True
            if stripped == "</details>":
                if matched:
                    spans.append((start, idx))
                start = None
                matched = False
    return spans


def title_phrase(title: str) -> tuple[str | None, str]:
    """Split a heading into its stable ID and human phrase."""
    ident = ID_RE.match(title)
    if not ident:
        return None, title.strip()
    rest = title[ident.end() :].lstrip(":").strip()
    return ident.group(1), rest


def placement_widget(layer: str, title: str, ident: str | None, phrase: str) -> list[str]:
    meta = LAYERS[layer]
    if ident:
        holds = f"It holds **{ident}** (*{phrase}*)."
    else:
        holds = f"It holds **{title}**."
    return [
        "<details>",
        PLACEMENT_SUMMARY,
        "",
        "> The following content is **reader guidance only**. It does not add, "
        "remove, or narrow binding obligations in this file or elsewhere.",
        ">",
        f"> This file is **binding incorporated implementation text** where "
        f"[`{meta['wrapper']}`](../{meta['wrapper']}) is incorporated under "
        f"[Chapter Sixteen](../core_16-16_incorporation.md). It must satisfy the "
        f"Sentient Constitution and does not override or narrow it. {holds}",
        ">",
        f"> Start at the [{meta['wrapper_label']}](../{meta['wrapper']}) for reading "
        f"order, or the [{meta['registry_label']}]({meta['registry']}) for identifier "
        f"rules and the family map. Most readers reach this file from a citation "
        f"rather than reading the folder front to back.",
        "",
        "</details>",
    ]


def owner_line(layer: str, ident: str | None, phrase: str, title: str) -> str:
    """One sentence naming what the file owns, with the ID descriptor the
    abbreviation audit requires."""
    if ident and phrase:
        subject = f"**{ident}** (*{phrase}*)"
    elif ident:
        subject = f"**{ident}**"
    else:
        name, _, rest = title.partition(":")
        subject = f"**{name.strip()}** (*{rest.strip()}*)" if rest else f"**{title}**"
    return f"This file is the {LAYERS[layer]['descriptor']} implementation home for {subject}."


def dac_widget(rows: list[str]) -> list[str]:
    return ["<details>", DAC_SUMMARY, "", *rows, "", "</details>"]


def transform(path: Path, layer: str) -> str | None:
    # A leading BOM would hide the first heading from the parser.
    text = path.read_text(encoding="utf-8").lstrip("\ufeff")
    lines = text.splitlines()
    heads = headings(lines)
    if not heads:
        return None
    first_idx, first_level, first_title = heads[0]
    if first_level == 1:
        return None  # already lifted

    # A file that already states its own placement keeps it; a generic widget
    # would only duplicate better, file-specific guidance.
    has_placement = PLACEMENT_SUMMARY in text

    siblings = [h for h in heads[1:] if h[1] == first_level]
    single_section = not siblings

    ident, phrase = title_phrase(first_title)

    dac_spans = find_blocks(lines, DAC_SUMMARY)
    trace_spans = find_blocks(lines, TRACE_SUMMARY)

    merged_rows: list[str] = []
    drop: set[int] = set()
    if single_section and dac_spans:
        seen: set[str] = set()
        for start, end in dac_spans:
            for line in lines[start:end]:
                stripped = line.strip()
                if stripped.startswith("- [") and stripped not in seen:
                    seen.add(stripped)
                    merged_rows.append(stripped)
            drop.update(range(start, end + 1))

    # The file-level Trace is any Trace opening before the second heading.
    boundary = heads[1][0] if len(heads) > 1 else len(lines)
    file_trace = next((s for s in trace_spans if s[0] < boundary), None)

    out: list[str] = []
    for idx, line in enumerate(lines):
        if idx in drop:
            continue

        if idx == first_idx:
            out.append(f"# {first_title}")
            if not has_placement:
                out.append("")
                out.extend(placement_widget(layer, first_title, ident, phrase))
                out.append("")
                out.append("<br>")
                out.append("")
                out.append(owner_line(layer, ident, phrase, first_title))
                out.append("")
                out.append("<br>")
                out.append("")
            continue

        match = HEADING_RE.match(line)
        if match and single_section and idx != first_idx:
            level = len(match.group(1))
            if level > first_level:
                out.append(f"{'#' * (level - 1)} {match.group(2).strip()}")
                continue

        out.append(line)

        # Attach the merged definition widget directly after the file Trace.
        if file_trace and idx == file_trace[1] and merged_rows:
            out.append("")
            out.extend(dac_widget(merged_rows))

    result = "\n".join(out)

    if merged_rows and not file_trace:
        # No file-level Trace to anchor to: place the widget under the owner line.
        anchor = result.find("<br>", result.find("</details>"))
        anchor = result.find("<br>", anchor + 4)
        if anchor != -1:
            insert = anchor + len("<br>")
            block = "\n\n" + "\n".join(dac_widget(merged_rows))
            result = result[:insert] + block + result[insert:]

    result = re.sub(r"\n{3,}", "\n\n", result)
    # Drop widget spacers that no longer follow a widget.
    result = re.sub(r"(^#{1,6} .*\n)\n*<br>\n+", r"\1\n", result, flags=re.M)
    # Keep a spacer after the last widget in the file-top stack.
    result = re.sub(r"(</details>\n)\n*(?=#{1,6} )", r"\1\n<br>\n\n", result)
    result = re.sub(r"\n{3,}", "\n\n", result)
    if not result.endswith("\n"):
        result += "\n"
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--layer")
    parser.add_argument("--file", help="Transform a single file (relative path).")
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()

    if args.file:
        targets = [root / args.file]
    else:
        layers = [args.layer] if args.layer else list(LAYERS)
        targets = []
        for layer in layers:
            targets.extend(sorted((root / layer).glob("*.md")))

    count = 0
    for path in targets:
        if path.name in SKIP_NAMES:
            continue
        layer = path.parent.name
        if layer not in LAYERS:
            continue
        result = transform(path, layer)
        if result is None:
            continue
        count += 1
        rel = path.relative_to(root).as_posix()
        print(f"{'lifted' if args.write else 'would lift'} {rel}")
        if args.write:
            path.write_text(result, encoding="utf-8")

    print(f"\n{count} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
