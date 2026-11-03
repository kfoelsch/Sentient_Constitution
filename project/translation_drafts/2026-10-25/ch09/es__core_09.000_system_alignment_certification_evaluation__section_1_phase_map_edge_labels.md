<!-- AI-assisted translation draft; unreviewed. §1.2 certification-phase chart edge labels, source lines 194, 199, 200–206; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Mermaid node IDs, edge syntax, and <br/> delimiters are structural and preserved; visible edge labels are translated. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — phase-chart edge labels (es)

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
    Rec -.->|VIb, §10 —<br/>solo entradas verificadas;<br/>certificación vigente o hechos<br/>surgidos durante la certificación| S
    G --->|Sí: operar<br/>dentro del registro| Ch
    G --->|Certificado,<br/>requisitos previos pendientes| Hold
    Ch -->|Defecto material:<br/>proteger y corregir| Rm
    Ch -->|Según el calendario, o<br/>si un cambio material o<br/>un desafío creíble<br/>exige revisión| Re
    Ch -.->|VIb, §10 —<br/>solo entradas verificadas;<br/>la operación puede aportar hechos<br/>para los registros de<br/>Contribución e Infracción| S2
    Rm -->|La evidencia de corrección<br/>se verifica en la<br/>siguiente revisión| Re
    G -->|No certificado| Rm
```
