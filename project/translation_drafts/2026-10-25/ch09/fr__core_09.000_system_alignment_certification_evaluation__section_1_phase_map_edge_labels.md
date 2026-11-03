<!-- AI-assisted translation draft; unreviewed. §1.2 certification-phase chart edge labels, source lines 194, 199, 200–206; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Mermaid node IDs, edge syntax, and <br/> delimiters are structural and preserved; visible edge labels are translated. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — phase-chart edge labels (fr)

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
    Rec -.->|VIb, §10 —<br/>entrées vérifiées uniquement ;<br/>certification en cours ou faits<br/>survenus pendant la certification| S
    G --->|Oui : exploiter<br/>dans le périmètre du dossier| Ch
    G --->|Certifié,<br/>prérequis en attente| Hold
    Ch -->|Défaut important :<br/>protéger et corriger| Rm
    Ch -->|Selon le calendrier, ou<br/>si un changement important ou<br/>une contestation crédible<br/>impose un réexamen| Re
    Ch -.->|VIb, §10 —<br/>entrées vérifiées uniquement ;<br/>l’exploitation peut fournir des faits<br/>pour les dossiers de Contribution<br/>et de Violation| S2
    Rm -->|Les preuves de correction<br/>sont vérifiées lors du<br/>prochain cycle d’examen| Re
    G -->|Non certifié| Rm
```
