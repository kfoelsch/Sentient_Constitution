#!/usr/bin/env python3
"""Tests for front_door_audit.

Each test builds a minimal repository that passes every check, breaks one
thing, and asserts that exactly the matching rule fires.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from front_door_audit import audit, core_chapter_count, roman_to_int  # noqa: E402

SCRIPT = Path(__file__).resolve().parent / "front_door_audit.py"

EDITION = "SC-Corpus-2026.01.01"
Q1 = "Does it reward conduct that helps others and repairs harm?"
Q2 = "Does it reward conduct that harms others or shifts costs onto them?"

GENERATED = (
    "doc_architecture/generated/rights_floor_sheet.md",
    "doc_architecture/generated/plain_terms_edition.md",
    "doc_architecture/generated/human_definition_lookup.md",
    "implementation/PRINT_PACK.md",
)

README = f"""# Test Constitution

<a id="edition"></a>
| | |
|---|---|
| **Corpus edition** | `{EDITION}` |
| **Effective date** | 2026-01-01 |
| **Status** | **Pre-release.** A working draft. |

<a id="read-in-your-language"></a>
## Read in your language

[Espanol](translations/es/README.md)

Where a translation and the English text differ, the English text is the one that counts.

## What is this?

It has 2 articles of rights and a Preamble and Chapters 1–6.

1. {Q1}
2. {Q2}

<a id="reading-paths"></a>
## Reading paths

Start with [START_HERE.md](START_HERE.md).

<a id="where-to-start"></a>
## Quick find

- [Rights at a glance](doc_architecture/generated/rights_floor_sheet.md)
- [Plain terms](doc_architecture/generated/plain_terms_edition.md)
- [Words](doc_architecture/generated/human_definition_lookup.md)
- [Print pack](implementation/PRINT_PACK.md)

<a id="the-full-text"></a>
## The full text

<a id="implementation-files"></a>
## Implementation files

<a id="is-this-in-effect"></a>
## Is this in effect?

<a id="binding-vs-support"></a>
## Binding vs support

Run `make regression` to check.

<a id="authorship"></a>
## Authorship

Written by Karl Ernst with Claude and ChatGPT.

<a id="license"></a>
## License

CC BY 4.0.
"""

START = """# Start here

This corpus is pre-release. See [README](README.md).

<a id="pre-release-status"></a>
## 1. Status

<a id="two-modes"></a>
## 2. Two ways

<a id="fit-tests"></a>
## 3. Fit

<a id="ranked-situations"></a>
## 4. Where it fits best

