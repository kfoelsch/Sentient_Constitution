#!/usr/bin/env python3
"""Integrity checks for the chapter-number registry and crosswalk."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from local_markdown_fragment_audit import anchor_info


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    registry = json.loads((root / "tools/architecture/chapter_numbers.json").read_text())
    crosswalk = json.loads((root / "tools/architecture/chapter_crosswalk.json").read_text())
    rows = registry["chapters"]
    by_source: dict[str, list[dict]] = {}
    for row in rows:
        for key in (row.get("original_file"), row.get("destination_file"), row.get("pre_consolidation_original_file")):
            if key:
                by_source.setdefault(key, []).append(row)
    assert len(rows) == 164
    assert len({row["machine_id"] for row in rows}) == len(rows)
    assert len({row["destination_file"] for row in rows}) == len(rows)
    assert all(row.get("destination_file") for row in rows)
    assert all((root / row["destination_file"]).is_file() for row in rows)

    maps = {row["source_file"]: row for row in crosswalk["anchor_maps"]}
    section_count = 0
    # Section IDs and real heading anchors must be reversible inside their
    # original file boundary. Some manifest entries repeat an identical
    # section row, so compare the unique mapping pairs rather than row count.
    forward_sections: dict[tuple[str, str], str] = {}
    inverse_sections: dict[tuple[str, str], str] = {}
    forward_anchors: dict[tuple[str, str], str] = {}
    inverse_anchors: dict[tuple[str, str], str] = {}
    for section in crosswalk["sections"]:
        source = section["source_file"]
        candidates = by_source.get(source, [])
        if not candidates:
            # Some old implementation files were absorbed into subcores during
            # the later consolidation. Resolve those crosswalk rows through the
            # registry's retained pre-consolidation machine ID or legacy section ID.
            candidates = [row for row in rows if section["machine_id"] in (
                row.get("machine_id"), row.get("pre_reorganization_2026_11_20"),
                row.get("pre_subcore_2026_11_20"), row.get("pre_consolidation_2026_11_24"),
                *(row.get("legacy_section_ids", [])), *(row.get("legacy_chapter_ids", []))
            )]
        if not candidates:
            candidates = [
                row for row in rows
                if any(
                    section["machine_id"].startswith(row.get(key, "") + ".")
                    for key in ("machine_id", "pre_reorganization_2026_11_20", "pre_subcore_2026_11_20")
                    if row.get(key)
                )
            ]
        assert candidates, (source, section["machine_id"])
        section_machine = section["machine_id"]
        def historical_ids(candidate):
            return [candidate.get("machine_id", ""), candidate.get("pre_reorganization_2026_11_20", ""),
                    candidate.get("pre_subcore_2026_11_20", ""), candidate.get("pre_assemblies_2026_11_23", ""),
                    candidate.get("pre_consolidation_display_id", "")]
        def match_score(candidate):
            ids = [value for value in historical_ids(candidate) if value]
            if section_machine in ids:
                return 4
            if any(section_machine.startswith(value + ".") for value in ids):
                return 3
            if any(value.startswith(section_machine + ".") for value in ids):
                return 2
            return 0
        candidates = sorted(candidates, key=match_score, reverse=True)
        row = candidates[0]
        # Old anchors are historical identifiers and can refer to headings
        # revised after the pre-numbering snapshot. Their reversible mapping
        # is checked below; the active destination anchor is checked against
        # the current destination document.
        legacy_key = (source, section["legacy_section_id"])
        machine_key = (source, section["machine_id"])
        old_anchor_key = (source, section["old_anchor"])
        new_anchor_key = (source, section["new_anchor"])
        assert forward_sections.setdefault(legacy_key, section["machine_id"]) == section["machine_id"]
        assert inverse_sections.setdefault(machine_key, section["legacy_section_id"]) == section["legacy_section_id"]
        assert forward_anchors.setdefault(old_anchor_key, section["new_anchor"]) == section["new_anchor"]
        assert inverse_anchors.setdefault(new_anchor_key, section["old_anchor"]) == section["old_anchor"]
        # The migration may relocate a qualified section to another file;
        # the crosswalk map itself keeps the historical source boundary.
        mapped = next(item["new_anchor"] for item in maps[source]["anchors"]
                      if item["old_anchor"] == section["old_anchor"])
        active_anchor = any(
            (root / candidate["destination_file"]).is_file()
            and mapped in anchor_info((root / candidate["destination_file"]).read_text())[0]
            for candidate in candidates
        )
        if not active_anchor:
            # Consolidation can relocate an old implementation section into an
            # attached subcore without retaining its obsolete editor anchor. Its
            # legacy identity must still be declared in the destination row.
            historical_machine_ids = {
                candidate.get(key, "")
                for candidate in candidates
                for key in ("machine_id", "pre_reorganization_2026_11_20", "pre_subcore_2026_11_20")
            }
            represented = any(
                section.get("legacy_section_id") in candidate.get("legacy_section_ids", [])
                or section.get("machine_id") in historical_machine_ids
                or any(
                    section.get("machine_id", "").startswith(machine_id + ".")
                    for machine_id in historical_machine_ids if machine_id
                )
                for candidate in candidates
            )
            assert represented, (source, mapped, [c["destination_file"] for c in candidates])
        section_count += 1

    assert all(inverse_sections[(source, machine)] == legacy
               for (source, legacy), machine in forward_sections.items())
    assert all(forward_sections[(source, legacy)] == machine
               for (source, machine), legacy in inverse_sections.items())
    assert all(inverse_anchors[(source, new)] == old
               for (source, old), new in forward_anchors.items())
    assert all(forward_anchors[(source, old)] == new
               for (source, new), old in inverse_anchors.items())

    import renumber_corpus_chapters as rewrite
    import trace_widget_numbering as trace_rewrite
    import router_table_lib as router_rewrite
    rewritten_sources = {path.relative_to(root).as_posix() for path in rewrite.walk(root)}
    assert not any(path.startswith("_pages_site/") for path in rewritten_sources)
    assert not {
        "tools/router_table_lib.py",
        "tools/router_bidirectional_sync.py",
        "tools/trace_widget_numbering.py",
        "tools/test_chapter_numbering_migration.py",
    } & rewritten_sources
    _unique, shared = rewrite.id_map(registry)
    assert shared

    trace_fixture = (
        "- Downstream: [One](one.md); [Two](two.md); [Three](three.md); [Four](four.md)\n"
        "- Short: [One](one.md); [Two](two.md)"
    )
    nested = trace_rewrite.nested_long_lines(trace_fixture)
    nested_lines = nested.splitlines()
    assert nested_lines[0] == "- Downstream:"
    children = [line for line in nested_lines[1:] if line.startswith("  - ")]
    assert len(children) == 4
    assert all(len(trace_rewrite.REFERENCE_RE.findall(line)) == 1 for line in children)
    assert nested_lines[-1] == "- Short: [One](one.md); [Two](two.md)"
    assert trace_rewrite.nested_long_lines(nested) == nested

    # Remove orphaned child bullets left when a prior D14 pass split a
    # generated router annotation before the annotation itself was stripped.
    routed_fixture = (
        "- Chapter Two basis: §3.1.\n"
        "  - **CJS-0.105 §1** (*Topic router*). Mandatory read-with: **CJS-3.110 §3**,\n"
        "  - **CI-6.215 §3** (*Contest-integrity monitoring*).\n"
        "  - **CJS-0.105 §1** (*Topic router*); primary owners\n"
        "  - **CI-16.205** (*Appointment and removal*),\n"
        "- Ordinary downstream reference: **CJS-3.110 §3**.\n"
    )
    cleaned_routes = router_rewrite.strip_routing_annotations(routed_fixture)
    assert "Topic router" not in cleaned_routes
    assert "CI-6.215" not in cleaned_routes
    assert "CI-16.205" not in cleaned_routes
    assert "Ordinary downstream reference" in cleaned_routes

    sync_report = subprocess.check_output(
        [sys.executable, str(root / "tools/router_bidirectional_sync.py"), "--root", str(root)],
        cwd=root,
        text=True,
    )
    assert "Dry run: 0 files would change." in sync_report, sync_report

    # Exercise the real finalizer in an isolated fixture. Historically its
    # restoration branch was nested under the historical-text guard, leaving
    # placeholders in ordinary files during a fresh replay.
    with tempfile.TemporaryDirectory(prefix="chapter-finalize-test-") as temp_name:
        temp_root = Path(temp_name)
        (temp_root / "tools/architecture").mkdir(parents=True)
        (temp_root / "ai_corpus/indexes").mkdir(parents=True)
        shutil.copy2(root / "tools/architecture/chapter_numbers.json",
                     temp_root / "tools/architecture/chapter_numbers.json")
        shutil.copy2(root / "tools/architecture/chapter_crosswalk.json",
                     temp_root / "tools/architecture/chapter_crosswalk.json")
        shutil.copy2(root / "ai_corpus/indexes/section_manifest.json",
                     temp_root / "ai_corpus/indexes/section_manifest.json")
        shared_item = next(iter(shared.items()))
        anchor_source = next(item for item in crosswalk["anchor_maps"] if item["anchors"])
        row_index = next(i for i, row in enumerate(rows)
                         if anchor_source["source_file"] in (row.get("original_file"), row.get("destination_file")))
        expected_anchor = anchor_source["anchors"][0]["new_anchor"]
        probe = temp_root / "finalize_probe.md"
        marker = lambda value: "⟦CH" + value + "⟧"
        probe.write_text(
            "[chapter](" + marker("FILE:0") + ") " + marker("ID:0") + ".2 "
            + marker("AMBIG:0") + " [section](" + marker("ANCHOR:" + str(row_index) + ":0") + ")\n",
            encoding="utf-8",
        )
        rewrite.replace_text(temp_root, registry, {}, "finalize")
        finalized = probe.read_text(encoding="utf-8")
        assert ("⟦" + "CH") not in finalized, finalized
        assert rows[0]["destination_file"] in finalized
        assert rows[0]["display_id"] + " §2" in finalized
        assert " and ".join(shared_item[1]) in finalized or shared_item[1][0] in finalized
        assert "(#" + expected_anchor + ")" in finalized

    # Unqualified shared IDs are represented as destination lists, not a winner.
    assert all(len(destinations) > 1 for destinations in shared.values())
    print(f"PASS: {len(rows)} chapter rows, {len(forward_sections)} reversible qualified sections, "
          f"{len(forward_anchors)} reversible heading anchors, and finalizer markers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
