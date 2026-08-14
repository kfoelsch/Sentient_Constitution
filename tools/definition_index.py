"""Shared index builders for Chapter Five and CJS-3 operational definitions."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_ALL, CH5_APEX, CH5_INDEX as CH5_PART_A, CH5_BANDS  # noqa: E402
from ch5_single_definition_audit import (  # noqa: E402
    HEADING_RE,
    body_until_next_heading,
    collect_cluster_members,
    href_for,
    owns_oec,
    previous_entry_anchor,
)
from cjs_odef_format import guidepost_complete  # noqa: E402

CJS3_FILES = (
    "corpus_joint_structure/cjs_03_cross_implementation_operational_terms.md",
    "corpus_joint_structure/cjs_03o_oversight_operations.md",
    "corpus_joint_structure/cjs_03p_participation_operations.md",
    "corpus_joint_structure/cjs_03a_accountability_operations.md",
    "corpus_joint_structure/cjs_03c_continuity_operations.md",
    "corpus_joint_structure/cjs_03i_integrative_operations.md",
)
CJS3_PROCESS_HOME = "corpus_joint_structure/cjs_03_audit_process.md"

CH01_FILES = (
    "core_00_preamble.md",
    "core_01_a_values_principles.md",
    "core_01_b_interaction_interpretation.md",
    "core_01_c_stewardship_capacity_principles.md",
)

CLUSTER_HEADING_RE = re.compile(r"^##\s+(CJS-3\.\d+)\s+(.+)$")
CH5_LINK_RE = re.compile(
    r"(?:core_05[a-z_\-]+\.md|Chapter Five|chapter five)",
    re.I,
)
CH5_TERM_LINK_RE = re.compile(
    r"\[([^\]]+)\]\((?:\.\./)?(core_05[a-z_\-]+\.md)(?:#[^)]*)?\)"
)
DEF_CLUSTER_RE = re.compile(r"\bDef\.([OPACI]\d+)\b")
PRINCIPLE_HEADING_RE = re.compile(r"^(#{3,4})\s+(\d+(?:\.\d+)*)(?:\.)?\s+(.+)$")
DAC_WIDGET_RE = re.compile(
    r"^- \[([^\]]+)\]\([^)]+\) · \[O\]\([^)]+\) · \[M\]\([^)]+\) · \[A\]\([^)]+\) · \[C\]\([^)]+\)",
    re.MULTILINE,
)
ODEF_CITE_RE = re.compile(r"\b(?:oDef|CJS-3)\.(\d+)\b")
CJS3_FILE_LINK_RE = re.compile(r"cjs_03[a-z0-9_]*\.md(?:#[a-z0-9\-]+)?", re.I)
LETTER_O_RE = re.compile(r"^- O:", re.MULTILINE)
LETTER_M_RE = re.compile(r"^- M:", re.MULTILINE)
LETTER_A_RE = re.compile(r"^- A:", re.MULTILINE)
LETTER_C_RE = re.compile(r"^- C:", re.MULTILINE)
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
    cluster_id: str | None = None
    has_o: bool = False
    has_m: bool = False
    has_a: bool = False
    has_c: bool = False


@dataclass
class PrincipleRecord:
    section: str
    title: str
    file: str
    line: int
    body: str = ""
    dac_terms: list[str] = field(default_factory=list)


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
    def has_what_it_is(self) -> bool:
        return self.has_op_o

    @property
    def has_how_to_measure(self) -> bool:
        return self.has_op_e

    @property
    def has_what_must_hold(self) -> bool:
        return self.has_op_c

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


def _category_for(lines: list[str], idx: int, depth: int, file_name: str) -> str:
    if file_name in CH5_APEX:
        return "apex"
    if depth == 5:
        return "dependent_cluster"
    window = "\n".join(lines[max(0, idx - 40) : idx])
    if ": Independent terms" in window or "### 1. Independent Definitions" in window:
        return "independent"
    return "semi_independent"


def _def_cluster_id(*texts: str) -> str | None:
    for text in texts:
        if not text:
            continue
        match = DEF_CLUSTER_RE.search(text)
        if match:
            return f"Def.{match.group(1)}"
    return None


def _guidepost_flags(body: str) -> tuple[bool, bool, bool, bool]:
    has_o, has_m, has_c = guidepost_complete(body)
    if LETTER_O_RE.search(body):
        has_o = True
    if LETTER_M_RE.search(body):
        has_m = True
    if LETTER_A_RE.search(body) or has_m:
        has_a = True
    else:
        has_a = False
    if LETTER_C_RE.search(body):
        has_c = True
    if has_m:
        has_a = True
    return has_o, has_m, has_a, has_c


def collect_ch5_entries(root: Path) -> list[Ch5Entry]:
    """Index Chapter Five definitions with O/M/A/C guidepost bodies."""
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
            owner = str(member_entries[0]["cluster"]) if member_entries else ""
            has_o, has_m, has_a, has_c = _guidepost_flags(body)
            entries.append(
                Ch5Entry(
                    term=label,
                    source_file=file_name,
                    anchor=f"#{anchor}",
                    line_start=idx + 1,
                    line_end=_body_end(lines, idx, depth),
                    category=_category_for(lines, idx, depth, file_name),
                    cluster_membership=member_entries[0] if member_entries else None,
                    cluster_id=_def_cluster_id(owner, label, body),
                    has_o=has_o,
                    has_m=has_m,
                    has_a=has_a,
                    has_c=has_c,
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
    process_path = root / CJS3_PROCESS_HOME
    if process_path.is_file():
        extra = process_path.read_text(encoding="utf-8")
        for cluster in clusters:
            if cluster.cluster_id != "CJS-3.3":
                continue
            cluster.body = f"{cluster.body}\n\n{extra}"
            cluster.ch5_links = sorted(set(cluster.ch5_links + _extract_ch5_links(extra)))
            extra_read = _extract_read_with(extra)
            if extra_read:
                cluster.read_with = list(dict.fromkeys([*cluster.read_with, *extra_read]))
            process_cluster = Cjs3Cluster(
                cluster_id="CJS-3.3",
                title=cluster.title,
                file=CJS3_PROCESS_HOME,
                start_line=1,
                end_line=len(extra.splitlines()),
                body=extra,
            )
            cluster.rules.extend(_extract_rules(process_cluster))
            break
    return clusters


def collect_ch1_principles(root: Path) -> list[PrincipleRecord]:
    """Index Preamble and Chapter One operative headings with D/A/C widget terms."""
    principles: list[PrincipleRecord] = []
    for rel in CH01_FILES:
        path = root / rel
        if not path.is_file():
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        starts: list[tuple[int, str, str]] = []
        for idx, line in enumerate(lines):
            match = PRINCIPLE_HEADING_RE.match(line.strip())
            if match:
                starts.append((idx, match.group(2), match.group(3).strip()))
        for pos, (start_idx, section, title) in enumerate(starts):
            end_idx = starts[pos + 1][0] if pos + 1 < len(starts) else len(lines)
            body = "\n".join(lines[start_idx + 1 : end_idx])
            if rel == "core_00_preamble.md":
                section = f"Preamble §{section}"
            principles.append(
                PrincipleRecord(
                    section=section,
                    title=title,
                    file=rel,
                    line=start_idx + 1,
                    body=body,
                    dac_terms=[match.group(1).strip() for match in DAC_WIDGET_RE.finditer(body)],
                )
            )
    return principles


def extract_ch5_term_cites(text: str) -> list[str]:
    skip = {"O", "M", "A", "C", "E"}
    return sorted(
        {
            label
            for match in CH5_TERM_LINK_RE.finditer(text)
            if (label := match.group(1).strip()) not in skip
        }
    )


def extract_odef_cites(text: str) -> list[str]:
    cites = {f"CJS-3.{number}" for number in ODEF_CITE_RE.findall(text)}
    cites.update(CJS3_FILE_LINK_RE.findall(text))
    return sorted(cites)


def ch5_term_lookup(entries: list[Ch5Entry]) -> dict[str, Ch5Entry]:
    """Case-insensitive lookup; prefers exact label match."""
    lookup: dict[str, Ch5Entry] = {}
    for entry in entries:
        lookup[entry.term.casefold()] = entry
    return lookup


# Tetrad leg heads live in apex files as letter-form O/M/A/C without #### titles,
# so collect_ch5_entries does not index them. Surface them for creep / anti-redefinition checks.
TETRAD_APEX_HEADS: tuple[tuple[str, str, str], ...] = (
    ("Participation", "core_05_apex_participation_leg.md", "#participation-constitutional"),
    ("Oversight", "core_05_apex_oversight_leg.md", "#oversight-constitutional"),
    ("Accountability", "core_05_apex_accountability_leg.md", "#accountability"),
    ("Timeliness", "core_05_apex_timeliness_leg.md", "#timeliness-constitutional"),
)
AIM_APEX_HEADS: tuple[tuple[str, str, str], ...] = (
    ("Flourishing", "core_05_apex_flourishing_aim.md", "#flourishing-constitutional"),
    ("Continuity", "core_05_apex_continuity_aim.md", "#continuity-aim-constitutional"),
    ("Continuity (Constitutional Aim)", "core_05_apex_continuity_aim.md", "#continuity-aim-constitutional"),
)


def _synthetic_apex_entry(term: str, source_file: str, anchor: str, category: str) -> Ch5Entry:
    return Ch5Entry(
        term=term,
        source_file=source_file,
        anchor=anchor,
        line_start=1,
        line_end=1,
        category=category,
        has_o=True,
        has_m=True,
        has_a=True,
        has_c=True,
    )


def tetrad_apex_term_lookup() -> dict[str, Ch5Entry]:
    """Synthetic Ch5Entry map for Constitutional Tetrad apex leg heads."""
    lookup: dict[str, Ch5Entry] = {}
    for term, source_file, anchor in TETRAD_APEX_HEADS:
        lookup[term.casefold()] = _synthetic_apex_entry(term, source_file, anchor, "tetrad_apex")
    return lookup


def apex_term_lookup() -> dict[str, Ch5Entry]:
    """Synthetic map for Tetrad legs and Two Constitutional Aims."""
    lookup = tetrad_apex_term_lookup()
    for term, source_file, anchor in AIM_APEX_HEADS:
        lookup.setdefault(term.casefold(), _synthetic_apex_entry(term, source_file, anchor, "apex"))
    return lookup


def collect_ch5_entries_with_apex(root: Path) -> list[Ch5Entry]:
    """Chapter Five leaves plus synthetic apex heads used as D/A/C targets."""
    entries = list(collect_ch5_entries(root))
    seen = {entry.term.casefold() for entry in entries}
    for entry in apex_term_lookup().values():
        if entry.term.casefold() not in seen:
            entries.append(entry)
            seen.add(entry.term.casefold())
    return sorted(entries, key=lambda item: item.term.casefold())


def ch5_term_lookup_with_tetrad_apex(entries: list[Ch5Entry]) -> dict[str, Ch5Entry]:
    """Chapter Five leaf lookup plus Tetrad apex leg heads (Participation, Oversight, …)."""
    lookup = ch5_term_lookup(entries)
    for key, entry in tetrad_apex_term_lookup().items():
        lookup.setdefault(key, entry)
    return lookup


def normalize_term_label(label: str) -> str:
    return re.sub(r"\s+", " ", label.strip()).casefold()
