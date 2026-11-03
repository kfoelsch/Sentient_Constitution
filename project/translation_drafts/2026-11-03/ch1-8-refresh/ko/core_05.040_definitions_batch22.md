# Chapter Five definition batch 22 — Pilot (ko)

**Status:** AI-assisted, unreviewed, non-binding draft. Full translation of the new entry; do not synchronize.
**Source:** `core_05.040_band_continuity.md` §Pilot; source SHA-256 `51164ed8a55d7d7803f9feac2b7db2e208c9124fc75bd0e1c58273250ff274ef`.

#### 파일럿

<details>
<summary><strong>추적</strong></summary>

- 정식 소관: 제9장 A부 §2.3 파일럿 인증; B부 §7.1 가동 개시 관문. 후속: CS-6.345 시스템 수명주기. 가동 개시, 잠정 인증, 시스템 인증/분류 기록, 의존성, 시스템 고착, 가역성과 함께 읽는다.

</details>

*쉽게 말해 실제이지만 의도적으로 제한된 출시다. 감응 존재자가 실제 영향을 받거나 의존하기 시작하므로 샌드박스 테스트가 아니다. 범위·대상 집단·기간을 미리 정한다. 실제 운영이므로 시작 전 별도 인증이 필요하고 인증 한계를 몰래 넘을 수 없다.*

- **What it is**
  - **In scope / out of scope / dependencies:** 범위: 전체 배포 전, 자체 시스템 인증 기록에 범위·대상·기간을 미리 명시하고 실제 영향/의존이 발생하는 가동 개시. 인증은 기록된 한계만 다룬다. 한계를 넘는 운영은 중대한 확장으로 별도 가동 개시이며 사전 인증이 필요하다. 베타/시험/미리보기 등의 명칭은 기준이 아니다. 실제 영향/의존이 없는 샌드박스 테스트나 정의를 충족하지 않는 채택 단계 배포는 제외. 가동 개시와 시스템 기록에 의존한다. 평가 깊이 및 파일럿을 하지 않은 이유는 제9장 A §2.3. 이 항목은 제5장 의미만 정한다.
<a id="pilot-a"></a>
- **How to measure and assess**
  - 연속성 측정군으로 평가: 시작 전 자체 인증과 한계가 기록됐는가; 한계 내 운영하고 초과 운영은 사전 별도 인증을 받았는가; 다른 이름의 실제 운영을 인증상 파일럿/전체 배포로 취급했는가.
<a id="pilot-c"></a>
- **What must hold**
  - **Primary failure:** 주요 실패: 자체 인증 없는 테스트로 취급; 범위·대상·종료 없는 파일럿이 사실상 전체 배포; 새 인증 없이 한계 초과; 나중의 거부/조건/취소를 감응 존재자에게 비싸게 만드는 의존/고착 조성.
