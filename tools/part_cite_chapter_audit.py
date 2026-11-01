#!/usr/bin/env python3
"""Require the chapter on a ``Part X §N`` citation that points outside its own chapter.

Rule ID: PART-CITE-CHAPTER-01

Chapters One, Six, Nine and Thirteen are split into lettered Parts, and the
letters repeat from chapter to chapter. ``Part B §7.2`` names no section until
the reader knows the chapter. Inside Chapter Nine that is fine, because the
reader is already there. Anywhere else (Chapter Ten, another chapter, an
adopted-implementation file, a front door) the citation must carry the chapter:

    [Chapter Nine Part B §7.2 Certification Defects and Correction](core_09.005_…#72-…)

The adopted-implementation families keep their own Parts (``CS-6.305`` is Part A and
``CS-6.310`` is Part B of CS chapter 6). Their qualifier is the document ID:
``CS-6.310 Part B §9.3 Type O``.

What it checks, for every ``Part A``–``Part F`` followed by ``§N``:

* **Linked citation.** The link target names the owning file, and that file gives
  the chapter and the Part letter (``tools/architecture/chapter_numbers.json`` plus the
  file's ``# CHAPTER …, PART X`` / ``# CS-6.305, Part A`` heading or ``_part_x`` file
  name). If the target is in another chapter than the citing file, the text must carry
  the qualifier (``missing-chapter``). A qualifier that names another chapter than the
  target is ``wrong-chapter``. A Part letter that disagrees with the target file is
  ``part-mismatch``.
* **Unlinked citation** (a later mention of the same section). The heading index of
  the Part files resolves ``Part B §7.2`` plus its title to one chapter, and the same
  rules apply. A mention is fixed when its title confirms the chapter, or when the citing
  file has no such Part itself and only one chapter has that Part and section. One that no
  Part heading explains, or that two chapters explain equally well, is ``unresolved``.

Accepted qualifiers, directly before ``Part``: ``Chapter Nine`` (or ``Chapter 9``),
``Ch9``, and a family document ID such as ``CS-6.310``, with an optional comma, ``'s``,
``**`` or ``[`` between: ``Chapter Nine Part B``, ``Chapter One, Part A``,
``Chapter Nine's Part B``, ``Chapter Nine [Part B §7](…)``, ``**Chapter Nine** Part B``,
``CS-6.305 Part A``.

``--write`` inserts the qualifier in front of each ``missing-chapter`` citation, inside
the link text (the corpus house style). It never touches ``wrong-chapter``,
``part-mismatch`` or ``unresolved`` findings, because those need a decision. ``--all`` is
a read-only inventory of what is not scanned by default (project drafts, translations,
archive, evidence, generated pages); it cannot be combined with ``--write``.

A later citation in a run inherits the chapter of the one before it when only a connector
separates them (``Chapter Nine Part A §3 and Part B §5``, ``Chapter One Part A §2, Part B §4``).
Each *linked* citation stands alone and carries its own qualifier.

Out of scope by design: fenced code, inline code, headings, ``doc_architecture.md`` (its
dated move log keeps the wording each move used), dated records under ``implementation/``
(``…_2026-06-24.md``), and dated change-log table rows (``| 2026-10-12 | v0.30 | …``), which
keep the numbering of their day.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RULE = "PART-CITE-CHAPTER-01"

CHAPTER_WORDS = (
    "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
    "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
    "Sixteen", "Seventeen", "Eighteen", "Nineteen",
)
WORD_TO_NUM = {word.lower(): number for number, word in enumerate(CHAPTER_WORDS)}

# Scanned only by --all (read-only): working drafts, history, other languages, generated output.
INVENTORY_ONLY_PREFIXES = (
    "project/",
    "translations/",
    "archive/",
    "evidence/",
    "_pages_site/",
    "doc_architecture/generated/",
    "ai_corpus/indexes/",
    "ai_corpus/visualization/",
    "evaluation/results/",
)
ALWAYS_SKIP_PARTS = {".git", "_to_delete", "node_modules", "__pycache__", ".vscode"}
BLANKET_EXEMPT = {"doc_architecture.md"}
TEXT_SUFFIXES = {".md", ".mdc", ".txt"}
DATED_RECORD_RE = re.compile(r"_\d{4}-\d{2}-\d{2}(?:[_.]|$)")

FENCE_RE = re.compile(r"^\s*(```|~~~)")
CODE_SPAN_RE = re.compile(r"`[^`\n]*`")
HEADING_RE = re.compile(r"^#{1,6}\s+(?P<num>\d+(?:\.\d+)*)\.?\s+(?P<title>.+?)\s*#*\s*$")
FAMILY_HEADING_RE = re.compile(
    r"^#{1,6}\s+(?P<fam>CS|CI|CJS|CF)-(?P<maj>\d+)\.(?P<min>\d+)\s+§\s*(?P<num>\d+(?:\.\d+)*)\.?\s+"
    r"(?P<title>.+?)\s*#*\s*$"
)
H1_PART_RE = re.compile(
    r"^#\s+(?:CHAPTER\s+\S+?|(?:CS|CI|CJS|CF)-\d+\.\d+),?\s+PART\s+([A-Z])\b", re.I | re.M
)
FILE_PART_RE = re.compile(r"_part_([a-z])\.md$")
DISPLAY_ID_RE = re.compile(r"^(?:(?P<fam>[A-Z]+)-)?(?P<maj>\d+)\.(?P<min>\d+)$")
REF_RE = re.compile(
    r"(?<![A-Za-z])Part\s+(?P<letter>[A-F])\b,?\s*(?P<mark>§§?)\s*(?P<sec>\d+(?:\.\d+)*)"
)
LINK_RE = re.compile(
    r"\[(?P<text>(?:[^\[\]]|\[[^\]]*\])*)\]\((?P<target>[^)\s]+)(?:\s+\"[^\"]*\")?\)"
)
QUALIFIER_BEFORE_RE = re.compile(
    r"(?:Chapter\s+(?P<name>[A-Za-z]+|\d+)"
    r"|(?<![A-Za-z])Ch\.?\s*(?P<abbr>\d+)"
    r"|(?<![A-Za-z])(?P<fam>CS|CI|CJS|CF)-(?P<maj>\d+)\.(?P<min>\d+))"
    r"(?:\*\*|\*|_)?(?:['’]s)?,?\s*(?:\[\*\*|\*\*|\[|\*|_)?$",
    re.I,
)
WORD_RE = re.compile(r"[a-z0-9]+")
DATED_ROW_RE = re.compile(r"^\s*\|\s*\d{4}-\d{2}-\d{2}\s*\|")
CONNECTOR_RE = re.compile(r"(?:,|\band\b|\bor\b|\bthrough\b|\bto\b|\bplus\b|&|/|[–—-])\s*(?:the\s+)?$", re.I)
MAX_CONNECTOR_GAP = 60

Key = tuple[str, int]  # (layer, chapter): ("CORE", 9) is Chapter Nine; ("CS", 6) is CS chapter 6


@dataclass(frozen=True)
class FileInfo:
    layer: str
    chapter: int
    letter: str | None  # None: this file is not a lettered Part
    rel: str
    doc_id: str | None  # "CS-6.305" for a family file, None for core

    @property
    def key(self) -> Key:
        return (self.layer, self.chapter)

    @property
    def qualifier(self) -> str:
        return self.doc_id if self.doc_id else f"Chapter {CHAPTER_WORDS[self.chapter]}"


@dataclass(frozen=True)
class Section:
    sec: str
    title: str
    file: FileInfo


@dataclass
class Context:
    files: dict[str, FileInfo] = field(default_factory=dict)  # basename -> info
    sections: dict[tuple[str, str], list[Section]] = field(default_factory=dict)
    lettered: set[tuple[Key, str]] = field(default_factory=set)  # (chapter key, letter) pairs that exist


@dataclass(frozen=True)
class Finding:
    rel: str
    line: int
    col: int  # 1-based
    kind: str
    ref: str
    message: str
    fix_col: int | None = None  # 0-based insertion column when auto-fixable
    fix_text: str = ""

    def render(self) -> str:
        return f"{self.rel}:{self.line}:{self.col}: [{RULE}:{self.kind}] {self.ref}: {self.message}"


def describe(key: Key) -> str:
    layer, chapter = key
    return f"Chapter {CHAPTER_WORDS[chapter]}" if layer == "CORE" else f"{layer}-{chapter}"


def part_letter(path: Path, rel: str) -> str | None:
    if path.is_file():
        match = H1_PART_RE.search(path.read_text(encoding="utf-8"))
        if match:
            return match.group(1).upper()
    match = FILE_PART_RE.search(rel)
    return match.group(1).upper() if match else None


def build_context(root: Path) -> Context:
    ctx = Context()
    data = json.loads(
        (root / "tools" / "architecture" / "chapter_numbers.json").read_text(encoding="utf-8")
    )
    for entry in data["chapters"]:
        display = DISPLAY_ID_RE.match(str(entry["display_id"]))
        if not display:
            continue
        layer = entry.get("layer", "CORE")
        dest = entry["destination_file"]
        info = FileInfo(
            layer,
            int(display.group("maj")),
            part_letter(root / dest, dest),
            dest,
            None if layer == "CORE" else str(entry["display_id"]),
        )
        ctx.files[Path(dest).name] = info
        original = entry.get("original_file")
        if original:
            ctx.files.setdefault(Path(original).name, info)
    for info in {i.rel: i for i in ctx.files.values()}.values():
        if info.letter is None:
            continue
        ctx.lettered.add((info.key, info.letter))
        path = root / info.rel
        if not path.is_file():
            continue
        in_fence = False
        for line in path.read_text(encoding="utf-8").splitlines():
            if FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            family = FAMILY_HEADING_RE.match(line)
            plain = HEADING_RE.match(line)
            match = family or plain
            if match:
                ctx.sections.setdefault((info.letter, match.group("num")), []).append(
                    Section(match.group("num"), match.group("title"), info)
                )
    return ctx


def title_matches(cited_after: str, heading_title: str) -> bool:
    """The lead words of the cited title agree with the heading title (or the reverse)."""
    cited = WORD_RE.findall(cited_after.lower())[:12]
    heading = WORD_RE.findall(heading_title.lower())
    if not cited or not heading:
        return False
    agree = 0
    for left, right in zip(cited, heading):
        if left != right:
            break
        agree += 1
    return agree >= min(len(heading), 2)


def qualifier_key(before: str) -> Key | None:
    match = QUALIFIER_BEFORE_RE.search(before)
    if not match:
        return None
    if match.group("name"):
        name = match.group("name")
        number = int(name) if name.isdigit() else WORD_TO_NUM.get(name.lower())
        return ("CORE", number) if number is not None and number < len(CHAPTER_WORDS) else None
    if match.group("abbr"):
        number = int(match.group("abbr"))
        return ("CORE", number) if number < len(CHAPTER_WORDS) else None
    return (match.group("fam").upper(), int(match.group("maj")))


def mask_code(line: str) -> str:
    return CODE_SPAN_RE.sub(lambda m: " " * len(m.group(0)), line)


def known_target(link: re.Match[str] | None, own: FileInfo | None, ctx: Context) -> FileInfo | None:
    """The file a link points at, when it is a mapped corpus file. A same-file fragment is the citing file."""
    if link is None:
        return None
    target = link.group("target")
    if target.startswith(("http://", "https://", "mailto:")):
        return None
    path = target.split("#", 1)[0]
    if not path:
        return own
    return ctx.files.get(Path(path).name)


def check_text(rel: str, text: str, ctx: Context) -> list[Finding]:
    own = ctx.files.get(Path(rel).name)
    findings: list[Finding] = []
    in_fence = False
    for number, raw in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence or raw.lstrip().startswith("#"):
            continue
        if DATED_ROW_RE.match(raw):
            continue
        line = mask_code(raw)
        links = list(LINK_RE.finditer(line))
        bound: set[int] = set()
        prev_end = -1
        prev_key: Key | None = None
        for match in REF_RE.finditer(line):
            link = next(
                (
                    lk
                    for lk in links
                    if lk.start("text") <= match.start() < lk.end("text") and id(lk) not in bound
                ),
                None,
            )
            if link is not None:
                bound.add(id(link))
            gap = line[prev_end:match.start()] if prev_end >= 0 else ""
            carry = (
                prev_key
                if prev_key is not None
                and link is None
                and len(gap) <= MAX_CONNECTOR_GAP
                and not re.search(r"[.;|]", gap)
                and CONNECTOR_RE.search(gap)
                else None
            )
            finding, key = judge(
                rel, number, match.start(), match.group("letter"), match.group("sec"),
                line[match.end():], qualifier_key(line[: match.start()]),
                known_target(link, own, ctx), own, ctx, carry,
            )
            if finding:
                findings.append(finding)
            prev_key = key
            prev_end = link.end() if link is not None else match.end()
    return findings


def judge(
    rel: str,
    line: int,
    start: int,
    letter: str,
    sec: str,
    after: str,
    qualifier: Key | None,
    target: FileInfo | None,
    own: FileInfo | None,
    ctx: Context,
    carry: Key | None,
) -> tuple[Finding | None, Key | None]:
    """Judge one citation. Returns the finding (if any) and the chapter the citation resolves to."""
    ref = f"Part {letter} §{sec}"
    col = start + 1
    own_key = own.key if own else None

    def missing(info: FileInfo, how: str) -> tuple[Finding, Key]:
        return (
            Finding(
                rel, line, col, "missing-chapter", ref,
                f"cites a section in {info.qualifier} without naming it ({how}); write '{info.qualifier} {ref}'"
                + (" and add the section title (CORPUS-REF-NAME-01)" if info.doc_id else ""),
                fix_col=start, fix_text=f"{info.qualifier} ",
            ),
            info.key,
        )

    def other(kind: str, message: str, key: Key | None) -> tuple[Finding, Key | None]:
        return Finding(rel, line, col, kind, ref, message), key

    if target is not None:  # linked to a mapped corpus file
        if target.letter != letter:
            have = f"Part {target.letter}" if target.letter else "not a lettered Part"
            return other(
                "part-mismatch",
                f"link target {target.rel} ({describe(target.key)}) is {have}, not Part {letter}",
                target.key,
            )
        if qualifier is not None and qualifier != target.key:
            return other(
                "wrong-chapter",
                f"says {describe(qualifier)} but link target {target.rel} is in {describe(target.key)}",
                target.key,
            )
        if qualifier is None and own_key != target.key:
            return missing(target, f"link target {target.rel}")
        return None, target.key

    if carry is not None and qualifier is None:  # a connector run: "Chapter Nine Part A §3 and Part B §5"
        return None, carry
    candidates = ctx.sections.get((letter, sec), [])
    if own_key is not None and any(c.file.key == own_key for c in candidates):
        if qualifier is None or qualifier == own_key:
            return None, own_key
    if qualifier is not None:
        if not candidates or any(c.file.key == qualifier for c in candidates):
            return None, qualifier
        where = ", ".join(sorted({describe(c.file.key) for c in candidates}))
        return other("wrong-chapter", f"says {describe(qualifier)} but no {ref} exists there ({where} has it)", qualifier)
    confirmed = [c for c in candidates if title_matches(after, c.title)]
    keys = {c.file.key for c in confirmed}
    if len(keys) == 1:
        return missing(confirmed[0].file, "found by section number and title")
    if len(keys) > 1:
        return other(
            "unresolved",
            "its title fits " + ", ".join(sorted(describe(k) for k in keys)) + "; name the chapter",
            None,
        )
    own_has_part = own_key is not None and (own_key, letter) in ctx.lettered
    if not own_has_part and len({c.file.key for c in candidates}) == 1:
        return missing(candidates[0].file, "the only chapter with this Part and section")
    if own_has_part:
        return None, own_key  # a Part of the citing chapter itself; nothing says otherwise
    return other("unresolved", "no Part heading with this number and title identifies the chapter; name it", None)


def default_scope(root: Path) -> list[str]:
    names = list(binding_corpus_scope(root, include_support_docs=True))
    extras: list[Path] = sorted(root.glob("*.md"))
    for pattern in (
        "docs/**/*.md", "guides/**/*.md", "implementation/**/*.md", "evaluation/**/*.md",
        "ai_corpus/*.md", "tools/*.md", ".cursor/rules/*.mdc",
    ):
        extras += sorted(root.glob(pattern))
    extras.append(root / "llms.txt")
    names += [p.relative_to(root).as_posix() for p in extras if p.is_file()]
    seen: set[str] = set()
    out: list[str] = []
    for rel in names:
        if rel in seen or rel in BLANKET_EXEMPT or rel.startswith(INVENTORY_ONLY_PREFIXES):
            continue
        if rel.startswith("implementation/") and DATED_RECORD_RE.search(Path(rel).name):
            continue
        seen.add(rel)
        if (root / rel).is_file():
            out.append(rel)
    return out


def inventory_scope(root: Path) -> list[str]:
    base = set(default_scope(root))
    out: list[str] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue
        rel = path.relative_to(root)
        if ALWAYS_SKIP_PARTS & set(rel.parts):
            continue
        name = rel.as_posix()
        if name not in BLANKET_EXEMPT and name not in base:
            out.append(name)
    return out


def scan(root: Path, rels: list[str], ctx: Context) -> list[Finding]:
    findings: list[Finding] = []
    for rel in rels:
        try:
            text = (root / rel).read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        findings.extend(check_text(rel, text, ctx))
    return findings


def apply_fixes(root: Path, findings: list[Finding]) -> int:
    by_file: dict[str, list[Finding]] = {}
    for item in findings:
        if item.fix_col is not None:
            by_file.setdefault(item.rel, []).append(item)
    fixed = 0
    for rel, items in by_file.items():
        path = root / rel
        with path.open(encoding="utf-8", newline="") as handle:
            lines = handle.read().split("\n")
        for item in sorted(items, key=lambda f: (f.line, f.fix_col or 0), reverse=True):
            row = lines[item.line - 1]
            lines[item.line - 1] = row[: item.fix_col] + item.fix_text + row[item.fix_col:]
            fixed += 1
        with path.open("w", encoding="utf-8", newline="") as handle:
            handle.write("\n".join(lines))
    return fixed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", default=str(ROOT), help="Repository root.")
    parser.add_argument("--write", action="store_true",
                        help="Insert the chapter qualifier into each missing-chapter citation.")
    parser.add_argument("--all", action="store_true",
                        help="Read-only inventory of files not scanned by default.")
    parser.add_argument("--summary", action="store_true", help="Print per-kind and per-file counts only.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    if args.all and args.write:
        print("--all is a read-only inventory; it cannot be combined with --write.", file=sys.stderr)
        return 2
    ctx = build_context(root)
    rels = inventory_scope(root) if args.all else default_scope(root)
    findings = scan(root, rels, ctx)
    if args.write:
        fixed = apply_fixes(root, findings)
        findings = scan(root, rels, ctx)
        print(f"{RULE}: inserted the chapter into {fixed} citation(s).")
    if args.summary:
        for kind, count in sorted(Counter(f.kind for f in findings).items()):
            print(f"{kind}: {count}")
        for rel, count in Counter(f.rel for f in findings).most_common():
            print(f"{count:6d}  {rel}")
    else:
        for item in findings:
            print(item.render())
    if findings:
        fixable = sum(1 for f in findings if f.fix_col is not None)
        print(
            f"{RULE}: {len(findings)} finding(s) in {len({f.rel for f in findings})} file(s)"
            f" ({fixable} fixable with --write; the rest need a decision).",
            file=sys.stderr,
        )
        return 1
    print(f"{RULE}: ok ({len(rels)} files).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
