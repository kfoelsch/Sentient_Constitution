#!/usr/bin/env python3
"""Tests for prune_audit_evidence (AUDIT-EVIDENCE-RETENTION-01)."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import prune_audit_evidence as pe  # noqa: E402

CONFIG = {
    "keep": 2,
    "families": {
        "alpha": ["alpha_report_{date}.md", "alpha_log_{date}.json"],
        "undated": ["relocation.md"],
        "single": ["SINGLE_{date}.md"],
    },
}


def build(root: Path, layout: dict[str, list[str]]) -> None:
    (root / "tools/architecture").mkdir(parents=True)
    (root / pe.CONFIG).write_text(json.dumps(CONFIG), encoding="utf-8")
    for folder, names in layout.items():
        (root / "evidence" / folder).mkdir(parents=True, exist_ok=True)
        for name in names:
            (root / "evidence" / folder / name).write_text("x", encoding="utf-8")


def names(root: Path, folder: str) -> list[str]:
    path = root / "evidence" / folder
    return sorted(p.name for p in path.iterdir()) if path.is_dir() else []


class PruneTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_third_to_last_run_is_deleted(self) -> None:
        build(self.root, {
            f"2026-10-0{d}": [f"alpha_report_2026-10-0{d}.md", f"alpha_log_2026-10-0{d}.json"]
            for d in (1, 2, 3)
        })
        removed = pe.prune(self.root)
        self.assertEqual(len(removed), 2)
        self.assertEqual(names(self.root, "2026-10-01"), [])
        self.assertEqual(len(names(self.root, "2026-10-02")), 2)
        self.assertEqual(len(names(self.root, "2026-10-03")), 2)

    def test_two_runs_or_fewer_are_untouched(self) -> None:
        build(self.root, {
            "2026-10-01": ["alpha_report_2026-10-01.md"],
            "2026-10-02": ["alpha_report_2026-10-02.md"],
        })
        self.assertEqual(pe.prune(self.root), [])

    def test_hand_written_records_are_never_deleted(self) -> None:
        build(self.root, {
            "2026-10-01": ["alpha_report_2026-10-01.md", "decision_note.md", "SINGLE_notes.md"],
            "2026-10-02": ["alpha_report_2026-10-02.md"],
            "2026-10-03": ["alpha_report_2026-10-03.md"],
        })
        pe.prune(self.root)
        self.assertEqual(names(self.root, "2026-10-01"), ["SINGLE_notes.md", "decision_note.md"])

    def test_families_are_counted_separately(self) -> None:
        build(self.root, {
            "2026-10-01": ["alpha_report_2026-10-01.md", "SINGLE_2026-10-01.md"],
            "2026-10-02": ["alpha_report_2026-10-02.md"],
            "2026-10-03": ["alpha_report_2026-10-03.md"],
        })
        pe.prune(self.root)
        self.assertEqual(names(self.root, "2026-10-01"), ["SINGLE_2026-10-01.md"])

    def test_undated_file_names_use_the_folder_date(self) -> None:
        build(self.root, {d: ["relocation.md"] for d in ("2026-10-01", "2026-10-02", "2026-10-03")})
        pe.prune(self.root)
        self.assertEqual(names(self.root, "2026-10-01"), [])
        self.assertEqual(names(self.root, "2026-10-03"), ["relocation.md"])

    def test_several_runs_in_one_folder_count_once(self) -> None:
        build(self.root, {
            "2026-10-01": ["alpha_report_2026-10-01.md", "alpha_report_2026-10-02.md"],
            "2026-10-02": ["alpha_report_2026-10-03.md"],
        })
        self.assertEqual(pe.prune(self.root), [])

    def test_dry_run_deletes_nothing(self) -> None:
        build(self.root, {f"2026-10-0{d}": [f"alpha_report_2026-10-0{d}.md"] for d in (1, 2, 3)})
        removed = pe.prune(self.root, dry_run=True)
        self.assertEqual(len(removed), 1)
        self.assertEqual(len(names(self.root, "2026-10-01")), 1)

    def test_non_dated_entries_in_evidence_are_ignored(self) -> None:
        build(self.root, {f"2026-10-0{d}": [f"alpha_report_2026-10-0{d}.md"] for d in (1, 2, 3)})
        (self.root / "evidence" / "definition_audit").mkdir()
        (self.root / "evidence" / "definition_audit" / "ledger.json").write_text("{}", encoding="utf-8")
        (self.root / "evidence" / "obligation_snapshot.json").write_text("{}", encoding="utf-8")
        pe.prune(self.root)
        self.assertTrue((self.root / "evidence/definition_audit/ledger.json").is_file())
        self.assertTrue((self.root / "evidence/obligation_snapshot.json").is_file())

    def test_bad_config_is_rejected(self) -> None:
        build(self.root, {})
        (self.root / pe.CONFIG).write_text(json.dumps({"keep": 0, "families": {"a": ["x"]}}), encoding="utf-8")
        with self.assertRaises(ValueError):
            pe.load_config(self.root)

    def test_real_config_loads_and_names_compile(self) -> None:
        repo = Path(__file__).resolve().parent.parent
        config = pe.load_config(repo)
        self.assertEqual(config["keep"], 2)
        for templates in config["families"].values():
            for template in templates:
                pe._compile(template)


if __name__ == "__main__":
    unittest.main()
