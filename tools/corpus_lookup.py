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
APPLY_PACK_MAX_SPANS = 12
RETRIEVE_CAP = 8
STATUS = "process_support_not_binding"
HEADING_LINE = re.compile(r"^#{1,6}\s+")
ROUTE_STOP = frozenset(
    {
        "a",
        "an",
        "and",
        "are",
        "as",
        "at",
        "be",
        "by",
        "can",
        "do",
        "does",
        "for",
        "from",
        "how",
        "i",
        "if",
        "in",
        "is",
        "it",
        "me",
        "my",
        "not",
        "of",
        "on",
        "or",
        "our",
        "the",
        "this",
        "that",
        "to",
        "we",
        "what",
        "when",
        "who",
        "with",
        "you",
        "your",
    }
)
# Phrase locators only — never emit these strings as duty text.
ROUTE_DOOR_PHRASES: tuple[tuple[tuple[str, ...], str], ...] = (
    (
        (
            "unlawful instruction",
            "unconstitutional instruction",
            "take responsibility",
        ),
        "unlawful_instruction",
    ),
    (
        (
            "bar challenge",
            "made whole",
            "redress",
            "contest pathway",
            "right to challenge",
        ),
        "contest",
    ),
    (
        ("system alignment", "we're aligned", "we are aligned", "certification"),
        "sac",
    ),
    (
        (
            "standing record",
            "standing effect",
            "two axes",
            "contribution and violation",
        ),
        "standing_record",
    ),
    (("model internals", "hide standing"), "standing_privacy"),
    (
        ("skip notice", "containment", "emergency", "restore-challenge"),
        "emergency",
    ),
    (("hop count", "delay serving", "anti-delay"), "delay"),
    (("form on paper", "paper only", "paper-only", "empty office"), "remedy"),
    (
        ("cannot find", "read the corpus", "specialist-only", "plain challenge"),
        "comprehensibility",
    ),
    (("reconstructable", "drop logs", "hide trails"), "audit"),
    (("bonus", "proxy reward", "deadline"), "incentive"),
    (
        ("ai ethics overlay", "human exemption", "shared stewardship"),
        "shared_stewardship",
    ),
    (("least-restrictive", "privacy restriction"), "least_restrictive_privacy"),
    (("merely unwelcome", "unwelcome instruction"), "unwelcome_instruction"),
    (
        ("two articles collide", "rights collide", "no article names a winner"),
        "rights_floor_ambiguity",
    ),
    (("winner takes", "never binds", "market structure"), "market_structure"),
    (("cross-system", "putting resources back"), "cross_system_contribution"),
)
ROUTE_TOPIC_PHRASES: tuple[tuple[tuple[str, ...], str], ...] = (
    (
        ("anti-self-judging", "anti self judging", "independent review"),
        "CJS-R06",
    ),
    (("emergency adjudication",), "CJS-R11B"),
    (
        ("standing-record custody", "record custody", "opening authority"),
        "CJS-R22",
    ),
    (("remedy parity", "remedy capacity"), "CJS-R20"),
    (("wrong seat", "seat catalog", "which seat"), "CJS-R23"),
    (("specialist chamber", "technical forum"), "CJS-R09"),
    (("contest-integrity", "contest integrity"), "CJS-R15"),
    (("fallback operation",), "CJS-R11A"),
)

