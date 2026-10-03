#!/usr/bin/env python3
"""Require named, resolving references to corpus sections (CS-/CI-/CJS-/CF-).

Rule ID: CORPUS-REF-NAME-01

Every reference in body prose to a corpus file or section must carry its
name and must resolve:

* **Named.** ``[CS-10.3](…)`` alone fails. Accepted forms put the name in
  the link text (``[CS-10.3 Gate criteria and advancement rules](…)``) or in
  a following gloss (``**CS-10.3** (*Gate criteria and advancement rules*)``
  or ``[**CS-10.3**](…) (*Gate criteria and advancement rules*)``). The
  both endpoints of a range (``CI-14.1 (*…*) through CI-14.3 (*…*)``) need
  names. Unlinked references (``CI-9``) are held to the same naming rule.
* **Resolving.** The cited ID must exist as a corpus heading. A link must
  point at the file that owns the ID; a section-level ID (``CS-10.3``) must
  carry a fragment, and that fragment must be an anchor of that section's
  own heading. A gloss or link-text name must agree with the heading title
  (either contains the other, compared as lowercase words).

``<details>`` widgets, headings, tables, HTML-only lines, blockquotes,
backticks, and fenced code are out of scope. ``--changed-only`` checks
added Markdown lines versus HEAD so legacy references do not block until
those lines are edited. A list-entry label (``- **CI-14.3** — description``)
is exempt: the description after the dash is its name.
"""

from __future__ import annotations

import argparse
import html
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope  # noqa: E402
from local_markdown_fragment_audit import github_slug  # noqa: E402
from section_cite_name_audit import (  # noqa: E402
    CODE_SPAN_RE,
    is_exempt_line,
    mask_details_and_fences,
)

ROOT = Path(__file__).resolve().parents[1]
RULE = "CORPUS-REF-NAME-01"
FAMILY_DIRS = (
    "corpus_systems",
    "corpus_institutions",
    "corpus_joint_structure",
    "corpus_forum",
)

ID_PATTERN = r"(?:CS|CI|CJS|CF)-\d+[A-Za-z]?(?:\.\d+)*"
ID_RE = re.compile(rf"\b({ID_PATTERN})\b")
HEADING_RE = re.compile(
    rf"^#{{1,6}}\s+\**({ID_PATTERN})\**(?:,\s*Part\s+[A-Z])?(?:[:\s—–-]+)(.*?)\s*$"
)
PREFIX_RE = re.compile(
    r"^(?:Interface\s*[—–-]\s*)?"
    r"(?:Article\s+[IVXLC]+(?:-[A-Z])?\s*\([^)]*\)\s*(?:[—–-]\s*)?)?(.*)$"
)
HTML_ANCHOR_RE = re.compile(r"""<a\s+(?:id|name)=["']([^"']+)["']""", re.I)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
LABEL_ENTRY_RE = re.compile(r"^\s*(?:[-*]|\d+\.)\s+\**(?:%s)$" % ID_PATTERN)
GLOSS_RE = re.compile(r"^[\s*_]*\(\*([^*]+?)\*\)")


@dataclass(frozen=True)
class Finding:
    file: str
    line: int
    ref: str
    detail: str
    fix: tuple[int, str] | None = None  # (column, text) to insert for --fix


@dataclass
class Section:
    files: set[str]
    title: str
    anchors: set[str]

    @property
    def short_name(self) -> str:
        rest = PREFIX_RE.match(self.title).group(1).strip()
        rest = re.sub(r"^\((.*)\)$", r"\1", rest).strip()
        return rest or self.title


def words(value: str) -> str:
    value = html.unescape(value).lower()
    value = re.sub(r"\([^)]*\bArticle\b[^)]*\)", " ", value, flags=re.I)
    return " ".join(re.findall(r"[a-z0-9]+", value))


def clean(value: str) -> str:
    return re.sub(r"[*_`]", "", value).strip()


