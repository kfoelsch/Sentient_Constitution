#!/usr/bin/env python3
"""Lightweight Chapter Five structural checks: §2 scaffolding, §3 mis-nested clusters, optional cluster-link and O/E/C heuristics."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_TOOLS = Path(__file__).resolve().parent
if str(_TOOLS) not in sys.path:
    sys.path.insert(0, str(_TOOLS))

from ch5_paths import CH5_ALL, CH5_PART_C  # noqa: E402


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", default=".", help="Workspace root")
    p.add_argument(
        "--file",
        action="append",
        help="Chapter Five file to scan; may be passed more than once. Defaults to all Chapter Five parts.",
    )
    p.add_argument(
        "--check-oec",
        action="store_true",
        help="Enable crude -O before -E/-C heuristic (noisy on subordinate ##### blocks)",
    )
    p.add_argument(
        "--check-cluster-member-anchors",
        action="store_true",
        help="Require each **Cluster members** (#slug) same-file link to have exact <a id=\"slug\"></a> in that file",
    )
    return p.parse_args()


def audit_dependent_context_markdown_headings(lines: list[str], path: Path) -> list[str]:
    """Disallow dependent-cluster context markers outside Part C."""
    errs: list[str] = []
    heading_re = re.compile(r"^(#{1,6})\s+Dependent-cluster context:")
    bold_re = re.compile(r"^\*\*Dependent-cluster context:")
    for lineno, line in enumerate(lines, start=1):
        stripped = line.strip()
        if heading_re.match(stripped):
            errs.append(
                f"{path}:{lineno}: dependent-cluster context must not be a Markdown heading; "
                "move the cluster to Part C or use ordinary prose inside a real definition"
            )
        if path.name != CH5_PART_C and bold_re.match(stripped):
            errs.append(
                f"{path}:{lineno}: dependent-cluster context must live in Part C; "
                "move the cluster contract to the dependent-clusters file"
            )
    return errs


def extract_cluster_member_slugs(cluster_body: str) -> list[str]:
    """Slugs from `- [Label](#slug)` lines under **Cluster members.** only (not Read-with)."""
    idx = cluster_body.find("**Cluster members.**")
    if idx < 0:
        return []
    rest = cluster_body[idx + len("**Cluster members.**") :]
    end_m = re.search(r"\n\*\*Read-with definitions\.\*\*", rest)
    list_region = rest[: end_m.start()] if end_m else rest
    slugs: list[str] = []
    for line in list_region.splitlines():
        line = line.strip()
        if not line.startswith("- ["):
            continue
        for m in re.finditer(r"\]\(#([a-z0-9\-]+)\)", line):
            slugs.append(m.group(1))
    return slugs


def slug_defined_in_chapter(text: str, slug: str) -> bool:
    """True if chapter defines the slug (primary or O/E/C-suffixed anchor)."""
    if f'<a id="{slug}"></a>' in text:
        return True
    return bool(re.search(rf'<a id="{re.escape(slug)}-[a-z0-9\-]+"></a>', text))


def audit_section3_cluster_member_anchors(
    text: str, path: Path, *, strict_primary: bool = False
) -> list[str]:
    errs: list[str] = []
    m3 = re.search(r"^### 3\.\s+Dependent", text, re.M)
    if not m3:
        return errs
    sec3 = text[m3.start() :]
    parts = re.split(r"(?=^#### 3\.\d+ )", sec3, flags=re.M)
    pat_heading = re.compile(r"^#### (3\.\d+ .+)$", re.M)
    for part in parts:
        hm = pat_heading.match(part)
        if not hm:
            continue
        label = hm.group(1).strip()
        slugs = extract_cluster_member_slugs(part)
        if not slugs:
            continue
        for slug in slugs:
            if strict_primary:
                ok = f'<a id="{slug}"></a>' in text
            else:
                ok = slug_defined_in_chapter(text, slug)
            if not ok:
                detail = (
                    "no exact <a id="
                    + repr(slug)
                    + "></a> in file"
                    if strict_primary
                    else "no matching <a id> in chapter"
                )
                errs.append(f"{path}: cluster {label!r} lists #{slug} but {detail}")
    return errs


def audit_section3_cluster_foreign_headings(text: str, path: Path) -> list[str]:
    """Heuristic: between #### 3.N and the next #### 3., flag other #### 3.x lines (mis-nested clusters)."""
    errs: list[str] = []
    m3 = re.search(r"^### 3\.\s+Dependent", text, re.M)
    if not m3:
        return errs
    sec3 = text[m3.start() :]
    blocks = re.split(r"(?=^#### 3\.\d+ )", sec3, flags=re.M)
    pat_cluster = re.compile(r"^#### (3\.\d+)\s", re.M)
    for block in blocks:
        heads = pat_cluster.findall(block)
        if len(heads) > 1:
            errs.append(
                f"{path}: possible mis-nested §3 cluster block starting {heads[0]!r} "
                f"contains extra numbered cluster headings: {heads!r}"
            )
    return errs


