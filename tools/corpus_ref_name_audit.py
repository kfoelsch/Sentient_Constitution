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

Headings, tables, HTML-only lines, blockquotes, backticks, and fenced code
are out of scope; ``<details>`` widget bodies (Trace, Definitions · Assessment
· Compliance) are in scope. ``--changed-only`` checks
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
from dataclasses import dataclass, field
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import binding_corpus_scope  # noqa: E402
from local_markdown_fragment_audit import github_slug  # noqa: E402
from section_cite_name_audit import (  # noqa: E402
    CODE_SPAN_RE,
    FENCE_RE,
    is_exempt_line,
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
DASH_NAME_RE = re.compile(r"^[*_]*\s+[—–-]\s+([^*_\[\]]+?)\s*(?:[*_]{2}|[.;,:)]|$)")
SUBSECTION_NAME_RE = re.compile(r"^(?:Part\s+[A-Z]\s+)?§\s*\d+(?:\.\d+)*\s*(.*)$")


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
    # Other accepted names: titles of the other parts of a multi-file ID
    # (CS-3 Part A / Part B) and the canonical name the registry gives it.
    aliases: set[str] = field(default_factory=set)

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
                    # An anchor inside a section body (for example the
                    # ``<a id="10-inspectable-attributable-action">`` that
                    # opens a named subsection) is a valid fragment of that
                    # section, however far below its heading it sits.
                    if current is not None:
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
                        section.aliases.add(clean(match.group(2)))
                    current, gap = section, 0
                    pending = set()
                elif line.strip():
                    pending = set()
    add_registry_names(root, index)
    return index


REGISTRY_NAME_RE = re.compile(rf"\*\*({ID_PATTERN})\s+[—–-]\s+([^*]+?)\*\*")


def add_registry_names(root: Path, index: dict[str, Section]) -> None:
    """Accept the canonical ``**CS-3 — System classification and handling**``
    names the family registries use, alongside the heading titles."""
    for family in FAMILY_DIRS:
        for path in sorted((root / family).glob("*_00_*registry*.md")):
            for match in REGISTRY_NAME_RE.finditer(path.read_text(encoding="utf-8")):
                section = index.get(match.group(1).upper())
                if section is not None:
                    section.aliases.add(clean(match.group(2)))


def section_title_agrees(name: str, section: Section) -> bool:
    """Name matches the heading title, another part's title, a registry name,
    or an anchor id of the section (anchors preserve earlier or router names,
    for example ``cjs-01-topic-router-stable-ids``)."""
    candidates = [section.title, *sorted(section.aliases), *sorted(section.anchors)]
    return any(title_agrees(name, t) for t in candidates)


_FILE_ANCHORS: dict[Path, set[str]] = {}


def file_anchors(path: Path) -> set[str]:
    """Every heading slug and ``<a id>`` in a file (for subsection fragments)."""
    if path not in _FILE_ANCHORS:
        anchors: set[str] = set()
        for line in path.read_text(encoding="utf-8").splitlines():
            anchors.update(HTML_ANCHOR_RE.findall(line))
            if line.startswith("#"):
                anchors.add(github_slug(line.lstrip("# ").strip()))
        _FILE_ANCHORS[path] = anchors
    return _FILE_ANCHORS[path]


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


def subsection_fragments(root: Path, rel_path: str, target: str, section: Section) -> set[str]:
    """Anchors of the file(s) that own the section, for a named-subsection link."""
    owners = [(root / rel_path).parent.joinpath(target)] if target else [root / f for f in section.files]
    found: set[str] = set()
    for owner in owners:
        if owner.is_file():
            found |= file_anchors(owner.resolve())
    return found


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
        if name is not None and name.lower().startswith("reserved"):
            return []  # ``CI-2`` (*reserved family ID*): an intentionally unused ID
        return [Finding(rel_path, line_no, ident, "no corpus heading defines this ID")]
    fragment = href.partition("#")[2] if href else ""
    subsection = SUBSECTION_NAME_RE.match(name) if name else None
    if subsection is not None:
        # ``CS-4 §10 inspectable attributable action``: the name after the
        # ``§N`` token names a subsection inside the ID's section, so it is
        # checked against the heading title or the linked anchor, not the
        # section title alone.
        subname = subsection.group(1).strip(" :—–-")
        if not subname:
            found.append(
                Finding(
                    rel_path,
                    line_no,
                    ident,
                    f"subsection reference {name!r} has no name; add the subsection title after the §",
                )
            )
        elif not (section_title_agrees(subname, section) or title_agrees(subname, fragment)):
            found.append(
                Finding(
                    rel_path,
                    line_no,
                    ident,
                    f"subsection name {subname!r} matches neither heading title {section.title!r} nor the linked anchor",
                )
            )
    elif name is None:
        found.append(
            Finding(
                rel_path,
                line_no,
                ident,
                f"corpus reference has no name; add (*{section.short_name}*) or put the name in the link text",
                (end, f" (*{section.short_name}*)"),
            )
        )
    elif not (
        section_title_agrees(name, section)
        or (fragment and title_agrees(name, fragment))
    ):
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
    valid_anchors = set(section.anchors)
    if subsection is not None:
        # ``CS-4 §10`` points inside CS-4 at a subsection that lives under a
        # numbered descendant (CS-4.10), so descendant anchors are valid too.
        prefix = f"{ident}."
        for key, child in index.items():
            if key.startswith(prefix):
                valid_anchors |= child.anchors
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
    elif fragment and fragment not in valid_anchors and not (
        name is not None
        and title_agrees(name, fragment)
        and fragment in subsection_fragments(root, rel_path, target, section)
    ):
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
            elif position == 0 and name is not None:
                sub = SUBSECTION_NAME_RE.match(name)
                trailing = gloss_after(line[link.end() :])
                if sub is not None and not sub.group(1).strip() and trailing:
                    # ``[CS-2 §5.2](…) (*Reclassification…*)``: the gloss names
                    # the subsection when the link text is only the number.
                    name = f"{name} {trailing}"
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
        # ``CJS-3.*n*`` is a placeholder pattern, not a cite of CJS-3.
        if re.match(r"[*_]*\.\*", after):
            continue
        # Skip IDs that sit inside a gloss or a quoted label.
        if re.search(r"\(\*[^*)]*$", before):
            continue
        name = gloss_after(re.sub(r"^[*_]+", "", after))
        if name is None and not re.match(r"[*_]*\s+[—–-]\s+§", after):
            # ``**CS-4 — Critical system stewardship**``: a dash name counts.
            dash = DASH_NAME_RE.match(after)
            if dash is not None:
                name = dash.group(1)
        findings.extend(
            check_reference(
                root, rel_path, line_no, ident, None, name, index,
                id_match.end() + len(re.match(r"[*_]*", after).group(0)),
            )
        )
    return findings


def mask_fences(text: str) -> str:
    """Blank fenced code; keep ``<details>`` widget bodies in scope.

    Trace and D/A/C widgets are where most cross-family routing lives, so a
    reference there needs a name like any other. The ``<details>``,
    ``<summary>`` and ``</details>`` tag lines are skipped by ``is_exempt_line``.
    """
    out: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            out.append("")
        else:
            out.append("" if in_fence else line)
    return "\n".join(out)


def scan_text(
    root: Path, rel_path: str, text: str, index: dict[str, Section]
) -> list[Finding]:
    findings: list[Finding] = []
    for line_no, line in enumerate(mask_fences(text).splitlines(), start=1):
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
                    # ``**CS-8 §9**``: a gloss after the ID would split the ID
                    # from its § token; leave it for a person to name both.
                    if re.match(r"\s*§", text[col:]):
                        continue
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
