#!/usr/bin/env python3
"""Repair local Markdown links in translations (link repair only; no text is retranslated).

For every translated file (and each locale README) this tool looks at the local
links that the link audit cannot resolve and rewrites only those links:

1. The file part. A historical English file name (any earlier numbering scheme,
   found from the git rename history, the chapter-number registry, or a
   layer-and-slug match) is mapped to the current English file. If the locale
   has a translation of that file, the link points at the translation;
   otherwise it points at the English file with a ``../../`` path.
2. The fragment. A fragment that no longer exists in the English file is
   replaced by the one anchor whose heading text matches once the old section
   number is ignored; if there is none, the fragment is dropped and the link
   goes to the file (listed in the report for review). A link into a
   translation keeps the English fragment by adding ``<a id="...">`` above the
   aligned translated heading (matched by section number, or by position when
   both files have the same heading outline); if the heading cannot be aligned
   the link goes to the English file instead.

Dry run by default; ``--write`` applies the changes. The report lists every
fragment that was dropped and every link sent to English because no aligned
translated heading was found.
"""

from __future__ import annotations

import argparse
import collections
import html
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))

import local_markdown_fragment_audit as mk  # noqa: E402
import translation_audit as ta  # noqa: E402

ROOT = ta.ROOT
SLUG_ALIASES = (("segregation", "separation"),)
_PREFIX_RE = re.compile(r"^(?:[a-z]+-)?\d[0-9a-z]*-")  # "63-", "cjs-5125-", "113-"
_NUM_HEAD_RE = re.compile(r"^(?:§\s*)?(\d+(?:\.\d+)*)\.?(?:\s|$)")
_ROMAN_RE = re.compile(r"\b([IVXL]{1,6}(?:-[A-Z])?)\b")
_LAYER_RE = re.compile(r"^([a-z]+)_(?:[0-9][0-9a-z.\-]*_)(.+)$")


# --- file resolution -------------------------------------------------------

def rename_history() -> dict[str, str]:
    """Return {old basename: current repo path} from git rename history."""
    out = subprocess.check_output(
        ["git", "log", "--reverse", "--name-status", "-M", "--format=@%H", "--diff-filter=R"],
        cwd=ROOT, text=True,
    )
    events: list[tuple[str, str]] = []
    for line in out.splitlines():
        if line.startswith("R"):
            _status, old, new = line.split("\t")
            events.append((old, new))
    index: dict[str, list[int]] = collections.defaultdict(list)
    for i, (old, _new) in enumerate(events):
        index[old].append(i)

    def forward(path: str, pos: int) -> str:
        while True:
            later = [j for j in index.get(path, []) if j > pos]
            if not later:
                return path
            pos = later[0]
            path = events[pos][1]

    result: dict[str, str] = {}
    for i, (old, new) in enumerate(events):
        final = forward(new, i)
        if (ROOT / final).is_file():
            result[os.path.basename(old)] = final
    return result


def layer_slug_index() -> dict[tuple[str, str], list[str]]:
    index: dict[tuple[str, str], list[str]] = collections.defaultdict(list)
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(("translations/", "_pages_site/", "archive/", "evidence/", ".git/")):
            continue
        m = _LAYER_RE.match(path.name)
        if m:
            index[(m.group(1), m.group(2))].append(rel)
    return index


class Resolver:
    def __init__(self) -> None:
        self.history = rename_history()
        self.layer_slug = layer_slug_index()

    def english(self, rel: str) -> Path | None:
        """Map a link path (possibly historical) to a current English file."""
        stripped = rel
        while stripped.startswith("../"):
            stripped = stripped[3:]
        if stripped and (ROOT / stripped).is_file() and not stripped.startswith("translations/"):
            return ROOT / stripped
        name = os.path.basename(rel)
        if (ROOT / name).is_file():
            return ROOT / name
        mapped = ta.canonical_core_path(ROOT / name)
        if mapped.is_file():
            return mapped
        final = self.history.get(name)
        if final:
            return ROOT / final
        m = _LAYER_RE.match(name)
        if m:
            slug = m.group(2)
            for old, new in SLUG_ALIASES:
                slug = slug.replace(old, new)
            hits = self.layer_slug.get((m.group(1), slug))
            if hits and len(hits) == 1:
                return ROOT / hits[0]
        m2 = re.match(r"^([a-z]+)_(.+)$", name)
        if m2:
            slug = m2.group(2)
            for old, new in SLUG_ALIASES:
                slug = slug.replace(old, new)
            hits = self.layer_slug.get((m2.group(1), slug))
            if hits and len(hits) == 1:
                return ROOT / hits[0]
        return None


