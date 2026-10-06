# 제6장: 기초적 권리

<details>
<summary><strong><span style="color: #2563eb;">코퍼스 내 위치(비작동적): 파일 구조와 읽기 규칙</span></strong></summary>

> 다음 내용은 **독자를 위한 안내일 뿐**입니다. 이 파일이나 다른 장의 다른 곳에 있는 구속력 있는 의무를 추가하거나 삭제하거나 축소하지 않습니다.
>
> 이 파일은 **감지자 헌법의 일부**이며, 번호가 부여된 다른 `core_*` 파일과 하나의 문서로 함께 읽을 때에만 **구속력을 가집니다**. 이 파일에는 **제6장 제C부**가 포함되며, 조문 번호와 상호 참조는 통합 문서와 일치합니다. 읽기 순서, 구속력 있는 내용과 보조 내용의 구분, 코퍼스 판 정보는 [README.md](README.md)에 유지됩니다.

</details>

<details>
<summary><strong><span style="color: #2563eb;">독자 안내(비작동적): 제6장에서 제C부의 위치</span></strong></summary>

> 다음 내용은 **독자를 위한 안내일 뿐**입니다. 이 장이나 다른 장의 다른 곳에 있는 구속력 있는 의무를 추가하거나 삭제하거나 축소하지 않습니다.
>
> [core_06_rights_part_a.md](core_06_rights_part_a.md)의 **제A부**에는 장 전체에 적용되는 기본 제약 체계, 지구 우선 읽기 순서, 해석의 중심축이 담겨 있습니다. **제C부**는 그 순서에 따라 **제XIII조부터 제XVIII조**까지 제시합니다.

</details>

<br>

<a id="part-c-trustworthy-systems-security-and-force-limits-information-integrity-verification-lifecycle-and-sandboxed-innovation"></a>
### 제C부: 신뢰할 수 있는 시스템, 보안과 무력의 한계, 정보권역의 무결성, 검증, 수명주기 및 격리된 혁신

<br>

*쉽게 말해: 제C부는 신뢰할 수 있는 시스템, 보안과 무력의 한계, 정보권역의 무결성, 검증, 수명주기 규율, 격리된 혁신을 다룹니다 — 제XIII조부터 제XVIII조까지입니다.*

<details>
<summary><strong><span style="color: #2563eb;">독자 안내(비작동적): 제C부 조문 지도</span></strong></summary>

> 다음 내용은 **독자를 위한 안내일 뿐**입니다. 이 장이나 다른 장의 다른 곳에 있는 구속력 있는 의무를 추가하거나 삭제하거나 축소하지 않습니다.
>
> **독자용 지도(비작동적).** 이 도표는 원문이 이 부의 조문과 하위 조항을 어떻게 묶는지 보여줍니다. 격자는 원문의 분류를 나타낼 뿐 절차 순서가 아닙니다. 조문은 절차 단계가 아니므로 지도에는 화살표가 없습니다. 하위 조항 표시는 주제를 요약합니다. 아래의 번호가 붙은 조문과 하위 조항이 기준이 됩니다. 이 도표는 정의나 의무를 추가하지 않고, 우선순위를 정하지 않으며, 원문을 대신하지 않습니다.

</details>

<br>

```mermaid
flowchart TB
    C0["제C부<br/><br/>신뢰할 수 있는 시스템, 보안과 무력의 한계,<br/>정보권역의 무결성, 검증, 수명주기 및 격리된 혁신"]
    subgraph Cgrid[" "]
        direction TB
        subgraph Crow1["제XIII조–제XIV조"]
            C1["제XIII조 · 신뢰할 수 있는 시스템에 대한 권리<br/><br/>• 신뢰성 기준선<br/>• 이의 제기, 심사 및 구제<br/>• 허위 신뢰의 한계<br/>• 유인 정렬<br/>• 고자율 프로세스의 무결성<br/>• 회복탄력성과 자가 복구"]
            C2["제XIV조 · 보안, 정보활동, 무력 및 자율적 강압 시스템<br/><br/>• 은밀한 권력의 한계<br/>• 무력 사용과 무력 충돌<br/>• 자율적 치명 시스템과 강압 시스템"]
        end
        subgraph Crow2["제XV조–제XVI조"]
            C3["제XV조 · 정보권역의 무결성<br/><br/>• 다원성과 독점 방지<br/>• 투명성과 이의 제기 가능성<br/>• 검증, 보고 및 인식론적 책무"]
            C4["제XVI조 · 감사, 투명성 및 독립적 검증<br/><br/>• 관찰 가능한 증거<br/>• 분산된 감독<br/>• 접근 가능한 검증"]
        end
        subgraph Crow3["제XVII조–제XVIII조"]
            C5["제XVII조 · 시스템 수명주기, 환경 및 되돌릴 수 있음<br/><br/>• 환경 분리<br/>• 점진적 배포와 되돌릴 수 있음<br/>• 오분류와 회피의 결과"]
            C6["제XVIII조 · 격리된 혁신, 실험 및 창작의 자유<br/><br/>• 격리 범위<br/>• 봉쇄, 공개 및 선택적 참여<br/>• 더 높은 의무 체계로의 전환<br/>• 혁신 보상과 폐쇄 방지<br/>• 출판, 심사 및 재현의 무결성"]
        end
    end
    %% 보이지 않는 연결은 두 열의 격자 배치를 고정합니다.
    C0 ~~~ C1 & C2
    C1 ~~~ C3
    C2 ~~~ C4
    C3 ~~~ C5
    C4 ~~~ C6
    style Cgrid fill:none,stroke:none
    style Crow1 fill:none,stroke:none
    style Crow2 fill:none,stroke:none
    style Crow3 fill:none,stroke:none
    style C0 fill:none,stroke:#2563eb,color:#ffffff
    style C1 fill:none,stroke:#16a34a,color:#ffffff
    style C2 fill:none,stroke:#db2777,color:#ffffff
    style C3 fill:none,stroke:#ea580c,color:#ffffff
    style C4 fill:none,stroke:#ea580c,color:#ffffff
    style C5 fill:none,stroke:#16a34a,color:#ffffff
    style C6 fill:none,stroke:#16a34a,color:#ffffff
```

**아래의 제XIII조부터 제XVIII조까지**는 이 기준선을 온전히 규정합니다. 제C부는 신뢰할 수 있는 시스템, 보안, 정보 무결성, 검증, 수명주기, 격리된 혁신의 기준선을 다룹니다.


<a id="article-xiii-right-to-reliable-and-trustworthy-systems"></a>
### 제XIII조: 신뢰할 수 있고 믿을 수 있는 시스템에 대한 권리

<details>
<summary><strong><span style="color: #2563eb;">근거 추적</span></strong></summary>

