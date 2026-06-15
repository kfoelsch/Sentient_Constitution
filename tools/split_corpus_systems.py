#!/usr/bin/env python3
"""Split corpus_systems.md into corpus_systems/ subfiles with a routing wrapper."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "corpus_systems.md"
TARGET_DIR = ROOT / "corpus_systems"

SECTIONS: list[tuple[str, int, int]] = [
    ("cs_01_scope_purpose_identifier_rules.md", 1, 76),
    ("cs_protocol_a_system_design_testing_verification_deployment.md", 77, 318),
    ("cs_protocol_b_system_comprehensibility_complexity_stewardship.md", 319, 339),
    ("cs_protocol_c_justice_safeguards_restitution_rehabilitation.md", 340, 470),
    ("cs_s1_information_types_and_handling.md", 471, 859),
    ("cs_s2_system_classification_and_handling.md", 860, 1472),
    ("cs_s3_critical_system_stewardship.md", 1473, 1729),
    ("cs_protocol_s4_adaptive_sustainability_ecosystem_resilience.md", 1730, 1825),
    ("cs_protocol_s5_resource_allocation_funding_stewardship.md", 1826, 2002),
    ("cs_protocol_t_transition_constitution_migration_governance.md", 2003, 2034),
    ("cs_protocol_r_subversion_response_replacement_reconstitution.md", 2035, 2141),
    (
        "cs_protocol_d_decentralized_constitutional_continuity_partition_resilience.md",
        2142,
        2225,
    ),
]

INDEX_ROWS: list[tuple[str, str]] = [
    (
        "Opening title, status, scope, and systems identifier rules",
        "cs_01_scope_purpose_identifier_rules.md",
    ),
    (
        "Protocol A: System Design, Testing, Verification, and Deployment",
        "cs_protocol_a_system_design_testing_verification_deployment.md",
    ),
    (
        "Protocol B: System Comprehensibility and Complexity Stewardship",
        "cs_protocol_b_system_comprehensibility_complexity_stewardship.md",
    ),
    (
        "Protocol C: Justice Safeguards, Restitution, and Rehabilitation Implementation",
        "cs_protocol_c_justice_safeguards_restitution_rehabilitation.md",
    ),
    (
        "Chapter S1 — Information Types and Handling",
        "cs_s1_information_types_and_handling.md",
    ),
    (
        "Chapter S2 — System Classification and Handling",
        "cs_s2_system_classification_and_handling.md",
    ),
    (
        "Chapter S3 — Critical System Stewardship",
        "cs_s3_critical_system_stewardship.md",
    ),
    (
        "Protocol S4 — Adaptive Sustainability and Ecosystem Resilience",
        "cs_protocol_s4_adaptive_sustainability_ecosystem_resilience.md",
    ),
    (
        "Protocol S5 — Resource Allocation and Funding Stewardship",
        "cs_protocol_s5_resource_allocation_funding_stewardship.md",
    ),
    (
        "Protocol T — Transition Constitution and Migration Governance",
        "cs_protocol_t_transition_constitution_migration_governance.md",
    ),
    (
        "Protocol R — Subversion Response, Replacement, and Reconstitution",
        "cs_protocol_r_subversion_response_replacement_reconstitution.md",
    ),
    (
        "Protocol D — Decentralized Constitutional Continuity and Partition Resilience",
        "cs_protocol_d_decentralized_constitutional_continuity_partition_resilience.md",
    ),
]

LINK_RE = re.compile(r"\]\(([^)]+)\)")


def rewrite_links(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        target = match.group(1)
        if (
            target.startswith("../")
            or target.startswith("http://")
            or target.startswith("https://")
            or target.startswith("#")
            or target.startswith("corpus_systems/")
        ):
            return match.group(0)
        return f"](../{target})"

    return LINK_RE.sub(repl, text)


def adapt_opening(text: str) -> str:
    text = text.replace(
        "> - This file is written in plain language with low jargon to improve accessibility, audit readability, and practical adoption testing.",
        "> - The CS folder is written in plain language with low jargon to improve accessibility, audit readability, and practical adoption testing.",
    )
    text = text.replace(
        "> - **Editorial map:** [doc_architecture.md](../doc_architecture.md) section 4 (definitions protocol) and section 2 (ownership map).",
        "> - **Navigation wrapper:** [corpus_systems.md](../corpus_systems.md) indexes the `corpus_systems/` subfiles.\n"
        "> - **Editorial map:** [doc_architecture.md](../doc_architecture.md) section 4 (definitions protocol) and section 2 (ownership map).",
    )
    text = text.replace(
        "- **CS** — this file (`corpus_systems.md`)",
        "- **CS** — this folder (`corpus_systems/`)",
    )
    return text


def strip_trailing_footer(text: str) -> str:
    text = re.sub(
        r"\n---\n\n\*Corpus alignment:.*?\n\n---\n\n\*\*Next file:\*\*.*$",
        "",
        text,
        flags=re.DOTALL,
    )
    return text.rstrip() + "\n"


def build_wrapper() -> str:
    rows = "\n".join(
        f"| {label} | [{filename}](corpus_systems/{filename}) |"
        for label, filename in INDEX_ROWS
    )
    return f"""# Systems implementation

