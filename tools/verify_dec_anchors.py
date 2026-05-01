"""Verify that every D/E/C widget row in the consumer files resolves to a live
anchor in ``core_05-05_definitions_a_independent.md``. Reports any dead
targets on stderr and returns non-zero if any are found.

Also enforces the Chapter Five colocation rule for selected dependent-cluster
members whose canonical Trace/O/E/C lives only in Part C (§3.*): those terms
must not reappear as section 1 — Independent Definitions entries in Part A,
and corpus links must target ``#...-partc`` in Part C instead of Part A.

Run from the repository root:

    python3 tools/verify_dec_anchors.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


CH5 = Path("core_05-05_definitions_a_independent.md")
CH5_C = Path("core_05-05_definitions_c_dependent_clusters.md")

# Base slugs (without ``-partc``) whose definition body must not be duplicated
# in Part A §1. Extend when a new Part-C-only cluster member is editorially gated
# the same way as *Harassment and Bullying* (§3.3).
PART_C_ONLY_CLUSTER_BASE_SLUGS = frozenset({"harassment-and-bullying"})

CONSUMERS = [
    Path("core_00-01_principles.md"),
    Path("core_02-04_definition_mechanics.md"),
    Path("core_06-06_standing_classification.md"),
    Path("core_06-06_standing_integration.md"),
    Path("core_07-07_misconduct.md"),
    Path("core_08-08_forum.md"),
    Path("core_09-09_rights_part_a.md"),
    Path("core_09-09_rights_part_b.md"),
    Path("core_09-09_rights_part_c.md"),
    Path("core_09-09_rights_part_d.md"),
    Path("core_10-10_governance.md"),
    Path("core_11-13_amendment.md"),
    Path("core_14-14_incorporation.md"),
]

LINK_RE = re.compile(r"\]\(core_05-05_definitions_a_independent\.md#([^)]+)\)")
ANCHOR_TAG_RE = re.compile(r'<a id="([^"]+)"></a>')
CORE_MD_GLOB = "core_*.md"
H2_RE = re.compile(r"^##\s+(.+?)\s*$")
H3_RE = re.compile(r"^###\s+(.+?)\s*$")
H4_RE = re.compile(r"^####\s+(.+?)\s*$")
H5_RE = re.compile(r"^#####\s+(.+?)\s*$")


def collect_ch5_anchors() -> set[str]:
    anchors: set[str] = set()
    for m in ANCHOR_TAG_RE.finditer(CH5.read_text(encoding="utf-8")):
        anchors.add(m.group(1))
    # Also include implicit heading anchors (auto-slug) for headings that do
    # not carry an explicit <a id="..."></a>.
    for line in CH5.read_text(encoding="utf-8").splitlines():
        for pat in (H2_RE, H3_RE, H4_RE, H5_RE):
            m = pat.match(line)
            if m:
                slug = m.group(1).lower()
                slug = re.sub(r"[^\w\s-]", "", slug)
                slug = re.sub(r"\s+", "-", slug)
                slug = re.sub(r"-+", "-", slug).strip("-")
                if slug:
                    anchors.add(slug)
    return anchors


def forbidden_part_a_slugs() -> set[str]:
    """Anchors/slugs that must not exist on Part A for Part-C-only members."""
    out: set[str] = set()
    for base in PART_C_ONLY_CLUSTER_BASE_SLUGS:
        out.add(base)
        out.add(f"{base}-e")
        out.add(f"{base}-c")
    return out


def _partc_anchor_for_forbidden(slug: str) -> str:
    if slug.endswith("-e"):
        return f"{slug[:-2]}-partc-e"
    if slug.endswith("-c"):
        return f"{slug[:-2]}-partc-c"
    return f"{slug}-partc"


def verify_part_c_only_not_in_part_a(anchors: set[str]) -> list[str]:
    errs: list[str] = []
    for slug in sorted(forbidden_part_a_slugs()):
        if slug in anchors:
            target = _partc_anchor_for_forbidden(slug)
            errs.append(
                f"{CH5}: Part A must not define #{slug} — canonical Trace/O/E/C is "
                f"only in {CH5_C} (use #{target})."
            )
    return errs


def verify_no_stale_part_a_links() -> list[tuple[str, int, str]]:
    """Links into Part A using a Part-C-only slug fragment (any O/E/C)."""
    bad: list[tuple[str, int, str]] = []
    root = Path(".")
    for path in sorted(root.glob(CORE_MD_GLOB)):
        for lineno, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            for m in LINK_RE.finditer(line):
                slug = m.group(1)
                for base in PART_C_ONLY_CLUSTER_BASE_SLUGS:
                    if slug == base or slug.startswith(f"{base}-"):
                        bad.append((str(path), lineno, slug))
                        break
    return bad


def main() -> int:
    anchors = collect_ch5_anchors()

    dup_errs = verify_part_c_only_not_in_part_a(anchors)
    if dup_errs:
        print(
            "PART A / PART C COLOCATION CONFLICT (§1 must not duplicate §3 member):",
            file=sys.stderr,
        )
        for msg in dup_errs:
            print(f"  {msg}", file=sys.stderr)

    stale = verify_no_stale_part_a_links()
    if stale:
        print(
            "STALE LINKS (Part-C-only term linked via Part A file):",
            file=sys.stderr,
        )
        for path, lineno, slug in stale:
            print(f"  {path}:{lineno}  #{slug}", file=sys.stderr)

    missing: list[tuple[str, int, str]] = []
    for consumer in CONSUMERS:
        if not consumer.exists():
            continue
        for lineno, line in enumerate(
            consumer.read_text(encoding="utf-8").splitlines(), start=1
        ):
            for m in LINK_RE.finditer(line):
                slug = m.group(1)
                if slug not in anchors:
                    missing.append((str(consumer), lineno, slug))

    if dup_errs or stale:
        return 1

    if missing:
        print(
            f"MISSING ANCHORS ({len(missing)} links into Chapter Five have no "
            f"matching anchor):",
            file=sys.stderr,
        )
        for path, lineno, slug in missing:
            print(f"  {path}:{lineno}  #{slug}", file=sys.stderr)
        return 1

    print(f"OK: all Chapter Five links across {len(CONSUMERS)} consumer files resolve.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
