#!/usr/bin/env python3
"""Audit Chapter Five single-definition and directory invariants.

The rule enforced here is intentionally simple:

- each visible Chapter Five definition label appears once;
- the non-operative directory has separate Definitions A-Z and Clusters A-Z
  lists, with no duplicate display labels;
- placeholder-only O/E/C shells are forbidden;
- a linked term appears in at most one ``Cluster members.`` roster.

HTML anchors and Markdown fragments are treated only as navigation targets.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_ALL, CH5_PART_A, CH5_PART_C  # noqa: E402

HEADING_RE = re.compile(r"^(#{4,5})\s+(.+)$")
ANCHOR_RE = re.compile(r'<a id="([^"]+)"></a>')
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
DIR_ROW_RE = re.compile(r"^-\s+\[([^\]]+)\]\(([^)]+)\)\s*$")

SECTION1_HEADING = "### 1. Independent Definitions"
DEFINITIONS_HEADING = "#### Definitions A-Z"
CLUSTERS_HEADING = "#### Clusters A-Z"

PLACEHOLDER_PATTERNS = (
    "canonical definition is in",
    "non-canonical pointer",
    "placeholder preserves",
    "alphabetical locator stub",
    "retained title is an alphabetical locator",
)


@dataclass(frozen=True)
class Entry:
    label: str
    href: str
    file: str
    line: int
    body: str


@dataclass(frozen=True)
class ClusterHead:
    label: str
    href: str
    file: str
    line: int


@dataclass(frozen=True)
class DirectoryRow:
    label: str
    href: str
    line: int
    list_name: str


@dataclass(frozen=True)
class ClusterMember:
    label: str
    href: str
    owner: str
    line: int


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Repository root.")
    return p.parse_args()


def auto_anchor(label: str) -> str:
    out = label.strip().lower()
    out = re.sub(r"[^\w\s-]", "", out)
    out = re.sub(r"\s+", "-", out)
    out = re.sub(r"-+", "-", out)
    return out.strip("-")


def previous_entry_anchor(lines: list[str], heading_idx: int) -> str | None:
    anchors: list[str] = []
    idx = heading_idx - 1
    while idx >= 0:
        stripped = lines[idx].strip()
        if not stripped:
            idx -= 1
            continue
        match = ANCHOR_RE.match(stripped)
        if match:
            anchors.append(match.group(1))
            idx -= 1
            continue
        if stripped == "---":
            idx -= 1
            continue
        break
    return anchors[0] if anchors else None


def body_until_next_heading(lines: list[str], heading_idx: int, max_depth: int) -> str:
    body: list[str] = []
    for idx in range(heading_idx + 1, len(lines)):
        match = HEADING_RE.match(lines[idx].strip())
        if match and len(match.group(1)) <= max_depth:
            break
        body.append(lines[idx])
    return "\n".join(body)


def owns_oec(body: str) -> bool:
    return bool(
        re.search(r"^- O:", body, re.MULTILINE)
        and re.search(r"^- [EC]:", body, re.MULTILINE)
    )


def href_for(file_name: str, anchor: str | None, label: str) -> str:
    fragment = anchor or auto_anchor(label)
    if file_name == CH5_PART_A:
        return f"#{fragment}"
    return f"{file_name}#{fragment}"


def collect_entries_and_clusters(root: Path) -> tuple[list[Entry], list[ClusterHead]]:
    entries: list[Entry] = []
    clusters: list[ClusterHead] = []
    for file_name in CH5_ALL:
        path = root / file_name
        lines = path.read_text(encoding="utf-8").splitlines()
        in_part_a_defs = False
        for idx, raw in enumerate(lines):
            stripped = raw.strip()
            if file_name == CH5_PART_A:
                if stripped == SECTION1_HEADING:
                    in_part_a_defs = True
                    continue
                if not in_part_a_defs:
                    continue
            match = HEADING_RE.match(stripped)
            if not match:
                continue
            depth = len(match.group(1))
            label = match.group(2).strip()

            if file_name == CH5_PART_C and depth == 4:
                numbered = re.match(r"(3\.(\d+))\s+(.+)", label)
                if numbered and int(numbered.group(2)) >= 3:
                    display = f"{numbered.group(1)} {numbered.group(3).strip()}"
                    clusters.append(
                        ClusterHead(
                            label=display,
                            href=href_for(
                                file_name, previous_entry_anchor(lines, idx), display
                            ),
                            file=file_name,
                            line=idx + 1,
                        )
                    )
                continue

            if file_name == CH5_PART_C:
                if depth != 5:
                    continue
                body = body_until_next_heading(lines, idx, 5)
            else:
                if depth != 4:
                    continue
                body = body_until_next_heading(lines, idx, 4)

            if owns_oec(body):
                entries.append(
                    Entry(
                        label=label,
                        href=href_for(file_name, previous_entry_anchor(lines, idx), label),
                        file=file_name,
                        line=idx + 1,
                        body=body,
                    )
                )
    return entries, clusters


def parse_directory(root: Path) -> tuple[list[DirectoryRow], list[str]]:
    path = root / CH5_PART_A
    lines = path.read_text(encoding="utf-8").splitlines()
    violations: list[str] = []
    try:
        defs_idx = next(i for i, line in enumerate(lines) if line.strip() == DEFINITIONS_HEADING)
        clusters_idx = next(i for i, line in enumerate(lines) if line.strip() == CLUSTERS_HEADING)
    except StopIteration:
        return [], [f"{path}: directory must contain '{DEFINITIONS_HEADING}' and '{CLUSTERS_HEADING}'"]
    if clusters_idx <= defs_idx:
        violations.append(f"{path}: '{CLUSTERS_HEADING}' must follow '{DEFINITIONS_HEADING}'")

    rows: list[DirectoryRow] = []

    def scan(start: int, end: int, list_name: str) -> None:
        for idx in range(start + 1, end):
            stripped = lines[idx].strip()
            if not stripped or stripped.startswith("<a id="):
                continue
            if stripped.startswith("#### "):
                continue
            if stripped == "</details>":
                break
            if stripped.startswith("- "):
                match = DIR_ROW_RE.match(stripped)
                if not match:
                    violations.append(f"{path}:{idx + 1}: malformed directory row: {stripped}")
                    continue
                rows.append(
                    DirectoryRow(
                        label=match.group(1).strip(),
                        href=match.group(2).strip(),
                        line=idx + 1,
                        list_name=list_name,
                    )
                )

    details_end = next(
        (i for i in range(clusters_idx + 1, len(lines)) if lines[i].strip() == "</details>"),
        len(lines),
    )
    scan(defs_idx, clusters_idx, "Definitions A-Z")
    scan(clusters_idx, details_end, "Clusters A-Z")
    return rows, violations


def normalized_sort_key(label: str, *, cluster: bool = False) -> str:
    if cluster:
        label = re.sub(r"^3\.\d+\s+", "", label)
    return label.casefold()


def sorted_violations(rows: list[DirectoryRow]) -> list[str]:
    violations: list[str] = []
    for list_name, cluster in (("Definitions A-Z", False), ("Clusters A-Z", True)):
        subset = [row for row in rows if row.list_name == list_name]
        prev: DirectoryRow | None = None
        prev_key = ""
        for row in subset:
            key = normalized_sort_key(row.label, cluster=cluster)
            if prev is not None and key < prev_key:
                violations.append(
                    f"{CH5_PART_A}:{row.line}: {list_name} row '{row.label}' "
                    f"should sort before '{prev.label}'"
                )
            prev = row
            prev_key = key
    return violations


def collect_cluster_members(root: Path) -> list[ClusterMember]:
    path = root / CH5_PART_C
    lines = path.read_text(encoding="utf-8").splitlines()
    members: list[ClusterMember] = []
    owner = ""
    in_roster = False
    for idx, raw in enumerate(lines):
        stripped = raw.strip()
        heading = re.match(r"^####\s+(3\.\d+\s+.+)$", stripped)
        if heading:
            owner = heading.group(1)
            in_roster = False
            continue
        if stripped == "**Cluster members.** This cluster comprises:" or stripped.startswith(
            "**Cluster members.** This cluster comprises "
        ):
            in_roster = True
            continue
        if in_roster and (
            stripped.startswith("**")
            or stripped == "---"
            or stripped.startswith("<a id=")
            or stripped.startswith("#### ")
        ):
            in_roster = False
            continue
        if in_roster and stripped.startswith("- "):
            for label, href in LINK_RE.findall(stripped):
                if href.startswith("core_05-05_definitions_") or href.startswith("#"):
                    members.append(ClusterMember(label=label, href=href, owner=owner, line=idx + 1))
    return members


def audit(root: Path) -> list[str]:
    violations: list[str] = []
    entries, clusters = collect_entries_and_clusters(root)
    directory_rows, directory_parse_violations = parse_directory(root)
    violations.extend(directory_parse_violations)

    by_label: dict[str, list[Entry]] = defaultdict(list)
    for entry in entries:
        by_label[entry.label].append(entry)
        lowered = entry.body.casefold()
        if any(marker in lowered for marker in PLACEHOLDER_PATTERNS):
            violations.append(
                f"{root / entry.file}:{entry.line}: placeholder-only or locator-style "
                f"definition body is not allowed for '{entry.label}'"
            )
    for label, label_entries in sorted(by_label.items()):
        if len(label_entries) > 1:
            rendered = ", ".join(f"{e.file}:{e.line}" for e in label_entries)
            violations.append(f"duplicate Chapter Five definition label '{label}': {rendered}")

    if directory_rows:
        directory_by_label: dict[str, list[DirectoryRow]] = defaultdict(list)
        for row in directory_rows:
            directory_by_label[row.label].append(row)
        for label, rows in sorted(directory_by_label.items()):
            if len(rows) > 1:
                rendered = ", ".join(f"line {row.line} ({row.list_name})" for row in rows)
                violations.append(f"{CH5_PART_A}: duplicate directory display label '{label}': {rendered}")
        violations.extend(sorted_violations(directory_rows))

        expected_defs = {(entry.label, entry.href) for entry in entries}
        actual_defs = {
            (row.label, row.href)
            for row in directory_rows
            if row.list_name == "Definitions A-Z"
        }
        expected_clusters = {(cluster.label, cluster.href) for cluster in clusters}
        actual_clusters = {
            (row.label, row.href)
            for row in directory_rows
            if row.list_name == "Clusters A-Z"
        }
        for label, href in sorted(expected_defs - actual_defs):
            violations.append(f"{CH5_PART_A}: missing definition directory row [{label}]({href})")
        for label, href in sorted(actual_defs - expected_defs):
            violations.append(f"{CH5_PART_A}: extra definition directory row [{label}]({href})")
        for label, href in sorted(expected_clusters - actual_clusters):
            violations.append(f"{CH5_PART_A}: missing cluster directory row [{label}]({href})")
        for label, href in sorted(actual_clusters - expected_clusters):
            violations.append(f"{CH5_PART_A}: extra cluster directory row [{label}]({href})")

    member_by_label: dict[str, list[ClusterMember]] = defaultdict(list)
    for member in collect_cluster_members(root):
        member_by_label[member.label].append(member)
    for label, members in sorted(member_by_label.items()):
        if len(members) > 1:
            rendered = ", ".join(f"line {m.line} ({m.owner})" for m in members)
            violations.append(
                f"{CH5_PART_C}: cluster member '{label}' appears in more than one roster: {rendered}"
            )

    return violations


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    violations = audit(root)
    if violations:
        print("FAIL: Chapter Five single-definition audit detected issues:", file=sys.stderr)
        for violation in violations:
            print(violation, file=sys.stderr)
        return 1
    print("PASS: Chapter Five has one definition row per label, one directory row per label, and one cluster-owner roster per term.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
