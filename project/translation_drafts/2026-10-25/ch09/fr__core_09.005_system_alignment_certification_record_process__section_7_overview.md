### 7. Résultats de certification

<details>
<summary><strong><span style="color: #2563eb;">Traçabilité</span></strong></summary>

- En amont :
  - [§6](#6-forum-process) (*procédure du forum et contestation crédible*) ;
  - [Partie A §2](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (9.000 §2) à
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*mauvaise classification, désalignement et défauts relevés lors de l’évaluation*) ;
  - [Deux objectifs constitutionnels](core_00.000_preamble.md#two-constitutional-aims) ;
  - [Chapitre trois §1](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1) et
  - [§2](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*intégrité des définitions et évasion*) ;
  - [Chapitre trois §2.1 Schémas courants d’évasion](core_03.000_definition_integrity.md#21-common-evasion-patterns) (3.000 §2.1) (*évasion du périmètre et des limites*) ;
  - [Charte du système](core_05.040_band_continuity.md#system-charter) (*désaccord entre comportement et Charte du système, et examen en retard*).
- En aval :
  - [Partie C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (*le résultat est inscrit dans le dossier*) ;
  - [Partie C §9.1](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification) (*la voie de contestation s’ouvre avec le résultat*) ;
  - [Partie C §9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) (*recertification et réouverture*) ;
  - [Partie C §10](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing) (*seuil des données vérifiées lorsque les faits étayent des constats défavorables*) ;
  - [Chapitre treize](core_14.000_forum.md#chapter-fourteen-forums-and-jurisdiction) (13.000) (*supervision des forums*) ;
  - [Chapitre dix](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) (10.000).
- À lire avec **[CS-6.305 §5](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Reclassification et gouvernance du cycle de vie*) pour la réévaluation programmée des types de données, et **[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*Exigence de reclassification*) pour les déclencheurs de réévaluation de la classe du système et la vérification SAC.
- Sous-sections :
  - [§7.1](#71-go-live-gate) (*seuil de mise en service*, avec
  - [§7.1.1 Systèmes déjà en exploitation](#711-systems-already-operating) et
  - [§7.1.2 Projets pilotes](#712-pilots)) ;
  - [§7.2](#72-certification-defects-and-correction) (*défauts de certification et correction*) ;
  - [§7.3](#73-remediation-readiness-willingness-and-capacity-to-correct) (*préparation à la correction : volonté et capacité de corriger*, avec
  - [§7.3.1 Volonté](#731-willingness),
  - [§7.3.2 Capacité](#732-capacity),
  - [§7.3.3 Étape de preuve](#733-proof-step),
  - [§7.3.4 Constats](#734-findings), et
  - [§7.3.5 Mêmes conditions pour chaque exploitant](#735-same-terms-for-every-operator)) ;
  - [§7.4](#74-denial-and-revocation) (*refus et révocation*, avec
  - [§7.4.1 Ce que sont le refus et la révocation](#741-what-denial-and-revocation-are),
  - [§7.4.2 Quand le refus ou la révocation est obligatoire](#742-when-denial-or-revocation-is-required),
  - [§7.4.3 Protection d’abord](#743-protection-first),
  - [§7.4.4 Procédure](#744-process),
  - [§7.4.5 Effet](#745-effect), et
  - [§7.4.6 Pas d’interdiction permanente](#746-not-a-permanent-bar)).

</details>

<br>

*En termes simples : chaque examen de certification s’achève par un résultat déclaré, étayé par les preuves et les préoccupations soulevées en cours de route. Aucun système n’est mis en service avant d’être certifié, avant que le résultat publié n’ait donné aux êtres sentients touchés une possibilité pratique de le contester, et avant que les protections requises pour la mise en service aient été vérifiées.*

Cette section est la **Phase IV, Décision**, après la [§6 Procédure du forum](#6-forum-process) (**Phase III, Examen**). Elle porte sur le résultat auquel parviennent les forums. La [§7.1 Seuil de mise en service](#71-go-live-gate) établit ce seuil ; la [§7.2 Défauts de certification et correction](#72-certification-defects-and-correction) indique ce qui suit la découverte d’un défaut.

Une décision de certification doit inscrire son résultat au dossier conformément à la [Partie C §8.1 Contenu minimal du dossier](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents), avec les préoccupations soulevées pour y parvenir. Le résultat est l’un des suivants :

- certification provisoire ;
- certification complète ;
- certification conditionnelle ;
- certification différée ;
- non-certification ;
- retrait ;
- expiration ; ou
- levée des conditions.

Un système qui n’a ni certification provisoire ni complète est **Non certifié**. C’est le cas lorsque la certification est :

- différée ;
- refusée ;
- retirée ; ou
- expirée.

La certification provisoire et la certification complète sont les deux **statuts** de certification. La [Partie C §9.2 Certification provisoire et complète](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) explique comment un système obtient, conserve et perd chaque statut. Les conditions d’une certification conditionnelle peuvent se rattacher à l’un ou l’autre.

<a id="71-go-live-gate"></a>