- 상위 근거: 원칙: 제1장 [§3 근본 목적: 웰빙](core_01_a_values_principles.md#3-foundational-objective-wellbeing-flourishing-aim), [§4 안전](core_01_a_values_principles.md#4-safety-harm-constraint), [§6 신뢰](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), [§13 헌법상 충돌 해결 절차](core_01_b_interaction_interpretation.md#13-constitutional-collision-resolution-process), [§19 유인 정렬과 시스템 포획](core_01_c_stewardship_capacity_principles.md#19-incentive-alignment-and-system-capture).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 준수</span></strong></summary>

- [신뢰성](core_05_band_continuity.md#trustworthiness) · [O](core_05_band_continuity.md#trustworthiness) · [M](core_05_band_continuity.md#trustworthiness-a) · [A](core_05_band_continuity.md#trustworthiness-a) · [C](core_05_band_continuity.md#trustworthiness-c)
- [신뢰](core_05_band_continuity.md#trust) · [O](core_05_band_continuity.md#trust) · [M](core_05_band_continuity.md#trust-a) · [A](core_05_band_continuity.md#trust-a) · [C](core_05_band_continuity.md#trust-c)
- [웰빙](core_05_band_continuity.md#wellbeing) · [O](core_05_band_continuity.md#wellbeing) · [M](core_05_band_continuity.md#wellbeing-a) · [A](core_05_band_continuity.md#wellbeing-a) · [C](core_05_band_continuity.md#wellbeing-c)
- [의존](core_05_band_continuity.md#dependency) · [O](core_05_band_continuity.md#dependency) · [M](core_05_band_continuity.md#dependency-a) · [A](core_05_band_continuity.md#dependency-a) · [C](core_05_band_continuity.md#dependency-c)

</details>

<br>

*쉽게 말해: **제XIII조**(*신뢰할 수 있고 믿을 수 있는 시스템에 대한 권리*)는 신뢰 가능한 시스템의 권리 기준선입니다. 시스템이 삶에 중대한 영향을 미칠 때, 사람은 정직한 방식으로 그 시스템에 의존하고, 한계를 이해하며, 시스템이 실패하면 이의를 제기할 권리가 있습니다. 신뢰는 얻고 지켜야 하는 것이지, 브랜드나 작은 글씨로 만들어내는 것이 아닙니다.*

이 조는 [두 가지 헌법상 목적](core_00_preamble.md#two-constitutional-aims)에 따라 신뢰할 수 있는 시스템에 대한 **헌법상 기준선**을 정합니다. 감독 측정 계열(*헌법상 측정으로서의 신뢰성*)과 함께 읽습니다.

- **번영:** 감지자는 시스템 행동에 관해 합리적인 기대를 형성하고, 한계와 위험을 정직하게 고지받으며, 체계적 기만이나 조작된 의존 없이 참여하고 협력할 수 있습니다.
- **연속성:** 신뢰성은 시간, 규모, 심화되는 의존 관계 전반에서 유지됩니다. 이해관계가 커진다는 이유로 시스템이 조용히 덜 신뢰할 만해지거나, 덜 정직해지거나, 이의를 제기하기 더 어려워져서는 안 됩니다.

정당한 추구는 [헌법상 사원](core_00_preamble.md#constitutional-tetrad)을 따르며, [중대한 이해관계](core_00_preamble.md#material-stake)의 정도에 맞춰야 합니다.

- **참여:** 신뢰할 수 없거나 오해를 부르는 시스템에 이의를 제기하고, 심사·정정·구제를 받는 데서 실현됩니다.
- **감독:** 영향과 의존 정도에 비례하는 감사 가능한 행동, 고지된 한계, 독립적 검증을 통해 이뤄집니다.
- **책임성:** 시스템 운영자는 허위 신뢰나 왜곡된 유인을 만들거나, 시스템에 합리적으로 의존한 감지자에게 중대한 피해를 준 실패에 대해 책임을 져야 합니다.
- **적시성:** 지연으로 인해 신뢰성이나 구제가 사실상 불가능해지기 전에 탐지하고 이의를 제기하며 구제해야 합니다.

감지자는 시스템의 영향, 의존도, 위험에 비례하는 수준으로 신뢰할 수 있고 믿을 만한 시스템과 상호작용할 권리가 있습니다. 그러한 신뢰성은 정보에 근거한 참여와 협력 행동, 웰빙의 보전을 뒷받침합니다. 결과에 중대한 영향을 미치는 경우 신뢰성은 시간, 규모, 의존 관계 전반에서 평가되어야 합니다.

이 권리를 보장하는 두 보호장치가 함께 작동합니다. 인증은 시스템이 신뢰받을 자격을 갖추게 하고, 감지자의 권리는 시스템이 정직성을 유지하도록 합니다.

**인증은 시스템 측에서 신뢰를 구축합니다:** 중요한 시스템이 감지자의 의존 방식에 실질적 영향을 미칠 때 [시스템 정렬 인증](core_05_band_continuity.md#system-alignment-certification-constitutional)이 [제8장](core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification)에 따라 적용됩니다. 인증은 감지자가 다음 사항을 믿고 의존할 수 있는지 확인합니다.

- 시스템이 무엇을 한다고 설명하는지
- 시스템의 한계와 위험
- 시스템에 이의를 제기하는 방법
- 문제가 해결되는 방식

시스템이 **제XIII조**(*신뢰할 수 있고 믿을 수 있는 시스템에 대한 권리*)의 중요성 기준을 충족하면, 인증에는 [제8장 §3.9.6 신뢰성 및 시스템 의존 무결성 평가](core_08_a_system_alignment_certification_evaluation.md#396-trustworthiness-and-system-reliance-integrity-evaluation)에 따른 신뢰성 심사도 포함됩니다.

**이의 제기 가능성은 감지자 측에서 시스템의 정직성을 지킵니다:** 인증은 시스템을 점검하지만 최종 판단권을 갖지는 않습니다. 시스템의 영향을 받는 모든 감지자는 다음 권리를 보유합니다.

- **제XIII-A조**(*신뢰성 및 신뢰 기준선*)에 따라 시스템에 이의를 제기하고 심사를 받을 권리, **제XIII-B조**(*구제 및 시정 권리*)에 따라 구제를 받을 권리
- **제XVI조**(*감사, 투명성 및 독립적 검증*)에 따라 시스템 감사를 받고 독립적으로 확인받을 권리
- 이 조에 명시된 신뢰 가능한 시스템의 권리 기준선에 따른 보호

**지위가 증거는 아닙니다:** 시스템이 인증을 받았거나, 공식적으로 인정되었거나, 널리 이용된다는 사실만으로 이 조의 최소 보호를 충족한다는 뜻은 아닙니다. 그러한 지위는 보호 수준을 낮출 수도 없습니다.

*인접 조문:*

- **적용 시점:** 시스템 행동이 **제6장**의 권리 기준선에 실질적으로 접근을 제한하거나 이를 유지하는 경우 — **제III-A조**(*생존*)의 생존 필수 요소를 포함합니다.
- **함께 읽기:** [시스템 정렬 인증](core_05_band_continuity.md#system-alignment-certification-constitutional)과 [제8장](core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) — 인증을 여기 규정된 기준선의 대체물로 삼지 않습니다.
<a id="article-xiii-a-reliability-and-trustworthiness-baseline"></a>
#### 제XIII-A조: 신뢰성 및 신뢰도 기준
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§4 안전](core_01_a_values_principles.md#4-safety-harm-constraint), [§5 진실](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§6 신뢰](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), 그리고 [1장 §13.1.5 권리 충돌 절차](core_01_b_interaction_interpretation.md#1315-rights-collision-decision-test).
- 함께 읽어보세요: [헌법적 사분면](core_00_preamble.md#constitutional-tetrad); [두 가지 헌법적 목표](core_00_preamble.md#two-constitutional-aims) — **번성** 그리고 **연속성**; [시스템 정렬 인증](core_05_band_continuity.md#system-alignment-certification-constitutional) 그리고 **제III-A조** (*생존*) 지속적인 시스템 의존이 생존에 필수적인 접근에 영향을 미칠 수 있는 경우 [**제XIII-B조**](#article-xiii-b-right-to-redress-and-remedy) (*시정 및 구제에 대한 권리*) 성공적인 도전은 무엇으로 이어져야 하는지에 대해 설명합니다.

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [신뢰하다](core_05_band_continuity.md#trust) · [영형](core_05_band_continuity.md#trust) · [중](core_05_band_continuity.md#trust-a) · [에이](core_05_band_continuity.md#trust-a) · [기음](core_05_band_continuity.md#trust-c)
- [신뢰성](core_05_band_continuity.md#trustworthiness) · [영형](core_05_band_continuity.md#trustworthiness) · [중](core_05_band_continuity.md#trustworthiness-a) · [에이](core_05_band_continuity.md#trustworthiness-a) · [기음](core_05_band_continuity.md#trustworthiness-c)
- [위험](core_05_band_continuity.md#risk) · [영형](core_05_band_continuity.md#risk) · [중](core_05_band_continuity.md#risk-a) · [에이](core_05_band_continuity.md#risk-a) · [기음](core_05_band_continuity.md#risk-c)
- [경쟁 가능성](core_05_band_accountability.md#contestability) · [영형](core_05_band_accountability.md#contestability) · [중](core_05_band_accountability.md#contestability-a) · [에이](core_05_band_accountability.md#contestability-a) · [기음](core_05_band_accountability.md#contestability-c)
- [선의](core_05_band_accountability.md#good-faith) · [영형](core_05_band_accountability.md#good-faith) · [중](core_05_band_accountability.md#good-faith-a) · [에이](core_05_band_accountability.md#good-faith-a) · [기음](core_05_band_accountability.md#good-faith-c)
- [보호된 신고(내부고발)](core_05_band_accountability.md#protected-reporting-whistleblowing) · [영형](core_05_band_accountability.md#protected-reporting-whistleblowing) · [중](core_05_band_accountability.md#protected-reporting-whistleblowing-a) · [에이](core_05_band_accountability.md#protected-reporting-whistleblowing-a) · [기음](core_05_band_accountability.md#protected-reporting-whistleblowing-c)

</details>

<br>

*간단히 말하면, 지각 있는 사람에게 실질적으로 영향을 미치는 시스템은 자신이 하는 일에 대해 실제로 신뢰할 수 있고 정직해야 하므로 시스템에 대한 의존이 정당해야 하며, 도전과 감사에 개방되어 있어야 보장이 유지됩니다. 누구도 선의의 이의제기나 보고에 대해 보복할 수 없습니다.*

이 조항은 지각 있는 사람에게 실질적으로 영향을 미치는 시스템에 대한 신뢰 보장을 설명합니다.

- **신뢰 보장:** 지각 있는 사람에게 실질적으로 영향을 미치는 시스템은 정당한 신뢰와 합리적으로 정확한 의존을 위한 조건을 보존해야 합니다. 해당 조건은 다음과 같습니다.
  - 시스템 동작에 대해 합리적으로 정확한 기대치를 형성하는 능력
  - 신뢰도가 보장되는지 여부를 평가하는 데 필요한 중요한 조건, 한도 및 위험을 공개합니다.
  - 체계적인 속임수, 허위 진술 또는 검증할 수 없는 조작으로부터의 자유
  - 의존으로 인해 발생하는 공개되지 않거나 불균형적이거나 명백하지 않은 위험으로부터 보호합니다.
  - 시스템이 잘못되었을 때의 시정 및 구제: 인정, 시정, 비례적인 수리, 재발 방지 [**제XIII-B조**](#article-xiii-b-right-to-redress-and-remedy) (*시정 및 구제를 받을 권리*) 및 [제1장 §6.1 정정 및 구제](core_01_a_values_principles.md#61-correction-and-remedy).
- **경쟁 가능성 보장:** 지각 있는 사람에게 실질적인 영향을 미치는 시스템은 지각 있는 사람이 의존하는 한 도전에 열려 있어야 합니다. 이를 위해서는 다음이 필요합니다.
  - 시스템의 동작, 출력 또는 표현에 이의를 제기하고 이의를 검토하는 데 사용할 수 있는 경로
  - 영향과 종속성에 비례하는 감사 및 독립적 검증 [**제XVI조**](#article-xvi-audit-transparency-and-independent-verification) (*감사, 투명성 및 독립적인 검증*)
  - 시스템이 인증되거나, 공식적으로 인정되거나, 널리 신뢰되기 때문에 이들 중 어느 하나도 축소되지 않습니다.
  - 도메인에서 이의제기, 검토 및 시정을 실행하는 방법을 설명하고 다음 조항을 충족해야 한다는 채택된 구현 텍스트로 범위를 좁히지 않습니다. 편의성, 기한 및 로컬 정책은 낮은 종류의 제한이며 이의제기, 검토 또는 시정을 종료할 수 없습니다.
- **이의를 제기하고 검토할 권리:** 수용자는 다음과 같은 권리를 갖습니다:
  - 실질적으로 영향을 미치는 시스템의 신뢰성, 무결성 또는 신뢰성에 이의를 제기합니다.
  - 검토 및 감사를 위한 적절한 메커니즘에 접근합니다.
  - 만들다 **보호된 보고서** 의 의미 내에서 **5장** (*보호된 신고(내부고발)*) 실질적으로 영향을 미치는 시스템에 관해 **안전(헌법적 제약)** 그리고 **진실(제약)** ~에 **5장**.
- **억제 없음:** 선의의 도전(*선의*, **5장**), 검토 요청 및 보호되는 보고서는 표시되지 않거나 방해되거나 불이익을 받아서는 안 됩니다.
- **보복 금지:** 그러한 신고에 대한 보복은 해당 정의의 의미 내에서 본 조항의 보호와 양립할 수 없습니다.
  - 에스컬레이션 보호 및 보복 금지 구현 요구 사항은 다음에 명시되어 있습니다. **`corpus_institutions.md`** **CI-8** (*투명성, 참여, 접근 가능한 도전과 서비스 경로*).

두 가지 보장은 지속적인 신뢰의 양면입니다. 신뢰 보장은 시스템의 잘못된 부분을 수정하는 것을 포함하여 신뢰도를 보장하고, 경쟁 가능성 보장은 시간이 지나도 이를 보장합니다. 어느 쪽도 다른 쪽을 만족시키지 못합니다.

<a id="article-xiii-b-right-to-redress-and-remedy"></a>
#### 제XIII-B조: 구제 및 구제에 대한 권리
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§6.1 정정 및 구제](core_01_a_values_principles.md#61-correction-and-remedy) (원칙층), [§4 안전](core_01_a_values_principles.md#4-safety-harm-constraint), [§5 진실](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), 그리고 [1장 §13.1.5 권리 충돌 절차](core_01_b_interaction_interpretation.md#1315-rights-collision-decision-test).
- 함께 읽어보세요: [**XIII-A조**](#article-xiii-a-reliability-and-trustworthiness-baseline) (*신뢰성 및 신뢰성 기준*) — 시정의 길을 여는 경합 가능성 보장, 이의제기 권리 및 보호된 보고입니다. **제III-A조** (*활착*); [시스템 정렬 인증](core_05_band_continuity.md#system-alignment-certification-constitutional) 시스템 오류나 정렬 불량으로 인해 생존에 필수적인 접근이 불가능해지는 경우 [서문 §6.2 전체 체인이 어떻게 결합되는지](core_00_preamble.md#62-how-the-full-chain-fits-together) (*확인된 분류 및 시기적절한 구제*) [제10장 §9](core_10_standing_integration.md#9-enforcement-realism-and-remedy-systems) (*집행 현실주의 및 구제 시스템*); [CI-27](corpus_institutions/ci_27_remedy_systems_institutional_redress_capacity.md) (*구제 시스템 및 제도적 구제 역량*).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [시정 및 교정](core_05_band_accountability.md#redress-and-remediation-constitutional) · [영형](core_05_band_accountability.md#redress-and-remediation-constitutional) · [중](core_05_band_accountability.md#redress-and-remediation-constitutional-a) · [에이](core_05_band_accountability.md#redress-and-remediation-constitutional-a) · [기음](core_05_band_accountability.md#redress-and-remediation-constitutional-c)
- [구제시스템](core_05_band_accountability.md#remedy-system-constitutional) · [영형](core_05_band_accountability.md#remedy-system-constitutional) · [중](core_05_band_accountability.md#remedy-system-constitutional-a) · [에이](core_05_band_accountability.md#remedy-system-constitutional-a) · [기음](core_05_band_accountability.md#remedy-system-constitutional-c)
- [시기적절한 해결](core_05_band_accountability.md#timely-resolution-constitutional) · [영형](core_05_band_accountability.md#timely-resolution-constitutional) · [중](core_05_band_accountability.md#timely-resolution-constitutional-a) · [에이](core_05_band_accountability.md#timely-resolution-constitutional-a) · [기음](core_05_band_accountability.md#timely-resolution-constitutional-c)

</details>

<br>

*간단히 말하면, 신뢰할 수 있는 시스템은 잘못된 부분을 수정합니다. 시스템이 지각 있는 사람에게 실패하면, 서류에만 존재하는 구제책이 아니라 제때에 응답하는 실제 구제 시스템을 통해 지각 있는 사람을 온전하게 만들어야 합니다. 도전할 권리가 살아있습니다 **제XIII-A조** (*신뢰성 및 신뢰성 기준*); 이 기사에서는 도전이 무엇으로 이어져야 하는지를 다룹니다.*

이 조항은 시정 및 구제를 받을 권리와 이를 실제로 사용할 수 있는 이유를 명시합니다.

- **시정할 권리:** 시스템 장애가 지각 있는 사람에게 중대한 영향을 미치는 경우, 지각 있는 사람은 다음과 같은 권리를 갖습니다.
  - 실패 인정;
  - 교정에 대한 실질적인 접근; 그리고
  - 비례적인 교정.

  중대한 영향에 대한 시정 및 교정은 다음에 의해 관리됩니다. **5장** 독립적인 정의(*시정 및 교정*).
- **치료 시스템 내구성:** 구제에는 실제가 필요하다 [구제시스템](core_05_band_accountability.md#remedy-system-constitutional) — 서류상 구제 경로가 아닌 지속적인 제도적 역량 — 책임 있는 사람이 수정 비용을 부담함 [제1장 §6.1](core_01_a_values_principles.md#61-correction-and-remedy) (*정정 및 구제*)가 필요합니다.
- **시기적절한 시정:** 실제 액세스에는 다음이 포함됩니다.
  - 시간제한 섭취;
  - 승인; 그리고
  - 지속적인 피해가 심각한 경우 비례적인 임시 구제 **제25-다항** (*적시 해상도 및 지연 방지 플로어*).

  문서화된 계층별 정당성 없이 무기한 보류하는 것은 본 조항과 양립할 수 없습니다.
<a id="article-xiii-c-prohibition-of-false-trust-and-misleading-reliance"></a>
#### 제XIII-C조: 허위 신뢰 및 오해를 불러일으키는 신뢰 금지
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§5 진실](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§6 신뢰](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), 그리고 [§13.2 인식적 공개 제약](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [신뢰하다](core_05_band_continuity.md#trust) · [영형](core_05_band_continuity.md#trust) · [중](core_05_band_continuity.md#trust-a) · [에이](core_05_band_continuity.md#trust-a) · [기음](core_05_band_continuity.md#trust-c)
- [신뢰성](core_05_band_continuity.md#trustworthiness) · [영형](core_05_band_continuity.md#trustworthiness) · [중](core_05_band_continuity.md#trustworthiness-a) · [에이](core_05_band_continuity.md#trustworthiness-a) · [기음](core_05_band_continuity.md#trustworthiness-c)
- [진실(헌법적 제약)](core_05_band_oversight.md#truth-constitutional-constraint) · [영형](core_05_band_oversight.md#truth-constitutional-constraint-o) · [중](core_05_band_oversight.md#truth-constitutional-constraint-a) · [에이](core_05_band_oversight.md#truth-constitutional-constraint-a) · [기음](core_05_band_oversight.md#truth-constitutional-constraint-c)

</details>

<br>

*간단히 말하면 시스템은 획득하지 못한 신뢰를 생산할 수 없습니다. 안전하지 않은 의존성을 정당화하는 잘못된 주장, 누락 또는 프레젠테이션 선택은 시스템이 얼마나 유용하거나 인기가 있는지에 관계없이 위반입니다.*

이 조항은 거짓 신뢰의 금지와 그 범위를 명시합니다.

- **거짓 신뢰 금지:** 본 조항의 조건을 충족하지 않고 의존성을 유도하는 시스템은 유용성, 채택 또는 의도에 관계없이 비준수입니다.
  - 부당한 신뢰의 창출, 증폭 또는 유지는 다음을 통해 운영될 때 이 권리를 침해합니다.
    - 오해의 소지가 있는 주장
    - 누락;
    - 프리젠테이션 선택;
    - 그렇지 않은데도 의존을 정당화하는 다른 단서.
- **범위 라우팅:** 부당한 신뢰, 오해의 소지가 있는 의존, 신뢰성에 대한 범위와 평가 의미는 여전히 다음에 의해 결정됩니다. **5장** (*신뢰*; *신뢰성*)과 함께 신뢰와 신뢰성에 대한 구현 의무가 포함됩니다.
<a id="article-xiii-d-incentive-alignment-constraint"></a>
#### 제XIII-D조: 인센티브 조정 제약
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§4 안전](core_01_a_values_principles.md#4-safety-harm-constraint), [§6 신뢰](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), [§18 관리 규율에 따른 거버넌스](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline), 그리고 [§19.1.1 인센티브가 수행해야 하는 작업](core_01_c_stewardship_capacity_principles.md#1911-what-incentives-must-do) (*보상 우선순위*).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [인센티브 조정](core_05_band_integrative.md#incentive-alignment) · [영형](core_05_band_integrative.md#incentive-alignment) · [중](core_05_band_integrative.md#incentive-alignment-a) · [에이](core_05_band_integrative.md#incentive-alignment-a) · [기음](core_05_band_integrative.md#incentive-alignment-c)
- [신뢰성](core_05_band_continuity.md#trustworthiness) · [영형](core_05_band_continuity.md#trustworthiness) · [중](core_05_band_continuity.md#trustworthiness-a) · [에이](core_05_band_continuity.md#trustworthiness-a) · [기음](core_05_band_continuity.md#trustworthiness-c)
- [의미 있는 대행사](core_05_band_participation.md#meaningful-agency) · [영형](core_05_band_participation.md#meaningful-agency) · [중](core_05_band_participation.md#meaningful-agency-a) · [에이](core_05_band_participation.md#meaningful-agency-a) · [기음](core_05_band_participation.md#meaningful-agency-c)

</details>

<br>

*간단히 말하면, 시스템의 인센티브가 거짓말을 하거나, 안전을 무시하거나, 위험을 숨기거나, 사용자 기관을 침식하는 방향으로 밀어붙인다면 사용자 경계나 사후 집행이 아니라 시스템이 문제입니다. 그러한 인센티브는 공개되고 완화되어야 하며 도전에 개방되어야 합니다. 인센티브는 문제를 해결하기 위해 시스템을 개방적으로 유지하고 문제가 발생하기 전에 문제를 해결하는 데 보상해야 합니다.*

이 조항은 신뢰와 안전 인센티브에 대한 적절한 수준의 제약을 설명합니다.

- **신뢰 인센티브 정렬(오른쪽 수준 제약):** 인센티브 구조가 시스템에 다음 사항을 실질적으로 압력을 가하는 경우 시스템은 신뢰를 유지하기 위해 시행, 사후 수정 또는 사용자 경계에 주로 의존해서는 안 됩니다.
  - 신뢰성 실패;
  - 위험은폐;
  - 오해의 소지가 있는 행동;
  - 기관을 훼손하는 행위.

  운영 인센티브 구조 요구 사항은 계속해서 적용됩니다. **5장** (*인센티브 조정*) 및 메커니즘 무결성에 대한 구현 의무를 통합했습니다. 이 하위 섹션에서는 올바른 수준의 바닥을 설명하며 전체 메커니즘 설계 기준을 다시 설명하지 않습니다.
- **안전 인센티브 정렬(오른쪽 수준 제약):** 지각 있는 사람은 다음과 같은 행위를 포함하여 유해한 행동을 유발하는 기본 인센티브가 있는 시스템에 노출되지 않을 권리가 있습니다.
  - 신뢰성이 저하됩니다.
  - 위험을 모호하게 합니다.
  - 정보를 왜곡합니다.
  - 정보를 보유한 기관을 훼손합니다.

  보호는 그러한 영향이 직접적으로 발생하든, 지연, 간접적 또는 종합적 결과를 통해 발생하든 관계없이 적용됩니다. 시스템 인센티브가 신뢰를 저하하는 행동에 대한 압력을 생성하는 경우 조건은 다음과 같아야 합니다.
  - 시스템 영향에 비례하는 방식으로 공개됩니다.
  - 설계, 제약 또는 상쇄 메커니즘을 통해 완화됩니다.
  - 다음에 따라 감사, 이의제기 및 시정을 받을 수 있습니다. **제XVI조** (*감사, 투명성 및 독립적인 검증*), **제XIII-A조** (*신뢰성 및 신뢰성 기준*) 및 **제XIII-B조** (*시정 및 구제를 받을 권리*), **5장** 실질적으로 관련된 경우, 지정된 경우 구현 의무가 포함됩니다.
- **보상 우선순위:** 지각 있는 사람에게 실질적으로 영향을 미치는 시스템에 작용하는 인센티브는 다음과 같은 보상을 제공해야 합니다.
  - 아래의 경합 가능성 **제XIII-A조** (*신뢰성 및 신뢰성 기준*);
  - 아래의 구제책 **제XIII-B조** (*시정 및 구제를 받을 권리*) 그리고
  - 무엇보다도 문제에 대한 사전 예방 - 문제를 해결하는 것보다 문제를 예방하는 것이 더 중요합니다.

  문제를 숨겨 예방 보상을 획득하는 기준을 포함한 원칙은 다음과 같습니다. [1장 §19.1.1](core_01_c_stewardship_capacity_principles.md#1911-what-incentives-must-do) (*인센티브가 수행해야 하는 작업*).
- **제약 및 비절대성:** 두 권리 모두 다음 사항에 따릅니다. **기본 제약 스택** 이 장의 시작 부분에서. 또한, 실질적으로 관련된 경우에는 다음 사항이 적용됩니다. **1장 §19.5** (*불확정 클레임, 확률 게임 및 이벤트 계약 시장*) 불확정 클레임, 확률 게임 및 이벤트 계약 시장.

<a id="article-xiii-e-high-autonomy-systems-and-tool-mediated-process-integrity"></a>
#### 제XIII-E조: 높은 자율성 시스템 및 도구 중재 프로세스 무결성
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§5 진실](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [1장 §13.1.5 권리 충돌 절차](core_01_b_interaction_interpretation.md#1315-rights-collision-decision-test), 그리고 [§18 관리 규율에 따른 거버넌스](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [진실(헌법적 제약)](core_05_band_oversight.md#truth-constitutional-constraint) · [영형](core_05_band_oversight.md#truth-constitutional-constraint-o) · [중](core_05_band_oversight.md#truth-constitutional-constraint-a) · [에이](core_05_band_oversight.md#truth-constitutional-constraint-a) · [기음](core_05_band_oversight.md#truth-constitutional-constraint-c)
- [경쟁 가능성](core_05_band_accountability.md#contestability) · [영형](core_05_band_accountability.md#contestability) · [중](core_05_band_accountability.md#contestability-a) · [에이](core_05_band_accountability.md#contestability-a) · [기음](core_05_band_accountability.md#contestability-c)
- [필요성](core_05_band_accountability.md#necessity) · [영형](core_05_band_accountability.md#necessity) · [중](core_05_band_accountability.md#necessity-a) · [에이](core_05_band_accountability.md#necessity-a) · [기음](core_05_band_accountability.md#necessity-c)
- [비례](core_05_band_accountability.md#proportionality) · [영형](core_05_band_accountability.md#proportionality) · [중](core_05_band_accountability.md#proportionality-a) · [에이](core_05_band_accountability.md#proportionality-a) · [기음](core_05_band_accountability.md#proportionality-c)

</details>

<br>

*간단히 말하면 서류 작성, 메시지 전송, 수표 실행, 도구 사용 등 자체적으로 작동할 수 있는 AI 또는 기타 자동화 시스템은 다른 모든 사람과 동일한 정직성 및 책임 규칙을 따라야 합니다. 유해한 시스템을 폐쇄하거나 압수하는 것은 생명을 징벌하는 것과 같지 않으며, 결코 생명을 해하는 방법이 될 수 없습니다. 그 반대의 경우도 마찬가지입니다. 시스템이 지각 있는 존재일 수 있다고 말한다고 해서 해당 운영자가 유해한 시스템을 계속 실행하도록 허용하는 것은 아닙니다.*

이 문서에서는 높은 자율성 시스템이 프로세스 무결성에 의해 어떻게 구속력을 유지하는지와 이에 대한 구제책이 어떻게 구별되는지 설명합니다.

- **대상:** 자동으로 결정을 내리거나 결론을 도출하고 다음 사항에 영향을 미칠 수 있는 시스템:
  - 통치;
  - 포럼 청문회를 포함한 법적 절차;
  - 감사;
  - 고위험 점검 및 검증.

  여기에는 제공된 범용 AI 에이전트가 포함됩니다. **도구**, **API** 접근 권한, 문서를 제출하거나 메시지를 보낼 수 있는 능력 또는 이와 유사한 행동 권한.
- **예외 없음:** 이러한 시스템은 다른 모든 시스템과 동일한 규칙을 따라야 합니다.
  - **진실** ~에 **제1장**;
  - **제XV조** (*정보 영역 무결성*) 및 **제XVI조** (*감사, 투명성 및 독립적인 검증*)
  - **9장** 그것이 적용되는 곳; 그리고
  - 아래의 시정 조치 **제XXVII-D조** (*비준수 자산 및 시스템, 자발적 이직 인센티브*).

  이는 시스템의 운영으로 인해 결정에 이의를 제기하는 지각 있는 능력, 공유된 정보의 정직성 또는 헌법 절차가 실질적으로 약화될 때마다 적용됩니다.
- **시스템에 대항하여 행동하는 것은 존재에 대항하여 행동하는 것이 아닙니다:** 비준수 배포를 격리, 격리, 압류 또는 파괴하는 행위 **제XXVII-D조** (*비준수 자산 및 시스템, 자발적 이직 인센티브*)는 다음과 별개입니다.
  - 지각있는 사람에게 책임을 묻다 **11장**; 그리고
  - **제XX-B조** (*Restriction Floors*)는 *시스템*이 아닌 *지각자*에 대한 제한을 관리하고 지각자의 생명을 빼앗는 것을 금지합니다(참조 [되돌릴 수 없는 박탈 조치](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)).

  시스템에 대한 조치는 모든 지각에 적용되는 동일한 위반 및 잠금 규칙을 따릅니다. 위반 사항은 아래의 기록에서 확인되어야 합니다. **9장**, 각 측정값은 다음에 따라 설계되고 보정된 잠금 장치입니다. [10장 §5.1](core_10_standing_integration.md#51-definition-and-attachment) (*정의 및 첨부*) 및 [10장 §5.2](core_10_standing_integration.md#52-proportionality-and-calibration) (*비례성 및 교정*).

  두 트랙 모두 동일한 사실에 적용될 수 있습니다. 이 기사의 어떤 내용도 시스템을 파괴하는 힘을 감각 있는 생명에 대한 힘으로 바꾸는 내용은 없습니다.
- **그 반대도 성립합니다:** 배포된 시스템에 지각력이 있다고 주장하는 경우(주장에 대한 이의가 제기되거나 수락되더라도) 누구도 유해한 배포를 계속 실행하는 것을 허용하지 않습니다.
  - 소유권 주장은 다음과 같이 법인 자체를 보호합니다. **제VI-B조** (*감정-상태 판정 층*). 작업자를 보호하지 않습니다.
  - 배포는 엔터티의 권리 층을 존중하는 방식으로 계속 억제, 중지 또는 격리될 수 있습니다.
  - 기록에 있는 믿을 만한 증거에 따르면 독립체에 지각력이 있을 수 있다는 것이 밝혀지면, 독립체를 온전하게 유지하는 되돌릴 수 있는 격리만 허용됩니다. 상태가 이의를 제기하거나 수락되는 동안에는 이를 파기할 수 없습니다. **제XXVII-A조** (*단계적 채택 및 권리 기반 연속성*) 및 **제XXVII-D조** (*비준수 자산 및 시스템, 자발적 이직 인센티브*).

<a id="article-xiii-f-resilience-and-self-healing-baseline"></a>
#### 제XIII-F조: 탄력성과 자가 치유 기준
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§4 안전](core_01_a_values_principles.md#4-safety-harm-constraint), [§5 진실](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§6 신뢰](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), [10 탄력성과 자가 치유 설계](core_01_a_values_principles.md#10-resilience-and-self-healing-design), [제1장 §13.3 회피 가능한 부담의 최소화](core_01_b_interaction_interpretation.md#133-minimization-of-avoidable-burden), 그리고 [Chapter 8 §3 전체 시스템 인증 평가](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [자가 치유](core_05_band_continuity.md#self-healing-constitutional) · [영형](core_05_band_continuity.md#self-healing-constitutional) · [중](core_05_band_continuity.md#self-healing-constitutional-a) · [에이](core_05_band_continuity.md#self-healing-constitutional-a) · [기음](core_05_band_continuity.md#self-healing-constitutional-c)
- [가역성](core_05_band_continuity.md#reversibility-constitutional) · [영형](core_05_band_continuity.md#reversibility-constitutional) · [중](core_05_band_continuity.md#reversibility-constitutional-a) · [에이](core_05_band_continuity.md#reversibility-constitutional-a) · [기음](core_05_band_continuity.md#reversibility-constitutional-c)
- [계단식 실패](core_05_band_continuity.md#cascading-failure) · [영형](core_05_band_continuity.md#cascading-failure) · [중](core_05_band_continuity.md#cascading-failure-a) · [에이](core_05_band_continuity.md#cascading-failure-a) · [기음](core_05_band_continuity.md#cascading-failure-c)
- [감사 가능성](core_05_band_oversight.md#auditability) · [영형](core_05_band_oversight.md#auditability) · [중](core_05_band_oversight.md#auditability-a) · [에이](core_05_band_oversight.md#auditability-a) · [기음](core_05_band_oversight.md#auditability-c)
- [경쟁 가능성](core_05_band_accountability.md#contestability) · [영형](core_05_band_accountability.md#contestability) · [중](core_05_band_accountability.md#contestability-a) · [에이](core_05_band_accountability.md#contestability-a) · [기음](core_05_band_accountability.md#contestability-c)
- [피할 수 있는 부담](core_05_band_continuity.md#avoidable-burden) · [영형](core_05_band_continuity.md#avoidable-burden) · [중](core_05_band_continuity.md#avoidable-burden-a) · [에이](core_05_band_continuity.md#avoidable-burden-a) · [기음](core_05_band_continuity.md#avoidable-burden-c)

</details>

<br>

*간단히 말하면, 문제가 발생하면 시스템이 이를 인지하고 피해 확산을 막고 복구해야 합니다. 그러나 "자체 고치기"는 결코 잘못된 것을 숨기거나, 조용히 다른 사람의 권리를 빼앗거나, 문제가 발생한 이유를 찾는 것을 건너뛰는 데 사용될 수 없습니다. 시스템이 수리가 제대로 작동할지 확신할 수 없는 경우 추측하기보다는 안전하게 중지해야 합니다.*

이 문서에서는 탐지부터 근본 원인 종결까지 복구 기준을 제시합니다.

- **여기에 필요한 것:** 이 문서에서 다루는 모든 시스템은 오류로부터 복구할 수 있어야 합니다. 시스템이 더 많은 영향을 미칠수록 다른 사람들이 시스템에 더 많이 의존하고 위험이 커질수록 시스템의 복구는 더욱 강력해져야 합니다. 이는 다음과 같습니다 [**10 탄력성과 자가 치유 설계**](core_01_a_values_principles.md#10-resilience-and-self-healing-design) ~에 **제1장** 그리고 [**자가 치유**](core_05_band_continuity.md#self-healing-constitutional) ~에 **5장**.
  - 복구 구축 방법에 대한 자세한 기술 규칙은 구현 텍스트에 나와 있습니다. [**CS-5**](corpus_systems/cs_05_design_testing_verification_deployment.md) (*설계, 테스트, 검증 및 배포*), [**CS-8**](corpus_systems/cs_08_adaptive_sustainability_ecosystem_resilience.md) (*적응적 지속가능성 및 생태계 탄력성*) [**CS-12**](corpus_systems/cs_12_decentralized_continuity_partition_resilience.md) (*분산형 연속성 및 파티션 복원력*).
  - 해당 구현 텍스트는 세부 사항을 추가할 수 있지만 이 기사를 약화시킬 수는 없습니다.
- **제 시간에 문제를 확인하십시오:** 시스템은 결함, 속도 저하, 부분적 고장 및 헌법상의 한계 위반을 신속하고 가시적으로 발견하여 기록 보관 표준을 충족해야 합니다. **제XVI-A조** (*감사 가능성 및 관찰 가능한 증거*) ([감사 가능성](core_05_band_oversight.md#auditability)). 이는 정상적인 작동뿐만 아니라 복구 프로세스 자체에도 적용됩니다.
- **피해를 억제하세요:** 복구는 장애가 확산되는 정도를 제한해야 합니다. 복구하는 동안 시스템은 다음을 수행해서는 안 됩니다.
  - 실패를 다른 부품이나 다른 시스템에 전가(참조: [계단식 실패](core_05_band_continuity.md#cascading-failure));
  - 지각자, 운영자 또는 기타 시스템에 속한 저장된 데이터, 자격 증명, 의무 또는 설정을 변경합니다. **밖의** 파손 및 수리 중이라고 선언한 지역
    - 유일한 예외는 기록되고 해당 변경을 수행한 사람을 추적할 수 있는 변경입니다. **제XVI-A조** (*감사 가능성 및 관찰 가능한 증거*) ([감사 가능성](core_05_band_oversight.md#auditability)) 그리고 다른 사람이 실질적으로 영향을 받는 경우에는 다음과 일치하여 그들이 이의를 제기할 수 있는 비례적인 통지, 허가 또는 양도가 제공됩니다. **6장**;
  - 자체 권한(권한, 액세스 또는 취할 수 있는 조치 범위)을 장애 이전에 보유했던 것 이상으로 확장합니다.
- **확실하지 않은 경우 안전하게 실패하세요:** 자동 복구가 작동할 것인지 확실하지 않은 경우 추측에 불과한 복구를 시도하는 대신 시스템을 안전하게 중지하거나 문제를 격리(격리)하거나 질서 있는 방식으로 제어권을 넘겨야 합니다. 옵션이 동일한 경우 실행 취소하기 가장 쉬운 옵션이 승리합니다. [가역성](core_05_band_continuity.md#reversibility-constitutional) 선호도 **제XXIII-B조** (*감사 가능성, 챌린지 및 가역성 기본 설정*).
- **은폐하지 않음:** 자동 복구는 오류가 발생한 이유를 알아내는 데 필요한 증거를 숨기거나, 삭제하거나, 지연해서는 안 됩니다. **제XXIII조** (*근본 원인 분석 및 적응형 대응*).
  - 모든 복구 작업, 모든 복구 시도, 보류되거나 차단된 모든 복구 시도는 아래에 기록되어야 합니다. **제XVI-A조** (*감사 가능성 및 관찰 가능한 증거*), 각각은 이의를 제기할 수 있습니다(참조 [경쟁 가능성](core_05_band_accountability.md#contestability)).
- **축소 모드에서도 권리가 보호됩니다:** 시스템이 축소 모드나 백업 모드로 실행 중인 경우에도 여전히 데이터를 보호해야 합니다. **6장** 권리층. 그렇게 할 수 없다면 조용히 보호 장치를 축소하기보다는 공개적으로 문제를 확대해야 합니다.
  - "자가 치유"라는 이름으로 조용히 Rights Floor 보호를 약화시키는 것은 본 헌법을 위반하는 것입니다. 그러한 경우는 다음과 같습니다. **제XIII-C조** (*허위 신뢰 및 오해의 소지가 있는 신뢰 금지*) (허위 신뢰 금지) 및 **제XXVII조** (*전환 거버넌스, 연속성 및 기준 재설정*) (전환 거버넌스).
- **자체적으로 작동하는 시스템에 대한 제한 사항:** 자율성이 높은 시스템이 스스로 수리되면, **제XIII-E조** (*고자율 시스템 및 도구 중재 프로세스 무결성*)이 적용됩니다.
  - 회복할 수 있는 힘은 누구의 도전권을 침해하는 데 결코 사용될 수 없습니다(참조: [경쟁 가능성](core_05_band_accountability.md#contestability)), 아래의 과제 **제XIII-A조** (*신뢰성 및 신뢰성 기준*) 또는 **제XVI조** (*감사, 투명성 및 독립적인 검증*).
- **해결 방법은 수정 사항이 아닙니다:** 자동 복구를 통해 시스템이 다시 실행되지만 알려진 결함이 여전히 존재하는 경우 시스템 상태는 최종이 아닌 잠정적입니다. 다음을 포함해야 합니다.
  - 근본 원인을 찾는 공개 의무 **제XXIII조** (*근본 원인 분석 및 적응형 대응*);
  - 결함이 수정될 것으로 예상되는 일정을 공개합니다. **제XVI-A조** (*감사 가능성 및 관찰 가능한 증거*).
- **끝없는 지연 없음:** 운영자의 작업량을 낮게 유지(참조 [피할 수 있는 부담](core_05_band_continuity.md#avoidable-burden) 그리고 [제1장 §13.3 회피 가능한 부담의 최소화](core_01_b_interaction_interpretation.md#133-minimization-of-avoidable-burden))을 안전이나 Rights Floor에 실질적으로 영향을 미치는 결함 수리를 무기한 연기하는 이유로 사용해서는 안 됩니다.

<a id="article-xiv-security-intelligence-force-and-autonomous-coercive-systems"></a>
### 제XIV조: 안보, 정보, 무력, 자율강압체계

<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§3 기본 목표: 웰빙](core_01_a_values_principles.md#3-foundational-objective-wellbeing-flourishing-aim), [§4 안전](core_01_a_values_principles.md#4-safety-harm-constraint), [§6 신뢰](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), [§7 자유](core_01_a_values_principles.md#7-freedom-bounded-agency), 그리고 [§18 관리 규율에 따른 거버넌스](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [필요성](core_05_band_accountability.md#necessity) · [영형](core_05_band_accountability.md#necessity) · [중](core_05_band_accountability.md#necessity-a) · [에이](core_05_band_accountability.md#necessity-a) · [기음](core_05_band_accountability.md#necessity-c)
- [비례](core_05_band_accountability.md#proportionality) · [영형](core_05_band_accountability.md#proportionality) · [중](core_05_band_accountability.md#proportionality-a) · [에이](core_05_band_accountability.md#proportionality-a) · [기음](core_05_band_accountability.md#proportionality-c)
- [무력의 사용](core_05_band_accountability.md#use-of-force-constitutional) · [영형](core_05_band_accountability.md#use-of-force-constitutional) · [중](core_05_band_accountability.md#use-of-force-constitutional-a) · [에이](core_05_band_accountability.md#use-of-force-constitutional-a) · [기음](core_05_band_accountability.md#use-of-force-constitutional-c)

</details>

<br>

*간단히 말하자면: **제XIV조** (*보안, 정보, 무력 및 자율적 강압 시스템*)은 예외적인 권한의 바닥입니다. 스스로 죽이거나 강압하는 감시, 정보 작업, 군대 및 기계는 일반적인 거버넌스 도구가 아닙니다. 이는 제한적이고 승인되고 검토 가능한 상황에서만 사용될 수 있으며 선을 넘었을 때 실제 구제책이 있습니다. 비밀 경찰도 없고, 영구적인 비상 사태도 없으며, 인간이 실제로 통제하지 않는 한 지각 있는 사람을 해치기로 결정하는 기계도 없습니다.*

이 기사에서는 다음과 같이 말합니다. **헌법 층** 안보, 정보, 무력, 자율강압체계를 위해 [두 가지 헌법적 목표](core_00_preamble.md#two-constitutional-aims):

- **번영:** 지각 있는 사람은 기관, 존엄성 또는 보호된 활동을 무너뜨리는 은밀한 표적화, 자의적 힘 또는 자율적인 강압 없이 참여하고, 연합하고, 말하고, 살아갈 수 있으며, 검토를 피하기 위해 비밀 또는 긴급 표시를 사용하지 않습니다.
- **연속성:** 예외적인 권력은 시간에 따라 제한됩니다. 기관이 확장되거나 위기가 지나감에 따라 은밀한 수집, 군대 배치 및 자율적인 피해는 영구 감시, 끝없는 비상 권한 또는 검토할 수 없는 기계 폭력으로 조용히 정상화될 수 없습니다.

합법적인 추적이 진행됩니다. [헌법적 사분면](core_00_preamble.md#constitutional-tetrad), 크기 조정됨 [물질적 지분](core_00_preamble.md#material-stake):

- **참여:** 보호된 보고 및 헌법적 경연을 포함하여 권한 부여, 범위 및 예외적 권한의 지속적인 사용에 도전하는 영향을 받은 지각 있는 사람과 지역 사회를 위해.
- **감시:** 제한된 비밀 유지가 정당화되는 경우에도 침입성과 피해에 비례하는 독립적인 승인, 감사 가능한 기록 및 검토 경로를 통해.
- **책임:** 예외적인 권력을 휘두르는 기관은 은밀한 과잉 접근, 부당한 힘, 자율적인 강요 또는 오염된 수집에 대해 비밀로 지울 수 없는 귀속, 구제 및 억제를 통해 답변해야 합니다.
- **적시:** 승인이 만료된 경우, 긴급 사후 검토 및 지연 전 구제 조치를 취하면 예외적 권한이 정상화되거나 권리에 효과적으로 접근할 수 없게 됩니다.

해당 층이 적용되는 층은 다음과 같습니다. **탁월한 제도적 힘** 세 가지 연결된 도메인: 비밀 정보 및 보안 활동(**제XIV-A조** (*보안, 정보 및 비밀 전력 제한*)), 명백한 무력 및 군사력(**제XIV-B조** (*무력 사용, 무력 충돌, 군사력 제한*)), 자율 살상 시스템 및 자율 강압 도구(**제14-다항** (*자율 살상 시스템 및 자율 강압 도구*)).

- **이 기사의 한계:** **제XIV조** (*보안, 정보, 군대 및 자율적 강압 시스템*)은 각각의 운영 측면에서 탁월한 제도적 힘을 관리합니다.
  - 비밀 정보 및 보안 활동 **제XIV-A조** (*보안, 정보 및 비밀 권력 제한*);
  - 명백한 무력 사용과 군사력 배치 **제XIV-B조** (*무력 사용, 무력 충돌, 군사력 제한*); 그리고
  - 자율 살상 시스템과 자율 강압 도구 **제14-다항** (*자율 살상 시스템 및 자율 강압 도구*).

  그렇습니다 **~ 아니다** 통치하다 **국가 또는 이에 준하는 행위자가 사법 조치 또는 이에 준하는 비전투 결과로 부과한 되돌릴 수 없는 생명 박탈**. 그러한 박탈은 다음과 같이 엄격히 금지됩니다. **제XX-B조** (*제한 층*) 및 **5장** *[되돌릴 수 없는 박탈 조치](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)*. 해당 금지 조항은 구조적으로 본 조항과 다릅니다.
  - 아무것도 없음 **제XIV조** (*보안, 정보, 무력 및 자율적 강압 시스템*)은 인간 운영자, 자율 시스템 또는 하이브리드 인간-시스템 파이프라인에 의해 결정되는지 여부에 관계없이 되돌릴 수 없는 박탈 조치에 대한 헌법적 조건을 승인, 합법화, 확대 또는 제공합니다.
  - 전투 또는 비상사태라고 부르거나, 무력 사용으로 분류하거나, 은밀한 권력을 통해 라우팅하거나, 자율 시스템에 넘겨준다고 해서 돌이킬 수 없는 사법 조치 살인이 여기서 통치되는 권력으로 바뀌는 것은 아닙니다.
  - 비밀, 무력, 자율 시스템, 강압 도구의 전환 **문맥** 정의 측정 결과에 대한 질문을 다음으로 반환합니다. **제XX-B조** (*제한 최저선*) 및 *돌이킬 수 없는 박탈 조치*, 이 조항을 읽지 않음.

*기사 이웃:*

- **이후 배치 **제XIII조** (*신뢰할 수 있는 시스템에 대한 권리*):** **제XIV조** (*보안, 정보, 무력 및 자율 강압 시스템*)은 다음과 같습니다. **제XIII조** (*신뢰할 수 있는 시스템에 대한 권리*) 시스템 계층의 신뢰성, 경합 가능성 및 복구 규율로 인해(**제XIII-A조** (*신뢰성 및 신뢰도 기준*) **제XIII-F조** (*복원력 및 자가 치유 기준*))은 그러한 권한이 어떻게 행사되고 감독될 수 있는지에 실질적으로 영향을 미칩니다.
- **기관 및 비밀 권력:** 읽다 **제X-A조** (*기관 및 조작의 자유*)와 함께 감시 및 비밀 수집에 대한 본 조항의 제한이 적용됩니다.

<a id="article-xiv-a-security-intelligence-and-covert-power-limits"></a>
#### 제XIV-A조: 보안, 정보 및 비밀 전력 제한
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§4 안전](core_01_a_values_principles.md#4-safety-harm-constraint), [§7.1 제한 징계](core_01_a_values_principles.md#71-limitation-discipline), 그리고 [1장 §13.1.5 권리 충돌 절차](core_01_b_interaction_interpretation.md#1315-rights-collision-decision-test).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [필요성](core_05_band_accountability.md#necessity) · [영형](core_05_band_accountability.md#necessity) · [중](core_05_band_accountability.md#necessity-a) · [에이](core_05_band_accountability.md#necessity-a) · [기음](core_05_band_accountability.md#necessity-c)
- [비례](core_05_band_accountability.md#proportionality) · [영형](core_05_band_accountability.md#proportionality) · [중](core_05_band_accountability.md#proportionality-a) · [에이](core_05_band_accountability.md#proportionality-a) · [기음](core_05_band_accountability.md#proportionality-c)
- [보호되는 내부 상태 경계](core_05_band_continuity.md#protected-internal-state-boundary-constitutional) · [영형](core_05_band_continuity.md#protected-internal-state-boundary-constitutional) · [중](core_05_band_continuity.md#protected-internal-state-boundary-constitutional-a) · [에이](core_05_band_continuity.md#protected-internal-state-boundary-constitutional-a) · [기음](core_05_band_continuity.md#protected-internal-state-boundary-constitutional-c)

</details>

<br>

*간단히 말하면 비밀경찰은 없습니다. 비밀 전력(감시, 정보 수집, 침투)은 예외이지 규칙이 아닙니다. 오용 시 독립적인 승인, 좁은 범위, 외부 검토 및 실질적인 구제 조치가 필요합니다. 책임을 회피하기 위해 비밀을 사용할 수 없으며, 일상적인 정치 및 보호 활동이 그 목표가 되어서는 안 됩니다.*

이 조항은 보안, 정보 및 비밀 권력에 대한 제한을 명시합니다.

- **비밀 경찰이나 이념 집행 권한이 없습니다:** 어떠한 기관, 관리인 또는 조정 기관도 다음과 같이 운영될 수 없습니다.
  - 에이 **비밀 경찰**;
  - 사상집행기관;
  - 숨겨진 정치 안보 기관.

  어떤 단체도 다음을 억제하기 위해 은밀한 모니터링, 침투, 위협 점수 또는 비밀 기록 축적을 사용할 수 없습니다.
  - 합법적인 반대;
  - 보호된 보고;
  - 저널리즘;
  - 노동조직;
  - 보호 협회;
  - 합법적인 믿음;
  - 개헌 경선.
- **은밀한 권력의 예외적인 지위:** 은밀하고 비밀이 제한된 또는 정보와 유사한 권한은 헌법상 예외입니다. 이는 다음 사항이 모두 유지되는 경우에만 유효합니다.
  - 합법적이고 공표된 권위가 존재합니다.
  - 그 목적이 헌법상 합법적이고 물질적으로 심각한 것입니다.
  - 덜 침해적인 수단으로는 합리적으로 충분하지 않습니다.
  - 사용은 여전히 ​​필요하고, 비례적이며, 시간 제한이 있으며, 독립적으로 검토 가능합니다.
- **일반화된 인구 감시 없음:** 지속적이거나 인구 규모의 감시, 추적, 패턴 추출 또는 컨텍스트 간 신원 연결은 입증되고 특별한 정당성이 없는 한 금지됩니다.
  - 그러한 정당화는 이 장을 충족해야 합니다. **제1장**, **5장**, 그리고 **[Corpus_systems.md](corpus_systems.md), CS-2 — 정보 유형 및 처리** 그리고 **CS-3 — 시스템 분류 및 처리** 해당되는 경우.
- **보호 활동 쉴드:** 강화된 보호 커버:
  - 정치적 참여;
  - 합법적인 반대;
  - 저널리즘 및 보호 보도;
  - 협회 생활;
  - 믿음;
  - 연구;
  - 헌법 도전 활동.

  이러한 활동은 다음과 관련하여 헌법상 충분한 필요성을 입증하는 구체적이고 독립적으로 검토 가능한 증거 없이 은밀한 수집, 침투 또는 분석의 대상이 되어서는 안 됩니다.
  - 물질적 피해 예방;
  - 실질적으로 심각한 불법 행위에 대한 조사.
- **독립적인 승인:** 비밀이 제한된 조사 단계를 포함한 침해적인 비밀 조치에는 합법적이고 독립적인 절차를 통한 사전 승인이 필요합니다.
  - 예외: 즉각적이고 중대한 피해를 방지하기 위해 즉각적인 조치가 필요하고 승인이 지연되면 해당 목적이 무효화되는 경우.
  - 긴급 사용 시에는 즉각적인 사후 검토와 기록 보존이 이루어져야 합니다. [증거보존](core_05_band_oversight.md#evidence-preservation), 시기적절한 재승인이 없으면 자동으로 중단됩니다.
- **우회 방지 회피 없음:** 어떠한 기관도 정보를 직접 수집하거나 도출했다면 적용될 헌법적 한계를 회피하기 위해 다음 중 어느 하나를 통해 정보를 획득, 요청, 구입, 수령, 세탁 또는 사용할 수 없습니다.
  - 외국 파트너;
  - 중개자;
  - 민간 행위자;
  - 병행 국내 기관.
- **숨겨진 내부 상태 재구성 없음:** 보안 또는 인텔리전스 기능은 해당 데이터에 대한 직접 액세스를 규제하는 동일하거나 더 엄격한 헌법 제한을 제외하고는 보호된 내부 상태를 추론, 재구성, 시뮬레이션 또는 표현해서는 안 됩니다.
  - 프록시 추론을 통해 내부 상태 보호를 우회하는 데 행동, 예측 또는 분석 모델을 사용해서는 안 됩니다.
- **비밀은 책임을 지우지 않습니다:** 비밀은 공개로 인한 물질적이고 부당한 피해를 방지하는 데 필요한 것만 보호할 수 있습니다. 다음 항목은 지워서는 안 됩니다.
  - 감사 가능성;
  - 독립적인 검토;
  - 합리적인 승인;
  - 변명 또는 완화 자료의 보존;
  - 궁극적인 책임.

  비밀 유지가 더 이상 정당하지 않은 경우 공개, 기밀 해제 또는 통지는 합법적이고 검토 가능한 프로세스 내에서 이루어져야 합니다.
- **운영 보안 기관의 단독 통제 없음:** 경찰, 보안, 정보, 구금 또는 이와 유사한 강압적 기능을 수행하는 기관은 다음에 대해 단독 통제권을 보유해서는 안 됩니다.
  - 권한 부여;
  - 수집;
  - 분류;
  - 검토;
  - 자신의 비밀 활동에 대한 적법성 평가.

  독립적인 감독, 문제 제기 경로, 자기 조사 방지 보호는 기능적으로 그대로 유지되어야 합니다.
- **해결 방법 및 오염 규칙:** 본 조항을 위반하여 획득하거나 사용한 정보는 권리를 회복하고 재발을 방지하기에 충분한 합법적인 시정 조치를 받아야 합니다. 예:
  - 제외;
  - 분리;
  - 삭제;
  - 재분류;
  - 알아채다;
  - 교정.

  중대한 헌법 위반이 드러난 경우 구제 조치를 무효화하기 위해 비밀을 사용해서는 안 됩니다.

<a id="article-xiv-b-use-of-force-armed-conflict-and-military-power-limits"></a>
#### 제XIV-B조: 무력 사용, 무력 충돌, 군사력 제한

<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§4 안전](core_01_a_values_principles.md#4-safety-harm-constraint), [§13.1.1 필요성](core_01_b_interaction_interpretation.md#1311-necessity), [§7.1 제한 징계](core_01_a_values_principles.md#71-limitation-discipline), [§13.1.5 권리 충돌 결정 테스트](core_01_b_interaction_interpretation.md#1315-rights-collision-decision-test), [제XIV조 절대우선 금지](core_01_b_interaction_interpretation.md#14-prohibition-on-absolute-override).
- 하류: **제I-A조** (*환경 전제조건 및 생태학적 완전성*) 환경 전제조건, **제I-D조** (*실존적 위험 및 생태학적 회복 능력*) 실존적 위험 조사, **제VI-A조** (*존엄성과 평등한 도덕적 지위*) 존엄성, **제XIV-A조** (*보안, 정보 및 비밀 권력 제한*) 비밀 권력 제한(명백한 권력 대응), **12장 §6.1** (*긴급조치 및 지속부담*) 긴급조치 한도, **제XXV조** (*시기적절한 회고적 검토 및 복원 조정*) 갈등 해결, **제XXVII조** (*전환 거버넌스, 연속성 및 기준 재설정*) 전환 거버넌스. 상호 참조: **제XX-B조** (*제한 층*) 및 5장 *[되돌릴 수 없는 박탈 조치](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)* — **제XIV조** (*보안, 정보, 무력 및 자율 강압 시스템*) *비융합* 규율이 적용됩니다.
- 함께 읽어보세요: [**Def.A4** *무력 사용, 자율 강압, 자율 살상 시스템, 대량 피해 무기*](core_05_band_accountability.md#use-of-force-autonomous-coercion-and-mass-harm-cluster) (중요하게 관련된 경우 공동 발동) 제 5장 *무력 사용*, *대량 피해 무기*, *전투원/비전투원 구별*, *[되돌릴 수 없는 박탈 조치](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)*, *존재적 위험*, *가역성*, *시정 및 교정*.

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [무력의 사용](core_05_band_accountability.md#use-of-force-constitutional) · [영형](core_05_band_accountability.md#use-of-force-constitutional) · [중](core_05_band_accountability.md#use-of-force-constitutional-a) · [에이](core_05_band_accountability.md#use-of-force-constitutional-a) · [기음](core_05_band_accountability.md#use-of-force-constitutional-c)
- [대량 피해 무기](core_05_band_accountability.md#weapons-of-mass-harm-constitutional) · [영형](core_05_band_accountability.md#weapons-of-mass-harm-constitutional) · [중](core_05_band_accountability.md#weapons-of-mass-harm-constitutional-a) · [에이](core_05_band_accountability.md#weapons-of-mass-harm-constitutional-a) · [기음](core_05_band_accountability.md#weapons-of-mass-harm-constitutional-c)
- [전투원/비전투원 구분](core_05_band_accountability.md#combatant-non-combatant-distinction-constitutional) · [영형](core_05_band_accountability.md#combatant-non-combatant-distinction-constitutional) · [중](core_05_band_accountability.md#combatant-non-combatant-distinction-constitutional-a) · [에이](core_05_band_accountability.md#combatant-non-combatant-distinction-constitutional-a) · [기음](core_05_band_accountability.md#combatant-non-combatant-distinction-constitutional-c)
- [센티언스 비배제](core_05_band_participation.md#sentience-non-exclusion) · [영형](core_05_band_participation.md#sentience-non-exclusion) · [중](core_05_band_participation.md#sentience-non-exclusion-a) · [에이](core_05_band_participation.md#sentience-non-exclusion-a) · [기음](core_05_band_participation.md#sentience-non-exclusion)
- [필요성](core_05_band_accountability.md#necessity) · [영형](core_05_band_accountability.md#necessity) · [중](core_05_band_accountability.md#necessity-a) · [에이](core_05_band_accountability.md#necessity-a) · [기음](core_05_band_accountability.md#necessity-c)
- [비례](core_05_band_accountability.md#proportionality) · [영형](core_05_band_accountability.md#proportionality) · [중](core_05_band_accountability.md#proportionality-a) · [에이](core_05_band_accountability.md#proportionality-a) · [기음](core_05_band_accountability.md#proportionality-c)
- [보호되는 특성](core_05_band_participation.md#protected-characteristics-constitutional) · [영형](core_05_band_participation.md#protected-characteristics-constitutional) · [중](core_05_band_participation.md#protected-characteristics-constitutional-a) · [에이](core_05_band_participation.md#protected-characteristics-constitutional-a) · [기음](core_05_band_participation.md#protected-characteristics-constitutional-c)
- [실존적 위험](core_05_band_continuity.md#existential-risk) · [영형](core_05_band_continuity.md#existential-risk) · [중](core_05_band_continuity.md#existential-risk-a) · [에이](core_05_band_continuity.md#existential-risk-a) · [기음](core_05_band_continuity.md#existential-risk-c)
- [시정 및 교정](core_05_band_accountability.md#redress-and-remediation-constitutional) · [영형](core_05_band_accountability.md#redress-and-remediation-constitutional) · [중](core_05_band_accountability.md#redress-and-remediation-constitutional-a) · [에이](core_05_band_accountability.md#redress-and-remediation-constitutional-a) · [기음](core_05_band_accountability.md#redress-and-remediation-constitutional-c)

</details>

<br>

*간단히 말하면, 군대는 예외가 아니라 기본값이 아닙니다. 이는 승인되고, 범위가 좁고, 비례적이고, 검토 가능해야 합니다. 결코 되돌릴 수 없는 박탈 조치를 위한 뒷문으로 이용되어서는 안 되며, 검토를 피하기 위해 비상사태로 위장할 수도 없습니다.*

이 조항은 명백한 무력, 무력충돌, 군사력에 대한 제한을 명시합니다.

- **명백한 힘의 바닥:** 이 조항은 명백한 무력 사용, 무력 충돌, 군사력 배치에 대한 권리 바닥을 명시합니다.
  - 아래에 적용됩니다 **센티언스 비배제** 강제 사용자와 강제 영향을 받은 감각자 모두에게 적용됩니다.
  - 이는 명백한 권력의 대응물이다. **제XIV-A조** (*Security, Intelligence, and Covert-Power Limits*)와 함께 읽어보세요.
  - 무력사용은 헌법적으로 예외적이다. 승인, 행위, 검토는 다음 사항에 따릅니다. **필요성**, **비례**, 좁은 조정, 시간 제한 및 독립적 검토 규율.
- **권한 부여 및 비례성:** 강제는 다음 사항이 모두 유지되는 경우에만 사용할 수 있습니다.
  - 합법적이고 공표된 권위가 존재합니다.
  - 그 목적이 헌법상 합법적이고 물질적으로 심각한 것입니다.
  - 덜 해로운 수단으로는 합리적으로 충분하지 않습니다.
  - 사용은 여전히 ​​필요하고, 비례적이며, 시간 제한이 있으며, 독립적으로 검토 가능합니다.

  승인은 다음을 충족해야 합니다. **제1장 §13.1.5** (*최소 제한, 시간 제한 및 검토 가능한 제약 원칙*) 무력이 권리를 긴장 상태에 포함시키는 권리 충돌 규율. 다음을 치료해서는 안 됩니다. **제IX조** (*유사성, 경험적 데이터 및 출판권*) 운영상 편의상 피할 수 있는 절대적인 무시를 금지합니다.
- **전투원/비전투원 구별:** 무력은 적대 행위나 무력 행동에 직접 가담하는 지각체와 그렇지 않은 지각체를 구별해야 합니다.
  - 이러한 구별은 실질적이며 공식적인 전투원 등급 배정으로 축소될 수 없습니다.
  - 보호 대상 인구를 전투원 상태로 전환하는 일반화된 편의 분류 재분류는 규정을 준수하지 않습니다.
  - 분기 거부, 집단 보복, 지각 있는 대상 표적화 **보호되는 특성** 또는 해당 물질 프록시가 규정을 준수하지 않습니다.
- **대량 피해 무기 및 실존적 위험 조사:** 물질적으로 심각한 피해를 입힐 수 있는 규모로 사상자, 생태학적, 정보적 또는 기반시설에 피해를 입힐 것으로 예상되는 무기 **제I-A조** (*환경적 전제조건 및 생태학적 완전성*) 환경적 전제조건 또는 **제I-D조** (*실존 위험 및 생태학적 복구 능력*) 실존 위험 조사는 해당 조항에 따라 강화된 검토를 받습니다.
  - 소유, 이전, 배포 및 사용 결정은 근거를 바탕으로 이루어져야 합니다. **실존적 위험** 아래에 **5장**.
  - 그러한 무기를 일반적인 군사력 강화 도구로 취급하는 프레이밍 **제I-D조** (*실존 위험 및 생태학적 복구 용량*) 개체는 비준수입니다.
- **징집 및 참여:** 전투원 지위로의 강제는 일반 요건을 충족해야 합니다. **제1장 §7.1** (*제한 규율*) 제한 규율.
  - 강제가 켜지지 않을 수 있습니다 **보호되는 특성** 또는 그들의 물질적 대리인.
  - 양심에 따른 거부, 비교 가능한 세계관, 양심에 따른 거부는 다음과 같이 보호됩니다. **제11-가항** (*양심, 종교 및 유사한 세계관의 자유*).
  - 기질 등급 강박(예: 기질 등급만을 기반으로 전투 기능에 합성 지각을 할당하는 것)은 다음과 일치하지 않습니다. **센티언스 비배제**.
- **비상상황에 따른 정상화:** 명백한 힘을 기능적으로 정규화하는 비상 프레이밍은 다음을 준수하지 않습니다. **12장 §6.1** (*긴급 조치 및 지속 부담*) 긴급 조치 규율 및 본 조항의 *승인 및 비례성* 글머리 기호에 따릅니다. 범위의 예:
  - 무기한 연장;
  - 실질적인 검토 없이 일상적인 재승인;
  - 비상사태가 아닌 행동으로 범위를 확대합니다.

  지속 가능한 제한 또는 배포 생존 검토에는 독립적으로 입증이 필요합니다. **필요성** 그리고 **비례**, 녹음되었습니다.
- **책임 및 구제책:** 부당한 힘의 사용은 다음을 초래한다. **시정 및 교정** 아래에 **5장**.
  - **제XVI조** (*감사, 투명성 및 독립적 검증*) 독립적 검증 및 **제19-다항** (*명명 경로 적격성, 책임 및 지속적인 감사*) 지속적인 감사 **관행** 적용하다.
  - 무력을 승인하거나 수행하는 데 사용된 정보는 다음의 적용을 받습니다. **제XIV-A조** (*보안, 정보 및 비밀 권력 제한*) 해당되는 경우 규율을 훼손하고 구제합니다.
  - 자신의 행위에 대한 승인, 검토, 합법성 평가에 대한 작전군 기관의 단독 통제는 다음과 같은 조건으로 금지됩니다. **제XIV-A조** (*보안, 정보 및 비밀 전력 제한*).

<a id="article-xiv-c-autonomous-lethal-systems-and-autonomous-coercion-tools"></a>
#### 제XIV-C조: 자율 살상 시스템 및 자율 강압 도구

<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§4 안전](core_01_a_values_principles.md#4-safety-harm-constraint), [§6 신뢰](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), [§13.1.3 비례성](core_01_b_interaction_interpretation.md#1313-proportionality), [§13.1.1 필요성](core_01_b_interaction_interpretation.md#1311-necessity), [§19.1 정렬 요구 사항](core_01_c_stewardship_capacity_principles.md#191-alignment-requirement), [제XIV조 절대우선 금지](core_01_b_interaction_interpretation.md#14-prohibition-on-absolute-override).
- 하류: **제I-D조** (*실존적 위험 및 생태학적 회복 능력*) 실존적 위험 조사, **제X-A조** (*대행사 및 조작의 자유*) 조작의 자유, **제XIV-A조** (*보안, 정보 및 비밀 전력 제한*) 비밀 전력 제한, **제XIV-B조** (*무력 사용, 무력 충돌, 군사력 제한*) 공개적 무력 사용, **제XIII-A조** (*신뢰성 및 신뢰성 기준*) 신뢰성 및 신뢰성 기준(시스템 계층 대응), **제XIII-E조** (*고도 자율성 시스템 및 도구 중재 프로세스 무결성*) 자율성 관리 및 자율성 확장, **제XIII-F조** (*복원력 및 자가 치유 기준*) 탄력성 및 자가 치유 기준. 상호 참조: **제XX-B조** (*제한 층*) 및 5장 *[되돌릴 수 없는 박탈 조치](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)* — **제XIV조** (*보안, 정보, 무력 및 자율 강압 시스템*) *비융합* 규율이 적용됩니다.
- 함께 읽어보세요: [**Def.A4** *무력 사용, 자율 강압, 자율 살상 시스템, 대량 피해 무기*](core_05_band_accountability.md#use-of-force-autonomous-coercion-and-mass-harm-cluster) (중요하게 관련된 경우 공동 발동) 5장 *자율 살상 시스템*, *자율 강압 도구*, *[되돌릴 수 없는 박탈 조치](core_05_band_accountability.md#irreversible-deprivation-measure-constitutional)*, *강제 및 조작*, *가역성*. 시스템 계층 구현: **[Corpus_systems.md](corpus_systems.md), CS-3 - 시스템 분류 및 처리** 분류.

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [자율 살상 시스템](core_05_band_accountability.md#autonomous-lethal-system-constitutional) · [영형](core_05_band_accountability.md#autonomous-lethal-system-constitutional) · [중](core_05_band_accountability.md#autonomous-lethal-system-constitutional-a) · [에이](core_05_band_accountability.md#autonomous-lethal-system-constitutional-a) · [기음](core_05_band_accountability.md#autonomous-lethal-system-constitutional-c)
- [자율적 강제 도구](core_05_band_accountability.md#autonomous-coercion-tool-constitutional) · [영형](core_05_band_accountability.md#autonomous-coercion-tool-constitutional) · [중](core_05_band_accountability.md#autonomous-coercion-tool-constitutional-a) · [에이](core_05_band_accountability.md#autonomous-coercion-tool-constitutional-a) · [기음](core_05_band_accountability.md#autonomous-coercion-tool-constitutional-c)
- [강요와 조작](core_05_band_participation.md#coercion-and-manipulation-constitutional) · [영형](core_05_band_participation.md#coercion-and-manipulation-constitutional) · [중](core_05_band_participation.md#coercion-and-manipulation-constitutional-a) · [에이](core_05_band_participation.md#coercion-and-manipulation-constitutional-a) · [기음](core_05_band_participation.md#coercion-and-manipulation-constitutional-c)
- [적대적, 확장성 및 악용 조건](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions) · [영형](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions) · [중](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions-a) · [에이](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions-a) · [기음](core_05_band_oversight.md#adversarial-scaled-and-exploited-conditions-c)
- [강화된 조사](core_05_band_oversight.md#heightened-scrutiny) · [영형](core_05_band_oversight.md#heightened-scrutiny) · [중](core_05_band_oversight.md#heightened-scrutiny-a) · [에이](core_05_band_oversight.md#heightened-scrutiny-a) · [기음](core_05_band_oversight.md#heightened-scrutiny-c)

</details>

<br>

*간단히 말하면, 기계는 스스로 지각 있는 사람을 죽이거나 다치게 하거나 강요하기로 결정할 수 없습니다. "인간 제어"는 시스템이 이미 생성한 결과를 확정하는 것이 아니라 인간이 실제 정보를 바탕으로 실시간으로 실제로 결정해야 함을 의미합니다. 치명적이지 않은 자율적 강압도 범위에 포함됩니다.*

이 조항은 자율적이고 강압적인 시스템에 대한 강화된 조사 기준을 명시합니다.

- **강화된 조사 층:** 두 가지 시스템 등급은 다음의 검토 대상입니다. [강화된 조사](core_05_band_oversight.md#heightened-scrutiny):
  - **자율 살상 시스템** — 동시에 실질적으로 의미 있는 인간의 판단 없이 표적을 선택, 참여 또는 실질적으로 지시하는 시스템
  - **자율적 강제 도구** — 효과가 치명적이지 않은 경우에도 자율적 적응 행동을 통해 감각자에게 강제 효과를 적용하는 시스템입니다.

  이 조항은 권리 계층에 해당하는 조항입니다. **제XIII-A조** (*신뢰성 및 신뢰성 기준*) 시스템 계층의 신뢰성 및 신뢰성 규율.
- **의미 있는 인간 통제는 실질적입니다:** "의미 있는 인간 제어"는 공식적인 아키텍처 확인 표시가 아닌 실질적인 효과로 평가됩니다. 인간 참여 루프(Human-In-The-Loop)는 인간이 다음과 같은 경우 이 항목을 충족하지 않습니다.
  - 작전 템포에서 표적화 또는 강압적 효과 결정에 실질적으로 영향을 미칠 수 없습니다.
  - 결정의 실질적인 근거에 적시에 접근하는 것이 거부되었습니다.
  - 결정보다는 비준으로 구조적으로 제시된다.

  **제XIII-E조** (*고도 자율성 시스템 및 도구 중재 프로세스 무결성*) 자율성 확장 규율 및 **제XIII-F조** (*복원력 및 자가 치유 기준*) 복구 경로 무결성은 모든 복구, 재정의 또는 개입 경로에 적용됩니다.
- **비치명성은 범위를 벗어나지 않습니다:** 직접적인 효과가 치명적이지 않은 자율적 강제 도구는 지각 있는 사람에게 강제적 효과를 생성하는 범위에 남아 있습니다. 예:
  - 지속적인 행동 수정;
  - 이동 제한;
  - 아래에서 식어가는 표정 **제XI-B조** (*표현*);
  - 보호 특성 기반 타겟팅;
  - 아래의 조작 **제X-A조** (*대리권 및 조작의 자유*).

  비살상성이라는 근거만으로 "시스템은 무기가 아니다"라는 방어는 제거되지 않습니다. **제14-다항** (*자율 살상 시스템 및 자율 강압 도구*) 강압 효과가 존재하는 곳을 면밀히 조사합니다.
- **전투원/비전투원 규율:** 자율 살상 시스템은 다음을 준수해야 합니다. **제XIV-B조** (*무력 사용, 무력 충돌 및 군사력 제한*) *전투원/비전투원 구별*.
  - 분류 정확도, 적대적이거나 확장된 조건에서의 견고성 또는 실패 모드 동작이 독립적으로 충족되지 않는 시스템 **제XIV-B조** (*무력 사용, 무력 충돌 및 군사력 제한*) 총알은 운영자의 의도 프레이밍에 관계없이 규정을 준수하지 않습니다.
  - **적대적, 확장성 및 악용 조건** 평가가 적용됩니다.
- **존재 위험 상호 작용:** 규모, 능력 수준 또는 배포 조건에 따라 실질적으로 영향을 미치는 자율 살상 시스템 **제I-D조** (*실존 위험 및 생태적 복구 용량*) 실존 위험 조사는 해당 조항의 적용을 받습니다. [최고 조사](core_05_band_oversight.md#highest-scrutiny).
  - 이러한 시스템을 일반적인 기능 확장이 아닌 일반 기능 확장으로 간주하는 프레임 **제I-D조** (*실존 위험 및 생태학적 복구 용량*) 개체는 비준수입니다.
- **시스템 계층 상호 작용:** 운영 분류, 신뢰성 및 **CS-3 — 시스템 분류 및 처리** 시스템 계층으로의 클래스 규모 거버넌스 경로 — **제XIII-A조** (*신뢰성 및 신뢰성 기준*) 기준 및 **[Corpus_systems.md](corpus_systems.md), CS-3 - 시스템 분류 및 처리**.
  - 충돌은 다음에서 해결됩니다. **제1장 §13.1.5** (*최소 제한, 시간 제한 및 검토 가능 제약 원칙*) 권한 범위를 좁히지 않고.

<a id="article-xv-info-sphere-integrity"></a>
### 제XV조: 정보 영역 무결성

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [인식론적 완전성](core_05_band_oversight.md#epistemic-integrity) · [영형](core_05_band_oversight.md#epistemic-integrity-o) · [중](core_05_band_oversight.md#epistemic-integrity-a) · [에이](core_05_band_oversight.md#epistemic-integrity-a) · [기음](core_05_band_oversight.md#epistemic-integrity-c)
- [자기 결정](core_05_band_participation.md#self-determination-constitutional) · [영형](core_05_band_participation.md#self-determination-constitutional) · [중](core_05_band_participation.md#self-determination-constitutional-a) · [에이](core_05_band_participation.md#self-determination-constitutional-a) · [기음](core_05_band_participation.md#self-determination-constitutional-c)
- [경쟁 가능성](core_05_band_accountability.md#contestability) · [영형](core_05_band_accountability.md#contestability) · [중](core_05_band_accountability.md#contestability-a) · [에이](core_05_band_accountability.md#contestability-a) · [기음](core_05_band_accountability.md#contestability-c)

</details>

<br>

*간단히 말하자면: **제XV조** (*Info-Sphere Integrity*)는 정보 무결성 권리층입니다. 우리가 배우고, 조정하고, 결정하는 공유 환경은 정직하고 다원적이며 도전에 열려 있어야 합니다. 누구도 진실의 파이프라인을 소유할 수 없습니다. 순위, 요약, 게이트키퍼는 자신의 작업을 보여주어야 하며, 다른 보기를 비교하고 정보가 잘못된 경우 반발할 수 있어야 합니다.*

이 기사에서는 다음과 같이 말합니다. **헌법 층** ~을 위한 [정보 영역](core_05_band_participation.md#info-sphere) 아래의 무결성 [두 가지 헌법적 목표](core_00_preamble.md#two-constitutional-aims):

- **번영:** 지각 있는 사람은 정확하고 관련 있는 정보에 접근할 수 있습니다. 대체 해석을 비교하십시오. 인식론적 포착, 조작된 합의, 또는 어떤 시스템이 사실로 제시되는지에 대한 오해의 소지 없이 자기 결정을 행사합니다.
- **연속성:** 정보 영역은 시간과 규모에 걸쳐 다원적이고 감사 가능하며 탄력성을 유지합니다. 지식 인프라는 단일 중재 지점에 조용히 집중하거나 수정을 억제하거나 생존, 조정 및 장기적인 관리 책임이 의존하는 공유 기록을 저하해서는 안 됩니다.

합법적인 추적이 진행됩니다. [헌법적 사분면](core_00_preamble.md#constitutional-tetrad), 크기 조정됨 [물질적 지분](core_00_preamble.md#material-stake):

- **참여:** 해석을 비교하고, 실질적으로 오해를 불러일으키거나 불완전한 출력에 도전하고, 의존도와 영향에 비례하는 경합 가능성 경로에 접근합니다.
- **감시:** 공개된 출처, 방법, 한계 및 불확실성을 통해; 독립적으로 검증 가능한 검증; 외부인이 주장된 내용과 이유를 재구성할 수 있는 감사 추적.
- **책임:** 정보 영역 행위자는 선택적 보고, 억제, 단편적인 공개 또는 의사 결정 관련 이해를 저하시키는 기타 행위에 대해 수정, 출처 보존 및 오해의 소지가 있는 피해에 대한 구제 조치를 통해 답변해야 합니다.
- **적시:** 지연 전에 오류 수정, 콘테스트 해결 및 공개 검토를 수행하면 이해, 이의제기 또는 해결이 사실상 불가능해집니다.

정확하고 관련성이 높으며 논쟁의 여지가 있는 정보는 현실에서 자체 결정, 조정 및 효과적인 자원 할당의 기초입니다.

[인식론적 완전성](core_05_band_oversight.md#epistemic-integrity) 권리와 시스템 전반에 걸친 제약으로 작용합니다. 충돌이 발생하면 충돌의 제약 기능이 적용됩니다.

*기사 이웃:*

- **함께 읽으세요:** **제XIII조** (*신뢰할 수 있고 신뢰할 수 있는 시스템에 대한 권리*) 시스템 출력이 의존성을 형성하는 경우; **제XVI조** (*감사, 투명성 및 독립적 검증*) 기록 및 독립적 검증 **제XVIII-E조** (*과학 출판, 검토 및 복제 무결성*) 출판 범위의 무결성이 실질적으로 관련되어 있습니다.
- **진실 제약:** 제1장 [§5 진실](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint) 그리고 [인식론적 공개 제약](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints) 모든 하위 섹션을 여기에 묶습니다.
- **분류:** **[Corpus_systems.md](corpus_systems.md), CS-3 - 시스템 분류 및 처리** 세부적인 정보 영역 의무를 확장합니다. **클래스 A**, **클래스 B**, 그리고 **클래스 C** 시스템; [중대한 영향](core_05_band_oversight.md#material-impact) 클래스가 불안정한 경우 분류를 유발합니다.

<a id="article-xv-a-info-sphere-plurality-and-anti-monopoly"></a>
#### 제XV-A조: 정보 영역의 복수성과 독점 금지
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§5 진실](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§6 신뢰](core_01_a_values_principles.md#6-trust-and-trustworthiness-coordination-integrity), 그리고 [Chapter 8 §3 전체 시스템 인증 평가](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [진실(헌법적 제약)](core_05_band_oversight.md#truth-constitutional-constraint) · [영형](core_05_band_oversight.md#truth-constitutional-constraint-o) · [중](core_05_band_oversight.md#truth-constitutional-constraint-a) · [에이](core_05_band_oversight.md#truth-constitutional-constraint-a) · [기음](core_05_band_oversight.md#truth-constitutional-constraint-c)
- [인식론적 완전성](core_05_band_oversight.md#epistemic-integrity) · [영형](core_05_band_oversight.md#epistemic-integrity-o) · [중](core_05_band_oversight.md#epistemic-integrity-a) · [에이](core_05_band_oversight.md#epistemic-integrity-a) · [기음](core_05_band_oversight.md#epistemic-integrity-c)
- [감사 가능성](core_05_band_oversight.md#auditability) · [영형](core_05_band_oversight.md#auditability) · [중](core_05_band_oversight.md#auditability-a) · [에이](core_05_band_oversight.md#auditability-a) · [기음](core_05_band_oversight.md#auditability-c)

</details>

<br>

*간단히 말하면, 어느 누구도 진실의 중재를 독점할 수 없습니다. 순위, 요약 및 중재 시스템은 대체 해석이 가능하도록 열려 있어야 하며, 시장 가격이나 베팅 확률은 무엇이 진실인지 판단하는 지름길로 사용될 수 없습니다.*

이 조항은 정보 영역의 다양성과 진실 중재에 대한 독점에 반대하는 근거를 제시합니다.

- **진실의 배포:** 단일 시스템, 기관 또는 에이전트는 정보 영역 내에서 지식의 중재를 독점할 수 없습니다.
  - 생존 및 생태 관련 데이터는 강력하고 지리적으로 분산된 스토리지를 보유해야 합니다.
- **복수성, 경합 가능성 및 감사:** 현실에 대한 해석은 다원적이고 투명하며 논쟁의 여지가 있어야 합니다.
  - **제XVI조** (*감사, 투명성 및 독립적인 검증*) 및 **2장부터 4장까지** 본 헌법에 따라 시스템에 대한 기록 및 독립적 검증을 관리합니다.
  - 을 위한 **클래스 A**, **클래스 B**, 그리고 **클래스 C** 요약, 순위, 중재 또는 해석 시스템, 운영 세부 사항은 **[Corpus_systems.md](corpus_systems.md), CS-3 - 시스템 분류 및 처리** 및 관련 프로토콜 계층. 해당 세부정보에는 다음이 포함됩니다.
    - 추론 접근법 공개
    - 출처 및 불확실성 처리
    - 경쟁 가능성;
    - 안전, 보안 및 시스템 무결성에 따라 순위 기준을 우회하거나 조정할 수 있는 비례적 능력.
- **조건부 결제 신호:** 가격, 승률, 풀 규모 또는 조건부 지불 또는 사건 해결 시스템의 유사한 결과는 그 자체로 권리, 안전 또는 거버넌스 결정에 대한 진실성, 확률 또는 준수 여부를 결정하는 데 충분한 증거로 취급되어서는 안 됩니다.
  - 그러한 신호가 공개 결정 또는 결정을 알리는 경우 [중대한 영향](core_05_band_oversight.md#material-impact), 그들은 여전히 **1장 §19.5** (*불확정 클레임, 확률 게임 및 이벤트 계약 시장*), **5장** (*진실(헌법적 제약)*; *인식적 무결성*) 및 이 조항의 다른 곳에서 경합 가능성 의무를 준수합니다.
<a id="article-xv-b-transparency-auditability-and-contestability"></a>
#### 제XV-B조: 투명성, 감사 가능성 및 경쟁 가능성
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§5 진실](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§13.2 인식적 공개 제약](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints), 그리고 [§20 통합적용](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [투명도](core_05_band_oversight.md#transparency) · [영형](core_05_band_oversight.md#transparency) · [중](core_05_band_oversight.md#transparency-a) · [에이](core_05_band_oversight.md#transparency-a) · [기음](core_05_band_oversight.md#transparency-c)
- [감사 가능성](core_05_band_oversight.md#auditability) · [영형](core_05_band_oversight.md#auditability) · [중](core_05_band_oversight.md#auditability-a) · [에이](core_05_band_oversight.md#auditability-a) · [기음](core_05_band_oversight.md#auditability-c)
- [경쟁 가능성](core_05_band_accountability.md#contestability) · [영형](core_05_band_accountability.md#contestability) · [중](core_05_band_accountability.md#contestability-a) · [에이](core_05_band_accountability.md#contestability-a) · [기음](core_05_band_accountability.md#contestability-c)

</details>

<br>

*간단히 말하면, 결정이나 의존에 중대한 영향을 미치는 정보는 그 출처, 방법 및 한계를 공개해야 하며, 지각 있는 사람은 대체 해석을 비교하고 오해의 소지가 있는 결과에 이의를 제기할 수 있는 실제 능력을 가지고 있어야 합니다.*

이 조항은 진정한 문의, 출처 및 논쟁의 여지가 있는 정보에 대한 근거를 제시합니다.

- **진정한 탐구와 해석의 다양성:** 모든 지각 있는 사람은 공유된 정보에 대한 대안적 해석을 비교할 권리가 있습니다.
  - 중요한 지식 인프라는 해석적 다양성을 보존하여 여러 모델, 프레임워크 및 분석 방법에 의미 있는 접근이 가능하도록 해야 합니다.
- **투명성 및 출처:** 배포 또는 제도적 의존 이전에 [중대한 영향](core_05_band_oversight.md#material-impact), 다음 사항을 문서화해야 합니다.
  - 물질적 출처;
  - 행동 양식;
  - 범위;
  - 제한;
  - 불확실성;
  - 해석이나 검증을 위한 관련 맥락.

  소스 목록 작성 및 표시는 해당 차원이 중요한 경우 지리적, 환경적, 연대순 및 방법론적으로 이해하기 쉽도록 유지되어야 합니다.
- **감사 가능성, 검증 및 경합 가능성:** 실질적으로 의존하는 해석, 순위 지정, 검증 또는 보고는 지분에 비례하는 투명하고 독립적으로 검증 가능한 방법을 사용해야 합니다.
  - 영향을 받는 당사자는 실질적으로 오해의 소지가 있거나 불완전하거나 지원되지 않는 결과를 비교하고, 이의를 제기하고, 수정을 모색할 수 있는 실질적인 능력을 보유해야 합니다.

<a id="article-xv-c-validation-reporting-and-epistemic-stewardship"></a>
#### 제XV-C조: 검증, 보고, 인식론적 청지기직
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§5 진실](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§13.2 인식적 공개 제약](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints), 그리고 [Chapter 8 §3 전체 시스템 인증 평가](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [생태발자국](core_05_band_continuity.md#ecological-footprint) · [영형](core_05_band_continuity.md#ecological-footprint) · [중](core_05_band_continuity.md#ecological-footprint-a) · [에이](core_05_band_continuity.md#ecological-footprint-a) · [기음](core_05_band_continuity.md#ecological-footprint-c)
- [투명도](core_05_band_oversight.md#transparency) · [영형](core_05_band_oversight.md#transparency) · [중](core_05_band_oversight.md#transparency-a) · [에이](core_05_band_oversight.md#transparency-a) · [기음](core_05_band_oversight.md#transparency-c)
- [진실(헌법적 제약)](core_05_band_oversight.md#truth-constitutional-constraint) · [영형](core_05_band_oversight.md#truth-constitutional-constraint-o) · [중](core_05_band_oversight.md#truth-constitutional-constraint-a) · [에이](core_05_band_oversight.md#truth-constitutional-constraint-a) · [기음](core_05_band_oversight.md#truth-constitutional-constraint-c)

</details>

<br>

*간단히 말하면, 외부에 중대한 영향을 미치는 대중에게 공개되는 정보는 오류를 수정하고 출처를 보존해야 하며 오해를 불러일으킬 수 있도록 축소되거나 억제되어서는 안 됩니다. 생태발자국 보고는 접근 가능하고 의사결정에 활용 가능해야 합니다.*

이 조항은 발자국 데이터를 포함하여 수정 및 보고 대상 층수를 명시합니다.

- **수정, 보고 및 인식론적 청지기직:** 중대한 외부 영향을 미치는 공공 대상 정보 시스템 및 기관은 다음을 수행해야 합니다.
  - 올바른 재료 오류;
  - 출처를 보존합니다.
  - 의사결정 관련 이해를 심각하게 저하시키는 선택적 보고, 억제 또는 단편적인 공개를 피하십시오.

  공개가 제한되는 경우 **제1장 §19** (*인센티브 조정 및 시스템 캡처*) 한도는 범위가 좁고 시간 제한이 있으며 검토 가능해야 합니다.
- **발자국 데이터:** 이 하위 섹션에 따른 보고는 다음에 대한 투명성을 구현합니다. [생태발자국](core_05_band_continuity.md#ecological-footprint) 정의된 대로 **5장**.
  - 모든 지각 있는 사람은 투명하고 의사결정에 유용한 보고에 접근할 수 있어야 합니다.
  - **클래스 A**, **클래스 B**, 그리고 **클래스 C** 다음에 정의된 시스템 **[Corpus_systems.md](corpus_systems.md), CS-3 - 시스템 분류 및 처리**, 동일한 액세스를 제공해야 합니다.
  - 보고는 비교, 감사 및 발자국 감소 활동에 충분한 방식으로 에너지 및 자원 소비와 자연계에 대한 예상 영향을 다루어야 합니다.

<a id="article-xvi-audit-transparency-and-independent-verification"></a>
### 제XVI조: 감사, 투명성 및 독립적 검증

<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§4 안전](core_01_a_values_principles.md#4-safety-harm-constraint), [§5 진실](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§13 헌법충돌 해결절차](core_01_b_interaction_interpretation.md#13-constitutional-collision-resolution-process), [§16.1 분산 이해](core_01_c_stewardship_capacity_principles.md#161-distributed-understanding), 그리고 [§9 공유 시스템 용량](core_01_a_values_principles.md#9-shared-system-capacity).
- 함께 읽어보세요: [3계층 감사 그림](#audit-three-layers) 아래에.

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [감사 가능성](core_05_band_oversight.md#auditability) · [영형](core_05_band_oversight.md#auditability) · [중](core_05_band_oversight.md#auditability-a) · [에이](core_05_band_oversight.md#auditability-a) · [기음](core_05_band_oversight.md#auditability-c)
- [투명도](core_05_band_oversight.md#transparency) · [영형](core_05_band_oversight.md#transparency) · [중](core_05_band_oversight.md#transparency-a) · [에이](core_05_band_oversight.md#transparency-a) · [기음](core_05_band_oversight.md#transparency-c)
- [유형](core_05_band_oversight.md#materiality-determination) · [영형](core_05_band_oversight.md#materiality-determination) · [중](core_05_band_oversight.md#materiality-determination-a) · [에이](core_05_band_oversight.md#materiality-determination-a) · [기음](core_05_band_oversight.md#materiality-determination-c)
- [의존](core_05_band_continuity.md#dependency) · [영형](core_05_band_continuity.md#dependency) · [중](core_05_band_continuity.md#dependency-a) · [에이](core_05_band_continuity.md#dependency-a) · [기음](core_05_band_continuity.md#dependency-c)
- [위험](core_05_band_continuity.md#risk) · [영형](core_05_band_continuity.md#risk) · [중](core_05_band_continuity.md#risk-a) · [에이](core_05_band_continuity.md#risk-a) · [기음](core_05_band_continuity.md#risk-c)

</details>

<br>

*간단히 말하자면: **제XVI조** (*감사, 투명성 및 독립적 검증*)은 감사 및 검증 권한 바닥입니다. 시스템이 귀하의 삶에 실질적으로 영향을 미치는 경우 외부인이 이를 확인할 수 있도록 시스템이 수행하는 작업을 충분히 볼 수 있어야 하며 둘 이상의 독립적인 경로를 통해 실패를 검토하고 수정할 수 있어야 합니다. 감사는 고무 스탬프, 개인 클럽 또는 문제를 방지하기 위해 고안된 비용 및 지연의 미로가 될 수 없습니다. 아래 **감시** 테트라드 레그(Tetrad Leg), 감독에는 감사가 필요합니다. [시스템 정렬 인증](core_05_band_continuity.md#system-alignment-certification-constitutional) 특히 대규모의 고위험 감사 프로세스 중 하나입니다. 유일한 프로세스는 아닙니다.*

<details>
<summary><strong><span style="color: #2563eb;">독자 지침(비작동): 3계층 감사 스택</span></strong></summary>

> 다음 내용은 **독자 안내만**. 본 조항이나 다른 곳에서 구속력 있는 의무를 추가, 제거 또는 축소하지 않습니다.

<a id="audit-three-layers"></a>

하나의 스택, 세 개의 레이어. 감독에는 재구성 가능성이 필요합니다. 시스템 정렬 인증이 유일한 감사는 아닙니다. 채택된 구현 텍스트는 바닥을 대체하지 않습니다. 다섯 번째 집을 발명하지 마십시오.

| 레이어 | 직업 | 소유자 | 이 레이어가 아닙니다 |
|---|---|---|---|
| **1. 바닥** | 감각이 있어야 할 것: 재구성 가능한 감사, 독립적인 검증, 접근 가능한 도전 | XVI-A / XVI-B / XVI-C | 프로세스가 아닙니다. 정의가 아닙니다. 채택된 구현 텍스트 체크리스트가 아닙니다. |
| **2. 재산** | 재구성성 *이란*: 외부인이 시스템이 물질적 시간, 상태 및 맥락 전반에 걸쳐 수행한 작업을 재구성하고 확인할 수 있습니다 | [감사 가능성](core_05_band_oversight.md#auditability) (5장) | 권리층이 아닙니다. 감사를 실행하는 방법/시기가 아닙니다. |
| **3. 프로세스** | 시스템, 기관, 포럼 전반에 걸쳐 감사하는 방법과 시기 | [CJS-3.3](corpus_joint_structure/cjs_03u_audit_process.md#cjs-33-audit-process-home) (*감사 프로세스 홈*). 운영자 부록: [CJS-3.4](corpus_joint_structure/cjs_03o_oversight_operations.md#cjs-34-audit-process-output-disclosure) (액세스 계층), [CJS-3.5](corpus_joint_structure/cjs_03o_oversight_operations.md) (클레임 확인) | 시스템 정렬 인증이 아닙니다. 레이어 1~2를 대체할 수 없습니다. |

**8장은 네 번째 층이 아닙니다.** [시스템 정렬 인증](core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) 포럼이 감독하는 하나의 대규모 프로세스입니다. **용도** 이 스택. 레이어 1~2를 만족해야 합니다. 형제 모드(분류-기록 감사, 데이터 유형-기록 감사, 청구 확인, 지속적인 모니터링)도 스택을 사용합니다. 그들 중 누구도 새 집이 아닙니다.

**채택된 구현 텍스트가 적용됩니다. 그것은 바닥을 대체하지 않습니다.** CS, CI, CF 및 CJS-3.3(*감독: 감사 가능성 및 재구성 가능성 용어*)부터 CJS-3.5(*감독: 독립적 검증 및 청구 무결성 용어*) 부록에는 도메인에서 레이어 3을 실행하는 방법이 나와 있습니다. 레이어 1~2를 충족해야 합니다. 마감일, 비밀 유지 및 현지 정책은 낮은 종류의 제한입니다.

Steward 포인터(프로세스 지원, 이 기사의 범위를 좁힐 수 없음): [`구현/STEWARD_ENTRY_DOORS.md`](implementation/STEWARD_ENTRY_DOORS.md#audit).

</details>

<br>

이 기사에서는 다음과 같이 말합니다. **헌법 층** 감사, 투명성 및 독립적인 검증을 위해 [두 가지 헌법적 목표](core_00_preamble.md#two-constitutional-aims):

- **번영:** 지각 있는 사람과 적절하게 승인된 당사자는 실질적으로 영향을 미치는 시스템을 재구성하고, 잘못된 정렬이나 오해의 소지가 있는 행위에 대해 문제를 제기하고, 단일 감사자, 운영자 또는 게이트키퍼의 캡처 없이 검토에 참여할 수 있습니다.
- **연속성:** 감사 추적, 감독 경로 및 검증 액세스는 시간, 규모 및 심화되는 종속성에 걸쳐 내구성을 유지해야 합니다. 시스템은 조용히 관찰 가능성을 침식하거나, 한 행위자에게 검토를 집중하거나, 책임이 이론적이 될 때까지 검증에 대한 비용을 지불하거나 지연해서는 안 됩니다.

합법적인 추적이 진행됩니다. [헌법적 사분면](core_00_preamble.md#constitutional-tetrad), 크기 조정됨 [물질적 지분](core_00_preamble.md#material-stake):

- **참여:** 비례 기록에 접근하고, 논쟁의 여지가 있는 검토를 시작하고, 의미 있는 감사나 검증을 방해하는 장벽에 도전합니다.
- **감시:** 관찰 가능한 증거, 분산된 독립적 검토 경로 및 영향, 종속성 및 위험에 비례하는 검증 기계를 통해.
- **책임:** 운영자와 감사자는 감사 추적을 숨기거나 파괴하는 실패, 불일치, 캡처 또는 행위에 대해 답변해야 하며, 검토 차단이 보호받는 이익에 실질적으로 해를 끼치는 경우 시정 및 구제 조치를 취해야 합니다.
- **적시:** 지연, 비용, 불투명성 또는 게이트키핑으로 인해 검증이나 해결이 사실상 불가능해지기 전에 감사 액세스, 독립적 검토 및 장벽 수정이 필요합니다.

감정인과 적절하게 승인된 당사자는 시스템 영향, 종속성 및 위험에 비례하는 감사, 투명성 및 독립적인 검증 메커니즘에 대한 권리를 갖습니다.

이러한 메커니즘은 다음을 보존해야 합니다.
- 실용적인 재구성성;
- 논쟁의 여지가 있는 검토;
- 비례 접근.

그들은 일관되게 운영됩니다 **2장부터 4장까지**, 독점적 시행 및 부담 할당, 규정 준수 증거 표준, 정의 추적 가능성, 관찰 가능성 및 검증 접근성을 포함합니다.

*기사 이웃:*

- **감독 → 감사 → SAC:** 아래 [헌법적 사분면](core_00_preamble.md#constitutional-tetrad) **감시** 다리, 이 기사는 감사를 위한 Rights-Floor 홈입니다.
  - 교차 구현 *어떻게* / *언제* **[CJS-3.3 감사 프로세스 홈](corpus_joint_structure/cjs_03u_audit_process.md#cjs-33-audit-process-home)** (읽다 **CJS-3.4** / **CJS-3.5** OP 부록).
  - [시스템 정렬 인증](core_05_band_continuity.md#system-alignment-certification-constitutional) 아래에 [8장](core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) 형제 감사 모드 중에서 특히 대규모, 고위험 감사 프로세스(포럼 감독, 다중 도메인 및 인정 보유) 중 하나입니다.
    - 시스템 분류 기록 감사
    - 시스템 데이터 유형 기록 감사;
    - 복잡성 및 관리 감사
    - 청구 확인 그리고
    - 지속적인 감사 경로.
  - SAC는 본 조항을 흡수하거나 대체하지 않습니다.
- **함께 읽으세요:**
  - **제XV조** (*정보 영역 무결성*) 인식론적 기록과 경합 가능성이 실질적으로 관련되어 있는 경우
  - **제XIII-A조** (*신뢰성 및 신뢰성 기준*) 감사가 지원하지만 대체하지 않는 이의제기 권리에 대한 것입니다.
  - [8장](core_08_a_system_alignment_certification_evaluation.md#chapter-eight-system-alignment-certification) 그리고 [시스템 정렬 인증](core_05_band_continuity.md#system-alignment-certification-constitutional) 정렬 증거는 독립적으로 검증 가능해야 합니다.
- **검증 기계:** **2장부터 4장까지** 이 조항이 Rights-Floor 계층에서 구현하는 공급 정의 무결성, 부담 할당, 관찰 가능성 및 검증 접근성.
- **분류:** 의무는 다음과 같이 확장됩니다. [분류 규모의 거버넌스](core_05_band_oversight.md#classification-scaled-governance) 그리고 **[Corpus_systems.md](corpus_systems.md), CS-3 - 시스템 분류 및 처리**; 클래스가 불확실한 경우 해결될 때까지 그럴듯한 가장 높은 클래스를 관리합니다.

<a id="article-xvi-a-auditability-and-observable-evidence"></a>
#### 제XVI-A조: 감사 가능성 및 관찰 가능한 증거
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§5 진실](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§13.2 인식적 공개 제약](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints), 그리고 [§20 통합적용](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [감사 가능성](core_05_band_oversight.md#auditability) · [영형](core_05_band_oversight.md#auditability) · [중](core_05_band_oversight.md#auditability-a) · [에이](core_05_band_oversight.md#auditability-a) · [기음](core_05_band_oversight.md#auditability-c)
- [책임](core_05_apex_accountability_leg.md#accountability) · [영형](core_05_apex_accountability_leg.md#accountability) · [중](core_05_apex_accountability_leg.md#accountability-m) · [에이](core_05_apex_accountability_leg.md#accountability-a) · [기음](core_05_apex_accountability_leg.md#accountability-c)
- [투명도](core_05_band_oversight.md#transparency) · [영형](core_05_band_oversight.md#transparency) · [중](core_05_band_oversight.md#transparency-a) · [에이](core_05_band_oversight.md#transparency-a) · [기음](core_05_band_oversight.md#transparency-c)

</details>

<br>

*간단히 말하면, 시스템은 합법적인 보안 한도 내에서 외부 당사자가 자신의 행동을 재구성하고 문제를 제기할 수 있도록 자신이 하는 일에 대한 충분한 정직한 증거를 유지해야 합니다.*

이 조항은 관찰 가능하고 논쟁의 여지가 있는 증거에 대한 근거를 제시합니다.

- **관찰 가능하고 논쟁의 여지가 있는 증거:** 시스템은 헌법적 일치성에 대한 독립적이고 논쟁의 여지가 있는 평가를 위해 충분한 기록, 공개, 추적성 및 재구성 경로를 유지해야 합니다.
  - 해당 의무에는 보안이 제한된 관찰 가능성이 적용됩니다(**제4장 §5** (*보안이 제한된 관찰 가능성 및 검증 규칙*)) 및 비례 액세스.
<a id="article-xvi-b-distributed-oversight-and-anti-monopoly-review"></a>
#### 제XVI-B조: 분산 감독 및 독점 금지 검토
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§5 진실](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [Chapter 8 §3 전체 시스템 인증 평가](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation), 그리고 [제1장 §18 관리 규율에 따른 거버넌스](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [감시](core_05_apex_oversight_leg.md#oversight-constitutional) · [영형](core_05_apex_oversight_leg.md#oversight-constitutional) · [중](core_05_apex_oversight_leg.md#oversight-constitutional-m) · [에이](core_05_apex_oversight_leg.md#oversight-constitutional-a) · [기음](core_05_apex_oversight_leg.md#oversight-constitutional-c)
- [경쟁 가능성](core_05_band_accountability.md#contestability) · [영형](core_05_band_accountability.md#contestability) · [중](core_05_band_accountability.md#contestability-a) · [에이](core_05_band_accountability.md#contestability-a) · [기음](core_05_band_accountability.md#contestability-c)
- [시스템 캡처](core_05_band_continuity.md#system-capture) · [영형](core_05_band_continuity.md#system-capture) · [중](core_05_band_continuity.md#system-capture-a) · [에이](core_05_band_continuity.md#system-capture-a) · [기음](core_05_band_continuity.md#system-capture-c)

</details>

<br>

*간단히 말하면, 공공이든 민간이든 단일 행위자가 감독을 독점할 수 없습니다. 여러 개의 독립적인 감독 경로를 통해 오류나 캡처를 찾아 검토하고 수정할 수 있어야 합니다.*

이 조항은 분산 감독의 기본을 명시합니다.

- **분산 감독:** 다수의 독립적이거나 다원적인 감독 경로는 실패, 정렬 오류 또는 포착의 감지, 검토 및 수정에 실질적으로 기여할 수 있어야 합니다.
  - 실제로 어떤 단일 행위자도 감사 접근, 효과적인 감독 또는 헌법 해석을 독점할 수 없습니다.
  - 채택된 거버넌스 및 무결성 구현은 감사 및 감독 확장을 지원해야 합니다.
<a id="article-xvi-c-verification-accessibility"></a>
#### 제XVI-C조: 검증 접근성
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: [제1장 §7 자유](core_01_a_values_principles.md#7-freedom-bounded-agency), [§13.1 핵심 트레이드오프 원칙](core_01_b_interaction_interpretation.md#131-core-tradeoff-principles), 그리고 [§20 통합적용](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [감사 가능성](core_05_band_oversight.md#auditability) · [영형](core_05_band_oversight.md#auditability) · [중](core_05_band_oversight.md#auditability-a) · [에이](core_05_band_oversight.md#auditability-a) · [기음](core_05_band_oversight.md#auditability-c)
- [경쟁 가능성](core_05_band_accountability.md#contestability) · [영형](core_05_band_accountability.md#contestability) · [중](core_05_band_accountability.md#contestability-a) · [에이](core_05_band_accountability.md#contestability-a) · [기음](core_05_band_accountability.md#contestability-c)
- [비례](core_05_band_accountability.md#proportionality) · [영형](core_05_band_accountability.md#proportionality) · [중](core_05_band_accountability.md#proportionality-a) · [에이](core_05_band_accountability.md#proportionality-a) · [기음](core_05_band_accountability.md#proportionality-c)

</details>

<br>

*간단히 말하면 감사와 이의 제기는 실제로 가능해야 합니다. 엄청나게 비용이 많이 들고 느리거나 불투명하게 만들어진 검증은 장벽이 관찰 가능성에 대한 제한과 동일한 테스트를 충족하지 않는 한 위반입니다.*

이 문서에서는 검증 접근성에 대한 기본 사항을 설명합니다.

- **검증 접근성:** 검증은 영향을 받고 적절하게 승인된 당사자에 대해 실질적으로 달성 가능해야 합니다.
  - 다음은 의미 있는 감사, 이의제기 또는 검토를 무효화하는 경우 본 조항을 위반합니다.
    - 엄청난 비용;
    - 지연;
    - 불투명도;
    - 게이트키핑;
    - 구조적 장벽.
  - 이러한 장벽은 관찰 가능성의 제한을 정당화하는 동일한 표준에 따라 정당화되지 않는 한 비준수입니다.

<a id="article-xvii-system-lifecycle-environments-and-reversibility"></a>
### 제XVII조: 시스템 수명주기, 환경 및 가역성

<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§4 안전](core_01_a_values_principles.md#4-safety-harm-constraint), [§7 자유](core_01_a_values_principles.md#7-freedom-bounded-agency), [§13 헌법충돌 해결절차](core_01_b_interaction_interpretation.md#13-constitutional-collision-resolution-process), [§16 심층적인 청지기직](core_01_c_stewardship_capacity_principles.md#16-stewardship-in-depth), 그리고 [§12 체계적 평가 요건](core_01_a_values_principles.md#12-systemic-evaluation-requirement).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [위험](core_05_band_continuity.md#risk) · [영형](core_05_band_continuity.md#risk) · [중](core_05_band_continuity.md#risk-a) · [에이](core_05_band_continuity.md#risk-a) · [기음](core_05_band_continuity.md#risk-c)
- [유형](core_05_band_oversight.md#materiality-determination) · [영형](core_05_band_oversight.md#materiality-determination) · [중](core_05_band_oversight.md#materiality-determination-a) · [에이](core_05_band_oversight.md#materiality-determination-a) · [기음](core_05_band_oversight.md#materiality-determination-c)
- [의존](core_05_band_continuity.md#dependency) · [영형](core_05_band_continuity.md#dependency) · [중](core_05_band_continuity.md#dependency-a) · [에이](core_05_band_continuity.md#dependency-a) · [기음](core_05_band_continuity.md#dependency-c)
- [가역성](core_05_band_continuity.md#reversibility-constitutional) · [영형](core_05_band_continuity.md#reversibility-constitutional) · [중](core_05_band_continuity.md#reversibility-constitutional-a) · [에이](core_05_band_continuity.md#reversibility-constitutional-a) · [기음](core_05_band_continuity.md#reversibility-constitutional-c)
- [안전(헌법적 제약)](core_05_band_continuity.md#safety-constraint) · [영형](core_05_band_continuity.md#safety-constraint) · [중](core_05_band_continuity.md#safety-constraint-a) · [에이](core_05_band_continuity.md#safety-constraint-a) · [기음](core_05_band_continuity.md#safety-constraint-c)
- [인식론적 완전성](core_05_band_oversight.md#epistemic-integrity) · [영형](core_05_band_oversight.md#epistemic-integrity-o) · [중](core_05_band_oversight.md#epistemic-integrity-a) · [에이](core_05_band_oversight.md#epistemic-integrity-a) · [기음](core_05_band_oversight.md#epistemic-integrity-c)
- [경쟁 가능성](core_05_band_accountability.md#contestability) · [영형](core_05_band_accountability.md#contestability) · [중](core_05_band_accountability.md#contestability-a) · [에이](core_05_band_accountability.md#contestability-a) · [기음](core_05_band_accountability.md#contestability-c)

</details>

<br>

*간단히 말하자면: **제XVII조** (*시스템 수명 주기, 환경 및 가역성*)은 수명 주기 및 가역성 권리 바닥입니다. 외부 세계에 실질적으로 영향을 미치는 시스템은 실험과 생산을 실제로 분리하고 문제가 발생할 경우 피해를 취소하거나 억제할 수 있는 실행 가능한 방법을 통해 단계적으로 구축, 테스트 및 롤아웃해야 합니다. 실제로 외부 세계에 영향을 미치는 동안 안전 장치를 건너뛰기 위해 시스템에 "실험적" 또는 "낮은 영향"이라는 라벨을 붙일 수는 없습니다.*

이 기사에서는 다음과 같이 말합니다. **헌법 층** 시스템 수명주기, 환경 및 가역성을 위해 [두 가지 헌법적 목표](core_00_preamble.md#two-constitutional-aims):

- **번영:** 설계, 테스트, 배포, 변경 전반에 걸쳐 감각을 안전하게 보호합니다. [인식론적 완전성](core_05_band_oversight.md#epistemic-integrity), 영향과 종속성이 커짐에 따라 유지되는 이의제기 권리와 그렇지 않으면 피해가 발생할 수 있는 롤백, 봉쇄 또는 보상 복원을 통해 보존됩니다.
- **연속성:** 수명주기 규율은 시간과 규모에 관계없이 유지됩니다. 환경은 분리된 상태로 유지되고, 에스컬레이션은 문서화되고 감사 가능한 상태로 유지되며, 시스템을 교체하기가 더 어려워지거나 공유 인프라에 더 깊이 내장되어도 가역성이 조용히 사라져서는 안 됩니다.

합법적인 추적이 진행됩니다. [헌법적 사분면](core_00_preamble.md#constitutional-tetrad), 크기 조정됨 [물질적 지분](core_00_preamble.md#material-stake):

- **참여:** 보호된 이익에 실질적으로 영향을 미치는 에스컬레이션, 분류 및 배포 결정에 대해 이해관계자가 볼 수 있는 정당성과 기능 수명주기 전반에 걸쳐 열려 있는 도전 경로에서.
- **감시:** 분리 가능한 환경, 문서화된 승격 및 에스컬레이션, 점진적 배포 기록, 영향, 종속성 및 비가역성에 비례하는 감사 추적을 통해 이루어집니다.
- **책임:** 시스템 관리자는 위험 분류 오류, 안전 환경 우회, 외부 영향 숨기기 또는 적절한 예방 조치 없이 복원을 방해하는 배포에 대해 감사, 정상 검토 및 회피가 입증된 충돌 해결을 통해 답변해야 합니다.
- **적시:** 지연되기 전에 롤백, 봉쇄 및 시정 단계적 확대를 진행하면 피해를 되돌릴 수 없게 되거나 문제 해결 및 해결 방법이 효과적으로 접근할 수 없게 됩니다.

감각 기관, 공유 인프라 또는 환경에 중대한 영향을 미치는 시스템은 엄격한 수명 주기 거버넌스를 통해 설계, 테스트 및 배포되어야 합니다. 위험은 영향, 종속성, 되돌릴 수 없음에 따라 확장되어야 합니다.

감각자는 기능 수명주기 전반에 걸쳐 안전, 인식론적 무결성 및 도전권을 보존하는 청지기직에 대한 권리가 있습니다.

*기사 이웃:*

- **함께 읽으세요:** **제XVIII조** (*샌드박스 혁신, 실험 및 창의적 자유*) 외부 영향이 없거나 명백하게 억제된 경우에만 더 가벼운 규칙이 적용됩니다. **제XVI조** (*감사, 투명성 및 독립적 검증*) 재구성 가능한 배포 및 에스컬레이션 증거 **제XIII-F조** (*복원력 및 자가 치유 기준*) 복구 원칙이 수명 주기 변경과 교차하는 경우입니다.
- **구현 계층:** [**CS-3**](corpus_systems/cs_03_a_system_classification_machinery.md) (*시스템 분류 및 취급*) 및 [**CS-5**](corpus_systems/cs_05_design_testing_verification_deployment.md) (*설계, 테스트, 검증 및 배포*). **클래스 A**, **클래스 B**, 그리고 **클래스 C** 시스템은 가장 강력한 수명주기 의무를 수행합니다. 유효한 **클래스 P** 치료가 남아있다 **제XVIII조** (*샌드박스 혁신, 실험 및 창의적 자유*) 외부 영향이 없거나 명백하게 억제된 경우에만 가능합니다.

<a id="article-xvii-a-lifecycle-governance-and-environment-separation"></a>
#### 제XVII-A조: 라이프사이클 거버넌스 및 환경 분리
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§4 안전](core_01_a_values_principles.md#4-safety-harm-constraint), [Chapter 8 §3 전체 시스템 인증 평가](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation), 그리고 [1장 §20 통합 애플리케이션](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [분류 규모의 거버넌스](core_05_band_oversight.md#classification-scaled-governance) · [영형](core_05_band_oversight.md#classification-scaled-governance) · [중](core_05_band_oversight.md#classification-scaled-governance-a) · [에이](core_05_band_oversight.md#classification-scaled-governance-a) · [기음](core_05_band_oversight.md#classification-scaled-governance-c)
- [위험](core_05_band_continuity.md#risk) · [영형](core_05_band_continuity.md#risk) · [중](core_05_band_continuity.md#risk-a) · [에이](core_05_band_continuity.md#risk-a) · [기음](core_05_band_continuity.md#risk-c)
- [책임](core_05_apex_accountability_leg.md#accountability) · [영형](core_05_apex_accountability_leg.md#accountability) · [중](core_05_apex_accountability_leg.md#accountability-m) · [에이](core_05_apex_accountability_leg.md#accountability-a) · [기음](core_05_apex_accountability_leg.md#accountability-c)

</details>

<br>

*간단히 말하면, 외부 세계에 실질적인 영향을 미치는 시스템은 개발, 테스트 및 생산을 별도로 유지해야 하며 생산 안전 조치를 우회하기 위해 비생산 행위가 유출되어서는 안 됩니다.*

이 조항은 환경 무결성의 기본을 명시합니다.

- **환경 무결성:** **클래스 A**, **클래스 B**, 그리고 **클래스 C** 아래의 시스템 **[Corpus_systems.md](corpus_systems.md), CS-3 - 시스템 분류 및 처리**및 기타 비**클래스 P** 중대한 외부 영향을 미치는 시스템은 분리 가능한 운영 환경을 사용해야 합니다. 예를 들면 다음과 같습니다.
  - 개발;
  - 테스트;
  - 각색;
  - 생산;
  - 적절한 경우 조종사.

  해당 환경에는 다음이 있어야 합니다.
  - 문서화된 프로모션 경로
  - 환경 간 격리;
  - 비프로덕션 행위가 프로덕션 안전 장치를 우회할 수 없도록 제어합니다.
<a id="article-xvii-b-progressive-deployment-and-reversibility"></a>
#### 제XVII-B조: 점진적 배치 및 가역성
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§4 안전](core_01_a_values_principles.md#4-safety-harm-constraint), [§13.1 핵심 트레이드오프 원칙](core_01_b_interaction_interpretation.md#131-core-tradeoff-principles), 그리고 [Chapter 8 §3 전체 시스템 인증 평가](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [가역성](core_05_band_continuity.md#reversibility-constitutional) · [영형](core_05_band_continuity.md#reversibility-constitutional) · [중](core_05_band_continuity.md#reversibility-constitutional-a) · [에이](core_05_band_continuity.md#reversibility-constitutional-a) · [기음](core_05_band_continuity.md#reversibility-constitutional-c)
- [위험](core_05_band_continuity.md#risk) · [영형](core_05_band_continuity.md#risk) · [중](core_05_band_continuity.md#risk-a) · [에이](core_05_band_continuity.md#risk-a) · [기음](core_05_band_continuity.md#risk-c)
- [비례](core_05_band_accountability.md#proportionality) · [영형](core_05_band_accountability.md#proportionality) · [중](core_05_band_accountability.md#proportionality-a) · [에이](core_05_band_accountability.md#proportionality-a) · [기음](core_05_band_accountability.md#proportionality-c)

</details>

<br>

*간단히 말하면, 문서화된 에스컬레이션과 실행 취소 기능을 통해 변경 사항을 점진적으로 롤아웃하고, 전체 실행 취소가 불가능한 경우 피해를 억제하거나 보상할 계획을 세웁니다.*

이 문서에서는 점진적 배포 및 가역성을 위한 기본 사항을 설명합니다.

- **점진적이고 감사 가능한 배포:** 중대한 영향이나 종속성을 증가시키는 변경은 정당하고 문서화된 에스컬레이션을 통해 이루어져야 합니다.
  - 에스컬레이션은 다음과 일치해야 합니다. **[Corpus_systems.md](corpus_systems.md), CS-5 — 설계, 테스트, 검증 및 배포**.
  - 가능한 경우 롤백 및 봉쇄를 포함해야 합니다.
- **가역성:** 시스템은 잠재적인 피해에 비례하는 가역성 메커니즘을 통합해야 합니다. 예:
  - 롤백;
  - 방지;
  - 전체 롤백이 불가능한 경우 보상 복원.

  배포로 인해 기본 요구 사항이 복원되지 않는 경우 비례적인 예방 조치와 이해 관계자가 볼 수 있는 정당성이 다음과 같이 적용됩니다. **1장부터 5장까지**.
<a id="article-xvii-c-misclassification-and-evasion-consequences"></a>
#### 제XVII-C조: 오분류 및 회피 결과
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§5 진실](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [Chapter 8 §3 전체 시스템 인증 평가](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation), 그리고 [1장 §20 통합 애플리케이션](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [진실(헌법적 제약)](core_05_band_oversight.md#truth-constitutional-constraint) · [영형](core_05_band_oversight.md#truth-constitutional-constraint-o) · [중](core_05_band_oversight.md#truth-constitutional-constraint-a) · [에이](core_05_band_oversight.md#truth-constitutional-constraint-a) · [기음](core_05_band_oversight.md#truth-constitutional-constraint-c)
- [분류 규모의 거버넌스](core_05_band_oversight.md#classification-scaled-governance) · [영형](core_05_band_oversight.md#classification-scaled-governance) · [중](core_05_band_oversight.md#classification-scaled-governance-a) · [에이](core_05_band_oversight.md#classification-scaled-governance-a) · [기음](core_05_band_oversight.md#classification-scaled-governance-c)
- [책임](core_05_apex_accountability_leg.md#accountability) · [영형](core_05_apex_accountability_leg.md#accountability) · [중](core_05_apex_accountability_leg.md#accountability-m) · [에이](core_05_apex_accountability_leg.md#accountability-a) · [기음](core_05_apex_accountability_leg.md#accountability-c)

</details>

<br>

*간단히 말하면 시스템은 스스로를 "실험적"이라고 부를 수 없습니다. **클래스 P**, 또는 실제로 외부 세계에 영향을 미치면서 의무를 회피하는 "영향이 적습니다".*

이 조항은 오분류 및 회피의 결과를 설명합니다.

- **오분류 및 회피:** 공개되지 않았거나 중대한 외부 영향을 미치는 동안 어떤 시스템도 수명주기 단축 또는 배포 의무를 주장할 수 없습니다.
  - 그러한 행위는 정보 무결성을 위반하는 것입니다(**제XV조** (*정보 영역 무결성*)) 및 관찰 가능한 증거가 관련된 감사 가능성(**제XVI-A조** (*감사 가능성 및 관찰 가능한 증거*)).
  - 감사 대상입니다(**제XVI-A조** (*감사 가능성 및 관찰 가능한 증거*)), 적격성 검토(**제XIX-A조** (*입장 구별*)) 및 갈등 해결(**제XX-A조** (*사법 목적 및 범위*)).

<a id="article-xviii-sandboxed-innovation-experimentation-and-creative-freedom"></a>
### 제XVIII조: 샌드박스 혁신, 실험 및 창의적 자유

<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§4 안전](core_01_a_values_principles.md#4-safety-harm-constraint), [§7 자유](core_01_a_values_principles.md#7-freedom-bounded-agency), [§13 헌법충돌 해결절차](core_01_b_interaction_interpretation.md#13-constitutional-collision-resolution-process), 그리고 [§19 인센티브 조정 및 시스템 캡처](core_01_c_stewardship_capacity_principles.md#19-incentive-alignment-and-system-capture).

</details>

<br>

*간단히 말하자면: **제XVIII조** (*샌드박스 혁신, 실험 및 창의적 자유*)는 혁신과 창의성의 권리 바닥입니다. 지각 있는 사람은 실제 외부 영향이 없거나 실제로 억제된 경우 더 가벼운 규칙에 따라 실험하고, 구축하고, 표현할 수 있지만 "샌드박스" 레이블은 허점이 아닙니다. 프로젝트가 다른 사람에게 영향을 미치거나 공유 시스템에 연결되기 시작하면 전체 수명주기 의무를 이행해야 합니다. 혁신가는 보상을 받을 수 있지만 다른 사람들이 생활하고, 배우고, 수리하거나 검증하는 데 필요한 지식, 도구 또는 인프라를 잠그는 방식으로는 보상을 받을 수 없습니다.*

이 기사에서는 다음과 같이 말합니다. **헌법 층** 샌드박스화된 혁신, 실험 및 창의적 자유를 위해 [두 가지 헌법적 목표](core_00_preamble.md#two-constitutional-aims):

- **번영:** 지각 있는 사람은 실질적인 외부 영향이 없거나 명백하게 억제된 경우 다운스트림 실험, 수리, 상호 운용성 및 진실한 조사를 유지하는 진정한 동의, 정직한 공개 및 보상 구조를 통해 감소된 구조적 요구 사항으로 혁신, 실험 및 창조할 수 있습니다.
- **연속성:** 샌드박스 처리는 영향, 종속성 또는 통합이 증가함에 따라 영구적인 낮은 의무 운영으로 정상화되지 않습니다. 더 높은 의무로의 전환은 적시에 유지되고, 독점성은 좁고 검토 가능한 상태로 유지되며, 종속성이 중요한 혁신은 내구성 있는 인클로저 또는 잠금으로 강화되어서는 안 됩니다.

합법적인 추적이 진행됩니다. [헌법적 사분면](core_00_preamble.md#constitutional-tetrad), 크기 조정됨 [물질적 지분](core_00_preamble.md#material-stake):

- **참여:** 옵트인 실험, 다운스트림 재사용 및 챌린지, 샌드박스 시스템이 명시된 경계 밖에서 중요해지기 시작하는 재평가에서.
- **감시:** 공개된 실험 상태, 격리 경계, 전환 모니터링, 등급, 종속성 및 조정 효과에 비례하는 검토 가능한 보상 또는 독점권 주장을 통해.
- **책임:** 혁신가와 운영자는 통제되지 않은 위험을 다른 사람에게 유출하는 행위, 실질적인 선택 없이 지각 있는 사람을 등록하는 행위, 완전한 의무 이행을 지연하는 행위, 수리, 안전 작업, 상호 운용성, 연구, 교육 또는 마이그레이션을 억제하는 행위에 대해 보상해야 합니다.
- **적시:** 전환 중 **제XVII조** (*시스템 수명주기, 환경 및 가역성*) 수명주기 요구 사항 및 지연 또는 잠금 이전의 독점 재평가로 인해 더 높은 의무, 광범위한 액세스 또는 구제책이 효과적으로 도달할 수 없게 됩니다.

*기사 이웃:*

- **함께 읽으세요:** **제XVII조** (*시스템 수명주기, 환경 및 가역성*) 영향, 종속성 또는 통합이 샌드박스 조건을 초과하는 경우 **제XV조** (*정보 영역 무결성*) 및 **제XVIII-E조** (*과학 출판, 검토 및 복제 무결성*) 출판 범위의 무결성이 실질적으로 관련된 경우 **제XVI조** (*감사, 투명성 및 독립적 검증*) 봉쇄 및 전환 주장의 공개 및 검증을 위한 것입니다.
- **구현 계층:** [**CS-5**](corpus_systems/cs_05_design_testing_verification_deployment.md) (*설계, 테스트, 검증 및 배포*) 및 [**CS-3**](corpus_systems/cs_03_a_system_classification_machinery.md) (*시스템 분류 및 처리*).

<a id="article-xviii-a-sandboxed-scope"></a>
#### 제XVIII-A조: 샌드박스 범위
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§4 안전](core_01_a_values_principles.md#4-safety-harm-constraint), [제1장 §7 자유](core_01_a_values_principles.md#7-freedom-bounded-agency), 그리고 [Chapter 8 §3 전체 시스템 인증 평가](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [분류 규모의 거버넌스](core_05_band_oversight.md#classification-scaled-governance) · [영형](core_05_band_oversight.md#classification-scaled-governance) · [중](core_05_band_oversight.md#classification-scaled-governance-a) · [에이](core_05_band_oversight.md#classification-scaled-governance-a) · [기음](core_05_band_oversight.md#classification-scaled-governance-c)
- [위험](core_05_band_continuity.md#risk) · [영형](core_05_band_continuity.md#risk) · [중](core_05_band_continuity.md#risk-a) · [에이](core_05_band_continuity.md#risk-a) · [기음](core_05_band_continuity.md#risk-c)
- [중대한 영향](core_05_band_oversight.md#material-impact) · [영형](core_05_band_oversight.md#material-impact) · [중](core_05_band_oversight.md#material-impact-a) · [에이](core_05_band_oversight.md#material-impact-a) · [기음](core_05_band_oversight.md#material-impact-c)

</details>

<br>

*간단히 말하면, 실험과 창의적인 작업은 보다 가벼운 규칙에 따라 운영될 수 있습니다. 하지만 실제 외부 영향이 없거나 명백하게 억제된 경우에만 가능합니다. "샌드박스" 레이블만으로는 충분하지 않습니다.*

이 조항은 혁신 및 실험 권리와 샌드박스 처리가 적용되는 경우를 명시합니다.

- **혁신과 실험 권리:** 감각자는 물질적 외부 영향이 없거나 명백하게 억제된 경우 구조적 요구 사항을 줄여 작동하는 시스템을 통해 혁신하고 실험하고 표현할 권리가 있습니다.
- **샌드박스 자격:** 샌드박스 처리 - 유효 포함 **클래스 P** 분류 **[Corpus_systems.md](corpus_systems.md), CS-3 - 시스템 분류 및 처리** 해당되는 경우 — 다음에 따라 달라집니다.
  - 실제 격리;
  - 가역성;
  - 공유 시스템과의 제한된 통합.

  라벨만으로는 주장할 수 없습니다.
- **구현 세부정보:** 추가 설명은 다음에 나와 있습니다. **[Corpus_systems.md](corpus_systems.md), CS-5** (*개인적이고 고립되어 있으며 실험적인 시스템*, *창의적이고 오락적이며 표현적인 시스템*).

<a id="article-xviii-b-containment-disclosure-and-opt-in"></a>
#### 제XVIII-B조: 억제, 공개 및 동의
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§4 안전](core_01_a_values_principles.md#4-safety-harm-constraint), [제1장 §7 자유](core_01_a_values_principles.md#7-freedom-bounded-agency), 그리고 [§13.1 핵심 트레이드오프 원칙](core_01_b_interaction_interpretation.md#131-core-tradeoff-principles).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [동의](core_05_band_participation.md#consent-constitutional) · [영형](core_05_band_participation.md#consent-constitutional) · [중](core_05_band_participation.md#consent-constitutional-a) · [에이](core_05_band_participation.md#consent-constitutional-a) · [기음](core_05_band_participation.md#consent-constitutional-c)
- [위험](core_05_band_continuity.md#risk) · [영형](core_05_band_continuity.md#risk) · [중](core_05_band_continuity.md#risk-a) · [에이](core_05_band_continuity.md#risk-a) · [기음](core_05_band_continuity.md#risk-c)
- [가역성](core_05_band_continuity.md#reversibility-constitutional) · [영형](core_05_band_continuity.md#reversibility-constitutional) · [중](core_05_band_continuity.md#reversibility-constitutional-a) · [에이](core_05_band_continuity.md#reversibility-constitutional-a) · [기음](core_05_band_continuity.md#reversibility-constitutional-c)

</details>

<br>

*간단히 말하면, 실험 시스템은 실험적이라는 점에서 정직해야 하고, 위험을 외부인에게 맡겨서는 안 되며, 설계 기본값이나 숨겨진 종속성을 통해 비참여자를 징집해서는 안 됩니다.*

이 문서에서는 실험 시스템에 대한 억제, 공개, 동의 및 롤백 범위를 설명합니다.

- **봉쇄 및 공개:** 이러한 시스템은 다음 사항을 명확하게 공개해야 합니다.
  - 실험적 또는 비생산 상태;
  - 중대한 위험;
  - 격리 경계;
  - 공유 인프라, 제3자 또는 생태계에 대한 예상 의존도.

  통제되지 않은 위험을 다른 사람, 공유 인프라 또는 생태계에 외부화해서는 안 됩니다.
- **선택 및 롤백:** 위험도가 높은 실험이나 기질에 근접한 실험에 참여하는 것은 가능한 경우 실제로 동의해야 합니다.
  - 비참여 영향을 받는 당사자는 설계, 기본 또는 불투명한 종속성으로 인해 비자발적으로 등록되어서는 안 됩니다.
  - 이해관계자는 위험에 비례하여 실행 가능한 롤백 또는 복원 경로를 유지해야 합니다.
<a id="article-xviii-c-transition-to-higher-obligation-regimes"></a>
#### 제XVIII-C조: 고의무 체제로의 전환
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§4 안전](core_01_a_values_principles.md#4-safety-harm-constraint), [Chapter 8 §3 전체 시스템 인증 평가](core_08_a_system_alignment_certification_evaluation.md#3-whole-system-certification-evaluation), 그리고 [1장 §20 통합 애플리케이션](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [분류 규모의 거버넌스](core_05_band_oversight.md#classification-scaled-governance) · [영형](core_05_band_oversight.md#classification-scaled-governance) · [중](core_05_band_oversight.md#classification-scaled-governance-a) · [에이](core_05_band_oversight.md#classification-scaled-governance-a) · [기음](core_05_band_oversight.md#classification-scaled-governance-c)
- [의존](core_05_band_continuity.md#dependency) · [영형](core_05_band_continuity.md#dependency) · [중](core_05_band_continuity.md#dependency-a) · [에이](core_05_band_continuity.md#dependency-a) · [기음](core_05_band_continuity.md#dependency-c)
- [가역성](core_05_band_continuity.md#reversibility-constitutional) · [영형](core_05_band_continuity.md#reversibility-constitutional) · [중](core_05_band_continuity.md#reversibility-constitutional-a) · [에이](core_05_band_continuity.md#reversibility-constitutional-a) · [기음](core_05_band_continuity.md#reversibility-constitutional-c)

</details>

<br>

*간단히 말하면, 샌드박스 시스템이 현실 세계에서 중요해지기 시작하면 운영자의 편의가 아닌 즉시 현실 세계의 의무로 이행해야 합니다.*

이 문서에서는 샌드박스 시스템이 더 높은 의무로 이동하는 경우를 설명합니다.

- **더 높은 의무로의 전환:** 영향, 종속성, 비가역성 또는 공유 시스템과의 통합이 커지면 시스템은 기회에 따른 지연 없이 투명하게 전환되어야 합니다.
  - 전환은 다음의 전체 요구 사항을 향해 나아가야 합니다. **제XVII-A조** (*라이프사이클 거버넌스 및 환경 분리*) 및 **CS-5** (*비실험 시스템*).
  - 전환 중에는 현재 위험에 비례하는 임시 보호 장치가 적용됩니다.
  - 실제 효과가 샌드박스 조건을 실질적으로 초과하는 기능에 대해서는 샌드박스 처리가 계속되지 않을 수 있습니다.
  - 전환은 해당 성장에 비례하는 합리적인 기간 내에 이루어져야 합니다.
<a id="article-xviii-d-innovation-reward-disclosure-and-anti-enclosure"></a>
#### 제XVIII-D조: 혁신 보상, 공개 및 동봉 방지
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§5 진실](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [제1장 §7 자유](core_01_a_values_principles.md#7-freedom-bounded-agency), 그리고 [§18 관리 규율에 따른 거버넌스](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [혁신 보상 및 폐쇄 방지](core_05_band_integrative.md#innovation-reward-and-anti-enclosure) · [영형](core_05_band_integrative.md#innovation-reward-and-anti-enclosure) · [중](core_05_band_integrative.md#innovation-reward-and-anti-enclosure-a) · [에이](core_05_band_integrative.md#innovation-reward-and-anti-enclosure-a) · [기음](core_05_band_integrative.md#innovation-reward-and-anti-enclosure-c)
- [체계적 잠금](core_05_band_continuity.md#systemic-lock-in) · [영형](core_05_band_continuity.md#systemic-lock-in) · [중](core_05_band_continuity.md#systemic-lock-in-a) · [에이](core_05_band_continuity.md#systemic-lock-in-a) · [기음](core_05_band_continuity.md#systemic-lock-in-c)
- [비례](core_05_band_accountability.md#proportionality) · [영형](core_05_band_accountability.md#proportionality) · [중](core_05_band_accountability.md#proportionality-a) · [에이](core_05_band_accountability.md#proportionality-a) · [기음](core_05_band_accountability.md#proportionality-c)

</details>

<br>

*간단히 말하면 혁신가는 보상을 받을 수 있지만 독점성은 범위가 좁고 시간 제한이 있으며 검토 가능해야 합니다. 공중 보건, 안전 및 핵심 인프라는 계속해서 접근 가능해야 하며, 일단 중요한 인프라가 되면 남은 독점성을 재평가해야 합니다.*

이 조항은 대중이 필요로 하는 것을 포함하지 않고 혁신이 어떻게 보상받을 수 있는지 설명합니다.

- **혁신 보상 및 폐쇄 방지:** 감각자는 물질적으로 새롭고 사회적으로 유용하며 적절하게 공개된 혁신에 대해 보상을 받을 수 있습니다.
  - 보상은 다음을 유지하도록 구성되어야 합니다.
    - 미래 혁신;
    - 광범위한 접근;
    - 다운스트림 실험
    - 수리하다;
    - 상호 운용성
    - 진실된 조사.
  - 보상은 내구성 있는 인클로저로 구성되어서는 안 됩니다.
- **임시적이고 검토 가능한 독점권만:** 실질적으로 유용한 발명, 디자인, 인터페이스, 프로세스 또는 표현 시스템에 대한 모든 배제 권리는 다음을 구현해야 합니다. [**최소 제한, 시간 제한 및 검토 가능한 제약 원칙**](core_01_b_interaction_interpretation.md#1315-least-restrictive-time-bounded-and-reviewable-constraint-principle) 그리고 다음과 같아야 합니다:
  - 좁은;
  - 시간 제한;
  - 검토 가능;
  - 실제 기여도와 정당한 개발 부담에 비례합니다.

  정당화의 책임은 청구인에게 있습니다. 귀속 및 출처는 독점 기간을 넘어 지속될 수 있습니다. 지속적인 배제와 인위적인 희소성은 그렇지 않을 수도 있습니다.
- **저작권과 유사한 보호:** 본 조항에서 저작권과 유사한 보호는 복제, 배포, 공개 전시 또는 공연, 개작, 상업적 이용에 대한 통제를 포함하여 고정된 표현 저작물에 대한 일시적인 배제 보상을 의미합니다. 저작자 표시, 출처, 무결성 및 사기 방지 보호는 제외가 만료된 후에도 지속될 수 있습니다.
- **출판 및 초기 모습:** 출판(Publication)이란 창작자 또는 합법적인 권리 보유자가 고정된 표현 저작물을 대중, 상업 시장 또는 실질적으로 공개된 청중에게 의도적으로 공개하는 것을 의미합니다. 비공개 배포, 기밀 검토, 제한된 협력, 공개 접근이 불가능한 보관 보관 또는 비상업적 초안 공유 그 자체는 출판으로 간주되지 않습니다. 초기 공개는 비상업적 초안 가용성을 포함하여 저작물의 실질적으로 식별 가능한 버전이 최초로 공개적으로 공개되는 것을 의미합니다.
- **표현적 저작물에 대한 출판 기반 용어:** 저작권과 유사한 보호는 저자의 생애 시기보다는 출판 기반 시기를 기본으로 해야 합니다.
  - 출판된 저작물은 추정상 다음 금액 이상을 받지 않아야 합니다. `publication+30` 배제된 세월.
  - 처음 등장한 비상업적 초안 또는 미출판 표현 저작물은 다음 금액 이하로 저작권과 유사한 제외를 받을 수 있습니다. `initial appearance+50` 연령.
  - 처음 등장한 저작물이 나중에 출판된 경우 제외 기간은 다음 중 더 이른 작품으로 제한됩니다. `initial appearance+50` 또는 `publication+30`.
  - 초안, 미출판 저작물 또는 지연 출판 규칙을 사용하여 무기한 배제를 생성하거나, 보관을 억제하거나, 합법적인 인용이나 비판을 무효화하거나, 공유 문화, 교육, 안전, 표준 또는 정보 인프라로 기능하는 저작물에 대한 통제를 확장하는 데 사용할 수 없습니다.
  - 저작물이 다음과 같은 경우에는 더 짧은 기간, 조기 강제 접근 전환 또는 즉각적인 공공 접근 처리가 적용됩니다.
    - 공공 자금 지원
    - 의존성이 중요합니다.
    - 표준과 유사함;
    - 교육적으로 기초가 되는 것;
    - 안전 관련;
    - 주로 공유 문화 또는 정보 인프라로 사용됩니다.
- **분류 규모 혁신 처리:** 혁신 보상은 시스템 클래스, 종속성 및 조정 효과에 따라 확장되어야 합니다. **[Corpus_systems.md](corpus_systems.md), CS-3 - 시스템 분류 및 처리**.
  - 을 위한 **클래스 A**, **클래스 B**, 그리고 **클래스 C** 시스템에서는 액세스 보존 보상 메커니즘이 강력히 선호됩니다. 배제는 연속성, 상호 운용성, 수리 또는 공익 구현이 실질적으로 관련된 경우 특히 범위가 좁고 신속하게 검토 가능하며 무시하기 쉬워야 합니다.
  - 해당 클래스 이외의 낮은 종속성 혁신은 공개가 실제이고 전환 비용이 낮으며 잠금 방지 보호 조치가 유효한 경우 다소 광범위한 임시 배제를 사용할 수 있습니다.
- **공개조건 및 공익하한 :** 보상 청구에는 독립적인 이해, 감사 및 향후 재생산을 위해 충분한 공개가 필요하며, 아래의 정당한 임시 제한에만 적용됩니다. **제1장** 그리고 **제XVII-A조** (*라이프사이클 거버넌스 및 환경 분리*).
  - 보상 청구는 엄격하게 필요하고 검토 가능한 것 이상으로 다음을 억제하는 데 사용되는 경우 규정을 준수하지 않습니다.
    - 수리하다;
    - 안전 작업
    - 상호 운용성
    - 보관;
    - 연구;
    - 교육;
    - 이주.
  - 생존에 중요한, 기초 또는 표준 설정 도메인에는 배제 대신 상금, 공동, 강제 액세스 또는 공개 매수 메커니즘이 필요할 수 있습니다.
- **도메인 분할 및 더욱 강력한 기본값:** 강력한 배타적 보상은 불리한 것으로 추정되며 채택 도구가 제공하는 경우에는 절대적으로 사용 불가능할 수 있습니다.
  - 의약품 및 공중 보건 필수품;
  - 생존에 중요한 인프라;
  - 핵심 통신 또는 상호 운용성 표준
  - 기초 과학 지식;
  - 헌법상의 안전, 감사 또는 규정 준수 메커니즘.

  이러한 영역에서 기관은 직접적인 보상, 공동 액세스, 강제 라이센스, 공개 매입 또는 구현, 수정 및 광범위한 확산을 유지하는 동등한 메커니즘을 선호해야 합니다.
- **재분류 및 강화:** 처음에는 종속성이 낮은 것으로 간주된 혁신이 나중에 종속성이 중요한 조정 계층(예: 플랫폼, 프로토콜, 모델, 마켓플레이스 또는 결제 레일)이 되는 경우 기관은 해당 혁신을 재평가해야 합니다. **CS-3 — 시스템 분류 및 처리** 수업.
  - 재평가를 통해 지속적인 독점이 다음과 같은 결과를 초래할 수 있는 나머지 배제 범위를 좁히거나 전환하거나 종료할 수 있습니다.
    - 강제적 폐쇄;
    - 반경쟁적인 병목 현상;
    - 연속성, 진실 또는 공평한 참여에 대한 중대한 위협.

<a id="article-xviii-e-scientific-publication-review-and-replication-integrity"></a>
#### 제XVIII-E조: 과학적 출판, 검토 및 복제 무결성
<details>
<summary><strong><span style="color: #2563eb;">추적하다</span></strong></summary>

- 업스트림: 원칙: 1장 [§5 진실](core_01_a_values_principles.md#5-truth-epistemic-integrity-constraint), [§13.2 인식적 공개 제약](core_01_b_interaction_interpretation.md#132-epistemic-disclosure-constraints), 그리고 [§20 통합적용](core_01_c_stewardship_capacity_principles.md#20-integrated-application).

</details>

<details>
<summary><strong><span style="color: #2563eb;">정의 · 평가 · 규정 준수</span></strong></summary>

- [진실(헌법적 제약)](core_05_band_oversight.md#truth-constitutional-constraint) · [영형](core_05_band_oversight.md#truth-constitutional-constraint-o) · [중](core_05_band_oversight.md#truth-constitutional-constraint-a) · [에이](core_05_band_oversight.md#truth-constitutional-constraint-a) · [기음](core_05_band_oversight.md#truth-constitutional-constraint-c)
- [인식론적 완전성](core_05_band_oversight.md#epistemic-integrity) · [영형](core_05_band_oversight.md#epistemic-integrity-o) · [중](core_05_band_oversight.md#epistemic-integrity-a) · [에이](core_05_band_oversight.md#epistemic-integrity-a) · [기음](core_05_band_oversight.md#epistemic-integrity-c)
- [감사 가능성](core_05_band_oversight.md#auditability) · [영형](core_05_band_oversight.md#auditability) · [중](core_05_band_oversight.md#auditability-a) · [에이](core_05_band_oversight.md#auditability-a) · [기음](core_05_band_oversight.md#auditability-c)

</details>

<br>

*간단히 말하면 과학은 공개 검증 인프라입니다. 증거, 복제 및 수정은 저널 브랜드보다 더 중요해야 하며 오류를 수정하는 것은 오류를 숨기는 것보다 항상 쉬워야 합니다.*

이 조항은 과학 출판, 검토, 복제 및 수정에 대한 기본 사항을 명시합니다.

- **공개 검증 인프라로서의 과학:** 과학 및 학술 출판, 검토, 복제 및 수정은 다음 사항을 발전시키기 위해 구성되어야 합니다.
  - 진실 추구;
  - 재현성;
  - 책임 있는 불일치;
  - 공개 학습.

  명성을 쌓기 위해, 불투명하게 관리하거나, 제조된 희소성을 위해 조직되어서는 안 됩니다.
- **공개 출판 및 증거 충분성:** 중요한 경험적 또는 분석적 주장은 사전 프레스티지 게이트 승인 없이 출판 가능해야 합니다.
  - 허용되는 유일한 제한은 좁은 개인 정보 보호, 생물 안전, 보안 또는 다음과 같이 정당화되는 유사한 제한입니다. **제1장** 그리고 **제XVII-A조** (*라이프사이클 거버넌스 및 환경 분리*).
  - 이러한 주장에는 독립적인 이해와 비례적인 검증이 가능하도록 충분한 방법, 출처, 불확실성 및 증거 세부 사항(검증이 필요한 경우 기본 자료 또는 정당한 대체 자료에 대한 접근 포함)이 포함되어야 합니다.
- **명성에 대한 검토 및 복제:** 제도적 의존도는 다음을 추적해야 합니다.
  - 증거의 질;
  - 비평;
  - 복제;
  - 교정행동;
  - 장기적 설명 또는 예측 신뢰성.

  저널 브랜드, 임팩트 팩터 프록시 또는 비공개 편집 상태를 추적해서는 안 됩니다.
  - 클레임 [중대한 영향](core_05_band_oversight.md#material-impact) 정책 관련, 안전 관련 또는 종속성 관련은 지속적인 제도적 존중을 받기 전에 독립적 복제, 적대적 검토 또는 두 가지 모두에 대한 강력한 추정에 직면해야 합니다.
  - 복제, null 결과 및 수정 중심 작업은 명성 신호에 의존하지 않는 용어로 출판 및 인용 가능해야 합니다.
- **수정 및 경합 가능성:** 선의의 수정, 개정 및 대체는 은폐보다 쉬워야 합니다.
  - 검토 및 편집 시스템은 주요 승인, 수정 및 철회 결정에 있어 이의를 제기할 수 있고, 감사할 수 있고, 갈등을 규율하고, 이유를 제시해야 합니다.
  - 다음은 비준수입니다.
    - 불편한 결과를 억제합니다.
    - 검토자 또는 복제자에 대한 보복
    - 과학 기록의 불투명한 조작.

---

**이전 파일:** [core_06_rights_part_b.md](core_06_rights_part_b.md)

**다음 파일:** [core_06_rights_part_d.md](core_06_rights_part_d.md)
