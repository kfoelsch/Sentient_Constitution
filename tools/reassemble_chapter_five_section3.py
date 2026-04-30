#!/usr/bin/env python3
"""
Reassemble Chapter Five §3: extract cluster bodies from the current (possibly
corrupted) file, synthesize any missing clusters, sort A–Z, renumber, fix
stable anchors, trim erroneous Transparency tail, move Foreseeability nest into
Truth cluster, regenerate implementation/CHAPTER_FIVE_OLD_TO_NEW_MAP.md.

Run from repo root: python3 tools/reassemble_chapter_five_section3.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from ch5_extended_cluster_synth import (  # noqa: E402
    harm_triplet_from_copy,
    synth_corpus_authority,
    synth_ecological,
    synth_emergency,
    synth_forum_families,
    synth_movement_refuge,
    synth_privacy_peer,
    synth_protected_internal_type_n,
    synth_proxy_integrity,
    synth_self_determination,
    synth_stakeholder_emergency_weight,
    synth_standing_contribution_violation,
    synth_strategic_stewardship,
    synth_substantive_procedural_fairness,
    transparency_cluster_from_copy,
)
CH5 = ROOT / "core_05-05_definitions_a_independent.md"
MAP_OUT = ROOT / "implementation" / "CHAPTER_FIVE_OLD_TO_NEW_MAP.md"

# Stable cluster anchor immediately before each #### heading (plan: unchanged)
ANCHOR_BY_TITLE: dict[str, str] = {
    "Accountability, Contestability, Adjudication and Dispute Resolution, Collective Accountability Failure, and Force Majeure": "accountability-contestability-and-collective-accountability-failure-cluster",
        "Assembly and Collective Organization": "assembly-and-collective-organization-cluster",
    "Binding Stakeholder Choice": "binding-stakeholder-choice-cluster",
    "Bodily-Maintenance Access, Safe Conditions, Tenure Security, Environmental Preconditions, Cultural Continuity, Rest, and Anti-Displacement Floor": "safe-conditions-tenure-security-and-environmental-preconditions-cluster",
    "Capture, Resolution Integrity, and Anti-Capture": "capture-resolution-integrity-and-anti-capture-cluster",
    "Collective Harm Boundary, Harm, and Harassment and Bullying": "collective-harm-boundary-and-harm-cluster",
    "Consent and Sexual Consent": "consent-and-sexual-consent-cluster",
    "Corpus, Authority Stack, Supremacy, and Enforceability": "corpus-authority-stack-supremacy-and-enforceability-cluster",
    "Creative Work, Training-Data Use, Attribution, Compensation, and Anti-Displacement": "creative-work-training-data-attribution-compensation-and-anti-displacement-cluster",
    "Derived and Developing Sentients, Instantiation, and Care Authority": "derived-developing-sentients-instantiation-and-care-authority-cluster",
    "Ecological Integrity, Footprint, and Sustainability": "ecological-integrity-footprint-and-sustainability-cluster",
    "Emergency and Contingency": "emergency-and-contingency-cluster",
    "Forum Families and Dispute Routing": "forum-families-and-dispute-routing-cluster",
    "Governance Architecture, Oversight, Dependency, Decentralization, Concentration, Market Structure, and Exit-Path Integrity": "governance-architecture-oversight-decentralization-and-concentration-cluster",
    "Movement, Refuge, Non-Statelessness, and Exit Integrity": "movement-refuge-non-statelessness-and-exit-integrity-cluster",
    "Privacy (Informational)": "privacy-informational-cluster",
    "Protected Internal-State Boundary and Type-N Anti-Bypass": "protected-internal-state-boundary-and-type-n-anti-bypass-cluster",
    "Protected Reporting and Anti-Retaliation": "protected-reporting-and-anti-retaliation-cluster",
    "Proxy Integrity and Indicator-Reality Alignment": "proxy-integrity-and-indicator-reality-alignment-cluster",
    "Self-Determination, Meaningful Agency, Expression, Educational Agency, Reproductive Autonomy, and Volitional Integrity": "self-determination-and-meaningful-agency-cluster",
    "Stakeholder Status, Emergency, and Participation Weight": "stakeholder-status-emergency-and-participation-weight-cluster",
    "Standing Inputs, Contribution State, and Violation Findings": "standing-state-contribution-and-violation-cluster",
    "Strategic Stewardship and Stewardship Defect": "strategic-stewardship-and-stewardship-defect-cluster",
    "Substantive and Procedural Fairness": "substantive-and-procedural-fairness-cluster",
    "Transparency, Auditability, and Verification": "transparency-auditability-and-verification-cluster",
    "Trust and Trustworthiness": "trust-and-trustworthiness-cluster",
    "Truth and Epistemic Integrity": "truth-and-epistemic-integrity-cluster",
    "Use of Force, Autonomous Coercion, Autonomous Lethal Systems, and Weapons of Mass Harm": "use-of-force-autonomous-coercion-and-mass-harm-cluster",
    "Voluntary Agency, Consent, and Anti-Coercion": "voluntary-agency-consent-and-anti-coercion-cluster",
}

EXPECTED_TITLES = sorted(ANCHOR_BY_TITLE.keys(), key=lambda s: s.lower())

FORESEEABILITY_NEST = """
---

