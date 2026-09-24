#!/usr/bin/env python3
"""Assemble a GitHub Pages tree that renders numbered core_* files.

Copies are byte-identical to repository sources and live only in the output
directory (default ``_pages_site/``, gitignored). This is not a second
constitution. If a rendered page and the repository file disagree, the
repository file wins. Opening the site is not adoption.

Published pages link to repository files that are not published here
(evidence, evaluation packs, PRE_PUBLICATION_SPEC, and so on). Rewriting those
links would break byte identity, so the builder leaves every copy untouched
and instead fills each gap in the *site*:

* a Markdown target gets a redirect stub at the same path that sends the
  reader to the repository file on GitHub;
* a directory target gets a redirect stub ``index.md`` to the GitHub tree;
* any other file (JSON schemas, a validator script) is copied verbatim.

Links that cannot be served (target missing from the repository, or under a
path Jekyll never publishes, such as ``.github/`` or ``_TEMPLATE.md``) are
reported by ``--check`` as warnings.

CI builds this tree fresh on every deploy (``.github/workflows/pages.yml``).
Run ``--write`` locally only to preview the site; do not regenerate it as part
of an editing pass.

Usage (from the repo root)::

    python3 tools/generate_pages_site.py --root . --write
    python3 tools/generate_pages_site.py --root . --check
"""

from __future__ import annotations

import argparse
import posixpath
import re
import shutil
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import (  # noqa: E402
    ADOPTED_IMPLEMENTATION_WRAPPERS,
    CORE_FILES,
    adopted_implementation_subfiles,
)
from generate_pages_corpus_index import first_heading  # noqa: E402
from generate_plain_terms_edition import read_edition  # noqa: E402

OUT_DEFAULT = "_pages_site"
BLOB = "https://github.com/kfoelsch/Sentient_Constitution/blob/main/"
TREE = "https://github.com/kfoelsch/Sentient_Constitution/tree/main/"
SKIP_NAMES = frozenset({"_TEMPLATE.md"})

FIXED_SUPPORT = (
    "START_HERE.md",
    "README.md",
    "guides/CONCEPTUAL_OVERVIEW.md",
    "guides/RECORD_OVERVIEW.md",
    "LICENSE",
    "AGENTS.md",
    "llms.txt",
    "project/VISION.md",
    "CONTRIBUTING.md",
    "implementation/FAQ.md",
    "implementation/PRINT_PACK.md",
    "implementation/PROCESS_PIPELINES_READER.md",
    "implementation/STEWARD_ENTRY_DOORS.md",
    "doc_architecture/generated/rights_floor_sheet.md",
    "doc_architecture/generated/human_definition_lookup.md",
    "doc_architecture/generated/print_pack.md",
)

SUPPORT_GLOBS = (
    "implementation/adoption/*.md",
    "implementation/adoption/easy_entry/*.md",
)

CONFIG = """\
title: Sentient Constitution
description: Pre-release model constitution. This host renders repository files. It is not a second constitution. Opening it is not adoption.
theme: jekyll-theme-primer
plugins:
  - jekyll-relative-links
  - jekyll-optional-front-matter
  - jekyll-titles-from-headings
  - jekyll-seo-tag
  - jekyll-redirect-from
relative_links:
  enabled: true
  collections: true
optional_front_matter:
  remove_originals: false
titles_from_headings:
  enabled: true
  strip_title: false
"""

INDEX_BANNER = (
    "> This Pages host **renders the same files** as the repository. "
    "It is not a second constitution. If a page here and the repository file "
    "disagree, the **repository file wins**. Opening this site is not adoption. "
    "Public door: [README.md](README.md). Using or adopting it: [START_HERE.md](START_HERE.md)."
)


def publish_list(root: Path) -> list[str]:
    rels: list[str] = []
    seen: set[str] = set()

    def add(rel: str) -> None:
        if rel in seen or Path(rel).name in SKIP_NAMES:
            return
        if (root / rel).is_file():
            seen.add(rel)
            rels.append(rel)

    for rel in CORE_FILES:
        add(rel)
    for rel in ADOPTED_IMPLEMENTATION_WRAPPERS:
        add(rel)
    for rel in adopted_implementation_subfiles(root):
        add(rel)
    for rel in FIXED_SUPPORT:
        add(rel)
    for pattern in SUPPORT_GLOBS:
        for path in sorted(root.glob(pattern)):
            if path.is_file():
                add(path.relative_to(root).as_posix())
    return rels


def copy_sources(root: Path, out: Path, rels: list[str]) -> None:
    for rel in rels:
        dest = out / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / rel, dest)


