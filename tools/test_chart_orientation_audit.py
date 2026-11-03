import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from chart_orientation_audit import scan_text


class ChartOrientationAuditTests(unittest.TestCase):
    def test_default_directions_pass(self):
        self.assertEqual([], scan_text("x.md", "```mermaid\nflowchart TB\n```\n```mermaid\nflowchart TD\n```"))

    def test_nondefault_direction_requires_exception(self):
        text = "```mermaid\nflowchart LR\nA --> B\n```"
        self.assertEqual(1, len(scan_text("x.md", text)))

    def test_exception_note_passes(self):
        text = "```mermaid\nflowchart LR\n%% VIS-CHART-ORIENT-04 exception: side-by-side comparison\nA --> B\n```"
        self.assertEqual([], scan_text("x.md", text))


if __name__ == "__main__":
    unittest.main()
