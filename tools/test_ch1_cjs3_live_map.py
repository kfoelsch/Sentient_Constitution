#!/usr/bin/env python3
"""Tests for the live cluster-map reader in ch1_cjs3_alignment_audit."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ch1_cjs3_alignment_audit as audit  # noqa: E402

TABLE = """\
| ID | Title | Leg | Aim | Profile | Chapter One § basis | Note |
|---|---|---|---|---|---|---|
| **CJS-5.110 §2** / **oDef.2** (*Oversight*) | Oversight | O | F | O·F | Chapter One §15.2, §6, §15.2 | — |
| **CJS-5.110 §3 and CJS-5.115 §3** / **oDef.3** (*Oversight*) | Oversight | O | F | O·F | Chapter One §18.2, §19.1 | — |
| **CJS-5.110 §4** / **oDef.4** (*Oversight*) | Oversight | O | F | O·F | — | — |
| not a cluster row | x | x | x | x | Chapter One §1 | x |
"""


class LiveMapTests(unittest.TestCase):
    def test_reads_sections_in_order_without_duplicates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = root / audit.CLUSTER_MAP_FILE
            target.parent.mkdir(parents=True)
            target.write_text(TABLE, encoding="utf-8")
            mapping = audit.load_live_cluster_map(root)
        self.assertEqual(mapping["CJS-5.110 §2"], ["15.2", "6"])
        self.assertEqual(mapping["CJS-5.110 §3"], ["18.2", "19.1"])
        self.assertNotIn("CJS-5.110 §4", mapping)
        self.assertEqual(len(mapping), 2)

    def test_missing_file_gives_empty_map(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(audit.load_live_cluster_map(Path(tmp)), {})

    def test_repo_map_covers_every_numbered_cluster(self) -> None:
        repo = Path(__file__).resolve().parent.parent
        mapping = audit.load_live_cluster_map(repo)
        self.assertEqual(set(mapping), set(audit.EXPECTED_CLUSTER_IDS))

    def test_repo_basis_lines_match_the_map(self) -> None:
        repo = Path(__file__).resolve().parent.parent
        auditor = audit.Ch1Cjs3AlignmentAuditor(repo)
        auditor.run()
        self.assertEqual(auditor.gaps["weak_trace"], [])


if __name__ == "__main__":
    unittest.main()
