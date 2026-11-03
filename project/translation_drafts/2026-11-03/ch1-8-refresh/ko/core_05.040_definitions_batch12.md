# Chapter Five definition batch 12 — Clean Recertification (ko)

**Status:** AI-assisted, unreviewed, non-binding draft. Full translation of the new entry; do not synchronize.
**Source:** `core_05.040_band_continuity.md` §Clean Recertification; source SHA-256 `51164ed8a55d7d7803f9feac2b7db2e208c9124fc75bd0e1c58273250ff274ef`.

#### 무결점 재인증

<details>
<summary><strong>추적</strong></summary>

- 정식 소관: 제9장 C부 §9.3.1 두 가지 상태. 재인증, 잠정 인증, 완전 인증과 함께 읽는다. 클러스터 구성요소 없음.

</details>

*쉽게 말해 현재 불일치가 없고, 임박한 불일치를 가리키는 모니터링 지표도 없는 재인증이 무결점이다. 완전 인증 산정에는 무결점 재인증만 포함된다.*

- **What it is**
  - **In scope / out of scope / dependencies:** 범위: 현재 불일치와 임박 지표가 모두 없는 재인증. 연속된 잠정 무결점 재인증의 필수 횟수는 완전 인증의 한 입력이다. 제외: 현재 불일치를 찾아 횟수를 0으로 되돌리는 실패한 재인증; 현재 불일치는 없지만 임박 지표가 있는 재인증(실패는 아니나 무결점 아님). 재인증, 잠정·완전 인증에 의존한다. 횟수와 완전 인증 요건은 제9장 C §9.3.1에 있다. 이 항목은 제5장 의미만 정한다.
<a id="clean-recertification-a"></a>
- **How to measure and assess**
  - 연속성 측정군으로 평가: 무결점 재인증만 횟수를 늘리는가, 실패한 재인증은 횟수를 0으로 되돌리는가.
<a id="clean-recertification-c"></a>
- **What must hold**
  - **Primary failure:** 주요 실패: 불일치·결함·기한 경과 점검·회귀 시험 실패가 미해결인데 무결점으로 산정하거나, 임박 불일치 지표를 지나 횟수를 늘리는 것.
