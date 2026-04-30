#!/usr/bin/env python3
"""Update Sentient Constitution chapter citations after core split + renumber."""
from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

FILES = [
    "corpus_systems.md",
    "corpus_primitives.md",
    "corpus_institutions.md",
    "README.md",
    "doc_architecture.md",
    "architecture_primer.md",
    "TODO.md",
    "implementation/CORPUS_INSTITUTIONS_OUTLINE_DRAFT_2026-04-10.md",
    "implementation/CH7_EXPANDED_VALIDITY_HANDLING_DRAFT.md",
    "implementation/INTERPRETATION_BASELINE_SHARED_2026-04-09.md",
    "implementation/TRANSITION_FRAMEWORK_2026.md",
]


def transform(text: str) -> str:
    t = text
    t = t.replace(
        "Sentient Constitution Chapters One through Eight",
        "Sentient Constitution Chapters One through Ten",
    )
    t = t.replace("Chapters 1–8", "Chapters 1–10")
    t = t.replace("Chapters 1-8", "Chapters 1-10")
    t = t.replace(
        "Sentient Constitution Chapters Two and Three",
        "Sentient Constitution Chapters Two through Five",
    )
    t = t.replace(
        "Sentient Constitution Chapters Six through Eight",
        "Sentient Constitution Chapters Eight through Ten",
    )
    t = t.replace(
        "Sentient Constitution Chapters Four through Eight",
        "Sentient Constitution Chapters Six through Ten",
    )
    for old, new in [
        ("Sentient Constitution Chapter Eight", "Sentient Constitution Chapter Ten"),
        ("Sentient Constitution Chapter Seven", "Sentient Constitution Chapter Nine"),
        ("Sentient Constitution Chapter Six", "Sentient Constitution Chapter Eight"),
        ("Sentient Constitution Chapter Five", "Sentient Constitution Chapter Seven"),
        ("Sentient Constitution Chapter Four", "Sentient Constitution Chapter Six"),
        ("Sentient Constitution Chapter Three", "Sentient Constitution Chapter Five"),
    ]:
        t = t.replace(old, new)
    t = t.replace(
        "Sentient Constitution Chapter Two, section 8.1",
        "Sentient Constitution Chapter Four, section 4.1",
    )
    # Remaining "Sentient Constitution Chapter Two" → verification stack
    t = t.replace(
        "Sentient Constitution Chapter Two",
        "Sentient Constitution Chapters Two through Four",
    )
    # Bare "Chapter Two/Three" in doc_architecture
    t = t.replace(
        "Sentient Constitution Chapter Two/Three",
        "Sentient Constitution Chapters Two through Five",
    )
    return t


def main() -> None:
    for rel in FILES:
        path = ROOT / rel
        if not path.is_file():
            continue
        orig = path.read_text(encoding="utf-8")
        new = transform(orig)
        if new != orig:
            path.write_text(new, encoding="utf-8")
            print("Updated", rel)


if __name__ == "__main__":
    main()