1. [Alpha](implementation/adoption/FIT_SITUATIONS.md#41-alpha)
2. [Beta](implementation/adoption/FIT_SITUATIONS.md#42-beta)

<a id="honest-non-fits"></a>
## 5. Where it does not fit

- One.
- Two.

## 6. Next
"""

FIT = """# Fit

<a id="41-alpha"></a>
### 4.1 Alpha

<a id="42-beta"></a>
### 4.2 Beta

## 5. Honest non-fits

- One.
- Two.

## 6. Kit routing
"""

ANNOUNCEMENT = f"""# Announcement

Pinned to `{EDITION}` (effective 2026-01-01), pre-release.

```text
The core text (the Preamble and Chapters One through Six) is binding.

{Q1}
{Q2}

Start: README.md
Using or adopting it: START_HERE.md
```
"""

PREAMBLE = f"""# Preamble

1. **{Q1}**
2. **{Q2}**
"""

MAKEFILE = """.PHONY: regression
regression:
\t@echo ok
"""


def build(root: Path) -> None:
    def put(rel: str, text: str) -> None:
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    put("README.md", README)
    put("START_HERE.md", START)
    put("AGENTS.md", f"Edition: `{EDITION}` (effective 2026-01-01). Pre-release.\nDoor: README.md. Adopters: START_HERE.md.\n")
    put("llms.txt", f"Edition: {EDITION}. Pre-release.\nStart: README.md\nUsing or adopting it: START_HERE.md\n")
    put("docs/index.md", f"Pre-release `{EDITION}`. [README](https://example.org/blob/main/README.md) [START_HERE](https://example.org/blob/main/START_HERE.md)\nAuthorship: Karl Ernst, with Claude and ChatGPT\n")
    put("implementation/adoption/ANNOUNCEMENT.md", ANNOUNCEMENT)
    put("implementation/adoption/FIT_SITUATIONS.md", FIT)
    put("CONTRIBUTING.md", f"Edition `{EDITION}` is pre-release. Attribution: Karl Ernst and collaborating AI models.\n")
    put("LICENSE", "Attribution: Karl Ernst and collaborating AI models (Claude Fable and Opus, ChatGPT), Sentient Constitution.\n")
    put("Makefile", MAKEFILE)
    put("core_00000_preamble.md", PREAMBLE)
    for number in range(1, 6):
        put(f"core_{number:02d}000_chapter.md", f"# Chapter {number}\n")
    put("core_06005_rights_part_a.md", "# Rights\n\n## Article I\n\n## Article II\n")
    put("translations/README.md", "| Espanol | [Open](es/README.md) |\n")
    put("translations/es/README.md", "# es\n")
    for rel in GENERATED:
        put(rel, "# generated\n")


class Fixture(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        build(self.root)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def edit(self, rel: str, old: str, new: str) -> None:
        path = self.root / rel
        text = path.read_text(encoding="utf-8")
        self.assertIn(old, text, f"fixture drift: {old!r} not in {rel}")
        path.write_text(text.replace(old, new), encoding="utf-8")

    def errors(self, **kwargs) -> list[str]:
        return audit(self.root, **kwargs)

    def assertRule(self, rule: str, **kwargs) -> list[str]:
        errors = [e for e in self.errors(**kwargs) if rule in e]
        self.assertTrue(errors, f"expected {rule} to fire")
        return errors

    def assertOnly(self, rule: str) -> None:
        other = [e for e in self.errors() if rule not in e]
        self.assertEqual(other, [], f"{rule} test also tripped other rules")


class BaselineTests(Fixture):
    def test_clean_fixture_passes(self) -> None:
        self.assertEqual(self.errors(), [])

    def test_helpers(self) -> None:
        self.assertEqual(roman_to_int("XXVIII"), 28)
        self.assertEqual(roman_to_int("XIV"), 14)
        self.assertEqual(core_chapter_count(self.root), 6)


class EditionTests(Fixture):
    def test_edition_drift_on_pointer_page(self) -> None:
        self.edit("AGENTS.md", EDITION, "SC-Corpus-2026.02.02")
        errors = self.assertRule("FRONT-DOOR-EDITION-01")
        self.assertTrue(any("AGENTS.md" in e for e in errors))
        self.assertOnly("FRONT-DOOR-EDITION-01")

    def test_missing_edition_on_page(self) -> None:
        self.edit("llms.txt", EDITION, "an edition")
        self.assertRule("FRONT-DOOR-EDITION-01")

    def test_effective_date_drift(self) -> None:
        self.edit("AGENTS.md", "effective 2026-01-01", "effective 2026-03-03")
        self.assertRule("FRONT-DOOR-EDITION-01")

    def test_steward_index_pin(self) -> None:
        index = self.root / "implementation" / "steward_owner_clock_index.json"
        index.write_text('{"pinned_to_edition": "SC-Corpus-2025.12.12"}', encoding="utf-8")
        self.assertRule("FRONT-DOOR-EDITION-01")
        index.write_text(f'{{"pinned_to_edition": "{EDITION}", "edition_effective": "2026-01-01"}}', encoding="utf-8")
        self.assertEqual(self.errors(), [])


class EditionDateTests(Fixture):
    def test_label_date_must_be_the_effective_date(self) -> None:
        self.edit("README.md", "| **Effective date** | 2026-01-01 |", "| **Effective date** | 2026-01-02 |")
        for rel in ("AGENTS.md", "implementation/adoption/ANNOUNCEMENT.md"):
            self.edit(rel, "effective 2026-01-01", "effective 2026-01-02")
        self.assertRule("FRONT-DOOR-EDITION-02")

    def test_tracking_requires_today(self) -> None:
        self.assertEqual(audit(self.root, tracks_date=date(2026, 1, 1)), [])
        errors = [e for e in audit(self.root, tracks_date=date(2026, 1, 2)) if "EDITION-03" in e]
        self.assertEqual(len(errors), 1)
        self.assertIn("make edition-bump", errors[0])

    def test_tracking_is_off_by_default(self) -> None:
        self.assertEqual(self.errors(), [])

    def test_cli_flag(self) -> None:
        cmd = [sys.executable, str(SCRIPT), "--root", str(self.root), "--edition-tracks-date"]
        late = subprocess.run(cmd + ["--today", "2026-02-02"], capture_output=True, text=True)
        self.assertEqual(late.returncode, 1)
        self.assertIn("FRONT-DOOR-EDITION-03", late.stdout)
        ok = subprocess.run(cmd + ["--today", "2026-01-01"], capture_output=True, text=True)
        self.assertEqual(ok.returncode, 0, ok.stdout)


class StatusTests(Fixture):
    def test_page_drops_pre_release(self) -> None:
        self.edit("llms.txt", "Pre-release.", "Final.")
        self.assertRule("FRONT-DOOR-STATUS-01")

    def test_readme_drops_pre_release_but_pages_keep_it(self) -> None:
        self.edit("README.md", "**Pre-release.** A working draft.", "Final edition.")
        errors = self.assertRule("FRONT-DOOR-STATUS-01")
        self.assertTrue(any("still mentions" in e for e in errors))


class ChapterTests(Fixture):
    def test_announcement_range_too_low(self) -> None:
        self.edit("implementation/adoption/ANNOUNCEMENT.md", "Chapters One through Six", "Chapters One through One")
        self.assertRule("FRONT-DOOR-CHAPTERS-01")
        self.assertOnly("FRONT-DOOR-CHAPTERS-01")

    def test_wrapped_line_is_still_caught(self) -> None:
        self.edit("implementation/adoption/ANNOUNCEMENT.md", "Chapters One through Six", "Chapters One\nthrough Nine")
        self.assertRule("FRONT-DOOR-CHAPTERS-01")

    def test_digit_range_in_readme(self) -> None:
        self.edit("README.md", "Chapters 1–6", "Chapters 1–16")
        self.assertRule("FRONT-DOOR-CHAPTERS-01")

    def test_other_ranges_are_not_core_claims(self) -> None:
        self.edit("README.md", "Chapters 1–6.", "Chapters 1–6. See Chapters 2–4 and Chapter 5.")
        self.assertEqual(self.errors(), [])

    def test_new_chapter_makes_old_claim_stale(self) -> None:
        (self.root / "core_07000_new.md").write_text("# Three\n", encoding="utf-8")
        self.assertRule("FRONT-DOOR-CHAPTERS-01")


class ArticleTests(Fixture):
    def test_count_claim(self) -> None:
        self.edit("README.md", "2 articles", "28 articles")
        self.assertRule("FRONT-DOOR-ARTICLES-01")

    def test_new_article_makes_count_stale(self) -> None:
        part = self.root / "core_06005_rights_part_a.md"
        part.write_text(part.read_text(encoding="utf-8") + "\n## Article III\n", encoding="utf-8")
        self.assertRule("FRONT-DOOR-ARTICLES-01")

    def test_sub_articles_do_not_count(self) -> None:
        part = self.root / "core_06005_rights_part_a.md"
        part.write_text(part.read_text(encoding="utf-8") + "\n### Article II-D Something\n", encoding="utf-8")
        self.assertEqual(self.errors(), [])

    def test_gap_in_numerals(self) -> None:
        part = self.root / "core_06005_rights_part_a.md"
        part.write_text(part.read_text(encoding="utf-8") + "\n## Article IV\n", encoding="utf-8")
        errors = self.assertRule("FRONT-DOOR-ARTICLES-01")
        self.assertTrue(any("not consecutive" in e for e in errors))

    def test_roman_range(self) -> None:
        self.edit("README.md", "2 articles of rights", "2 articles of rights (Articles I–IX)")
        self.assertRule("FRONT-DOOR-ARTICLES-01")


class CountTests(Fixture):
    def test_definition_claim_above_registry(self) -> None:
        reg = self.root / "ai_corpus" / "indexes" / "definition_registry.json"
        reg.parent.mkdir(parents=True)
        reg.write_text('{"definition_count": 150, "definitions": []}', encoding="utf-8")
        self.edit("implementation/adoption/ANNOUNCEMENT.md", "is binding.", "is binding. It defines more than\ntwo hundred terms.")
        self.assertRule("FRONT-DOOR-COUNT-01")
        reg.write_text('{"definition_count": 263, "definitions": []}', encoding="utf-8")
        self.assertEqual(self.errors(), [])


class LanguageTests(Fixture):
    def test_translation_missing_from_readme(self) -> None:
        (self.root / "translations" / "fr").mkdir()
        (self.root / "translations" / "fr" / "README.md").write_text("# fr\n", encoding="utf-8")
        errors = self.assertRule("FRONT-DOOR-LANG-01")
        self.assertTrue(any("lacks translations/fr" in e for e in errors))
        self.assertTrue(any("table lacks fr" in e for e in errors))

    def test_readme_links_a_removed_language(self) -> None:
        self.edit("README.md", "[Espanol](translations/es/README.md)", "[Espanol](translations/es/README.md) [Deutsch](translations/de/README.md)")
        self.assertRule("FRONT-DOOR-LANG-01")

    def test_english_governs_statement_required(self) -> None:
        self.edit("README.md", "the English text is the one that counts", "the translation is fine")
        self.assertRule("FRONT-DOOR-LANG-01")


class QuestionTests(Fixture):
    def test_readme_wording_drift(self) -> None:
        self.edit("README.md", "helps others and repairs harm", "helps others and prevents harm")
        errors = self.assertRule("FRONT-DOOR-QUESTIONS-01")
        self.assertTrue(any("README.md" in e for e in errors))

    def test_preamble_change_flags_both_pages(self) -> None:
        self.edit("core_00000_preamble.md", "helps others and repairs harm", "helps others and prevents harm")
        errors = self.assertRule("FRONT-DOOR-QUESTIONS-01")
        self.assertEqual(len([e for e in errors if "does not quote" in e]), 2)

    def test_announcement_wrapped_and_quoted_copy_passes(self) -> None:
        self.edit(
            "implementation/adoption/ANNOUNCEMENT.md",
            Q1,
            '"Does it reward conduct that helps\nothers and repairs harm?"',
        )
        self.assertEqual(self.errors(), [])

    def test_preamble_layout_change_is_loud(self) -> None:
        (self.root / "core_00000_preamble.md").write_text("# Preamble\n", encoding="utf-8")
        errors = self.assertRule("FRONT-DOOR-QUESTIONS-01")
        self.assertTrue(any("expected the two numbered" in e for e in errors))


class MakeAndLinkTests(Fixture):
    def test_unknown_make_target(self) -> None:
        self.edit("README.md", "`make regression`", "`make regresion`")
        self.assertRule("FRONT-DOOR-MAKE-01")

    def test_multi_target_command(self) -> None:
        self.edit("README.md", "`make regression`", "`make regression nonexistent-target`")
        self.assertRule("FRONT-DOOR-MAKE-01")

    def test_phony_only_targets_count(self) -> None:
        (self.root / "Makefile").write_text(MAKEFILE + ".PHONY: extra-one \\\n\textra-two\n", encoding="utf-8")
        self.edit("README.md", "`make regression`", "`make extra-two`")
        self.assertEqual(self.errors(), [])

    def test_missing_tool_script(self) -> None:
        self.edit("README.md", "Run `make regression` to check.", "Run `make regression` or `python3 tools/gone.py`.")
        self.assertRule("FRONT-DOOR-MAKE-01")

    def test_broken_link_to_non_markdown_file(self) -> None:
        self.edit("README.md", "CC BY 4.0.", "CC BY 4.0. See [workflow](.github/workflows/pages.yml).")
        self.assertRule("FRONT-DOOR-LINK-01")

    def test_directory_link_ok(self) -> None:
        (self.root / "implementation" / "adoption" / "kits").mkdir()
        self.edit("README.md", "CC BY 4.0.", "CC BY 4.0. See [kits](implementation/adoption/kits/).")
        self.assertEqual(self.errors(), [])

    def test_links_in_fenced_examples_ignored(self) -> None:
        self.edit("README.md", "CC BY 4.0.", "```text\n[x](missing/thing.md)\n```")
        self.assertEqual(self.errors(), [])


class FitTests(Fixture):
    def test_ranked_item_points_at_wrong_heading(self) -> None:
        self.edit("START_HERE.md", "#41-alpha", "#42-beta")
        self.assertRule("FRONT-DOOR-FIT-01")

    def test_new_situation_not_ranked_in_start_here(self) -> None:
        self.edit("implementation/adoption/FIT_SITUATIONS.md", "## 5. Honest", "### 4.3 Gamma\n\n## 5. Honest")
        errors = self.assertRule("FRONT-DOOR-FIT-01")
        self.assertTrue(any("2 items but" in e for e in errors))

    def test_heading_slug_accepted_when_explicit_id_removed(self) -> None:
        self.edit("implementation/adoption/FIT_SITUATIONS.md", '<a id="41-alpha"></a>\n', "")
        self.assertEqual(self.errors(), [])

    def test_non_fit_bullet_count(self) -> None:
        self.edit("START_HERE.md", "- Two.\n", "- Two.\n- Three.\n")
        self.assertRule("FRONT-DOOR-FIT-01")


class AuthorPointerSectionTests(Fixture):
    def test_model_missing_from_docs_index(self) -> None:
        self.edit("docs/index.md", " and ChatGPT", "")
        errors = self.assertRule("FRONT-DOOR-AUTHOR-01")
        self.assertTrue(any("ChatGPT" in e for e in errors))

    def test_contributing_needs_only_the_author(self) -> None:
        self.assertEqual(self.errors(), [])
        self.edit("CONTRIBUTING.md", "Karl Ernst", "Someone Else")
        self.assertRule("FRONT-DOOR-AUTHOR-01")

    def test_license_line_shape_is_checked(self) -> None:
        (self.root / "LICENSE").write_text("CC BY 4.0\n", encoding="utf-8")
        self.assertRule("FRONT-DOOR-AUTHOR-01")

    def test_pointer_missing(self) -> None:
        self.edit("AGENTS.md", "Adopters: START_HERE.md.", "")
        self.assertRule("FRONT-DOOR-POINTER-01")

    def test_pointer_page_deleted(self) -> None:
        (self.root / "llms.txt").unlink()
        self.assertRule("FRONT-DOOR-POINTER-01")

    def test_required_section_removed(self) -> None:
        self.edit("README.md", '<a id="binding-vs-support"></a>\n## Binding vs support', "## What counts as binding")
        errors = self.assertRule("FRONT-DOOR-SECTIONS-01")
        self.assertTrue(any("binding-vs-support" in e for e in errors))

    def test_section_present_through_heading_slug(self) -> None:
        self.edit("README.md", '<a id="where-to-start"></a>\n', "")
        self.assertEqual(self.errors(), [])


class DuplicateTests(Fixture):
    def test_same_target_twice_in_one_list(self) -> None:
        self.edit("README.md", "- [Print pack](implementation/PRINT_PACK.md)\n", "- [Print pack](implementation/PRINT_PACK.md)\n- Print: [PRINT_PACK](implementation/PRINT_PACK.md)\n")
        self.assertRule("FRONT-DOOR-DUP-01")

    def test_same_target_in_separate_lists_ok(self) -> None:
        self.edit(
            "README.md",
            "- [Print pack](implementation/PRINT_PACK.md)\n",
            "- [Print pack](implementation/PRINT_PACK.md)\n\nA paragraph breaks the list.\n\n- [Print again](implementation/PRINT_PACK.md)\n",
        )
        self.assertEqual(self.errors(), [])

    def test_different_fragments_are_different_targets(self) -> None:
        self.edit(
            "README.md",
            "- [Print pack](implementation/PRINT_PACK.md)\n",
            "- [Print pack](implementation/PRINT_PACK.md#a)\n- [Print pack](implementation/PRINT_PACK.md#b)\n",
        )
        self.assertEqual(self.errors(), [])


class GeneratedTests(Fixture):
    def test_readme_stops_linking_a_generated_file(self) -> None:
        self.edit("README.md", "- [Words](doc_architecture/generated/human_definition_lookup.md)\n", "")
        self.assertRule("FRONT-DOOR-GENERATED-01")

    def test_generated_file_missing(self) -> None:
        (self.root / "implementation" / "PRINT_PACK.md").unlink()
        self.assertRule("FRONT-DOOR-GENERATED-01")

    def test_untracked_generated_file_flagged_in_git_repo(self) -> None:
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        errors = self.assertRule("FRONT-DOOR-GENERATED-01")
        self.assertTrue(any("not tracked" in e for e in errors))
        subprocess.run(["git", "-C", str(self.root), "add", "-A"], check=True)
        self.assertEqual([e for e in self.errors() if "GENERATED" in e], [])

    def test_freshness_runs_make_targets(self) -> None:
        errors = self.assertRule("FRONT-DOOR-GENERATED-01", freshness=True)
        self.assertEqual(len(errors), 4)
        stubs = "".join(f"{t}:\n\t@echo ok\n" for t in (
            "plain-terms-edition-check", "reader-accessibility-check", "print-pack-check", "pages-corpus-index-check"))
        (self.root / "Makefile").write_text(MAKEFILE + stubs, encoding="utf-8")
        self.assertEqual(self.errors(freshness=True), [])


class CliTests(Fixture):
    def run_cli(self) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(self.root)], capture_output=True, text=True
        )

    def test_exit_zero_when_clean(self) -> None:
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS", result.stdout)

    def test_exit_one_with_findings(self) -> None:
        self.edit("AGENTS.md", EDITION, "SC-Corpus-2026.02.02")
        result = self.run_cli()
        self.assertEqual(result.returncode, 1)
        self.assertIn("FAIL: 1 front-door divergence", result.stdout)
        self.assertIn("FRONT-DOOR-EDITION-01", result.stdout)


if __name__ == "__main__":
    unittest.main()
