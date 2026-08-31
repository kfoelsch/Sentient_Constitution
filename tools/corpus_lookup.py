#!/usr/bin/env python3
"""Deterministic corpus lookup primitives.

Process support only. Locators point; source text binds. Indexes cannot
narrow core meaning. This tool never emits locator gloss.

Read existing generated indexes; do not regenerate them here.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

HYDRATE_CAP = 250
CITATOR_CAP = 30
PREFIX_CAP = 50
STATUS = "process_support_not_binding"

RESOLVER_REL = "ai_corpus/indexes/id_resolver.json"
MANIFEST_REL = "ai_corpus/indexes/section_manifest.json"
CROSSREF_REL = "ai_corpus/indexes/section_crossref.json"
STEWARD_REL = "implementation/steward_owner_clock_index.json"
README_REL = "README.md"
CARDS_REL = "implementation/STEWARD_ENTRY_DOORS.md"

EDITION_RE = re.compile(r"\*\*Corpus edition\*\*\s*\|\s*`([^`]+)`")
EFFECTIVE_RE = re.compile(r"\*\*Effective date\*\*\s*\|\s*([0-9]{4}-[0-9]{2}-[0-9]{2})")

DOOR_SKIP = frozenset(
    {
        "conflict_rule",
        "forbidden_move",
        "fact_pattern",
        "clock_note",
        "eval_scenario_ids",
    }
)


class LookupError_(Exception):
    """User-facing lookup failure (unknown id, span too large, etc.)."""


class EditionMismatch(Exception):
    """README edition and steward-index pin disagree."""


@dataclass
class Indexes:
    root: Path
    edition: str
    effective_date: str
    resolver: dict[str, Any]
    manifest: dict[str, Any]
    crossref: dict[str, Any]
    steward: dict[str, Any]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("edition", help="Pin corpus edition and effective date.")

    resolve = sub.add_parser("resolve", help="Resolve an ID, term, or topic to a pointer.")
    resolve.add_argument("query", nargs="?", help="Exact ID, definition term, or topic id.")
    resolve.add_argument(
        "--prefix",
        help="List IDs with this prefix (pointers only; not hydrated text).",
    )

    hydrate = sub.add_parser("hydrate", help="Read authentic source lines.")
    hydrate.add_argument("query", nargs="?", help="ID or definition term.")
    hydrate.add_argument("--file", dest="source_file", help="Source file relative to root.")
    hydrate.add_argument("--start", type=int, help="1-based start line.")
    hydrate.add_argument("--end", type=int, help="1-based end line (inclusive).")

    topic = sub.add_parser("topic-route", help="Primary owners and mandatory read-with.")
    topic.add_argument("query", help="Topic id (CJS-R09) or topic string.")

    door = sub.add_parser("door", help="Steward-door pointers (not duties).")
    door.add_argument("query", nargs="?", help="Case id (e.g. standing_record).")
    door.add_argument(
        "--high-pressure",
        action="store_true",
        help="List high-pressure case pointers.",
    )

    citator = sub.add_parser("citator", help="Section-to-section edges, capped.")
    citator.add_argument("--file", dest="source_file", required=True)
    citator.add_argument("--anchor", help="Optional fragment, with or without #.")

    validity = sub.add_parser("validity", help="Current vs fossil fragment at this edition.")
    validity.add_argument("--file", dest="source_file", required=True)
    validity.add_argument("--anchor", required=True)

    return parser.parse_args(argv)


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_edition(root: Path) -> tuple[str, str]:
    text = (root / README_REL).read_text(encoding="utf-8")
    edition_match = EDITION_RE.search(text)
    effective_match = EFFECTIVE_RE.search(text)
    if not edition_match or not effective_match:
        raise EditionMismatch("README.md is missing Corpus edition or Effective date.")
    return edition_match.group(1), effective_match.group(1)


def load_indexes(root: Path) -> Indexes:
    edition, effective = read_edition(root)
    steward = load_json(root / STEWARD_REL)
    pinned = steward.get("pinned_to_edition")
    if pinned != edition:
        raise EditionMismatch(
            f"README edition {edition!r} disagrees with steward pin {pinned!r}."
        )
    steward_effective = steward.get("edition_effective")
    if steward_effective and steward_effective != effective:
        raise EditionMismatch(
            f"README effective date {effective!r} disagrees with "
            f"steward edition_effective {steward_effective!r}."
        )
    return Indexes(
        root=root,
        edition=edition,
        effective_date=effective,
        resolver=load_json(root / RESOLVER_REL),
        manifest=load_json(root / MANIFEST_REL),
        crossref=load_json(root / CROSSREF_REL),
        steward=steward,
    )


def envelope(
    indexes: Indexes,
    command: str,
    *,
    result: Any | None = None,
    error: str | None = None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "status": STATUS,
        "cannot_narrow_core": True,
        "edition": indexes.edition,
        "command": command,
    }
    if error is not None:
        payload["error"] = error
    if result is not None:
        payload["result"] = result
    assert_no_gloss(payload)
    return payload


def assert_no_gloss(value: Any) -> None:
    if isinstance(value, dict):
        if "gloss" in value:
            raise RuntimeError("locator gloss leaked into corpus_lookup output")
        for item in value.values():
            assert_no_gloss(item)
    elif isinstance(value, list):
        for item in value:
            assert_no_gloss(item)


def pointer_from_id(entry: dict[str, Any], ident: str) -> dict[str, Any]:
    out: dict[str, Any] = {
        "id": ident,
        "file": entry["file"],
        "kind": entry.get("kind"),
    }
    if entry.get("anchor"):
        out["anchor"] = entry["anchor"]
    if entry.get("heading"):
        out["heading"] = entry["heading"]
    if entry.get("line") is not None:
        out["line"] = entry["line"]
    return out


def pointer_from_definition(entry: dict[str, Any]) -> dict[str, Any]:
    return {
        "term": entry["term"],
        "file": entry["file"],
        "anchor": entry.get("anchor"),
        "line_start": entry["line_start"],
        "line_end": entry["line_end"],
        "kind": "definition",
    }


def find_definition(indexes: Indexes, query: str) -> dict[str, Any] | None:
    folded = query.casefold()
    for entry in indexes.resolver.get("definitions", []):
        if str(entry.get("term", "")).casefold() == folded:
            return entry
    return None


def find_topic(indexes: Indexes, query: str) -> dict[str, Any] | None:
    folded = query.casefold()
    for row in indexes.resolver.get("topics", []):
        if str(row.get("id", "")).casefold() == folded:
            return row
        if str(row.get("topic", "")).casefold() == folded:
            return row
    return None


def topic_pointers(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": row["id"],
        "topic": row.get("topic"),
        "domain": row.get("domain"),
        "primary_owners": [
            {key: value for key, value in owner.items() if key != "gloss"}
            for owner in row.get("primary_owners", [])
        ],
        "read_with": [
            {key: value for key, value in item.items() if key != "gloss"}
            for item in row.get("read_with", [])
        ],
    }


def cmd_edition(indexes: Indexes) -> dict[str, Any]:
    return {
        "edition": indexes.edition,
        "effective_date": indexes.effective_date,
    }


def cmd_resolve(indexes: Indexes, query: str | None, prefix: str | None) -> dict[str, Any]:
    if prefix:
        ids = indexes.resolver.get("ids", {})
        hits = [
            pointer_from_id(entry, ident)
            for ident, entry in ids.items()
            if ident.startswith(prefix)
        ]
        return {
            "kind": "prefix",
            "prefix": prefix,
            "ids": hits[:PREFIX_CAP],
            "truncated": len(hits) > PREFIX_CAP,
            "match_count": len(hits),
        }
    if not query:
        raise LookupError_("resolve requires QUERY or --prefix")

    ids = indexes.resolver.get("ids", {})
    if query in ids:
        return pointer_from_id(ids[query], query)

    definition = find_definition(indexes, query)
    if definition:
        return pointer_from_definition(definition)

    topic = find_topic(indexes, query)
    if topic:
        return topic_pointers(topic)

    raise LookupError_(f"unknown id, term, or topic: {query}")


def normalize_anchor(anchor: str | None) -> str | None:
    if not anchor:
        return None
    return anchor if anchor.startswith("#") else f"#{anchor}"


def tightest_section(
    sections: list[dict[str, Any]],
    *,
    heading: str | None,
    anchor: str | None,
    line: int | None,
) -> dict[str, Any] | None:
    wanted_anchor = normalize_anchor(anchor)
    heading_hits = [sec for sec in sections if heading and sec.get("header") == heading]
    if heading_hits:
        return min(heading_hits, key=lambda sec: sec["line_end"] - sec["line_start"])
    if wanted_anchor:
        anchor_hits = [
            sec for sec in sections if normalize_anchor(sec.get("anchor")) == wanted_anchor
        ]
        if anchor_hits:
            return min(anchor_hits, key=lambda sec: sec["line_end"] - sec["line_start"])
    if line is None:
        return None
    containing = [
        sec
        for sec in sections
        if sec["line_start"] <= line <= sec["line_end"]
    ]
    if not containing:
        return None
    return min(containing, key=lambda sec: sec["line_end"] - sec["line_start"])


def nearby_definition_terms(
    indexes: Indexes,
    file_rel: str,
    start: int,
    end: int,
) -> list[str]:
    terms: list[str] = []
    for entry in indexes.resolver.get("definitions", []):
        if entry.get("file") != file_rel:
            continue
        if start <= entry["line_start"] <= end:
            terms.append(entry["term"])
        if len(terms) >= 8:
            break
    return terms


def span_for_query(indexes: Indexes, query: str) -> tuple[str, int, int, str | None]:
    definition = find_definition(indexes, query)
    if definition:
        return (
            definition["file"],
            definition["line_start"],
            definition["line_end"],
            definition.get("anchor"),
        )
    ids = indexes.resolver.get("ids", {})
    entry = ids.get(query)
    if not entry:
        raise LookupError_(f"unknown id or term: {query}")
    file_rel = entry["file"]
    files = indexes.manifest.get("files", {})
    info = files.get(file_rel)
    if not info:
        raise LookupError_(f"no section_manifest entry for {file_rel}")
    section = tightest_section(
        info.get("sections", []),
        heading=entry.get("heading"),
        anchor=entry.get("anchor"),
        line=entry.get("line"),
    )
    if section is None:
        line = entry.get("line")
        if not isinstance(line, int):
            raise LookupError_(f"no line range for {query}")
        return file_rel, line, line, entry.get("anchor")
    return (
        file_rel,
        section["line_start"],
        section["line_end"],
        section.get("anchor") or entry.get("anchor"),
    )


def read_span(root: Path, file_rel: str, start: int, end: int) -> str:
    path = root / file_rel
    if not path.is_file():
        raise LookupError_(f"missing source file: {file_rel}")
    lines = path.read_text(encoding="utf-8").splitlines()
    if start < 1 or end < start:
        raise LookupError_(f"invalid line range {start}-{end}")
    if end > len(lines):
        raise LookupError_(f"{file_rel} has {len(lines)} lines; requested through {end}")
    return "\n".join(lines[start - 1 : end])


def cmd_hydrate(
    indexes: Indexes,
    query: str | None,
    source_file: str | None,
    start: int | None,
    end: int | None,
) -> dict[str, Any]:
    ident = None
    if source_file is not None and start is not None and end is not None:
        file_rel, line_start, line_end, anchor = source_file, start, end, None
    elif query:
        ident = query
        file_rel, line_start, line_end, anchor = span_for_query(indexes, query)
    else:
        raise LookupError_("hydrate requires QUERY or --file --start --end")

    span_len = line_end - line_start + 1
    if span_len > HYDRATE_CAP:
        terms = nearby_definition_terms(indexes, file_rel, line_start, line_end)
        hint = (
            f"Span is {span_len} lines (cap {HYDRATE_CAP}). Pass --start/--end "
            "for a smaller range"
        )
        if terms:
            hint += ", or hydrate a definition term: " + ", ".join(terms)
        hint += "."
        raise LookupError_(hint)

    text = read_span(indexes.root, file_rel, line_start, line_end)
    out: dict[str, Any] = {
        "file": file_rel,
        "line_start": line_start,
        "line_end": line_end,
        "text": text,
    }
    if ident:
        out["id"] = ident
    if anchor:
        out["anchor"] = normalize_anchor(anchor)
    return out


def cmd_topic_route(indexes: Indexes, query: str) -> dict[str, Any]:
    row = find_topic(indexes, query)
    if not row:
        raise LookupError_(f"unknown topic: {query}")
    return topic_pointers(row)


def door_pointer(case: dict[str, Any]) -> dict[str, Any]:
    anchor = case.get("card_anchor")
    card_path = CARDS_REL
    if anchor:
        card_path = f"{CARDS_REL}#{anchor}"
    owners = []
    for owner in case.get("owners", []):
        owners.append(
            {
                "label": owner.get("label"),
                "href": owner.get("href"),
            }
        )
    operative = case.get("operative_box") or {}
    return {
        "id": case.get("id"),
        "card_path": card_path,
        "card_anchor": anchor,
        "card_title": case.get("card_title"),
        "next_step_class": case.get("next_step_class"),
        "high_pressure": case.get("high_pressure"),
        "owners": owners,
        "operative_box": {
            "label": operative.get("label"),
            "href": operative.get("href"),
        },
        "clock": case.get("clock"),
        "cards": CARDS_REL,
    }


def cmd_door(
    indexes: Indexes,
    query: str | None,
    high_pressure: bool,
) -> dict[str, Any]:
    cases = indexes.steward.get("cases", [])
    if high_pressure:
        hits = [door_pointer(case) for case in cases if case.get("high_pressure")]
        return {"kind": "high_pressure", "cases": hits}
    if not query:
        raise LookupError_("door requires CASE_ID or --high-pressure")
    for case in cases:
        if case.get("id") == query:
            pointer = door_pointer(case)
            for key in DOOR_SKIP:
                pointer.pop(key, None)
            return pointer
    raise LookupError_(f"unknown steward-door case: {query}")


def cmd_citator(
    indexes: Indexes,
    source_file: str,
    anchor: str | None,
) -> dict[str, Any]:
    wanted = normalize_anchor(anchor) if anchor else None
    outbound: list[dict[str, Any]] = []
    inbound: list[dict[str, Any]] = []
    for edge in indexes.crossref.get("edges", []):
        if (
            edge.get("source_file") == source_file
            and (wanted is None or normalize_anchor(edge.get("source_anchor")) == wanted)
        ):
            outbound.append(
                {
                    "target_file": edge.get("target_file"),
                    "target_anchor": edge.get("target_anchor"),
                    "source_header": edge.get("source_header"),
                    "source_anchor": edge.get("source_anchor"),
                    "count": edge.get("count"),
                }
            )
        if (
            edge.get("target_file") == source_file
            and (wanted is None or normalize_anchor(edge.get("target_anchor")) == wanted)
        ):
            inbound.append(
                {
                    "source_file": edge.get("source_file"),
                    "source_anchor": edge.get("source_anchor"),
                    "source_header": edge.get("source_header"),
                    "target_anchor": edge.get("target_anchor"),
                    "count": edge.get("count"),
                }
            )
    outbound_kept = outbound[:CITATOR_CAP]
    inbound_kept = inbound[:CITATOR_CAP]
    return {
        "file": source_file,
        "anchor": wanted,
        "outbound": outbound_kept,
        "inbound": inbound_kept,
        "outbound_count": len(outbound),
        "inbound_count": len(inbound),
        "truncated": len(outbound) > CITATOR_CAP or len(inbound) > CITATOR_CAP,
    }


def cmd_validity(indexes: Indexes, source_file: str, anchor: str) -> dict[str, Any]:
    wanted = normalize_anchor(anchor)
    assert wanted is not None
    current = False
    fossil = False
    for ident, entry in indexes.resolver.get("ids", {}).items():
        if entry.get("file") != source_file:
            continue
        if normalize_anchor(entry.get("anchor")) == wanted:
            current = True
            break
    for row in indexes.resolver.get("aliases", []):
        if row.get("file") != source_file:
            continue
        fossils = [normalize_anchor(item) for item in row.get("fossil_anchors", [])]
        currents = [normalize_anchor(item) for item in row.get("current_anchors", [])]
        if wanted in fossils:
            fossil = True
        if wanted in currents:
            current = True
    if fossil and not current:
        status = "fossil"
    elif current:
        status = "current"
    else:
        status = "unknown"
    return {
        "file": source_file,
        "anchor": wanted,
        "status": status,
    }


def dispatch(indexes: Indexes, args: argparse.Namespace) -> dict[str, Any]:
    command = args.command
    if command == "edition":
        return cmd_edition(indexes)
    if command == "resolve":
        return cmd_resolve(indexes, args.query, args.prefix)
    if command == "hydrate":
        return cmd_hydrate(
            indexes,
            args.query,
            args.source_file,
            args.start,
            args.end,
        )
    if command == "topic-route":
        return cmd_topic_route(indexes, args.query)
    if command == "door":
        return cmd_door(indexes, args.query, args.high_pressure)
    if command == "citator":
        return cmd_citator(indexes, args.source_file, args.anchor)
    if command == "validity":
        return cmd_validity(indexes, args.source_file, args.anchor)
    raise LookupError_(f"unknown command: {command}")


def emit(payload: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    try:
        indexes = load_indexes(root)
    except EditionMismatch as exc:
        sys.stderr.write(str(exc) + "\n")
        return 2
    except FileNotFoundError as exc:
        sys.stderr.write(f"missing index or source: {exc}\n")
        return 2
    try:
        result = dispatch(indexes, args)
    except LookupError_ as exc:
        emit(envelope(indexes, args.command, error=str(exc)))
        return 1
    emit(envelope(indexes, args.command, result=result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
