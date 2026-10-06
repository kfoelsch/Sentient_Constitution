#!/usr/bin/env python3
"""Add REF-ARTICLES-GLOSS parenthetical titles to bare Chapter Six article cites.

Default mode rewrites files. ``--check`` is the audit form: it reports bare
cites without writing and exits 1 on any finding. ``--check --changed-only``
limits the report to lines added versus HEAD (the form wired into
``make regression`` as ``article-cite-gloss-audit``) so legacy cites do not
block until those lines are edited.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

from corpus_paths import binding_corpus_scope
from corpus_ref_name_audit import added_line_numbers

ROOT = pathlib.Path(__file__).resolve().parents[1]
PART_FILES = sorted(ROOT.glob("core_06_rights_part_*.md"))

HEADING_RE = re.compile(
    r"^#{3,5} Article ([IVXLCDM]+(?:-[A-Z](?:\.\d+)?)?): (.+?)\s*$"
)
LABEL_RE = r"[IVXLCDM]+(?:-[A-Z](?:\.\d+)?)?"
# Skip a bold cite that is already glossed, either directly after it or after
# the closing link: ``[**Article XI**](url) (*Title*)`` must not gain a second gloss.
BOLD_CITE_RE = re.compile(
    rf"\*\*Article ({LABEL_RE})\*\*(?!\s*\(\*)(?!\]\([^)]*\)\s*\(\*)"
)
# Repair links that already carry a gloss inside the link text and repeat it after.
DUP_GLOSS_RE = re.compile(
    r"(\[[^\]]*\(\*(?P<t>[^*()]+)\*\)\]\([^)]*\))\s*\(\*(?P=t)\*\)"
)
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
        "--check",
        action="store_true",
        help="Audit mode: list bare article cites, write nothing, exit 1 if any.",
    )
    parser.add_argument(
        "--changed-only",
        action="store_true",
        help="With --check: only report lines added versus HEAD.",
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


GENERATED_LABEL_ROW_RE = re.compile(r"^\|\s*(?:CS|CI|CJS|CF)-\d+[A-Za-z]?(?:\.\d+)*:")
GLOSS_SPAN_RE = re.compile(r"\(\*.*?\*\)")


def gloss_line(line: str, titles: dict[str, str]) -> str:
    """Gloss bare Article cites in ``line``, skipping text inside ``(*...*)``.

    An existing gloss can legitimately mention an Article (for example the
    CI-19 name ``... Article VII-E (...) interface``); rewriting inside it
    would corrupt the gloss, and a name inserted by another tool would be
    re-flagged here forever. Glosses are swapped for ``(*\x00N\x00*)``
    placeholders so a cite followed by a gloss still reads as glossed.
    """
    if GENERATED_LABEL_ROW_RE.match(line):
        return line  # generated index rows carry a section title, not a cite
    saved: list[str] = []

    def stash(match: re.Match[str]) -> str:
        saved.append(match.group(0))
        return f"(*\x00{len(saved) - 1}\x00*)"

    text = GLOSS_SPAN_RE.sub(stash, line)
    text = BOLD_CITE_RE.sub(lambda m: gloss_bold(m, titles), text)
    text = LINK_CITE_RE.sub(lambda m: gloss_link(m, titles), text)
    text = BARE_CITE_RE.sub(lambda m: gloss_bare(m, titles), text)
    return re.sub(r"\(\*\x00(\d+)\x00\*\)", lambda m: saved[int(m.group(1))], text)


def process_file(path: pathlib.Path, titles: dict[str, str], dry_run: bool) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    changed = 0
    out: list[str] = []
    for line in lines:
        if HEADING_RE.match(line):
            out.append(line)
            continue
        new_line = gloss_line(line, titles)
        if new_line != line:
            changed += 1
        out.append(new_line)
    if changed and not dry_run:
        path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return changed


def check_file(
    path: pathlib.Path,
    titles: dict[str, str],
    only_lines: set[int] | None,
) -> list[tuple[int, str]]:
    """Return (line number, line) for each line the fixer would gloss."""
    findings: list[tuple[int, str]] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if only_lines is not None and number not in only_lines:
            continue
        if HEADING_RE.match(line):
            continue
        new_line = gloss_line(line, titles)
        if new_line != line:
            findings.append((number, line))
    return findings


def run_check(root: pathlib.Path, titles: dict[str, str], changed_only: bool) -> int:
    scope = [p for p in binding_corpus_scope(root) if (root / p).is_file()]
    changed: dict[str, set[int]] | None = None
    if changed_only:
        changed = added_line_numbers(root, set(scope))
        scope = [p for p in scope if p in changed]
    total = 0
    for rel_path in scope:
        only = changed.get(rel_path) if changed is not None else None
        for number, _line in check_file(root / rel_path, titles, only):
            print(f"  {rel_path}:{number}: REF-ARTICLES-GLOSS: bare Article cite; "
                  "add (*title*) (run tools/apply_article_cite_gloss.py to fix)")
            total += 1
    mode = "changed-only" if changed_only else "full"
    if total:
        print(f"FAIL: REF-ARTICLES-GLOSS ({mode}) — {total} line(s) with bare Article cites.")
        return 1
    print(f"PASS: REF-ARTICLES-GLOSS ({mode}) — Article cites carry their titles.")
    return 0


def main() -> int:
    args = parse_args()
    root = pathlib.Path(args.root).resolve()
    titles = load_titles()
    if args.check:
        return run_check(root, titles, args.changed_only)
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
