#!/usr/bin/env python3
"""Tests for Chapter Nine inbound-fragment source coverage."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from local_markdown_fragment_audit import audit, source_files


class LocalMarkdownFragmentAuditTests(unittest.TestCase):
    def test_default_scope_includes_implementation_and_generated_docs(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = root / "core_09-09_standing_integration.md"
            target.write_text(
                '<a id="present"></a>\n# Chapter Nine\n',
                encoding="utf-8",
            )

            implementation = root / "implementation" / "guide.md"
            implementation.parent.mkdir()
            implementation.write_text(
                "[broken](../core_09-09_standing_integration.md#missing-implementation)\n",
                encoding="utf-8",
            )

            generated = root / "doc_architecture" / "generated" / "index.md"
            generated.parent.mkdir(parents=True)
            generated.write_text(
                "[broken](../../core_09-09_standing_integration.md#missing-generated)\n",
                encoding="utf-8",
            )

            paths = source_files(root)
            self.assertIn(implementation, paths)
            self.assertIn(generated, paths)

            findings = audit(root, paths, target.resolve())
            self.assertEqual(
                {finding.source for finding in findings},
                {
                    "implementation/guide.md",
                    "doc_architecture/generated/index.md",
                },
            )


if __name__ == "__main__":
    unittest.main()
