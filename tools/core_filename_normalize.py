#!/usr/bin/env python3
"""One-shot: split remaining multi-chapter core files and drop doubled NN-NN names.

Do not rerun after the live files have been renamed. Historical names remain
under archive/.
"""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from local_markdown_fragment_audit import HTML_ANCHOR_RE, github_slug  # noqa: E402

SKIP_DIR_NAMES = {
    ".git",
    "archive",
    "evidence",
    "__pycache__",
    ".venv",
    "node_modules",
}

TEXT_SUFFIXES = {
    ".md",
    ".py",
    ".json",
    ".yml",
    ".yaml",
    ".csv",
    ".txt",
    ".mmd",
    ".mdc",
}

SIMPLE_RENAMES = {
    "subcore_03.030_burden_traceability_verification.md": (
        "subcore_03.030_burden_traceability_verification.md"
    ),
    "core_04.000_rights_part_a.md": "core_04.000_rights_part_a.md",
    "core_04.005_rights_part_b.md": "core_04.005_rights_part_b.md",
    "core_04.010_rights_part_c.md": "core_04.010_rights_part_c.md",
    "core_04.015_rights_part_d.md": "core_04.015_rights_part_d.md",
    "core_04.020_rights_part_e.md": "core_04.020_rights_part_e.md",
    "core_10.000_standing_assessment.md": "core_10.000_standing_assessment.md",
    "core_11.000_standing_measurement.md": "core_11.000_standing_measurement.md",
    "core_12.000_standing_integration.md": "core_12.000_standing_integration.md",
    "core_12.005_contribution_consequences.md": "core_12.005_contribution_consequences.md",
    "core_12.010_violation_consequences.md": "core_12.010_violation_consequences.md",
    "core_12.015_final_effect_restoration_enforcement.md": "core_12.015_final_effect_restoration_enforcement.md",
    "core_14.000_forum.md": "core_14.000_forum.md",
    "core_15.000_governance.md": "core_15.000_governance.md",
    "core_19.000_incorporation.md": "core_19.000_incorporation.md",
}

CH2 = "subcore_03.010_definition_structure.md"
CH3 = "subcore_03.020_definition_integrity.md"
CH13 = "core_16.000_non_regression.md"
CH14 = "core_17.000_expansion_supremacy.md"
CH15 = "core_18.000_amendment_ratification.md"

NEW_CORE_FILES = """CORE_FILES = (
    "core_00.000_preamble.md",
    "core_02.000_values_principles.md",
    "core_02.005_interaction_interpretation.md",
    "core_02.010_stewardship_capacity_principles.md",
    "subcore_03.010_definition_structure.md",
    "subcore_03.020_definition_integrity.md",
    "subcore_03.030_burden_traceability_verification.md",
    "core_03.000_definitions_home.md",
    "subcore_03.040_apex_accountability_leg.md",
    "subcore_03.045_apex_continuity_aim.md",
    "subcore_03.050_apex_flourishing_aim.md",
    "subcore_03.055_apex_oversight_leg.md",
    "subcore_03.060_apex_participation_leg.md",
    "subcore_03.065_apex_timeliness_leg.md",
    "subcore_03.070_band_accountability.md",
    "subcore_03.075_band_continuity.md",
    "subcore_03.080_band_integrative.md",
    "subcore_03.085_band_oversight.md",
    "subcore_03.090_band_participation.md",
    "subcore_03.095_band_performance.md",
    "core_06.000_functional_independence_separation_of_duties.md",
    "subcore_08.020_system_alignment_certification_evaluation.md",
    "core_08.005_system_alignment_certification_record_process.md",
    "core_08.010_system_alignment_certification_illustrations.md",
    "core_09.000_institutional_alignment_certification.md",
    "core_10.000_standing_assessment.md",
    "core_11.000_standing_measurement.md",
    "core_12.000_standing_integration.md",
    "core_12.005_contribution_consequences.md",
    "core_12.010_violation_consequences.md",
    "core_12.015_final_effect_restoration_enforcement.md",
    "core_13.000_misconduct_designation.md",
    "core_13.005_misconduct_pattern_applications.md",
    "core_14.000_forum.md",
    "core_10.010_application_vignettes.md",
    "core_04.000_rights_part_a.md",
    "core_04.005_rights_part_b.md",
    "core_04.010_rights_part_c.md",
    "core_04.015_rights_part_d.md",
    "core_04.020_rights_part_e.md",
    "core_15.000_governance.md",
    "core_16.000_non_regression.md",
    "core_17.000_expansion_supremacy.md",
    "core_18.000_amendment_ratification.md",
    "core_19.000_incorporation.md",
)"""

