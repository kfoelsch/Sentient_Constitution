"""Additional §3 dependent-cluster bodies for Chapter Five reassembly."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COPY_CH5 = ROOT.parent / "Constitution copy" / "core_05-05_definitions_a_independent.md"


def strip_leading_anchor_lines(s: str) -> str:
    lines = s.splitlines()
    i = 0
    while i < len(lines) and lines[i].strip().startswith("<a id="):
        i += 1
    return "\n".join(lines[i:]).strip()


def harm_triplet_from_copy() -> str:
    if not COPY_CH5.is_file():
        raise SystemExit(f"Expected backup copy at {COPY_CH5} for Harm recovery")
    text = COPY_CH5.read_text(encoding="utf-8")
    m = re.search(
        r"(<a id=\"harm\"></a>\s*\n##### Harm\n.*?"
        r"<a id=\"irreversible-harm-c\"></a>\n"
        r"- C: Triggers highest constraint thresholds\.\n)",
        text,
        re.DOTALL,
    )
    if not m:
        raise SystemExit("Could not extract Harm / Psychological / Irreversible block from Constitution copy")
    return m.group(1).strip() + "\n"


def transparency_cluster_from_copy() -> str:
    """Cluster boilerplate + Transparency through Verification Robustness (Foreseeability nest stays under Truth)."""
    if not COPY_CH5.is_file():
        raise SystemExit(f"Expected backup copy at {COPY_CH5} for Transparency cluster recovery")
    raw = COPY_CH5.read_text(encoding="utf-8")
    m_t = re.search(
        r"#### Transparency\n+\n*(<details>.*?</details>\n\n<br>\n\n"
        r"- O:.*?\n<a id=\"transparency-e\"></a>\n"
        r"- E:.*?\n<a id=\"transparency-c\"></a>\n"
        r"- C:.*?\n)",
        raw,
        re.DOTALL,
    )
    if not m_t:
        raise SystemExit("Could not extract #### Transparency block from Constitution copy")
    trans_inner = '<a id="transparency"></a>\n#### Transparency\n' + m_t.group(1)

    m_audit = re.search(
        r"##### Audit Scope Sufficiency\n.*?"
        r"<a id=\"verification-robustness-c\"></a>\n"
        r"- C: Verification must remain reliable.*?\n",
        raw,
        re.DOTALL,
    )
    if not m_audit:
        raise SystemExit("Could not extract Audit Scope .. Verification Robustness from Constitution copy")
    tail = m_audit.group(0)
    tail = tail.replace(
        "##### Auditability\n",
        '<a id="auditability"></a>\n##### Auditability\n',
        1,
    )
    tail = tail.replace(
        "##### Evaluation Completeness Constraint\n<a id=\"evaluation-completeness-constraint-e\"></a>",
        '<a id="evaluation-completeness-constraint"></a>\n##### Evaluation Completeness Constraint\n\n'
        "- O: A constraint requiring evaluation and assurance work to cover materially plausible failure, misuse, interaction, and adversarial pathways before compliance claims rest on selectively narrow scenario sets.\n"
        '<a id="evaluation-completeness-constraint-e"></a>',
        1,
    )
    tail = tail.replace(
        "##### Verifiability\n",
        '<a id="verifiability"></a>\n##### Verifiability\n',
        1,
    )
    intro = strip_leading_anchor_lines(
        """
This cluster is the joint-invocation home for disclosure, audit, observability, verification mechanics, and proportionate
assurance depth where Chapters Two through Four require traceable, contestable evidence of system behavior and compliance claims.

**Admission scope.** This cluster applies where a matter materially concerns transparency of materially decision-relevant
behavior, auditability and reconstructor-grade records, evaluation completeness against plausible failure modes, observable
indicators, independent verification, or verification accessibility and independence under scaled or adversarial conditions.
Outside that admission scope, individual entries may still operate as supporting Independent Definitions without importing the whole cluster.

