<!-- AI-assisted translation draft; unreviewed. §1.2 certification-phase chart edge labels, source lines 194, 199, 200–206; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Mermaid node IDs, edge syntax, and <br/> delimiters are structural and preserved; visible edge labels are translated. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — phase-chart edge labels (id)

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
    Rec -.->|VIb, §10 —<br/>hanya masukan terverifikasi;<br/>sertifikasi terkini atau fakta<br/>yang timbul selama sertifikasi| S
    G --->|Ya: beroperasi<br/>dalam cakupan rekaman| Ch
    G --->|Tersertifikasi,<br/>prasyarat masih tertunda| Hold
    Ch -->|Cacat material:<br/>lindungi dan perbaiki| Rm
    Ch -->|Sesuai jadwal, atau<br/>jika perubahan material atau<br/>tantangan kredibel<br/>memerlukan peninjauan| Re
    Ch -.->|VIb, §10 —<br/>hanya masukan terverifikasi;<br/>operasi dapat menyediakan fakta<br/>untuk rekaman Kontribusi<br/>dan Pelanggaran| S2
    Rm -->|Bukti koreksi diperiksa<br/>pada siklus peninjauan<br/>berikutnya| Re
    G -->|Tidak Bersertifikat| Rm
```
