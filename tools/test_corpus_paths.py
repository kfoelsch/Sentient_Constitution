#!/usr/bin/env python3
"""Tests for tools/corpus_paths.py subcore discovery (TIER-PLACE-01)."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import corpus_paths


class SubcoreScopeTest(unittest.TestCase):
    def test_subcore_files_join_binding_scope(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "subcore_23.100_forum_intake.md").write_text("# x\n", encoding="utf-8")
            (root / "notes_subcore.md").write_text("# y\n", encoding="utf-8")
            self.assertEqual(corpus_paths.subcore_files(root), ["subcore_23.100_forum_intake.md"])
            scope = corpus_paths.binding_corpus_scope(root)
            self.assertIn("subcore_23.100_forum_intake.md", scope)
            self.assertNotIn("notes_subcore.md", scope)
            self.assertLess(scope.index(corpus_paths.CORE_FILES[-1]), scope.index("subcore_23.100_forum_intake.md"))

    def test_no_subcore_files_is_empty(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(corpus_paths.subcore_files(Path(tmp)), [])


if __name__ == "__main__":
    unittest.main()
