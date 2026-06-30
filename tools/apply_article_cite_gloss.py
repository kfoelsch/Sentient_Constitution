#!/usr/bin/env python3
"""Add REF-ARTICLES-GLOSS parenthetical titles to bare Chapter Six article cites."""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PART_FILES = sorted(ROOT.glob("core_06-06_rights_part_*.md"))

HEADING_RE = re.compile(
    r"^#{3,5} Article ([IVXLCDM]+(?:-[A-Z](?:\.\d+)?)?): (.+?)\s*$"
)
LABEL_RE = r"[IVXLCDM]+(?:-[A-Z](?:\.\d+)?)?"
BOLD_CITE_RE = re.compile(rf"\*\*Article ({LABEL_RE})\*\*(?!\s*\(\*)")
LINK_CITE_RE = re.compile(
    rf"\[Article ({LABEL_RE})\]\(([^)]+)\)(?!\s*\(\*)"
)


def load_titles() -> dict[str, str]:
    titles: dict[str, str] = {}
    for path in PART_FILES:
        for line in path.read_text(encoding="utf-8").splitlines():
            match = HEADING_RE.match(line)
            if match:
                titles[match.group(1)] = match.group(2)
    return titles


def gloss_bold(match: re.Match[str], titles: dict[str, str]) -> str:
    label = match.group(1)
    title = titles.get(label)
    if not title:
        return match.group(0)
    return f"**Article {label}** (*{title}*)"


def gloss_link(match: re.Match[str], titles: dict[str, str]) -> str:
    label, url = match.group(1), match.group(2)
    title = titles.get(label)
    if not title:
        return match.group(0)
    return f"[Article {label}]({url}) (*{title}*)"


def process_file(path: pathlib.Path, titles: dict[str, str], dry_run: bool) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    changed = 0
    out: list[str] = []
    for line in lines:
        if HEADING_RE.match(line):
            out.append(line)
            continue
        new_line = BOLD_CITE_RE.sub(lambda m: gloss_bold(m, titles), line)
        new_line = LINK_CITE_RE.sub(lambda m: gloss_link(m, titles), new_line)
        if new_line != line:
            changed += 1
        out.append(new_line)
    if changed and not dry_run:
        path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return changed


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    titles = load_titles()
    total = 0
    for path in PART_FILES:
        n = process_file(path, titles, dry_run)
        print(f"{path.name}: {n} lines updated")
        total += n
    print(f"total: {total} lines")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
