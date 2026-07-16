#!/usr/bin/env python3
"""Add REF-ARTICLES-GLOSS parenthetical titles to bare Chapter Six article cites."""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

from corpus_paths import binding_corpus_scope

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
BARE_CITE_RE = re.compile(
    rf"(?<!this )(?<!\[)(?<!\*\*)\bArticle ({LABEL_RE})\b(?!\s*\(\*)"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default=".",
        help="Workspace root. Defaults to current directory.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report changes without writing files.",
    )
    return parser.parse_args()


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


def gloss_bare(match: re.Match[str], titles: dict[str, str]) -> str:
    label = match.group(1)
    title = titles.get(label)
    if not title:
        return match.group(0)
    return f"**Article {label}** (*{title}*)"


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
        new_line = BARE_CITE_RE.sub(lambda m: gloss_bare(m, titles), new_line)
        if new_line != line:
            changed += 1
        out.append(new_line)
    if changed and not dry_run:
        path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return changed


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve()
    titles = load_titles()
    scope = binding_corpus_scope(root)
    total = 0
    for rel_path in scope:
        path = root / rel_path
        if not path.is_file():
            continue
        n = process_file(path, titles, args.dry_run)
        if n:
            print(f"{rel_path}: {n} lines updated")
            total += n
    print(f"total: {total} lines")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
