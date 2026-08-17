#!/usr/bin/env python3
"""Tests for NAV-PRE-RELEASE-FRAGMENT-01 leftover fragment pruning."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from fossil_anchor_audit import collect_prunes, remaining_citations

ROOT = Path(__file__).resolve().parents[1]


class FossilAnchorAuditTests(unittest.TestCase):
    def test_dual_ids_are_pruned_to_current(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "core_09-09_standing_integration.md").write_text(
                "<a id=\"411-duty-to-resist-unlawful-or-unconstitutional-instructions\"></a>\n"
                "<a id=\"54-duty-to-resist-unlawful-or-unconstitutional-instructions\"></a>\n"
                "#### 5.4 Duty to resist unlawful or unconstitutional instructions\n",
                encoding="utf-8",
            )
            (root / "core_01_c_stewardship_capacity_principles.md").write_text(
                "[Chapter Nine §5.4](core_09-09_standing_integration.md"
                "#411-duty-to-resist-unlawful-or-unconstitutional-instructions)\n",
                encoding="utf-8",
            )
            impl = root / "implementation"
            impl.mkdir()
            (impl / "index.json").write_text(
                '{\n  "href": "core_09-09_standing_integration.md'
                '#411-duty-to-resist-unlawful-or-unconstitutional-instructions"\n}\n',
                encoding="utf-8",
            )
            prunes = collect_prunes(root)
            self.assertTrue(
                any(
                    item.fossil
                    == "411-duty-to-resist-unlawful-or-unconstitutional-instructions"
                    and item.current
                    == "54-duty-to-resist-unlawful-or-unconstitutional-instructions"
                    for item in prunes
                ),
                msg=repr(prunes),
            )
            leftovers = remaining_citations(root, prunes)
            self.assertTrue(
                any("core_01_c_stewardship_capacity_principles.md" in item for item in leftovers),
                msg="\n".join(leftovers),
            )
            self.assertTrue(
                any("implementation/index.json" in item for item in leftovers),
                msg="\n".join(leftovers),
            )

    def test_repo_has_no_leftover_fragments(self) -> None:
        prunes = collect_prunes(ROOT)
        leftovers = remaining_citations(ROOT, prunes)
        self.assertEqual(prunes, [], msg="\n".join(f"{p.file}: #{p.fossil}" for p in prunes))
        self.assertEqual(leftovers, [], msg="\n".join(leftovers))


if __name__ == "__main__":
    unittest.main()