*(Edition alignment: same labels as the Sentient Constitution numbered `core_*.md` files (see [README.md](README.md)), `corpus_joint_structure.md`, `corpus_institutions.md`, and `corpus_forum.md`.)*

**Compatibility entrypoint:** this root file is the stable navigation wrapper for the systems implementation file. Substantive CS text now lives in the `corpus_systems/` subfiles listed below. Broad references to `corpus_systems.md` continue to mean the systems implementation file as a whole.

**Authority note:** the linked subfiles are binding incorporated implementation text where `corpus_systems.md` is incorporated under Sentient Constitution Chapter Fifteen. The wrapper is an index and does not restate or narrow the subfile text.

## Systems Index

| Stable family | Authoritative subfile |
|---|---|
{rows}

---

**Next file:** [cs_01_scope_purpose_identifier_rules.md](corpus_systems/cs_01_scope_purpose_identifier_rules.md)
"""


def main() -> None:
    lines = SOURCE.read_text(encoding="utf-8").splitlines(keepends=True)
    TARGET_DIR.mkdir(exist_ok=True)

    filenames = [name for name, _, _ in SECTIONS]
    for index, (filename, start, end) in enumerate(SECTIONS):
        chunk = "".join(lines[start - 1 : end])
        chunk = rewrite_links(chunk)
        if index == 0:
            chunk = adapt_opening(chunk)
        else:
            chunk = strip_trailing_footer(chunk)

        if index < len(SECTIONS) - 1:
            next_file = filenames[index + 1]
            chunk = chunk.rstrip() + "\n\n---\n\n"
            if index > 0:
                prev_file = filenames[index - 1]
                chunk += f"**Previous file:** [{prev_file}]({prev_file})\n\n"
            chunk += f"**Next file:** [{next_file}]({next_file})\n"
        else:
            chunk = chunk.rstrip() + "\n\n---\n\n"
            chunk += (
                "*Corpus alignment:* edition `SC-Corpus-2026.04.32`, effective **2026-04-24**; "
                "canonical mapping in [doc_architecture.md](../doc_architecture.md) **section 17**.\n\n"
                "---\n\n"
                f"**Previous file:** [{filenames[index - 1]}]({filenames[index - 1]})\n\n"
                "**Next file:** [corpus_institutions.md](../corpus_institutions.md)\n"
            )

        (TARGET_DIR / filename).write_text(chunk, encoding="utf-8")

    SOURCE.write_text(build_wrapper(), encoding="utf-8")
    print(f"Wrote {len(SECTIONS)} subfiles under {TARGET_DIR.relative_to(ROOT)}/")
    print(f"Rewrote wrapper {SOURCE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