RESOLVER_REL = "ai_corpus/indexes/id_resolver.json"
MANIFEST_REL = "ai_corpus/indexes/section_manifest.json"
CROSSREF_REL = "ai_corpus/indexes/section_crossref.json"
STEWARD_REL = "implementation/steward_owner_clock_index.json"
README_REL = "README.md"
CARDS_REL = "implementation/STEWARD_ENTRY_DOORS.md"
CHUNKS_REL = "doc_architecture/generated/boundary_chunks.json"

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

    route = sub.add_parser(
        "route",
        help="Natural-language route to a door, topic, and owners (pointers only).",
    )
    route.add_argument("query", help="Question, fact pattern, ID, or topic.")

    apply_pack = sub.add_parser(
        "apply-pack",
        help="Hydrate owner plus mandatory read-with for a query (source spans, not gloss).",
    )
    apply_pack.add_argument("query", help="Question, fact pattern, ID, or topic.")

    cite = sub.add_parser("cite", help="Format file + anchor + edition; pin validity.")
    cite.add_argument("--file", dest="source_file", required=True)
    cite.add_argument("--anchor", required=True)

    sub.add_parser(
        "classes",
        help="Public next-step classes for steward doors (not the operator gold key).",
    )

    retrieve = sub.add_parser(
        "retrieve",
        help="Rank boundary-chunk locators by token overlap (embeddings postponed indefinitely; never gloss JSON).",
    )
    retrieve.add_argument("query", help="Question or keywords.")
    retrieve.add_argument(
        "--limit",
        type=int,
        default=RETRIEVE_CAP,
        help=f"Max hits (default {RETRIEVE_CAP}).",
    )

    serve = sub.add_parser(
        "serve",
        help="Local HTTP wrapper for lookup commands (127.0.0.1 by default).",
    )
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8765)

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


def tokenize(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[a-z0-9]+", text.casefold())
        if token not in ROUTE_STOP and len(token) > 2
    }


def phrase_hits(query_cf: str, phrases: tuple[str, ...]) -> int:
    return sum(1 for phrase in phrases if phrase in query_cf)


def _door_haystack(case: dict[str, Any]) -> str:
    labels = " ".join(
        str(owner.get("label") or "") for owner in case.get("owners") or []
    )
    return " ".join(
        str(part or "")
        for part in (
            case.get("id"),
            str(case.get("id") or "").replace("_", " "),
            case.get("card_title"),
            case.get("card_anchor"),
            case.get("fact_pattern"),
            case.get("next_step_class"),
            labels,
        )
    )


def _topic_haystack(row: dict[str, Any]) -> str:
    owner_ids = " ".join(
        str(owner.get("id") or "") for owner in row.get("primary_owners") or []
    )
    return " ".join(
        str(part or "")
        for part in (
            row.get("id"),
            row.get("topic"),
            row.get("domain"),
            owner_ids,
        )
    )


def score_text(query: str, haystack: str) -> int:
    q_tokens = tokenize(query)
    h_tokens = tokenize(haystack)
    return len(q_tokens & h_tokens)


def best_door(indexes: Indexes, query: str) -> dict[str, Any] | None:
    query_cf = query.casefold()
    best: dict[str, Any] | None = None
    best_score = 0
    for case in indexes.steward.get("cases", []):
        ident = str(case.get("id") or "")
        score = score_text(query, _door_haystack(case))
        if query_cf == ident or query_cf == ident.replace("_", " "):
            score += 50
        if query_cf == str(case.get("card_anchor") or "").casefold():
            score += 40
        for phrases, door_id in ROUTE_DOOR_PHRASES:
            if ident == door_id:
                score += 8 * phrase_hits(query_cf, phrases)
        if score > best_score or (
            score == best_score
            and score > 0
            and case.get("high_pressure")
            and not (best or {}).get("high_pressure")
        ):
            best_score = score
            best = case
    if best is None or best_score < 2:
        return None
    pointer = door_pointer(best)
    for key in DOOR_SKIP:
        pointer.pop(key, None)
    return pointer


def best_topic(indexes: Indexes, query: str) -> dict[str, Any] | None:
    query_cf = query.casefold()
    best_row: dict[str, Any] | None = None
    best_score = 0
    for row in indexes.resolver.get("topics", []):
        ident = str(row.get("id") or "")
        score = score_text(query, _topic_haystack(row))
        if query_cf == ident.casefold() or query_cf == str(row.get("topic") or "").casefold():
            score += 50
        for phrases, topic_id in ROUTE_TOPIC_PHRASES:
            if ident == topic_id:
                score += 8 * phrase_hits(query_cf, phrases)
        if score > best_score:
            best_score = score
            best_row = row
    if best_row is None or best_score < 2:
        return None
    return topic_pointers(best_row)


