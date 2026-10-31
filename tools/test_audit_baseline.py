#!/usr/bin/env python3
"""Tests for the shrink-only baseline helper (AUDIT-SCOPE-01)."""

from __future__ import annotations

import tempfile
import unittest
from collections import Counter
from pathlib import Path

import audit_baseline


class AuditBaselineTests(unittest.TestCase):
    def test_key_ignores_whitespace_and_numbers_duplicates(self) -> None:
        seen: Counter = Counter()
        a = audit_baseline.make_key("f.md", "same   text", seen)
        b = audit_baseline.make_key("f.md", "same text", seen)
        self.assertNotEqual(a, b)
        self.assertTrue(b.endswith("#2"))
        self.assertEqual(a, audit_baseline.make_key("f.md", "same text", Counter()))

    def test_new_findings_fail_and_fixed_ones_go_stale(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            seen: Counter = Counter()
            old = audit_baseline.make_key("f.md", "old problem", seen)
            audit_baseline.write(root, "demo", "DEMO-01", [(old, "old problem")])
            keyed = [(audit_baseline.make_key("f.md", "new problem", Counter()), "new problem", "NEW")]
            new, stale = audit_baseline.split(root, "demo", keyed)
            self.assertEqual(new, ["NEW"])
            self.assertEqual(stale, [old])
            same = [(old, "old problem", "OLD")]
            new, stale = audit_baseline.split(root, "demo", same)
            self.assertEqual((new, stale), ([], []))


if __name__ == "__main__":
    unittest.main()
