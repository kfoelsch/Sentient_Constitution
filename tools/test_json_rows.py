#!/usr/bin/env python3
"""Tests for json_rows."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from json_rows import dumps_rows  # noqa: E402

PAYLOAD = {
    "$schema": "../schemas/x.schema.json",
    "generated_at": "t",
    "flag": True,
    "nothing": None,
    "empty_list": [],
    "empty_dict": {},
    "files": {
        "a.md": {"total_lines": 3, "sections": [{"header": "Ünï ☃", "level": 1}, {"header": "B", "level": 2}]},
        "b.md": {"total_lines": 0, "sections": []},
    },
    "items": [{"k": 1, "v": [1, 2]}, {"k": 2, "v": []}],
    "nested": {"deep": {"x": [1, {"y": 2}]}},
}


class RoundTripTests(unittest.TestCase):
    def test_parses_back_identically_with_key_order(self) -> None:
        for depth in (2, 3, 4, 5, 9):
            out = json.loads(dumps_rows(PAYLOAD, depth))
            self.assertEqual(out, PAYLOAD)
            self.assertEqual(list(out), list(PAYLOAD))
            self.assertEqual(list(out["files"]["a.md"]), ["total_lines", "sections"])

    def test_unicode_is_not_escaped(self) -> None:
        self.assertIn("Ünï ☃", dumps_rows(PAYLOAD))

    def test_default_depth_writes_one_entry_per_line(self) -> None:
        lines = dumps_rows(PAYLOAD).splitlines()
        self.assertIn('    {"k":1,"v":[1,2]},', lines)
        self.assertIn('    {"k":2,"v":[]}', lines)
        self.assertIn('    "a.md": {"total_lines":3,"sections":[{"header":"Ünï ☃","level":1},{"header":"B","level":2}]},', lines)

    def test_deeper_row_depth_expands_nested_records(self) -> None:
        lines = dumps_rows(PAYLOAD, 5).splitlines()
        self.assertIn('        {"header":"Ünï ☃","level":1},', lines)

    def test_per_key_override(self) -> None:
        text = dumps_rows(PAYLOAD, 3, {"files": 5})
        self.assertIn('        {"header":"B","level":2}', text.splitlines())
        self.assertIn('    {"k":1,"v":[1,2]},', text.splitlines())

    def test_empty_containers_and_empty_payload(self) -> None:
        self.assertIn('"empty_list": []', dumps_rows(PAYLOAD))
        self.assertIn('"empty_dict": {}', dumps_rows(PAYLOAD))
        self.assertEqual(json.loads(dumps_rows({})), {})

    def test_idempotent_through_load(self) -> None:
        once = dumps_rows(PAYLOAD)
        self.assertEqual(dumps_rows(json.loads(once)), once)

    def test_smaller_than_indent_2(self) -> None:
        self.assertLess(len(dumps_rows(PAYLOAD)), len(json.dumps(PAYLOAD, indent=2, ensure_ascii=False)))


if __name__ == "__main__":
    unittest.main()