NEW_CORE_CHAIN = """CORE_CHAIN = (
    "core_00.000_preamble.md",
    "core_02.000_values_principles.md",
    "core_02.005_interaction_interpretation.md",
    "core_02.010_stewardship_capacity_principles.md",
    "subcore_03.010_definition_structure.md",
    "subcore_03.020_definition_integrity.md",
    "subcore_03.030_burden_traceability_verification.md",
    "core_03.000_definitions_home.md",
    "subcore_03.040_apex_accountability_leg.md",
    "subcore_03.045_apex_continuity_aim.md",
    "subcore_03.050_apex_flourishing_aim.md",
    "subcore_03.055_apex_oversight_leg.md",
    "subcore_03.060_apex_participation_leg.md",
    "subcore_03.065_apex_timeliness_leg.md",
    "subcore_03.070_band_accountability.md",
    "subcore_03.075_band_continuity.md",
    "subcore_03.080_band_integrative.md",
    "subcore_03.085_band_oversight.md",
    "subcore_03.090_band_participation.md",
    "subcore_03.095_band_performance.md",
    "core_06.000_functional_independence_separation_of_duties.md",
    "subcore_08.020_system_alignment_certification_evaluation.md#chapter-six-part-a-certification-evaluation",
    "core_08.005_system_alignment_certification_record_process.md#chapter-six-part-b-certification-record-and-process",
    "core_08.010_system_alignment_certification_illustrations.md#chapter-six-part-c-certification-illustrations",
    "core_09.000_institutional_alignment_certification.md#chapter-nine-institutional-alignment-certification",
    "core_10.000_standing_assessment.md",
    "core_11.000_standing_measurement.md",
    "core_12.000_standing_integration.md",
    "core_12.005_contribution_consequences.md",
    "core_12.010_violation_consequences.md",
    "core_12.015_final_effect_restoration_enforcement.md",
    "core_13.000_misconduct_designation.md",
    "core_13.005_misconduct_pattern_applications.md",
    "core_14.000_forum.md",
    "core_10.010_application_vignettes.md",
    "core_04.000_rights_part_a.md",
    "core_04.005_rights_part_b.md",
    "core_04.010_rights_part_c.md",
    "core_04.015_rights_part_d.md",
    "core_04.020_rights_part_e.md",
    "core_15.000_governance.md",
    "core_16.000_non_regression.md",
    "core_17.000_expansion_supremacy.md",
    "core_18.000_amendment_ratification.md",
    "core_19.000_incorporation.md",
)"""

HEADING_RE = re.compile(r"^#{1,6}[ \t]+(.+?)[ \t]*$")
ATX_CHAPTER_RE = re.compile(r"^## CHAPTER .+$", re.M)


def placement_widget(body_lines: str) -> str:
    return (
        "<details>\n"
        "<summary><strong><span style=\"color: #2563eb;\">Corpus placement "
        "(non-operative): file structure and reading rules</span></strong></summary>\n"
        "\n"
        f"{body_lines.rstrip()}\n"
        "\n"
        "</details>\n"
    )


