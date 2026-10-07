#!/usr/bin/env python3
"""Tests that the readability audit scores prose only, not markup."""

from __future__ import annotations

import unittest

from readability_audit import prose_lines, split_sentences_with_lines

SAMPLE = """<a id="32-example"></a>
#### 3.2 Example Heading
<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [Chapter One §12 Systemic Evaluation Requirement](core_01_b_interaction_interpretation.md#12-systemic-evaluation-requirement).
</details>

```mermaid
flowchart TD
  A1[Certification accountability] --> B2
```

| Col | Col |
|---|---|
See `make regression`, <https://example.org>, and https://example.org/a/b.
<!-- a hidden
comment -->
Done."""


class ProseLinesTests(unittest.TestCase):
    def test_line_count_is_preserved(self) -> None:
        self.assertEqual(len(prose_lines(SAMPLE)), len(SAMPLE.splitlines()))

    def test_link_target_dropped_and_link_text_kept(self) -> None:
        lines = prose_lines(SAMPLE)
        self.assertIn("Chapter One §12 Systemic Evaluation Requirement", lines[5])
        self.assertNotIn("core_01_b", lines[5])
        self.assertNotIn("interaction", lines[5])

    def test_markup_contributes_no_words(self) -> None:
        words = " ".join(s for _, s in split_sentences_with_lines(SAMPLE))
        for markup_word in ("mermaid", "flowchart", "summary", "span", "color",
                            "regression", "example", "hidden", "comment", "Trace"):
            self.assertNotIn(markup_word, words)

    def test_headings_are_not_sentences(self) -> None:
        sentences = [s for _, s in split_sentences_with_lines(SAMPLE)]
        self.assertFalse(any("Example Heading" in s for s in sentences))

    def test_findings_keep_source_line_numbers(self) -> None:
        lines = dict((s, n) for n, s in split_sentences_with_lines(SAMPLE))
        self.assertEqual(lines["Done."], len(SAMPLE.splitlines()))


if __name__ == "__main__":
    unittest.main()
