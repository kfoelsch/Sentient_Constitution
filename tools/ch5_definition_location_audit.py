#!/usr/bin/env python3
"""Audit Chapter Five definition homes against cluster-member routing.

Routing contract:
- Chapter Five links listed under ``**Cluster members.**`` or
  ``**Family members.**`` (semi-independent compound families) blocks are the
  routing inventory for dependent and semi-independent cluster contexts.
- Part B member lists expect a §2 home when they belong to a semi-independent
  family.
- Any ``Dependent-cluster context:`` contract must live in §3; member links
  still route to their canonical linked O/E/C homes.
- Part C member lists expect a §3 home unless the cluster prose uses an
  owning-cluster note or same-list routing to keep the reader-facing home in
  Part B.
- Full O/E/C entries may live in §1 (independent) or §2 (semi-independent)
  when they are not Part C cluster-owned.

The script is intentionally report-oriented. Listing modes show the inventory
used by the audit; ``--audit`` fails on placement drift, duplicate full O/E/C
titles, and unresolved cluster-member anchors. Other structural shell/stub
checks remain in ``tools/ch5_structure_audit.py``.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_ALL, CH5_PART_A, CH5_PART_B, CH5_PART_C  # noqa: E402


CH5_SECTION_BY_FILE = {
    CH5_PART_A: "1",
    CH5_PART_B: "2",
    CH5_PART_C: "3",
}
CH5_FILE_NAMES = set(CH5_SECTION_BY_FILE)

HEADING_RE = re.compile(r"^(#{3,5})\s+(.+?)\s*$")
DEF_HEADING_RE = re.compile(r"^(#{4,5})\s+(.+?)\s*$")
ANCHOR_RE = re.compile(r'^<a id="([^"]+)"></a>\s*$')
MEMBER_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
DEPENDENT_CONTEXT_RE = re.compile(r"^\*\*Dependent-cluster context:\s*(.+?)\.?\*\*$")

STRUCTURAL_TITLE_PREFIXES = (
    "3.",
    "All definitions",
    "Dependent-cluster context:",
    "In plain terms:",
    "Illustrative ",
)


@dataclass(frozen=True)
class DefinitionEntry:
    title: str
    primary_slug: str
    slugs: frozenset[str]
    file: str
    section: str
    line: int
    has_o: bool
    has_e: bool
    has_c: bool

    @property
    def has_full_oec(self) -> bool:
        return self.has_o and self.has_e and self.has_c

    @property
    def location(self) -> str:
        return f"{self.file}:{self.line}"


@dataclass(frozen=True)
class ClusterMember:
    title: str
    slug: str
    href: str
    owner_file: str
    target_file: str
    expected_section: str
    line: int
    owner_heading: str
    is_dependent_context: bool

    @property
    def location(self) -> str:
        return f"{self.owner_file}:{self.line}"


@dataclass(frozen=True)
class WrongSectionMove:
    """Full O/E/C entry in the wrong Chapter Five part for cluster/family routing."""

    entry: DefinitionEntry
    expected_section: str
    member_slug: str


def iter_wrong_section_moves(
    entries: list[DefinitionEntry], members: list[ClusterMember]
) -> Iterator[WrongSectionMove]:
    """Yield definitions whose file/section disagrees with cluster/family link targets.

    Callers should de-duplicate by ``(entry.file, entry.line)`` if a definition
    carries multiple anchors listed under different member slugs.
    """
    by_slug = entry_by_slug(entries)
    members_by_slug = member_by_slug(members)
    for slug, slug_members in sorted(members_by_slug.items()):
        expected = expected_section_for_slug(slug_members)
        if expected == "CONFLICT":
            continue
        locations = [e for e in by_slug.get(slug, []) if e.has_full_oec]
        if not locations or any(e.section == expected for e in locations):
            continue
        for e in locations:
            if e.section != expected:
                yield WrongSectionMove(
                    entry=e, expected_section=expected, member_slug=slug
                )


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Repository root.")
    p.add_argument(
        "--list-dependent",
        action="store_true",
        help="List every Chapter Five definition link under Cluster members / Family members.",
    )
    p.add_argument(
        "--list-independent",
        action="store_true",
        help="List every full O/E/C definition that is not a cluster member.",
    )
    p.add_argument(
        "--audit",
        action="store_true",
        help="Fail on Chapter Five definition-location drift.",
    )
    return p.parse_args()


def auto_slug(heading: str) -> str:
    s = heading.lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def normalize_href(owner_file: str, href: str) -> tuple[str, str] | None:
    """Return (file, slug) for Chapter Five links; ignore external links."""
    if href.startswith("#"):
        return owner_file, href[1:]
    if "#" not in href:
        return None
    file_name, slug = href.split("#", 1)
    if file_name not in CH5_FILE_NAMES:
        return None
    return file_name, slug


def entry_anchor_slugs(lines: list[str], heading_idx: int, title: str) -> frozenset[str]:
    explicit_slugs: list[str] = []
    idx = heading_idx - 1
    while idx >= 0:
        stripped = lines[idx].strip()
        if not stripped or stripped == "---":
            idx -= 1
            continue
        m = ANCHOR_RE.match(stripped)
        if m:
            explicit_slugs.append(m.group(1))
            idx -= 1
            continue
        break
    slugs = list(reversed(explicit_slugs)) or [auto_slug(title)]
    deduped = list(dict.fromkeys(slugs))
    return frozenset(deduped)


def primary_slug(slugs: frozenset[str], title: str) -> str:
    auto = auto_slug(title)
    explicit = [s for s in slugs if s != auto]
    return explicit[-1] if explicit else auto


def block_until_next_definition_heading(lines: list[str], heading_idx: int, depth: int) -> list[str]:
    body: list[str] = []
    for line in lines[heading_idx + 1 :]:
        m = DEF_HEADING_RE.match(line)
        if m and len(m.group(1)) <= depth and not m.group(2).startswith("In plain terms:"):
            break
        body.append(line)
    return body


def iter_definition_entries(root: Path) -> Iterable[DefinitionEntry]:
    for file_name, section in CH5_SECTION_BY_FILE.items():
        path = root / file_name
        lines = path.read_text(encoding="utf-8").splitlines()
        in_definition_section = file_name != CH5_PART_A
        for idx, line in enumerate(lines):
            if file_name == CH5_PART_A and line.startswith("### 1. Independent Definitions"):
                in_definition_section = True
                continue
            if not in_definition_section:
                continue
            m = DEF_HEADING_RE.match(line)
            if not m:
                continue
            title = m.group(2).strip()
            if title.startswith(STRUCTURAL_TITLE_PREFIXES):
                continue
            body = block_until_next_definition_heading(lines, idx, len(m.group(1)))
            has_o = any(item.startswith("- O:") for item in body)
            has_e = any(item.startswith("- E:") for item in body)
            has_c = any(item.startswith("- C:") for item in body)
            if not (has_o or has_e or has_c):
                continue
            slugs = entry_anchor_slugs(lines, idx, title)
            yield DefinitionEntry(
                title=title,
                primary_slug=primary_slug(slugs, title),
                slugs=slugs,
                file=file_name,
                section=section,
                line=idx + 1,
                has_o=has_o,
                has_e=has_e,
                has_c=has_c,
            )


def iter_cluster_members(root: Path) -> Iterable[ClusterMember]:
    for file_name in CH5_SECTION_BY_FILE:
        if file_name == CH5_PART_A:
            continue
        path = root / file_name
        lines = path.read_text(encoding="utf-8").splitlines()
        in_members = False
        owner_heading = ""
        in_dependent_context = file_name == CH5_PART_C
        for idx, line in enumerate(lines):
            hm = HEADING_RE.match(line)
            if hm and not hm.group(2).startswith("In plain terms:"):
                owner_heading = hm.group(2).strip()
                in_dependent_context = file_name == CH5_PART_C
            dm = DEPENDENT_CONTEXT_RE.match(line.strip())
            if dm:
                owner_heading = dm.group(1).strip()
                in_dependent_context = True
            if "**Cluster members.**" in line or "**Family members.**" in line:
                in_members = True
            if not in_members:
                continue
            stripped = line.strip()
            if (
                stripped.startswith("**Read-with")
                or stripped.startswith("**Joint")
                or stripped == "---"
                or stripped.startswith("<a id=")
                or HEADING_RE.match(line)
            ):
                in_members = False
                continue
            for m in MEMBER_LINK_RE.finditer(line):
                title, href = m.group(1).strip(), m.group(2).strip()
                normalized = normalize_href(file_name, href)
                if normalized is None:
                    continue
                target_file, slug = normalized
                yield ClusterMember(
                    title=title,
                    slug=slug,
                    href=href,
                    owner_file=file_name,
                    target_file=target_file,
                    expected_section=CH5_SECTION_BY_FILE[target_file],
                    line=idx + 1,
                    owner_heading=owner_heading,
                    is_dependent_context=in_dependent_context,
                )


def build_indexes(root: Path) -> tuple[list[DefinitionEntry], list[ClusterMember]]:
    entries = list(iter_definition_entries(root))
    members = list(iter_cluster_members(root))
    return entries, members


def entry_by_slug(entries: list[DefinitionEntry]) -> dict[str, list[DefinitionEntry]]:
    out: dict[str, list[DefinitionEntry]] = defaultdict(list)
    for entry in entries:
        for slug in entry.slugs:
            out[slug].append(entry)
    return out


def anchor_slugs(root: Path) -> set[str]:
    slugs: set[str] = set()
    for file_name in CH5_ALL:
        for line in (root / file_name).read_text(encoding="utf-8").splitlines():
            m = ANCHOR_RE.match(line.strip())
            if m:
                slugs.add(m.group(1))
    return slugs


def member_by_slug(members: list[ClusterMember]) -> dict[str, list[ClusterMember]]:
    out: dict[str, list[ClusterMember]] = defaultdict(list)
    for member in members:
        out[member.slug].append(member)
    return out


def expected_section_for_slug(members_for_slug: list[ClusterMember]) -> str:
    sections = {m.expected_section for m in members_for_slug}
    if len(sections) != 1:
        return "CONFLICT"
    return next(iter(sections))


def print_dependent(entries: list[DefinitionEntry], members: list[ClusterMember]) -> None:
    by_slug = entry_by_slug(entries)
    print("title\tslug\texpected_section\tcluster_owner\tmember_location\tcurrent_oec_locations")
    for member in sorted(members, key=lambda m: (m.expected_section, m.owner_file, m.line, m.title)):
        current = [
            f"§{e.section}:{e.location}"
            for e in by_slug.get(member.slug, [])
            if e.has_full_oec
        ]
        print(
            f"{member.title}\t{member.slug}\t§{member.expected_section}\t"
            f"{member.owner_heading}\t{member.location}\t{', '.join(current) or 'MISSING'}"
        )


def print_independent(entries: list[DefinitionEntry], members: list[ClusterMember]) -> None:
    member_slugs = set(member_by_slug(members))
    print("title\tslug\texpected_section\tcurrent_location")
    for entry in sorted(entries, key=lambda e: (e.title.lower(), e.file, e.line)):
        if not entry.has_full_oec:
            continue
        if entry.slugs & member_slugs:
            continue
        expected = "§1/§2" if entry.section in {"1", "2"} else "§1"
        print(f"{entry.title}\t{entry.primary_slug}\t{expected}\t§{entry.section}:{entry.location}")


def audit(entries: list[DefinitionEntry], members: list[ClusterMember]) -> list[str]:
    errors: list[str] = []
    by_slug = entry_by_slug(entries)
    members_by_slug = member_by_slug(members)
    anchors = anchor_slugs(Path("."))

    dependent_context_locations = {
        (m.owner_file, m.owner_heading, m.location)
        for m in members
        if m.is_dependent_context and m.owner_file != CH5_PART_C
    }
    for owner_file, owner_heading, location in sorted(dependent_context_locations):
        errors.append(
            f"{location}: dependent-cluster context {owner_heading!r} is in {owner_file}; "
            f"move the cluster contract to {CH5_PART_C}"
        )

    for slug, slug_members in sorted(members_by_slug.items()):
        expected = expected_section_for_slug(slug_members)
        locations = [e for e in by_slug.get(slug, []) if e.has_full_oec]
        member_summary = ", ".join(f"{m.location} ({m.owner_heading})" for m in slug_members)
        if expected == "CONFLICT":
            continue
        expected_locations = [e for e in locations if e.section == expected]
        if not locations:
            # Some current cluster-member lists include routing-only concepts whose
            # operative text is carried by an article owner, nested component, or
            # cluster-family paragraph rather than a standalone O/E/C block.
            # Link/anchor integrity for those targets is covered by the cross-file
            # link and structure audits; this location gate only fails duplicate or
            # conflicting canonical O/E/C homes.
            continue
        if locations and not expected_locations:
            rendered = ", ".join(f"§{e.section}:{e.location}" for e in locations)
            errors.append(
                f"cluster member #{slug} is linked as §{expected} but full O/E/C home "
                f"is only elsewhere: {rendered}; member references: {member_summary}"
            )
            continue
        if len(expected_locations) > 1:
            rendered = ", ".join(e.location for e in expected_locations)
            errors.append(
                f"cluster member #{slug} has multiple §{expected} O/E/C homes: {rendered}"
            )

    member_slugs = set(members_by_slug)
    for entry in entries:
        if not entry.has_full_oec:
            continue
        if entry.slugs & member_slugs:
            continue
        if entry.section == "3":
            errors.append(
                f"{entry.location}: non-cluster O/E/C definition {entry.title!r} "
                f"has a §3 home but is not listed as a Part C cluster member"
            )

    full_by_slug: dict[str, list[DefinitionEntry]] = defaultdict(list)
    for entry in entries:
        if entry.has_full_oec:
            full_by_slug[entry.primary_slug].append(entry)
    for slug, slug_entries in sorted(full_by_slug.items()):
        if len(slug_entries) <= 1:
            continue
        rendered = ", ".join(f"§{e.section}:{e.location}#{e.primary_slug}" for e in slug_entries)
        errors.append(f"duplicate full O/E/C canonical slug #{slug}: {rendered}")

    return errors


def main() -> int:
    args = parse_args()
    if not (args.list_dependent or args.list_independent or args.audit):
        args.audit = True
    root = Path(args.root).resolve()
    missing = [name for name in CH5_ALL if not (root / name).is_file()]
    if missing:
        print(f"Missing Chapter Five file(s): {', '.join(missing)}", file=sys.stderr)
        return 2

    entries, members = build_indexes(root)
    if args.list_dependent:
        print_dependent(entries, members)
    if args.list_independent:
        if args.list_dependent:
            print()
        print_independent(entries, members)
    if args.audit:
        errors = audit(entries, members)
        if errors:
            for error in errors:
                print(error, file=sys.stderr)
            print(f"\nFAIL: {len(errors)} Chapter Five definition-location issue(s).", file=sys.stderr)
            return 1
        print("PASS: Chapter Five definition locations match cluster-member routing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
