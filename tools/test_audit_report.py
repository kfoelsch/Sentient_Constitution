#!/usr/bin/env python3
"""Tests for audit_report (AUDIT-REGISTRY-01)."""

from __future__ import annotations

import contextlib
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audit_report as ar  # noqa: E402
import validate_ai_manifests as manifests  # noqa: E402

MAKEFILE = """\
PYTHON ?= python3
.PHONY: regression regression-full alpha-audit beta-check gamma-test delta-evidence-audit helper audit-report

regression:
\t@status=0; \\
\tfor target in \\
\t\talpha-audit \\
\t\tbeta-check \\
\t\tgamma-test; do \\
\t\t$(MAKE) $$target || status=$$?; \\
\tdone; \\
\texit $$status

regression-full:
\t@true

alpha-audit:
\t@echo "alpha ok"

beta-check:
\t@echo "FAIL: beta is broken"; echo "  detail one"; echo "  detail two"; exit 1

gamma-test:
\t@echo "gamma ok"

delta-evidence-audit:
\t@echo "writes a report"

helper:
\t@true

audit-report:
\t@true
"""

REGISTRY = {
    "ignored": {"audit-report": "runs the others"},
    "categories": [{"id": "one", "title": "First group"}, {"id": "two", "title": "Second group"}],
    "targets": {
        "alpha-audit": {"category": "one", "run": "auto", "writes": False},
        "beta-check": {"category": "one", "run": "auto", "writes": False},
        "gamma-test": {"category": "two", "run": "auto", "writes": True},
        "delta-evidence-audit": {"category": "two", "run": "never", "writes": True},
    },
}


class MakefileReadingTests(unittest.TestCase):
    def test_regression_targets_keep_makefile_order(self) -> None:
        self.assertEqual(ar.regression_targets(MAKEFILE), ["alpha-audit", "beta-check", "gamma-test"])

    def test_audit_like_includes_phony_audits_and_regression_but_not_helpers(self) -> None:
        like = ar.audit_like_targets(MAKEFILE)
        self.assertIn("delta-evidence-audit", like)
        self.assertIn("gamma-test", like)
        self.assertNotIn("helper", like)

    def test_phony_continuation_lines_are_joined(self) -> None:
        text = ".PHONY: a-audit \\\n  b-audit\n"
        self.assertEqual(ar.phony_targets(text), {"a-audit", "b-audit"})


class RegistryCheckTests(unittest.TestCase):
    def test_matching_registry_has_no_problems(self) -> None:
        self.assertEqual(ar.check_registry(REGISTRY, MAKEFILE), [])

    def test_unregistered_audit_target_is_reported(self) -> None:
        reg = json.loads(json.dumps(REGISTRY))
        del reg["targets"]["beta-check"]
        problems = ar.check_registry(reg, MAKEFILE)
        self.assertEqual(len(problems), 1)
        self.assertIn("beta-check", problems[0])

    def test_stale_unknown_category_and_bad_flags_are_reported(self) -> None:
        reg = json.loads(json.dumps(REGISTRY))
        reg["targets"]["gone-audit"] = {"category": "one", "run": "auto", "writes": False}
        reg["targets"]["alpha-audit"]["category"] = "nope"
        reg["targets"]["gamma-test"]["run"] = "sometimes"
        reg["targets"]["beta-check"]["writes"] = "no"
        text = "\n".join(ar.check_registry(reg, MAKEFILE))
        for needle in ("gone-audit", "unknown category", "run must be", "writes must be"):
            self.assertIn(needle, text)


class SelectionTests(unittest.TestCase):
    def test_regression_scope_skips_never_and_outside_targets(self) -> None:
        reg = json.loads(json.dumps(REGISTRY))
        reg["targets"]["extra-audit"] = {"category": "two", "run": "auto", "writes": False}
        reg_list = ar.regression_targets(MAKEFILE)
        self.assertEqual(ar.select_targets(reg, reg_list, "regression", set()), ["alpha-audit", "beta-check", "gamma-test"])
        self.assertEqual(ar.select_targets(reg, reg_list, "all", set())[-1], "extra-audit")
        self.assertEqual(ar.select_targets(reg, reg_list, "regression", {"two"}), ["gamma-test"])


