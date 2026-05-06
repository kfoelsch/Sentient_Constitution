#!/usr/bin/env python3
"""Audit Chapter Five definition homes against cluster-member routing.

Placement contract:
- **Independent definitions:** canonical full O/E/C appear **only** in Part A
  (**Chapter Five section 1**). Cluster/family routing may point to them, but
  it never relocates their canonical bodies into section 2 or section 3.
- **Semi-independent definitions:** canonical full O/E/C appear **only** in Part B
  (**Chapter Five section 2**). They are never relocated into section 3.
- **Dependent-cluster definitions:** canonical full O/E/C for cluster-owned members
  appear **only** in Part C (**section 3**). The cluster contracts, dependent-cluster
  context lines, and other **section-3** definition bodies are authored **only** in
  Part C — not relocated into §1 or §2.

Routing inventory:
- Links listed under ``**Cluster members.**`` or ``**Family members.**``
  are the routing inventory for the local cluster type. A Part B roster is a
  semi-independent-cluster roster; a Part C roster is a dependent-cluster roster.
  ``**Read-with definitions.**``, ``**Read-with.**``, ``**Owning cluster note.**``,
  and ordinary prose links **do not** count as cluster membership—their cross-links may
  target any Chapter Five file.
- **Semi-independent joint-invocation cluster contracts** are introduced by
  ``**Cluster context**`` lines and must appear **only** in Part B (section 2).
  ``tools/ch5_structure_audit.py`` enforces that placement across Chapter Five files.
- Part B member rosters (**Cluster members.** / **Family members.**) may point to
  Part A only for entries whose canonical full O/E/C home remains **§1**. If a
  semi-independent term's O/E/C is in Part B, the roster must target Part B.
- Any ``Dependent-cluster context:`` contract must live in §3. For **Part C**
  dependent clusters, every ``**Cluster members.**`` link must target
  ``core_05-05_definitions_c_dependent_clusters.md`` (same file), and the linked slug’s
  full **O / E / C** must appear in **section 3**—not only under Part A or Part B.

The script is intentionally report-oriented. Listing modes show the routed
cluster/family inventory used by the audit; ``--audit`` fails on placement drift, stale Part B roster links
that still target Part A after a term’s O/E/C moved to §2, duplicate full O/E/C
titles, conflicting §2+§3 homes for the same slug, and unresolved cluster-member
anchors. Other structural shell/stub checks remain in ``tools/ch5_structure_audit.py``.
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
CLUSTER_MEMBERS_LINE = re.compile(r"^\*\*Cluster members\.\*\*")
FAMILY_MEMBERS_LINE = re.compile(r"^\*\*Family members\.\*\*")

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
    part_c_cluster_roster: bool  # Part C **Cluster members.** (Part C has no Family rosters)

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
        "--list-routed",
        action="store_true",
        help=(
            "List every Chapter Five link under Cluster members / Family members "
            "(Part B semi-independent cluster rosters and Part C dependent-cluster rosters)."
        ),
    )
    p.add_argument(
        "--list-dependent",
        action="store_true",
        help=argparse.SUPPRESS,
    )
    p.add_argument(
        "--list-independent",
        action="store_true",
        help=(
            "List every full O/E/C definition that is not listed in a "
            "Cluster members / Family members roster. This is a routing view; "
            "it can include §1 independent and §2 semi-independent entries."
        ),
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


def routing_expected_section(_owner_file: str, target_file: str, _slug: str) -> str:
    """Map roster link targets to expected canonical §1 / §2 / §3 for full O/E/C bodies."""
    return CH5_SECTION_BY_FILE[target_file]


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
            if CLUSTER_MEMBERS_LINE.match(
                line.strip()
            ) or FAMILY_MEMBERS_LINE.match(line.strip()):
                in_members = True
            if not in_members:
                continue
            stripped = line.strip()
            if (
                stripped.startswith("**Read-with")
                or stripped.startswith("**Joint")
                or stripped.startswith("**Owning cluster note")
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
                part_c_cluster_roster = file_name == CH5_PART_C
                expected_section = (
                    "3"
                    if part_c_cluster_roster
                    else routing_expected_section(file_name, target_file, slug)
                )
                yield ClusterMember(
                    title=title,
                    slug=slug,
                    href=href,
                    owner_file=file_name,
                    target_file=target_file,
                    expected_section=expected_section,
                    line=idx + 1,
                    owner_heading=owner_heading,
                    is_dependent_context=in_dependent_context,
                    part_c_cluster_roster=part_c_cluster_roster,
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


def print_routed(entries: list[DefinitionEntry], members: list[ClusterMember]) -> None:
    by_slug = entry_by_slug(entries)
    print("title\tslug\troster_kind\texpected_section\tcluster_owner\tmember_location\tcurrent_oec_locations")
    for member in sorted(members, key=lambda m: (m.expected_section, m.owner_file, m.line, m.title)):
        roster_kind = (
            "dependent-cluster"
            if member.owner_file == CH5_PART_C
            else "semi-independent-cluster"
        )
        current = [
            f"§{e.section}:{e.location}"
            for e in by_slug.get(member.slug, [])
            if e.has_full_oec
        ]
        print(
            f"{member.title}\t{member.slug}\t{roster_kind}\t§{member.expected_section}\t"
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
        expected = {"1": "§1", "2": "§2", "3": "§3"}[entry.section]
        print(f"{entry.title}\t{entry.primary_slug}\t{expected}\t§{entry.section}:{entry.location}")


def audit(entries: list[DefinitionEntry], members: list[ClusterMember]) -> list[str]:
    errors: list[str] = []
    by_slug = entry_by_slug(entries)
    members_by_slug = member_by_slug(members)
    for member in members:
        if (
            member.part_c_cluster_roster
            and member.target_file != CH5_PART_C
        ):
            errors.append(
                f"{member.location}: Part C **Cluster members.** link targets "
                f"{member.target_file} (#{member.slug}); roster members must use "
                f"{CH5_PART_C} anchors (relocate full O/E/C here). **Read-with** links "
                f"may still target Part A/B."
            )

    for member in members:
        if member.owner_file == CH5_PART_B and member.target_file == CH5_PART_A:
            loc_sec2 = [
                e
                for e in by_slug.get(member.slug, [])
                if e.has_full_oec and e.section == "2"
            ]
            if loc_sec2:
                errors.append(
                    f"{member.location}: Part B cluster roster still links to "
                    f"{CH5_PART_A} (#{member.slug}) but O/E/C is in §2; update href "
                    f"to {CH5_PART_B} or run tools/ch5_reanchor_post_split.py"
                )

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
            detail = "; ".join(
                f"{m.location}→§{m.expected_section}"
                for m in sorted(slug_members, key=lambda x: (x.owner_file, x.line))
            )
            errors.append(
                f"cluster member #{slug} has conflicting expected canonical sections "
                f"across rosters: {detail}"
            )
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
        secs = {e.section for e in slug_entries}
        if "2" in secs and "3" in secs:
            rendered = ", ".join(f"§{e.section}:{e.location}" for e in slug_entries)
            errors.append(
                f"canonical slug #{slug} has full O/E/C in both §2 and §3 (semi-independent "
                f"bodies belong only in §2; dependent-cluster bodies only in §3): {rendered}"
            )
            continue
        rendered = ", ".join(f"§{e.section}:{e.location}#{e.primary_slug}" for e in slug_entries)
        errors.append(f"duplicate full O/E/C canonical slug #{slug}: {rendered}")

    return errors


def main() -> int:
    args = parse_args()
    if args.list_dependent:
        args.list_routed = True
    if not (args.list_routed or args.list_independent or args.audit):
        args.audit = True
    root = Path(args.root).resolve()
    missing = [name for name in CH5_ALL if not (root / name).is_file()]
    if missing:
        print(f"Missing Chapter Five file(s): {', '.join(missing)}", file=sys.stderr)
        return 2

    entries, members = build_indexes(root)
    if args.list_routed:
        print_routed(entries, members)
    if args.list_independent:
        if args.list_routed:
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