def ch2_stack_reader_guidance() -> str:
    return f"""<details>
<summary><strong><span style="color: #2563eb;">Reader guidance (non-operative): definition stack and where Subcore 3-A lives</span></strong></summary>

> Chapter Three, including its subcore** form the constitutional definition stack; **[CJS](corpus_joint_structure.md)** carries operational definitions that apply it:
> - **Subcore 3-A (this file)** — O/M/A/C definition structure and component alignment: every definition links **Ontological (O)** (what it is), the **Measurement (M)** register interwoven with the **Assessment (A)** duty (how it must be measured and assessed), and **Compliance (C)** (what must hold) ([§1 Purpose and Role]({CH2}#1-purpose-and-role); [§2 Definition Integrity Requirement]({CH2}#2-definition-integrity-requirement)).
> - **Subcore 3-B** — definition integrity, evasion, and non-compliance ([Subcore 3-B]({CH3}#subcore-3-b-definition-integrity-evasion-and-non-compliance)).
> - **Subcore 3-C** — burden of proof, definition traceability, observability, verification under security limits, and verification accessibility ([Subcore 3-C — Burden of Proof, Traceability, and Verification](subcore_03.030_burden_traceability_verification.md#subcore-3-c-burden-of-proof-traceability-and-verification)).
> - **Chapter Three** — shared vocabulary for measurement, evaluation, and compliance (stand-alone, grouped, and package definitions in sections 1–3 across the five Tetrad band files and constitutional aim files: [Subcore 3-F — Flourishing aim](subcore_03.050_apex_flourishing_aim.md), [Subcore 3-M — Oversight](subcore_03.085_band_oversight.md), [Subcore 3-N — Participation](subcore_03.090_band_participation.md), [Subcore 3-J — Accountability](subcore_03.070_band_accountability.md), [Subcore 3-K — Continuity](subcore_03.075_band_continuity.md), [Subcore 3-L — Integrative](subcore_03.080_band_integrative.md)); reading order and map in [Part A](core_03.000_definitions_home.md#6-compass-and-definition-map).
> - **CJS** — operational definitions for cross-implementation terms ([CJS-3.105](corpus_joint_structure/cjs_03.105_cross_implementation_operational_terms.md#cjs-31-constitutional-compass-and-cluster-map) operational cluster library); apply Chapter Three canonical homes—do not redefine them. Domain taxonomies and protocols in **CS**, **CI**, and **CF** follow the same rule.
>
> Additional navigation:
> - **Anti-relocation rule:** procedural workflows, enforcement mechanics, and classification schemas beyond definitional scope must not be absorbed into this chapter.

</details>
"""


def footer(prev: str, nxt: str) -> str:
    return (
        "\n---\n\n"
        f"**Previous file:** [{prev}]({prev})\n"
        "\n"
        f"**Next file:** [{nxt}]({nxt})\n"
    )


def collect_anchors(text: str) -> set[str]:
    anchors: set[str] = set()
    for match in HTML_ANCHOR_RE.finditer(text):
        value = next(group for group in match.groups() if group)
        anchors.add(html.unescape(value))
    for line in text.splitlines():
        heading = HEADING_RE.match(line)
        if heading:
            anchors.add(github_slug(heading.group(1)))
    return anchors


def strip_trailing_nav(text: str) -> str:
    text = text.rstrip() + "\n"
    text = re.sub(
        r"\n---\s*\n\s*\*\*Previous file:\*\*[^\n]*\n+\s*\*\*Next file:\*\*[^\n]*\s*$",
        "\n",
        text,
    )
    text = re.sub(r"\n---\s*$", "\n", text)
    return text.rstrip() + "\n"


def rewrite_local_hashes(body: str, this_file: str, frag_map: dict[str, str]) -> str:
    def repl(match: re.Match[str]) -> str:
        frag = match.group(1)
        dest = frag_map.get(frag)
        if dest and dest != this_file:
            return f"]({dest}#{frag})"
        return match.group(0)

    return re.sub(r"\]\(#([A-Za-z0-9][A-Za-z0-9_-]*)\)", repl, body)


