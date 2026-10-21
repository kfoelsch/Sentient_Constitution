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
    by_source = {row["original_file"]: row for row in rows}
    assert len(rows) == 117
    assert len({row["machine_id"] for row in rows}) == len(rows)
    assert len({row["destination_file"] for row in rows}) == len(rows)
    assert len({row["original_file"] for row in rows}) == len(rows)
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
    baseline_anchors: dict[str, set[str]] = {}
    for section in crosswalk["sections"]:
        source = section["source_file"]
        row = by_source[source]
        if source not in baseline_anchors:
            original_text = subprocess.check_output(
                ["git", "show", f"pre-chapter-numbering-2026-10-21:{source}"],
                cwd=root, text=True,
            )
            baseline_anchors[source] = anchor_info(original_text)[0]
        assert section["old_anchor"] in baseline_anchors[source], (source, section["old_anchor"])
        legacy_key = (source, section["legacy_section_id"])
        machine_key = (source, section["machine_id"])
        old_anchor_key = (source, section["old_anchor"])
        new_anchor_key = (source, section["new_anchor"])
        assert forward_sections.setdefault(legacy_key, section["machine_id"]) == section["machine_id"]
        assert inverse_sections.setdefault(machine_key, section["legacy_section_id"]) == section["legacy_section_id"]
        assert forward_anchors.setdefault(old_anchor_key, section["new_anchor"]) == section["new_anchor"]
        assert inverse_anchors.setdefault(new_anchor_key, section["old_anchor"]) == section["old_anchor"]
        # A qualified section destination retains its original file boundary.
        assert source in by_source
        destination = root / row["destination_file"]
        anchors = anchor_info(destination.read_text())[0]
        mapped = next(item["new_anchor"] for item in maps[source]["anchors"]
                      if item["old_anchor"] == section["old_anchor"])
        assert mapped in anchors, (row["destination_file"], mapped)
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
        "- Chapter One basis: §3.1.\n"
        "  - **CJS-0.105 §1** (*Topic router*). Mandatory read-with: **CJS-5.110 §3**,\n"
        "  - **CI-8.215 §3** (*Contest-integrity monitoring*).\n"
        "  - **CJS-0.105 §1** (*Topic router*); primary owners\n"
        "  - **CI-14.205** (*Appointment and removal*),\n"
        "- Ordinary downstream reference: **CJS-5.110 §3**.\n"
    )
    cleaned_routes = router_rewrite.strip_routing_annotations(routed_fixture)
    assert "Topic router" not in cleaned_routes
    assert "CI-8.215" not in cleaned_routes
    assert "CI-14.205" not in cleaned_routes
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
                         if row["original_file"] == anchor_source["source_file"])
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
