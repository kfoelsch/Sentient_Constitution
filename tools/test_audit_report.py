#!/usr/bin/env python3
"""Tests for audit_report (AUDIT-REGISTRY-01)."""

from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import audit_report as ar  # noqa: E402

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


if __name__ == "__main__":
    unittest.main()
