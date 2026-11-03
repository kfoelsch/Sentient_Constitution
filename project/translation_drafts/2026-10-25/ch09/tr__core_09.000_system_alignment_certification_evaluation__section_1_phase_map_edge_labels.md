<!-- AI-assisted translation draft; unreviewed. §1.2 certification-phase chart edge labels, source lines 194, 199, 200–206; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Mermaid node IDs, edge syntax, and <br/> delimiters are structural and preserved; visible edge labels are translated. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — phase-chart edge labels (tr)

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
    Rec -.->|VIb, §10 —<br/>yalnızca doğrulanmış girdiler;<br/>mevcut sertifikasyon veya sertifikasyon<br/>sırasında ortaya çıkan olgular| S
    G --->|Evet: kayıt<br/>kapsamında işlet| Ch
    G --->|Sertifikalı,<br/>önkoşullar beklemede| Hold
    Ch -->|Önemli kusur:<br/>koru ve düzelt| Rm
    Ch -->|Takvime göre ya da<br/>önemli değişiklik veya<br/>güvenilir itiraz inceleme<br/>gerektirdiğinde| Re
    Ch -.->|VIb, §10 —<br/>yalnızca doğrulanmış girdiler;<br/>işletim,<br/>Katkı ve İhlal kayıtları için<br/>olgular sağlayabilir| S2
    Rm -->|Düzeltme kanıtı<br/>sonraki inceleme<br/>döngüsünde kontrol edilir| Re
    G -->|Sertifikalandırılmadı| Rm
```
