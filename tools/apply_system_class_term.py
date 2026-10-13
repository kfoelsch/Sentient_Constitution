#!/usr/bin/env python3
"""TERM-SYSTEM-CLASS-01: say "system class", not a bare "class".

Chapter Nine (and any other file passed with ``--files``) names the tier a
system is sorted into its *system class*. A bare "class" is ambiguous for a
reader who has not met the term, so prose and headings say "system class".

What the tool leaves alone:

* named levels: ``Class A``, ``Class B``, ``Classes A, B, and C``, ``Class P``;
* terms already qualified: ``system class``, ``system's class``, ``impact class``,
  ``risk class``, and the generic ``class of ...``;
* link targets, anchor ids, inline code, bare URLs, HTML tags, and fenced blocks.

Casing follows the text: ``class`` -> ``system class``; ``Class`` at the start of a
sentence -> ``System class``; ``Class`` inside a title-cased phrase (``Class
Scaling and Escalation``) -> ``System Class``. A heading the tool changes is put in
Chicago headline case (``Illustrative System Class Profiles (Non-Exhaustive)``);
link text that quotes the old heading gets the new one.

Renaming a heading changes its fragment id (``#513-class-scaling-and-escalation``).
The tool renames the ``<a id>`` above the heading and retargets every link in the
live corpus that points at it, and rewrites that link's text the same way so link
text keeps matching the heading (``section-cite-name-audit``).

Default mode rewrites files. ``--dry-run`` reports what would change and writes
nothing. ``--check`` is the audit form: it lists lines that still carry a bare
"class" and exits 1 on any finding; ``--check --changed-only`` limits it to lines
added versus HEAD. Spots the tool will not decide alone (``class-wide``,
``substrate- and class-level``) are printed as REVIEW and never rewritten.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

from corpus_ref_name_audit import added_line_numbers
from local_markdown_fragment_audit import github_slug
from fossil_anchor_audit import live_text_files, resolve_link_file

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_GLOB = "core_08*.md"

CLASS_RE = re.compile(r"(?<![\w/-])([Cc]lass(?:es)?)(?!\w)")
HEADING_RE = re.compile(r"^(#{1,6})(\s+)(.*?)\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
MASK_RES = [
    re.compile(r"`[^`]*`"),
    re.compile(r"<[^>\n]+>"),
    re.compile(r"\]\([^)]*\)"),
    re.compile(r"https?://[^\s)>\]]+"),
]
LINK_RE = re.compile(r"\[(?P<text>[^\]]*)\]\((?P<target>[^)\s]+)(?P<rest>[^)]*)\)")
ANCHOR_ID_RE = re.compile(r'(<a\s+id=")([^"]+)(")')

# Words that already qualify "class": "system class", "impact class", "risk class".
QUALIFIERS = {"system", "system's", "system’s", "systems'", "systems’", "impact", "risk"}
# "handling class" may name a data-handling tier, not the system class; a person decides.
REVIEW_PREV = {"handling"}
SENTENCE_START_RE = re.compile(r"(?:^|[.!?:;|>\"“(\[*_-])\s*$")


SMALL_WORDS = {
    "a", "an", "the", "and", "but", "or", "nor", "for", "so", "yet", "as", "at", "by",
    "in", "of", "off", "on", "per", "to", "up", "via", "from", "with", "into", "onto",
    "over", "upon", "than", "about", "above", "across", "after", "against", "along",
    "among", "around", "before", "behind", "below", "beneath", "beside", "between",
    "beyond", "down", "during", "inside", "like", "near", "past", "since", "through",
    "throughout", "toward", "under", "until", "within", "without",
}


def chicago_title(title: str) -> str:
    """Chicago-style headline case: major words capitalised, small words not.

    The first and last word, and the first word after a colon or dash, are always
    capitalised. Each part of a hyphenated word is treated as a word of its own
    (``Data-Handling``, ``Non-Exhaustive``). Only the first letter changes, so
    ``CS-3`` and ``Class A`` keep their shape.
    """
    parts = re.split(r"(\s+)", title)
    word_idx = [i for i, p in enumerate(parts) if p.strip()]
    out = list(parts)
    for n, i in enumerate(word_idx):
        word = parts[i]
        forced = n == 0 or n == len(word_idx) - 1 or (n > 0 and re.search(r"[:—–]$", parts[word_idx[n - 1]]))
        pieces = word.split("-")
        fixed = []
        for k, piece in enumerate(pieces):
            core = re.sub(r"^[^\w§]+", "", piece)
            bare = re.sub(r"[^\w']+", "", piece).lower()
            small = bare in SMALL_WORDS and not (forced and k == 0)
            if not core or core[0].isdigit() or core[0] == "§" or small or piece.startswith("\x00"):
                fixed.append(piece)
                continue
            lead = len(piece) - len(core)
            fixed.append(piece[:lead] + core[0].upper() + core[1:])
        out[i] = "-".join(fixed)
    return "".join(out)


def mask(line: str) -> tuple[str, list[str]]:
    saved: list[str] = []

    def stash(match: re.Match[str]) -> str:
        saved.append(match.group(0))
        return f"\x00{len(saved) - 1}\x00"

    for pattern in MASK_RES:
        line = pattern.sub(stash, line)
    return line, saved


def unmask(line: str, saved: list[str]) -> str:
    for _ in range(3):
        line = re.sub(r"\x00(\d+)\x00", lambda m: saved[int(m.group(1))], line)
    return line


def decide(masked: str, match: re.Match[str]) -> tuple[str, str]:
    """Return (action, reason): action is rewrite, skip, or review."""
    before, after = masked[: match.start()], masked[match.end() :]
    if re.match(r"\s+[A-Z](?![\w'])", after):
        return "skip", "named level"
    if re.match(r"\s+of\b", after):
        return "skip", "generic 'class of'"
    prev = re.search(r"([\w'’]+)\s+$", before)
    if prev and prev.group(1).lower() in QUALIFIERS:
        return "skip", "already qualified"
    if prev and prev.group(1).lower() in REVIEW_PREV:
        return "review", "may be a different class (handling)"
    if re.search(r"\w-\s*$", before):
        return "review", "hyphenated before"
    if after.startswith("-") and not re.match(r"-[Ss]cal", after):
        return "review", "hyphenated after"
    return "rewrite", ""


def replacement(masked: str, match: re.Match[str], in_heading: bool) -> str:
    word = match.group(1)
    after = masked[match.end() :]
    if re.match(r"-[Ss]cal", after):
        # "class-scaled" is one modifier; hyphenate it whole: "system-class-scaled".
        if word[0].islower():
            return "system-" + word
        return "System-" + (word if after.startswith("-S") else word.lower())
    if word[0].islower():
        return "system " + word
    if in_heading:
        return "System " + word
    if re.match(r"(?:-|\s+)[A-Z]", after) and not SENTENCE_START_RE.search(masked[: match.start()]):
        return "System " + word
    if re.match(r"-[A-Z]", after):
        return "System " + word
    return "System " + word.lower()


def rewrite_line(line: str, in_heading: bool = False) -> tuple[str, list[tuple[str, str]]]:
    """Return the rewritten line and its REVIEW items as (reason, context)."""
    masked, saved = mask(line)
    review: list[tuple[str, str]] = []
    out: list[str] = []
    cursor = 0
    for match in CLASS_RE.finditer(masked):
        action, reason = decide(masked, match)
        if action == "review":
            lo, hi = max(0, match.start() - 30), match.end() + 30
            review.append((reason, unmask(masked[lo:hi], saved)))
        if action != "rewrite":
            continue
        out.append(masked[cursor : match.start()])
        out.append(replacement(masked, match, in_heading))
        cursor = match.end()
    out.append(masked[cursor:])
    return unmask("".join(out), saved), review


def rewrite_text_fragment(text: str) -> str:
    """Rewrite a stretch of link text the way a heading would be rewritten."""
    return rewrite_line(text, in_heading=False)[0]


def process_lines(lines: list[str]):
    """Yield (index, old, new, review) for each line, skipping fenced blocks."""
    fenced = False
    for index, line in enumerate(lines):
        if FENCE_RE.match(line):
            fenced = not fenced
            yield index, line, line, []
            continue
        if fenced:
            yield index, line, line, []
            continue
        heading = HEADING_RE.match(line)
        if heading:
            new_title, review = rewrite_line(heading.group(3), in_heading=True)
            if new_title != heading.group(3):
                new_title = chicago_title(new_title)
            new = f"{heading.group(1)}{heading.group(2)}{new_title}"
            yield index, line, new, review
        else:
            new, review = rewrite_line(line)
            yield index, line, new, review


def heading_slugs(old: str, new: str) -> tuple[str, str] | None:
    old_h, new_h = HEADING_RE.match(old), HEADING_RE.match(new)
    if not (old_h and new_h) or old_h.group(3) == new_h.group(3):
        return None
    return github_slug(old_h.group(3)), github_slug(new_h.group(3))


def scope_files(root: pathlib.Path, patterns: list[str]) -> list[str]:
    found: set[str] = set()
    for pattern in patterns:
        found.update(p.relative_to(root).as_posix() for p in root.glob(pattern) if p.is_file())
    return sorted(found)


def retitle_link_text(text: str, pair: tuple[str, str] | None) -> str:
    """Give link text the new heading when it quotes the old one (``§5.1.5 Old Title``)."""
    if pair:
        old, new = pair
        prefix = re.match(r"^(§[\d.]+\s+)?", text).group(0)
        rest = text[len(prefix):]
        if rest in (old, rewrite_line(old)[0], rewrite_line(old, in_heading=True)[0]):
            return prefix + new
    return rewrite_text_fragment(text)


def retarget(
    root: pathlib.Path,
    rel: str,
    text: str,
    renames: dict[str, dict[str, str]],
    titles: dict[str, dict[str, tuple[str, str]]] | None = None,
) -> tuple[str, int]:
    """Point links at renamed fragments and rewrite their link text to match."""
    count = 0
    titles = titles or {}

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        target = match.group("target")
        dest = resolve_link_file(root, root / rel, target)
        mapping = renames.get(dest or "")
        if not mapping:
            return match.group(0)
        _path, sep, frag = target.partition("#")
        if not sep or frag not in mapping:
            return match.group(0)
        count += 1
        new_text = retitle_link_text(match.group("text"), titles.get(dest, {}).get(frag))
        new_target = target.replace("#" + frag, "#" + mapping[frag], 1)
        return f"[{new_text}]({new_target}{match.group('rest')})"

    return LINK_RE.sub(repl, text), count


def rename_anchor_ids(text: str, mapping: dict[str, str]) -> tuple[str, int]:
    count = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        new = mapping.get(match.group(2))
        if new is None:
            return match.group(0)
        count += 1
        return match.group(1) + new + match.group(3)

    return ANCHOR_ID_RE.sub(repl, text), count


def run_check(root: pathlib.Path, patterns: list[str], changed_only: bool) -> int:
    files = scope_files(root, patterns)
    changed = added_line_numbers(root, set(files)) if changed_only else None
    total = 0
    for rel in files:
        if changed is not None and rel not in changed:
            continue
        lines = (root / rel).read_text(encoding="utf-8").splitlines()
        for index, old, new, _review in process_lines(lines):
            if new == old:
                continue
            if changed is not None and (index + 1) not in changed.get(rel, set()):
                continue
            print(f"  {rel}:{index + 1}: TERM-SYSTEM-CLASS-01: bare 'class'; say 'system class' "
                  "(run tools/apply_system_class_term.py to fix)")
            total += 1
    mode = "changed-only" if changed_only else "full"
    if total:
        print(f"FAIL: TERM-SYSTEM-CLASS-01 ({mode}) — {total} line(s) use a bare 'class'.")
        return 1
    print(f"PASS: TERM-SYSTEM-CLASS-01 ({mode}) — system class is named in full.")
    return 0


def run_fix(root: pathlib.Path, patterns: list[str], dry_run: bool, show: int) -> int:
    files = scope_files(root, patterns)
    new_text: dict[str, str] = {}
    renames: dict[str, dict[str, str]] = {}
    titles: dict[str, dict[str, tuple[str, str]]] = {}
    changed_lines = 0
    review_items: list[tuple[str, int, str, str]] = []
    samples: list[tuple[str, int, str, str]] = []
    per_file: dict[str, int] = {}
    heading_changes: list[tuple[str, str, str]] = []
    for rel in files:
        raw = (root / rel).read_text(encoding="utf-8")
        lines = raw.split("\n")
        out = list(lines)
        for index, old, new, review in process_lines(lines):
            for reason, context in review:
                review_items.append((rel, index + 1, reason, context))
            if new == old:
                continue
            out[index] = new
            changed_lines += 1
            per_file[rel] = per_file.get(rel, 0) + 1
            if len(samples) < show:
                samples.append((rel, index + 1, old, new))
            slugs = heading_slugs(old, new)
            if slugs:
                renames.setdefault(rel, {})[slugs[0]] = slugs[1]
                titles.setdefault(rel, {})[slugs[0]] = (
                    HEADING_RE.match(old).group(3), HEADING_RE.match(new).group(3))
                heading_changes.append((rel, old, new))
        new_text[rel] = "\n".join(out)
    # Rename the anchor ids above renamed headings, then retarget links everywhere.
    anchors_renamed = 0
    for rel, mapping in renames.items():
        new_text[rel], count = rename_anchor_ids(new_text[rel], mapping)
        anchors_renamed += count
    links_retargeted = 0
    touched: set[str] = set(files)
    if renames:
        for path in live_text_files(root):
            if path.suffix != ".md":
                continue
            rel = path.relative_to(root).as_posix()
            text = new_text.get(rel)
            if text is None:
                text = path.read_text(encoding="utf-8")
            text2, count = retarget(root, rel, text, renames, titles)
            if count:
                new_text[rel] = text2
                links_retargeted += count
                touched.add(rel)
    written = 0
    for rel in sorted(touched):
        path = root / rel
        if new_text.get(rel) is not None and new_text[rel] != path.read_text(encoding="utf-8"):
            written += 1
            if not dry_run:
                path.write_text(new_text[rel], encoding="utf-8")
    verb = "would change" if dry_run else "changed"
    print(f"{verb}: {changed_lines} line(s) in {len(per_file)} scope file(s); "
          f"{len(heading_changes)} heading(s) renamed; {anchors_renamed} anchor id(s); "
          f"{links_retargeted} link(s) retargeted; {written} file(s) {'to write' if dry_run else 'written'}.")
    for rel, count in sorted(per_file.items()):
        print(f"  {rel}: {count}")
    for rel, old, new in heading_changes:
        print(f"  HEADING {rel}\n    - {old}\n    + {new}")
    for rel, number, old, new in samples:
        print(f"  SAMPLE {rel}:{number}\n    - {old}\n    + {new}")
    for rel, number, reason, context in review_items:
        print(f"  REVIEW {rel}:{number}: {reason}: …{context}…")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Workspace root. Defaults to current directory.")
    parser.add_argument("--files", action="append", default=None,
                        help=f"Glob under root (repeatable). Defaults to {DEFAULT_GLOB}.")
    parser.add_argument("--check", action="store_true", help="Audit: list bare 'class', write nothing, exit 1 if any.")
    parser.add_argument("--changed-only", action="store_true", help="With --check: only lines added versus HEAD.")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing files.")
    parser.add_argument("--show", type=int, default=0, help="With a fix run: print this many before/after samples.")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve()
    patterns = args.files or [DEFAULT_GLOB]
    if args.check:
        return run_check(root, patterns, args.changed_only)
    return run_fix(root, patterns, args.dry_run, args.show)


if __name__ == "__main__":
    sys.exit(main())
