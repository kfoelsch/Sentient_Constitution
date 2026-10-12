#!/usr/bin/env python3
"""Tests for bump_edition."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bump_edition import bump, edition_for, read_current, rewrite_text  # noqa: E402

SCRIPT = Path(__file__).resolve().parent / "bump_edition.py"
OLD = "SC-Corpus-2026.08.09"

README = f"""# T

| | |
|---|---|
| **Corpus edition** | `{OLD}` |
| **Effective date** | 2026-08-09 |
"""

FILES = {
    "README.md": README,
    "AGENTS.md": f"- **Edition:** `{OLD}` (effective 2026-08-09). Pre-release.\n",
    "llms.txt": f"Edition: {OLD} (effective 2026-08-09). Pre-release.\n",
    "implementation/steward_owner_clock_index.json": f'{{"pinned_to_edition": "{OLD}", "edition_effective": "2026-08-09"}}\n',
    "implementation/adoption/easy_entry/E01.md": f"**Pinned to corpus edition:** `{OLD}`\n",
    "implementation/adoption/README.md": f"Pinned `{OLD}`; see also the 2026-08-09 schema example.\n",
    "project/VISION.md": "Reformed 2026-08-09 (not an edition pin).\n",
    "doc_architecture.md": f"Pilots remain pinned to `{OLD}`. <!-- edition-pin: keep -->\nLive pin `{OLD}`.\n",
    # historical or generated: must not change
    "translations/es/README.md": f"Based on `{OLD}`\n",
    "archive/old.md": f"`{OLD}` effective 2026-08-09\n",
    "evidence/2026-09-09/x.md": f"`{OLD}`\n",
    "ai_corpus/indexes/id_resolver.json": f'{{"edition": "{OLD}"}}\n',
    "doc_architecture/generated/topic.md": f"`{OLD}`\n",
    "docs/corpus_index.md": f"`{OLD}`\n",
    "evaluation/external_audit_2026-08/README.md": f"Pinned to `{OLD}` (effective 2026-08-09).\n",
    "evaluation/self_application/results/2026-08-22_cursor.md": f"- **Corpus edition pin:** `{OLD}`\n",
    "evaluation/self_application/results/_TEMPLATE.md": f"- **Corpus edition pin:** `{OLD}`\n",
}


def build(root: Path) -> None:
    for rel, text in FILES.items():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    (root / "implementation" / "schemas").mkdir(parents=True, exist_ok=True)
    (root / "implementation" / "schemas" / "example.json").write_text('{"logged_at": "2026-08-09T02:18:00-05:00"}\n', encoding="utf-8")


class BumpTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        build(self.root)
        self.day = date(2026, 10, 12)
        self.new = "SC-Corpus-2026.10.12"

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def text(self, rel: str) -> str:
        return (self.root / rel).read_text(encoding="utf-8")

    def test_edition_format(self) -> None:
        self.assertEqual(edition_for(date(2026, 1, 5)), "SC-Corpus-2026.01.05")

    def test_dry_run_changes_nothing(self) -> None:
        results = bump(self.root, self.day, write=False)
        self.assertTrue(results)
        self.assertEqual(self.text("README.md"), README)

    def test_readme_table_is_rewritten(self) -> None:
        bump(self.root, self.day, write=True)
        self.assertEqual(read_current(self.root), (self.new, "2026-10-12"))

    def test_live_pins_move(self) -> None:
        bump(self.root, self.day, write=True)
        self.assertIn(f"`{self.new}` (effective 2026-10-12)", self.text("AGENTS.md"))
        self.assertIn(f"{self.new} (effective 2026-10-12)", self.text("llms.txt"))
        index = self.text("implementation/steward_owner_clock_index.json")
        self.assertIn(f'"pinned_to_edition": "{self.new}"', index)
        self.assertIn('"edition_effective": "2026-10-12"', index)
        self.assertIn(self.new, self.text("implementation/adoption/easy_entry/E01.md"))
        self.assertIn(self.new, self.text("evaluation/self_application/results/_TEMPLATE.md"))

    def test_only_the_edition_line_changes_in_a_mixed_line(self) -> None:
        bump(self.root, self.day, write=True)
        self.assertEqual(
            self.text("implementation/adoption/README.md"),
            f"Pinned `{self.new}`; see also the 2026-08-09 schema example.\n",
        )

    def test_unrelated_dates_stay(self) -> None:
        bump(self.root, self.day, write=True)
        self.assertEqual(self.text("project/VISION.md"), "Reformed 2026-08-09 (not an edition pin).\n")
        self.assertIn("2026-08-09T02:18:00", self.text("implementation/schemas/example.json"))

    def test_historical_and_generated_files_stay(self) -> None:
        bump(self.root, self.day, write=True)
        for rel in (
            "translations/es/README.md",
            "archive/old.md",
            "evidence/2026-09-09/x.md",
            "ai_corpus/indexes/id_resolver.json",
            "doc_architecture/generated/topic.md",
            "docs/corpus_index.md",
            "evaluation/external_audit_2026-08/README.md",
            "evaluation/self_application/results/2026-08-22_cursor.md",
        ):
            self.assertEqual(self.text(rel), FILES[rel], rel)

    def test_keep_marker_protects_one_line_only(self) -> None:
        bump(self.root, self.day, write=True)
        lines = self.text("doc_architecture.md").splitlines()
        self.assertIn(OLD, lines[0])
        self.assertIn(self.new, lines[1])

    def test_second_run_is_a_no_op(self) -> None:
        bump(self.root, self.day, write=True)
        self.assertEqual(bump(self.root, self.day, write=True), [])

    def test_bumping_forward_again(self) -> None:
        bump(self.root, self.day, write=True)
        bump(self.root, date(2026, 10, 20), write=True)
        self.assertEqual(read_current(self.root), ("SC-Corpus-2026.10.20", "2026-10-20"))
        self.assertIn("SC-Corpus-2026.10.20", self.text("AGENTS.md"))
        self.assertNotIn("SC-Corpus-2026.10.12", self.text("AGENTS.md"))

    def test_rewrite_text_counts_lines(self) -> None:
        text, changed = rewrite_text(f"a {OLD}\nb\nc effective 2026-08-09\n", OLD, "2026-08-09", self.new, "2026-10-12")
        self.assertEqual(changed, 2)
        self.assertEqual(text, f"a {self.new}\nb\nc effective 2026-10-12\n")

    def test_cli_dry_run_then_write(self) -> None:
        dry = subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.root), "--date", "2026-10-12"], capture_output=True, text=True)
        self.assertEqual(dry.returncode, 0, dry.stderr)
        self.assertIn("Dry run", dry.stdout)
        self.assertEqual(self.text("README.md"), README)
        done = subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.root), "--date", "2026-10-12", "--write"], capture_output=True, text=True)
        self.assertEqual(done.returncode, 0, done.stderr)
        self.assertEqual(read_current(self.root)[0], self.new)
        again = subprocess.run([sys.executable, str(SCRIPT), "--root", str(self.root), "--date", "2026-10-12", "--write"], capture_output=True, text=True)
        self.assertIn("nothing to do", again.stdout)


if __name__ == "__main__":
    unittest.main()
