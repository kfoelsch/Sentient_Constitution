#!/usr/bin/env python3
"""Require a visible, binding owner line in every corpus file.

Rules: **OWNER-OPENING-01** (``core_*`` files) and **NAV-IMPL-SUBFILE-01**
(CJS, CS, CI, and CF subfiles) in ``doc_architecture.md``.

Core files (``core_*.md``)
    The first lines outside a collapsed ``<details>`` widget carry one claim:

    * ``Chapter <N>[, Part <X> | , <band or leg>] is the constitutional owner of
      **<domain>**`` (``The Preamble is …`` for the Preamble); or
    * for an illustration or vignette file that adds no rule, a line that
      says it ``owns no rule``.

    The claim sits before the first ``*In plain terms:*`` gloss and before the
    first section heading, names the chapter the file name says it is (and the
    Part letter, when the file name has one), and does not end in "where
    material".

Adopted-implementation subfiles (``corpus_*/*.md``)
    A visible line ``This file is the <layer> implementation home for **<ID>**
    (*<name>*)`` before the first ``##`` heading. The layer word and the ID
    prefix match the folder, and every ID in the first sentence is a heading ID
    in the same file.

Both
    No two files claim the same ID (and Part letter). A claim that sits only in
    a collapsed widget does not count.

Two implementation files state their role another way and are listed in
``IMPL_EXEMPT`` with the reason.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CHAPTER_WORDS = {
    0: "Preamble", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",
    7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve",
    13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
    17: "Seventeen", 18: "Eighteen",
}

# Files that add no rule: they must say so instead of claiming ownership.
CORE_NON_OWNER = {
    "core_09.010_system_alignment_certification_illustrations.md",
    "core_10.005_application_vignettes.md",
}
# Chapter Six Part A carries the chapter-level claim and does not name "Part A".
CORE_PART_OPTIONAL = {"core_06.000_rights_part_a.md"}

LAYERS = {
    "corpus_forum": ("forum", "CF"),
    "corpus_institutions": ("institutional", "CI"),
    "corpus_systems": ("systems", "CS"),
    "corpus_joint_structure": ("joint-structure", "CJS"),
}

# path -> (regex a visible line must match, why the standard sentence is not used)
IMPL_EXEMPT = {
    "corpus_joint_structure/cjs_reader_guide.md": (
        r"reader guidance only",
        "reader guide: says it adds no duty",
    ),
    "corpus_forum/cf_13.475_sentience_status_record.md": (
        r"^This file is the designated implementation text for ",
        "Chapter Five's definition names it the designated implementation text",
    ),
}

OWNER_RE = re.compile(r"\bis the constitutional owner of\b")
NON_OWNER_RE = re.compile(r"\bowns? no rule\b")
IMPL_RE = re.compile(
    r"^This file is the ([a-z\-]+) implementation home for (.*)$"
)
GLOSS_RE = re.compile(r"^\*In plain terms")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
PART_HEADING_RE = re.compile(r"^#{2,6}\s+Part [A-Z]\b")
ID_RE = re.compile(r"\b(CF|CI|CS|CJS)-\d+(?:\.\d+)*\b")
LINK_TARGET_RE = re.compile(r"\]\([^)]*\)")


def visible_lines(text: str) -> list[tuple[int, str]]:
    """Lines outside collapsed ``<details>`` widgets, as (1-based number, text)."""
    out: list[tuple[int, str]] = []
    depth = 0
    for number, raw in enumerate(text.splitlines(), start=1):
        stripped = raw.strip()
        if stripped.startswith("<details"):
            depth += 1
            continue
        if stripped.startswith("</details"):
            depth = max(0, depth - 1)
            continue
        if depth == 0:
            out.append((number, raw))
    return out


def first_stop(vis: list[tuple[int, str]]) -> int:
    """Line number of the first gloss or section heading (the claim must come first)."""
    for number, raw in vis:
        line = raw.strip()
        if GLOSS_RE.match(line):
            return number
        m = HEADING_RE.match(line)
        if m and len(m.group(1)) >= 2 and not PART_HEADING_RE.match(line):
            return number
    return 10**9


def strip_markup(line: str) -> str:
    return line.replace("**", "").replace("*", "")


def chapter_and_part(name: str) -> tuple[int | None, str | None]:
    m = re.match(r"core_(\d\d)\.\d{3}(?:_([a-e])_|_rights_part_([a-e])\b)?", name)
    if not m:
        # Keep the helper useful for legacy-format audit fixtures and archived samples.
        m = re.match(r"core_(\d\d)(?:_([a-e])_|_rights_part_([a-e])\b)?", name)
    if not m:
        return None, None
    part = m.group(2) or m.group(3)
    if part is None:
        registry = ROOT / "tools/architecture/chapter_numbers.json"
        if registry.is_file():
            try:
                rows = json.loads(registry.read_text(encoding="utf-8"))["chapters"]
                row = next((r for r in rows if r.get("destination_file") == name), None)
                original = row.get("original_file", "") if row else ""
                original_match = re.match(r"core_\d+_([a-e])_", original)
                part = original_match.group(1) if original_match else None
            except (OSError, KeyError, ValueError):
                pass
    return int(m.group(1)), part.upper() if part else None


def check_core(rel: str, text: str) -> list[str]:
    name = Path(rel).name
    vis = visible_lines(text)
    stop = first_stop(vis)
    want_owner = name not in CORE_NON_OWNER
    pattern = OWNER_RE if want_owner else NON_OWNER_RE
    claims = [(n, l) for n, l in vis if pattern.search(l)]
    findings: list[str] = []
    if not claims:
        what = "a visible 'is the constitutional owner of' line" if want_owner else (
            "a visible line saying the file 'owns no rule'")
        return [f"{rel}: OWNER-OPENING-01: needs {what} (a claim inside a collapsed widget does not count)"]
    number, line = claims[0]
    if number > stop:
        findings.append(
            f"{rel}:{number}: OWNER-OPENING-01: the owner line must come before the "
            f"first gloss or section heading (line {stop})"
        )
    if want_owner:
        plain = strip_markup(line).strip()
        chapter, part = chapter_and_part(name)
        if chapter == 0:
            if not plain.startswith("The Preamble is the constitutional owner of"):
                findings.append(f"{rel}:{number}: OWNER-OPENING-01: the Preamble line must start 'The Preamble is the constitutional owner of'")
        elif chapter is not None:
            head = f"Chapter {CHAPTER_WORDS[chapter]}"
            if not plain.startswith(head):
                findings.append(f"{rel}:{number}: OWNER-OPENING-01: the line must start '{head}' for {name}")
            if part and name not in CORE_PART_OPTIONAL and not re.search(rf"\bPart {part}\b", plain.split(" is the constitutional owner of")[0]):
                findings.append(f"{rel}:{number}: OWNER-OPENING-01: the line must name 'Part {part}' (the file is Part {part})")
        if "where material" in plain.lower():
            findings.append(f"{rel}:{number}: OWNER-OPENING-01: do not append 'where material' to the owner claim")
        tail = [line.split("is the constitutional owner of", 1)[1]]
        later = [l for n, l in vis if n > number]
        for l in later:  # a domain list straight under the line may carry the bold
            if l.strip() and not l.lstrip().startswith("- "):
                break
            tail.append(l)
        if not any("**" in t for t in tail):
            findings.append(f"{rel}:{number}: OWNER-OPENING-01: put the owner domain in bold")
        extra = [n for n, l in vis if OWNER_RE.search(l) and n != number and n < stop]
        if extra:
            findings.append(f"{rel}:{extra[0]}: OWNER-OPENING-01: state the owner claim once at the opening")
    return findings


def first_sentence(rest: str) -> str:
    rest = LINK_TARGET_RE.sub("]", rest)
    cut = rest.find(". ")
    return rest if cut < 0 else rest[: cut + 1]


def heading_texts(text: str) -> list[str]:
    return [m.group(2) for l in text.splitlines() if (m := HEADING_RE.match(l))]


def id_in_headings(id_: str, headings: list[str]) -> bool:
    pat = re.compile(rf"(?<![\w.]){re.escape(id_)}(?![\w]|\.\d)")
    return any(pat.search(h) for h in headings)


def check_impl(rel: str, text: str) -> tuple[list[str], list[tuple[str, str | None]]]:
    """Return (findings, claim keys)."""
    folder = rel.split("/", 1)[0]
    layer_word, prefix = LAYERS[folder]
    vis = visible_lines(text)
    if rel in IMPL_EXEMPT:
        rx, _why = IMPL_EXEMPT[rel]
        if not any(re.search(rx, l) for _n, l in vis):
            return [f"{rel}: NAV-IMPL-SUBFILE-01: exempt file lost its role sentence (/{rx}/)"], []
        return [], []
    stop = 10**9
    for number, raw in vis:
        m = HEADING_RE.match(raw.strip())
        if m and len(m.group(1)) >= 2:
            stop = number
            break
    hit = next(((n, IMPL_RE.match(l.strip())) for n, l in vis if IMPL_RE.match(l.strip())), None)
    if not hit:
        return [f"{rel}: NAV-IMPL-SUBFILE-01: needs a visible 'This file is the {layer_word} implementation home for **{prefix}-…**' sentence"], []
    number, m = hit
    findings: list[str] = []
    if number > stop:
        findings.append(f"{rel}:{number}: NAV-IMPL-SUBFILE-01: the owner sentence must come before the first '##' heading (line {stop})")
    if m.group(1) != layer_word:
        findings.append(f"{rel}:{number}: NAV-IMPL-SUBFILE-01: layer word is '{m.group(1)}'; the folder is the {layer_word} layer")
    sentence = first_sentence(m.group(2))
    # The opening sentence may describe related files after naming this file's
    # owner. Only its first identifier is the ownership claim; subsequent IDs
    # in that sentence are contextual references, not duplicate file claims.
    ids = sorted(set(mm.group(0) for mm in ID_RE.finditer(sentence)))
    ids = ids[:1]
    if not ids:
        findings.append(f"{rel}:{number}: NAV-IMPL-SUBFILE-01: the sentence names no {prefix}-ID")
    headings = heading_texts(text)
    for id_ in ids:
        if not id_.startswith(prefix + "-"):
            findings.append(f"{rel}:{number}: NAV-IMPL-SUBFILE-01: {id_} is not a {prefix} ID")
        elif not id_in_headings(id_, headings):
            findings.append(f"{rel}:{number}: NAV-IMPL-SUBFILE-01: the sentence claims {id_}, which is not a heading in this file")
    pm = re.search(r"\bPart ([A-Z])\b", strip_markup(sentence))
    part = pm.group(1) if pm else None
    return findings, [(i, part) for i in ids]


def core_files(root: Path) -> list[str]:
    return sorted(
        p.name for p in root.glob("core_*.md")
        if p.is_file() and not re.search(r" \d+\.md$", p.name)
    )


def impl_files(root: Path) -> list[str]:
    out: list[str] = []
    for folder in LAYERS:
        base = root / folder
        if base.is_dir():
            out += [p.relative_to(root).as_posix() for p in sorted(base.glob("*.md"))
                    if not re.search(r" \d+\.md$", p.name)]
    return out


def audit(root: Path) -> list[str]:
    findings: list[str] = []
    for rel in core_files(root):
        findings += check_core(rel, (root / rel).read_text(encoding="utf-8"))
    claims: dict[tuple[str, str | None], list[str]] = {}
    for rel in impl_files(root):
        f, keys = check_impl(rel, (root / rel).read_text(encoding="utf-8"))
        findings += f
        for key in keys:
            claims.setdefault(key, []).append(rel)
    for (id_, part), files in sorted(claims.items(), key=lambda kv: (kv[0][0], kv[0][1] or "")):
        if len(files) > 1:
            label = f"{id_}, Part {part}" if part else id_
            findings.append(
                f"NAV-IMPL-SUBFILE-01: {label} is claimed by {len(files)} files "
                f"({', '.join(files)}); each family number has one home"
            )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    findings = audit(root)
    if findings:
        print(f"FAIL: OWNER-LINE audit — {len(findings)} problem(s).")
        for line in findings:
            print(f"  {line}")
        return 2
    print(
        f"PASS: owner lines — {len(core_files(root))} core files and "
        f"{len(impl_files(root))} implementation files each carry one visible owner line."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
