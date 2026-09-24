#!/usr/bin/env python3
"""Tests for the anchor/heading drift audit."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from anchor_heading_drift_audit import scan


class AnchorHeadingDriftTests(unittest.TestCase):
    def scan_text(self, text: str) -> list:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "core_00_preamble.md").write_text(text, encoding="utf-8")
            return scan(root, ["core_00_preamble.md"])

    def test_drifted_name_is_reported(self) -> None:
        findings = self.scan_text(
            '<a id="345-chapter-eleven-floor-boundary"></a>\n\n'
            "#### 3.4.5 Rights-Floor Boundary\n"
        )
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].expected, "345-rights-floor-boundary")

    def test_matching_anchor_is_clean(self) -> None:
        self.assertEqual(
            self.scan_text(
                '<a id="345-rights-floor-boundary"></a>\n\n'
                "#### 3.4.5 Rights-Floor Boundary\n"
            ),
            [],
        )

    def test_alias_set_is_left_alone(self) -> None:
        """Stacked anchors keep older links alive and are deliberate."""
        self.assertEqual(
            self.scan_text(
                '<a id="4-old-name"></a>\n<a id="4-newer-name"></a>\n\n'
                "### 4. Newest Name\n"
            ),
            [],
        )

    def test_duplicate_headings_are_left_alone(self) -> None:
        """Two sections share a title, so their anchors must differ."""
        self.assertEqual(
            self.scan_text(
                '<a id="1-tetrad-leg-decomposition"></a>\n\n'
                "### Tetrad Leg decomposition\n\n"
                '<a id="2-tetrad-leg-decomposition"></a>\n\n'
                "### Tetrad Leg decomposition\n"
            ),
            [],
        )

    def test_semantic_ids_are_left_alone(self) -> None:
        """An unnumbered id like oversight-constitutional is intentional."""
        self.assertEqual(
            self.scan_text('<a id="oversight-constitutional"></a>\n\n#### Oversight\n'),
            [],
        )

    def test_renumbered_section_is_not_treated_as_a_rename(self) -> None:
        """A different section number means a move, which this rule does not judge."""
        self.assertEqual(
            self.scan_text('<a id="91-stewardship"></a>\n\n### 9. Stewardship\n'),
            [],
        )

    def test_heading_slug_present_among_aliases_is_clean(self) -> None:
        self.assertEqual(
            self.scan_text(
                '<a id="2-the-measurements"></a>\n'
                '<a id="2-measurements-overview"></a>\n\n'
                "### 2. Measurements Overview\n"
            ),
            [],
        )


if __name__ == "__main__":
    unittest.main()
