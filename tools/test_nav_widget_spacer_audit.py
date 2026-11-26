#!/usr/bin/env python3
"""Tests for the widget spacer audit (NAV-DAC-12-SPACER)."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import nav_widget_spacer_audit as nwsa

TRACE = '<details>\n<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>\n\n- Upstream: x\n\n</details>'
OTHER = '<details>\n<summary><strong><span style="color: #2563eb;">Implementation (non-operative)</span></strong></summary>\n\n- x\n\n</details>'
DEC_SUMMARY = '<summary><strong><span style="color: #2563eb;">Definitions (O · M · A · C)</span></strong></summary>'


def dec_widget(*, blank_after: bool = True, blank_before_close: bool = True) -> str:
    after = "\n" if blank_after else ""
    before = "\n\n" if blank_before_close else "\n"
    return f"<details>\n{DEC_SUMMARY}\n{after}- [Term](subcore.md#term){before}</details>"


def findings(body: str) -> list[str]:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        path = root / "core_99.000_demo.md"
        path.write_text(body, encoding="utf-8")
        return nwsa.audit_file(path, root)


class SpacerTests(unittest.TestCase):
    def test_stack_with_one_br_after_last_passes(self):
        self.assertEqual(findings(f"# H\n\n{TRACE}\n\n{OTHER}\n<br>\n\nProse.\n"), [])

    def test_br_between_stacked_widgets_fails(self):
        out = findings(f"# H\n\n{TRACE}\n\n<br>\n\n{OTHER}\n<br>\n\nProse.\n")
        self.assertTrue(any("between stacked widgets" in f for f in out))

    def test_missing_br_after_last_widget_fails(self):
        out = findings(f"# H\n\n{TRACE}\n\nProse.\n")
        self.assertTrue(any("missing <br>" in f for f in out))

    def test_definitions_widget_with_markdown_boundaries_passes(self):
        self.assertEqual(findings(f"# H\n\n{dec_widget()}\n<br>\n"), [])

    def test_missing_blank_after_definitions_summary_fails(self):
        out = findings(f"# H\n\n{dec_widget(blank_after=False)}\n<br>\n")
        self.assertTrue(any("blank line after the O/M/A/C summary" in f for f in out))

    def test_missing_blank_before_definitions_close_fails(self):
        out = findings(f"# H\n\n{dec_widget(blank_before_close=False)}\n<br>\n")
        self.assertTrue(any("blank line before </details>" in f for f in out))


if __name__ == "__main__":
    unittest.main()
