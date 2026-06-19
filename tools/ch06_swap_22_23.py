#!/usr/bin/env python3
"""Swap Ch6 §2.2 (operational) and §2.3 (no-offset); renumber subsections and anchors."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CH06 = ROOT / "core_06-06_standing_assessment.md"

ANCHOR_REMAP = {
    "22-standing-record-operational-requirements": "23-standing-record-operational-requirements",
    "23-linked-records-and-no-offset-bridge": "22-linked-records-and-no-offset-bridge",
    "211-related-record-cross-references": "231-related-record-cross-references",
    "212-minimum-record-contents": "232-minimum-record-contents",
    "216-collective-and-actor-specific-records": "233-collective-and-actor-specific-records",
    "213-versioning": "234-versioning",
    "214-implementation-visibility": "235-implementation-visibility",
    "215-implementation-tools": "236-implementation-tools",
    "227-forum-boundary": "237-forum-boundary",
}


def remap_anchors(text: str) -> str:
    for old, new in ANCHOR_REMAP.items():
        text = text.replace(f'id="{old}"', f'id="{new}"')
        text = text.replace(f"#{old}", f"#{new}")
    return text


def main() -> None:
    text = CH06.read_text()
    start = text.index('<a id="21-standing-records-as-the-unit-of-application"></a>')
    end = text.index('<a id="4-primary-axis-categories-slot-grammar-and-defaults"></a>')
    block = text[start:end]

    # Split old operational (2.2) vs no-offset (2.3)
    op_start = block.index('<a id="22-standing-record-operational-requirements"></a>')
    no_start = block.index('<a id="23-linked-records-and-no-offset-bridge"></a>')
    intro = block[:op_start]
    operational = block[op_start:no_start]
    no_offset = block[no_start:]

    # Renumber operational block
    operational = operational.replace(
        '<a id="22-standing-record-operational-requirements"></a>',
        '<a id="23-standing-record-operational-requirements"></a>',
    )
    operational = operational.replace(
        "#### 2.2 Standing record operational requirements",
        "#### 2.3 Standing record operational requirements",
    )
    operational = operational.replace("##### 2.2.1 ", "##### 2.3.1 ")
    operational = operational.replace("##### 2.2.2 ", "##### 2.3.2 ")
    operational = operational.replace("##### 2.2.3 ", "##### 2.3.3 ")
    operational = operational.replace("##### 2.2.4 ", "##### 2.3.4 ")
    operational = operational.replace("##### 2.2.5 ", "##### 2.3.5 ")
    operational = operational.replace("##### 2.2.6 ", "##### 2.3.6 ")
    operational = operational.replace("##### 2.2.7 ", "##### 2.3.7 ")

    # Renumber no-offset block
    no_offset = no_offset.replace(
        '<a id="23-linked-records-and-no-offset-bridge"></a>',
        '<a id="22-linked-records-and-no-offset-bridge"></a>',
    )
    no_offset = no_offset.replace(
        "#### 2.3 Linked records and no-offset bridge",
        "#### 2.2 Linked records and no-offset bridge",
    )
    no_offset = no_offset.replace(
        "- Upstream: [§2.2.1](#211-related-record-cross-references) (*related-record cross-references*); [§2.2.2](#212-minimum-record-contents) (*verified-input gate*); [§2.2.7](#227-forum-boundary) (*forum boundary*).\n"
        "- Downstream: [§4.0](#40-slot-grammar-and-display-labels)",
        "- Upstream: [§2.1](#21-standing-records-as-the-unit-of-application) (*axis-pure standing records and linked-record possibility*).\n"
        "- Downstream: [§2.3.1](#231-related-record-cross-references) (*related-record cross-references*); [§2.3.2](#232-minimum-record-contents) (*verified-input gate*); [§2.3.7](#237-forum-boundary) (*forum boundary*); [§4.0](#40-slot-grammar-and-display-labels)",
    )

    new_block = intro + no_offset + operational
    new_block = remap_anchors(new_block)

    # Section-number prose inside §2 block
    prose = [
        ("section 2.2.7", "section 2.3.7"),
        ("section 2.2.6", "section 2.3.6"),
        ("section 2.2.5", "section 2.3.5"),
        ("section 2.2.4", "section 2.3.4"),
        ("section 2.2.3", "section 2.3.3"),
        ("section 2.2.2", "section 2.3.2"),
        ("section 2.2.1", "section 2.3.1"),
        ("sections 2.2.1", "sections 2.3.1"),
        ("sections 2.2.4–2.2.6", "sections 2.3.4–2.3.6"),
        ("under **section 2.3**.", "under **section 2.2**."),
        ("under **section 2.3** and", "under **section 2.2** and"),
        ("rules in **section 2.3**", "rules in **section 2.2**"),
        ("see **section 2.3** and **sections 2.3.1", "see **section 2.2** and **sections 2.3.1"),
    ]
    for old, new in prose:
        new_block = new_block.replace(old, new)

    text = text[:start] + new_block + text[end:]
    text = remap_anchors(text)

    # Header-level prose outside swapped block
    replacements = [
        (
            "(*§§2.1–2.3 — standing records, operational requirements, and no-offset bridge*)",
            "(*§§2.1–2.3 — standing records, no-offset bridge, and operational requirements*)",
        ),
        (
            "**Axis-pure standing records** → **verified-input gate and forum boundary** → **no-offset bridge**",
            "**Axis-pure standing records** → **no-offset bridge** → **verified-input gate and forum boundary**",
        ),
        (
            "- Downstream: [§2.2.2](#232-minimum-record-contents) (*verified-input gate*); [§2.2.7](#237-forum-boundary) (*forum boundary*); [§2.2](#22-linked-records-and-no-offset-bridge) (*linked-record no-offset bridge*);",
            "- Downstream: [§2.2](#22-linked-records-and-no-offset-bridge) (*linked-record no-offset bridge*); [§2.3.2](#232-minimum-record-contents) (*verified-input gate*); [§2.3.7](#237-forum-boundary) (*forum boundary*);",
        ),
        (
            "*In plain terms: Section 2 creates **standing records** — focused case files about one sentient, institution, or situation over a clear time period. Each file is **axis-pure**: a **contribution standing record** for verified good, or a **violation standing record** for verified adverse findings — not both in one file. Related files may **cross-reference** each other; **section 2.3.2** lists what each file must contain and what counts as verified input. The files are not permanent popularity scores or vague labels. **Sections 2.3.4–2.3.6** cover versioning and implementation visibility; **section 2.3.7** keeps forums separate from standing calculus; **section 2.2** states the no-offset rule when linked contribution and violation records coexist.*",
            "*In plain terms: Section 2 creates **standing records** — focused case files about one sentient, institution, or situation over a clear time period. Each file is **axis-pure**: a **contribution standing record** for verified good, or a **violation standing record** for verified adverse findings — not both in one file. **Section 2.2** states the no-offset rule when linked contribution and violation records coexist. Related files must **cross-reference** each other under **section 2.3.1**; **section 2.3.2** lists what each file must contain and what counts as verified input. The files are not permanent popularity scores or vague labels. **Sections 2.3.4–2.3.6** cover versioning and implementation visibility; **section 2.3.7** keeps forums separate from standing calculus.*",
        ),
        ("**§§2.1 and 2.3.2**", "**§§2.1 and 2.3.2**"),  # already correct after remap
    ]
    for old, new in replacements:
        if old in text:
            text = text.replace(old, new)

    CH06.write_text(text)

    # Corpus-wide anchor remap (skip archive)
    for path in ROOT.rglob("*"):
        if path == CH06 or "archive/" in str(path):
            continue
        if path.suffix not in {".md", ".json"}:
            continue
        original = path.read_text()
        updated = remap_anchors(original)
        updated = updated.replace("§2.2.7", "§2.3.7")
        updated = updated.replace("§2.2.2", "§2.3.2")
        updated = updated.replace("§2.2.1", "§2.3.1")
        updated = updated.replace("Chapter Six §2.2 Standing Record operational requirements", "Chapter Six §2.3 Standing record operational requirements")
        updated = updated.replace("§2.2 Standing Record operational requirements", "§2.3 Standing record operational requirements")
        updated = updated.replace("operational requirements in Chapter Six §2.2", "operational requirements in Chapter Six §2.3")
        updated = updated.replace("Chapter Six section 2.2", "Chapter Six section 2.3")
        if updated != original:
            path.write_text(updated)

    print("Swapped §2.2 and §2.3; renumbered subsections and anchors.")


if __name__ == "__main__":
    main()