# --- anchors and headings --------------------------------------------------

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class Anchors:
    def __init__(self) -> None:
        self.cache: dict[Path, tuple[set[str], set[str], dict[str, str]]] = {}

    def info(self, path: Path) -> tuple[set[str], set[str], dict[str, str]]:
        if path not in self.cache:
            self.cache[path] = mk.anchor_info(read(path))
        return self.cache[path]

    def get(self, path: Path) -> set[str]:
        return self.info(path)[0]

    def drop(self, path: Path) -> None:
        self.cache.pop(path, None)


def strip_prefix(slug: str) -> str:
    previous = None
    while previous != slug:
        previous = slug
        slug = _PREFIX_RE.sub("", slug, count=1)
    return slug


def fix_fragment(frag: str, info: tuple[set[str], set[str], dict[str, str]]) -> str | None:
    """Return the current anchor for a stale English fragment, or None."""
    anchors, heading_slugs, _ids = info
    if frag in anchors:
        return frag
    for old, new in SLUG_ALIASES:
        swapped = frag.replace(old, new)
        if swapped in anchors:
            return swapped
    key = strip_prefix(frag)
    if len(key) < 6:
        return None
    for pool in (heading_slugs, anchors):
        hits = [a for a in pool if strip_prefix(a) == key]
        if len(hits) == 1:
            return hits[0]
    return None


def headings(text: str) -> list[dict]:
    """ATX headings outside fences: level, text, github slug (deduplicated), line index."""
    lines = text.split("\n")
    result: list[dict] = []
    used: set[str] = set()
    counters: dict[str, int] = {}
    fence = None
    for i, line in enumerate(lines):
        m = mk.FENCE_RE.match(line)
        if m:
            marker = m.group(1)[0]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            continue
        if fence:
            continue
        atx = mk.ATX_HEADING_RE.match(line)
        if not atx or atx.group(2) is None:
            continue
        base = mk.github_slug(atx.group(2))
        slug, n = base, counters.get(base, 1)
        while slug in used:
            slug = f"{base}-{n}"
            n += 1
        used.add(slug)
        counters[base] = n
        result.append({"level": len(atx.group(1)), "text": atx.group(2), "slug": slug, "line": i})
    return result


def heading_key(h: dict, english: bool) -> tuple | None:
    text = re.sub(r"[*_`]", "", h["text"]).strip()
    m = _NUM_HEAD_RE.match(text)
    if m:
        return ("n", h["level"], m.group(1))
    if english and re.match(r"^Article\b", text):
        m = _ROMAN_RE.search(text[8:40])
        if m:
            return ("a", h["level"], m.group(1))
    if not english:
        m = _ROMAN_RE.search(text[:40])
        if m and re.search(r"[A-Za-z]", text) is not None and re.match(r"^\W*\S+\s+[IVXL]", text):
            return ("a", h["level"], m.group(1))
    return None


class Aligner:
    """Map an English anchor to the line index of the aligned translated heading."""

    def __init__(self) -> None:
        self.cache: dict[tuple[Path, Path], dict[str, int]] = {}

    def align(self, english: Path, translation: Path) -> dict[str, int]:
        key = (english, translation)
        if key in self.cache:
            return self.cache[key]
        e = headings(read(english))
        t = headings(read(translation))
        mapping: dict[str, int] = {}
        id_to_heading = mk.anchor_info(read(english))[2]
        if [h["level"] for h in e] == [h["level"] for h in t]:
            for eh, th in zip(e, t):
                mapping[eh["slug"]] = th["line"]
        else:
            ekeys = collections.defaultdict(list)
            tkeys = collections.defaultdict(list)
            for h in e:
                k = heading_key(h, True)
                if k:
                    ekeys[k].append(h)
            for h in t:
                k = heading_key(h, False)
                if k:
                    tkeys[k].append(h)
            for k, ehs in ekeys.items():
                ths = tkeys.get(k, [])
                if len(ehs) == 1 and len(ths) == 1:
                    mapping[ehs[0]["slug"]] = ths[0]["line"]
        for ident, slug in id_to_heading.items():
            if slug in mapping and ident not in mapping:
                mapping[ident] = mapping[slug]
        self.cache[key] = mapping
        return mapping


# --- main repair -----------------------------------------------------------

def rel_posix(target: Path, start: Path) -> str:
    return Path(os.path.relpath(target, start)).as_posix()


def locale_counterparts(locale: str) -> dict[Path, Path]:
    pairs, _ = ta.translation_pairs(locale)
    return {ROOT / p.source: ROOT / p.translation for p in pairs}