def lift_opening_reader_guidance(body: str) -> tuple[str, str]:
    body = body.lstrip()
    if body.startswith("<br>"):
        body = body[len("<br>") :].lstrip()
    if not body.startswith("<details>"):
        return "", body
    end = body.find("</details>")
    if end == -1:
        return "", body
    widget = body[: end + len("</details>")] + "\n"
    if "Reader guidance (non-operative):" not in widget:
        return "", body
    rest = body[end + len("</details>") :].lstrip()
    if rest.startswith("<br>"):
        rest = rest[len("<br>") :].lstrip()
    return widget, rest


def assemble_file(
    *,
    heading: str,
    placement: str,
    extra_before_body: str,
    body_prefix: str,
    body: str,
    this_file: str,
    frag_map: dict[str, str],
    prev: str,
    nxt: str,
) -> str:
    slug = github_slug(heading)
    body = strip_trailing_nav(body)
    body = re.sub(r"^## CHAPTER .+\n", "", body, count=1)
    body = rewrite_local_hashes(body, this_file, frag_map)
    lifted, body = lift_opening_reader_guidance(body)
    widgets = extra_before_body.rstrip()
    if lifted:
        widgets = (widgets + "\n\n" + lifted).strip() + "\n" if widgets else lifted
    parts = [
        f'<a id="{slug}"></a>\n',
        f"# {heading}\n\n",
        placement_widget(placement),
        "\n",
    ]
    if widgets:
        parts.append(widgets if widgets.endswith("\n") else widgets + "\n")
    if body_prefix:
        parts.append("\n<br>\n\n" + body_prefix.rstrip() + "\n")
        if body:
            parts.append("\n" + body.lstrip())
    else:
        parts.extend(["\n<br>\n\n", body.lstrip()])
    return "".join(parts).rstrip() + footer(prev, nxt)


def parse_chapter_blocks(text: str) -> list[tuple[str, str]]:
    matches = list(ATX_CHAPTER_RE.finditer(text))
    blocks: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        heading_line = match.group(0)
        heading = heading_line[3:].strip()
        blocks.append((heading, text[start:end]))
    return blocks


def split_source(old_name: str, specs: list[dict[str, str]]) -> dict[str, str]:
    path = ROOT / old_name
    text = path.read_text(encoding="utf-8")
    blocks = parse_chapter_blocks(text)
    by_heading = {heading: body for heading, body in blocks}
    frag_map: dict[str, str] = {}
    collisions: list[str] = []
    for spec in specs:
        body = by_heading[spec["heading"]]
        for anchor in collect_anchors(body):
            if anchor in frag_map and frag_map[anchor] != spec["new_file"]:
                collisions.append(f"{old_name}#{anchor}")
            frag_map[anchor] = spec["new_file"]
        heading_slug = github_slug(spec["heading"])
        frag_map[heading_slug] = spec["new_file"]
    if collisions:
        raise SystemExit("anchor collisions: " + ", ".join(collisions))

    written: dict[str, str] = {}
    for spec in specs:
        assembled = assemble_file(
            heading=spec["heading"],
            placement=spec["placement"],
            extra_before_body=spec.get("extra_before_body", ""),
            body_prefix=spec.get("body_prefix", ""),
            body=by_heading[spec["heading"]],
            this_file=spec["new_file"],
            frag_map=frag_map,
            prev=spec["prev"],
            nxt=spec["nxt"],
        )
        dest = ROOT / spec["new_file"]
        dest.write_text(assembled, encoding="utf-8")
        written[spec["new_file"]] = assembled
        print(f"wrote {spec['new_file']}")
    path.unlink()
    print(f"removed {old_name}")
    return frag_map


def iter_rewrite_paths() -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        if path.name == "Makefile" or path.suffix in TEXT_SUFFIXES:
            paths.append(path)
    return paths


