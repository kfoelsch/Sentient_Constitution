#!/usr/bin/env python3
"""Tests for TIME-LOCK-01 (copies of the tier windows follow their owners)."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import time_window_lockstep_audit as audit

CF = """\
| **Pipeline stage** | **Tier A** (≤ 7 days) | **Tier B** (≤ 14 days) | **Tier C** (≤ 30 days) | **Tier L** (≤ 60 days) | **Tier P** (≤ 90 days) |
| --- | --- | --- | --- | --- | --- |
| Forum access and intake acknowledgment | 24 hours | 2 calendar days | 4 calendar days | 8 calendar days | 12 calendar days |
| **Integrated resolution outer bound** (sum of the stages) | ≤ **7 calendar days** | ≤ **14 calendar days** | ≤ **30 calendar days** | ≤ **60 calendar days** | ≤ **90 calendar days** |

The review window is 24 hours for Tier A, and 2, 4, 8, and 12 calendar days for Tiers B, C, L, and P.
"""

CH13 = """\
- **Tier outer bound:** hard bounds:
  - **Tier A:** at most **7 days** (1 week);
  - **Tier B:** at most **14 days** (2 weeks);
  - **Tier C:** at most **30 days** (one month);
  - **Tier L:** at most **60 days** (two months);
  - **Tier P:** at most **90 days** (three months).
"""

CH7 = """\
| Class and Tier | Response window (intake target) | Resolution window (outer bound) |
|---|---|---|
| Class A, Tier A | 24 hours | 7 calendar days |
| Class B, Tier B | 2 calendar days | 14 calendar days |
| Class C, Tier C | 4 calendar days | 30 calendar days |
| Class L, Tier L | 8 calendar days | 60 calendar days |

Prompt review is 24 hours in Tier A, and 2, 4, 8, and 12 days in Tiers B, C, L, and P.
"""

REGISTRY = {
    "sources": {"stage_table": "cf.md", "outer_bounds": "ch13.md"},
    "tables": [
        {
            "file": "ch7.md",
            "header": ["Class and Tier", "Response window (intake target)", "Resolution window (outer bound)"],
            "rows": {
                "Class A, Tier A": "A",
                "Class B, Tier B": "B",
                "Class C, Tier C": "C",
                "Class L, Tier L": "L",
            },
        }
    ],
    "phrases": [{"file": "cf.md"}, {"file": "ch7.md"}],
}


class Lockstep(unittest.TestCase):
    def setUp(self) -> None:
        self.dir = tempfile.TemporaryDirectory()
        self.root = Path(self.dir.name)
        self.write("cf.md", CF)
        self.write("ch13.md", CH13)
        self.write("ch7.md", CH7)
        self.registry_path = self.root / "registry.json"
        self.registry_path.write_text(json.dumps(REGISTRY), encoding="utf-8")
        self._original = audit.REGISTRY_PATH
        audit.REGISTRY_PATH = self.registry_path

    def tearDown(self) -> None:
        audit.REGISTRY_PATH = self._original
        self.dir.cleanup()

    def write(self, name: str, text: str) -> None:
        (self.root / name).write_text(text, encoding="utf-8")

    def read(self, name: str) -> str:
        return (self.root / name).read_text(encoding="utf-8")

    def test_matching_copies_pass(self) -> None:
        self.assertEqual(audit.run(self.root, fix=False), 0)

    def test_changed_outer_bound_in_owner_flags_the_table(self) -> None:
        self.write("cf.md", CF.replace("≤ 30 days", "≤ 28 days").replace("≤ **30 calendar days**", "≤ **28 calendar days**"))
        self.write("ch13.md", CH13.replace("**30 days** (one month)", "**28 days** (four weeks)"))
        self.assertEqual(audit.run(self.root, fix=False), 1)

    def test_fix_rewrites_table_and_sentences_from_the_owners(self) -> None:
        self.write("cf.md", CF.replace("| 4 calendar days |", "| 3 calendar days |").replace("4, 8, and 12", "3, 8, and 12"))
        self.assertEqual(audit.run(self.root, fix=False), 1)
        self.assertEqual(audit.run(self.root, fix=True), 0)
        self.assertIn("| Class C, Tier C | 3 calendar days | 30 calendar days |", self.read("ch7.md"))
        self.assertIn("2, 3, 8, and 12 days in Tiers B, C, L, and P", self.read("ch7.md"))
        self.assertEqual(audit.run(self.root, fix=False), 0)

    def test_fix_changes_only_the_drifted_cells(self) -> None:
        self.write("ch7.md", CH7.replace("| 14 calendar days |", "| 15 calendar days |"))
        self.assertEqual(audit.run(self.root, fix=True), 0)
        self.assertEqual(self.read("ch7.md"), CH7)

    def test_sources_that_disagree_are_never_fixed(self) -> None:
        self.write("ch13.md", CH13.replace("**14 days** (2 weeks)", "**15 days** (2 weeks)"))
        before = self.read("ch7.md")
        self.assertEqual(audit.run(self.root, fix=True), 2)
        self.assertEqual(self.read("ch7.md"), before)

    def test_missing_registered_table_is_an_error(self) -> None:
        self.write("ch7.md", "No table here. 24 hours in Tier A, and 2, 4, 8, and 12 days in Tiers B, C, L, and P.\n")
        self.assertEqual(audit.run(self.root, fix=False), 2)

    def test_missing_registered_sentence_is_an_error(self) -> None:
        self.write("cf.md", CF.replace("The review window", "The window"). replace("24 hours for Tier A, and 2, 4, 8, and 12 calendar days for Tiers B, C, L, and P", "see the table"))
        self.assertEqual(audit.run(self.root, fix=False), 2)

    def test_missing_table_row_is_an_error(self) -> None:
        self.write("ch7.md", CH7.replace("| Class L, Tier L | 8 calendar days | 60 calendar days |\n", ""))
        self.assertEqual(audit.run(self.root, fix=False), 2)

    def test_hours_and_for_in_wording_are_kept(self) -> None:
        self.write("ch7.md", CH7.replace("24 hours in Tier A", "12 hours in Tier A"))
        self.assertEqual(audit.run(self.root, fix=True), 0)
        self.assertIn("24 hours in Tier A, and 2, 4, 8, and 12 days in Tiers B, C, L, and P", self.read("ch7.md"))


if __name__ == "__main__":
    unittest.main()
