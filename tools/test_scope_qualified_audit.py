#!/usr/bin/env python3
"""Tests for SCOPE-QUALIFIED-01 (a bare "scope" with no owner or kind named)."""

from __future__ import annotations

import unittest

from lexical_vocabulary_audit import _mask_inline_code_and_link_targets
from scope_qualified_audit import bare_scope_phrases, scan_text


def phrases(line: str) -> list[str]:
    return bare_scope_phrases(_mask_inline_code_and_link_targets(line))


class ScopeQualifiedTests(unittest.TestCase):
    def test_flags_the_scope(self) -> None:
        self.assertEqual(phrases("The custodian acts for the scope."), ["the scope"])
        self.assertEqual(phrases("Outside that scope, entries may apply alone."), ["that scope"])

    def test_flags_possessive_and_indefinite_use(self) -> None:
        self.assertEqual(phrases("Definitions under this aim inherit its scope."), ["its scope"])
        self.assertEqual(phrases("It lets a scope operate before go-live."), ["a scope"])
        self.assertEqual(phrases("Each part's own scope controls."), ["own scope"])

    def test_flags_generic_modifiers_and_plural(self) -> None:
        self.assertEqual(phrases("Quietly widening the whole scope is a failure."), ["whole scope"])
        self.assertEqual(phrases("Writing a narrow scope is no shelter."), ["narrow scope"])
        self.assertEqual(phrases("The scopes in which a floor is enforceable are listed."), ["the scopes"])

    def test_accepts_a_named_kind(self) -> None:
        self.assertEqual(phrases("The chartered scope is stated."), [])
        self.assertEqual(phrases("The release scope is public."), [])
        self.assertEqual(phrases("The enforceability scope is declared."), [])
        self.assertEqual(phrases("Each cluster states its admission scope."), [])

    def test_accepts_the_field_labels(self) -> None:
        self.assertEqual(phrases("- **In scope:** The point at which a system first operates."), [])
        self.assertEqual(phrases("- **Out of scope:** A pilot."), [])
        self.assertEqual(phrases("- **Admission scope:** privacy matters."), [])
        self.assertEqual(phrases("It applies in scope and not out of scope."), [])

    def test_accepts_scope_of_or_for(self) -> None:
        self.assertEqual(phrases("It fixes the scope of the Charter."), [])
        self.assertEqual(phrases("Time is set aside for a scope for review."), [])

    def test_accepts_a_pointer_or_relative_clause(self) -> None:
        self.assertEqual(phrases("Evaluate within the scope above."), [])
        self.assertEqual(phrases("Inside the scope each cluster states, it applies."), [])
        self.assertEqual(phrases("It applies to the scope it is supervised under."), [])
        self.assertEqual(phrases("Only within the scope that was actually adopted."), [])

    def test_accepts_scope_as_a_modifier(self) -> None:
        self.assertEqual(phrases("A published scope document names the seats."), [])
        self.assertEqual(phrases("Decisions need a scope cap and an expiry."), [])
        self.assertEqual(phrases("No scope creep is allowed."), [])

    def test_accepts_class_letter_and_emphasis_markers(self) -> None:
        self.assertEqual(phrases("At Class A scope, full separation is required."), [])
        self.assertEqual(phrases("It fails if Class A scope lacks independent participation."), [])
        self.assertEqual(phrases("- the **scope** of restriction"), [])
        self.assertEqual(phrases("A scope is declared."), ["a scope"])

    def test_accepts_the_verb_and_unmodified_use(self) -> None:
        self.assertEqual(phrases("They must scope the review in advance."), [])
        self.assertEqual(phrases("Under what scope and durable terms authority is held."), [])
        self.assertEqual(phrases("Facts within scope are checked."), [])

    def test_ignores_inline_code_and_link_targets(self) -> None:
        self.assertEqual(phrases("It rests on `the scope` and [the rule](core_13.000_the_scope.md)."), [])

    def test_scan_skips_fences_and_exempt_file(self) -> None:
        text = "```\nThe custodian acts for the scope.\n```\nThe custodian acts for the scope.\n"
        found = scan_text("core_11.000_standing_assessment.md", text)
        self.assertEqual([f.line for f in found], [4])
        self.assertEqual(scan_text("doc_architecture.md", "The custodian acts for the scope.\n"), [])

    def test_chapter_five_is_not_exempt(self) -> None:
        found = scan_text("core_05.040_band_continuity.md", "Outside that scope, entries apply.\n")
        self.assertEqual([f.line for f in found], [1])


if __name__ == "__main__":
    unittest.main()
