"""Shared index builders for Chapter Five and CJS-3 operational definitions."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_ALL, CH5_INDEX as CH5_PART_A, CH5_BANDS  # noqa: E402
from ch5_single_definition_audit import (  # noqa: E402
    HEADING_RE,
    body_until_next_heading,
    collect_cluster_members,
    href_for,
    owns_oec,
    previous_entry_anchor,
)

CJS3_FILES = (
    "corpus_joint_structure/cjs_03_cross_implementation_operational_terms.md",
    "corpus_joint_structure/cjs_03o_oversight_operations.md",
    "corpus_joint_structure/cjs_03p_participation_operations.md",
    "corpus_joint_structure/cjs_03a_accountability_operations.md",
    "corpus_joint_structure/cjs_03c_continuity_operations.md",
    "corpus_joint_structure/cjs_03i_integrative_operations.md",
)

CLUSTER_HEADING_RE = re.compile(r"^##\s+(CJS-3\.\d+)\s+(.+)$")
CH5_LINK_RE = re.compile(
    r"(?:core_05[a-z_\-]+\.md|Chapter Five|chapter five)",
    re.I,
)
OP_COMPONENT_RE = re.compile(r"^- OP-[OEC]:", re.MULTILINE)


@dataclass(frozen=True)
class Ch5Entry:
    term: str
    source_file: str
    anchor: str
    line_start: int
    line_end: int
    category: str
    cluster_membership: dict[str, str | int] | None = None


@dataclass
class Cjs3OperationalRule:
    label: str
    cluster_id: str
    file: str
    line: int
    has_op_o: bool = False
    has_op_e: bool = False
    has_op_c: bool = False
    body: str = ""
    ch5_links: list[str] = field(default_factory=list)

    @property
    def complete(self) -> bool:
        return self.has_op_o and self.has_op_e and self.has_op_c

    @property
    def missing_components(self) -> list[str]:
        return [
            name
            for name, present in (
                ("What it is", self.has_op_o),
                ("How to measure and assess", self.has_op_e),
                ("What must hold", self.has_op_c),
            )
            if not present
        ]


@dataclass
class Cjs3Cluster:
    cluster_id: str
    title: str
    file: str
    start_line: int
    end_line: int
    body: str
    read_with: list[str] = field(default_factory=list)
    rules: list[Cjs3OperationalRule] = field(default_factory=list)
    ch5_links: list[str] = field(default_factory=list)


def _body_end(lines: list[str], heading_idx: int, max_depth: int) -> int:
    for idx in range(heading_idx + 1, len(lines)):
        stripped = lines[idx].strip()
        match = HEADING_RE.match(stripped)
        if (
            match
            and len(match.group(1)) <= max_depth
            and not match.group(2).strip().startswith("In plain terms:")
        ):
            return idx
    return len(lines)


def _category_for(lines: list[str], idx: int, depth: int) -> str:
    if depth == 5:
        return "dependent_cluster"
    window = "\n".join(lines[max(0, idx - 40) : idx])
    if ": Independent terms" in window or "### 1. Independent Definitions" in window:
        return "independent"
    return "semi_independent"


def collect_ch5_entries(root: Path) -> list[Ch5Entry]:
    """Index Chapter Five definitions with O/E/C bodies."""
    from collections import defaultdict

    memberships: dict[str, list[dict[str, str | int]]] = defaultdict(list)
    for member in collect_cluster_members(root):
        cluster_file = member.target.split("#", 1)[0] if "#" in member.target else CH5_BANDS[0]
        memberships[member.label].append(
            {
                "cluster": member.owner,
                "cluster_file": cluster_file,
                "line": member.line,
            }
        )

    entries: list[Ch5Entry] = []
    for file_name in CH5_ALL:
        if file_name == CH5_PART_A:
            continue
        path = root / file_name
        if not path.is_file():
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        for idx, raw in enumerate(lines):
            stripped = raw.strip()
            match = HEADING_RE.match(stripped)
            if not match:
                continue
            depth = len(match.group(1))
            label = match.group(2).strip()
            if label.startswith("In plain terms:") or re.match(r"3\.\d+(?:\.\d+)?\s", label):
                continue
            if depth not in (4, 5):
                continue
            body = body_until_next_heading(lines, idx, depth)
            if not owns_oec(body):
                continue
            anchor_href = href_for(file_name, previous_entry_anchor(lines, idx), label)
            anchor = anchor_href.split("#", 1)[-1]
            member_entries = memberships.get(label, [])
            entries.append(
                Ch5Entry(
                    term=label,
                    source_file=file_name,
                    anchor=f"#{anchor}",
                    line_start=idx + 1,
                    line_end=_body_end(lines, idx, depth),
                    category=_category_for(lines, idx, depth),
                    cluster_membership=member_entries[0] if member_entries else None,
                )
            )
    return sorted(entries, key=lambda entry: entry.term.casefold())


def _extract_read_with(body: str) -> list[str]:
    refs: list[str] = []
    in_block = False
    for line in body.splitlines():
        stripped = line.strip()
        if stripped == "Read it with:":
            in_block = True
            continue
        if in_block:
            if stripped.startswith("- "):
                refs.append(stripped[2:].strip())
                continue
            if stripped:
                break
    return refs


def _extract_ch5_links(text: str) -> list[str]:
    return sorted(set(CH5_LINK_RE.findall(text)))


def _extract_rules(cluster: Cjs3Cluster) -> list[Cjs3OperationalRule]:
    lines = cluster.body.splitlines()
    rules: list[Cjs3OperationalRule] = []
    current: Cjs3OperationalRule | None = None
    previous_label: tuple[str, int] | None = None
    block_lines: list[str] = []

    def is_label(line: str) -> bool:
        stripped = line.strip()
        if not stripped:
            return False
        if stripped.startswith(
            (
                "- ",
                "#",
                "|",
                "---",
                "<",
                "```",
                "*In plain terms:",
                "**Primary ",
                "**Secondary ",
                "**Tertiary ",
                "**In scope:",
                "**Out of scope:",
                "**Depends on:",
            )
        ):
            return False
        if re.match(r"^\d+\.\s", stripped):
            return False
        if stripped in {
            "Read it with:",
            "Role-definition reading rule",
            "Competency gate and standing interface",
        }:
            return True
        if stripped.endswith(":"):
            return False
        return True

    def flush_rule() -> None:
        nonlocal current, block_lines
        if current is None:
            return
        body = "\n".join(block_lines)
        current.body = body
        current.ch5_links = _extract_ch5_links(body)
        block_lines = []
        current = None

    for offset, line in enumerate(lines, start=cluster.start_line + 1):
        stripped = line.strip()
        if is_label(stripped):
            flush_rule()
            previous_label = (stripped, offset)
            continue
        if stripped in {
            "- **What it is**",
            "- **How to measure and assess**",
            "- **What must hold**",
        } or stripped.startswith("- OP-"):
            if current is None:
                label, label_line = previous_label or ("Unlabeled operational rule", offset)
                current = Cjs3OperationalRule(
                    label=label,
                    cluster_id=cluster.cluster_id,
                    file=cluster.file,
                    line=label_line,
                )
                rules.append(current)
            block_lines.append(line)
            if stripped == "- **What it is**" or stripped.startswith("- OP-O:"):
                current.has_op_o = True
            elif stripped == "- **How to measure and assess**" or stripped.startswith("- OP-E:"):
                current.has_op_e = True
            elif stripped == "- **What must hold**" or stripped.startswith("- OP-C:"):
                current.has_op_c = True
            if current.complete:
                flush_rule()
    flush_rule()
    return rules


def _extract_clusters_from_file(root: Path, rel_path: str) -> list[Cjs3Cluster]:
    path = root / rel_path
    if not path.is_file():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    starts: list[tuple[int, str, str]] = []
    for idx, line in enumerate(lines):
        match = CLUSTER_HEADING_RE.match(line)
        if match:
            starts.append((idx, match.group(1), match.group(2).strip()))

    clusters: list[Cjs3Cluster] = []
    for pos, (start_idx, cluster_id, title) in enumerate(starts):
        end_idx = starts[pos + 1][0] if pos + 1 < len(starts) else len(lines)
        body = "\n".join(lines[start_idx + 1 : end_idx])
        cluster = Cjs3Cluster(
            cluster_id=cluster_id,
            title=title,
            file=rel_path,
            start_line=start_idx + 1,
            end_line=end_idx,
            body=body,
            read_with=_extract_read_with(body),
            ch5_links=_extract_ch5_links(body),
        )
        cluster.rules = _extract_rules(cluster)
        clusters.append(cluster)
    return clusters


def collect_cjs3_clusters(root: Path) -> list[Cjs3Cluster]:
    clusters: list[Cjs3Cluster] = []
    for rel_path in CJS3_FILES:
        clusters.extend(_extract_clusters_from_file(root, rel_path))
    return clusters


def ch5_term_lookup(entries: list[Ch5Entry]) -> dict[str, Ch5Entry]:
    """Case-insensitive lookup; prefers exact label match."""
    lookup: dict[str, Ch5Entry] = {}
    for entry in entries:
        lookup[entry.term.casefold()] = entry
    return lookup


def normalize_term_label(label: str) -> str:
    return re.sub(r"\s+", " ", label.strip()).casefold()
