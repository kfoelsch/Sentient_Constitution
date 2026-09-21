"""One-shot helper: add ``-e`` and ``-c`` anchors to every definition entry in
``core_05-05_definitions_a_independent.md``.

Scope:
- Operates on both level-4 (``####``) and level-5 (``#####``) entries. Level-5
  entries are the sub-components of clustered definitions (for example, the
  Harm cluster contains ``##### Harm``, ``##### Psychological Harm``,
  ``##### Irreversible Harm``, and so on). Each such component with its own
  ``O:`` / ``E:`` / ``C:`` bullets gets its own anchors.
- For each entry, determines the canonical slug as either the explicit
  ``<a id="slug"></a>`` tag immediately preceding the heading or, absent that,
  the GitHub-style auto-slug of the heading text.
- Inserts ``<a id="{slug}-e"></a>`` immediately before the first ``- E: `` bullet
  in that entry, and ``<a id="{slug}-c"></a>`` immediately before the first
  ``- C: `` bullet.
- If the target anchor line is already present (idempotency), no change is made.

Run from the repository root:

    python3 tools/add_oec_anchors.py

The script modifies ``core_05-05_definitions_a_independent.md`` in place and
prints a summary of entries updated. It is safe to re-run.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


TARGET = Path("core_05-05_definitions_a_independent.md")

ANCHOR_RE = re.compile(r'^<a id="([^"]+)"></a>\s*$')
H4_RE = re.compile(r"^####\s+(.+?)\s*$")
H5_RE = re.compile(r"^#####\s+(.+?)\s*$")
H3_RE = re.compile(r"^###\s+")
SECTION_BREAK_RE = re.compile(r"^---\s*$")
E_BULLET_RE = re.compile(r"^- E: ")
C_BULLET_RE = re.compile(r"^- C: ")
EXISTING_E_ANCHOR_RE = re.compile(r'^<a id="[^"]+-e"></a>\s*$')
EXISTING_C_ANCHOR_RE = re.compile(r'^<a id="[^"]+-c"></a>\s*$')


def auto_slug(heading: str) -> str:
    """Approximate GitHub's heading-slug algorithm: lowercase, strip punctuation
    except spaces and hyphens, replace whitespace runs with a single hyphen,
    collapse consecutive hyphens."""
    slug = heading.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug, flags=re.UNICODE)
    slug = re.sub(r"\s+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def process(lines: list[str]) -> tuple[list[str], int, int]:
    out: list[str] = []
    updated_entries = 0
    skipped_already_anchored = 0

    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]

        h4_match = H4_RE.match(line)
        h5_match = H5_RE.match(line)
        heading_text: str | None = None
        if h4_match:
            heading_text = h4_match.group(1)
        elif h5_match:
            heading_text = h5_match.group(1)

        if heading_text is None:
            out.append(line)
            i += 1
            continue

        # Found a #### or ##### heading. Determine slug.
        slug: str | None = None
        # Explicit anchor is the last non-blank line before the heading.
        j = len(out) - 1
        while j >= 0 and out[j].strip() == "":
            j -= 1
        if j >= 0:
            anchor_match = ANCHOR_RE.match(out[j])
            if anchor_match:
                slug = anchor_match.group(1)
        if slug is None:
            slug = auto_slug(heading_text)

        # Emit the heading line and advance.
        out.append(line)
        i += 1

        # Scan forward for the body of this entry up to the next entry or
        # major section boundary (---, ### or ##, next #### or #####).
        e_anchor_inserted = False
        c_anchor_inserted = False
        already_has_e_anchor = False
        already_has_c_anchor = False

        while i < n:
            body = lines[i]
            # Terminate entry scan when we hit the next structural marker.
            if (
                H4_RE.match(body)
                or H5_RE.match(body)
                or H3_RE.match(body)
                or body.startswith("## ")
                or body.startswith("# ")
            ):
                break
            if SECTION_BREAK_RE.match(body):
                # Section break ends the entry body.
                out.append(body)
                i += 1
                break

            # Idempotency check: does an -e / -c anchor already sit immediately
            # above an E or C bullet?
            if (
                i + 1 < n
                and EXISTING_E_ANCHOR_RE.match(body)
                and E_BULLET_RE.match(lines[i + 1])
            ):
                already_has_e_anchor = True
            if (
                i + 1 < n
                and EXISTING_C_ANCHOR_RE.match(body)
                and C_BULLET_RE.match(lines[i + 1])
            ):
                already_has_c_anchor = True

            if E_BULLET_RE.match(body) and not e_anchor_inserted and not already_has_e_anchor:
                out.append(f'<a id="{slug}-e"></a>\n')
                e_anchor_inserted = True
            if C_BULLET_RE.match(body) and not c_anchor_inserted and not already_has_c_anchor:
                out.append(f'<a id="{slug}-c"></a>\n')
                c_anchor_inserted = True

            out.append(body)
            i += 1

        if e_anchor_inserted or c_anchor_inserted:
            updated_entries += 1
        elif already_has_e_anchor and already_has_c_anchor:
            skipped_already_anchored += 1

    return out, updated_entries, skipped_already_anchored


def main() -> int:
    if not TARGET.exists():
        print(f"error: cannot find {TARGET}", file=sys.stderr)
        return 2

    original = TARGET.read_text(encoding="utf-8").splitlines(keepends=True)
    updated, count_updated, count_skipped = process(original)

    TARGET.write_text("".join(updated), encoding="utf-8")
    print(
        f"{TARGET}: updated {count_updated} entries, "
        f"skipped {count_skipped} already-anchored entries"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
