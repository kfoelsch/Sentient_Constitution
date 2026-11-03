<!-- AI-assisted translation draft; unreviewed. §1.2 certification-phase chart edge labels, source lines 194, 199, 200–206; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Mermaid node IDs, edge syntax, and <br/> delimiters are structural and preserved; visible edge labels are translated. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — phase-chart edge labels (vi)

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
    Rec -.->|VIb, §10 —<br/>chỉ dùng đầu vào đã xác minh;<br/>chứng nhận hiện hành hoặc sự kiện<br/>phát sinh trong quá trình chứng nhận| S
    G --->|Có: vận hành<br/>trong phạm vi hồ sơ| Ch
    G --->|Đã chứng nhận,<br/>điều kiện tiên quyết còn chờ| Hold
    Ch -->|Khiếm khuyết trọng yếu:<br/>bảo vệ và khắc phục| Rm
    Ch -->|Theo lịch, hoặc khi<br/>thay đổi trọng yếu hay<br/>khiếu nại đáng tin<br/>đòi hỏi rà soát| Re
    Ch -.->|VIb, §10 —<br/>chỉ dùng đầu vào đã xác minh;<br/>vận hành có thể cung cấp sự kiện<br/>cho hồ sơ Đóng góp<br/>và Vi phạm| S2
    Rm -->|Bằng chứng khắc phục được<br/>kiểm tra ở đợt rà soát<br/>tiếp theo| Re
    G -->|Chưa được chứng nhận| Rm
```
