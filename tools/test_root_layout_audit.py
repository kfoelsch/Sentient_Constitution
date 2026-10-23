#!/usr/bin/env python3
"""Tests for root_layout_audit."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from root_layout_audit import classify, find_strays, rewrite_links, root_candidates  # noqa: E402

SCRIPT = Path(__file__).resolve().parent / "root_layout_audit.py"


class ClassifyTests(unittest.TestCase):
    def test_plain_language_variants_flagged(self) -> None:
        for name in ("Article_XX_plain_language.md", "plain-language-notes.md", "X_Plain_Language.md"):
            self.assertEqual(classify(name).rule_id, "RL-PLAIN-01", name)

    def test_wip_and_draft_tokens_flagged(self) -> None:
        for name in ("foo_wip.md", "WIP_notes.md", "x-draft.md", "DRAFT.md", "notes.wip.md"):
            self.assertEqual(classify(name).rule_id, "RL-WIP-01", name)

    def test_bundles_flagged_in_any_case(self) -> None:
        for name in ("ch08_push.bundle", "lobbying_push.bundle", "X.BUNDLE", "a_wip.bundle"):
            self.assertEqual(classify(name).rule_id, "RL-BUNDLE-01", name)
        self.assertIsNone(classify("bundle_notes.md"))
        self.assertIsNone(classify("unbundled.md"))

    def test_plain_rule_wins_over_draft(self) -> None:
        self.assertEqual(classify("ARTICLE_VIII_PLAIN_LANGUAGE_DRAFT.md").rule_id, "RL-PLAIN-01")

    def test_legitimate_root_files_pass(self) -> None:
        for name in ("README.md", "AGENTS.md", "core_06.010_rights_part_c.md", "steward_box_review.md",
                     "Makefile", "doc_architecture.md", "swipe.md", "drafting_contracts.md"):
            self.assertIsNone(classify(name), name)

    def test_subdirectory_paths_ignored(self) -> None:
        self.assertEqual(find_strays(["project/plain_language/Article_XX_plain_language.md",
                                      "project/ARTICLE_VIII_PLAIN_LANGUAGE_DRAFT.md"]), [])


class RewriteTests(unittest.TestCase):
    def test_links_repointed_and_siblings_kept(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            new = root / "project" / "plain_language"
            new.mkdir(parents=True)
            (root / "core_06.md").write_text("x")
            (new / "Article_XXI_plain_language.md").write_text("x")
            text = ("[a](core_06.md#frag) [b](Article_XXI_plain_language.md) "
                    "[c](https://example.com/core_06.md) [d](#local) [e](missing.md)")
            out = rewrite_links(text, root, new)
            self.assertIn("[a](../../core_06.md#frag)", out)
            self.assertIn("[b](Article_XXI_plain_language.md)", out)
            self.assertIn("(https://example.com/core_06.md)", out)
            self.assertIn("[d](#local)", out)
            self.assertIn("[e](missing.md)", out)


def run_git(root: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True)


class EndToEndTests(unittest.TestCase):
    def make_repo(self, td: str) -> Path:
        root = Path(td)
        run_git(root, "init", "-q")
        (root / "README.md").write_text("hi\n")
        (root / "core_01.md").write_text("core\n")
        return root

    def audit(self, root: Path, *extra: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run([sys.executable, str(SCRIPT), "--root", str(root), *extra],
                              capture_output=True, text=True)

    def test_clean_repo_passes(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = self.make_repo(td)
            r = self.audit(root)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_untracked_stray_fails_and_ignored_is_skipped(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = self.make_repo(td)
            (root / ".gitignore").write_text("ignored_wip.md\n")
            (root / "ignored_wip.md").write_text("x")
            self.assertEqual(self.audit(root).returncode, 0)
            (root / "Article_XX_plain_language.md").write_text("x")
            r = self.audit(root)
            self.assertEqual(r.returncode, 1)
            self.assertIn("Article_XX_plain_language.md: RL-PLAIN-01", r.stdout)

    def test_staged_mode_sees_only_staged_additions(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = self.make_repo(td)
            (root / "notes_wip.md").write_text("x")
            self.assertEqual(self.audit(root, "--staged").returncode, 0)
            run_git(root, "add", "notes_wip.md")
            r = self.audit(root, "--staged")
            self.assertEqual(r.returncode, 1)
            self.assertIn("RL-WIP-01", r.stdout)

    def test_fix_moves_plain_files_and_rewrites_links(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = self.make_repo(td)
            (root / "Article_XX_plain_language.md").write_text(
                "[core](core_01.md#a) [sib](Article_XXI_plain_language.md)\n")
            (root / "Article_XXI_plain_language.md").write_text("[core](core_01.md)\n")
            self.assertEqual(self.audit(root, "--fix").returncode, 0)
            dest = root / "project" / "plain_language"
            self.assertFalse((root / "Article_XX_plain_language.md").exists())
            self.assertEqual((dest / "Article_XX_plain_language.md").read_text(),
                             "[core](../../core_01.md#a) [sib](Article_XXI_plain_language.md)\n")
            self.assertEqual((dest / "Article_XXI_plain_language.md").read_text(), "[core](../../core_01.md)\n")
            self.assertEqual(self.audit(root).returncode, 0)

    def test_fix_refuses_to_overwrite_and_leaves_wip_alone(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = self.make_repo(td)
            (root / "project" / "plain_language").mkdir(parents=True)
            (root / "project" / "plain_language" / "A_plain_language.md").write_text("old")
            (root / "A_plain_language.md").write_text("new")
            (root / "x_wip.md").write_text("w")
            r = self.audit(root, "--fix")
            self.assertEqual(r.returncode, 1)
            self.assertEqual((root / "project" / "plain_language" / "A_plain_language.md").read_text(), "old")
            self.assertTrue((root / "A_plain_language.md").exists())
            self.assertTrue((root / "x_wip.md").exists())

    def test_untracked_bundle_fails_and_fix_leaves_it(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = self.make_repo(td)
            (root / "x_push.bundle").write_bytes(b"PK")
            r = self.audit(root)
            self.assertEqual(r.returncode, 1)
            self.assertIn("x_push.bundle: RL-BUNDLE-01", r.stdout)
            self.assertEqual(self.audit(root, "--fix").returncode, 1)
            self.assertTrue((root / "x_push.bundle").exists())

    def test_root_candidates_skips_deleted_tracked_files(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = self.make_repo(td)
            (root / "gone_wip.md").write_text("x")
            run_git(root, "add", "-A")
            (root / "gone_wip.md").unlink()
            self.assertNotIn("gone_wip.md", root_candidates(root, staged=False))


if __name__ == "__main__":
    unittest.main()