def replace_split_filename(
    text: str,
    old: str,
    frag_map: dict[str, str],
    default: str,
    missing: list[str],
) -> str:
    pattern = re.compile(re.escape(old) + r"(?:#([A-Za-z0-9][A-Za-z0-9_-]*))?")

    def repl(match: re.Match[str]) -> str:
        frag = match.group(1)
        if not frag:
            return default
        dest = frag_map.get(frag)
        if dest is None:
            missing.append(f"{old}#{frag}")
            dest = default
        return f"{dest}#{frag}"

    return pattern.sub(repl, text)


def replace_tuple_block(text: str, name: str, new_block: str) -> str:
    pattern = re.compile(
        rf"{re.escape(name)} = \([\s\S]*?\n\)",
        re.M,
    )
    updated, count = pattern.subn(new_block, text, count=1)
    if count != 1:
        raise SystemExit(f"failed to replace {name} tuple")
    return updated


def insert_after_line(text: str, needle: str, extra_lines: list[str]) -> str:
    insertion = needle + "".join("\n    " + line for line in extra_lines)
    if needle not in text:
        raise SystemExit(f"missing list needle {needle!r}")
    return text.replace(needle, insertion)


def main() -> int:
    if not (ROOT / "subcore_03.010_definition_structure.md").exists():
        print("already normalized; nothing to do")
        return 0

    frag_02_03 = split_source(
        "subcore_03.010_definition_structure.md",
        [
            {
                "heading": (
                    "SUBCORE 3-A: DEFINITION STRUCTURE AND COMPONENT REQUIREMENTS"
                ),
                "new_file": CH2,
                "placement": (
                    "> This file is **part of the Sentient Constitution** and is "
                    "**binding only together** with the other numbered `core_*` files "
                    "read as one instrument. It contains **Subcore 3-A**: definition "
                    "structure and component alignment (O/M/A/C). **Subcore 3-B** — "
                    "definition integrity, evasion, and non-compliance — is in "
                    f"[`{CH3}`]({CH3}). Chapter numbering and cross-references match "
                    "the integrated instrument. Reading order, the binding/support split, "
                    "and corpus edition metadata are maintained in [README.md](README.md).\n"
                    ">\n"
                    "> **Upstream:** [Chapter Two, Part C](core_02.010_stewardship_capacity_principles.md).\n"
                    f"> **Downstream:** [Subcore 3-B]({CH3}#subcore-3-b-definition-integrity-evasion-and-non-compliance); "
                    "[Subcore 3-C](subcore_03.030_burden_traceability_verification.md#subcore-3-c-burden-of-proof-traceability-and-verification)."
                ),
                "extra_before_body": ch2_stack_reader_guidance(),
                "body_prefix": (
                    "*In plain terms: Chapter Three, including its subcore are the constitutional "
                    "definition stack — built (Two), kept honest (Three), checked (Four), "
                    "named (Five). Subcore 3-A builds each definition from linked parts — what "
                    "a term is (O), how it must be measured and assessed (the measurement "
                    "register interwoven with assessment, M/A), and what must hold in practice "
                    "(C). Cross-implementation operational definitions live in "
                    "[CJS](corpus_joint_structure.md) ([CJS-3.105 — Cross-Implementation Operational "
                    "Terms](corpus_joint_structure/cjs_03.105_cross_implementation_operational_terms.md"
                    "#cjs-31-constitutional-compass-and-cluster-map)); they apply Chapter Three "
                    "terms and do not redefine them.*\n"
                ),
                "prev": "core_02.010_stewardship_capacity_principles.md",
                "nxt": CH3,
            },
            {
                "heading": (
                    "SUBCORE 3-B: DEFINITION INTEGRITY, EVASION, AND NON-COMPLIANCE"
                ),
                "new_file": CH3,
                "placement": (
                    "> This file is **part of the Sentient Constitution** and is "
                    "**binding only together** with the other numbered `core_*` files "
                    "read as one instrument. It contains **Subcore 3-B**: definition "
                    "integrity, evasion, and non-compliance. **Subcore 3-A** — "
                    "definition structure and component alignment — is in "
                    f"[`{CH2}`]({CH2}). Chapter numbering and cross-references match "
                    "the integrated instrument. Reading order, the binding/support split, "
                    "and corpus edition metadata are maintained in [README.md](README.md).\n"
                    ">\n"
                    f"> **Upstream:** [Subcore 3-A]({CH2}#subcore-3-a-definition-structure-and-component-requirements).\n"
                    "> **Downstream:** [Subcore 3-C](subcore_03.030_burden_traceability_verification.md#subcore-3-c-burden-of-proof-traceability-and-verification)."
                ),
                "prev": CH2,
                "nxt": "subcore_03.030_burden_traceability_verification.md",
            },
        ],
    )

    frag_13_15 = split_source(
        "core_16.000_non_regression.md",
        [
            {
                "heading": (
                    "CHAPTER FIFTEEN: NON-REGRESSION AND SUBSTANTIVE AMENDMENT VALIDITY"
                ),
                "new_file": CH13,
                "placement": (
                    "> This file is **part of the Sentient Constitution** and is "
                    "**binding only together** with the other numbered `core_*` files "
                    "read as one instrument. It contains **Chapter Fifteen**: substantive "
                    "non-regression and substantive amendment validity (Test 1). "
                    f"**Chapter Sixteen** is in [`{CH14}`]({CH14}). **Chapter Seventeen** "
                    f"is in [`{CH15}`]({CH15}). Amendment validity must preserve both "
                    "[Two Constitutional Aims](core_00.000_preamble.md#two-constitutional-aims) "
                    "— **Flourishing** and **Continuity** — and must not hollow the "
                    "[Constitutional Tetrad](core_00.000_preamble.md#constitutional-tetrad) "
                    "below [material stake](core_00.000_preamble.md#material-stake) requirements. "
                    "Chapter numbering and cross-references match the integrated "
                    "instrument. Reading order, the binding/support split, and corpus "
                    "edition metadata are maintained in [README.md](README.md)."
                ),
                "prev": "core_15.000_governance.md",
                "nxt": CH14,
            },
            {
                "heading": (
                    "CHAPTER SIXTEEN: EXPANSION, SUPREMACY, AND EXTERNAL LEGAL ORDERS"
                ),
                "new_file": CH14,
                "placement": (
                    "> This file is **part of the Sentient Constitution** and is "
                    "**binding only together** with the other numbered `core_*` files "
                    "read as one instrument. It contains **Chapter Sixteen**: additive "
                    "expansion of protection, supremacy, and external legal orders. "
                    f"**Chapter Fifteen** (non-regression) is in [`{CH13}`]({CH13}). "
                    f"**Chapter Seventeen** (ratification and procedural validity) is in "
                    f"[`{CH15}`]({CH15}). Chapter numbering and cross-references match the "
                    "integrated instrument. Reading order, the binding/support split, "
                    "and corpus edition metadata are maintained in [README.md](README.md)."
                ),
                "prev": CH13,
                "nxt": CH15,
            },
            {
                "heading": (
                    "CHAPTER SEVENTEEN: AMENDMENT, RATIFICATION, AND PROCEDURAL VALIDITY"
                ),
                "new_file": CH15,
                "placement": (
                    "> This file is **part of the Sentient Constitution** and is "
                    "**binding only together** with the other numbered `core_*` files "
                    "read as one instrument. It contains **Chapter Seventeen**: amendment, "
                    "ratification, and procedural validity (Tests 2–4). "
                    f"**Chapter Fifteen** is in [`{CH13}`]({CH13}). **Chapter Sixteen** "
                    f"is in [`{CH14}`]({CH14}). Chapter numbering and cross-references match "
                    "the integrated instrument. Reading order, the binding/support split, "
                    "and corpus edition metadata are maintained in [README.md](README.md)."
                ),
                "prev": CH14,
                "nxt": "core_19.000_incorporation.md",
            },
        ],
    )

    for old, new in SIMPLE_RENAMES.items():
        src = ROOT / old
        dest = ROOT / new
        if not src.exists():
            raise SystemExit(f"missing {old}")
        src.rename(dest)
        print(f"renamed {old} -> {new}")

    missing_frags: list[str] = []
    for path in iter_rewrite_paths():
        original = path.read_text(encoding="utf-8")
        updated = original
        updated = replace_split_filename(
            updated,
            "subcore_03.010_definition_structure.md",
            frag_02_03,
            CH2,
            missing_frags,
        )
        updated = replace_split_filename(
            updated,
            "core_16.000_non_regression.md",
            frag_13_15,
            CH13,
            missing_frags,
        )
        for old, new in SIMPLE_RENAMES.items():
            updated = updated.replace(old, new)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(f"rewrote refs in {path.relative_to(ROOT)}")

    unique_missing = sorted(set(missing_frags))
    if unique_missing:
        print("unmapped split fragments (routed to chapter start file):")
        for item in unique_missing:
            print(f"  {item}")

    corpus_paths = ROOT / "tools/corpus_paths.py"
    corpus_paths.write_text(
        replace_tuple_block(
            corpus_paths.read_text(encoding="utf-8"),
            "CORE_FILES",
            NEW_CORE_FILES,
        ),
        encoding="utf-8",
    )
    footer_audit = ROOT / "tools/footer_audit.py"
    footer_audit.write_text(
        replace_tuple_block(
            footer_audit.read_text(encoding="utf-8"),
            "CORE_CHAIN",
            NEW_CORE_CHAIN,
        ),
        encoding="utf-8",
    )

    markdown_audit = ROOT / "tools/corpus_markdown_audit.py"
    md_text = markdown_audit.read_text(encoding="utf-8")
    md_text = insert_after_line(
        md_text,
        f'    "{CH2}",',
        [f'"{CH3}",'],
    )
    md_text = insert_after_line(
        md_text,
        f'    "{CH13}",',
        [f'"{CH14}",', f'"{CH15}",'],
    )
    markdown_audit.write_text(md_text, encoding="utf-8")

    dac = ROOT / "tools/ch5_dac_widget_audit.py"
    dac_text = dac.read_text(encoding="utf-8")
    if f'    "{CH3}",' not in dac_text:
        dac_text = insert_after_line(dac_text, f'    "{CH2}",', [f'"{CH3}",'])
        dac.write_text(dac_text, encoding="utf-8")

    def_app = ROOT / "tools/definition_appropriateness_audit.py"
    def_text = def_app.read_text(encoding="utf-8")
    def_text = def_text.replace(
        'rel.startswith("core_02-03") or rel.startswith("core_04-04")',
        'rel.startswith("core_02.") or rel.startswith("core_03.") or rel.startswith("core_04.")',
    )
    def_app.write_text(def_text, encoding="utf-8")

    pointer = ROOT / "tools/ch4_ch9_pointer_audit.py"
    pointer_text = pointer.read_text(encoding="utf-8")
    pointer_text = pointer_text.replace(
        r"core_02-03|core_04-04",
        r"core_02_|core_03_|core_04_",
    )
    pointer.write_text(pointer_text, encoding="utf-8")

    ch13 = ROOT / CH13
    ch13_text = ch13.read_text(encoding="utf-8")
    ch13_text = ch13_text.replace(
        "**Chapter Seventeen** in this file",
        f"**Chapter Seventeen** in [`{CH15}`]({CH15}#chapter-seventeen-amendment-ratification-and-procedural-validity)",
    )
    ch13.write_text(ch13_text, encoding="utf-8")

    print("core filename normalize complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
