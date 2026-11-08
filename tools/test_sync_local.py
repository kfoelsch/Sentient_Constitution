#!/usr/bin/env python3
"""Tests for sync_local (GIT-LOCAL-SYNC-01), run against throwaway git repositories."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sync_local as sl  # noqa: E402


def run(cwd: Path, *args: str) -> str:
    proc = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if proc.returncode:
        raise AssertionError(f"git {' '.join(args)}: {proc.stderr}")
    return proc.stdout.strip()


class Repos:
    """A bare origin, a local clone, and a second clone that plays the part of GitHub merging."""

    def __init__(self, tmp: str) -> None:
        base = Path(tmp)
        self.origin = base / "origin.git"
        subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(self.origin)], check=True)
        self.other = base / "other"
        subprocess.run(["git", "clone", "-q", str(self.origin), str(self.other)], check=True, capture_output=True)
        self._identify(self.other)
        self.commit(self.other, "a.txt", "one\n", "first")
        run(self.other, "push", "-q", "origin", "main")
        self.local = base / "local"
        subprocess.run(["git", "clone", "-q", str(self.origin), str(self.local)], check=True, capture_output=True)
        self._identify(self.local)

    @staticmethod
    def _identify(path: Path) -> None:
        run(path, "config", "user.email", "t@example.com")
        run(path, "config", "user.name", "T")
        run(path, "config", "commit.gpgsign", "false")

    @staticmethod
    def commit(path: Path, name: str, text: str, msg: str) -> None:
        (path / name).write_text(text, encoding="utf-8")
        run(path, "add", name)
        run(path, "commit", "-q", "-m", msg)

    def merge_branch_upstream(self, branch: str) -> None:
        """Merge ``branch`` into origin/main with a merge commit and delete it there, like a merged pull request."""
        run(self.other, "fetch", "-q", "origin")
        run(self.other, "checkout", "-q", "main")
        run(self.other, "pull", "-q", "--ff-only", "origin", "main")
        run(self.other, "merge", "-q", "--no-ff", "-m", f"Merge {branch}", f"origin/{branch}")
        run(self.other, "push", "-q", "origin", "main")
        run(self.origin, "branch", "-q", "-D", branch)


class SyncTests(unittest.TestCase):
    def test_merged_branch_is_left_and_deleted_and_main_fast_forwarded(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            r = Repos(tmp)
            run(r.local, "switch", "-q", "-c", "work")
            Repos.commit(r.local, "b.txt", "two\n", "work commit")
            run(r.local, "push", "-q", "-u", "origin", "work")
            r.merge_branch_upstream("work")
            lines = sl.sync(r.local)
            self.assertEqual(run(r.local, "branch", "--show-current"), "main")
            self.assertNotIn("work", run(r.local, "branch", "--list"))
            self.assertEqual(run(r.local, "rev-parse", "main"), run(r.local, "rev-parse", "origin/main"))
            self.assertTrue((r.local / "b.txt").exists())
            self.assertTrue(any("deleted work" in line for line in lines), lines)

    def test_replayed_commits_with_new_hashes_still_count_as_merged(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            r = Repos(tmp)
            run(r.local, "switch", "-q", "-c", "work")
            Repos.commit(r.local, "b.txt", "two\n", "work commit")
            run(r.local, "push", "-q", "-u", "origin", "work")
            # The same change reaches origin/main under a different hash, as a replayed pull request would.
            run(r.other, "fetch", "-q", "origin")
            run(r.other, "checkout", "-q", "main")
            run(r.other, "cherry-pick", "origin/work")
            run(r.other, "push", "-q", "origin", "main")
            run(r.origin, "branch", "-q", "-D", "work")
            sl.sync(r.local)
            self.assertEqual(run(r.local, "branch", "--show-current"), "main")
            self.assertNotIn("work", run(r.local, "branch", "--list"))

    def test_branch_with_unmerged_commit_is_never_deleted(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            r = Repos(tmp)
            run(r.local, "switch", "-q", "-c", "work")
            Repos.commit(r.local, "b.txt", "two\n", "pushed commit")
            run(r.local, "push", "-q", "-u", "origin", "work")
            r.merge_branch_upstream("work")
            Repos.commit(r.local, "c.txt", "three\n", "local only")
            lines = sl.sync(r.local)
            self.assertEqual(run(r.local, "branch", "--show-current"), "work")
            self.assertIn("work", run(r.local, "branch", "--list"))
            self.assertTrue(any("not in origin/main" in line for line in lines), lines)

    def test_dirty_tracked_file_blocks_switching(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            r = Repos(tmp)
            run(r.local, "switch", "-q", "-c", "work")
            Repos.commit(r.local, "b.txt", "two\n", "work commit")
            run(r.local, "push", "-q", "-u", "origin", "work")
            r.merge_branch_upstream("work")
            (r.local / "a.txt").write_text("edited\n", encoding="utf-8")
            lines = sl.sync(r.local)
            self.assertEqual(run(r.local, "branch", "--show-current"), "work")
            self.assertEqual((r.local / "a.txt").read_text(encoding="utf-8"), "edited\n")
            self.assertTrue(any("uncommitted" in line for line in lines), lines)

    def test_untracked_files_do_not_block(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            r = Repos(tmp)
            run(r.local, "switch", "-q", "-c", "work")
            Repos.commit(r.local, "b.txt", "two\n", "work commit")
            run(r.local, "push", "-q", "-u", "origin", "work")
            r.merge_branch_upstream("work")
            (r.local / "scratch.txt").write_text("keep me\n", encoding="utf-8")
            sl.sync(r.local)
            self.assertEqual(run(r.local, "branch", "--show-current"), "main")
            self.assertTrue((r.local / "scratch.txt").exists())

    def test_main_fast_forwards_in_place_and_other_gone_branches_are_listed_not_deleted(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            r = Repos(tmp)
            run(r.local, "switch", "-q", "-c", "old")
            Repos.commit(r.local, "b.txt", "two\n", "old work")
            run(r.local, "push", "-q", "-u", "origin", "old")
            run(r.local, "switch", "-q", "main")
            r.merge_branch_upstream("old")
            lines = sl.sync(r.local)
            self.assertEqual(run(r.local, "rev-parse", "main"), run(r.local, "rev-parse", "origin/main"))
            self.assertIn("old", run(r.local, "branch", "--list"))                  # listed, not deleted
            self.assertTrue(any("safe to delete: old" in line for line in lines), lines)
            sl.sync(r.local, delete_merged=True)
            self.assertNotIn("old", run(r.local, "branch", "--list"))

    def test_dry_run_changes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            r = Repos(tmp)
            run(r.local, "switch", "-q", "-c", "work")
            Repos.commit(r.local, "b.txt", "two\n", "work commit")
            run(r.local, "push", "-q", "-u", "origin", "work")
            r.merge_branch_upstream("work")
            lines = sl.sync(r.local, dry_run=True)
            self.assertEqual(run(r.local, "branch", "--show-current"), "work")
            self.assertTrue(any(line.startswith("would ") for line in lines), lines)

    def test_diverged_main_is_left_alone(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            r = Repos(tmp)
            Repos.commit(r.local, "mine.txt", "x\n", "commit on main")
            lines = sl.sync(r.local)
            self.assertTrue(any("left alone" in line for line in lines), lines)


if __name__ == "__main__":
    unittest.main()
