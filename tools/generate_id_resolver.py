#!/usr/bin/env python3
"""Generate a compact AI locator: ID / topic / term / alias → file#anchor.

Derived process support. Locators point; they do not restate duties.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from corpus_paths import source_markdown_files  # noqa: E402
from family_map_lib import iter_entries, load_family_map, resolve_section_file  # noqa: E402
from generate_definition_registry import collect_entries, principle_layer_entries  # noqa: E402
from router_table_lib import (  # noqa: E402
    load_router_rows,
    router_domain,
)
from section_label_anchor_audit import (  # noqa: E402
    id_matches_current,
    parse_clusters,
    source_paths,
)

ANCHOR_RE = re.compile(r'<a id="([^"]+)"></a>')
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$")
SECTION_ID_RE = re.compile(
    r"^((?:CF|CI|CJS|CS)-[0-9]+(?:\.[0-9]+)*[A-Z]?|Def\.[OPACI]\d+)\b"
)
GLOSS_FILES = (
    "tools/glosses_cf.json",
    "tools/glosses_cs_cjs.json",
    "tools/glosses_cf_sections.json",
    "tools/glosses_rest_sections.json",
    "tools/section_glosses.json",
)
STEWARD_INDEX = Path("implementation/steward_owner_clock_index.json")
LEXICAL_PATH = Path("tools/architecture/lexical_guardrails.json")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument("--output", required=True, help="Output JSON path.")
    return parser.parse_args()


def slugify(header: str) -> str:
    text = header.lower().strip()
    text = re.sub(r"&", " and ", text)
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")


def load_glosses(root: Path) -> dict[str, str]:
    combined: dict[str, str] = {}
    for rel in GLOSS_FILES:
        path = root / rel
        if not path.is_file():
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            continue
        for key, value in payload.items():
            if isinstance(value, str):
                combined[key] = value
            elif isinstance(value, dict):
                for inner_key, inner in value.items():
                    if isinstance(inner, str):
                        combined[f"{key}#{inner_key}"] = inner
    return combined


def gloss_for(
    glosses: dict[str, str],
    file_rel: str,
    heading: str,
    section_id: str,
    *,
    allow_file_fallback: bool,
) -> str | None:
    candidates = [
        f"{file_rel}#{heading}",
        f"{file_rel}#{section_id}",
    ]
    if allow_file_fallback:
        candidates.extend([file_rel, Path(file_rel).name])
    for key in candidates:
        hit = glosses.get(key)
        if hit:
            return hit
    prefix = f"{file_rel}#"
    for key, value in glosses.items():
        if not key.startswith(prefix):
            continue
        frag = key.split("#", 1)[-1]
        if (
            frag == section_id
            or frag.startswith(section_id + " ")
            or frag.startswith(section_id + ":")
        ):
            return value
    return None


def pick_anchor(pending: list[str], heading: str, section_id: str) -> str:
    if pending:
        slug = slugify(heading)
        for candidate in pending:
            if candidate == slug or candidate == section_id.lower().replace(".", ""):
                return f"#{candidate}"
        compact = section_id.lower().replace(".", "").replace("def.", "def")
        for candidate in pending:
            if candidate.replace("-", "").startswith(compact):
                return f"#{candidate}"
        return f"#{pending[-1]}"
    return f"#{slugify(heading)}"


def scan_section_ids(root: Path) -> dict[str, dict[str, Any]]:
    found: dict[str, dict[str, Any]] = {}
    for path in source_markdown_files(root):
        rel = path.relative_to(root).as_posix()
        lines = path.read_text(encoding="utf-8").splitlines()
        pending: list[str] = []
        for idx, line in enumerate(lines, start=1):
            stripped = line.strip()
            anchor = ANCHOR_RE.match(stripped)
            if anchor:
                pending.append(anchor.group(1))
                continue
            heading = HEADING_RE.match(stripped)
            if not heading:
                if stripped:
                    pending = []
                continue
            title = heading.group(2).strip()
            match = SECTION_ID_RE.match(title)
            if match:
                section_id = match.group(1)
                if section_id not in found:
                    found[section_id] = {
                        "file": rel,
                        "heading": title,
                        "anchor": pick_anchor(pending, title, section_id),
                        "line": idx,
                    }
            pending = []
    return found


def family_kind(section_id: str) -> str:
    if section_id.startswith("Def."):
        return "cluster"
    if re.match(r"^(?:CF|CI|CJS|CS)-\d+$", section_id) or section_id in {
        "CJS-0",
        "CJS-0.1",
    }:
        return "family"
    return "section"


def build_ids(root: Path, glosses: dict[str, str]) -> dict[str, dict[str, Any]]:
    scanned = scan_section_ids(root)
    family_map = load_family_map(root)
    ids: dict[str, dict[str, Any]] = {}
    for section_id, info in scanned.items():
        entry: dict[str, Any] = {
            "file": info["file"],
            "anchor": info["anchor"],
            "heading": info["heading"],
            "line": info["line"],
            "kind": family_kind(section_id),
        }
        gloss = gloss_for(
            glosses,
            info["file"],
            info["heading"],
            section_id,
            allow_file_fallback=family_kind(section_id) != "section",
        )
        if gloss:
            entry["gloss"] = gloss
        ids[section_id] = entry
    for raw in iter_entries(family_map):
        raw_id = str(raw.get("id", "")).strip()
        file_rel = raw.get("file")
        if not raw_id or not file_rel or raw.get("status") == "reserved":
            continue
        if raw_id in ids:
            continue
        entry = {
            "file": file_rel,
            "anchor": f"#{raw['anchor']}" if raw.get("anchor") else None,
            "heading": raw.get("label", raw_id),
            "kind": "family",
        }
        gloss = gloss_for(
            glosses,
            file_rel,
            str(raw.get("label", "")),
            raw_id,
            allow_file_fallback=True,
        )
        if gloss:
            entry["gloss"] = gloss
        ids[raw_id] = {key: value for key, value in entry.items() if value is not None}
    return dict(sorted(ids.items(), key=lambda item: item[0]))


def resolve_attach(
    root: Path,
    section_id: str,
    ids: dict[str, dict[str, Any]],
    family_map: dict[str, Any],
) -> dict[str, str]:
    hit = ids.get(section_id)
    if hit:
        out = {"id": section_id, "file": hit["file"]}
        if hit.get("anchor"):
            out["anchor"] = hit["anchor"]
        return out
    file_rel = resolve_section_file(family_map, section_id)
    if file_rel:
        return {"id": section_id, "file": file_rel}
    return {"id": section_id}


def build_topics(
    root: Path,
    ids: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    family_map = load_family_map(root)
    rows = []
    for row in load_router_rows(root):
        rows.append(
            {
                "id": row.row_id,
                "topic": row.topic,
                "domain": router_domain(row),
                "primary_owners": [
                    resolve_attach(root, section_id, ids, family_map)
                    for section_id in row.primary_attach
                ],
                "read_with": [
                    resolve_attach(root, section_id, ids, family_map)
                    for section_id in row.read_with_attach
                ],
            }
        )
    return rows


def build_definitions(root: Path) -> list[dict[str, Any]]:
    entries = []
    for item in sorted(
        collect_entries(root) + principle_layer_entries(root),
        key=lambda entry: entry.term.casefold(),
    ):
        entries.append(
            {
                "term": item.term,
                "file": item.source_file,
                "anchor": item.anchor,
                "line_start": item.line_start,
                "line_end": item.line_end,
            }
        )
    return entries


def build_aliases(root: Path) -> list[dict[str, Any]]:
    aliases: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for path in source_paths(root):
        rel = path.relative_to(root).as_posix()
        clusters = parse_clusters(path.read_text(encoding="utf-8"))
        emitted: set[int] = set()
        for info in clusters.values():
            lineno = info.get("lineno")
            if lineno in emitted:
                continue
            current = info.get("current")
            ids = info.get("ids") or []
            if not current or len(ids) < 2:
                continue
            current_ids = [
                anchor_id
                for anchor_id in ids
                if id_matches_current(anchor_id, current)
            ]
            fossils = [
                anchor_id
                for anchor_id in ids
                if anchor_id not in current_ids
            ]
            if not current_ids or not fossils:
                continue
            key = (rel, current_ids[0])
            if key in seen:
                continue
            seen.add(key)
            emitted.add(lineno)
            aliases.append(
                {
                    "file": rel,
                    "title": info.get("title", ""),
                    "current_number": current,
                    "current_anchors": [f"#{item}" for item in current_ids],
                    "fossil_anchors": [f"#{item}" for item in fossils],
                }
            )
    aliases.sort(key=lambda row: (row["file"], row["current_number"]))
    return aliases


def build_steward_doors(root: Path) -> dict[str, Any]:
    path = root / STEWARD_INDEX
    payload = json.loads(path.read_text(encoding="utf-8"))
    cases = []
    for case in payload.get("cases", []):
        cases.append(
            {
                "id": case.get("id"),
                "card_anchor": case.get("card_anchor"),
                "next_step_class": case.get("next_step_class"),
            }
        )
    return {
        "index": STEWARD_INDEX.as_posix(),
        "cards": "implementation/STEWARD_ENTRY_DOORS.md",
        "case_ids": [case["id"] for case in cases if case.get("id")],
        "cases": cases,
    }


def build_lexical(root: Path) -> dict[str, Any]:
    payload = json.loads((root / LEXICAL_PATH).read_text(encoding="utf-8"))
    return {
        "source": LEXICAL_PATH.as_posix(),
        "avoid_to_prefer": [
            {"avoid": row["avoid"], "prefer": row["prefer"]}
            for row in payload.get("ambiguous_labels", [])
            if isinstance(row, dict) and "avoid" in row and "prefer" in row
        ],
    }


def build_payload(root: Path) -> dict[str, Any]:
    glosses = load_glosses(root)
    ids = build_ids(root, glosses)
    return {
        "$schema": "../schemas/id_resolver.schema.json",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "status": "process_support_not_binding",
        "cannot_narrow_core": True,
        "description": (
            "Derived locator: family/section IDs, CJS-0.1 topics, Chapter Five "
            "terms, and current/fossil anchors. Indexes point; source text binds."
        ),
        "ids": ids,
        "topics": build_topics(root, ids),
        "definitions": build_definitions(root),
        "aliases": build_aliases(root),
        "steward_doors": build_steward_doors(root),
        "lexical": build_lexical(root),
    }


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    output = root / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = build_payload(root)
    output.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(
        f"Wrote id resolver ({len(payload['ids'])} ids, "
        f"{len(payload['topics'])} topics, "
        f"{len(payload['definitions'])} definitions) to {output}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
