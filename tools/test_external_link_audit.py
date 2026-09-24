#!/usr/bin/env python3
"""Tests for LINK-OFF-CORPUS-15 off-corpus and machine-local link detection."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from external_link_audit import audit, extract_links, machine_local_reason

ROOT = Path(__file__).resolve().parents[1]

VSCODE_PREVIEW = (
    "https://file+.vscode-resource.vscode-cdn.net/Users/someone/Documents/"
    "Sentient_Constitution/README.md#standing-pipeline-and-forums"
)


def write(root: Path, rel: str, text: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class ExternalLinkAuditTests(unittest.TestCase):
    def test_binding_corpus_rejects_absolute_and_root_targets(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write(
                root,
                "core_06_rights_part_a.md",
                "- Downstream: [README](README.md#standing-pipeline-and-forums).\n"
                "- Read with: [§1.2 Layer scope](#12-layer-scope).\n"
                "- Source: [spec](https://example.org/spec).\n"
                "- Path: [local](/etc/hosts).\n",
            )
            findings, _ = audit(root)
            self.assertEqual(len(findings), 2, msg="\n".join(findings))
            self.assertTrue(any("https: URL" in item for item in findings), findings)
            self.assertTrue(any("root-absolute path" in item for item in findings), findings)
            self.assertFalse(any(":1:" in item for item in findings), findings)
            self.assertFalse(any(":2:" in item for item in findings), findings)

    def test_support_document_keeps_external_citation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write(root, "README.md", "See [the archive](https://web.archive.org/x).\n")
            findings, external = audit(root)
            self.assertEqual(findings, [])
            self.assertEqual(len(external), 1)

    def test_editor_preview_url_is_caught_everywhere(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write(root, "README.md", f"[README]({VSCODE_PREVIEW})\n")
            write(root, "core_12_forum.md", f"[README]({VSCODE_PREVIEW})\n")
            findings, _ = audit(root)
            self.assertEqual(len(findings), 2, msg="\n".join(findings))
            self.assertTrue(all("editor preview URL" in item for item in findings), findings)

    def test_machine_local_shapes(self) -> None:
        for target in (
            "file:///Users/someone/notes.md",
            "/Users/someone/Documents/x.md",
            "~/Documents/x.md",
            "C:\\Users\\someone\\x.md",
            "http://localhost:4000/index.html",
            "/Users/someone/.cursor/projects/canvas.md",
        ):
            with self.subTest(target=target):
                self.assertIsNotNone(machine_local_reason(target))
        for target in ("README.md#frag", "#frag", "https://example.org/x", "mailto:a@b.org"):
            with self.subTest(target=target):
                self.assertIsNone(machine_local_reason(target))

    def test_code_examples_are_not_links(self) -> None:
        text = (
            "Example: `[README](https://example.org/README.md)`\n\n"
            "```\n[README](https://example.org/README.md)\n```\n"
        )
        self.assertEqual(extract_links("doc_architecture.md", text), [])

    def test_repository_is_clean(self) -> None:
        findings, _ = audit(ROOT)
        self.assertEqual(findings, [], msg="\n".join(findings))


if __name__ == "__main__":
    unittest.main()