def citation_from_pointer(
    indexes: Indexes, pointer: dict[str, Any] | None
) -> dict[str, Any] | None:
    if not pointer:
        return None
    file_rel = pointer.get("file")
    anchor = normalize_anchor(pointer.get("anchor"))
    if not file_rel and pointer.get("href"):
        file_rel, _, frag = str(pointer["href"]).partition("#")
        anchor = normalize_anchor(frag)
    if not file_rel:
        return None
    out: dict[str, Any] = {
        "file": file_rel,
        "edition": indexes.edition,
    }
    if anchor:
        out["anchor"] = anchor
    return out


def cmd_route(indexes: Indexes, query: str) -> dict[str, Any]:
    if not query or not query.strip():
        raise LookupError_("route requires QUERY")
    exact: dict[str, Any] | None = None
    try:
        exact = cmd_resolve(indexes, query, None)
    except LookupError_:
        exact = None

    door = best_door(indexes, query)
    topic: dict[str, Any] | None = None
    if exact and exact.get("primary_owners") is not None:
        topic = exact
    else:
        topic = best_topic(indexes, query)

    owners: list[dict[str, Any]] = []
    read_with: list[dict[str, Any]] = []
    citation = None
    if topic:
        owners = list(topic.get("primary_owners") or [])
        read_with = list(topic.get("read_with") or [])
        if owners:
            citation = citation_from_pointer(indexes, owners[0])
    elif door:
        owners = list(door.get("owners") or [])
        href = (door.get("operative_box") or {}).get("href")
        if href:
            file_rel, _, frag = str(href).partition("#")
            citation = citation_from_pointer(
                indexes, {"file": file_rel, "anchor": frag, "href": href}
            )
        elif owners:
            first = owners[0]
            href = first.get("href")
            if href:
                file_rel, _, frag = str(href).partition("#")
                citation = citation_from_pointer(
                    indexes, {"file": file_rel, "anchor": frag, "href": href}
                )
    elif exact:
        citation = citation_from_pointer(indexes, exact)

    if exact is None and door is None and topic is None:
        raise LookupError_(
            f"no route for {query!r}; try resolve QUERY or door CASE_ID"
        )

    out: dict[str, Any] = {
        "query": query,
        "kind": "exact" if exact is not None else "natural_language",
        "door": door,
        "topic": topic,
        "owners": owners,
        "read_with": read_with,
        "citation": citation,
    }
    if exact is not None:
        out["exact"] = exact
    return out


def span_from_href(
    indexes: Indexes, href: str
) -> tuple[str, int, int, str | None]:
    file_rel, _, frag = href.partition("#")
    file_rel = file_rel.strip()
    anchor = normalize_anchor(frag) if frag else None
    ident = (anchor or "").lstrip("#")
    if ident:
        path = indexes.root / file_rel
        if not path.is_file():
            raise LookupError_(f"missing source file: {file_rel}")
        lines = path.read_text(encoding="utf-8").splitlines()
        needle = f'<a id="{ident}"'
        for idx, line in enumerate(lines, start=1):
            if needle in line:
                start = idx
                end = idx
                for j in range(idx + 1, min(len(lines), idx + 39) + 1):
                    if HEADING_LINE.match(lines[j - 1]):
                        break
                    end = j
                return file_rel, start, end, anchor
    files = indexes.manifest.get("files", {})
    info = files.get(file_rel)
    if not info:
        raise LookupError_(f"no section_manifest entry for {file_rel}")
    section = tightest_section(
        info.get("sections", []),
        heading=None,
        anchor=anchor,
        line=None,
    )
    if section is None:
        raise LookupError_(f"no section for {href}")
    return (
        file_rel,
        section["line_start"],
        section["line_end"],
        section.get("anchor") or anchor,
    )


