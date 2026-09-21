"""Recognize lines changed only by the 2026 Chapter Seven insertion.

Changed-line audits use this narrow equivalence rule while the insertion is an
uncommitted repository-wide migration. It does not exempt new prose or any
change beyond the enumerated filename and explicit Chapter 7–16 shifts.
"""

from __future__ import annotations

import re


PATH_RENAMES = {
    "core_08-11_application_vignettes.md": "core_09-12_application_vignettes.md",
    "core_07_a_system_alignment_certification_evaluation.md": "core_08_a_system_alignment_certification_evaluation.md",
    "core_07_b_system_alignment_certification_record_process.md": "core_08_b_system_alignment_certification_record_process.md",
    "core_07_system_alignment_certification.md": "core_08_system_alignment_certification.md",
    "core_08_standing_assessment.md": "core_09_standing_assessment.md",
    "core_09_standing_integration.md": "core_10_standing_integration.md",
    "core_10_a_misconduct_designation.md": "core_11_a_misconduct_designation.md",
    "core_10_b_misconduct_pattern_applications.md": "core_11_b_misconduct_pattern_applications.md",
    "core_11_forum.md": "core_12_forum.md",
    "core_12_governance.md": "core_13_governance.md",
    "core_13_non_regression.md": "core_14_non_regression.md",
    "core_14_expansion_supremacy.md": "core_15_expansion_supremacy.md",
    "core_15_amendment_ratification.md": "core_16_amendment_ratification.md",
    "core_16_incorporation.md": "core_17_incorporation.md",
}

NUMBER_WORDS = {
    "Seven": "Eight",
    "Eight": "Nine",
    "Nine": "Ten",
    "Ten": "Eleven",
    "Eleven": "Twelve",
    "Twelve": "Thirteen",
    "Thirteen": "Fourteen",
    "Fourteen": "Fifteen",
    "Fifteen": "Sixteen",
    "Sixteen": "Seventeen",
}

ALL_NUMBER_WORDS = (
    "One|Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten|Eleven|Twelve|"
    "Thirteen|Fourteen|Fifteen|Sixteen|Seventeen"
)


def _replace_paths(text: str) -> str:
    placeholders: dict[str, str] = {}
    for index, (old, new) in enumerate(
        sorted(PATH_RENAMES.items(), key=lambda item: len(item[0]), reverse=True)
    ):
        token = f"@@CH7_INSERT_PATH_{index}@@"
        text = text.replace(old, token)
        placeholders[token] = new
    for token, value in placeholders.items():
        text = text.replace(token, value)
    return text


def _replace_chapter_references(text: str) -> str:
    variants: dict[str, str] = {}
    for old, new in NUMBER_WORDS.items():
        variants[old] = new
        variants[old.upper()] = new.upper()
        variants[old.lower()] = new.lower()

    replacements: dict[str, str] = {}

    def protect(value: str) -> str:
        token = f"@@CH7_INSERT_WORD_{len(replacements)}@@"
        replacements[token] = variants.get(value, value)
        return token

    range_re = re.compile(
        rf"(\b(?:Chapters|CHAPTERS|chapters)\s+)"
        rf"({ALL_NUMBER_WORDS}|{ALL_NUMBER_WORDS.lower()}|{ALL_NUMBER_WORDS.upper()})"
        rf"(\s+(?:through|to)\s+|[–-])"
        rf"({ALL_NUMBER_WORDS}|{ALL_NUMBER_WORDS.lower()}|{ALL_NUMBER_WORDS.upper()})"
    )
    text = range_re.sub(
        lambda match: (
            f"{match.group(1)}{protect(match.group(2))}"
            f"{match.group(3)}{protect(match.group(4))}"
        ),
        text,
    )
    chapter_re = re.compile(
        rf"(\b(?:Chapter|CHAPTER|chapter|Chapters|CHAPTERS|chapters)\s+)"
        rf"({ALL_NUMBER_WORDS}|{ALL_NUMBER_WORDS.lower()}|{ALL_NUMBER_WORDS.upper()})\b"
    )
    text = chapter_re.sub(
        lambda match: f"{match.group(1)}{protect(match.group(2))}", text
    )
    text = re.sub(
        r"(\b(?:Chapter|CHAPTER|chapter|Chapters|CHAPTERS|chapters)\s+)(\d{1,2})\b",
        lambda match: (
            f"{match.group(1)}{int(match.group(2)) + 1}"
            if 7 <= int(match.group(2)) <= 16
            else match.group(0)
        ),
        text,
    )

    slug_replacements: dict[str, str] = {}
    for index, (old, new) in enumerate(NUMBER_WORDS.items()):
        for separator, marker in (("-", "H"), ("_", "U")):
            token = f"@@CH7_INSERT_SLUG_{marker}_{index}@@"
            text = text.replace(f"chapter{separator}{old.lower()}", token)
            slug_replacements[token] = f"chapter{separator}{new.lower()}"

    for token, value in replacements.items():
        text = text.replace(token, value)
    for token, value in slug_replacements.items():
        text = text.replace(token, value)
    return text


def forward_insert_chapter_seven(text: str) -> str:
    """Apply only the enumerated mechanical changes from the insertion."""
    text = _replace_paths(text)
    text = _replace_chapter_references(text)
    text = text.replace(
        "core_01_c_stewardship_capacity_principles.md#102-segregation-of-duties",
        "core_07_functional_independence_segregation_of_duties.md#2-four-seat-constitutional-floor",
    )
    text = text.replace(
        "Chapter One §10.2 Segregation of Duties",
        "Chapter Seven §2 Four-Seat Constitutional Floor",
    )
    text = text.replace(
        "Chapter One §10.2 *Segregation of duties*",
        "Chapter Seven §2 *Four-seat constitutional floor*",
    )
    return text


def is_insertion_only_change(old_lines: list[str], new_line: str) -> bool:
    """Return true when a new diff line equals an enumerated forward rewrite."""
    return any(forward_insert_chapter_seven(old_line) == new_line for old_line in old_lines)
