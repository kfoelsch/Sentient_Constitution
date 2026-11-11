#!/usr/bin/env python3
"""Tests for the Implementation widget audit (NAV-IMPL-WIDGET-01)."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import implementation_widget_audit as iwa

CORE = "core_15.000_demo.md"
OWNER_A = "corpus_forum/cf_15.405_alpha.md"
OWNER_B = "corpus_forum/cf_15.410_beta.md"
LINK_A = f"[Alpha rules]({OWNER_A}#cf-15405-alpha-rules)"
LINK_B = f"[Beta rules]({OWNER_B}#cf-15410-beta-rules)"
WIDGET_TOP = '<details>\n<summary><strong>Trace</strong></summary>\n\n- Upstream: x\n\n</details>\n\n<br>\n\n'
WIDGET_TOP_NO_BR = '<details>\n<summary><strong>Trace</strong></summary>\n\n- Upstream: x\n\n</details>\n\n'
SUMMARY = '<summary><strong><span style="color: #2563eb;">Implementation (non-operative)</span></strong></summary>'
HEADING = "## 2. Default venue"


def owner(ident: str, title: str, home: str = "15") -> str:
    return f"# {ident}: {title}\n\nCore home: {home}\n\nBody.\n"


def widget(*links: str) -> str:
    return "<details>\n" + SUMMARY + "\n\n" + "\n".join(f"- {x}" for x in links) + "\n\n</details>\n<br>\n\n"


def core(block: str) -> str:
    return f"# CH\n\n{HEADING}\n\n{WIDGET_TOP}{block}Prose begins.\n"


def run(core_text: str, owners: list[str], write: bool = False, why: str | None = None):
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "tools/architecture").mkdir(parents=True)
        (root / "corpus_forum").mkdir()
        chapters = {"chapters": [{"layer": "CORE", "core_home": "15", "destination_file": CORE}]}
        (root / "tools/architecture/chapter_numbers.json").write_text(json.dumps(chapters), encoding="utf-8")
        (root / OWNER_A).write_text(owner("CF-15.405", "Alpha rules"), encoding="utf-8")
        (root / OWNER_B).write_text(owner("CF-15.410", "Beta rules", home="14"), encoding="utf-8")
        (root / CORE).write_text(core_text, encoding="utf-8")
        unit = {"file": CORE, "heading": "2. Default venue", "owners": owners}
        if why:
            unit["why"] = why
        findings, _ = iwa.audit(root, {"units": [unit]}, write=write)
        return findings, (root / CORE).read_text(encoding="utf-8")


class AuditTests(unittest.TestCase):
    def test_single_owner_inline_passes(self):
        findings, _ = run(core(f"Implementation: {LINK_A}.\n\n"), ["CF-15.405"])
        self.assertEqual(findings, [])

    def test_two_owners_widget_passes(self):
        findings, _ = run(core(widget(LINK_A, LINK_B)), ["CF-15.405", "CF-15.410"], why="shared")
        self.assertEqual(findings, [])

    def test_single_owner_widget_fails(self):
        findings, _ = run(core(widget(LINK_A)), ["CF-15.405"])
        self.assertTrue(any("inline" in f for f in findings))

    def test_two_owners_inline_fails(self):
        findings, _ = run(core(f"Implementation: {LINK_A}; {LINK_B}.\n\n"), ["CF-15.405", "CF-15.410"], why="shared")
        self.assertTrue(any("take a widget" in f for f in findings))

    def test_missing_block_fails(self):
        findings, _ = run(core(""), ["CF-15.405"])
        self.assertTrue(any("missing the inline" in f for f in findings))

    def test_missing_br_fails(self):
        block = widget(LINK_A, LINK_B).replace("</details>\n<br>\n\n", "</details>\n\n")
        findings, _ = run(core(block), ["CF-15.405", "CF-15.410"], why="shared")
        self.assertTrue(any("<br>" in f for f in findings))

    def test_id_label_fails(self):
        block = widget(f"[CF-15.405]({OWNER_A}#cf-15405-alpha-rules)", LINK_B)
        findings, _ = run(core(block), ["CF-15.405", "CF-15.410"], why="shared")
        self.assertTrue(any("is not the file's title" in f for f in findings))

    def test_dead_anchor_fails(self):
        block = widget(f"[Alpha rules]({OWNER_A}#nowhere)", LINK_B)
        findings, _ = run(core(block), ["CF-15.405", "CF-15.410"], why="shared")
        self.assertTrue(any("not a heading or anchor" in f for f in findings))

    def test_order_differs_fails(self):
        findings, _ = run(core(widget(LINK_B, LINK_A)), ["CF-15.405", "CF-15.410"], why="shared")
        self.assertTrue(any("order or target" in f for f in findings))

    def test_wrong_core_home_needs_why(self):
        findings, _ = run(core(widget(LINK_A, LINK_B)), ["CF-15.405", "CF-15.410"])
        self.assertTrue(any("Core home" in f for f in findings))

    def test_widget_above_trace_fails(self):
        text = f"# CH\n\n{HEADING}\n\n{widget(LINK_A, LINK_B)}{WIDGET_TOP}Prose begins.\n"
        findings, _ = run(text, ["CF-15.405", "CF-15.410"], why="shared")
        self.assertTrue(any("last in the opening stack" in f for f in findings))

    def test_unregistered_line_fails(self):
        text = core(f"Implementation: {LINK_A}.\n\n") + f"\nImplementation: {LINK_B}.\n"
        findings, _ = run(text, ["CF-15.405"])
        self.assertTrue(any("not in tools/architecture" in f for f in findings))

    def test_write_inserts_widget_and_line(self):
        findings, text = run(core(""), ["CF-15.405", "CF-15.410"], write=True, why="shared")
        self.assertEqual(findings, [])
        self.assertIn("Implementation (non-operative)", text)
        findings, text = run(core(""), ["CF-15.405"], write=True)
        self.assertEqual(findings, [])
        self.assertIn("Implementation: [Alpha rules]", text)

    def test_write_leaves_no_br_between_stacked_widgets(self):
        findings, text = run(core(""), ["CF-15.405", "CF-15.410"], write=True, why="shared")
        self.assertEqual(findings, [])
        between = text.split("</details>", 1)[1].split("<details>", 1)[0]
        self.assertNotIn("<br>", between)
        self.assertEqual(text.count("<br>"), 1)


if __name__ == "__main__":
    unittest.main()
