"""Parse CJS-2.1 topic router rows and locate implementation sections."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from pathlib import Path

ROUTER_PATH = Path("corpus_joint_structure/cjs_00_registry_and_reading_rules.md")
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
    r"^(#{1,3})\s+((?:CF|CI|CJS)-[0-9]+(?:\.[0-9]+)?[A-Z]?(?:\.[0-9]+)?)[:*\s]",
    re.M,
)
ROUTER_DOMAIN_ORDER = (
    "Forum operations",
    "Institutional governance",
    "Cross-implementation integrity",
)
ROUTER_READ_RE = re.compile(r"^\*\*Router read:\*\*.*$", re.M)
TOPIC_ROUTE_BULLET_RE = re.compile(
    r"^- Topic routing \((?:primary owner|mandatory read-with)\):.*$",
    re.M,
)
TRACE_SUMMARY_MARKER = (
    '<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>'
)
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


def extract_section(text: str, section_id: str) -> str | None:
    """Return the slice of ``text`` owned by ``section_id``.

    The heading may sit at any depth from ``#`` to ``###``; the section runs
    until the next heading of the same or shallower depth, so promoting a file
    to an H1 title does not change which body a section owns.
    """
    heading = re.search(rf"^(#{{1,3}})\s+{re.escape(section_id)}[:*\s]", text, re.M)
    if heading is None:
        return None
    level = len(heading.group(1))
    tail = text[heading.end() :]
    boundary = re.search(
        rf"^---\s*\n+\s*#{{1,{level}}}\s+|^#{{1,{level}}}\s+", tail, re.M
    )
    end = heading.end() + (boundary.start() if boundary else len(tail))
    return text[heading.start() : end]


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
        f"Topic routing (primary owner): **{row.row_id}** (*{short_topic(row.topic)}*) "
        f"in **CJS-2.1** (*Topic router*).{suffix}"
    )


def read_with_line(row: RouterRow) -> str:
    if len(row.primary_attach) == 1:
        owners = f"primary owner **{row.primary_attach[0]}**"
    else:
        owners = "primary owners " + ", ".join(f"**{item}**" for item in row.primary_attach)
    return (
        f"Topic routing (mandatory read-with): **{row.row_id}** (*{short_topic(row.topic)}*) "
        f"in **CJS-2.1** (*Topic router*); {owners}."
    )


def section_title(text: str, section_id: str) -> str | None:
    colon = re.compile(
        rf"^(#{{1,3}})\s+{re.escape(section_id)}:\s+(.+?)\s*$",
        re.M,
    )
    match = colon.search(text)
    if match:
        return match.group(2).strip()
    spaced = re.compile(
        rf"^(#{{1,3}})\s+{re.escape(section_id)}\s+(.+?)\s*$",
        re.M,
    )
    match = spaced.search(text)
    if match:
        return match.group(2).strip()
    return None


def section_markdown_link(
    root: Path,
    section_id: str,
    section_index: dict[str, Path],
    *,
    from_dir: Path | None = None,
) -> str:
    path = section_index.get(section_id)
    if path is None:
        return f"**{section_id}**"
    file_text = path.read_text(encoding="utf-8")
    title = section_title(file_text, section_id) or section_id
    if from_dir is None:
        from_dir = root / ROUTER_PATH.parent
    try:
        rel = Path(os.path.relpath(path, from_dir))
    except ValueError:
        rel = path
    return f"[{section_id} — {title}]({rel.as_posix()})"


def router_domain(row: RouterRow) -> str:
    if row.primary_attach:
        first = row.primary_attach[0]
        if first.startswith("CF-"):
            return "Forum operations"
        if first.startswith("CI-"):
            return "Institutional governance"
    if re.search(r"\bCJS-", row.owner_cell):
        return "Cross-implementation integrity"
    return "Cross-implementation integrity"


def human_primary_owner_links(
    root: Path,
    row: RouterRow,
    section_index: dict[str, Path],
    *,
    from_dir: Path | None = None,
) -> str:
    if not row.primary_attach:
        return row.owner_cell.strip()
    links = [
        section_markdown_link(root, section_id, section_index, from_dir=from_dir)
        for section_id in row.primary_attach
    ]
    return ", ".join(links)


def human_read_with_summary(row: RouterRow, *, limit: int = 4) -> str:
    items = row.read_with_attach[:limit]
    if not items:
        return "see integrator table for the full list"
    summary = ", ".join(f"**{item}**" for item in items)
    if len(row.read_with_attach) > limit:
        summary += ", …"
    return summary


def section_has_primary_route(section_text: str, row: RouterRow) -> bool:
    if row.row_id not in section_text:
        return False
    lowered = section_text.lower()
    if "topic routing (primary owner):" in lowered and row.row_id in section_text:
        return True
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
    if "topic routing (mandatory read-with):" in lowered and row.row_id in section_text:
        return True
    if "**router read:**" in lowered and "mandatory read-with" in lowered:
        return True
    if "mandatory read-with for" in lowered and row.row_id in section_text:
        return True
    return False


def strip_routing_annotations(section_text: str) -> str:
    lines = section_text.splitlines()
    kept: list[str] = []
    for line in lines:
        if ROUTER_READ_RE.match(line):
            continue
        if TOPIC_ROUTE_BULLET_RE.match(line):
            continue
        kept.append(line)
    return "\n".join(kept)


def strip_legacy_router_read_labels(text: str) -> str:
    """Remove legacy **Router read:** body lines without touching topic-routing trace bullets."""
    lines = text.splitlines()
    return "\n".join(line for line in lines if not ROUTER_READ_RE.match(line))


def trace_content_bounds(section_text: str) -> tuple[int, int] | None:
    trace_start = section_text.find(TRACE_SUMMARY_MARKER)
    if trace_start < 0:
        return None
    content_start = section_text.find("\n", trace_start)
    if content_start < 0:
        return None
    content_start += 1
    close = section_text.find("\n</details>", content_start)
    if close < 0:
        return None
    return content_start, close


def apply_topic_routing_to_trace(section_text: str, routing_lines: list[str]) -> str:
    cleaned = strip_routing_annotations(section_text)
    bounds = trace_content_bounds(cleaned)
    if bounds is None:
        if not routing_lines:
            return cleaned
        block = "\n".join(f"- {line}" for line in routing_lines) + "\n\n"
        insert_at = 0
        parts = cleaned.split("</details>", 2)
        if len(parts) >= 3:
            prefix = parts[0] + "</details>" + parts[1] + "</details>"
            tail = parts[2]
            match = re.search(r"\n*<br>\s*\n*", tail)
            insert_at = len(prefix) + (match.end() if match else 0)
        return cleaned[:insert_at] + block + cleaned[insert_at:].lstrip("\n")

    content_start, content_end = bounds
    trace_body = cleaned[content_start:content_end].rstrip("\n")
    if routing_lines:
        bullets = "\n".join(f"- {line}" for line in routing_lines)
        new_trace = f"{trace_body}\n{bullets}\n" if trace_body.strip() else f"{bullets}\n"
    else:
        new_trace = f"{trace_body}\n" if trace_body else ""
    return cleaned[:content_start] + new_trace + cleaned[content_end:]
