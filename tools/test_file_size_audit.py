#!/usr/bin/env python3
"""Tests for file_size_audit."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from file_size_audit import LIMIT_BYTES, audit  # noqa: E402

SCRIPT = Path(__file__).resolve().parent / "file_size_audit.py"


class AuditLogicTests(unittest.TestCase):
    def test_at_limit_passes_one_over_fails(self) -> None:
        v, s, a = audit({"ok.md": LIMIT_BYTES, "big.md": LIMIT_BYTES + 1}, {})
        self.assertEqual([m.split(":")[0] for m in v], ["big.md"])
        self.assertEqual((s, a), ([], []))

    def test_exempt_file_is_reported_not_failed(self) -> None:
        v, s, a = audit({"gen.json": LIMIT_BYTES + 5}, {"gen.json": "generated"})
        self.assertEqual((v, s), ([], []))
        self.assertIn("exempt: generated", a[0])

    def test_stale_exemption_fails_when_file_shrinks_or_vanishes(self) -> None:
        _, s, _ = audit({"gen.json": 10}, {"gen.json": "x", "gone.json": "y"})
        self.assertEqual(sorted(m.split(":")[0] for m in s), ["gen.json", "gone.json"])

    def test_stale_check_can_be_skipped_for_staged_mode(self) -> None:
        _, s, _ = audit({}, {"gen.json": "x"}, check_stale=False)
        self.assertEqual(s, [])


class EndToEndTests(unittest.TestCase):
    def make_repo(self, td: str) -> Path:
        root = Path(td)
        subprocess.run(["git", "-C", str(root), "init", "-q"], check=True, capture_output=True)
        (root / "README.md").write_text("hi\n")
        return root

    def run_audit(self, root: Path, *extra: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(SCRIPT), "--root", str(root), "--no-exemptions", *extra],
                              capture_output=True, text=True)

    def test_clean_then_oversize_untracked_then_ignored(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = self.make_repo(td)
            self.assertEqual(self.run_audit(root).returncode, 0)
            (root / "sub").mkdir()
            (root / "sub" / "dump.json").write_bytes(b"x" * (LIMIT_BYTES + 1))
            r = self.run_audit(root)
            self.assertEqual(r.returncode, 1)
            self.assertIn("sub/dump.json", r.stdout)
            (root / ".gitignore").write_text("sub/dump.json\n")
            self.assertEqual(self.run_audit(root).returncode, 0)

    def test_staged_mode_checks_staged_blob_size(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = self.make_repo(td)
            (root / "big.bin").write_bytes(b"x" * (LIMIT_BYTES + 1))
            self.assertEqual(self.run_audit(root, "--staged").returncode, 0)
            subprocess.run(["git", "-C", str(root), "add", "big.bin"], check=True, capture_output=True)
            r = self.run_audit(root, "--staged")
            self.assertEqual(r.returncode, 1)
            self.assertIn("big.bin", r.stdout)


if __name__ == "__main__":
    unittest.main()
