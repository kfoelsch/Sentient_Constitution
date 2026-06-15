"""Parse CJS-2.1 topic router rows and locate implementation sections."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

ROUTER_PATH = Path("corpus_joint_structure/cjs_02_implementation_integration_map.md")
CORPUS_FOLDERS = ("corpus_forum", "corpus_institutions", "corpus_joint_structure")
SKIP_PARTS = {"archive", ".git", "__pycache__", "node_modules", "evidence"}

ROW_RE = re.compile(
    r"^\|\s+\*\*(CJS-R[^*]+)\*\*\s+\|\s+([^|]+)\|\s+([^|]+)\|\s+([^|]+)\|",
    re.M,
)
SECTION_ID_RE = re.compile(
    r"^((?:CF|CI|CJS)-[0-9]+(?:\.[0-9]+)?[A-Z]?(?:\.[0-9]+)?)"
)
SECTION_HEADING_RE = re.compile(
    r"^(##|###)\s+((?:CF|CI|CJS)-[0-9]+(?:\.[0-9]+)?[A-Z]?(?:\.[0-9]+)?)[:*\s]",
    re.M,
)
ROUTER_READ_RE = re.compile(r"^\*\*Router read:\*\*.*$", re.M)
RANGE_RE = re.compile(
    r"\*\*(CF|CI|CJS)-([0-9]+)\.([0-9]+)\*\*[–-]\*\*\1-\2\.([0-9]+)\*\*"
)


@dataclass
class RouterRow:
    row_id: str
    topic: str
    owner_cell: str
    read_with_cell: str
    primary_attach: list[str] = field(default_factory=list)
    read_with_attach: list[str] = field(default_factory=list)


def parse_section_id(text: str) -> str | None:
    match = SECTION_ID_RE.match(text.strip())
    return match.group(1) if match else None


def parse_primary_owner_ids(owner_cell: str) -> list[str]:
    range_match = RANGE_RE.search(owner_cell)
    if range_match:
        prefix, major, start, end = range_match.groups()
        return [f"{prefix}-{major}.{index}" for index in range(int(start), int(end) + 1)]
    ids: list[str] = []
    for bold in re.findall(r"\*\*([^*]+)\*\*", owner_cell):
        section_id = parse_section_id(bold)
        if section_id:
            ids.append(section_id)
    if not ids:
        inline = re.search(r"(CJS-[0-9]+(?:\.[0-9]+)?[A-Z]?)", owner_cell)
        if inline:
            ids.append(inline.group(1))
    return ids


def primary_attach_ids(owner_cell: str) -> list[str]:
    owners = parse_primary_owner_ids(owner_cell)
    if not owners:
        return []
    if RANGE_RE.search(owner_cell):
        subsection_parents = {owner.rsplit(".", 1)[0] for owner in owners if "." in owner}
        if len(subsection_parents) == 1 and all("." in owner for owner in owners):
            parent = next(iter(subsection_parents))
            if parent.startswith(("CF-", "CI-")):
                return [parent]
    return owners


def prune_redundant_parents(ids: list[str]) -> list[str]:
    id_set = set(ids)
    return [
        section_id
        for section_id in ids
        if not any(other != section_id and other.startswith(section_id + ".") for other in id_set)
    ]


def extract_syncable_read_with_ids(read_with_cell: str, rows_by_id: dict[str, RouterRow]) -> list[str]:
    ids: list[str] = []
    for row_id in re.findall(r"\*\*(CJS-R[^*]+)\*\*", read_with_cell):
        row = rows_by_id.get(row_id.strip())
        if row:
            ids.extend(primary_attach_ids(row.owner_cell))
    for bold in re.findall(r"\*\*([^*]+)\*\*", read_with_cell):
        section_id = parse_section_id(bold)
        if section_id:
            ids.append(section_id)
    seen: set[str] = set()
    ordered: list[str] = []
    for section_id in ids:
        if section_id not in seen:
            seen.add(section_id)
            ordered.append(section_id)
    return ordered


def load_router_rows(root: Path) -> list[RouterRow]:
    text = (root / ROUTER_PATH).read_text(encoding="utf-8")
    rows: list[RouterRow] = []
    for match in ROW_RE.finditer(text):
        row = RouterRow(
            row_id=match.group(1).strip(),
            topic=re.sub(r"\s+", " ", match.group(2)).strip(),
            owner_cell=match.group(3).strip(),
            read_with_cell=match.group(4).strip(),
        )
        rows.append(row)
    rows_by_id = {row.row_id: row for row in rows}
    for row in rows:
        row.primary_attach = primary_attach_ids(row.owner_cell)
        row.read_with_attach = prune_redundant_parents(
            extract_syncable_read_with_ids(row.read_with_cell, rows_by_id)
        )
    return rows


def build_section_index(root: Path) -> dict[str, Path]:
    index: dict[str, Path] = {}
    for folder in CORPUS_FOLDERS:
        folder_path = root / folder
        if not folder_path.is_dir():
            continue
        for path in folder_path.glob("*.md"):
            text = path.read_text(encoding="utf-8")
            for match in SECTION_HEADING_RE.finditer(text):
                section_id = match.group(2)
                index.setdefault(section_id, path)
    return index


def heading_level_hint(section_id: str) -> str:
    if re.match(r"CJS-\d+[A-Z]\.\d+$", section_id):
        return "##"
    if re.match(r"(?:CF|CI|CJS)-\d+\.\d+", section_id):
        return "###"
    return "##"


def extract_section(text: str, section_id: str) -> str | None:
    cluster_boundary = r"^---\s*\n+\s*##\s+"
    level = heading_level_hint(section_id)
    if level == "##":
        pattern = (
            rf"^##\s+{re.escape(section_id)}[:*\s].*?"
            rf"(?={cluster_boundary}|^##\s+|\Z)"
        )
    else:
        pattern = (
            rf"^(##|###)\s+{re.escape(section_id)}[:*\s].*?"
            rf"(?=^(?:##|###)\s+|\Z)"
        )
    match = re.search(pattern, text, re.M | re.S)
    return match.group(0) if match else None


def short_topic(topic: str, limit: int = 72) -> str:
    topic = re.sub(r"\s+", " ", topic).strip()
    if len(topic) <= limit:
        return topic
    return topic[: limit - 1].rstrip() + "…"


def primary_owner_line(row: RouterRow) -> str:
    if len(row.read_with_attach) <= 8:
        read_with = ", ".join(f"**{item}**" for item in row.read_with_attach)
        suffix = f" Mandatory read-with: {read_with}."
    else:
        suffix = "; see that row for mandatory read-with."
    return (
        f"**Router read:** Primary owner for **{row.row_id}** (*{short_topic(row.topic)}*) "
        f"in **CJS-2.1** (*Topic router (stable IDs)*).{suffix}"
    )


def read_with_line(row: RouterRow) -> str:
    if len(row.primary_attach) == 1:
        owners = f"primary owner **{row.primary_attach[0]}**"
    else:
        owners = "primary owners " + ", ".join(f"**{item}**" for item in row.primary_attach)
    return (
        f"**Router read:** Mandatory read-with for **{row.row_id}** (*{short_topic(row.topic)}*) "
        f"in **CJS-2.1** (*Topic router (stable IDs)*); {owners}."
    )


def section_has_primary_route(section_text: str, row: RouterRow) -> bool:
    if row.row_id not in section_text:
        return False
    lowered = section_text.lower()
    if "**router read:**" in lowered and "primary owner" in lowered and row.row_id in section_text:
        return True
    if "**joint read:**" in lowered and row.row_id in section_text:
        return True
    if "primary owner for" in lowered and row.row_id in section_text:
        return True
    if "for cross-implementation routing" in lowered and row.row_id in section_text:
        return True
    return False


def section_has_read_with_route(section_text: str, row: RouterRow) -> bool:
    if row.row_id not in section_text:
        return False
    if not any(owner in section_text for owner in row.primary_attach):
        return False
    lowered = section_text.lower()
    if "**router read:**" in lowered and "mandatory read-with" in lowered:
        return True
    if "mandatory read-with for" in lowered and row.row_id in section_text:
        return True
    return False
