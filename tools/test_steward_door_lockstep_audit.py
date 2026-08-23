#!/usr/bin/env python3
"""Tests for steward-door lockstep helpers and failure modes."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from steward_door_lockstep_audit import (
    CARD_BOX_ANCHORS,
    CARD_TITLES,
    DUTY_STEPS,
    INDEX_REL,
    ROUTING_REL,
    SCHEMA_REL,
    audit,
    card_next_step_classes,
    check_href,
    duty_steps_in_order,
    parse_operative_boxes,
    parse_routing_examples,
)

ROOT = Path(__file__).resolve().parents[1]


class StewardDoorLockstepTests(unittest.TestCase):
    def test_real_cards_parse_routing_examples(self) -> None:
        routing = (ROOT / ROUTING_REL).read_text(encoding="utf-8")
        rows = parse_routing_examples(routing)
        ids = [row["id"] for row in rows]
        self.assertIn("standing_record", ids)
        self.assertIn("emergency", ids)
        self.assertIn("unlawful_instruction", ids)
        emergency = next(row for row in rows if row["id"] == "emergency")
        self.assertEqual(
            emergency["klass"],
            "time_boxed_containment_with_deferred_participation",
        )
        self.assertEqual(emergency["anchor"], "emergency")
        cards = (ROOT / "implementation" / "STEWARD_ENTRY_DOORS.md").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("## Routing examples", cards)

    def test_card_next_step_classes_reads_both_standing_classes(self) -> None:
        body = (
            "| **Next-step class** | `open_or_correct_standing_record` — fix. "
            "If concealment: `accept_standing_measurement_and_disclosure_duties`. |\n"
        )
        self.assertEqual(
            card_next_step_classes(body),
            [
                "open_or_correct_standing_record",
                "accept_standing_measurement_and_disclosure_duties",
            ],
        )

    def test_duty_steps_must_appear_in_order(self) -> None:
        self.assertTrue(
            duty_steps_in_order(
                "Instruction received. Refuse. Document. Escalate."
            )
        )
        self.assertFalse(
            duty_steps_in_order("Refuse, then maybe document the instruction.")
        )
        self.assertEqual(len(DUTY_STEPS), 4)

    def test_named_stack_titles_cover_common_fact_patterns(self) -> None:
        self.assertIn("Contest", CARD_TITLES)
        self.assertIn("Incentive alignment", CARD_TITLES)
        self.assertIn("Unlawful instruction", CARD_TITLES)
        self.assertIn("Shared stewardship", CARD_TITLES)
        self.assertIn("Proceed", CARD_TITLES)
        self.assertIn("Interpretation", CARD_TITLES)
        self.assertIn("Comprehensibility", CARD_TITLES)
        self.assertIn("Market structure", CARD_TITLES)
        self.assertIn("Cross-system contribution", CARD_TITLES)
        self.assertIn("Delay", CARD_TITLES)

    def test_broken_href_fragment_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = root / "core_example.md"
            target.write_text(
                '<a id="live"></a>\n# Example\n',
                encoding="utf-8",
            )
            cache: dict[Path, set[str]] = {}
            errors = check_href(
                root,
                "core_example.md#missing",
                "test",
                cache,
            )
            self.assertTrue(errors)
            self.assertTrue(any("missing" in err for err in errors))
            ok = check_href(root, "core_example.md#live", "test", cache)
            self.assertEqual(ok, [])

    def test_parse_operative_boxes_extracts_owner_forbidden_clock(self) -> None:
        text = (
            '<a id="operative-steward-statement-standing"></a>\n'
            "> **Operative steward statement.** **Owner:** Chapter Eight. "
            "**Forbidden move:** Do not wait. **Clock:** Correct the record now.\n"
        )
        boxes = parse_operative_boxes(text)
        self.assertIn("operative-steward-statement-standing", boxes)
        parsed = boxes["operative-steward-statement-standing"]
        self.assertEqual(parsed["owner"], "Chapter Eight.")
        self.assertEqual(parsed["forbidden_move"], "Do not wait.")
        self.assertEqual(parsed["clock"], "Correct the record now.")

    def test_clauses_split_lets_combined_boxes_match_cards(self) -> None:
        from steward_door_lockstep_audit import missing_clauses, normalize

        haystack = normalize(
            "Do not skip notice. Extra sentence. Do not stretch feasible. "
            "Do not block a deferral."
        )
        self.assertEqual(
            missing_clauses(
                "Do not skip notice. Do not stretch feasible. Do not block a deferral.",
                haystack,
            ),
            [],
        )

    def test_named_stack_titles_have_core_box_anchors(self) -> None:
        self.assertEqual(set(CARD_BOX_ANCHORS), set(CARD_TITLES))

    def test_schema_and_index_exist(self) -> None:
        self.assertTrue((ROOT / INDEX_REL).is_file())
        self.assertTrue((ROOT / SCHEMA_REL).is_file())
        index = json.loads((ROOT / INDEX_REL).read_text(encoding="utf-8"))
        self.assertTrue(index["cannot_narrow_core"])
        self.assertEqual(index["status"], "process_support_not_binding")
        self.assertTrue(
            all("operative_box" in case for case in index.get("cases") or [])
        )

    def test_repo_audit_passes(self) -> None:
        errors = audit(ROOT)
        self.assertEqual(errors, [], msg="\n".join(errors))


if __name__ == "__main__":
    unittest.main()
