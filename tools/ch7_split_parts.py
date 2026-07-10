#!/usr/bin/env python3
"""Split Chapter Seven into Part A (evaluation) and Part B (record/process)."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OLD = ROOT / "core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation"
PART_A = ROOT / "core_07_a_system_alignment_certification_evaluation.md"
PART_B = ROOT / "core_07_b_system_alignment_certification_record_process.md"
STUB = OLD

PART_A_NAME = "core_07_a_system_alignment_certification_evaluation.md"
PART_B_NAME = "core_07_b_system_alignment_certification_record_process.md"

SPLIT_MARKER = '<a id="11-certification-record"></a>'

# Anchors owned by Part B (§11–§16 and legacy record/process anchors)
PART_B_ANCHOR_PREFIXES = (
    "11-certification-record",
    "111-minimum-record-contents",
    "112-cross-section-record-requirements",
    "113-rights-floor-record-evaluation",
    "12-transparency-auditability-and-contestability",
    "13-forum-supervision-and-component-roles",
    "14-supervisory-sequence-and-contestability-chain",
    "141-supervisory-sequence",
    "142-contestability-chain",
    "143-anti-bypass",
    "15-relationship-to-standing",
    "16-reopening-drift-and-non-evasion",
    "3-certification-record",
    "2-certification-record",
    "7-transparency-auditability-and-contestability",
    "6-transparency-auditability-and-contestability",
    "9-forum-supervision-and-component-roles",
    "8-forum-supervision-and-component-roles",
    "8-supervisory-sequence-and-contestability-chain",
    "7-supervisory-sequence-and-contestability-chain",
    "81-supervisory-sequence",
    "82-contestability-chain",
    "11-reopening-drift-and-non-evasion",
    "10-reopening-drift-and-non-evasion",
    "31-minimum-record-contents",
    "32-cross-section-record-requirements",
    "33-rights-floor-record-evaluation-non-substitution",
)


def split_body(text: str) -> tuple[str, str]:
    idx = text.index(SPLIT_MARKER)
    return text[:idx].rstrip() + "\n", text[idx:].lstrip()


def part_a_header_block() -> str:
    return """<a id="chapter-seven-system-alignment-certification"></a>