**Cluster members.** This cluster comprises:

- [Transparency](#transparency);
- [Auditability](#auditability);
- [Audit Scope Sufficiency](#audit-scope-sufficiency-e);
- [Evaluation Completeness Constraint](#evaluation-completeness-constraint);
- [Observability](#observability);
- [Verifiability](#verifiability);
- [Verification Accessibility](#verification-accessibility);
- [Verification Feasibility](#verification-feasibility);
- [Verification Independence](#verification-independence);
- [Verification Proportionality](#verification-proportionality);
- [Verification Robustness](#verification-robustness).

**Read-with definitions.** Apply [Accountability](#accountability), [Contestability](#contestability), [Materiality Determination](#materiality-determination), [Risk](#risk), [Safety (Constraint)](#safety-constraint), [Truth (Constitutional Constraint)](#truth-constitutional-constraint), [Epistemic Integrity](#epistemic-integrity), and Chapters Two through Four mechanics where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate
disclosure, logging, metrics, audit sampling, verification UX, or independence questions in a way that satisfies a nominal channel
while defeating practical reconstructability, contestability, or proportionate assurance depth.
"""
    )
    return intro + "\n\n" + trans_inner + "\n\n---\n\n" + tail.strip() + "\n"


def synth_corpus_authority() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for operative corpus identity, authority-stack hierarchy, supremacy within valid adoption scope, and enforceability through observable and contestable compliance assessment.

**Admission scope.** This cluster applies where a matter materially concerns which text is binding, edition custody, supremacy ordering among sources, incorporation scope, or whether claimed obligations are enforceably grounded in the adopted corpus. Outside that admission scope, [Corpus](#corpus) and [Authority Stack and Internal Hierarchy](#authority-stack) may operate as supporting Independent Definitions without importing the whole cluster.

**Cluster members.** This cluster comprises:

- [Corpus](#corpus);
- [Authority Stack and Internal Hierarchy](#authority-stack);
- [Supremacy and Enforceability](#supremacy-and-enforceability);
- [Constitutional Constraint Violation](#constitutional-constraint-violation), where materially implicated in supremacy or custody disputes.

**Read-with definitions.** Apply [Auditability](#auditability), [Contestability](#contestability), [Truth (Constitutional Constraint)](#truth-constitutional-constraint), [Materiality Determination](#materiality-determination), and Chapter Twelve / Chapter Fourteen mechanics where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate labeling, process-artifact, edition-display, or interpretive-gloss questions in a way that treats non-binding material as operative corpus or inverts supremacy ordering without a valid adoption path.
"""
    )


def synth_ecological() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for ecological integrity, footprint discipline, and sustainability pathways where environmental preconditions, intergenerational responsibility, and materially interdependent ecological merits must be evaluated together.

**Admission scope.** This cluster applies where a matter materially concerns ecological state, cumulative or systemic environmental harm, restoration or remediation obligations, footprint accounting, sustainability tradeoffs, or environmental preconditions for sentient wellbeing. Outside that admission scope, [Ecological Integrity](#ecological-integrity-constitutional) and [Sustainability](#sustainability) may operate as supporting Independent Definitions without importing the whole cluster.

**Cluster members.** This cluster comprises:

- [Ecological Integrity](#ecological-integrity-constitutional);
- [Ecological Footprint](#ecological-footprint);
- [Sustainability](#sustainability);
- [Environmental Preconditions](#environmental-preconditions-constitutional), where materially implicated;
- [Intergenerational Responsibility](#intergenerational-responsibility-constitutional), where materially implicated.

**Read-with definitions.** Apply [Material Impact](#material-impact), [Risk](#risk), [Reversibility](#reversibility-constitutional), [Truth (Constitutional Constraint)](#truth-constitutional-constraint), [Transparency](#transparency), and [Safety (Constraint)](#safety-constraint) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate single-metric, single-timescale, or single-jurisdiction views in a way that defeats footprint integrity, precondition discipline, or restoration feasibility where those components jointly apply.
"""
    )


def synth_emergency() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for emergency and contingency pathways across constitutional, stakeholder-system, and pre-deliberation binding-choice layers where time-compressed action must remain reviewable, reversible where feasible, and non-entrenched.

**Admission scope.** This cluster applies where a matter materially concerns declared emergency, contingency operation, stakeholder emergency weighting, or binding collective choice taken before full deliberation completes. Outside that admission scope, [Emergency and Contingency](#emergency-and-contingency-constitutional) may operate as a supporting Independent Definition without importing the whole cluster.

**Cluster members.** This cluster comprises:

- [Emergency and Contingency](#emergency-and-contingency-constitutional);
- [Constitutional Emergency and Contingency](#constitutional-emergency-and-contingency);
- [Stakeholder Emergency and Contingency](#stakeholder-emergency-and-contingency);
- [Emergency Pre-Deliberation Action (Binding Collective Choice)](#emergency-pre-deliberation-action-binding-collective-choice).

**Read-with definitions.** Apply [Governance](#governance), [Force Majeure](#force-majeure-constitutional), [Oversight](#oversight-constitutional), [Contestability](#contestability), [Reversibility](#reversibility-constitutional), [Proportionality](#proportionality), [Necessity](#necessity), and [Auditability](#auditability) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate urgency labeling, procedural shortcut, stakeholder-symbolism, or post-hoc record questions in a way that preserves nominal emergency form while defeating continuation burden, restoration, or challenge pathways required by the cluster members.
"""
    )


def synth_forum_families() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for the six constitutional forum families and primary-stakes routing discipline stated in Chapter Nine, read together with adjudication and dispute-resolution hooks where venue, certification, or cross-family coordination is materially implicated.

**Admission scope.** This cluster applies where a matter materially concerns default venue, primary-stakes characterization, family-to-family transfer or certification, anti-self-judging backup routing, or which forum family’s intake and merits rules govern. Outside that admission scope, individual forum-family entries may still be cited as supporting Independent Definitions without importing the whole cluster.

**Cluster members.** This cluster comprises:

- [Forum Family, Sentient](#forum-family-sentient);
- [Forum Family, Technical](#forum-family-technical);
- [Forum Family, Institutional](#forum-family-institutional);
- [Forum Family, Environment](#forum-family-environment);
- [Forum Family, Integrity](#forum-family-integrity);
- [Forum Family, Constitutional](#forum-family-constitutional);
- [Primary-Stakes Routing](#primary-stakes-routing);
- [Adjudication and Dispute Resolution](#adjudication-and-dispute-resolution-constitutional), where materially implicated in routing or review design.

**Read-with definitions.** Apply [Contestability](#contestability), [Procedural Fairness](#procedural-fairness-constitutional), [Auditability](#auditability), [Materiality Determination](#materiality-determination), [System Capture](#system-capture), and Chapter Eight mechanics where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate caption, intake label, or specialty-panel questions in a way that collapses distinct forum functions or defeats primary-stakes routing, certification, or anti-self-judging backup discipline.

<a id="primary-stakes-routing"></a>
##### Primary-Stakes Routing

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Owner: [Chapter Nine §2](core_09-09_forum.md#2-default-venue-and-primary-stakes); read with [Chapter Nine §5](core_09-09_forum.md#5-intake-triage-mixed-stakes-and-routing-asymmetry), [Chapter Nine §6](core_09-09_forum.md#6-transfer-consolidation-and-coordination), and [Chapter Nine §8](core_09-09_forum.md#7-escalation-and-certification).

</details>

<br>

- O: The routing rule that assigns a matter to the forum family responsible for the matter's main legal, remedial, safeguard, constitutional, or practical stake, rather than the family suggested by the caption, party preference, administrative convenience, or tactical framing.
<a id="primary-stakes-routing-e"></a>
- E: Identify the matter's primary stake from the claim or defense as a whole, including the requested relief, necessary parties, coercive safeguards, constitutional floor, practical effect, and any component question that must be referred, certified, stayed, or coordinated under Chapter Nine.
<a id="primary-stakes-routing-c"></a>
- C: Non-compliant: treating captions, intake labels, specialty-panel labels, funding incentives, or administrative convenience as controlling where they contradict the forum family assigned by Chapter Nine's primary-stakes table, transfer rules, certification rules, or anti-self-judging backup discipline.

<a id="forum-family-sentient"></a>
##### Forum Family, Sentient

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Owner: [Chapter Nine §4.2.1](core_09-09_forum.md#421-sentient-forums); read with [Chapter Six §2.1](core_06-06_standing_assessment.md#2-standing-records-and-verified-inputs) primary-stakes routing.

</details>

<br>

- O: The forum family whose primary stake is sentient-versus-sentient disputes centered on private or community obligations, civil harms, restoration, or local norms, without final resolution of constitutional validity or institutional mandate as the primary question.
<a id="forum-family-sentient-e"></a>
- E: Apply Chapter Nine default-venue and primary-stakes rules together with Chapter Six classification preservation; refuse caption-driven routing that contradicts the primary stake described in Chapter Nine §2’s table row for **Sentient**.
<a id="forum-family-sentient-c"></a>
- C: Non-compliant: collapsing **Sentient** routing into institutional or constitutional final merits where primary-stakes routing under Chapter Nine requires another lead family; using **Sentient** forums as the sole mandatory path where asymmetry or dependency requires **Institutional** or **Integrity** availability per Chapter Nine §5.

<a id="forum-family-technical"></a>
##### Forum Family, Technical

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Owner: [Chapter Nine §4.2.2](core_09-09_forum.md#422-technical-forum-domains).

</details>

<br>

- O: The forum family — including specialized chambers or panels within other families — whose primary stake is technical-governance procedure, expert-evidence standards, knowledge governance, standards stewardship, or bounded uncertainty reduction material to adjudication or regulation.
<a id="forum-family-technical-e"></a>
- E: Distinguish primary technical-administration stakes from rights-, mandate-, or ecological-merits stakes that require another family under Chapter Nine §2; preserve cross-family certification rather than letting technical specialization displace ordinary routing (Chapter Nine §4.5).
<a id="forum-family-technical-c"></a>
- C: Non-compliant: treating technical labels as automatic venue trump over primary-stakes routing; using technical panels to displace lawfully assigned merits authority for non-technical primary questions.

<a id="forum-family-institutional"></a>
##### Forum Family, Institutional

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Owner: [Chapter Nine §4.2.3](core_09-09_forum.md#423-institutional-forums); read with [corpus_institutions.md](corpus_institutions.md) supervised-scope language.

</details>

<br>

- O: The forum family for disputes where an institution is a necessary party or the primary stake is institutional authority, mandate, supervised scope, classification under adopted instruments, or compliance with institutional duties.
<a id="forum-family-institutional-e"></a>
- E: Verify necessary-party and mandate predicates under Chapter Eight §§2 and 5; coordinate with **Integrity** lead defaults for Chapter Seven classification only where Chapter Eight’s collision rules permit.
<a id="forum-family-institutional-c"></a>
- C: Non-compliant: denying **Institutional** routing where the primary stake row in Chapter Nine §2 requires it; using internal process labels to avoid independent merits review where capture or conflict allegations materially require **Integrity** or backup routing.

<a id="forum-family-environment"></a>
##### Forum Family, Environment

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Owner: [Chapter Nine §4.2.4](core_09-09_forum.md#424-environment-forums); read with [Ecological Integrity](#ecological-integrity-constitutional) and [Environmental Preconditions](#environmental-preconditions-constitutional).

</details>

<br>

- O: The forum family whose primary stake is ecological integrity, environmental preconditions, lifecycle or systemic ecological harm, restoration or remediation of shared systems, attributable environmental burdens, or pattern ecological failure material to classification or rights-floor enforcement.
<a id="forum-family-environment-e"></a>
- E: Integrate Chapter Six and Chapter Seven integration hooks with Chapter Nine primary-stakes tests; preserve certification to **Constitutional** forums where validity or structural remedy merges per Chapter Nine §8.
<a id="forum-family-environment-c"></a>
- C: Non-compliant: treating ecological merits as purely private disputes when the primary stake is environmental under Chapter Nine §2; segmenting restoration and preconditions analysis to defeat joint ecological merits evaluation.

<a id="forum-family-integrity"></a>
##### Forum Family, Integrity

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Owner: [Chapter Nine §4.2.5](core_09-09_forum.md#425-integrity-forums); read with Chapter Eight slot assignment due-process cross-references in Chapter Nine §8.

</details>

<br>

- O: The forum family for disputes whose primary stake is integrity of office, process, contest pathways, disclosure, conflict rules, anti-capture duties, or pattern systemic integrity failure across institutions where classification, final Chapter Eight assignment, or rights-floor enforcement depends on that determination — including alignment rulings and coordinated records described in Chapter Nine §4.2.5.
<a id="forum-family-integrity-e"></a>
- E: Apply anti-self-judging backups from Chapter Nine §6 where the forum’s own bias, capture, or concealment is the primary issue; separate alignment-led coordination from provisional operational-law doctrine governed by Chapter Nine §4.3 for other families.
<a id="forum-family-integrity-c"></a>
- C: Non-compliant: using **Integrity** lead to silently displace **Constitutional** certification where structural validity or class-wide remedy requires it; refusing backup routing where Chapter Nine §6’s rule assigns an independent lead family.

<a id="forum-family-constitutional"></a>
##### Forum Family, Constitutional

<details>
<summary><strong><span style="color: #2563eb;">Trace</span></strong></summary>

- Owner: [Chapter Nine §4.2.6](core_09-09_forum.md#426-constitutional-forums); read with [Article XII-B](core_10-10_rights_part_c.md#article-xii-b-right-to-challenge-review-and-redress) certification hooks.

</details>

<br>

- O: The forum family that decides constitutional validity and meaning, structural remedies altering governance for classes of actors or systems, certified questions from other families, and supremacy disputes where constitutional text alone can resolve the certified issue.
<a id="forum-family-constitutional-e"></a>
- E: Preserve Article XXIII-class review safeguards and Chapter Eight due-process hooks when certification or escalation arrives from lower families; distinguish certified constitutional questions from companion operational-law provisional rulings under Chapter Nine §4.3 and §8.
<a id="forum-family-constitutional-c"></a>
- C: Non-compliant: treating non-certifiable operational detail as final constitutional disposition; collapsing certification discipline so families bypass Chapter Nine §8 when constitutional validity, meaning, or structural remedy is materially at stake.
"""
    )


def synth_movement_refuge() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for movement, refuge from non-compliance, non-statelessness, and exit integrity where mobility, hosting continuity, and dependency-sensitive exit are materially interdependent.

**Admission scope.** This cluster applies where a matter materially concerns migration or relocation rights, refuge status from non-compliant jurisdictions, prevention of arbitrary statelessness, or interoperability, portability, and exit integrity for essential environments and digital participation. Outside that admission scope, [Movement and Relocation](#movement-and-relocation-constitutional) and [Refuge from Non-Compliance](#refuge-from-non-compliance-constitutional) may operate as supporting Independent Definitions without importing the whole cluster.

**Cluster members.** This cluster comprises:

- [Movement and Relocation](#movement-and-relocation-constitutional);
- [Refuge from Non-Compliance](#refuge-from-non-compliance-constitutional);
- [Non-Statelessness](#non-statelessness).

**Read-with definitions.** Apply [Dependency](#dependency), [Meaningful Agency](#meaningful-agency), [Procedural Fairness](#procedural-fairness-constitutional), [Safe Conditions](#safe-conditions-constitutional), [Tenure Security](#tenure-security-constitutional), [Article XIX](core_10-10_rights_part_c.md#article-xix-interoperability-portability-and-exit-integrity), and [Materiality Determination](#materiality-determination) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate travel, hosting, platform-exit, or interoperability questions in a way that preserves nominal mobility while defeating refuge, non-statelessness, or exit-integrity protections where those components jointly apply.
"""
    )


def synth_privacy_peer() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the peer-level joint-invocation home for distributed **Privacy (Informational)** coverage across Chapter Ten articles, stated in Chapter Five **section 2** reader navigation and carried here as a dependent cluster for §3.1 discipline.

**Admission scope.** This cluster applies wherever privacy matters materially implicate more than one article-level locus named in the cluster members list. Outside that admission scope, [Privacy (Informational)](#privacy-informational) may operate alone.

**Cluster members.** This cluster comprises the Chapter Five §2.3 enumeration:

- [Article VII-A](core_10-10_rights_part_b.md#article-vii-a-self-ownership-of-body-and-mind);
- [Article VII-B](core_10-10_rights_part_b.md#article-vii-b-internal-state-boundary-and-type-n-protection);
- [Article VIII](core_10-10_rights_part_b.md#article-viii-likeness-experiential-data-and-publication-rights);
- [Article IX-A](core_10-10_rights_part_b.md#article-ix-a-agency-and-freedom-from-manipulation);
- [Article XIII-A](core_10-10_rights_part_c.md#article-xiii-a-security-intelligence-and-covert-power-limits);
- [Privacy (Informational)](#privacy-informational) as the umbrella definition tying the distribution together.

**Read-with definitions.** Apply [Protected Internal-State Boundary](#protected-internal-state-boundary-constitutional), [Consent](#consent-constitutional), [Truth (Constitutional Constraint)](#truth-constitutional-constraint), [Surveillance Boundary](#surveillance-boundary), and **[corpus_systems.md](corpus_systems.md), CS-3** where Type N or comparable handling is implicated.

**Joint invocation and anti-bypass.** Under §3.1, privacy matters within admission scope must not be segmented across articles in a way that satisfies one article’s standard while evading another’s materially implicated discipline; anti-read-across for standard-setting remains as stated in Chapter Five §2.3.
"""
    )


def synth_protected_internal_type_n() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for protected internal-state boundary discipline and Type-N anti-bypass pathways where inference, reconstruction, or operational proxies threaten cognitive or emotional privacy.

**Admission scope.** This cluster applies where a matter materially concerns internal-state inference, Type N handling, protected intimate-signal gating, or security-layer access to states comparable to those protected under Article VII-B. Outside that admission scope, [Protected Internal-State Boundary](#protected-internal-state-boundary-constitutional) may operate alone.

**Cluster members.** This cluster comprises:

- [Protected Internal-State Boundary](#protected-internal-state-boundary-constitutional);
- [Protected Intimate-Signal Gating](#protected-intimate-signal-gating), where materially implicated;
- [Type N](corpus_systems.md) handling cross-references where **CS-3** applies by operation of companion adoption.

**Read-with definitions.** Apply [Privacy (Informational)](#privacy-informational), [Consent](#consent-constitutional), [Epistemic Integrity](#epistemic-integrity), [Truth (Constitutional Constraint)](#truth-constitutional-constraint), [Auditability](#auditability), and [Surveillance Boundary](#surveillance-boundary) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate consent, security, modeling, or redaction questions in a way that reconstructs protected internal states through operationally equivalent means while claiming formal compliance.
"""
    )


def synth_proxy_integrity() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for proxy integrity and indicator–reality alignment where stewards rely on metrics, dashboards, or surrogate indicators for materially rights- or safety-relevant decisions.

**Admission scope.** This cluster applies where a matter materially concerns proxy selection, indicator gaming, divergent proxies, or assurance that measured signals track constitutionally material outcomes. Outside that admission scope, [Proxy Integrity](#proxy-integrity-constitutional) and [Indicator–Reality Alignment](#indicator-reality-alignment-constitutional) may operate as supporting Independent Definitions without importing the whole cluster.

**Cluster members.** This cluster comprises:

- [Proxy Divergence](#proxy-divergence);
- [Proxy Metric Gaming and Indicator-Reality Gaps](#proxy-metric-gaming-and-indicator-reality-gaps).

**Read-with definitions.** Apply [Auditability](#auditability), [Truth (Constitutional Constraint)](#truth-constitutional-constraint), [Materiality Determination](#materiality-determination), [Risk](#risk), [Safety (Constraint)](#safety-constraint), and [Incentive Alignment](#incentive-alignment) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate data-quality, governance-metrics, or narrative-framing questions in a way that optimizes proxies while materially misaligning indicators from the risks or harms they purport to measure.
"""
    )


def synth_self_determination() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for self-determination, meaningful agency, expression, educational agency, reproductive autonomy, and volitional integrity where those freedoms are materially interdependent under Chapter Nine.

**Admission scope.** This cluster applies where a matter materially concerns autonomy of thought, expression, education, reproductive choice, volitional continuity, or manipulation-resistant agency. Outside that admission scope, individual entries such as [Self-Determination](#self-determination-constitutional) may operate alone.

**Cluster members.** This cluster comprises:

- [Self-Determination](#self-determination-constitutional);
- [Meaningful Agency](#meaningful-agency);
- [Expression](#expression-constitutional);
- [Educational Agency](#educational-agency-constitutional);
- [Reproductive Autonomy](#reproductive-autonomy-constitutional);
- [Freedom (Bounded Agency)](#freedom-bounded-agency), where volitional or bounded-agency disciplines materially intersect this cluster.

**Read-with definitions.** Apply [Coercion and Manipulation](#coercion-and-manipulation-constitutional), [Consent](#consent-constitutional), [Privacy (Informational)](#privacy-informational), [Dignity and Equal Moral Standing](#dignity-and-equal-moral-standing), [Dependency](#dependency), and [Truth (Constitutional Constraint)](#truth-constitutional-constraint) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate speech, platform, curricular, reproductive, or surveillance questions in a way that preserves nominal liberty while defeating substantive agency through coercion, manipulation, or informational capture.
"""
    )


def synth_stakeholder_emergency_weight() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for stakeholder status, emergency participation, and participation weight within already-authorized governance structures — distinct from foundational constitutional choice under Chapter Ten.

**Admission scope.** This cluster applies where a matter materially concerns who counts as a stakeholder, how emergency affects stakeholder pathways, or how participation weight scales for materially affected sentients inside an authorized system. Outside that admission scope, [Stakeholder](#stakeholder) may operate alone.

**Cluster members.** This cluster comprises:

- [Stakeholder](#stakeholder);
- [Stakeholder Participation Weight](#stakeholder-participation-weight);
- [Stakeholder Emergency and Contingency](#stakeholder-emergency-and-contingency).

**Read-with definitions.** Apply [Governance](#governance), [Materiality Determination](#materiality-determination), [Dependency](#dependency), [Proportionality](#proportionality), [Feasibility](#feasibility), [Meaningful Agency](#meaningful-agency), [Binding Stakeholder Choice](#binding-stakeholder-choice-cluster), and [Article XI](core_10-10_rights_part_b.md#article-xi-stakeholder-system-participation-representation-and-due-process) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate notice, consultation, weighting, or emergency questions in a way that substitutes symbolic participation for proportionate stakeholder influence or evades restoration duties after contingency measures end.
"""
    )


def synth_standing_contribution_violation() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for contribution state, standing records and effects, verified violation findings, and violation-nature typing under Chapter Six — the definitional interface Chapter Five supplies for Axis I / Axis II vocabulary.

**Admission scope.** This cluster applies where a matter materially concerns standing classification inputs, verified violations, or how violation nature and process/response character interact with forum routing and remedies. Outside that admission scope, individual Chapter Six hooks may be cited without importing the full cluster.

**Cluster members.** This cluster comprises:

- [Contribution State](#contribution-state);
- [Standing Record](#standing-record-chapter-six);
- [Standing Effect](#standing-effect-chapter-six);
- [Violation Nature](#violation-nature-chapter-six);
- [Verified Violation Findings](#verified-violation-findings);
- [Participant Standing](#participant-standing-constitutional), where reputation- or record-based gating intersects Axis I typing.

**Read-with definitions.** Apply [Auditability](#auditability), [Contestability](#contestability), [Materiality Determination](#materiality-determination), [Adjudication and Dispute Resolution](#adjudication-and-dispute-resolution-constitutional), and [Chapter Six §2.1](core_06-06_standing_assessment.md#2-standing-records-and-verified-inputs) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate narrative, procedural, or evidentiary compartments in a way that defeats joint assessment, verified-input gates, or non-substitution discipline required by Chapter Six.
"""
    )


def synth_strategic_stewardship() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for strategic stewardship obligation and stewardship defect where long-horizon custody, incentive alignment, and systemic harm pathways are materially interdependent.

**Admission scope.** This cluster applies where a matter materially concerns institutional or systemic stewardship duties, defective incentive structures, or failures of foresight and proportionality that affect ecological, safety, or rights floors. Outside that admission scope, [Strategic Stewardship Obligation](#strategic-stewardship-obligation-constitutional) may operate alone.

**Cluster members.** This cluster comprises:

- [Strategic Stewardship Obligation](#strategic-stewardship-obligation-constitutional);
- [Stewardship Defect](#stewardship-defect-constitutional);
- [Incentive Alignment](#incentive-alignment), where materially implicated in stewardship evaluation.

**Read-with definitions.** Apply [Existential Risk](#existential-risk), [Safety (Constraint)](#safety-constraint), [Risk](#risk), [Foreseeability Diligence](#foreseeability-diligence), [Materiality Determination](#materiality-determination), and [Accountability](#accountability) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate CSR-narrative, compliance-artifact, or short-horizon incentive questions in a way that masks stewardship defects or defeats proportionate long-horizon safeguards.
"""
    )


def synth_substantive_procedural_fairness() -> str:
    return strip_leading_anchor_lines(
        """This cluster is the joint-invocation home for substantive and procedural fairness where outcome justice and process justice are materially interdependent for the same decision or proceeding.

**Admission scope.** This cluster applies where a matter materially concerns distributive or outcome fairness together with hearing, notice, impartiality, or review procedures — or where segmentation would defeat either dimension. Outside that admission scope, [Substantive Fairness](#substantive-fairness-constitutional) or [Procedural Fairness](#procedural-fairness-constitutional) may operate alone.

**Cluster members.** This cluster comprises:

- [Substantive Fairness](#substantive-fairness-constitutional);
- [Procedural Fairness](#procedural-fairness-constitutional).

**Read-with definitions.** Apply [Contestability](#contestability), [Auditability](#auditability), [Materiality Determination](#materiality-determination), [Dignity and Equal Moral Standing](#dignity-and-equal-moral-standing), [Protected Characteristics](#protected-characteristics-constitutional), and [Redress and Remediation](#redress-and-remediation-constitutional) where materially implicated.

**Joint invocation and anti-bypass.** Under §3.1, a matter within the admission scope must not be segmented into separate outcome-only or procedure-only frames in a way that delivers nominal process while defeating substantive fairness, or substantive labels while defeating meaningful challenge and review.
"""
    )