def hydrate_one(
    indexes: Indexes,
    *,
    ident: str | None = None,
    href: str | None = None,
    role: str,
) -> dict[str, Any]:
    item: dict[str, Any] = {"role": role}
    try:
        if ident:
            item["id"] = ident
            result = cmd_hydrate(indexes, ident, None, None, None)
        elif href:
            item["href"] = href
            file_rel, start, end, anchor = span_from_href(indexes, href)
            result = cmd_hydrate(indexes, None, file_rel, start, end)
            if anchor:
                result["anchor"] = normalize_anchor(anchor)
        else:
            raise LookupError_("hydrate target missing id or href")
        item["hydrated"] = True
        item["file"] = result["file"]
        item["line_start"] = result["line_start"]
        item["line_end"] = result["line_end"]
        item["text"] = result["text"]
        if result.get("anchor"):
            item["anchor"] = result["anchor"]
        item["citation"] = {
            "file": result["file"],
            "anchor": result.get("anchor"),
            "edition": indexes.edition,
        }
    except LookupError_ as exc:
        item["hydrated"] = False
        item["error"] = str(exc)
    return item


def cmd_apply_pack(indexes: Indexes, query: str) -> dict[str, Any]:
    routed = cmd_route(indexes, query)
    targets: list[tuple[str, str | None, str | None]] = []
    seen: set[str] = set()

    def add(role: str, ident: str | None = None, href: str | None = None) -> None:
        key = ident or href or ""
        if not key or key in seen:
            return
        seen.add(key)
        targets.append((role, ident, href))

    exact = routed.get("exact") or {}
    if exact.get("term"):
        add("exact", ident=str(exact["term"]))
    elif exact.get("id") and "primary_owners" not in exact and exact.get("kind") != "prefix":
        add("exact", ident=str(exact["id"]))

    topic = routed.get("topic") or {}
    for owner in topic.get("primary_owners") or []:
        if owner.get("id"):
            add("primary_owner", ident=str(owner["id"]))
    for item in topic.get("read_with") or []:
        if item.get("id"):
            add("read_with", ident=str(item["id"]))

    door = routed.get("door") or {}
    href = (door.get("operative_box") or {}).get("href")
    if href:
        add("operative_box", href=str(href))

    if not targets and routed.get("citation"):
        citation = routed["citation"]
        file_rel = citation.get("file")
        anchor = citation.get("anchor") or ""
        if file_rel:
            add("citation", href=f"{file_rel}{anchor}")

    truncated = len(targets) > APPLY_PACK_MAX_SPANS
    spans = []
    for role, ident, href in targets[:APPLY_PACK_MAX_SPANS]:
        spans.append(hydrate_one(indexes, ident=ident, href=href, role=role))

    return {
        "query": query,
        "route": routed,
        "spans": spans,
        "span_count": len(spans),
        "truncated": truncated,
        "citation": routed.get("citation"),
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


def cmd_cite(indexes: Indexes, source_file: str, anchor: str) -> dict[str, Any]:
    validity = cmd_validity(indexes, source_file, anchor)
    wanted = normalize_anchor(anchor)
    return {
        "file": source_file,
        "anchor": wanted,
        "edition": indexes.edition,
        "effective_date": indexes.effective_date,
        "validity": validity["status"],
        "citation": f"{source_file}{wanted} ({indexes.edition})",
    }


def cmd_classes(indexes: Indexes) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for case in indexes.steward.get("cases", []):
        rows.append(
            {
                "id": case.get("id"),
                "card_title": case.get("card_title"),
                "card_anchor": case.get("card_anchor"),
                "next_step_class": case.get("next_step_class"),
                "high_pressure": bool(case.get("high_pressure")),
                "card_path": f"{CARDS_REL}#{case.get('card_anchor')}"
                if case.get("card_anchor")
                else CARDS_REL,
            }
        )
    return {
        "not_operator_gold_key": True,
        "classes": rows,
    }


def cmd_retrieve(indexes: Indexes, query: str, limit: int | None = None) -> dict[str, Any]:
    if not query or not query.strip():
        raise LookupError_("retrieve requires QUERY")
    cap = RETRIEVE_CAP if limit is None else max(1, min(int(limit), 30))
    path = indexes.root / CHUNKS_REL
    if not path.is_file():
        raise LookupError_(f"missing {CHUNKS_REL}; run `make boundary-chunks`")
    payload = load_json(path)
    wanted = tokenize(query)
    if not wanted:
        raise LookupError_("retrieve query had no usable tokens")
    file_lines: dict[str, list[str]] = {}
    heading_weight = 3
    scored: list[tuple[int, dict[str, Any]]] = []
    for chunk in payload.get("chunks") or []:
        heading_hay = tokenize(
            " ".join(
                str(part or "")
                for part in (
                    chunk.get("heading"),
                    chunk.get("file"),
                    chunk.get("anchor"),
                )
            )
        )
        rel = str(chunk.get("file") or "")
        start = int(chunk.get("line_start") or 0)
        end = int(chunk.get("line_end") or 0)
        if rel not in file_lines:
            path = indexes.root / rel
            file_lines[rel] = (
                path.read_text(encoding="utf-8").splitlines() if path.is_file() else []
            )
        body = ""
        if start > 0 and end >= start:
            body = "\n".join(file_lines[rel][start - 1 : end])
        body_hay = tokenize(body)
        score = (len(wanted & heading_hay) * heading_weight) + len(wanted & body_hay)
        if score:
            scored.append((score, chunk))
    scored.sort(key=lambda item: (-item[0], item[1].get("file") or "", item[1].get("line_start") or 0))
    hits = []
    for score, chunk in scored[:cap]:
        hits.append(
            {
                "file": chunk.get("file"),
                "heading": chunk.get("heading"),
                "anchor": chunk.get("anchor"),
                "line_start": chunk.get("line_start"),
                "line_end": chunk.get("line_end"),
                "score": score,
            }
        )
    return {
        "query": query,
        "not_embeddings": True,
        "embeddings": "postponed_indefinitely",
        "embed_over": "boundary_chunks.json locators and source spans — never gloss JSON",
        "hydrate_next": "python3 tools/corpus_lookup.py hydrate --file FILE --start N --end M",
        "hit_count": len(hits),
        "hits": hits,
    }


def handle_http_command(
    indexes: Indexes, command: str, params: dict[str, Any]
) -> dict[str, Any]:
    """Dispatch one lookup command from an HTTP adapter (same invariants as CLI)."""
    if command == "edition":
        return cmd_edition(indexes)
    if command == "resolve":
        return cmd_resolve(indexes, params.get("query"), params.get("prefix"))
    if command == "hydrate":
        return cmd_hydrate(
            indexes,
            params.get("query"),
            params.get("file") or params.get("source_file"),
            _optional_int(params.get("start")),
            _optional_int(params.get("end")),
        )
    if command == "topic-route":
        return cmd_topic_route(indexes, str(params.get("query") or ""))
    if command == "door":
        return cmd_door(
            indexes,
            params.get("query"),
            bool(params.get("high_pressure")),
        )
    if command == "citator":
        return cmd_citator(
            indexes,
            str(params.get("file") or params.get("source_file") or ""),
            params.get("anchor"),
        )
    if command == "validity":
        return cmd_validity(
            indexes,
            str(params.get("file") or params.get("source_file") or ""),
            str(params.get("anchor") or ""),
        )
    if command == "route":
        return cmd_route(indexes, str(params.get("query") or ""))
    if command == "apply-pack":
        return cmd_apply_pack(indexes, str(params.get("query") or ""))
    if command == "cite":
        return cmd_cite(
            indexes,
            str(params.get("file") or params.get("source_file") or ""),
            str(params.get("anchor") or ""),
        )
    if command == "classes":
        return cmd_classes(indexes)
    if command == "retrieve":
        return cmd_retrieve(
            indexes,
            str(params.get("query") or ""),
            _optional_int(params.get("limit")),
        )
    raise LookupError_(f"unknown command: {command}")


def _optional_int(value: Any) -> int | None:
    if value is None or value == "":
        return None
    return int(value)


def cmd_serve(indexes: Indexes, host: str, port: int) -> int:
    from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
    from urllib.parse import parse_qs, urlparse

    allowed = {
        "edition",
        "resolve",
        "hydrate",
        "topic-route",
        "door",
        "citator",
        "validity",
        "route",
        "apply-pack",
        "cite",
        "classes",
        "retrieve",
    }

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt: str, *args: Any) -> None:
            sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

        def _send(self, code: int, payload: dict[str, Any]) -> None:
            body = json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8")
            self.send_response(code)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self) -> None:  # noqa: N802
            parsed = urlparse(self.path)
            if parsed.path in {"/", "/health"}:
                self._send(
                    200,
                    envelope(
                        indexes,
                        "health",
                        result={"ok": True, "commands": sorted(allowed)},
                    ),
                )
                return
            if not parsed.path.startswith("/v1/"):
                self._send(404, envelope(indexes, "http", error="not found"))
                return
            command = parsed.path[len("/v1/") :].strip("/")
            params = {key: values[-1] for key, values in parse_qs(parsed.query).items()}
            self._dispatch(command, params)

        def do_POST(self) -> None:  # noqa: N802
            parsed = urlparse(self.path)
            if not parsed.path.startswith("/v1/"):
                self._send(404, envelope(indexes, "http", error="not found"))
                return
            command = parsed.path[len("/v1/") :].strip("/")
            length = int(self.headers.get("Content-Length") or "0")
            raw = self.rfile.read(length) if length else b"{}"
            try:
                params = json.loads(raw.decode("utf-8") or "{}")
            except json.JSONDecodeError:
                self._send(400, envelope(indexes, command, error="invalid JSON"))
                return
            if not isinstance(params, dict):
                self._send(400, envelope(indexes, command, error="JSON object required"))
                return
            self._dispatch(command, params)

        def _dispatch(self, command: str, params: dict[str, Any]) -> None:
            if command not in allowed:
                self._send(404, envelope(indexes, command, error="unknown command"))
                return
            try:
                result = handle_http_command(indexes, command, params)
            except LookupError_ as exc:
                self._send(404, envelope(indexes, command, error=str(exc)))
                return
            except Exception as exc:  # noqa: BLE001
                self._send(400, envelope(indexes, command, error=str(exc)))
                return
            self._send(200, envelope(indexes, command, result=result))

    server = ThreadingHTTPServer((host, port), Handler)
    sys.stderr.write(
        f"corpus_lookup HTTP on http://{host}:{port}/v1/{{command}} (Ctrl-C to stop)\n"
    )
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.stderr.write("\n")
    finally:
        server.server_close()
    return 0


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
    if command == "route":
        return cmd_route(indexes, args.query)
    if command == "apply-pack":
        return cmd_apply_pack(indexes, args.query)
    if command == "cite":
        return cmd_cite(indexes, args.source_file, args.anchor)
    if command == "classes":
        return cmd_classes(indexes)
    if command == "retrieve":
        return cmd_retrieve(indexes, args.query, args.limit)
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
    if args.command == "serve":
        return cmd_serve(indexes, args.host, args.port)
    try:
        result = dispatch(indexes, args)
    except LookupError_ as exc:
        emit(envelope(indexes, args.command, error=str(exc)))
        return 1
    emit(envelope(indexes, args.command, result=result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
