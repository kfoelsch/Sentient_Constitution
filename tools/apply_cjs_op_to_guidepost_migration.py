#!/usr/bin/env python3
"""Migrate CJS-3 oDef OP-O/OP-E/OP-C triads to Chapter Five guidepost form.

Target shape per titled entry:

    <a id="{slug}"></a>
    {Title}

    *In plain terms: …*

    - **What it is**
      - **In scope:** …
      - **Out of scope:** …
    <a id="{slug}-a"></a>
    - **How to measure and assess**
      - **Primary measure:** …

        **Primary assessment:** …
    <a id="{slug}-c"></a>
    - **What must hold**
      - **Primary failure:** …

Regular single-line OP triads are converted automatically. Multiline or
title-less blocks are converted when a title can be recovered; otherwise they
are reported and left for hand edit. Always prefer ``--dry-run`` first.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CJS3_FILES = [
    "corpus_joint_structure/cjs_03_cross_implementation_operational_terms.md",
    "corpus_joint_structure/cjs_03o_oversight_operations.md",
    "corpus_joint_structure/cjs_03p_participation_operations.md",
    "corpus_joint_structure/cjs_03a_accountability_operations.md",
    "corpus_joint_structure/cjs_03c_continuity_operations.md",
    "corpus_joint_structure/cjs_03i_integrative_operations.md",
]

NONCOMPLIANT_PREFIX_RE = re.compile(
    r"^(?:"
    r"It is non-compliant to\s+"
    r"|Non-compliant:\s*"
    r")",
    re.IGNORECASE,
)

ASSESS_PREFIXES = (
    "Reviewers must verify that ",
    "Reviewers must verify ",
    "Reviewers must assess ",
    "Reviewers must look at ",
    "Reviewers must check ",
    "Reviewers must make sure ",
    "Evaluation must verify that ",
    "Evaluation must verify ",
    "Evaluation must assess ",
    "Evaluation must apply ",
    "Evaluation must compare ",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Repository root.")
    parser.add_argument(
        "--file",
        action="append",
        dest="files",
        help="Limit to one or more relative paths (repeatable).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned conversions without writing files.",
    )
    return parser.parse_args()


def slugify(title: str) -> str:
    text = title.strip().lower()
    text = text.replace("**", "")
    text = re.sub(r"[`'\"“”‘’]", "", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    if not text:
        text = "odef-term"
    return text[:80]


def unique_slug(base: str, used: set[str]) -> str:
    slug = base
    n = 2
    while slug in used:
        slug = f"{base}-{n}"
        n += 1
    used.add(slug)
    return slug


def join_continuation(lines: list[str]) -> str:
    parts: list[str] = []
    for idx, line in enumerate(lines):
        raw = line.rstrip()
        if idx == 0:
            parts.append(raw)
            continue
        stripped = raw.strip()
        if not stripped:
            continue
        if parts[-1].endswith("-"):
            parts[-1] = parts[-1][:-1] + stripped
        else:
            parts[-1] = parts[-1].rstrip() + " " + stripped
    return "\n".join(parts) if len(lines) > 1 and any(
        ln.strip().startswith(("1.", "2.", "3.", "-", "*")) for ln in lines[1:]
    ) else " ".join(p.strip() for p in parts if p.strip())


def collect_op_field(lines: list[str], start: int, label: str) -> tuple[str, int]:
    """Return field text and index of the last consumed line."""
    if start >= len(lines) or not lines[start].startswith(f"- {label}:"):
        raise ValueError(f"expected - {label}: at line {start + 1}")
    first = lines[start][len(f"- {label}:") :].lstrip()
    block = [first]
    i = start + 1
    while i < len(lines):
        stripped = lines[i]
        if stripped.startswith("- OP-") or stripped.startswith("- **"):
            break
        if stripped.startswith("#") or stripped.startswith("---"):
            break
        if stripped.startswith("<a id=") or stripped.startswith("<details"):
            break
        if not stripped.strip():
            # allow blank only inside numbered continuation blocks
            if i + 1 < len(lines) and lines[i + 1].startswith("  "):
                i += 1
                continue
            break
        if stripped.startswith("  ") or stripped.startswith("\t"):
            block.append(stripped)
            i += 1
            continue
        break
    # Preserve numbered lists under OP-O as markdown under In scope
    if any(ln.strip().startswith(("1.", "2.", "3.")) for ln in block[1:]):
        text = block[0].rstrip()
        for ln in block[1:]:
            text += "\n" + ln.rstrip()
        return text, i - 1
    return join_continuation(block), i - 1


def looks_like_title(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    # Bold article titles like **Article VII-B** … are valid titles.
    if stripped.startswith("**") and len(stripped) <= 160:
        return True
    if stripped.startswith(
        ("#", "-", "|", "<", "*", ">", "`", "Use this", "The ", "Before ", "Read ", "One ", "Some ", "Where ", "When ", "If ", "For ", "In an ", "Apply ", "See ")
    ):
        return False
    if stripped.endswith(":") and len(stripped) < 40:
        return False
    if len(stripped) > 160:
        return False
    # Long prose ending in period is probably not a title
    if stripped.endswith(".") and len(stripped) > 90:
        return False
    return True


def find_title(lines: list[str], op_o_index: int) -> tuple[str | None, int | None]:
    """Return (title, title_line_index) walking backward from OP-O."""
    i = op_o_index - 1
    while i >= 0:
        stripped = lines[i].strip()
        if not stripped or stripped.startswith("<a id="):
            i -= 1
            continue
        if looks_like_title(lines[i]):
            return lines[i].strip(), i
        return None, None
    return None, None


def derive_primary_measure(op_e: str) -> str:
    text = op_e.strip()
    for prefix in ASSESS_PREFIXES:
        if text.startswith(prefix):
            text = text[len(prefix) :]
            break
    text = text.rstrip(".")
    if text:
        text = text[0].lower() + text[1:]
    return text or "the operational evidence and controls named in the assessment duty"


def derive_out_of_scope(title: str) -> str:
    bare = re.sub(
        r"\s+(terms|controls|requirements|duties|limits|protections|interface|preference)$",
        "",
        title.strip(),
        flags=re.IGNORECASE,
    )
    if bare:
        bare = bare[0].lower() + bare[1:]
    else:
        bare = "this operational claim"
    return (
        f"ordinary process talk, symbolic labels, or adjacent owner-file duties "
        f"with no material stake in {bare}."
    )


def derive_plain_terms(op_o: str) -> str:
    # First sentence; keep links.
    text = op_o.strip()
    # If multiline numbered list, use only the lead sentence
    text = text.split("\n", 1)[0].strip()
    if ". " in text:
        text = text.split(". ", 1)[0].strip() + "."
    elif not text.endswith("."):
        text = text + "."
    if len(text) > 240:
        text = text[:237].rsplit(" ", 1)[0] + "…"
    if text and text[0].isupper() and not text.startswith(("A ", "An ", "The ", "Where ", "When ", "If ", "For ", "No ", "Any ", "Systems ", "Operators ", "Authorities ", "Material ", "Eligible ", "High-", "Class ", "Common-", "Emergency ", "Local ", "Delegated ", "Constitutional ", "Accountable ", "Authorized ", "Competency ", "Role-", "Quorum ", "Participation ", "Stakeholder ", "Foundational ", "Opaque-", "Parity ", "Pluralistic ", "Transparency ", "Ongoing ", "Misrepresentation ", "Enforcement-", "Anti-", "Audit ", "Independent ", "Disclosure ", "Secrecy ", "Override ", "Intervention ")):
        # Keep capital for proper-term starts; otherwise lightly downcase first letter for gloss voice
        pass
    return text[0].lower() + text[1:] if text and text[0].isupper() else text


def derive_failure(op_c: str) -> str:
    text = op_c.strip()
    # Glue artifact from legacy "addressed.---"
    if text.endswith("---"):
        text = text[:-3].rstrip()
    text = NONCOMPLIANT_PREFIX_RE.sub("", text)
    # Drop the compliance predicate; keep subject and any when/if/where clause.
    text = re.sub(r"\s+are non-compliant(?=\s|\.|$)", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+is non-compliant(?=\s|\.|$)", "", text, flags=re.IGNORECASE)
    text = text.strip()
    if text and not text.endswith("."):
        text += "."
    if text:
        text = text[0].upper() + text[1:]
    return text


def format_in_scope(op_o: str) -> str:
    if "\n" in op_o:
        lead, rest = op_o.split("\n", 1)
        return lead.rstrip() + "\n" + rest.rstrip()
    return op_o.strip()


def render_entry(
    title: str,
    slug: str,
    op_o: str,
    op_e: str,
    op_c: str,
) -> str:
    in_scope = format_in_scope(op_o)
    out_scope = derive_out_of_scope(title)
    measure = derive_primary_measure(op_e)
    assessment = op_e.strip()
    failure = derive_failure(op_c)
    plain = derive_plain_terms(op_o)

    in_scope_block = in_scope
    if "\n" in in_scope_block:
        # keep nested list indentation under In scope
        lines = in_scope_block.splitlines()
        rebuilt = [f"  - **In scope:** {lines[0]}"]
        for ln in lines[1:]:
            rebuilt.append(ln if ln.startswith("  ") else "    " + ln.lstrip())
        in_scope_md = "\n".join(rebuilt)
    else:
        in_scope_md = f"  - **In scope:** {in_scope_block}"

    return "\n".join(
        [
            f'<a id="{slug}"></a>',
            title,
            "",
            f"*In plain terms: {plain}*",
            "",
            "- **What it is**",
            in_scope_md,
            f"  - **Out of scope:** {out_scope}",
            f'<a id="{slug}-a"></a>',
            "- **How to measure and assess**",
            f"  - **Primary measure:** {measure}",
            "",
            f"    **Primary assessment:** {assessment}",
            f'<a id="{slug}-c"></a>',
            "- **What must hold**",
            f"  - **Primary failure:** {failure}",
        ]
    )


def migrate_text(text: str, rel: str) -> tuple[str, int, list[str]]:
    lines = text.splitlines()
    used_slugs: set[str] = set(
        re.findall(r'<a id="([^"]+)"></a>', text)
    )
    out: list[str] = []
    i = 0
    converted = 0
    skipped: list[str] = []

    while i < len(lines):
        line = lines[i]
        if not line.startswith("- OP-O:"):
            out.append(line)
            i += 1
            continue

        try:
            op_o, o_end = collect_op_field(lines, i, "OP-O")
            if o_end + 1 >= len(lines) or not lines[o_end + 1].startswith("- OP-E:"):
                raise ValueError("missing OP-E after OP-O")
            op_e, e_end = collect_op_field(lines, o_end + 1, "OP-E")
            if e_end + 1 >= len(lines) or not lines[e_end + 1].startswith("- OP-C:"):
                raise ValueError("missing OP-C after OP-E")
            op_c, c_end = collect_op_field(lines, e_end + 1, "OP-C")
        except ValueError as exc:
            skipped.append(f"{rel}:{i + 1}: {exc}")
            out.append(line)
            i += 1
            continue

        title, title_idx = find_title(lines, i)
        if title is None:
            skipped.append(f"{rel}:{i + 1}: no recoverable title before OP-O")
            out.append(line)
            i += 1
            continue

        # Drop the title line already emitted into out (and any intervening anchors/blanks stay)
        # Title was already appended when we walked past it — remove trailing copy from out.
        # Walk back in `out` to remove title and optional blank/anchor immediately before OP-O.
        # Simpler approach: rebuild by not including title when we see it is about to be replaced.
        # Because title was already written to out, strip it now.
        # Remove from out: optional trailing blanks, then title line, keep earlier anchors.
        while out and not out[-1].strip():
            out.pop()
        if out and out[-1].strip() == title:
            out.pop()
        # Keep preceding <a id> that is NOT the term slug we will add — drop none usually.
        # If an existing term-ish anchor sits immediately above title, leave it; we add our own.

        slug = unique_slug(slugify(title), used_slugs)
        entry = render_entry(title, slug, op_o, op_e, op_c)
        if out and out[-1].strip():
            out.append("")
        out.extend(entry.splitlines())
        converted += 1
        i = c_end + 1
        # Skip a single trailing blank that belonged to the old block; keep structural blanks later
        if i < len(lines) and not lines[i].strip():
            # ensure one blank after entry by letting next loop handle content;
            # add blank separator if next content is another title/OP
            if i + 1 < len(lines) and lines[i + 1].strip():
                out.append("")
            i += 1

    return "\n".join(out) + ("\n" if text.endswith("\n") else ""), converted, skipped


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    files = args.files or CJS3_FILES
    total = 0
    all_skipped: list[str] = []

    for rel in files:
        path = root / rel
        if not path.is_file():
            print(f"missing: {rel}", file=sys.stderr)
            return 1
        original = path.read_text(encoding="utf-8")
        updated, count, skipped = migrate_text(original, rel)
        all_skipped.extend(skipped)
        total += count
        if args.dry_run:
            print(f"{rel}: would convert {count} triad(s); skip {len(skipped)}")
            continue
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            print(f"{rel}: converted {count} triad(s)")
        else:
            print(f"{rel}: no changes ({count} converted in-memory match)")

    print(f"total converted: {total}")
    if all_skipped:
        print("skipped for hand edit:", file=sys.stderr)
        for item in all_skipped:
            print(f"  - {item}", file=sys.stderr)
        return 0 if total else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
