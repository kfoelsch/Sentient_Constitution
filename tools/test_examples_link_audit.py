#!/usr/bin/env python3
"""Tests for the worked-example link audit (EXAMPLES-LINK-01)."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import examples_link_audit as ela

EXAMPLE = "corpus_systems/cs_09.320_illustrations.md"
CORE = "core_09.000_demo.md"
REGISTRY = {"files": {EXAMPLE: {"illustrates": [CORE]}}}
TRACE_LINK = f"- Worked examples (they add no rule): [CS-9.320]({EXAMPLE}#x)."
CLOSING = f"*Worked examples (they add no rule):* [CS-9.320]({EXAMPLE}#x)."
FOOTER = "---\n\n**Previous file:** [a.md](a.md)\n\n**Next file:** [b.md](b.md)\n"


def core(trace_bullet: str = TRACE_LINK, closing: str = CLOSING, footer: str = FOOTER) -> str:
    return (
        "# CHAPTER\n\n<details>\n<summary><strong>Trace</strong></summary>\n\n"
        f"- Upstream: x\n{trace_bullet}\n\n</details>\n\n<br>\n\nBody.\n\n{closing}\n\n{footer}"
    )


class AuditTests(unittest.TestCase):
    def run_audit(self, core_text: str, example_text: str = f"[back](../{CORE})\n") -> list[str]:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "corpus_systems").mkdir()
            (root / EXAMPLE).write_text(example_text, encoding="utf-8")
            (root / CORE).write_text(core_text, encoding="utf-8")
            return ela.audit(root, REGISTRY)

    def test_complete_chapter_passes(self):
        example = f"# X\n\n<a id=\"x\"></a>\n\n[back](../{CORE})\n"
        self.assertEqual(self.run_audit(core(), example_text=example), [])

    def test_missing_trace_link_fails(self):
        findings = self.run_audit(core(trace_bullet="- Read with: y"))
        self.assertTrue(any("Trace widget needs a link" in f for f in findings))

    def test_missing_closing_line_fails(self):
        findings = self.run_audit(core(closing=""))
        self.assertTrue(any("needs a closing" in f for f in findings))

    def test_closing_line_below_footer_does_not_count(self):
        text = core(closing="", footer=FOOTER + "\n" + CLOSING + "\n")
        self.assertTrue(any("needs a closing" in f for f in self.run_audit(text)))

    def test_closing_line_inside_widget_does_not_count(self):
        text = core(closing="").replace("</details>", f"{CLOSING}\n\n</details>", 1)
        self.assertTrue(any("needs a closing" in f for f in self.run_audit(text)))

    def test_example_without_link_back_fails(self):
        findings = self.run_audit(core(), example_text="no link here\n")
        self.assertTrue(any("no link back" in f for f in findings))

    def test_unregistered_chapter_with_one_sided_link_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "corpus_systems").mkdir()
            (root / EXAMPLE).write_text(f"[back](../{CORE})\n", encoding="utf-8")
            (root / CORE).write_text(core(), encoding="utf-8")
            (root / "core_20.000_other.md").write_text(core(closing=""), encoding="utf-8")
            findings = ela.audit(root, REGISTRY)
        self.assertTrue(any(f.startswith("core_20.000_other.md") and "no closing" in f for f in findings))

    def test_dead_anchor_into_example_file_fails(self):
        text = core().replace(f"{EXAMPLE}#x", f"{EXAMPLE}#no-such-heading")
        example = f"# Real heading\n\n[back](../{CORE})\n"
        findings = self.run_audit(text, example_text=example)
        self.assertTrue(any("not a heading or anchor" in f for f in findings))

    def test_live_anchor_passes(self):
        text = core().replace(f"{EXAMPLE}#x", f"{EXAMPLE}#real-heading")
        example = f"# Real heading\n\n[back](../{CORE})\n"
        self.assertEqual(self.run_audit(text, example_text=example), [])

    def test_file_without_footer_uses_end_of_file(self):
        example = f"# X\n\n<a id=\"x\"></a>\n\n[back](../{CORE})\n"
        self.assertEqual(self.run_audit(core(footer=""), example_text=example), [])


if __name__ == "__main__":
    unittest.main()