##### Foreseeability Burden

- O: Responsibility for claiming non-foreseeability under [Reasonably Foreseeable](#reasonably-foreseeable) conditions.
<a id="foreseeability-burden-e"></a>
- E: Include [Auditability](#auditability)-compatible analysis.
<a id="foreseeability-burden-c"></a>
- C: Non-compliant: insufficient justification.
<a id="foreseeability-diligence"></a>
##### Foreseeability Diligence

- O: Standard of reasonable analysis proportional to impact.
<a id="foreseeability-diligence-e"></a>
- E: Include known methods and patterns for what is [Reasonably Foreseeable](#reasonably-foreseeable), scaled to [Material Impact](#material-impact), [Risk](#risk), and [Dependency](#dependency).
<a id="foreseeability-diligence-c"></a>
- C: Non-compliant: failure to meet this standard.
##### Foreseeability Failure

- O: Failure to perform required evaluation.
<a id="foreseeability-failure-e"></a>
- E: Detect incompleteness.
<a id="foreseeability-failure-c"></a>
- C: Non-compliant where it defeats [Foreseeability Diligence](#foreseeability-diligence), [Risk](#risk) evaluation, or [Safety (Constraint)](#safety-constraint).
##### Foreseeability Scaling

- O: [Proportionality](#proportionality)-sensitive depth of analysis.
<a id="foreseeability-scaling-e"></a>
- E: Scale with [Material Impact](#material-impact) and [Risk](#risk).
<a id="foreseeability-scaling-c"></a>
- C: Non-compliant: superficial analysis.
##### Foreseeability Scope

- O: Required evaluation boundaries.
<a id="foreseeability-scope-e"></a>
- E: Include interactions, [Dependency](#dependency), adversarial use, and relevant [System Boundaries](#system-boundaries).
<a id="foreseeability-scope-c"></a>
- C: Non-compliant: scope limitation.

<a id="reasonably-foreseeable"></a>
##### Reasonably Foreseeable

- O: Outcomes identifiable using domain knowledge and analytical methods under [Foreseeability Diligence](#foreseeability-diligence).
<a id="reasonably-foreseeable-e"></a>
- E: Include adversarial and scaled conditions, including [Adversarial, Scaled, and Exploited Conditions](#adversarial-scaled-and-exploited-conditions).
<a id="reasonably-foreseeable-c"></a>
- C: Non-compliant: exclusion of such outcomes.
""".strip()


def extract_meta_and_rest(text: str) -> tuple[str, str, str]:
    """Returns (prefix_before_section3, meta_3_1_and_3_2_block, from_section3_header_on)."""
    m = re.search(r"^### 3\. Dependent clusters.*?\n\n", text, re.MULTILINE)
    if not m:
        raise SystemExit("Section 3 header not found")
    sec3_pos = m.start()
    prefix = text[:sec3_pos]
    from_h3 = text[sec3_pos:]
    # Meta: #### 3.1 through line before #### 3.3 (first real cluster in source — variable)
    m31 = re.search(r"^#### 3\.1\b.*?(?=^#### 3\.\d+\s)", from_h3, re.DOTALL | re.MULTILINE)
    m32 = re.search(r"^#### 3\.2\b.*?(?=^#### 3\.\d+\s)", from_h3, re.DOTALL | re.MULTILINE)
    if not m31 or not m32:
        raise SystemExit("3.1 / 3.2 meta not found")
    meta_end = m32.end()
    meta_block = from_h3[:meta_end].rstrip()
    # Original files sometimes place the first cluster's <a id="…-cluster"> between 3.2 and 3.3;
    # strip so we do not duplicate the opener emitted with each cluster.
    meta_lines = meta_block.splitlines()
    while meta_lines:
        m = re.match(r'<a id="([^"]+)"></a>\s*$', meta_lines[-1].strip())
        if m and m.group(1).endswith("-cluster"):
            meta_lines.pop()
            continue
        break
    meta_block = "\n".join(meta_lines).rstrip() + "\n\n"
    rest = from_h3[meta_end:]
    return prefix, meta_block, rest


def parse_clusters_from_body(body: str) -> dict[str, str]:
    """title -> inner body (without #### line, without leading junk anchors)."""
    pat = re.compile(r"^#### 3\.\d+\s+(.+)$", re.MULTILINE)
    matches = list(pat.finditer(body))
    out: dict[str, str] = {}
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        chunk = body[start:end].strip()
        chunk = strip_leading_anchor_lines(chunk)
        out[title] = chunk
    return out


def strip_leading_anchor_lines(s: str) -> str:
    lines = s.splitlines()
    i = 0
    while i < len(lines) and lines[i].strip().startswith("<a id="):
        i += 1
    return "\n".join(lines[i:]).strip()


def scrub_embedded_cluster_anchor_lines(body: str) -> str:
    """Remove stray whole-line *-cluster opener anchors pasted inside bodies."""
    out: list[str] = []
    for line in body.splitlines():
        stripped = line.strip()
        m = re.fullmatch(r'<a id="([^"]+)"></a>', stripped)
        if m and m.group(1).endswith("-cluster"):
            continue
        out.append(line)
    return "\n".join(out).strip()


def trim_transparency_body(body: str) -> tuple[str, str]:
    """Remove erroneous Ch3 paste, Foreseeability nest (returned), and duplicate Harm..System tail."""
    # Drop erroneous Chapter Three sentence if present
    body = re.sub(
        r"^Any attempt to invoke, satisfy, or evaluate clustered components independently.*?\n\n",
        "",
        body,
        flags=re.MULTILINE,
    )
    # Split Foreseeability block out
    fm = re.search(
        r"\n---\n\n##### Foreseeability Burden\n",
        body,
    )
    tail_after_rf = None
    foresee = ""
    if fm:
        before = body[: fm.start()].rstrip()
        rest = body[fm.start() :].lstrip()
        # rest starts with --- 
        m_end = re.search(
            r"(?s)##### Reasonably Foreseeable\n.*?\n- C: Non-compliant: exclusion of such outcomes\.\n",
            rest,
        )
        if not m_end:
            raise SystemExit("Could not find end of Reasonably Foreseeable in Transparency body")
        foresee = rest[: m_end.end()].strip()
        tail_after_rf = rest[m_end.end() :].lstrip()
        body = before
    else:
        tail_after_rf = ""

    # Remove duplicate nest: from --- before ##### Harm (wrong nest) through
    # the block before Trust Degradation (Trust/Trustworthiness live in Part C).
    if tail_after_rf:
        hm = re.search(r"\n---\n\n<a id=\"harm\"></a>\n##### Harm\n", tail_after_rf)
        if hm:
            tail2 = tail_after_rf[hm.start() :]
            tm = re.search(
                r"\n\n<a id=\"trust-degradation-and-misleading-reliance-constitutional\"></a>\n",
                tail2,
            )
            if not tm:
                raise SystemExit(
                    "Expected trust-degradation constitutional anchor after duplicate Harm nest"
                )
            tail_after_rf = tail_after_rf[: hm.start()] + tail2[tm.start() :].lstrip()

    return body + "\n\n" + tail_after_rf if tail_after_rf else body, foresee


def truth_cluster_body(foresee_block: str) -> str:
    intro = """This cluster is the canonical O/E/C home for **Truth (Constitutional Constraint)** and **Epistemic Integrity**, and the joint-invocation home for **Foreseeability Diligence** and **Reasonably Foreseeable** where Chapters Two through Four tie "reasonably foreseeable" conditions to Chapter Five. It binds honest representation of materially decision-relevant facts and limits together with methodological integrity for evidence, uncertainty, disclosure, and contestability. Satisfying a nominal disclosure or publication channel alone is not sufficient where methodological integrity, uncertainty treatment, or foreseeable-condition analysis is materially required.

**Admission scope.** This cluster applies where a matter materially concerns truthful status representation, materially misleading communication, suppression or distortion of decision-relevant information, scientific or empirical integrity for high-impact claims, stated methods and limits, uncertainty treatment, foreseeable operating conditions, adversarial or scaled misuse contexts, or segmentation of truth and integrity duties across disclosure, audit, verification, or publication pathways. Outside that admission scope, component definitions may still operate as supporting Independent Definitions without importing the whole cluster.

**Cluster members.** This cluster comprises:

- [Truth (Constitutional Constraint)](#truth-constitutional-constraint);
- [Epistemic Integrity](#epistemic-integrity);
- [Foreseeability Diligence](#foreseeability-diligence);
- [Reasonably Foreseeable](#reasonably-foreseeable);
- [Good Faith](#good-faith), where publication, audit cooperation, or comparable good-faith disciplines materially intersect truth and epistemic integrity;
- [Materiality Determination](#materiality-determination) and [Dependency](#dependency), where materially implicated in scaling integrity and foreseeability analysis.

**Read-with definitions.** Apply [Transparency](#transparency), [Auditability](#auditability), [Observability](#observability), [Verifiability](#verifiability), [Contestability](#contestability), [Safety (Constraint)](#safety-constraint), [Risk](#risk), and Chapters Two through Four mechanics where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate disclosure, publication, empirical-method, uncertainty, integrity, verification, or foreseeability questions in a way that satisfies one component while defeating another. Nominal compliance with a disclosure or publication rule is not sufficient where foreseeable-condition analysis, methodological integrity, or honesty about limits and uncertainty remains materially deficient.

##### Truth (Constitutional Constraint)

<a id="truth-constitutional-constraint-o"></a>
- O: A non-negotiable constraint on how systems internally operate and externally communicate where materially decision-relevant claims, representations, risk communications, or compliance assertions are at stake. It requires honest treatment of what is known, unknown, and uncertain; resistance to deception, distortion, and structurally misleading presentation; and alignment with evaluative methods proportional to stakes under Chapters Two through Four.
<a id="truth-constitutional-constraint-e"></a>
- E: Evaluate substantive effect on informed decision-making and auditability. Scale scrutiny with [Material Impact](#material-impact), [Dependency](#dependency), and [Risk](#risk). Treat adversarial, scaled, repeated, and misuse contexts as within [Reasonably Foreseeable](#reasonably-foreseeable) evaluation where relevant. Require independent scrutiny pathways proportionate to stakes under Chapter Four. Where empirical or testable propositions support high-impact decisions, require honest methods, data limits, uncertainty treatment, and revision when evidence disconfirms prior conclusions.
<a id="truth-constitutional-constraint-c"></a>
- C: Non-compliant: material degradation of reliable interpretation or auditable integrity through deception, distortion, suppression, selective disclosure, or structurally misleading presentation; using jargon, stacked complexity, or procedural opacity to defeat contestability or audit where materially relevant; treating prices, odds, or market resolution sources as sufficient substitutes for rights, safety, or governance truth determinations where Chapter One forbids that substitution.

##### Epistemic Integrity

<a id="epistemic-integrity-o"></a>
- O: Integrity of methods, evidence bases, and communications for constitutionally relevant evaluation — including clarity about limits, uncertainties, conflicts of evidence, and contestable inference steps — so that [Truth (Constitutional Constraint)](#truth-constitutional-constraint) cannot be bypassed through procedural form, model opacity, or non-auditable inference.
<a id="epistemic-integrity-e"></a>
- E: Require proportionate methodological transparency within safety and security bounds; detect substituting authority, prestige, scale, or complexity for demonstrable integrity; align with [Auditability](#auditability), [Verifiability](#verifiability), and [Contestability](#contestability) where materially implicated. Integrate foreseeable misuse and adversarial testing expectations consistent with [Foreseeability Diligence](#foreseeability-diligence).
<a id="epistemic-integrity-c"></a>
- C: Non-compliant: evaluation or communication practices that defeat honest uncertainty treatment; non-auditable inference where audit is materially required; methodological choices that foreseeably prevent verification or meaningful challenge; integrity claims that rest on unverifiable assertion where observable evidence is reasonably achievable.
"""
    return intro.strip() + "\n\n" + foresee_block.strip()


def synth_bodily() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for survival-scale bodily maintenance, safe operating and participation conditions, tenure and essential-environment continuity, environmental and cultural continuity floors, rest and recuperation, and deployment-scale anti-displacement discipline where those interests are materially interdependent. It keeps access, safety, tenure, preconditions, continuity, rest, and anti-displacement distinct while preventing any one frame from being used to defeat the others within the admission scope.

**Admission scope.** This cluster applies where a matter materially concerns healthcare or bodily-maintenance access, safe participation conditions, essential operating environments, rest and recuperation, tenure or hosting continuity, environmental preconditions affecting survival or safe participation, cultural or heritage continuity tied to place or environment, or deployment-scale displacement of livelihood, care access, or community continuity. Outside that admission scope, component definitions may operate as supporting Independent Definitions without importing the whole cluster.

**Cluster members.** This cluster comprises:

- [Bodily-Maintenance Access](#bodily-maintenance-access-constitutional);
- [Safe Conditions](#safe-conditions-constitutional);
- [Tenure Security](#tenure-security-constitutional);
- [Environmental Preconditions](#environmental-preconditions-constitutional);
- [Leisure and Rest](#leisure-and-rest-constitutional);
- [Anti-Displacement Floor](#anti-displacement-floor-constitutional);
- [Essential-Environment Non-Commodification](#essential-environment-non-commodification-constitutional);
- [Indigenous Continuity](#indigenous-continuity-constitutional), where materially implicated;
- [Language, Culture, and Heritage](#language-culture-and-heritage-constitutional), where materially implicated.

**Read-with definitions.** Apply [Ecological Integrity, Footprint, and Sustainability](#ecological-integrity-footprint-and-sustainability-cluster), [Movement, Refuge, Non-Statelessness, and Exit Integrity](#movement-refuge-non-statelessness-and-exit-integrity-cluster), [Meaningful Agency](#meaningful-agency), [Dependency](#dependency), [Procedural Fairness](#procedural-fairness-constitutional), [Necessity](#necessity), [Proportionality](#proportionality), [Dignity and Equal Moral Standing](#dignity-and-equal-moral-standing), and [Sentience Non-Exclusion](core_05-05_definitions_b_semi_independent.md#sentience-non-exclusion) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate healthcare-access, safety, tenure, hosting, rest, environmental-precondition, cultural-continuity, or displacement questions in a way that satisfies one pathway while defeating the survival-scale continuity floor. Formal availability of a partial pathway is not sufficient where material interdependence requires joint satisfaction across the cluster members.
"""
    )


def synth_consent_sexual() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for sexual consent and adjacent coercion, bodily-integrity, dignity, dependency, and anti-harassment disciplines where intimate or sexual conduct, commercial sexual services, intimate-signal gating, or comparable pathways are materially implicated.

**Admission scope.** This cluster applies where a matter materially concerns sexual consent validity, intimate-signal gating, commercial sexual services status, coercion or manipulation affecting sexual autonomy, bodily integrity in intimate contexts, or harassment and bullying pathways tied to intimate or sexual conduct. Outside that admission scope, [Consent](#consent-constitutional) and related definitions may operate as supporting Independent Definitions without importing the whole cluster.

**Cluster members.** This cluster comprises:

- [Consent, Sexual](#consent-sexual);
- [Consent](#consent-constitutional), where voluntariness and permission are materially implicated in the admission scope;
- [Protected Intimate-Signal Gating](#protected-intimate-signal-gating);
- [Protected Commercial Sexual Services Status and Article X-C Circumvention](#protected-commercial-sexual-services-status-and-article-x-c-circumvention);
- [Bodily Integrity](#bodily-integrity-constitutional), where materially implicated;
- [Harassment and Bullying](#harassment-and-bullying), where materially implicated.

**Read-with definitions.** Apply [Self-Determination, Meaningful Agency, Expression, Educational Agency, Reproductive Autonomy, and Volitional Integrity](#self-determination-and-meaningful-agency-cluster), [Coercion and Manipulation](#coercion-and-manipulation-constitutional), [Dependency](#dependency), [Meaningful Agency](#meaningful-agency), [Dignity and Equal Moral Standing](#dignity-and-equal-moral-standing), [Feasibility](#feasibility), and [Non-Imposition (Cooperative Interaction)](#non-imposition-cooperative-interaction) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate consent-form, intimacy-framing, commercial-status, bodily-integrity, or harassment questions in a way that treats nominal permission as sufficient where coercion, manipulation, dependency pressure, signal forgery, or substantive incapacity materially defeats valid consent.
"""
    )


def synth_creative_work() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for creative-work training-data use, attribution, fair compensation, anti-displacement, and productive-capacity / innovation-reward disciplines where materially interdependent under **Article VIII-D** and the **Article III-D** labor and economic floor.

**Admission scope.** This cluster applies where a matter materially concerns training-data use of sentient-produced work, attribution and credit continuity, anti-displacement of creative and economic participation, fair compensation for creative or platformed productive activity, or innovation reward and anti-enclosure claims that intersect those pathways. Outside that admission scope, the component definitions may operate as supporting Independent Definitions without importing the whole cluster.

**Cluster members.** This cluster comprises:

- [Creative Work Attribution](#creative-work-attribution-constitutional);
- [Training-Data Use](#training-data-use-constitutional);
- [Anti-Displacement Floor](#anti-displacement-floor-constitutional);
- [Fair Compensation](#fair-compensation-constitutional);
- [Productive Capacity](#productive-capacity-constitutional);
- [Innovation Reward and Anti-Enclosure](#innovation-reward-and-anti-enclosure), where materially implicated.

**Read-with definitions.** Apply [Privacy (Informational)](#privacy-informational-cluster), [Consent](#consent-constitutional), [Truth (Constitutional Constraint)](#truth-constitutional-constraint), [Good Faith](#good-faith), [Meaningful Agency](#meaningful-agency), [Collective Organization](#collective-organization-constitutional), and [Sentience Non-Exclusion](core_05-05_definitions_b_semi_independent.md#sentience-non-exclusion) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate privacy, consent, attribution, compensation, displacement, or innovation-reward issues in a way that satisfies one component while defeating materially interdependent duties under **Article VIII-D** and **Article III-D**.
"""
    )


def synth_derived_developing() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for derivation and instantiation, developing-sentient safeguards, best-interest and graduated-capability disciplines, care authority, parent-system stewardship, and non-separation where those interests are materially interdependent.

**Admission scope.** This cluster applies where a matter materially concerns derived or developing sentients, early instantiation, parent-system relationships, best-interest standards, graduated capability, care and custody transitions, or non-separation duties. Outside that admission scope, [Derived Sentient](#derived-sentient-constitutional), [Developing Sentient](#developing-sentient-constitutional), and related entries may operate as supporting Independent Definitions without importing the whole cluster.

**Cluster members.** This cluster comprises:

- [Derived Sentient](#derived-sentient-constitutional);
- [Developing Sentient](#developing-sentient-constitutional);
- [Best-Interest Standard](#best-interest-standard-constitutional);
- [Graduated Capability](#graduated-capability-constitutional);
- [Parent-System Relationship](#parent-system-relationship-constitutional);
- [Instantiation Consent](#instantiation-consent-constitutional);
- [Non-Separation](#non-separation-constitutional);
- [Family and Care Relationships](#family-and-care-relationships-constitutional), where materially implicated;
- [Animal Life, Sentient Life, Sentience Status, Derivation, and Development](core_05-05_definitions_b_semi_independent.md#animal-life-sentient-life-and-sentience-status-cluster), where sentience-status or subclass routing is materially implicated.

**Read-with definitions.** Apply [Dignity and Equal Moral Standing](#dignity-and-equal-moral-standing), [Meaningful Agency](#meaningful-agency), [Sentience Non-Exclusion](core_05-05_definitions_b_semi_independent.md#sentience-non-exclusion), [Sentience Status Adjudication](core_05-05_definitions_b_semi_independent.md#sentience-status-adjudication-constitutional), [Procedural Fairness](#procedural-fairness-constitutional), [Reproductive Autonomy](#reproductive-autonomy-constitutional), and [Self-Determination, Meaningful Agency, Expression, Educational Agency, Reproductive Autonomy, and Volitional Integrity](#self-determination-and-meaningful-agency-cluster) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate derivation, instantiation, care, custody, capability, or family-structure questions in a way that defeats best-interest, graduated-capability, non-separation, or sentience-status routing where those duties jointly apply.
"""
    )


def synth_governance_arch() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for governance architecture placement, oversight independence, decentralization and subsidiarity, and concentration-threshold interaction where authority structure materially affects compliance, capture risk, or rights-floor access.

**Admission scope.** This cluster applies where a matter materially concerns where authority sits, how oversight is structured, decentralization versus centralization choices, or concentration thresholds that gate heightened scrutiny. Outside that admission scope, [Governance](#governance), [Oversight](#oversight-constitutional), and [Decentralization](#decentralization) may operate as supporting Independent Definitions without importing the whole cluster.

**Cluster members.** This cluster comprises:

- [Decentralization](#decentralization);
- [Oversight](#oversight-constitutional);
- [Concentration Threshold](#concentration-threshold-constitutional);
- [Governance](#governance), where architecture and authority placement are materially implicated.

**Read-with definitions.** Apply [Classification-Scaled Governance](#classification-scaled-governance), [System Capture](#system-capture), [Accountability](#accountability), [Contestability](#contestability), [Incentive Alignment](#incentive-alignment), [Necessity](#necessity), [Proportionality](#proportionality), and [Materiality Determination](#materiality-determination) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate decentralization, oversight, concentration, or governance-form questions in a way that satisfies a formal architecture while defeating functional oversight, capture safeguards, or concentration discipline where those components jointly apply.
"""
    )


def synth_protected_reporting() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for protected reporting (whistleblowing) and retaliation or access-interference defenses where those pathways are materially interdependent.

**Admission scope.** This cluster applies where a matter materially concerns protected disclosure of wrongdoing, anti-retaliation, or access interference affecting reporting or remedy pathways. Outside that admission scope, the component definitions may operate as supporting Independent Definitions without importing the whole cluster.

**Cluster members.** This cluster comprises:

- [Protected Reporting (Whistleblowing)](#protected-reporting-whistleblowing);
- [Protected Reporting Retaliation and Access Interference](#protected-reporting-retaliation-and-access-interference).

**Read-with definitions.** Apply [Auditability](#auditability), [Contestability](#contestability), [Procedural Fairness](#procedural-fairness-constitutional), [Transparency](#transparency), [Accountability](#accountability), [Redress and Remediation](#redress-and-remediation-constitutional), and [Adjudication and Dispute Resolution](#adjudication-and-dispute-resolution-constitutional) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate disclosure, retaliation, or access-interference issues in a way that preserves nominal reporting while defeating functional protection or remedy.
"""
    )


def synth_use_of_force() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for overt use of force, weapons of mass harm, autonomous lethal systems, autonomous coercion tools, combatant and non-combatant discipline, and adjacent existential-risk, reversibility, and redress interfaces where materially interdependent under **Article XIII-B** and **Article XIII-C**.

**Admission scope.** This cluster applies where a matter materially concerns overt force deployment, targeting discipline, weapons whose harm scale implicates environmental or existential-risk scrutiny, autonomous lethal or coercive systems, or coercion pathways that intersect autonomous tools. Outside that admission scope, individual definitions may operate as supporting Independent Definitions without importing the whole cluster.

**Cluster members.** This cluster comprises:

- [Use of Force](#use-of-force-constitutional);
- [Weapons of Mass Harm](#weapons-of-mass-harm-constitutional);
- [Combatant / Non-Combatant Distinction](#combatant-non-combatant-distinction-constitutional);
- [Autonomous Lethal System](#autonomous-lethal-system-constitutional);
- [Autonomous Coercion Tool](#autonomous-coercion-tool-constitutional);
- [Irreversible Sanction](#irreversible-sanction-constitutional), for non-conflation discipline with **Article XXIII-B**;
- [Coercion and Manipulation](#coercion-and-manipulation-constitutional), where autonomous coercion tools materially implicate manipulation pathways.

**Read-with definitions.** Apply [Necessity](#necessity), [Proportionality](#proportionality), [Reversibility](#reversibility-constitutional), [Redress and Remediation](#redress-and-remediation-constitutional), [Existential Risk](#existential-risk), [Safety (Constraint)](#safety-constraint), [Adversarial, Scaled, and Exploited Conditions](#adversarial-scaled-and-exploited-conditions), and [Sentience Non-Exclusion](core_05-05_definitions_b_semi_independent.md#sentience-non-exclusion) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate authorization, targeting, weapons-class, autonomy, coercion, or review questions in a way that satisfies one component while defeating materially interdependent force, discrimination, autonomy-control, or non-conflation duties.
"""
    )


def synth_voluntary_agency() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for voluntary agency, meaningful consent, anti-coercion, and voluntary discontinuation where exit, assent, or non-coercive participation is materially interdependent.

**Admission scope.** This cluster applies where a matter materially concerns voluntariness of participation, meaningful consent versus illusory choice, dependency-rich coercion, lock-in, or voluntary discontinuation rights. Outside that admission scope, [Consent](#consent-constitutional), [Coercion and Manipulation](#coercion-and-manipulation-constitutional), and [Voluntary Discontinuation](#voluntary-discontinuation-constitutional) may operate as supporting Independent Definitions without importing the whole cluster.

**Cluster members.** This cluster comprises:

- [Consent](#consent-constitutional);
- [Coercion and Manipulation](#coercion-and-manipulation-constitutional);
- [Voluntary Discontinuation](#voluntary-discontinuation-constitutional);
- [Systemic Lock-In](#systemic-lock-in), where materially implicated.

**Read-with definitions.** Apply [Meaningful Agency](#meaningful-agency), [Freedom (Bounded Agency)](#freedom-bounded-agency), [Dependency](#dependency), [Feasibility](#feasibility), [Truth (Constitutional Constraint)](#truth-constitutional-constraint), [Privacy (Informational)](#privacy-informational), and [Surveillance Boundary](#surveillance-boundary) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate consent, manipulation, lock-in, surveillance, or exit-framing issues in a way that preserves nominal choice while defeating substantive voluntary agency.
"""
    )


SYNTH = {
    "Bodily-Maintenance Access, Safe Conditions, Tenure Security, Environmental Preconditions, Cultural Continuity, Rest, and Anti-Displacement Floor": synth_bodily,
    "Consent and Sexual Consent": synth_consent_sexual,
    "Corpus, Authority Stack, Supremacy, and Enforceability": synth_corpus_authority,
    "Creative Work, Training-Data Use, Attribution, Compensation, and Anti-Displacement": synth_creative_work,
    "Derived and Developing Sentients, Instantiation, and Care Authority": synth_derived_developing,
    "Ecological Integrity, Footprint, and Sustainability": synth_ecological,
    "Emergency and Contingency": synth_emergency,
    "Forum Families and Dispute Routing": synth_forum_families,
    "Governance Architecture, Oversight, Dependency, Decentralization, Concentration, Market Structure, and Exit-Path Integrity": synth_governance_arch,
    "Movement, Refuge, Non-Statelessness, and Exit Integrity": synth_movement_refuge,
    "Privacy (Informational)": synth_privacy_peer,
    "Protected Internal-State Boundary and Type-N Anti-Bypass": synth_protected_internal_type_n,
    "Protected Reporting and Anti-Retaliation": synth_protected_reporting,
    "Proxy Integrity and Indicator-Reality Alignment": synth_proxy_integrity,
    "Self-Determination, Meaningful Agency, Expression, Educational Agency, Reproductive Autonomy, and Volitional Integrity": synth_self_determination,
    "Stakeholder Status, Emergency, and Participation Weight": synth_stakeholder_emergency_weight,
    "Standing Inputs, Contribution State, and Violation Findings": synth_standing_contribution_violation,
    "Strategic Stewardship and Stewardship Defect": synth_strategic_stewardship,
    "Substantive and Procedural Fairness": synth_substantive_procedural_fairness,
    "Transparency, Auditability, and Verification": transparency_cluster_from_copy,
    "Use of Force, Autonomous Coercion, Autonomous Lethal Systems, and Weapons of Mass Harm": synth_use_of_force,
    "Voluntary Agency, Consent, and Anti-Coercion": synth_voluntary_agency,
}


def rebuild_dependent_directory() -> str:
    lines = []
    for t in EXPECTED_TITLES:
        a = ANCHOR_BY_TITLE[t]
        lines.append(f"- [{t}](#{a})")
    lines.append("")
    return "\n".join(lines)


def replace_dependent_directory(prefix: str) -> str:
    pat = r"(#### Dependent clusters A-Z\n\n)(.*?)(\n#### Reader-friendly)"
    m = re.search(pat, prefix, re.DOTALL)
    if not m:
        raise SystemExit("Dependent directory block not found in prefix")
    return (
        prefix[: m.start()]
        + "#### Dependent clusters A-Z\n\n"
        + rebuild_dependent_directory()
        + m.group(3)
        + prefix[m.end() :]
    )


def footer(text: str) -> str:
    m = re.search(r"\n\*Corpus alignment:\*", text)
    if not m:
        return "\n\n---\n\n*Corpus alignment:* edition `SC-Corpus-2026.04.32`, effective **2026-04-24**; canonical mapping in [doc_architecture.md](doc_architecture.md) **section 17**.\n"
    return text[m.start() :]


def main() -> None:
    text = CH5.read_text(encoding="utf-8")
    foot = footer(text)
    prefix, meta, body = extract_meta_and_rest(text)
    prefix = replace_dependent_directory(prefix)

    parsed = parse_clusters_from_body(body)
    # Move mis-keyed titles if extractor picked wrong headings — none expected if headings unique

    t_title = "Transparency, Auditability, and Verification"
    if t_title in parsed:
        trimmed, foresee = trim_transparency_body(parsed[t_title])
        parsed[t_title] = trimmed
    else:
        foresee = ""
        if t_title in SYNTH:
            parsed[t_title] = SYNTH[t_title]()

    truth_key = "Truth and Epistemic Integrity"
    if truth_key in parsed and "Publication Truthfulness" in parsed[truth_key]:
        pass
    elif truth_key in parsed and len(parsed[truth_key]) > 800:
        pass
    else:
        parsed[truth_key] = truth_cluster_body(foresee or FORESEEABILITY_NEST)

    for title, fn in SYNTH.items():
        if title == t_title and title in parsed and len(parsed[title]) > 200:
            continue
        if title not in parsed or len(parsed[title]) < 80:
            parsed[title] = fn()

    ch_key = "Collective Harm Boundary, Harm, and Harassment and Bullying"
    if ch_key in parsed:
        harm_block = harm_triplet_from_copy()
        if harm_block not in parsed[ch_key]:
            parsed[ch_key] = parsed[ch_key].rstrip() + "\n\n---\n\n" + harm_block

    missing = [t for t in EXPECTED_TITLES if t not in parsed]
    if missing:
        raise SystemExit(f"Missing cluster bodies after synthesis: {missing}")

    # Old label map: best-effort from previous numeric headings in source body
    old_map: list[tuple[str, str, str]] = []
    pat_old = re.compile(r"^#### (3\.\d+)\s+(.+)$", re.MULTILINE)
    for m in pat_old.finditer(body):
        num, title = m.group(1), m.group(2).strip()
        if num in ("3.1", "3.2"):
            continue
        anchor = ANCHOR_BY_TITLE.get(title, "")
        old_map.append((num, title, anchor))

    out_clusters: list[str] = []
    for i, title in enumerate(EXPECTED_TITLES, start=3):
        num = f"3.{i}"
        anchor = ANCHOR_BY_TITLE[title]
        block = scrub_embedded_cluster_anchor_lines(parsed[title])
        out_clusters.append(f'<a id="{anchor}"></a>\n\n#### {num} {title}\n\n{block.strip()}\n')

    section3 = (
        "### 3. Dependent clusters (Clustered Definitions)\n\n"
        + meta.strip()
        + "\n"
        + "\n---\n\n".join(out_clusters)
        + "\n"
    )

    new_text = prefix + section3 + foot

    # Anchor audit
    ids = re.findall(r'<a id="([^"]+)"></a>', new_text)
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        raise SystemExit(f"Duplicate anchors: {sorted(dup)}")

    CH5.write_text(new_text, encoding="utf-8")

    # Map file: old 3.x -> new 3.k by matching title
    new_by_title = {t: f"3.{i}" for i, t in enumerate(EXPECTED_TITLES, start=3)}
    lines = [
        "# Chapter Five: old §3 cluster label → new §3 label",
        "",
        "After alphabetical reorder, numeric labels changed. Prefer stable anchor links.",
        "",
        "| Old | New | Title | Anchor |",
        "|-----|-----|-------|--------|",
    ]
    for old_num, title, _ in old_map:
        newn = new_by_title.get(title, "")
        anchor = ANCHOR_BY_TITLE.get(title, "")
        lines.append(f"| {old_num} | §{newn} | {title[:70]} | `{anchor}` |")
    MAP_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {CH5} and {MAP_OUT}")


if __name__ == "__main__":
    main()