def build_index(root: Path) -> dict[str, Section]:
    """Map every corpus section ID to its file(s), title, and heading anchors."""
    index: dict[str, Section] = {}
    for family in FAMILY_DIRS:
        for path in sorted((root / family).glob("*.md")):
            rel = path.relative_to(root).as_posix()
            pending: set[str] = set()
            current: Section | None = None
            gap = 99
            for line in path.read_text(encoding="utf-8").splitlines():
                gap += 1
                anchor_ids = HTML_ANCHOR_RE.findall(line)
                if anchor_ids and not line.lstrip().startswith("#"):
                    pending.update(anchor_ids)
                    if current is not None and gap <= 2:
                        current.anchors.update(anchor_ids)
                    continue
                match = HEADING_RE.match(line)
                if match:
                    ident = match.group(1).upper()
                    anchors = set(pending) | {github_slug(line.lstrip("# ").strip())}
                    section = index.get(ident)
                    if section is None:
                        section = Section({rel}, clean(match.group(2)), anchors)
                        index[ident] = section
                    else:
                        section.files.add(rel)
                        section.anchors.update(anchors)
                    current, gap = section, 0
                    pending = set()
                elif line.strip():
                    pending = set()
    return index


def title_agrees(name: str, title: str) -> bool:
    a = words(name)
    if not a:
        return False
    for candidate in (title, PREFIX_RE.match(title).group(1)):
        b = words(candidate)
        if b and (a in b or b in a):
            return True
    return False


def normalize_id(ident: str) -> str:
    return ident.upper()


def gloss_after(text: str) -> str | None:
    match = GLOSS_RE.match(text)
    return match.group(1) if match else None


def name_from_link_text(label: str, ident: str) -> str | None:
    """Return the name embedded after the ID in link text, if any."""
    visible = clean(label)
    pos = visible.upper().find(ident)
    if pos < 0:
        return None
    rest = visible[pos + len(ident) :].lstrip(" :—–-")
    return rest or None


def check_reference(
    root: Path,
    rel_path: str,
    line_no: int,
    ident: str,
    href: str | None,
    name: str | None,
    index: dict[str, Section],
    end: int,
) -> list[Finding]:
    found: list[Finding] = []
    ident = normalize_id(ident)
    section = index.get(ident)
    if section is None:
        return [Finding(rel_path, line_no, ident, "no corpus heading defines this ID")]
    if name is None:
        found.append(
            Finding(
                rel_path,
                line_no,
                ident,
                f"corpus reference has no name; add (*{section.short_name}*) or put the name in the link text",
                (end, f" (*{section.short_name}*)"),
            )
        )
    elif name is not None and not title_agrees(name, section.title):
        found.append(
            Finding(
                rel_path,
                line_no,
                ident,
                f"name {name!r} does not match heading title {section.title!r}",
            )
        )
    if href is None:
        return found
    target, _, fragment = href.partition("#")
    if target:
        resolved = (root / rel_path).parent.joinpath(target).resolve()
        try:
            resolved_rel = resolved.relative_to(root).as_posix()
        except ValueError:
            resolved_rel = target
        if not resolved.is_file():
            found.append(Finding(rel_path, line_no, ident, f"link target {target} does not exist"))
        elif resolved_rel not in section.files:
            found.append(
                Finding(
                    rel_path,
                    line_no,
                    ident,
                    f"link points at {resolved_rel} but {ident} is defined in {', '.join(sorted(section.files))}",
                )
            )
    if "." in ident and not fragment:
        found.append(
            Finding(rel_path, line_no, ident, "section-level reference links the file without its section anchor")
        )
    elif fragment and fragment not in section.anchors:
        found.append(
            Finding(
                rel_path,
                line_no,
                ident,
                f"fragment #{fragment} is not an anchor of the {ident} heading",
            )
        )
    return found


