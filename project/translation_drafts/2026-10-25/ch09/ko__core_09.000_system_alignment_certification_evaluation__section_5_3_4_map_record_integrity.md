<!-- AI-assisted translation draft; unreviewed. §5.3.4 map and record integrity, source lines 1209–1215; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §5.3.4 map and record integrity (ko)

## English source (lines 1209–1215)

Before relying on dependency maps and resource-flow records, certification must check that they meet **Article V-A** (*Dependency Mapping and Resource-Flow Transparency*). They must be:

- **Complete:** they cover significant upstream and downstream dependencies, resource flows, and any relationships that are hidden or lopsided, where those matter.
- **Current:** they are updated often enough given how fast things change and how critical the system is, including its system class under [§2 System Class Evaluation](#2-system-class-evaluation). They show the system as it runs now, not as it ran at the last certification.
- **Auditable:** they are open to audit under **Article XVI-A** (*Auditability and Observable Evidence*).

A map or record that fails any of these tests cannot support a finding that the system gives back enough. The gap must be written down and handled under *Defects and misalignment* below.

## Translation draft

##### 5.3.4 지도와 기록의 무결성

의존성 지도와 자원 흐름 기록에 의존하기 전에 인증은 이것들이 **Article V-A** (*Dependency Mapping and Resource-Flow Transparency*)를 충족하는지 확인해야 합니다. 다음 요건을 갖춰야 합니다:

- **완전성:** 중요한 상류·하류 의존성, 자원 흐름, 중요할 경우 숨겨지거나 편중된 관계를 모두 다룹니다.
- **최신성:** 변화 속도와 시스템의 중요도에 맞춰 충분히 자주 갱신하며, [§2 System Class Evaluation](#2-system-class-evaluation)-에 따른 시스템 등급도 고려합니다. 마지막 인증 당시가 아니라 현재 작동하는 모습을 보여야 합니다.
- **감사 가능성:** **Article XVI-A** (*Auditability and Observable Evidence*)에 따라 감사가 가능하도록 공개되어야 합니다.

이 요건 중 하나라도 충족하지 못한 지도나 기록은 시스템이 충분한 지원을 돌려준다는 판단을 뒷받침할 수 없습니다. 그 공백을 기록하고 아래의 *Defects and misalignment*에 따라 처리해야 합니다.