class ExcerptTests(unittest.TestCase):
    def test_excerpt_keeps_fail_line_and_indented_detail(self) -> None:
        out = "noise\nFAIL: 2 problems\n  a.md:3 bad\n  b.md:9 bad\nmore noise\nmake: *** Error 1\n"
        self.assertEqual(ar.failure_excerpt(out, 12), ["FAIL: 2 problems", "  a.md:3 bad", "  b.md:9 bad"])

    def test_excerpt_keeps_an_unindented_detail_line_under_a_fail_line(self) -> None:
        out = "FAIL: 1 divergence(s)\nREADME.md: edition is out of date\nanother detail\nunrelated line\n"
        self.assertEqual(ar.failure_excerpt(out, 12), ["FAIL: 1 divergence(s)", "README.md: edition is out of date", "another detail"])

    def test_failure_words_inside_file_names_do_not_count(self) -> None:
        out = "| `ci_13_institutional_failure_sanctions.md` | 15 |\n| other.md | 16 |\n"
        self.assertEqual(ar.failure_excerpt(out, 5), ["| `ci_13_institutional_failure_sanctions.md` | 15 |", "| other.md | 16 |"])

    def test_traceback_is_shown_by_its_last_lines(self) -> None:
        frames = "".join(f'  File "x.py", line {i}, in f\n    call()\n' for i in range(8))
        out = "Traceback (most recent call last):\n" + frames + "AttributeError: no such name\n"
        shown = ar.failure_excerpt(out, 12)
        self.assertEqual(len(shown), 6)
        self.assertEqual(shown[-1], "AttributeError: no such name")

    def test_excerpt_falls_back_to_the_tail_and_respects_the_limit(self) -> None:
        out = "\n".join(f"line {i}" for i in range(30))
        self.assertEqual(ar.failure_excerpt(out, 3), ["line 27", "line 28", "line 29"])


class EndToEndTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "Makefile").write_text(MAKEFILE, encoding="utf-8")
        (self.root / "tools" / "architecture").mkdir(parents=True)
        (self.root / ar.REGISTRY_REL).write_text(json.dumps(REGISTRY), encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_run_groups_by_category_and_expands_only_the_failure(self) -> None:
        names = ["alpha-audit", "beta-check", "gamma-test"]
        results = ar.run_all(self.root, names, REGISTRY, jobs=2, timeout=60)
        self.assertEqual({n: r["rc"] != 0 for n, r in results.items()}, {"alpha-audit": False, "beta-check": True, "gamma-test": False})
        rows = ar.summarize(results, REGISTRY, names)
        self.assertEqual([(r["id"], r["passed"], r["total"]) for r in rows], [("one", 1, 2), ("two", 1, 1)])
        text = ar.render_text(rows, results, names, REGISTRY, scope="regression", jobs=2, elapsed=1.0,
                              only_failing=False, verbose=False, max_lines=12, slowest=0)
        self.assertIn("First group", text)
        self.assertIn("FAIL: beta-check", text)
        self.assertIn("  detail one", text)
        self.assertIn("Result: FAIL (1 gate target failing; 2/3 pass)", text)
        self.assertNotIn("alpha ok", text)

    def test_main_exit_codes_and_json(self) -> None:
        base = ["--root", str(self.root)]
        with contextlib.redirect_stdout(io.StringIO()) as out, contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(ar.main(base + ["--category", "two"]), 0)
            self.assertEqual(ar.main(base), 1)
            self.assertEqual(ar.main(base + ["--category", "nope"]), 2)
            self.assertEqual(ar.main(base + ["--check-registry"]), 0)
            out.truncate(0)
            out.seek(0)
            self.assertEqual(ar.main(base + ["--json", "--category", "one"]), 1)
        data = json.loads(out.getvalue())
        self.assertFalse(data["passed"])
        self.assertEqual(data["targets"]["alpha-audit"]["rc"], 0)
        self.assertIn("excerpt", data["targets"]["beta-check"])

    def test_timeout_is_a_failure_not_a_crash(self) -> None:
        (self.root / "Makefile").write_text(MAKEFILE.replace('@echo "alpha ok"', "@sleep 5"), encoding="utf-8")
        res = ar.run_target(self.root, "alpha-audit", timeout=0.5)
        self.assertEqual(res["rc"], 124)
        self.assertIn("TIMEOUT", res["output"])

    def install_refresh_fixture(self, *, fail: bool = False) -> None:
        text = MAKEFILE.replace("\t\tgamma-test;", "\t\tai-manifest-validate \\\n\t\tgamma-test;")
        text += '\nai-manifest-validate:\n\t@test -f refreshed\n'
        text = text.replace('@echo "gamma ok"', '@touch audited')
        (self.root / "Makefile").write_text(text, encoding="utf-8")
        reg = json.loads(json.dumps(REGISTRY))
        reg["targets"]["ai-manifest-validate"] = {"category": "two", "run": "auto", "writes": False}
        (self.root / ar.REGISTRY_REL).write_text(json.dumps(reg), encoding="utf-8")
        (self.root / "tools/validate_ai_manifests.py").write_text(
            'raise SystemExit("refresh generator failed")' if fail else
            'from pathlib import Path\nPath("refreshed").touch()\nprint("generator output")\n',
            encoding="utf-8",
        )

    def test_refresh_precedes_audits_and_preserves_json_output(self) -> None:
        self.install_refresh_fixture()
        with contextlib.redirect_stdout(io.StringIO()) as out:
            rc = ar.main(["--root", str(self.root), "--category", "two", "--json"])
        self.assertEqual(rc, 0)
        self.assertTrue(json.loads(out.getvalue())["passed"])
        self.assertTrue((self.root / "audited").exists())

    def test_refresh_failure_stops_audits_and_returns_json_failure(self) -> None:
        self.install_refresh_fixture(fail=True)
        with contextlib.redirect_stdout(io.StringIO()) as out:
            rc = ar.main(["--root", str(self.root), "--category", "two", "--json"])
        self.assertEqual(rc, 1)
        self.assertFalse(json.loads(out.getvalue())["passed"])
        self.assertIn("refresh generator failed", out.getvalue())
        self.assertFalse((self.root / "audited").exists())

    def test_inspection_filtered_and_no_refresh_modes_do_not_refresh(self) -> None:
        self.install_refresh_fixture()
        base = ["--root", str(self.root)]
        for flags, expected in [(["--list"], 0), (["--check-registry"], 0),
                                (["--category", "one"], 1),
                                (["--category", "two", "--no-refresh"], 1)]:
            with self.subTest(flags=flags), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(ar.main(base + flags), expected)
                self.assertFalse((self.root / "refreshed").exists())


class ManifestRefreshTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.relative = "ai_corpus/indexes/section_manifest.json"
        self.output = self.root / self.relative
        self.output.parent.mkdir(parents=True)
        self.output.write_text(json.dumps({"files": {}, "generated_at": "old", "stale": True}))
        self.generated = {"files": {}, "generated_at": "new"}
        script = self.root / "generate.py"
        script.write_text(
            'import json, sys\nfrom pathlib import Path\n'
            f'Path(sys.argv[-1]).write_text(json.dumps({self.generated!r}))\n'
        )
        for patcher in [mock.patch.dict(manifests.EXPECTED_OUTPUTS, {"section_manifest": self.relative}, clear=True),
                        mock.patch.dict(manifests.GENERATORS, {"section_manifest": "generate.py"}, clear=True)]:
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_stale_outputs_refresh_and_fresh_outputs_keep_bytes_and_mtime(self) -> None:
        with self.assertRaisesRegex(SystemExit, "stale"):
            manifests.check_freshness(self.root)
        self.assertEqual(manifests.check_freshness(self.root, refresh=True), [self.relative])
        # A timestamp change alone must not rewrite the file.
        self.output.write_text(json.dumps({"files": {}, "generated_at": "different"}))
        before = self.output.read_bytes(), self.output.stat().st_mtime_ns
        self.assertEqual(manifests.check_freshness(self.root, refresh=True), [])
        self.assertEqual((self.output.read_bytes(), self.output.stat().st_mtime_ns), before)

    def test_missing_and_invalid_json_are_rebuilt(self) -> None:
        for contents in [None, "not JSON"]:
            with self.subTest(contents=contents):
                if contents is None:
                    self.output.unlink()
                else:
                    self.output.write_text(contents)
                self.assertEqual(manifests.check_freshness(self.root, refresh=True), [self.relative])
                self.assertEqual(json.loads(self.output.read_text()), self.generated)

    def test_invalid_generated_data_or_generator_failure_preserves_existing_output(self) -> None:
        before = self.output.read_bytes()
        script = self.root / "generate.py"
        script.write_text('import sys\nfrom pathlib import Path\nPath(sys.argv[-1]).write_text("{}")\n')
        with self.assertRaisesRegex(SystemExit, "files object"):
            manifests.check_freshness(self.root, refresh=True)
        self.assertEqual(self.output.read_bytes(), before)
        script.write_text('raise SystemExit("broken generator")\n')
        with self.assertRaises(subprocess.CalledProcessError):
            manifests.check_freshness(self.root, refresh=True)
        self.assertEqual(self.output.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
