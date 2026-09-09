#!/usr/bin/env python3
"""Tests for section-label / current-numbering fragment ids."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from section_label_anchor_audit import (
    audit,
    compact,
    hyphenated,
    id_matches_current,
    parse_clusters,
)

ROOT = Path(__file__).resolve().parents[1]


class SectionLabelAnchorTests(unittest.TestCase):
    def test_compact_and_hyphenated_forms(self) -> None:
        self.assertEqual(compact("5.4"), "54")
        self.assertEqual(hyphenated("5.4"), "5-4")
        self.assertTrue(
            id_matches_current(
                "54-duty-to-resist-unlawful-or-unconstitutional-instructions",
                "5.4",
            )
        )
        self.assertTrue(
            id_matches_current(
                "4-3-voluntary-public-accountability-expression",
                "4.3",
            )
        )
        self.assertFalse(
            id_matches_current(
                "411-duty-to-resist-unlawful-or-unconstitutional-instructions",
                "5.4",
            )
        )
        self.assertFalse(id_matches_current("11-two-question", "1"))

    def test_named_rule_under_parent_inherits_section_number(self) -> None:
        text = (
            "<a id=\"54-special-violation-rules\"></a>\n"
            "#### 5.4 Special violation rules\n\n"
            "<a id=\"411-duty-to-resist-unlawful-or-unconstitutional-instructions\"></a>\n"
            "**Duty to resist.**\n"
        )
        clusters = parse_clusters(text)
        info = clusters["411-duty-to-resist-unlawful-or-unconstitutional-instructions"]
        self.assertEqual(info["current"], "5.4")
        self.assertEqual(
            info["ids"],
            ["411-duty-to-resist-unlawful-or-unconstitutional-instructions"],
        )

    def test_missing_alias_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "core_09_standing_integration.md").write_text(
                "<a id=\"54-special-violation-rules\"></a>\n"
                "#### 5.4 Special violation rules\n\n"
                "<a id=\"411-duty-to-resist-unlawful-or-unconstitutional-instructions\"></a>\n"
                "**Duty to resist.**\n",
                encoding="utf-8",
            )
            citing = root / "core_01_c_stewardship_capacity_principles.md"
            citing.write_text(
                "[Chapter Nine §5.4 Duty to resist]"
                "(core_09_standing_integration.md"
                "#411-duty-to-resist-unlawful-or-unconstitutional-instructions)\n",
                encoding="utf-8",
            )
            errors = audit(root)
            self.assertTrue(errors, msg="expected a missing-alias finding")
            self.assertTrue(
                any("current-numbering alias" in err for err in errors),
                msg="\n".join(errors),
            )

    def test_current_numbering_id_satisfies_section_label(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "core_09_standing_integration.md").write_text(
                "<a id=\"54-special-violation-rules\"></a>\n"
                "#### 5.4 Special violation rules\n\n"
                "<a id=\"54-duty-to-resist-unlawful-or-unconstitutional-instructions\"></a>\n"
                "**Duty to resist.**\n",
                encoding="utf-8",
            )
            (root / "core_01_c_stewardship_capacity_principles.md").write_text(
                "[Chapter Nine §5.4 Duty to resist]"
                "(core_09_standing_integration.md"
                "#54-duty-to-resist-unlawful-or-unconstitutional-instructions)\n",
                encoding="utf-8",
            )
            errors = audit(root)
            self.assertEqual(errors, [], msg="\n".join(errors))

    def test_repo_audit_passes(self) -> None:
        errors = audit(ROOT)
        self.assertEqual(errors, [], msg="\n".join(errors))


if __name__ == "__main__":
    unittest.main()