def scan_line(
    root: Path, rel_path: str, line_no: int, line: str, index: dict[str, Section]
) -> list[Finding]:
    if is_exempt_line(line):
        return []
    line = CODE_SPAN_RE.sub(lambda m: " " * len(m.group(0)), line)
    findings: list[Finding] = []
    covered: list[tuple[int, int]] = []
    for link in LINK_RE.finditer(line):
        ids = [m for m in ID_RE.finditer(link.group(1))]
        if not ids:
            continue
        covered.append((link.start(), link.end()))
        for position, id_match in enumerate(ids):
            ident = id_match.group(1)
            name = name_from_link_text(link.group(1), normalize_id(ident)) if position == 0 else None
            if name is None and position == 0:
                name = gloss_after(line[link.end() :])
            elif position == 0 and gloss_after(line[link.end() :]) is not None:
                name = name  # name embedded in the link text wins
            findings.extend(
                check_reference(
                    root, rel_path, line_no, ident,
                    link.group(2) if position == 0 else None,
                    name, index, link.end(),
                )
            )
    for id_match in ID_RE.finditer(line):
        if LABEL_ENTRY_RE.match(line[: id_match.end()]) and re.match(
            r"[*_]*\s+[—–-]\s", line[id_match.end() :]
        ):
            continue
        if any(start <= id_match.start() < end for start, end in covered):
            continue
        ident = id_match.group(1)
        before = line[: id_match.start()]
        after = line[id_match.end() :]
        # Skip IDs that sit inside a gloss or a quoted label.
        if re.search(r"\(\*[^*)]*$", before):
            continue
        name = gloss_after(re.sub(r"^[*_]+", "", after))
        findings.extend(
            check_reference(
                root, rel_path, line_no, ident, None, name, index,
                id_match.end() + len(re.match(r"[*_]*", after).group(0)),
            )
        )
    return findings


def scan_text(
    root: Path, rel_path: str, text: str, index: dict[str, Section]
) -> list[Finding]:
    findings: list[Finding] = []
    for line_no, line in enumerate(mask_details_and_fences(text).splitlines(), start=1):
        findings.extend(scan_line(root, rel_path, line_no, line, index))
    return findings


def added_line_numbers(root: Path, scope: set[str]) -> dict[str, set[int]]:
    result = subprocess.run(
        ["git", "diff", "--unified=0", "--diff-filter=ACM", "HEAD", "--", *sorted(scope)],
        cwd=root, check=True, capture_output=True, text=True,
    )
    added: dict[str, set[int]] = {}
    rel_path: str | None = None
    for line in result.stdout.splitlines():
        if line.startswith("+++ b/"):
            rel_path = line.removeprefix("+++ b/")
        elif line.startswith("@@") and rel_path:
            match = re.search(r"\+(\d+)(?:,(\d+))?", line)
            if match:
                start = int(match.group(1))
                count = int(match.group(2)) if match.group(2) is not None else 1
                added.setdefault(rel_path, set()).update(range(start, start + count))
    return added


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--changed-only", action="store_true")
    parser.add_argument("--paths", nargs="*")
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Insert the suggested (*name*) gloss after unnamed references.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    index = build_index(root)
    scope = list(binding_corpus_scope(root, include_support_docs=False))
    changed: dict[str, set[int]] | None = None
    if args.paths:
        scope = [p for p in args.paths if p in set(scope)]
    elif args.changed_only:
        changed = added_line_numbers(root, set(scope))
        scope = [p for p in scope if p in changed]
    findings: list[Finding] = []
    for rel_path in scope:
        path = root / rel_path
        if not path.is_file():
            continue
        for finding in scan_text(root, rel_path, path.read_text(encoding="utf-8"), index):
            if changed is None or finding.line in changed.get(rel_path, set()):
                findings.append(finding)
    if args.fix:
        by_file: dict[str, dict[int, list[tuple[int, str]]]] = {}
        for f in findings:
            if f.fix:
                by_file.setdefault(f.file, {}).setdefault(f.line, []).append(f.fix)
        for rel_path, lines_map in by_file.items():
            path = root / rel_path
            lines = path.read_text(encoding="utf-8").split("\n")
            for line_no, inserts in lines_map.items():
                text = lines[line_no - 1]
                for col, glossed in sorted(set(inserts), reverse=True):
                    text = text[:col] + glossed + text[col:]
                lines[line_no - 1] = text
            path.write_text("\n".join(lines), encoding="utf-8")
        print(f"FIXED: inserted names in {len(by_file)} file(s); re-run to verify.")
        return 0
    if not findings:
        mode = "changed-only" if args.changed_only else "full"
        print(f"PASS: {RULE} ({mode}) — corpus references are named and resolve.")
        return 0
    print(f"FAIL: {RULE} — {len(findings)} corpus reference problem(s).")
    for f in findings:
        print(f"  {f.file}:{f.line}: {RULE}: {f.ref}: {f.detail}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
