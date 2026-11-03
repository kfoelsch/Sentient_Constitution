<!-- AI-assisted translation draft; unreviewed. §1.2 certification-phase chart edge labels, source lines 194, 199, 200–206; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Mermaid node IDs, edge syntax, and <br/> delimiters are structural and preserved; visible edge labels are translated. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — phase-chart edge labels (ja)

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
    Rec -.->|VIb, §10 —<br/>検証済み入力のみ；<br/>現行の認証または認証中に<br/>生じた事実| S
    G --->|はい：記録の<br/>範囲内で運用| Ch
    G --->|認証済み、<br/>前提条件は未完了| Hold
    Ch -->|重大な欠陥：<br/>保護して是正| Rm
    Ch -->|予定どおり、または<br/>重大な変更または<br/>信頼できる異議により<br/>審査が必要となった場合| Re
    Ch -.->|VIb, §10 —<br/>検証済み入力のみ；<br/>運用によりContribution記録と<br/>Violation記録のための<br/>事実が得られることがある| S2
    Rm -->|是正の証拠は<br/>次回の審査サイクルで<br/>確認する| Re
    G -->|未認証| Rm
```
