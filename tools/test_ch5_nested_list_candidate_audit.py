#!/usr/bin/env python3
"""Tests for the Chapter Five nested-list candidate finder."""

from __future__ import annotations

import unittest
from io import StringIO
from pathlib import Path
from unittest.mock import patch

_TOOLS = Path(__file__).resolve().parent
import sys

if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_nested_list_candidate_audit import (  # noqa: E402
    main,
    scan_text,
)


class NestedListCandidateTests(unittest.TestCase):
    def _lines(self, text: str, *, min_score: int = 8) -> list[int]:
        return [item.line for item in scan_text(text, min_score=min_score)]

    def test_packed_semicolon_failure_is_flagged(self) -> None:
        text = """#### Stay

- **What it is**
  - **In scope:** A pause.
<a id="stay-c"></a>
- **What must hold**
  - **Primary failure:** It is non-compliant to use informal delay; keep a Stay indefinite; block contestability; treat a Stay as final approval; label a merits ruling as a Stay; or refuse to lift it.
"""
        hits = scan_text(text)
        self.assertEqual(self._lines(text), [7])
        self.assertEqual(hits[0].role, "primary-failure")
        self.assertTrue(any(k.startswith("semicolons:") for k in hits[0].kinds))
        self.assertIn("nested bullets", hits[0].recommendation)

    def test_nested_children_are_not_flagged(self) -> None:
        text = """#### Remedy System

- **What must hold**
  - **Primary failure:** It is non-compliant to:
    - run paper-only pathways;
    - leave trauma unresolved; or
    - treat ownership of standards as command authority.
"""
        self.assertEqual(scan_text(text), [])

    def test_colon_intro_without_children_is_flagged(self) -> None:
        text = """#### Harm

- **What it is**
  - **In scope:** Material worsening of protected conditions. This includes:
"""
        hits = scan_text(text)
        self.assertEqual(len(hits), 1)
        self.assertIn("colon-intro", hits[0].kinds)
        self.assertEqual(hits[0].recommendation, "Nest the list this line introduces.")

    def test_colon_intro_with_children_is_not_flagged(self) -> None:
        text = """#### Harm

- **What it is**
  - **In scope:** Material worsening of protected conditions. This includes:
    - delayed harm;
    - indirect harm; and
    - system-wide harm.
"""
        self.assertEqual(scan_text(text), [])

    def test_skips_details_trace_lists(self) -> None:
        text = """#### Stay

<details>
<summary>Trace</summary>

- Read with: notice; chance to be heard; reasons; impartial structures; contest path; and traceability.

</details>

- **What it is**
  - **In scope:** A temporary pause.
"""
        self.assertEqual(scan_text(text), [])

    def test_skips_primary_measure_boilerplate(self) -> None:
        text = """#### Feasibility

- **How to measure and assess**
  - **Primary measure:** Accountability measurement family and Timeliness measurement family — used alongside any other relevant measures to assess responsibility and whether action happens without harmful delay; also check backlog; capture; and delay.
"""
        self.assertEqual(scan_text(text), [])

    def test_skips_short_out_of_scope(self) -> None:
        text = """#### Feasibility

- **What it is**
  - **Out of scope:** theoretical possibility talk with no required action.
"""
        self.assertEqual(scan_text(text), [])

    def test_packed_assessment_continuation_is_flagged(self) -> None:
        text = """#### Collective Accountability Failure

- **How to measure and assess**
  - **Primary measure:** Accountability measurement family.

    **Primary assessment:** For each role, assess duty; knowledge; ability to resist or escalate; command and dependency structure; documented response pathways; and whether actors used contestability when they faced unlawful directives.
"""
        hits = scan_text(text)
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0].role, "primary-assessment")
        self.assertTrue(any(k.startswith("semicolons:") for k in hits[0].kinds))

    def test_assessment_with_nested_list_is_not_flagged(self) -> None:
        text = """#### Adjudication and Dispute Resolution

- **How to measure and assess**
  - **Primary measure:** Accountability measurement family.

    **Primary assessment:**
    - Apply due process.
    - Requirements for access are governed here.
    - Owner-layer procedures must not narrow this definition.
"""
        self.assertEqual(scan_text(text), [])

    def test_guidepost_header_is_skipped(self) -> None:
        text = """#### Feasibility

- **What it is**
"""
        self.assertEqual(scan_text(text, min_score=1), [])

    def test_including_list_is_flagged(self) -> None:
        text = """#### Good Faith

- **What it is**
  - **In scope:** Honest purpose in the constitutional settings where Good Faith is required, including publication under Article VIII, participation in audits, and cooperation with Oversight when disclosure duties apply. It means sincerely trying to align conduct with stated facts, applicable rules, and epistemic integrity.
"""
        hits = scan_text(text)
        self.assertEqual(len(hits), 1)
        self.assertIn("including-list", hits[0].kinds)

    def test_or_chain_failure_is_flagged(self) -> None:
        text = """#### Due Process

- **What must hold**
  - **Primary failure:** It is non-compliant to decide a materially impactful outcome without timely notice, a meaningful chance to be heard, understandable reasons, impartial or appropriately independent structures where adjudication applies, a way to contest or seek secondary review, or traceability under Chapters Two through Four. A due-process label or procedure that exists only on paper and has no real effect in the situation being evaluated is also non-compliant.
"""
        hits = scan_text(text)
        self.assertEqual(len(hits), 1)
        self.assertIn("or-chain", hits[0].kinds)

    def test_pointer_line_is_skipped(self) -> None:
        text = """#### Standing Record

- **What it is**
  - Chapter Five pointer; canonical concept: Chapter Eight §2.1; operational requirements: Chapter Eight §3.
"""
        self.assertEqual(scan_text(text), [])

    def test_min_score_filters(self) -> None:
        text = """#### Stay

- **What must hold**
  - **Primary failure:** It is non-compliant to use informal delay; keep a Stay indefinite; block contestability; treat a Stay as final approval; label a merits ruling as a Stay; or refuse to lift it.
"""
        self.assertTrue(scan_text(text, min_score=8))
        self.assertEqual(scan_text(text, min_score=99), [])

    def test_main_advisory_exit_zero(self) -> None:
        buf = StringIO()
        with patch("sys.stdout", buf):
            code = main(
                [
                    "--root",
                    str(_TOOLS.parent),
                    "--file",
                    "core_05_band_accountability.md",
                    "--top",
                    "3",
                ]
            )
        self.assertEqual(code, 0)
        self.assertIn("CH5-NEST-CANDIDATE", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
