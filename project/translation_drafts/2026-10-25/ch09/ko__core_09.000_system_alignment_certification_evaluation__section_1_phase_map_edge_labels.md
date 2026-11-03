<!-- AI-assisted translation draft; unreviewed. §1.2 certification-phase chart edge labels, source lines 194, 199, 200–206; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Mermaid node IDs, edge syntax, and <br/> delimiters are structural and preserved; visible edge labels are translated. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — phase-chart edge labels (ko)

## English source

```mermaid
    Rec -.->|VIb, §10 —<br/>verified inputs only;<br/>current certification or facts<br/>arising during certification| S
    G --->|Yes: operate<br/>within the record| Ch
    G --->|Certified,<br/>prerequisites pending| Hold
    Ch -->|Material defect:<br/>protect and correct| Rm
    Ch -->|On schedule, or<br/>material change or<br/>credible challenge<br/>requires review| Re
    Ch -.->|VIb, §10 —<br/>verified inputs only;<br/>operation may supply facts<br/>for Contribution and<br/>Violation records| S2
    Rm -->|Correction evidence<br/>is checked in the<br/>next review pass| Re
    G -->|Not Certified| Rm
```

## Translation draft

```mermaid
    Rec -.->|VIb, §10 —<br/>검증된 입력만;<br/>현재 인증 또는 인증 중<br/>발생한 사실| S
    G --->|예: 기록의<br/>범위 안에서 운영| Ch
    G --->|인증됨,<br/>선행 요건 미완료| Hold
    Ch -->|중대한 결함:<br/>보호하고 시정| Rm
    Ch -->|일정에 따라, 또는<br/>중대한 변경이나<br/>신뢰할 수 있는 이의제기로<br/>검토가 필요할 때| Re
    Ch -.->|VIb, §10 —<br/>검증된 입력만;<br/>운영 과정에서 Contribution 및<br/>Violation 기록에 필요한<br/>사실이 나올 수 있음| S2
    Rm -->|시정 증거는<br/>다음 검토 주기에서<br/>확인| Re
    G -->|인증되지 않음| Rm
```