def localize_index(text: str, published: set[str]) -> str:
    text = text.replace("](../", "](")
    blob_re = re.compile(re.escape(BLOB) + r"([^)\s]+)")

    def repl(match: re.Match[str]) -> str:
        rel = match.group(1)
        path = rel.split("#", 1)[0]
        if path in published:
            return rel
        return match.group(0)

    return blob_re.sub(repl, text)


def insert_banner(text: str) -> str:
    if "renders the same files" in text:
        return text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            close = end + len("\n---")
            return text[:close] + "\n\n" + INDEX_BANNER + "\n" + text[close:]
    return INDEX_BANNER + "\n\n" + text


def render_corpus_index(root: Path, published: list[str]) -> str:
    edition, effective = read_edition(root)
    lines = [
        "---",
        "title: Numbered core files",
        "description: Pages render of numbered core_*. Repository files bind.",
        "---",
        "",
        "# Numbered core files",
        "",
        "This page is **process support**. It is **not** the Constitution. Opening it is not adoption.",
        "",
        f"Corpus edition: `{edition}` · effective **{effective}**",
        "",
        "> These links open files **on this Pages host**. They are copies assembled at build time from the repository. If a page here and the repository file disagree, the repository file wins.",
        "",
        "Auto-generated by `make pages-site`. Do not edit by hand.",
        "",
        "## Binding source",
        "",
    ]
    published_set = set(published)
    for rel in CORE_FILES:
        if rel not in published_set:
            continue
        title = first_heading(root, rel)
        lines.append(f"- [{title}]({rel}) — `{rel}`")
    lines.extend(
        [
            "",
            "## First-hour adopted implementation texts (process support)",
            "",
            "- [README.md](README.md) (public door)",
            "- [START_HERE.md](START_HERE.md) (using or adopting it)",
            "- [Big-picture overview](guides/CONCEPTUAL_OVERVIEW.md)",
            "- [Rights Floor wall sheet](doc_architecture/generated/rights_floor_sheet.md)",
            "- [Print pack](implementation/PRINT_PACK.md)",
            "- [Easy-entry briefs](implementation/adoption/easy_entry/README.md)",
            "- [Process chain](implementation/PROCESS_PIPELINES_READER.md)",
            "- [FAQ](implementation/FAQ.md)",
            "",
        ]
    )
    return "\n".join(lines)


# --- links to repository files that are not published --------------------

INLINE_LINK_RE = re.compile(r'\]\(\s*(?:<([^>\n]+)>|([^)\s]+))(?:\s+"[^"]*")?\s*\)')
REF_LINK_RE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*<?(\S+?)>?(?:\s|$)", re.M)
NON_RELATIVE_RE = re.compile(r"^(?:[a-zA-Z][a-zA-Z0-9+.-]*:|//|/|#)")
DIR_INDEX_NAMES = ("index.md", "README.md")


def relative_link_targets(rel: str, text: str) -> list[str]:
    """Repository-relative paths that ``rel`` links to (fragments dropped)."""
    targets: list[str] = []
    base = posixpath.dirname(rel)
    inline = [a or b for a, b in INLINE_LINK_RE.findall(text)]
    for raw in inline + REF_LINK_RE.findall(text):
        if NON_RELATIVE_RE.match(raw):
            continue
        path = unquote(raw.split("#", 1)[0].split("?", 1)[0])
        if not path:
            continue
        targets.append(posixpath.normpath(posixpath.join(base, path)))
    return targets


def jekyll_excluded(rel: str) -> bool:
    """Jekyll never publishes paths with a component starting with . or _."""
    return any(part[:1] in "._" for part in rel.split("/"))


def classify_link_gaps(root: Path, site_files: set[str]) -> dict[str, dict[str, list[str]]]:
    """Map gap kind -> {target: [linking pages]} for links the site cannot serve.

    Kinds: ``md`` / ``dir`` / ``file`` (fillable) and ``missing`` /
    ``excluded`` / ``outside`` (reported only).
    """
    gaps: dict[str, dict[str, list[str]]] = {}
    for rel in sorted(site_files):
        if not rel.endswith(".md"):
            continue
        text = (root / rel).read_text(encoding="utf-8")
        for target in relative_link_targets(rel, text):
            if target in site_files:
                continue
            if target == ".." or target.startswith("../"):
                kind = "outside"
            elif (root / target).is_dir():
                if any(f"{target}/{n}" in site_files for n in DIR_INDEX_NAMES):
                    continue
                kind = "excluded" if jekyll_excluded(target) else "dir"
            elif (root / target).is_file():
                if jekyll_excluded(target):
                    kind = "excluded"
                elif target.endswith(".md"):
                    kind = "md"
                else:
                    kind = "file"
            else:
                kind = "missing"
            gaps.setdefault(kind, {}).setdefault(target, []).append(rel)
    return gaps