<a id="chapter-seven-system-alignment-certification-and-recognition"></a>
<a id="chapter-seven-part-a-certification-evaluation"></a>
# CHAPTER SEVEN, PART A: SYSTEM ALIGNMENT CERTIFICATION — EVALUATION

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other chapters.
>
> This file is **part of the Sentient Constitution** and is **binding only together** with the other numbered `core_*` files read as one instrument. It contains **Chapter Seven, Part A** — certification **evaluation** requirements (system class, whole-system factors, and domain evaluation hooks). **Part B** — certification record, forum process, standing bridge, and reopening — is in [`core_07_b_system_alignment_certification_record_process.md`](core_07_b_system_alignment_certification_record_process.md).
>
> - **Constitutional owner (joint with Part B):** forum-supervised **system alignment certification and related records** — evaluation domains (Part A); certification-record duties, recognition outcomes, revalidation cadence, supervisory sequence, contestability chain, and verified-input bridge to Chapter Eight (Part B).
> - **Verification substrate owner:** [Chapter Four — Burden of Proof, Traceability, and Verification](core_04-04_burden_traceability_verification.md#chapter-four-burden-of-proof-traceability-and-verification) (within Chapters Two through Four) owns burden allocation, compliance evidence, definition traceability, observability, and security-constrained verification. Chapter Seven **applies** that discipline to system alignment certification records; it does **not** restate Chapter Four sections **1** through **5**.
> - **Implementation owner:** system-class handling, Protocol A, and forum-process detail in designated implementation files must remain consistent with Chapter Seven and may be stricter where the corpus already provides stricter-rule logic.
> - **Anti-relocation rule:** Part A does not restate Chapter Five canonical definitions, Chapter Three anti-evasion discipline (see [Part B §16](core_07_b_system_alignment_certification_record_process.md#16-reopening-drift-and-non-evasion)), Chapter Eight contribution or standing classification, or Chapter Nine standing effects. **[Part B §15](core_07_b_system_alignment_certification_record_process.md#15-relationship-to-standing)** states the standing bridge boundary explicitly.
>
> **Upstream:** Chapter Five definitions and Chapters Two through Four record, verification, burden, and tracing discipline.
> **Downstream:** [Part B](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process) (*record, forum process, and standing bridge*); Chapter Eight standing records and verified inputs; Chapter Nine standing effects; Chapter Eleven forum supervision and system alignment certification pathways.

</details>

<br>

Chapter Seven, **Part A**, is the constitutional owner of **system alignment certification evaluation** — what forums must verify before a certification record may reflect recognition, validation, revalidation, or continued reliance. Record contents, forum supervision, contest paths, and the standing bridge are in **[Part B](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process)**.

<br>
"""


def part_b_header_block() -> str:
    return """<a id="chapter-seven-part-b-certification-record-and-process"></a>
# CHAPTER SEVEN, PART B: SYSTEM ALIGNMENT CERTIFICATION — RECORD AND PROCESS

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other chapters.
>
> This file is **part of the Sentient Constitution** and is **binding only together** with the other numbered `core_*` files read as one instrument. It contains **Chapter Seven, Part B** — certification **record** contents, transparency and contestability, forum component roles, supervisory sequence, standing bridge, and reopening. **Part A** — evaluation requirements — is in [`core_07_a_system_alignment_certification_evaluation.md`](core_07_a_system_alignment_certification_evaluation.md).
>
> - **Constitutional owner (joint with Part A):** forum-supervised **system alignment certification and related records**.
> - **Evaluation inputs:** [Part A §2](core_07_a_system_alignment_certification_evaluation.md#2-system-class-evaluation) through [§10](core_07_a_system_alignment_certification_evaluation.md#10-trustworthiness-and-system-reliance-integrity-evaluation) supply evaluation outputs reflected on the certification record.
> - **Anti-relocation rule:** Part B does not restate Part A evaluation mechanics, Chapter Five canonical definitions, Chapter Eight standing classification, or Chapter Nine standing effects. **§15** states the standing bridge boundary explicitly.
>
> **Upstream:** [Part A](core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation); Chapter Eleven forum supervision; Chapters Two through Four verification discipline.
> **Downstream:** Chapter Eight standing records and verified inputs; Chapter Nine standing effects.

</details>

<br>

Chapter Seven, **Part B**, owns the **certification record**, **forum-supervised process**, and **standing bridge** for system alignment certification. Evaluation requirements live in **[Part A](core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation)**.

<br>

### 1. Purpose and Role (record and process)

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Upstream: [Part A §1](core_07_a_system_alignment_certification_evaluation.md#1-purpose-and-role) (*certification purpose and evaluation roadmap*); [Part A §2](core_07_a_system_alignment_certification_evaluation.md#2-system-class-evaluation) through [§10](core_07_a_system_alignment_certification_evaluation.md#10-trustworthiness-and-system-reliance-integrity-evaluation) (*evaluation outputs for the record*); [Constitutional Tetrad](core_00_preamble.md#constitutional-tetrad); [Two Constitutional Aims](core_00_preamble.md#two-constitutional-aims).
- Downstream: [§11](#11-certification-record) through [§16](#16-reopening-drift-and-non-evasion); [Chapter Eight](core_08-08_standing_assessment.md#chapter-eight-compliance-violation-and-standing-model); [Chapter Eleven](core_11-11_forum.md#chapter-eleven-forums-and-jurisdiction).
- Read with: [corpus_forum.md](corpus_forum.md), **CF-5** and **CF-7**.

</details>

<br>

*In plain terms: Part A says what must be **evaluated**. Part B says what must go **on the record**, how **forums** run the process, how people **challenge** outcomes, and how certification may feed **standing** — without letting certification substitute for standing classification or effects.*

Forum-supervised certification must produce a bounded **System Alignment Certification Record** under [§11](#11-certification-record) that reflects Part A evaluation outputs, satisfies [§12](#12-transparency-auditability-and-contestability), follows the forum roles in [§13](#13-forum-supervision-and-component-roles) and supervisory sequence in [§14](#14-supervisory-sequence-and-contestability-chain), and may supply verified inputs to Chapter Eight only through [§15](#15-relationship-to-standing). Defective certification, misclassification, and evasion route under [§16](#16-reopening-drift-and-non-evasion).

<br>
"""


def stub_content() -> str:
    return """<a id="chapter-seven-system-alignment-certification-index"></a>
# CHAPTER SEVEN: SYSTEM ALIGNMENT CERTIFICATION (READING INDEX)

<details>
<summary><strong><span style="color: #2563eb;">Corpus placement (non-operative): file structure and reading rules</span></strong></summary>

> The following content is **reader guidance only**. It does not add, remove, or narrow binding obligations elsewhere in this file or in other chapters.
>
> **Chapter Seven** is split across two binding files read as one instrument:
>
> | Part | File | Owns |
> |------|------|------|
> | **Part A — Evaluation** | [`core_07_a_system_alignment_certification_evaluation.md`](core_07_a_system_alignment_certification_evaluation.md) | §1–§10: purpose, system class, whole-system evaluation, domain evaluation hooks, illustrative class walkthroughs |
> | **Part B — Record and process** | [`core_07_b_system_alignment_certification_record_process.md`](core_07_b_system_alignment_certification_record_process.md) | §11–§16: certification record, transparency/contestability, forum roles, supervisory sequence, standing bridge, reopening |
>
> Legacy anchors from the former single-file Chapter Seven are preserved on the Part A and Part B files. Generic **Chapter Seven** links in other files route to the appropriate part by section number.

</details>

<br>

Read **Part A** first for evaluation requirements; **Part B** for record, forum process, and standing bridge.

- [Chapter Seven, Part A — Evaluation](core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation)
- [Chapter Seven, Part B — Record and Process](core_07_b_system_alignment_certification_record_process.md#chapter-seven-part-b-certification-record-and-process)
"""


def patch_part_a_body(body: str) -> str:
    # Remove old chapter header from split body (lines 1-26 approx)
    body = re.sub(
        r"^<a id=\"chapter-seven-system-alignment-certification\"></a>\s*\n"
        r"<a id=\"chapter-seven-system-alignment-certification-and-recognition\"></a>\s*\n"
        r"# CHAPTER SEVEN: SYSTEM ALIGNMENT CERTIFICATION\s*\n"
        r"<details>.*?</details>\s*\n<br>\s*\n"
        r"Chapter Seven is the constitutional owner of \*\*system alignment certification and related records\*\*\.\s*\n<br>\s*\n",
        "",
        body,
        count=1,
        flags=re.DOTALL,
    )

    # §1 roadmap: point §11-§16 to Part B
    body = body.replace(
        "([§11](#11-certification-record))",
        f"([Part B §11]({PART_B_NAME}#11-certification-record))",
    )
    body = body.replace(
        "([§12](#12-transparency-auditability-and-contestability), [§14](#14-supervisory-sequence-and-contestability-chain))",
        f"([Part B §12]({PART_B_NAME}#12-transparency-auditability-and-contestability), [Part B §14]({PART_B_NAME}#14-supervisory-sequence-and-contestability-chain))",
    )
    body = body.replace(
        "([§16](#16-reopening-drift-and-non-evasion) and evaluation sections throughout)",
        f"([Part B §16]({PART_B_NAME}#16-reopening-drift-and-non-evasion) and evaluation sections throughout)",
    )

    # §1 trace downstream §11-§16
    for sec in ("11", "12", "13", "14", "15", "16"):
        body = body.replace(
            f"[§{sec}](#{sec}-",
            f"[Part B §{sec}]({PART_B_NAME}#{sec}-",
        )

    # §1 trace anti-relocation §16
    body = body.replace(
        "(see [§16](#16-reopening-drift-and-non-evasion))",
        f"(see [Part B §16]({PART_B_NAME}#16-reopening-drift-and-non-evasion))",
    )
    body = body.replace(
        "**§15** states the standing bridge",
        f"**[Part B §15]({PART_B_NAME}#15-relationship-to-standing)** states the standing bridge",
    )

    # Closing pointer to Part B
    if "Part B" not in body.split("#### 1.1 Rights floors")[-1][:500]:
        pass

    footer = f"""
<br>

*Continue to record, forum process, and standing bridge:* [Chapter Seven, Part B — Record and Process]({PART_B_NAME}#chapter-seven-part-b-certification-record-and-process) ([§11]({PART_B_NAME}#11-certification-record) through [§16]({PART_B_NAME}#16-reopening-drift-and-non-evasion)).
"""
    return body.rstrip() + footer + "\n"


def patch_part_b_body(body: str) -> str:
    # Cross-file refs to Part A §2-§10
    for n in range(2, 11):
        body = re.sub(
            rf"\(#({n}|{n}\.[\d]+)-",
            rf"({PART_A_NAME}#\1-",
            body,
        )
        # Fix double filename if already patched
        body = body.replace(f"({PART_A_NAME}{PART_A_NAME}#", f"({PART_A_NAME}#")

    # Markdown link form [§N](#N-...) -> Part A
    for n in range(2, 11):
        body = re.sub(
            rf"\[§{n}(?:\.[\d]+)?\]\(#",
            lambda m, n=n: f"[§{m.group(0).split('§')[1].split(']')[0]}]({PART_A_NAME}#",
            body,
        )

    # Simpler: replace [§2](#2- with [§2](part_a#2-
    for n in range(2, 11):
        body = body.replace(f"[§{n}](#{n}-", f"[§{n}]({PART_A_NAME}#{n}-")
        for sub in ("1", "2", "3", "4", "5", "6", "7", "8"):
            body = body.replace(
                f"[§{n}.{sub}](#{n}{sub}-",
                f"[§{n}.{sub}]({PART_A_NAME}#{n}{sub}-",
            )
            body = body.replace(
                f"[§{n}.{sub}](#{n}.{sub}-",
                f"[§{n}.{sub}]({PART_A_NAME}#{n}{sub}-",
            )

    # §2.1, §3.8, §4.1, §5.1, §6.1
    for anchor in (
        "21-illustrative-class-profiles-non-exhaustive",
        "38-illustrative-whole-system-application-by-class",
        "41-illustrative-data-handling-application-by-class",
        "51-illustrative-ecological-footprint-application-by-class",
        "61-illustrative-cross-system-support-application-by-class",
    ):
        body = body.replace(f"](#{anchor})", f"]({PART_A_NAME}#{anchor})")

    # §3 without number prefix in ranges
    body = body.replace(
        f"[§3](#3-whole-system-certification-evaluation)",
        f"[§3]({PART_A_NAME}#3-whole-system-certification-evaluation)",
    )
    body = body.replace(
        "through [§10](#10-trustworthiness",
        f"through [§10]({PART_A_NAME}#10-trustworthiness",
    )
    body = body.replace(
        "[§2](#2-system-class-evaluation) through [§10](#10-trustworthiness",
        f"[§2]({PART_A_NAME}#2-system-class-evaluation) through [§10]({PART_A_NAME}#10-trustworthiness",
    )

    # §16 reopening refs to Part A evaluation sections stay internal to part B for §16 upstream - those are in same file for §5-§10 defects

    return body


def anchor_target(anchor: str) -> str:
    for prefix in PART_B_ANCHOR_PREFIXES:
        if anchor == prefix or anchor.startswith(prefix):
            return PART_B_NAME
    return PART_A_NAME


def migrate_corpus_links(text: str) -> str:
    old = "core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation"

    def repl(m: re.Match[str]) -> str:
        anchor = m.group(1) or ""
        if not anchor:
            return f"{PART_A_NAME}#chapter-seven-part-a-certification-evaluation"
        target = anchor_target(anchor)
        return f"{target}#{anchor}"

    text = re.sub(
        re.escape(old) + r"(?:#([\w\-]+))?",
        repl,
        text,
    )
    return text


def main() -> None:
    original = OLD.read_text(encoding="utf-8")
    part_a_body, part_b_body = split_body(original)

    part_a = part_a_header_block() + patch_part_a_body(part_a_body)
    part_b = part_b_header_block() + patch_part_b_body(part_b_body)

    PART_A.write_text(part_a, encoding="utf-8")
    PART_B.write_text(part_b, encoding="utf-8")
    STUB.write_text(stub_content(), encoding="utf-8")

    # Migrate all markdown/json in repo (except the three ch7 files we just wrote)
    skip = {PART_A, PART_B, STUB}
    patterns = ["**/*.md", "**/*.json", "**/*.py", "**/*.csv"]
    changed: list[Path] = []
    for pattern in patterns:
        for path in ROOT.glob(pattern):
            if path in skip or "node_modules" in path.parts:
                continue
            if path.name.startswith(".") and path.suffix != ".md":
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except (UnicodeDecodeError, IsADirectoryError):
                continue
            if "core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation" not in text:
                continue
            new_text = migrate_corpus_links(text)
            if new_text != text:
                path.write_text(new_text, encoding="utf-8")
                changed.append(path)

    # corpus_paths.py: add new files, keep stub
    cp = ROOT / "tools" / "corpus_paths.py"
    cp_text = cp.read_text(encoding="utf-8")
    if PART_A_NAME not in cp_text:
        cp_text = cp_text.replace(
            '    "core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation",',
            '    "core_07_a_system_alignment_certification_evaluation.md",\n'
            '    "core_07_b_system_alignment_certification_record_process.md",\n'
            '    "core_07_a_system_alignment_certification_evaluation.md#chapter-seven-part-a-certification-evaluation",',
        )
        cp.write_text(cp_text, encoding="utf-8")
        changed.append(cp)

    print(f"Wrote {PART_A.name} ({PART_A.stat().st_size} bytes)")
    print(f"Wrote {PART_B.name} ({PART_B.stat().st_size} bytes)")
    print(f"Wrote stub {STUB.name}")
    print(f"Updated {len(changed)} files with migrated links")


if __name__ == "__main__":
    main()
