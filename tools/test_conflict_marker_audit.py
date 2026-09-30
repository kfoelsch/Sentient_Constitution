#!/usr/bin/env python3
"""Tests for conflict_marker_audit."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from conflict_marker_audit import scan  # noqa: E402

L, R = "<" * 7, ">" * 7


class ConflictMarkerTests(unittest.TestCase):
    def test_start_marker_with_label_fails(self) -> None:
        self.assertEqual(len(scan("a.md", f"text\n{L} HEAD\nx\n".encode())), 1)

    def test_end_marker_with_sha_fails(self) -> None:
        self.assertEqual(len(scan("a.md", f"{R} 5f677ba9d086e8f03d8668a660e1ba70ee468042\n".encode())), 1)

    def test_bare_markers_fail(self) -> None:
        self.assertEqual(len(scan("a.md", f"{L}\n{R}\n".encode())), 2)

    def test_setext_heading_underline_passes(self) -> None:
        self.assertEqual(scan("a.md", b"Title\n=======\n\nBody\n"), [])

    def test_indented_or_inline_markers_pass(self) -> None:
        self.assertEqual(scan("a.md", f"    {L} HEAD\ntext {R} x\n".encode()), [])

    def test_binary_is_skipped(self) -> None:
        self.assertEqual(scan("a.bin", b"\0" + f"{L} HEAD\n".encode()), [])


if __name__ == "__main__":
    unittest.main()