def audit_section3_noncluster_heading_oec(text: str, path: Path) -> list[str]:
    """Flag §3 Markdown subheadings that render as definition stubs without full O/E/C."""
    errs: list[str] = []
    m3 = re.search(r"^### 3\.\s+Dependent", text, re.M)
    if not m3:
        return errs
    sec3 = text[m3.start() :]
    heading_re = re.compile(r"^(#{4,5})\s+(.+)$", re.M)
    matches = list(heading_re.finditer(sec3))
    for idx, match in enumerate(matches):
        title = match.group(2).strip()
        if re.match(r"3\.\d+\b", title):
            continue
        body_start = match.end()
        body_end = matches[idx + 1].start() if idx + 1 < len(matches) else len(sec3)
        body = sec3[body_start:body_end]
        has_o = "\n- O:" in body
        has_e = "\n- E:" in body
        has_c = "\n- C:" in body
        if (has_o, has_e, has_c) != (True, True, True):
            lineno = text[: m3.start() + match.start()].count("\n") + 1
            errs.append(
                f"{path}:{lineno}: §3 non-cluster Markdown heading lacks full O/E/C "
                f"({title!r}; O={has_o}, E={has_e}, C={has_c}); demote subcomponent labels "
                "or provide a real definition body"
            )
    return errs


def audit_section3_numbered_shells(text: str, path: Path) -> list[str]:
    """Flag numbered §3 cluster sections that do not contain any local definition body."""
    errs: list[str] = []
    m3 = re.search(r"^### 3\.\s+Dependent", text, re.M)
    if not m3:
        return errs
    sec3 = text[m3.start() :]
    matches = list(re.finditer(r"^#### (3\.\d+)\s+(.+)$", sec3, re.M))
    for idx, match in enumerate(matches):
        number = match.group(1)
        if number in {"3.1", "3.2"}:
            continue
        body_start = match.end()
        body_end = matches[idx + 1].start() if idx + 1 < len(matches) else len(sec3)
        body = sec3[body_start:body_end]
        has_definition_body = "\n- O:" in body
        has_cluster_contract = (
            "**Admission scope.**" in body
            and "**Cluster members.**" in body
            and "**Joint invocation and anti-bypass.**" in body
        )
        if not has_definition_body and not has_cluster_contract:
            lineno = text[: m3.start() + match.start()].count("\n") + 1
            errs.append(
                f"{path}:{lineno}: §3 numbered section has neither local definition bodies "
                f"nor a complete cluster contract ({number} {match.group(2)!r}); "
                "move locator-only context to ordinary references or provide real cluster content"
            )
    return errs


def main() -> int:
    args = parse_args()
    root = Path(args.root)
    files = args.file or list(CH5_ALL)
    errs: list[str] = []

    for file_name in files:
        path = root / file_name
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()

        errs.extend(audit_dependent_context_markdown_headings(lines, path))

        if args.check_cluster_member_anchors:
            errs.extend(
                audit_section3_cluster_member_anchors(
                    text, path, strict_primary=True
                )
            )
        errs.extend(audit_section3_cluster_foreign_headings(text, path))
        errs.extend(audit_section3_numbered_shells(text, path))
        errs.extend(audit_section3_noncluster_heading_oec(text, path))

        # Duplicate §2 reader group titles: same #### line twice within 25 lines
        pat_s2_title = re.compile(r"^#### (.+)$")
        recent_titles: list[tuple[int, str]] = []
        sec2 = False
        for lineno, line in enumerate(lines, start=1):
            if "### 2. Semi-independent" in line:
                sec2 = True
            if sec2 and "### 3. Dependent clusters" in line:
                break
            m = pat_s2_title.match(line.strip())
            if sec2 and m:
                title = m.group(1).strip()
                for pl, pt in recent_titles:
                    if pt == title and lineno - pl <= 25:
                        errs.append(f"{path}:{lineno}: duplicate §2 group title near line {pl}: {title!r}")
                recent_titles.append((lineno, title))
                recent_titles = [(a, b) for a, b in recent_titles if lineno - a <= 25]

        # Repeated reader preamble in §2 (paste / double-reorder artifact)
        preamble = "**Reader grouping (non-operative).**"
        sec2 = False
        last_preamble_line: int | None = None
        for lineno, line in enumerate(lines, start=1):
            if "### 2. Semi-independent" in line:
                sec2 = True
                last_preamble_line = None
            if sec2 and "### 3. Dependent clusters" in line:
                break
            if sec2 and line.strip().startswith(preamble):
                if last_preamble_line is not None and lineno - last_preamble_line <= 12:
                    errs.append(
                        f"{path}:{lineno}: repeated §2 {preamble[:40]!r}… near line {last_preamble_line}"
                    )
                last_preamble_line = lineno

        if args.check_oec:
            i = 0
            in_ch5 = False
            while i < len(lines):
                line = lines[i]
                if line.startswith("## CHAPTER FIVE"):
                    in_ch5 = True
                if not in_ch5:
                    i += 1
                    continue
                if re.match(r"^#{3,5} ", line) and not line.startswith("######"):
                    depth = len(line) - len(line.lstrip("#"))
                    if depth in (3, 4, 5):
                        block: list[str] = []
                        j = i + 1
                        while j < len(lines):
                            nl = lines[j]
                            if re.match(r"^#{3,5} ", nl) and not nl.startswith("######"):
                                break
                            block.append(nl)
                            j += 1
                        joined = "\n".join(block)
                        if re.search(r"\n- E:", joined) or re.search(r"\n- C:", joined):
                            if "- O:" not in joined and "- O " not in joined:
                                if "Trace" not in joined[:200]:
                                    errs.append(
                                        f"{path}:{i + 1}: possible missing - O: before E/C in block after: {line.strip()[:70]}"
                                    )
                        i = j
                        continue
                i += 1

    if errs:
        for e in errs[:200]:
            print(e, file=sys.stderr)
        if len(errs) > 200:
            print(f"... and {len(errs) - 200} more", file=sys.stderr)
        return 1
    print("PASS: ch5_structure_audit")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
