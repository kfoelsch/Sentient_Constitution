#!/usr/bin/env python3
"""Pre-release fragment policy: one current id per heading; no fossil aliases.

Fails when a numbered heading still carries leftover fragment ids from an
earlier number or title, or when companion family headings still keep the
pre-promotion ``#2-…`` id beside ``#cs-4-2-…``. ``--write`` retargets live
citations to the current id and removes the leftover ``<a id>`` tags.

Archive and dated evidence files are left as historical record.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope  # noqa: E402
from generate_id_resolver import build_aliases  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RULE = "NAV-PRE-RELEASE-FRAGMENT-01"

ANCHOR_LINE_RE = re.compile(r'^<a id="([^"]+)"></a>\s*$')
ANCHOR_TAG_RE = re.compile(r'<a id="([^"]+)"></a>')
FAMILY_HEADING_RE = re.compile(
    r"^(#{2,3})\s+(CS|CI|CF|CJS)-(\d+)\.(\d+)\b", re.I
)
MD_LINK_RE = re.compile(
    r"\]\(\s*(?P<target><[^>\n]+>|[^)\s]+)"
    r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"
)
JSON_HREF_RE = re.compile(
    r'(?P<prefix>"href"\s*:\s*")(?P<href>[^"]+)(?P<suffix>")'
)
SKIP_PREFIXES = (
    "archive/",
    "evidence/",
    "ai_corpus/indexes/",
    "ai_corpus/visualization/",
    "doc_architecture/generated/",
    "evaluation/results/",
)
STEWARD_CARDS = "implementation/STEWARD_ENTRY_DOORS.md"
STEWARD_EXTRAS = (
    "duty-to-resist",
    "minimum-inspectable-action-set",
)
STEWARD_CURRENT = "shared-refusal-and-logging"


@dataclass(frozen=True)
class Prune:
    file: str
    fossil: str
    current: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument(
        "--write",
        action="store_true",
        help="Retarget citations and remove leftover fragment ids.",
    )
    return parser.parse_args()


def live_text_files(root: Path) -> list[Path]:
    names = list(binding_corpus_scope(root, include_support_docs=True))
    extras = [
        *sorted(root.glob("implementation/**/*.md")),
        *sorted(root.glob("implementation/**/*.json")),
        *sorted(root.glob("evaluation/**/*.md")),
        *sorted(root.glob(".cursor/rules/*.mdc")),
        *sorted(root.glob("ai_corpus/*.md")),
        *sorted(root.glob("tools/*.md")),
        root / "CONSTITUTIONAL_REGRESSION_SCENARIOS.md",
    ]
    names.extend(
        path.relative_to(root).as_posix()
        for path in extras
        if path.is_file()
    )
    seen: set[str] = set()
    out: list[Path] = []
    for rel in names:
        if rel in seen or rel.startswith(SKIP_PREFIXES):
            continue
        seen.add(rel)
        path = root / rel
        if path.is_file():
            out.append(path)
    return out


def companion_heading_prunes(root: Path) -> list[Prune]:
    prunes: list[Prune] = []
    for rel in binding_corpus_scope(root):
        path = root / rel
        if not path.is_file():
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        pending: list[str] = []
        for line in lines:
            stripped = line.strip()
            anchor = ANCHOR_LINE_RE.match(stripped)
            if anchor:
                pending.append(anchor.group(1))
                continue
            heading = FAMILY_HEADING_RE.match(stripped)
            if heading and pending:
                family, major, minor = heading.group(2).lower(), heading.group(3), heading.group(4)
                prefix = f"{family}-{major}-{minor}-"
                exact = f"{family}-{major}-{minor}"
                current_ids = [
                    item
                    for item in pending
                    if item == exact or item.startswith(prefix)
                ]
                current = current_ids[0] if current_ids else None
                if current:
                    for item in pending:
                        if item != current:
                            prunes.append(Prune(rel, item, current))
                pending = []
                continue
            if stripped:
                pending = []
    return prunes


def collect_prunes(root: Path) -> list[Prune]:
    prunes: list[Prune] = []
    seen: set[tuple[str, str]] = set()

    def add(item: Prune) -> None:
        key = (item.file, item.fossil)
        if key in seen or item.fossil == item.current:
            return
        seen.add(key)
        prunes.append(item)

    for row in build_aliases(root):
        currents = [item.lstrip("#") for item in row.get("current_anchors") or []]
        if not currents:
            continue
        current = currents[0]
        for fossil in row.get("fossil_anchors") or []:
            add(Prune(row["file"], fossil.lstrip("#"), current))

    for item in companion_heading_prunes(root):
        add(item)

    cards_path = root / STEWARD_CARDS
    cards = cards_path.read_text(encoding="utf-8") if cards_path.is_file() else ""
    for fossil in STEWARD_EXTRAS:
        if f'id="{fossil}"' in cards:
            add(Prune(STEWARD_CARDS, fossil, STEWARD_CURRENT))
    return prunes


def mapping_for(prunes: list[Prune]) -> dict[str, dict[str, str]]:
    by_file: dict[str, dict[str, str]] = {}
    for item in prunes:
        by_file.setdefault(item.file, {})[item.fossil] = item.current
    return by_file


def resolve_link_file(root: Path, source: Path, target: str) -> str | None:
    raw = target.strip()
    if raw.startswith("<") and raw.endswith(">"):
        raw = raw[1:-1]
    if raw.startswith(("http://", "https://", "mailto:")):
        return None
    path_part, hash_sep, _frag = raw.partition("#")
    if not hash_sep:
        return None
    if not path_part:
        return source.relative_to(root).as_posix()
    root_resolved = root.resolve()
    candidates = [
        (source.parent / path_part).resolve(),
        (root / path_part).resolve(),
    ]
    for dest in candidates:
        try:
            rel = dest.relative_to(root_resolved).as_posix()
        except ValueError:
            continue
        if dest.is_file() or (root / rel).is_file():
            return rel
    return None


def retarget_markdown(root: Path, path: Path, text: str, by_file: dict[str, dict[str, str]]) -> str:
    def repl(match: re.Match[str]) -> str:
        target = match.group("target")
        rel = resolve_link_file(root, path, target)
        if rel is None:
            return match.group(0)
        fossils = by_file.get(rel)
        if not fossils:
            return match.group(0)
        path_part, hash_sep, frag = target.partition("#")
        if not hash_sep or frag not in fossils:
            return match.group(0)
        return match.group(0).replace("#" + frag, "#" + fossils[frag], 1)

    return MD_LINK_RE.sub(repl, text)


def retarget_json_hrefs(root: Path, path: Path, text: str, by_file: dict[str, dict[str, str]]) -> str:
    def repl(match: re.Match[str]) -> str:
        href = match.group("href")
        rel = resolve_link_file(root, path, href)
        if rel is None:
            return match.group(0)
        fossils = by_file.get(rel)
        if not fossils:
            return match.group(0)
        _path, hash_sep, frag = href.partition("#")
        if not hash_sep or frag not in fossils:
            return match.group(0)
        return (
            match.group("prefix")
            + href.replace("#" + frag, "#" + fossils[frag], 1)
            + match.group("suffix")
        )

    return JSON_HREF_RE.sub(repl, text)


def strip_anchor_tags(text: str, fossils: set[str]) -> str:
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    for line in lines:
        stripped = line.strip()
        match = ANCHOR_LINE_RE.match(stripped)
        if match and match.group(1) in fossils:
            continue
        def drop_tag(tag: re.Match[str]) -> str:
            return "" if tag.group(1) in fossils else tag.group(0)

        new = ANCHOR_TAG_RE.sub(drop_tag, line)
        if new.strip() or not ANCHOR_TAG_RE.search(line):
            out.append(new)
    return "".join(out)


def apply_prunes(root: Path, prunes: list[Prune]) -> int:
    by_file = mapping_for(prunes)
    changed = 0
    for path in live_text_files(root):
        original = path.read_text(encoding="utf-8")
        updated = retarget_markdown(root, path, original, by_file)
        if path.suffix == ".json":
            updated = retarget_json_hrefs(root, path, updated, by_file)
        rel = path.relative_to(root).as_posix()
        fossils = set(by_file.get(rel, {}))
        if fossils:
            updated = strip_anchor_tags(updated, fossils)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    return changed


def remaining_citations(root: Path, prunes: list[Prune]) -> list[str]:
    by_file = mapping_for(prunes)
    findings: list[str] = []
    for path in live_text_files(root):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root).as_posix()
        for match in MD_LINK_RE.finditer(text):
            target = match.group("target")
            dest = resolve_link_file(root, path, target)
            if dest is None:
                continue
            fossils = by_file.get(dest)
            if not fossils:
                continue
            _path, hash_sep, frag = target.partition("#")
            if hash_sep and frag in fossils:
                line = text[: match.start()].count("\n") + 1
                findings.append(
                    f"{rel}:{line}: citation still uses leftover #{frag}; "
                    f"use #{fossils[frag]} ({RULE})"
                )
        if path.suffix == ".json":
            for match in JSON_HREF_RE.finditer(text):
                href = match.group("href")
                dest = resolve_link_file(root, path, href)
                if dest is None:
                    continue
                fossils = by_file.get(dest)
                if not fossils:
                    continue
                _path, hash_sep, frag = href.partition("#")
                if hash_sep and frag in fossils:
                    line = text[: match.start()].count("\n") + 1
                    findings.append(
                        f"{rel}:{line}: citation still uses leftover #{frag}; "
                        f"use #{fossils[frag]} ({RULE})"
                    )
        if rel in by_file:
            for match in ANCHOR_LINE_RE.finditer(text):
                fossil = match.group(1)
                if fossil in by_file[rel]:
                    line = text[: match.start()].count("\n") + 1
                    findings.append(
                        f"{rel}:{line}: leftover fragment #{fossil}; current is "
                        f"#{by_file[rel][fossil]} ({RULE})"
                    )
    return findings


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    prunes = collect_prunes(root)
    if args.write:
        changed = apply_prunes(root, prunes)
        prunes = collect_prunes(root)
        leftovers = remaining_citations(root, prunes)
        if leftovers:
            print("Fossil-anchor prune left unresolved items:", file=sys.stderr)
            for item in leftovers:
                print(f"  - {item}", file=sys.stderr)
            return 1
        print(
            f"Pruned leftover fragments in {changed} file(s); "
            "current ids only."
        )
        return 0

    leftovers = remaining_citations(root, prunes)
    if not prunes and not leftovers:
        print("PASS: no leftover fossil or legacy fragment ids.")
        return 0
    print(
        f"FAIL: {len(prunes)} leftover fragment id(s); "
        "pre-release keeps current numbering only.",
        file=sys.stderr,
    )
    for item in prunes[:40]:
        print(
            f"  - {item.file}: #{item.fossil} → #{item.current}",
            file=sys.stderr,
        )
    if len(prunes) > 40:
        print(f"  - … {len(prunes) - 40} more", file=sys.stderr)
    for item in leftovers[:20]:
        print(f"  - {item}", file=sys.stderr)
    print(f"Re-run with --write to retarget and strip. ({RULE})", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