def process_locale(locale: str, write: bool, report: list[str]) -> collections.Counter:
    resolver, anchors, aligner = RESOLVER, ANCHORS, ALIGNER
    counterpart = locale_counterparts(locale)
    pairs, _ = ta.translation_pairs(locale)
    sources = {ROOT / p.translation: ROOT / p.source for p in pairs}
    files = [ROOT / p.translation for p in pairs] + [ROOT / "translations" / locale / "README.md"]
    stats: collections.Counter = collections.Counter()
    injections: dict[Path, dict[str, int]] = collections.defaultdict(dict)  # file -> {id: heading line}

    for sp in files:
        text = read(sp)
        lines = text.split("\n")
        edits: dict[int, list[tuple[str, str]]] = collections.defaultdict(list)
        for link in mk.links_in(sp, text):
            raw = link.raw_target
            u = urlsplit(raw)
            if u.scheme or u.netloc or raw.startswith("//"):
                continue
            rel = unquote(u.path)
            frag = unquote(u.fragment) if u.fragment else None
            target = (sp if not rel else sp.parent / rel).resolve()
            target = ta.canonical_core_path(target)
            if target.is_file():
                ok = (not frag) or target.suffix.lower() != ".md" or frag in anchors.get(target)
                if ok:
                    continue
                # target exists; only the fragment is stale
                if "translations" in target.parts:
                    english = sources.get(target)
                    is_translation = True
                else:
                    english = target
                    is_translation = False
            else:
                english = resolver.english(rel) if rel else None
                if english is None:
                    stats["unmapped"] += 1
                    report.append(f"UNMAPPED {sp.relative_to(ROOT)}:{link.line} {raw}")
                    continue
                is_translation = False
            new_frag = None
            if frag:
                new_frag = fix_fragment(frag, anchors.info(english)) if english.suffix == ".md" else frag
                if new_frag is None:
                    stats["fragment-dropped"] += 1
                    report.append(f"DROPPED {sp.relative_to(ROOT)}:{link.line} {raw} (no matching heading in {english.name})")
            # choose local translation or English
            local = target if is_translation else counterpart.get(english)
            if local is not None and local.is_file():
                local_name = "" if (local == sp and new_frag) else local.name
                if new_frag is None or new_frag in anchors.get(local):
                    new_target = local_name + (f"#{new_frag}" if new_frag else "")
                    stats["to-translation"] += 1
                else:
                    line_idx = aligner.align(english, local).get(new_frag)
                    if line_idx is not None:
                        injections[local][new_frag] = line_idx
                        new_target = local_name + f"#{new_frag}"
                        stats["to-translation+anchor"] += 1
                    else:
                        new_target = rel_posix(english, sp.parent) + f"#{new_frag}"
                        stats["to-english(unaligned)"] += 1
                        report.append(f"ENGLISH {sp.relative_to(ROOT)}:{link.line} {raw} -> {new_target}")
            else:
                new_target = rel_posix(english, sp.parent) + (f"#{new_frag}" if new_frag else "")
                stats["to-english"] += 1
            if new_target != raw:
                edits[link.line].append((raw, new_target))
        if edits and write:
            for line_no, subs in edits.items():
                s = lines[line_no - 1]
                for old, new in subs:
                    s = s.replace(f"]({old})", f"]({new})").replace(f"](<{old}>)", f"](<{new}>)")
                    if re.match(r"^\s{0,3}\[[^\]]+\]:", s):
                        s = s.replace(f" {old}", f" {new}", 1) if f" {old}" in s else s
                lines[line_no - 1] = s
            sp.write_text("\n".join(lines), encoding="utf-8")
            ANCHORS.drop(sp)
        stats["links-rewritten"] += sum(len(v) for v in edits.values())

    if write:
        for path, wanted in injections.items():
            body = read(path).split("\n")
            existing = mk.anchor_info("\n".join(body))[0]
            for ident, line_idx in sorted(wanted.items(), key=lambda kv: -kv[1]):
                if ident in existing:
                    continue
                body[line_idx:line_idx] = [f'<a id="{ident}"></a>', ""]
            path.write_text("\n".join(body), encoding="utf-8")
            ANCHORS.drop(path)
            stats["anchors-added"] += len(wanted)
    else:
        stats["anchors-added"] += sum(len(v) for v in injections.values())
    return stats


RESOLVER = ALIGNER = ANCHORS = None  # type: ignore


def main() -> int:
    global RESOLVER, ALIGNER, ANCHORS
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--locale", help="one locale (default: all)")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--report", default="")
    args = ap.parse_args()
    RESOLVER, ALIGNER, ANCHORS = Resolver(), Aligner(), Anchors()
    report: list[str] = []
    total: collections.Counter = collections.Counter()
    for directory in ta.locale_dirs(args.locale):
        stats = process_locale(directory.name, args.write, report)
        total.update(stats)
        print(directory.name, dict(stats))
    print("TOTAL", dict(total))
    if args.report:
        Path(args.report).write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"{'wrote' if args.write else 'dry run (use --write)'}; report lines: {len(report)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
