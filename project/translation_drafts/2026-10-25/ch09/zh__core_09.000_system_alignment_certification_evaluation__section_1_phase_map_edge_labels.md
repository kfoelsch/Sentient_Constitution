<!-- AI-assisted translation draft; unreviewed. §1.2 certification-phase chart edge labels, source lines 194, 199, 200–206; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Mermaid node IDs, edge syntax, and <br/> delimiters are structural and preserved; visible edge labels are translated. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — phase-chart edge labels (zh)

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
    Rec -.->|VIb, §10 —<br/>仅限已核验的输入；<br/>当前认证或认证期间<br/>出现的事实| S
    G --->|是：在记录<br/>范围内运行| Ch
    G --->|已认证，<br/>先决条件尚待满足| Hold
    Ch -->|重大缺陷：<br/>保护并纠正| Rm
    Ch -->|按计划进行，或在<br/>重大变化或<br/>可信挑战要求<br/>复审时| Re
    Ch -.->|VIb, §10 —<br/>仅限已核验的输入；<br/>运行过程可为贡献记录<br/>和违规记录<br/>提供事实| S2
    Rm -->|纠正证据将在<br/>下一轮审查中<br/>核验| Re
    G -->|未获认证| Rm
```
