#!/usr/bin/env python3
"""Tests for section-label / current-numbering fragment ids."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from section_label_anchor_audit import (
    RULE_CITE,
    RULE_SEQ,
    audit,
    compact,
    heading_sequence_errors,
    hyphenated,
    id_matches_current,
    parse_clusters,
    parse_heading_index,
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

    def test_section_label_mismatch_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "core_14_expansion_supremacy.md").write_text(
                "### 3. Anti-Evasion Clause and Constitutional-Misconduct Referral\n\n"
                "[§11](#3-anti-evasion-clause-and-constitutional-misconduct-referral)\n",
                encoding="utf-8",
            )
            errors = audit(root)
            self.assertTrue(
                any(RULE_CITE in err and "prose §11" in err for err in errors),
                msg="\n".join(errors),
            )

    def test_matching_section_label_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "core_14_expansion_supremacy.md").write_text(
                "### 3. Anti-Evasion Clause and Constitutional-Misconduct Referral\n\n"
                "[§3](#3-anti-evasion-clause-and-constitutional-misconduct-referral)\n",
                encoding="utf-8",
            )
            errors = audit(root)
            self.assertEqual(
                [err for err in errors if RULE_CITE in err or "current-numbering" in err],
                [],
                msg="\n".join(errors),
            )

    def test_missing_fragment_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "core_14_expansion_supremacy.md").write_text(
                "### 3. Anti-Evasion Clause\n\n"
                "[§3](#3-does-not-exist)\n",
                encoding="utf-8",
            )
            errors = audit(root)
            self.assertTrue(
                any("fragment is absent" in err and RULE_CITE in err for err in errors),
                msg="\n".join(errors),
            )

    def test_duplicate_sibling_headings_are_reported(self) -> None:
        _, numbered = parse_heading_index(
            "### 3. Supremacy\n"
            "#### 3.16 Internal Hierarchy\n"
            "#### 3.16 Stricter External\n"
            "#### 3.3 Conflict Disclosure\n"
        )
        errors = heading_sequence_errors("core_14_expansion_supremacy.md", numbered)
        self.assertTrue(
            any("duplicate heading §3.16" in err and RULE_SEQ in err for err in errors),
            msg="\n".join(errors),
        )
        self.assertTrue(
            any("non-consecutive" in err and RULE_SEQ in err for err in errors),
            msg="\n".join(errors),
        )

    def test_consecutive_subsections_pass_sequence(self) -> None:
        _, numbered = parse_heading_index(
            "### 3. Supremacy Relative to Other Binding Norms\n"
            "#### 3.1 Internal Hierarchy for Adopters\n"
            "#### 3.2 Stricter External Protections\n"
            "#### 3.3 Conflict Disclosure and Mitigation\n"
        )
        errors = heading_sequence_errors("core_14_expansion_supremacy.md", numbered)
        self.assertEqual(errors, [], msg="\n".join(errors))

    def test_repo_audit_passes(self) -> None:
        errors = audit(ROOT)
        self.assertEqual(errors, [], msg="\n".join(errors))


if __name__ == "__main__":
    unittest.main()
