#!/usr/bin/env python3
"""Validate AI corpus manifests and optionally check source freshness."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


EXPECTED_OUTPUTS = {
    "section_manifest": "ai_corpus/indexes/section_manifest.json",
    "definition_registry": "ai_corpus/indexes/definition_registry.json",
    "crossref_matrix": "ai_corpus/indexes/crossref_matrix.json",
    "section_crossref": "ai_corpus/indexes/section_crossref.json",
    "id_resolver": "ai_corpus/indexes/id_resolver.json",
}


GENERATORS = {
    "section_manifest": "tools/generate_section_manifest.py",
    "definition_registry": "tools/generate_definition_registry.py",
    "crossref_matrix": "tools/generate_crossref_matrix.py",
    "section_crossref": "tools/generate_section_crossref.py",
    "id_resolver": "tools/generate_id_resolver.py",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument(
        "--check-freshness",
        action="store_true",
        help="Regenerate manifests in a temporary directory and compare source-derived content.",
    )
    return parser.parse_args()


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"Missing manifest: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}") from exc


def without_generation_time(payload: Any) -> Any:
    if isinstance(payload, dict):
        return {
            key: without_generation_time(value)
            for key, value in payload.items()
            if key != "generated_at"
        }
    if isinstance(payload, list):
        return [without_generation_time(value) for value in payload]
    return payload


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def validate_section_manifest(payload: dict[str, Any]) -> None:
    require(isinstance(payload.get("files"), dict), "section_manifest.json must contain a files object")
    for file_name, info in payload["files"].items():
        require(isinstance(info.get("total_lines"), int), f"{file_name}: missing total_lines")
        require(isinstance(info.get("sections"), list), f"{file_name}: missing sections list")
        for section in info["sections"]:
            require(isinstance(section.get("header"), str), f"{file_name}: section missing header")
            require(isinstance(section.get("level"), int), f"{file_name}: section missing level")
            require(isinstance(section.get("line_start"), int), f"{file_name}: section missing line_start")
            require(isinstance(section.get("line_end"), int), f"{file_name}: section missing line_end")
            require(
                1 <= section["line_start"] <= section["line_end"] <= info["total_lines"],
                f"{file_name}: invalid line range for {section.get('header')!r}",
            )


def validate_definition_registry(payload: dict[str, Any]) -> None:
    definitions = payload.get("definitions")
    require(isinstance(definitions, list), "definition_registry.json must contain a definitions list")
    require(payload.get("definition_count") == len(definitions), "definition_count does not match definitions")
    seen_terms: set[str] = set()
    for entry in definitions:
        term = entry.get("term")
        require(isinstance(term, str) and term, "definition entry missing term")
        require(term not in seen_terms, f"duplicate definition term: {term}")
        seen_terms.add(term)
        require(isinstance(entry.get("source_file"), str), f"{term}: missing source_file")
        require(isinstance(entry.get("anchor"), str) and entry["anchor"].startswith("#"), f"{term}: invalid anchor")
        require(isinstance(entry.get("line_start"), int), f"{term}: missing line_start")
        require(isinstance(entry.get("line_end"), int), f"{term}: missing line_end")
        require(entry["line_start"] <= entry["line_end"], f"{term}: invalid line range")
        require(
            entry.get("category")
            in {"independent", "semi_independent", "dependent_cluster", "principle_layer"},
            f"{term}: invalid category",
        )


def validate_section_crossref(payload: dict[str, Any]) -> None:
    edges = payload.get("edges")
    require(isinstance(edges, list), "section_crossref.json must contain edges")
    require(
        payload.get("edge_count") in (None, len(edges)),
        "section_crossref edge_count does not match edges",
    )
    for edge in edges:
        require(isinstance(edge.get("source_file"), str), "section_crossref edge missing source_file")
        require(isinstance(edge.get("target_file"), str), "section_crossref edge missing target_file")
        require(isinstance(edge.get("count"), int) and edge["count"] > 0, "section_crossref invalid count")


def validate_id_resolver(payload: dict[str, Any]) -> None:
    require(payload.get("cannot_narrow_core") is True, "id_resolver must stamp cannot_narrow_core")
    ids = payload.get("ids")
    require(isinstance(ids, dict) and ids, "id_resolver.json must contain ids")
    for section_id, entry in ids.items():
        require(isinstance(entry.get("file"), str), f"{section_id}: missing file")
        require(entry.get("kind") in {"family", "section", "cluster"}, f"{section_id}: invalid kind")
    topics = payload.get("topics")
    require(isinstance(topics, list) and topics, "id_resolver.json must contain topics")
    for row in topics:
        require(isinstance(row.get("id"), str) and row["id"].startswith("CJS-R"), "topic missing CJS-R id")
        require(isinstance(row.get("primary_owners"), list), f"{row.get('id')}: missing primary_owners")
    definitions = payload.get("definitions")
    require(isinstance(definitions, list) and definitions, "id_resolver.json must contain definitions")
    doors = payload.get("steward_doors")
    require(isinstance(doors, dict), "id_resolver.json must contain steward_doors")
    require(isinstance(doors.get("index"), str), "steward_doors missing index pointer")


def validate_crossref_matrix(payload: dict[str, Any]) -> None:
    graph = payload.get("graph")
    require(isinstance(graph, dict), "crossref_matrix.json must contain graph")
    nodes = graph.get("nodes")
    edges = graph.get("edges")
    require(isinstance(nodes, list), "crossref_matrix.json graph must contain nodes")
    require(isinstance(edges, list), "crossref_matrix.json graph must contain edges")
    node_ids = {node.get("id") for node in nodes if isinstance(node, dict)}
    require(all(isinstance(node_id, str) for node_id in node_ids), "crossref nodes must have string ids")
    for edge in edges:
        source = edge.get("source")
        require(source in node_ids, f"crossref edge source not in nodes: {source}")
        targets = edge.get("targets")
        require(isinstance(targets, list), f"{source}: edge missing targets")
        for target in targets:
            target_file = target.get("file")
            require(target_file in node_ids, f"{source}: target not in nodes: {target_file}")
            require(isinstance(target.get("count"), int) and target["count"] > 0, f"{source}: invalid count")
            require(isinstance(target.get("anchors"), list), f"{source}: target anchors must be a list")


def validate_shapes(root: Path) -> None:
    validate_section_manifest(load_json(root / EXPECTED_OUTPUTS["section_manifest"]))
    validate_definition_registry(load_json(root / EXPECTED_OUTPUTS["definition_registry"]))
    validate_crossref_matrix(load_json(root / EXPECTED_OUTPUTS["crossref_matrix"]))
    validate_section_crossref(load_json(root / EXPECTED_OUTPUTS["section_crossref"]))
    validate_id_resolver(load_json(root / EXPECTED_OUTPUTS["id_resolver"]))


def check_freshness(root: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="ai-manifest-") as temp:
        temp_root = Path(temp)
        generated_paths: dict[str, Path] = {}
        for name, script in GENERATORS.items():
            out_path = temp_root / f"{name}.json"
            generated_paths[name] = out_path
            subprocess.run(
                [sys.executable, str(root / script), "--root", str(root), "--output", str(out_path)],
                check=True,
                cwd=root,
            )
        stale: list[str] = []
        for name, expected_rel in EXPECTED_OUTPUTS.items():
            current = without_generation_time(load_json(root / expected_rel))
            generated = without_generation_time(load_json(generated_paths[name]))
            if current != generated:
                stale.append(expected_rel)
        if stale:
            joined = "\n  - ".join(stale)
            raise SystemExit(f"AI corpus manifests are stale:\n  - {joined}\nRun `make ai-corpus-sync`.")


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    validate_shapes(root)
    if args.check_freshness:
        check_freshness(root)
    print("AI corpus manifests are valid and fresh." if args.check_freshness else "AI corpus manifests are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