def redirect_stub(title: str, url: str) -> str:
    safe = title.replace('"', "'")
    return (
        "---\n"
        f'title: "{safe}"\n'
        f"redirect_to: {url}\n"
        "sitemap: false\n"
        "---\n\n"
        f"This repository file is not published on this Pages host. "
        f"Open it on GitHub: [{safe}]({url})\n"
    )


def fill_link_gaps(root: Path, out: Path, site_files: set[str]) -> tuple[list[str], dict[str, dict[str, list[str]]]]:
    """Write stubs / verbatim copies for fillable gaps.

    Returns (verbatim-copied rels, unresolved gaps).
    """
    gaps = classify_link_gaps(root, site_files)
    copied: list[str] = []
    for target in sorted(gaps.pop("md", {})):
        dest = out / target
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(redirect_stub(target, BLOB + target), encoding="utf-8")
    for target in sorted(gaps.pop("dir", {})):
        dest = out / target / "index.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(redirect_stub(target + "/", TREE + target), encoding="utf-8")
    for target in sorted(gaps.pop("file", {})):
        dest = out / target
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / target, dest)
        copied.append(target)
    return copied, gaps


def assemble(root: Path, out: Path) -> list[str]:
    """Assemble the site; return every repository file copied into it."""
    return assemble_with_report(root, out)[0]


def assemble_with_report(
    root: Path, out: Path
) -> tuple[list[str], dict[str, dict[str, list[str]]]]:
    """Assemble the site; return (copied files, links the site cannot serve)."""
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    rels = publish_list(root)
    copy_sources(root, out, rels)
    published = set(rels)
    index_src = (root / "docs/index.md").read_text(encoding="utf-8")
    (out / "index.md").write_text(
        insert_banner(localize_index(index_src, published)), encoding="utf-8"
    )
    (out / "corpus_index.md").write_text(
        render_corpus_index(root, rels), encoding="utf-8"
    )
    (out / "_config.yml").write_text(CONFIG, encoding="utf-8")
    copied, unresolved = fill_link_gaps(root, out, set(rels))
    return rels + copied, unresolved


def copies_match(root: Path, out: Path, rels: list[str]) -> list[str]:
    errors: list[str] = []
    for rel in rels:
        src = root / rel
        dest = out / rel
        if not dest.is_file():
            errors.append(f"missing copy: {rel}")
            continue
        if src.read_bytes() != dest.read_bytes():
            errors.append(f"copy drifted: {rel}")
    return errors


def report_unresolved(unresolved: dict[str, dict[str, list[str]]]) -> None:
    labels = {
        "missing": "target not in repository",
        "excluded": "target under a path Jekyll does not publish",
        "outside": "target outside the repository",
    }
    for kind, targets in sorted(unresolved.items()):
        for target, linking in sorted(targets.items()):
            pages = sorted(set(linking))
            print(f"warning: {labels.get(kind, kind)}: {target} (linked from {pages[0]}"
                  + (f" and {len(pages) - 1} more" if len(pages) > 1 else "") + ")")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument("--root", default=".", help="Repository root.")
    p.add_argument("--out", default=OUT_DEFAULT, help="Output directory.")
    mode = p.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="Write assembled site (default).")
    mode.add_argument("--check", action="store_true", help="Assemble in a temp dir and verify copies.")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    if args.check:
        with tempfile.TemporaryDirectory(prefix="pages-site-") as tmp:
            out = Path(tmp) / "site"
            rels, unresolved = assemble_with_report(root, out)
            errors = copies_match(root, out, rels)
            if errors:
                print("pages site check failed:")
                for err in errors:
                    print(f"  {err}")
                return 1
            if not (out / "index.md").is_file() or not (out / "core_00_preamble.md").is_file():
                print("pages site check failed: missing index or Preamble")
                return 1
            report_unresolved(unresolved)
            print(f"pages site is assemblable ({len(rels)} files).")
            return 0
    out = (root / args.out).resolve()
    rels = assemble(root, out)
    errors = copies_match(root, out, rels)
    if errors:
        print("pages site write produced drift:")
        for err in errors:
            print(f"  {err}")
        return 1
    print(f"Wrote {out.relative_to(root)} ({len(rels)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
