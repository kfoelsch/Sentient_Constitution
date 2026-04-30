#!/usr/bin/env python3
"""One-off patch: remove alphabetical locator stub blocks from Ch5 §2 (see doc / rule)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "core_05-05_definitions_a_independent.md"
text = PATH.read_text(encoding="utf-8")

REMOVALS: list[str] = [
    # Duplicate id (full entry lives earlier in §2)
    """---

<a id="foundational-constitutional-choice"></a>

---

""",
    """---

<a id="ecological-integrity"></a>
#### Ecological Integrity

The canonical O/E/C statement for **Ecological Integrity** lives in the [Ecological Integrity, Footprint, and Sustainability cluster](#ecological-integrity-footprint-and-sustainability-cluster). This retained title is an alphabetical locator stub only.

<a id="educational-agency"></a>
#### Educational Agency

<a id="educational-agency"></a>
The canonical O/E/C statement for **Educational Agency** lives in the [Self-Determination, Meaningful Agency, Expression, Educational Agency, Reproductive Autonomy, and Volitional Integrity cluster](#self-determination-and-meaningful-agency-cluster). This retained title is an alphabetical locator stub only.

---

""",
    """---

<a id="epistemic-integrity"></a>

#### Epistemic Integrity

The canonical O/E/C statement for **Epistemic Integrity** lives in the [Truth and Epistemic Integrity cluster](#truth-and-epistemic-integrity-cluster). This retained title is an alphabetical locator stub only.

---

<a id="expression-constitutional"></a>

#### Expression

The canonical O/E/C statement for **Expression** lives in the [Self-Determination, Meaningful Agency, Expression, Educational Agency, Reproductive Autonomy, and Volitional Integrity cluster](#self-determination-and-meaningful-agency-cluster). This retained title is an alphabetical locator stub only.

---

""",
    """---

<a id="intergenerational-responsibility-constitutional"></a>
#### Intergenerational Responsibility

The canonical O/E/C statement for **Intergenerational Responsibility** lives in the [Ecological Integrity, Footprint, and Sustainability cluster](#ecological-integrity-footprint-and-sustainability-cluster). This retained title is an alphabetical locator stub only.

---

""",
    """

<a id="meaningful-agency"></a>

#### Meaningful Agency

The canonical O/E/C statement for **Meaningful Agency** lives in the [Self-Determination, Meaningful Agency, Expression, Educational Agency, Reproductive Autonomy, and Volitional Integrity cluster](#self-determination-and-meaningful-agency-cluster). This retained title is an alphabetical locator stub only.

""",
    """---

<a id="privacy-informational"></a>

#### Privacy (Informational)

<a id="privacy-informational-e"></a>
<a id="privacy-informational-c"></a>
The canonical O/E/C statement for **Privacy (Informational)** lives in the [Privacy (Informational) cluster](#privacy-informational-cluster). This retained title is an alphabetical locator stub only.

---

<a id="procedural-fairness-constitutional"></a>

#### Procedural Fairness

<a id="procedural-fairness-constitutional-e"></a>
<a id="procedural-fairness-constitutional-c"></a>
The canonical O/E/C statement for **Procedural Fairness** lives in the [Substantive and Procedural Fairness cluster](#substantive-and-procedural-fairness-cluster). This retained title is an alphabetical locator stub only.

---

""",
    """---

<a id="protected-internal-state-boundary-constitutional"></a>

#### Protected Internal-State Boundary

<a id="protected-internal-state-boundary-constitutional-e"></a>
<a id="protected-internal-state-boundary-constitutional-c"></a>
The canonical O/E/C statement for **Protected Internal-State Boundary** lives in the [Protected Internal-State Boundary and Type-N Anti-Bypass cluster](#protected-internal-state-boundary-and-type-n-anti-bypass-cluster). This retained title is an alphabetical locator stub only.

<a id="protected-internal-state-reconstruction-and-correlational-bypass"></a>
#### Protected Internal-State Reconstruction and Correlational Bypass

<a id="protected-internal-state-reconstruction-and-correlational-bypass-e"></a>
<a id="protected-internal-state-reconstruction-and-correlational-bypass-c"></a>
The canonical O/E/C statement for **Protected Internal-State Reconstruction and Correlational Bypass** lives in the [Protected Internal-State Boundary and Type-N Anti-Bypass cluster](#protected-internal-state-boundary-and-type-n-anti-bypass-cluster). This retained title is an alphabetical locator stub only.

<a id="protected-reporting-whistleblowing"></a>
#### Protected Reporting (Whistleblowing)

<a id="protected-reporting-whistleblowing-e"></a>
<a id="protected-reporting-whistleblowing-c"></a>
The canonical O/E/C statement for **Protected Reporting (Whistleblowing)** lives in the [Protected Reporting and Anti-Retaliation cluster](#protected-reporting-and-anti-retaliation-cluster). This retained title is an alphabetical locator stub only.

<a id="protected-reporting-retaliation-and-access-interference"></a>

#### Protected Reporting Retaliation and Access Interference

<a id="protected-reporting-retaliation-and-access-interference-e"></a>
<a id="protected-reporting-retaliation-and-access-interference-c"></a>
The canonical O/E/C statement for **Protected Reporting Retaliation and Access Interference** lives in the [Protected Reporting and Anti-Retaliation cluster](#protected-reporting-and-anti-retaliation-cluster). This retained title is an alphabetical locator stub only.

---

""",
    """<a id="proxy-divergence"></a>

#### Proxy Divergence

<a id="proxy-divergence-e"></a>
<a id="proxy-divergence-c"></a>
The canonical O/E/C statement for **Proxy Divergence** lives in the [Proxy Integrity and Indicator-Reality Alignment cluster](#proxy-integrity-and-indicator-reality-alignment-cluster). This retained title is an alphabetical locator stub only.

<a id="proxy-metric-gaming-and-indicator-reality-gaps"></a>
#### Proxy Metric Gaming and Indicator-Reality Gaps

<a id="proxy-metric-gaming-and-indicator-reality-gaps-e"></a>
<a id="proxy-metric-gaming-and-indicator-reality-gaps-c"></a>
The canonical O/E/C statement for **Proxy Metric Gaming and Indicator-Reality Gaps** lives in the [Proxy Integrity and Indicator-Reality Alignment cluster](#proxy-integrity-and-indicator-reality-alignment-cluster). This retained title is an alphabetical locator stub only.

---

""",
    """---

<a id="reproductive-autonomy-constitutional"></a>

#### Reproductive Autonomy

The canonical O/E/C statement for **Reproductive Autonomy** lives in the [Self-Determination, Meaningful Agency, Expression, Educational Agency, Reproductive Autonomy, and Volitional Integrity cluster](#self-determination-and-meaningful-agency-cluster). This retained title is an alphabetical locator stub only.

---

""",
    """---

<a id="self-determination-constitutional"></a>

#### Self-Determination

The canonical O/E/C statement for **Self-Determination** lives in the [Self-Determination, Meaningful Agency, Expression, Educational Agency, Reproductive Autonomy, and Volitional Integrity cluster](#self-determination-and-meaningful-agency-cluster). This retained title is an alphabetical locator stub only.

""",
    """---

<a id="stewardship-defect-constitutional"></a>

#### Stewardship Defect

<a id="stewardship-defect-constitutional-e"></a>
<a id="stewardship-defect-constitutional-c"></a>
The canonical O/E/C statement for **Stewardship Defect** lives in the [Strategic Stewardship and Stewardship Defect cluster](#strategic-stewardship-and-stewardship-defect-cluster). This retained title is an alphabetical locator stub only.

---

<a id="decentralization"></a>
<a id="strategic-stewardship-obligation-constitutional"></a>

#### Strategic Stewardship Obligation

<a id="strategic-stewardship-obligation-constitutional-e"></a>
<a id="strategic-stewardship-obligation-constitutional-c"></a>
The canonical O/E/C statement for **Strategic Stewardship Obligation** lives in the [Strategic Stewardship and Stewardship Defect cluster](#strategic-stewardship-and-stewardship-defect-cluster). This retained title is an alphabetical locator stub only.

---

""",
    """<a id="substantive-fairness-constitutional"></a>

#### Substantive Fairness

<a id="substantive-fairness-constitutional-e"></a>
<a id="substantive-fairness-constitutional-c"></a>
The canonical O/E/C statement for **Substantive Fairness** lives in the [Substantive and Procedural Fairness cluster](#substantive-and-procedural-fairness-cluster). This retained title is an alphabetical locator stub only.

""",
    """<a id="surveillance-boundary"></a>
#### Surveillance Boundary

The canonical O/E/C statement for **Surveillance Boundary** lives in the [Privacy (Informational) cluster](#privacy-informational-cluster). This retained title is an alphabetical locator stub only.

<a id="sustainability"></a>
#### Sustainability

The canonical O/E/C statement for **Sustainability** lives in the [Ecological Integrity, Footprint, and Sustainability cluster](#ecological-integrity-footprint-and-sustainability-cluster). This retained title is an alphabetical locator stub only.

""",
    """---

<a id="training-data-use"></a>
#### Training-Data Use

The canonical O/E/C statement for **Training-Data Use** lives in the [Privacy (Informational) cluster](#privacy-informational-cluster). This retained title is an alphabetical locator stub only.

---

<a id="transparency"></a>
#### Transparency

The canonical O/E/C statement for **Transparency** lives in the [Transparency, Auditability, and Verification cluster](#transparency-auditability-and-verification-cluster). This retained title is an alphabetical locator stub only.

---

""",
    """<a id="truth-constitutional-constraint"></a>

#### Truth (Constitutional Constraint)

The canonical O/E/C statement for **Truth (Constitutional Constraint)** lives in the [Truth and Epistemic Integrity cluster](#truth-and-epistemic-integrity-cluster). This retained title is an alphabetical locator stub only.

---

""",
    """---

<a id="voluntary-discontinuation-constitutional"></a>

#### Voluntary Discontinuation

The canonical O/E/C statement for **Voluntary Discontinuation** lives in the [Voluntary Agency, Consent, and Anti-Coercion cluster](#voluntary-agency-consent-and-anti-coercion-cluster). This retained title is an alphabetical locator stub only.

<a id="voluntary-discontinuation-constitutional-e"></a>
<a id="voluntary-discontinuation-constitutional-c"></a>

---""",
]

for i, old in enumerate(REMOVALS):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"Removal block {i}: expected 1 occurrence, found {count}")
    text = text.replace(old, "", 1)

PATH.write_text(text, encoding="utf-8")
print("OK: core_05-05_definitions_a_independent.md updated")
