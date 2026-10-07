#!/usr/bin/env python3
"""Tests that obligation-diff evidence keeps changes and drops bulk."""

from __future__ import annotations

import unittest

from obligation_inventory_diff import slim_evidence


def rec(modality: str, text: str) -> dict:
    return {"modality": modality, "text": text, "terms": text.lower().split()}


class SlimEvidenceTests(unittest.TestCase):
    def setUp(self) -> None:
        keep = rec("DUTY", "Certification must verify the record.")
        self.before = {"generated": "2026-10-06", "files": {
            "a.md": [keep, rec("PROHIBITION", "A system must not be downclassified.")],
            "b.md": [rec("DUTY", "Unchanged clause must stay.")],
        }}
        self.after = {"generated": "2026-10-06", "files": {
            "a.md": [keep, rec("DUTY", "A system must be reclassified upward.")],
            "b.md": [rec("DUTY", "Unchanged clause must stay.")],
        }}
        self.out = slim_evidence(self.before, self.after, ["finding"], ["note"])

    def test_unchanged_records_and_terms_are_dropped(self) -> None:
        text = repr(self.out)
        self.assertNotIn("Unchanged clause", text)
        self.assertNotIn("Certification must verify", text)
        self.assertNotIn("terms", text)
        self.assertNotIn("b.md", self.out["changes"])

    def test_changed_records_keep_modality_and_wording(self) -> None:
        change = self.out["changes"]["a.md"]
        self.assertEqual(change["removed"], [{"modality": "PROHIBITION", "text": "A system must not be downclassified."}])
        self.assertEqual(change["added"], [{"modality": "DUTY", "text": "A system must be reclassified upward."}])

    def test_counts_reconcile(self) -> None:
        info = self.out["files"]["a.md"]
        self.assertEqual((info["before"], info["after"], info["unchanged"]), (2, 2, 1))

    def test_findings_notes_and_format_are_kept(self) -> None:
        self.assertEqual(self.out["findings"], ["finding"])
        self.assertEqual(self.out["notes"], ["note"])
        self.assertEqual(self.out["format"], "obligation-diff-slim/1")

    def test_duplicate_clauses_are_counted_not_collapsed(self) -> None:
        dup = rec("DUTY", "Same words twice must hold.")
        out = slim_evidence({"files": {"c.md": [dup, dup]}}, {"files": {"c.md": [dup]}}, [], [])
        self.assertEqual(len(out["changes"]["c.md"]["removed"]), 1)
        self.assertEqual(out["files"]["c.md"]["unchanged"], 1)


if __name__ == "__main__":
    unittest.main()
