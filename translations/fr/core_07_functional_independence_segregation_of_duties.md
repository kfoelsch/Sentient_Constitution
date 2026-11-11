<a id="chapter-seven-functional-independence-and-segregation-of-duties"></a>
# CHAPITRE SEPT : INDÉPENDANCE FONCTIONNELLE ET SÉPARATION DES TÂCHES

<details>
<summary><strong><span style="color: #2563eb;">Placement de corpus (non opératoire) : structure des fichiers et règles de lecture</span></strong></summary>

> Le contenu suivant est **conseils au lecteur uniquement**. Il n’ajoute, ne supprime ni ne restreint les obligations contraignantes ailleurs dans ce fichier ou dans d’autres chapitres.
>
> Ce fichier fait **partie de la Constitution sentiente** et ne lie qu’en combinaison avec les autres fichiers numérotés `core_*`, qui doivent être lus comme un instrument unique. Il contient le **Chapitre sept** : le seuil interprocessus en matière d’indépendance fonctionnelle et de séparation des tâches. Il suit le plancher des droits du chapitre six et précède les chapitres de procédure constitutionnelle, à commencer par [la certification de l’alignement du système du chapitre huit](../../core_09.000_system_alignment_certification_evaluation.md#chapter-nine-system-alignment-certification).
>
> - **Titulaire constitutionnel :** l’exigence minimale de sièges distincts pour les actes matériellement contraignants ; le contenu minimal universel de chaque [dossier d’acte matériellement contraignant](../../core_05.035_band_accountability.md#materially-binding-act-record) ; l’indépendance vis-à-vis de l’acteur et de sa [ligne de contrôle matériel](../../core_05.035_band_accountability.md#material-control-line) ; la publication du parcours et l’attribution des rôles ; le traitement des conflits, des vacances de siège, des remplacements et des erreurs d’attribution ; le regroupement proportionné des sièges ; les transferts attribuables ; et les conditions minimales d’indépendance que tout processus constitutionnel ultérieur doit appliquer.
> - **Source de la couche principe :** [Chapitre un §18.3](core_01_c_stewardship_capacity_principles.md#183-separation-of-duties) nécessite une gouvernance pour préserver l’indépendance fonctionnelle et achemine ici l’architecture des sièges opérationnels.
> - **Responsable de la mise en œuvre :** [CJS-5.125 §11](../../corpus_joint_structure/cjs_05.125_accountability_operations.md#constitutional-lane-and-functional-separation) (*Voie constitutionnelle et séparation fonctionnelle*), [CI-8.205 §2](../../corpus_institutions/ci_08.205_institutional_design_separation_of_powers.md#ci-8205-2-functional-separation-lanes) et [CI-16.205 §6](../../corpus_institutions/ci_16.205_appointment_competency_rotation_removal.md#ci-16205-6-seat-catalog--process-role-archetypes-and-operational-boundaries) définissent les sièges et les rendent opérationnels. Ils peuvent être plus stricts et ajouter des types de sièges à autorité spéciale délimitée ; ils ne peuvent pas restreindre ce chapitre.
> - **L’application propre à chaque processus reste du ressort des chapitres ultérieurs :** le chapitre neuf applique cette exigence à la certification d’alignement du système et à la certification d’alignement institutionnel ; [le chapitre onze §5.1](../../core_11.000_standing_assessment.md#51-separation-of-duties) l’applique aux dossiers de standing ; le chapitre quinze et [corpus_forum.md](../../corpus_forum.md) l’appliquent aux procédures du forum. Ces chapitres peuvent ajouter les garanties requises par leur sujet ; ils ne peuvent pas créer un substitut plus faible.
>
> Ordre de lecture : §1 objet, portée et limites de compétence → §2 seuil constitutionnel à quatre sièges → §3 indépendance, conflits et lignes de contrôle → §4 attribution au mauvais siège → §5 attribution publiée, vacances et remplacements → §6 adaptation proportionnée et regroupement des sièges → §7 mesures d’urgence → §8 dossiers d’acte et transferts attribuables → §9 relation avec les processus ultérieurs.

</details>

<details>
<summary><strong><span style="color: #2563eb;">Tracer</span></strong></summary>

- En amont: [Tétrade constitutionnelle](core_00_preamble.md#constitutional-tetrad) - en particulier **surveillance** et **responsabilité**; [enjeu matériel](core_00_preamble.md#material-stake); [Chapitre un §17.1 Norme de gestion partagée](core_01_c_stewardship_capacity_principles.md#171-shared-stewardship-standard); [Chapitre un §18 Gouvernance dans le cadre de la discipline d'intendance](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline); [Article XVI](core_06_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification) (*Audit, transparence et vérification indépendante*).
- Sous-sections : [§1](#1-purpose-scope-and-owner-boundary); [§2](#2-four-seat-constitutional-requirement); [§3](#3-independence-conflict-and-control-lines); [§4](#4-wrong-seat-routing); [§5](#5-published-placement-vacancy-and-substitution); [§6](#6-proportional-scaling-and-merged-hosting); [§7](#7-emergency-and-urgent-action); [§8](#8-act-records-and-attributable-handoffs); [§9](#9-relationship-to-later-processes).
- En aval: [Chapitre huit](../../core_09.000_system_alignment_certification_evaluation.md#chapter-nine-system-alignment-certification); [Chapitre neuf](../../core_10_standing_assessment.md#chapter-ten-contribution-violation-and-standing-model--measurement); [Chapitre douze](../../core_13_forum.md#chapter-thirteen-forums-and-jurisdiction); [Chapitre treize](../../core_14_governance.md#chapter-fourteen-constitutional-contract-legitimacy-authorization-and-stewardship); texte de mise en œuvre désigné mentionné ci-dessus.
- Lire avec : [Chapitre un §19.3 Détection de désalignement](core_01_c_stewardship_capacity_principles.md#193-misalignment-detection) (*détection et examen pluriels*); [Action attribuable](../../core_05.035_band_accountability.md#attributable-action); [Intégrité de l'attribution](../../core_05.035_band_accountability.md#attribution-integrity); [Auditabilité](core_05_band_oversight.md#auditability); [Contestabilité](../../core_05.035_band_accountability.md#contestability); [Proportionnalité](../../core_05.035_band_accountability.md#proportionality).

</details>

<br>

Le chapitre sept est le titulaire constitutionnel du **socle d'indépendance fonctionnelle et de séparation des tâches pour les actes matériellement contraignants**.

<a id="1-purpose-scope-and-owner-boundary"></a>
### 1. Objectif, portée et limites du titulaire

<details>
<summary><strong><span style="color: #2563eb;">Tracer</span></strong></summary>

- En amont : réclamation du titulaire désigné au début du chapitre ; [Chapitre un §18](core_01_c_stewardship_capacity_principles.md#18-governance-under-stewardship-discipline); [Surveillance](core_05_apex_oversight_leg.md#oversight-constitutional); [Responsabilité](core_05_apex_accountability_leg.md#accountability).
- En aval: [§2](#2-four-seat-constitutional-requirement) à travers [§9](#9-relationship-to-later-processes); tout processus ultérieur qui produit ou modifie un acte matériellement contraignant.
- Lire avec : [Chapitre quatre](core_04_burden_traceability_verification.md#chapter-four-burden-of-proof-traceability-and-verification) pour le substrat de vérification ; [Article XIII-A](core_06_rights_part_c.md#article-xiii-a-reliability-and-trustworthiness-baseline) (*Référence de fiabilité et de fiabilité*) et [Article XIII-B](core_06_rights_part_c.md#article-xiii-b-right-to-redress-and-remedy) (*Droit à réparation et recours*) pour contestation et réparation ; [Article XVI](core_06_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification) (*Audit, transparence et vérification indépendante*) pour les planchers de droits à vérification indépendante.

</details>

<br>

*En termes simples : avant de pouvoir faire confiance à un processus constitutionnel – ou à une décision au niveau des parties prenantes au sein d’un système, d’une institution ou d’un domaine de décision limité –, les emplois qui s’y trouvent doivent être séparés. Ce plancher s'applique à la fois au [Couche de contrat constitutionnel](core_05_band_integrative.md#constitutional-contract-layer) et à [Participation au système des parties prenantes](../../core_05.055_band_participation.md#stakeholder-status-and-weight). Un bureau sensible, un système d’IA, un organisme de parties prenantes ou un représentant cherchant un résultat ne peut pas non plus fournir le contrôle prétendument indépendant, contrôler le dossier officiel de ce contrôle ou décider de sa contestation.*

Ce chapitre s'applique à chaque [Acte matériellement contraignant](../../core_05.035_band_accountability.md#materially-binding-act), tel que le définit le chapitre cinq, notamment :

- une décision;
- une autorisation ou une certification;
- une constatation ;
- une entrée dans un dossier ou un changement de version important ;
- une version, un déploiement, une continuation ou un retrait ;
- un décaissement ou une allocation ; et
- une disposition d'un défi.

Les sièges du présent chapitre définissent qui peut faire quoi pour un acte donné ; ce ne sont pas des titres de poste. Le même sentient, bureau ou système peut occuper des sièges différents pour des actes différents. Un titre, une délégation, une capacité technique ou la capacité d’effectuer une étape n’élargit pas le siège occupé pour cet acte.

Ce chapitre indique le plancher de séparation des tâches entre les processus. Il ne déménage pas :

- charge de preuve, traçabilité ou méthode de vérification du chapitre quatre ;
- les significations canoniques du chapitre cinq ;
- Planchers de droits du chapitre six ;
- le contenu des enregistrements spécifiques au processus des chapitres huit à douze ; ou
- catalogues de sièges opérationnels, méthodes de dotation en personnel et mécanismes de plan de voie à partir du texte de mise en œuvre désigné.

<a id="2-four-seat-constitutional-requirement"></a>
### 2. Exigence constitutionnelle de quatre sièges

<details>
<summary><strong><span style="color: #2563eb;">Tracer</span></strong></summary>

- En amont: [§1](#1-purpose-scope-and-owner-boundary); [Chapitre un §18.3](core_01_c_stewardship_capacity_principles.md#183-separation-of-duties); [Chapitre un §17.1](core_01_c_stewardship_capacity_principles.md#171-shared-stewardship-standard).
- En aval: [§3](#3-independence-conflict-and-control-lines) à travers [§9](#9-relationship-to-later-processes); [CI-4.6](../../corpus_institutions/ci_16.205_appointment_competency_rotation_removal.md#ci-16205-6-seat-catalog--process-role-archetypes-and-operational-boundaries) (*Catalogue de sièges — archétypes de processus-rôle et limites opérationnelles*).
- Lire avec : [§6](#6-proportional-scaling-and-merged-hosting) pour le seul chemin d’hébergement fusionné autorisé.

</details>

<br>

*En termes simples : tout acte matériellement contraignant a quatre tâches : demander ou agir, vérifier, tenir le procès-verbal officiel et entendre la contestation. Les emplois restent distincts même lorsqu'une petite organisation est autorisée à en placer une paire autorisée dans un même bureau.*

<details>
<summary><strong><span style="color: #2563eb;">Guidage du lecteur (non opérationnel) : carte à quatre places</span></strong></summary>

> Le contenu suivant est **conseils au lecteur uniquement**. Il n’ajoute, ne supprime ou ne restreint aucune obligation contraignante ailleurs dans ce chapitre ou dans d’autres chapitres.
>
> **Lecteur de carte (non opérationnel).** Ce diagramme montre les quatre sièges et un cycle de vie typique d'un enregistrement. Il n'ajoute pas un cinquième siège de mise en œuvre, n'exige pas qu'un examen soit terminé avant chaque action, ni ne modifie les règles opérationnelles de cette section et des §§3 à 6.

</details>

<br>

```mermaid
flowchart TB
    subgraph Scope["Portée et matérialité"]
        direction LR
        A["Décision importante<br/><br/>ou acte officiel"]
        H["Mêmes règles de séparation<br/><br/>pour les intendants sensibles et IA"]
        M["Plus de préjudice potentiel, de dépendance<br/><br/>ou de portée nécessite une séparation plus forte"]
        A --> M
        H --> M
    end
    X["Le siège initiateur ne peut pas vérifier son propre acte ;<br/><br/>le vérificateur ne peut pas non plus garder le dossier<br/>ou entendre la contestation"]
    Map["Carte de rôle publiée<br/><br/>attribue des sièges pour cet acte"]
    subgraph Seats["Quatre sièges principaux"]
        direction TB
        I["Siège initiateur<br/><br/>Demander, proposer, exploiter,<br/>réclamer ou commencer l'acte"]
        V["Siège de vérification ou d’autorisation<br/><br/>Vérifier les preuves et l'autorité ;<br/>autoriser, conditionner ou refuser"]
        E["Siège de consignation<br/><br/>Inscrire, gérer les versions, conserver<br/>et publier le dossier officiel"]
        C["Siège de contestation<br/><br/>Recevoir et examiner une contestation ;<br/>corriger, limiter ou acheminer"]
        I -.->|cycle de vie typique d’un dossier| V
        V -.->|autorisation| E
        E -.-> C
        Z["                                  "]
    end
    Act["Mettre en œuvre ou appliquer<br/><br/>la décision autorisée"]
    M --> X
    X --> Map
    Map --> I
    Map --> V
    Map --> E
    Map --> C
    E -.->|portée enregistrée| Act
    C -.->|résultat confirmé ou corrigé| Act
    style A fill:none,stroke:#64748b,color:#ffffff
    style H fill:none,stroke:#0f766e,color:#ffffff
    style M fill:none,stroke:#64748b,color:#ffffff
    style X fill:none,stroke:#ea580c,color:#ffffff
    style Map fill:none,stroke:#2563eb,color:#ffffff
    style I fill:none,stroke:#64748b,color:#ffffff
    style V fill:none,stroke:#ea580c,color:#ffffff
    style E fill:none,stroke:#2563eb,color:#ffffff
    style C fill:none,stroke:#ea580c,color:#ffffff
    style Act fill:none,stroke:#9333ea,color:#ffffff
    style Z fill:none,stroke:none
```

Les flèches en pointillés à l'intérieur du groupe de sièges montrent un cycle de vie typique d’un enregistrement. Les flèches vers la mise en œuvre sont des liens de traçabilité, et non une séquence d'attente de révision obligatoire.

Chaque acte matériellement contraignant comporte quatre sièges fonctionnellement distincts. Le chapitre cinq fournit leurs significations canoniques ; cette section indique les règles de placement et d'incompatibilité entre processus :

1. **[Siège initial](../../core_05.035_band_accountability.md#initiating-seat)** — demande, propose, opère, revendique ou commence de toute autre manière l'acte.
2. **[Siège de vérification ou d’autorisation](../../core_05.035_band_accountability.md#verify-or-authorize-seat)** — vérifie les preuves et l'autorité par rapport à la norme en vigueur et vérifie, autorise, refuse ou conditionne l'acte.
3. **[Siège de consignation](../../core_05.035_band_accountability.md#record-seat)** — saisit, versions, conserve, conserve et publie le [Dossier d'acte](../../core_05.035_band_accountability.md#materially-binding-act-record) de ce que le siège de vérification ou d'autorisation a déterminé.
4. **[Siège de contestation](../../core_05.035_band_accountability.md#contest-seat)** — reçoit et examine une contestation, ordonne des corrections ou des limites lorsque cela est autorisé, et achemine tout problème hors de son autorité.

Ces sièges s’appliquent aussi bien aux intendants humains qu’aux intendants de l’IA. Si un système exécute un acte, le signe, puis utilise son propre journal comme preuve, il occupe simultanément les postes d'initiation, de vérification et d'enregistrement. L'automatisation du processus ne rend pas le contrôle indépendant.

Les combinaisons suivantes sont interdites sur un même acte :

- le siège initiateur ne doit pas vérifier ou autoriser son propre acte ;
- le siège de vérification ou d'autorisation ne doit pas détenir le siège d'enregistrement ;
- le siège de vérification ou d'autorisation ne doit pas détenir le siège de concours ; et
- l'exploitant d'un système ne doit pas vérifier ni autoriser un acte concernant ce système.

Les chapitres ultérieurs ou le texte de mise en œuvre incorporé peuvent interdire des appariements supplémentaires pour un processus particulier. Ils ne peuvent pas autoriser un appariement interdit ici.

L’exigence de séparation des fonctions s’applique à toutes les classes et se satisfait au moyen des quatre sièges. La question qui varie selon la classe est de savoir si ces sièges peuvent être fusionnés ou confiés à un même titulaire. Pour une institution ou un système opérant dans le périmètre de :

<a id="3-independence-conflict-and-control-lines"></a>
### 3. Indépendance, conflits et lignes de contrôle

<details>
<summary><strong><span style="color: #2563eb;">Tracer</span></strong></summary>

- En amont: [§2](#2-four-seat-constitutional-requirement); [Responsabilité à l'échelle de l'autorité](core_01_c_stewardship_capacity_principles.md#181-governance-as-authorized-structure); [Article XXIV](core_06_rights_part_d.md) (*Interprétation constitutionnelle, révision et garanties anti-capture*).
- En aval: [§4](#4-wrong-seat-routing); [§5](#5-published-placement-vacancy-and-substitution); [§8](#8-act-records-and-attributable-handoffs); Rôles des composants de certification du chapitre huit ; Garde des dossiers du chapitre neuf ; Chapitre douze forum anti-auto-jugement.
- Lire avec : [ligne de contrôle matériel](../../core_05.035_band_accountability.md#material-control-line); [CI-5](../../corpus_institutions/ci_08.210_conflict_integrity_anti_capture_anti_corruption.md) (*Intégrité des conflits, anti-capture et anti-corruption*) et [CF-7](../../corpus_forum/cf_15.425_integrity_safeguards_anti_capture_anti_self_judging.md) (*Garanties d'intégrité, opérations anti-capture et soutien anti-auto-jugement*) pour les conflits opérationnels et les garanties anti-auto-jugement.

</details>

<br>

*En termes simples : changer le nom inscrit sur le bureau ne crée pas l’indépendance. Une autorité de vérification ou une personne chargée de l’examen n’est pas indépendante si l’entité sentiente ou le service qui cherche à obtenir le résultat peut la diriger, la révoquer, la récompenser, la punir ou passer outre discrètement à sa décision concernant cet acte.*

L’indépendance fonctionnelle est jugée par l’autorité et le contrôle réels, et non par les étiquettes. Sur le même acte :

- le siège de vérification ou d'autorisation et le siège de concours doivent être à l'extérieur du siège initiateur [ligne de contrôle matériel](../../core_05.035_band_accountability.md#material-control-line);
- un parti dont le propre intérêt est déterminé par la loi ne doit pas détenir le siège de vérification ou d'autorisation ou de contestation ;
- un détenteur de dossier en conflit doit transmettre ce dossier, avec sa piste d'audit complète, au substitut publié plutôt que de trancher le conflit ou d'en abandonner la garde ; et
- la récusation supprime l'autorité sur l'acte; il ne transfère pas le siège au demandeur, à la ligne hiérarchique du demandeur ou à la personne la plus proche.

Retracez la [Material Control Line](../../core_05.035_band_accountability.md#material-control-line) pour l’acte concerné. Une infrastructure partagée, un soutien administratif ou l’historique des nominations n’établissent pas à eux seuls cette ligne, mais ces arrangements ne doivent pas entraver l’indépendance du jugement en pratique.

Une seconde signature, un comité de façade, une étiquette interne ou une attestation générée par un outil ne suffit pas à établir l’indépendance si l’instance censée effectuer la vérification n’a ni autorité, ni accès aux preuves, ni liberté à l’égard du contrôle matériel, ni réelle capacité de refuser et d’orienter le dossier.

<a id="4-wrong-seat-routing"></a>
### 4. Acheminement au mauvais siège

<details>
<summary><strong><span style="color: #2563eb;">Tracer</span></strong></summary>

- En amont: [§2](#2-four-seat-constitutional-requirement); [§3](#3-independence-conflict-and-control-lines).
- En aval: [§5](#5-published-placement-vacancy-and-substitution); [§8](#8-act-records-and-attributable-handoffs); [Règles de siège partagé CI-4.6](../../corpus_institutions/ci_16.205_appointment_competency_rotation_removal.md#ci-46-shared-seat-rules).
- Lire avec : [Chapitre premier §17.5 Devoir de résister](core_01_c_stewardship_capacity_principles.md#175-duty-to-resist).

</details>

<br>

*En termes simples : si une étape ne relève pas de vous, ne vous en saisissez pas en silence et ne vous retirez pas simplement. Consignez la lacune et transmettez l’affaire au bon endroit. Mieux encore, concevez le processus pour que chaque étape arrive au bon endroit sans que personne ait à remarquer le problème.*

Un commissaire invité à faire un pas hors de son siège doit :

1. refuser cette mesure sans prétendre en décider le bien-fondé ;
2. nommer le siège qui pourra l'occuper et, le cas échéant, son titulaire ou son suppléant ;
3. enregistrer la demande, le siège occupé, l'écart ou le conflit et l'itinéraire emprunté ;
 4. préserver les éléments de preuve et l’intégrité de tout dossier officiel déjà reçu ; et
5. itinéraire sans retard évitable.

Cette réponse relève de l’accomplissement du devoir, et non de l’abandon de l’acte. L’acte se poursuit par le siège approprié. Accomplir l’étape parce que le steward est le plus proche, le plus rapide, le plus ancien ou le seul à posséder les connaissances nécessaires ne remédie pas à l’absence d’un siège.

<a id="5-published-placement-vacancy-and-substitution"></a>
### 5. Placement publié, poste vacant et remplacement

<details>
<summary><strong><span style="color: #2563eb;">Tracer</span></strong></summary>

- En amont: [§2](#2-four-seat-constitutional-requirement); [§3](#3-independence-conflict-and-control-lines); [Transparence](core_05_band_oversight.md#transparency); [Auditabilité](core_05_band_oversight.md#auditability).
- En aval: [§8](#8-act-records-and-attributable-handoffs); [CI-3.2](../../corpus_institutions/ci_08.205_institutional_design_separation_of_powers.md#ci-8205-2-functional-separation-lanes) (*Voies de séparation fonctionnelle*); [CI-4.5](../../corpus_institutions/ci_16.205_appointment_competency_rotation_removal.md#ci-16205-5-authorized-roles-and-accountability-chains) (*Rôles autorisés et chaînes de responsabilité*); Enregistrements des chapitres huit et neuf.
- Lire avec : [Charte](../../core_05.040_band_continuity.md) et [Chapitre treize §5](core_12_governance.md#5-authorized-roles-competency-development-and-contribution).

</details>

<br>

*En termes simples : une organisation doit indiquer qui occupe chaque poste avant l'arrivée du cas difficile, y compris qui prend la relève lorsque le titulaire ordinaire est absent ou en conflit.*

Tout adoptant qui prend des actes matériellement contraignants doit maintenir une carte publiée, vérifiable et contestable qui identifie :

- quelle voie, bureau, rôle ou processus héberge chaque siège ;
- les actes et la portée auxquels s'applique ce placement ;
- chaque accord d'hébergement fusionné autorisé et sa garantie d'indépendance ;
- le remplaçant d'un titulaire absent, exclu, capturé ou en conflit ; et
- l'itinéraire indépendant lorsqu'aucun remplaçant qualifié n'est disponible.

Un siège non placé, vacant ou en conflit est un défaut de gouvernance à enregistrer et à corriger. Elle ne passe pas automatiquement au siège initiateur, à une partie intéressée, à un opérateur ou à un supérieur hiérarchique dans leur [ligne de contrôle matériel](../../core_05.035_band_accountability.md#material-control-line). Jusqu'à ce qu'elle soit corrigée, la loi achemine vers le chemin de substitution ou indépendant publié. Vous ne pouvez pas contourner l’exigence d’indépendance simplement parce que vous êtes pressé.

La délégation préserve les mêmes limites de siège, les mêmes devoirs de preuve, les mêmes registres et horloges, et reste soumise aux [ligne de contrôle matériel](../../core_05.035_band_accountability.md#material-control-line). Il ne crée pas de nouveau siège, ne fusionne pas les sièges et ne permet pas à un délégué de faire ce que le siège du délégué ne pourrait pas faire, notamment en convertissant une recommandation à l'échelle de la classe ou une exigence de séparation complète de quatre sièges en autorisation de fusion.

<a id="6-proportional-scaling-and-merged-hosting"></a>
### 6. Mise à l'échelle proportionnelle et hébergement fusionné

<details>
<summary><strong><span style="color: #2563eb;">Tracer</span></strong></summary>

- En amont: [§2](#2-four-seat-constitutional-requirement); [enjeu matériel](core_00_preamble.md#material-stake); [Nécessité](../../core_05.035_band_accountability.md#necessity); [Proportionnalité](../../core_05.035_band_accountability.md#proportionality).
- En aval: [Chapitre neuf §3.7](core_11_standing_assessment.md#59-informal-and-small-scope-records); [CJS-2.4](../../corpus_joint_structure/cjs_20.110_specific_joint_interlocks.md#cjs-20110-4-class-scaled-lane-staffing-and-competency-redundancy) (*Dotation en personnel des couloirs et redondance des compétences à l'échelle de la classe*); [CI-3.2](../../corpus_institutions/ci_08.205_institutional_design_separation_of_powers.md#ci-8205-2-functional-separation-lanes) (*Voies de séparation fonctionnelle*).
- Lire avec : [Fardeau évitable](../../core_05.040_band_continuity.md#avoidable-burden) et chapitre un [§3.3 Processus anti-dégradation](core_01_a_values_principles.md#33-anti-degrading-process).

</details>

<br>

*En termes simples : les petits groupes informels n’ont pas besoin de quatre grands départements. Ils ont besoin d’un véritable contrôle indépendant, d’un dossier utilisable et d’un parcours de contestation. L'échelle modifie la méthode de dotation, pas la séparation protégée.*

La force, le personnel, la redondance et la formalité de la séparation varient en fonction de l'enjeu matériel, de la classe du système, de la dépendance et des dommages raisonnablement prévisibles.

Un adoptant petit ou informel peut placer deux sièges dans un même bureau ou sensible uniquement lorsque tous les éléments suivants sont remplis :

- la fusion est nécessaire et proportionnée à son étendue ;
- il est publié, vérifiable, contestable et divulgué au procès-verbal de l'acte ;
- une garantie d'indépendance fait face aux risques créés par la fusion ;
- le siège initiateur ne vérifie ni n'autorise son propre acte ;
- la vérification et l'enregistrement et la vérification et la contestation restent interdits ; et
- une voie indépendante reste disponible lorsqu'un conflit, un préjudice matériel ou une contestation dépasse les limites légales du titulaire fusionné.

Le travail informel, non rémunéré, d'entraide, de soins, de réparation, d'enseignement, de coopération et d'intendance communautaire peut faire appel à un organisme de confiance désintéressé doté d'une autorité publiée pour le contrôle pertinent. La Constitution n’exige pas de formalité institutionnelle que la portée ne peut raisonnablement atteindre lorsqu’il existe une voie véritablement désintéressée et responsable.

Le manque de personnel, la rapidité, la commodité ou la concentration de l'expertise ne justifient pas en soi une fusion. La posture à l’échelle de la classe [§2 Plancher constitutionnel à quatre places](#2-four-seat-constitutional-requirement) régit : aucun départ n’est disponible pour la classe A, et tout départ pour la classe B ou la classe C doit répondre aux exigences ci-dessus. Plus l’enjeu matériel est élevé, plus forte est la présomption de fonctions séparées, de redondance des compétences et de remplacements indépendants.

<a id="7-emergency-and-urgent-action"></a>
### 7. Urgence et action urgente

<details>
<summary><strong><span style="color: #2563eb;">Tracer</span></strong></summary>

- En amont: [§2](#2-four-seat-constitutional-requirement); [§6](#6-proportional-scaling-and-merged-hosting); [Chapitre Douze §6.1 Mesures d'urgence et charge de continuation](../../core_15.000_forum.md#61-emergency-measures-and-continuation-burden); [posture intérimaire par défaut](core_01_b_interaction_interpretation.md#default-interim-posture).
- En aval : processus d'incident, de confinement, de libération, de continuation et d'examen post-événement dans le texte de mise en œuvre désigné.
- Lire avec : [Opportunité](core_05_apex_timeliness_leg.md#timeliness-constitutional), [Préservation des preuves](core_05_band_oversight.md#evidence-preservation), et [CI-4.6 Catalogue de sièges — archétypes de processus-rôle et limites opérationnelles](../../corpus_institutions/ci_16.205_appointment_competency_rotation_removal.md#ci-46-seat-containment).

</details>

<br>

*En clair : une urgence réelle peut justifier d’agir avant la fin du contrôle ordinaire. Cela change la séquence, et non la propriété des sièges ou la posture de séparation à l’échelle des classes. Il ne permet pas à l’acteur de certifier sa propre suite, d’effacer la trace ou de devenir ensuite le critique final.*

Lorsque le retard créerait un risque raisonnablement prévisible de préjudice grave et imminent, un siège autorisé d’initiative ou de confinement peut prendre la mesure réversible minimale nécessaire avant l’achèvement de la vérification préalable ordinaire, uniquement si :

- l’autorité d’urgence, son champ, son début, son expiration et son motif sont consignés immédiatement ou dès que cela est matériellement possible ;
- les preuves et les objections sont préservées ;
- l’avis et la participation sont rétablis dans le délai constitutionnel applicable ;
- un siège indépendant de vérification ou d’autorisation examine toute continuation au-delà de la limite immédiate ; et
- l’acte fait l’objet d’un examen indépendant après les faits.

L’action d’urgence ne :

- permet pas à l’acteur de vérifier la poursuite de sa propre action ;
- ne fait pas de l’acteur le dépositaire d’un dossier en conflit ;
- ne permet pas à l’acteur d’entendre la contestation de son propre acte ;
- ne transforme pas une nécessité temporaire en autorité permanente ;
- ne permet pas la fusion de l’un des quatre sièges dans une institution ou un système de classe A.

Aucun des éléments suivants ne constitue à lui seul une urgence :

- une date limite ;
- une cible de publication ;
- une pénurie de personnel; ou
- un souci de réputation.

<a id="8-act-records-and-attributable-handoffs"></a>
### 8. Enregistrements d'actes et transferts attribuables

<details>
<summary><strong><span style="color: #2563eb;">Tracer</span></strong></summary>

- En amont: [§2](#2-four-seat-constitutional-requirement) à travers [§7](#7-emergency-and-urgent-action); [Acte matériellement contraignant](../../core_05.035_band_accountability.md#materially-binding-act-record); [Action attribuable](../../core_05.035_band_accountability.md#attributable-action); [Intégrité de l'attribution](../../core_05.035_band_accountability.md#attribution-integrity).
- En aval: [CS-4 §10 action attribuable inspectable](../../corpus_systems/cs_16.305_critical_system_stewardship.md#cs-16305-103-inspectable-attributable-action); [Règles de siège partagé CI-4.6](../../corpus_institutions/ci_16.205_appointment_competency_rotation_removal.md#ci-46-shared-seat-rules); chaque enregistrement de processus régi par le §8 ; [`materially_binding_act_record.schema.json`](../../implementation/schemas/materially_binding_act_record.schema.json) (*formulaire de base vérifiable par machine ; support de processus, pas une deuxième définition*).
- Lire avec : [§4 Acheminement au mauvais siège](#4-wrong-seat-routing) et [Chapitre quatre §5](core_04_burden_traceability_verification.md#5-compliance-evidence-standard).

</details>

<br>

*En termes simples : chaque acte matériellement contraignant comporte un compte rendu d'acte indiquant ce qui s'est passé, qui a occupé chaque siège, ce qui a été décidé et où se déroule la contestation.*

Chaque acte matériellement contraignant doit disposer d’un [Materially Binding Act Record](../../core_05.035_band_accountability.md#materially-binding-act-record) (**Act Record**) identifiable. L’Act Record peut figurer dans un seul dossier officiel propre au processus applicable ou dans un ensemble lié de dossiers officiels attribuables et préservant l’intégrité. Aucun document en double distinct n’est requis si le dossier officiel existant ou l’ensemble lié identifie clairement tous les éléments exigés, en conserve les liens et l’historique des versions, et demeure accessible par la voie officielle autorisée.

Le dossier d’acte doit identifier, au minimum :

- une identité stable du dossier, sa version actuelle et les horodatages substantiels de création et de modification ;
- l’acte, son périmètre matériel, son statut et l’autorité qui le régit ;
- le siège initiateur, son titulaire et son autorité ;
- le siège de vérification ou d’autorisation, son titulaire, la norme applicable, la décision, les conditions ou motifs substantiels et l’heure de la décision ;
- le siège de tenue des dossiers, son titulaire, l’autorité de conservation et la version enregistrée ;
- le siège de contestation ou la voie publiée de contestation, ainsi que l’état actuel de la contestation ou de la correction ;
- chaque délégation, récusation, substitution, fusion autorisée ou dérogation d’urgence ; et
- les preuves et liens de dossier substantiels, transmissions, refus, conditions, objections non résolues, échéances, versions remplacées et corrections nécessaires pour reconstituer l’acte.

Les règles légitimes de protection de la vie privée, de confidentialité et de sécurité déterminent qui peut consulter les éléments protégés et comment ils sont partagés. Elles ne justifient jamais l’effacement de la trace officielle ni sa mise hors d’usage lorsqu’une personne chargée d’un examen et dûment autorisée en a besoin pour vérifier l’acte, le contester, le corriger ou demander réparation.

Les journaux indiquent qui a fait quoi, mais ne prouvent pas à eux seuls que l’action était valide. Un journal, une signature, une trace de modèle, une liste de contrôle ou une attestation créée par le sentient ou le système qui a effectué l’action n’a qu’un rôle limité :

- Ces éléments peuvent constituer des preuves ou être liés à l’Act Record.
- Ils ne peuvent remplacer ni un examen et une décision indépendants, ni l’Act Record officiel lui-même.

<a id="9-relationship-to-later-processes"></a>
### 9. Relation avec les processus ultérieurs

<details>
<summary><strong><span style="color: #2563eb;">Tracer</span></strong></summary>

- En amont: [§1](#1-purpose-scope-and-owner-boundary) à travers [§8](#8-act-records-and-attributable-handoffs).
- En aval: [Chapitre huit](../../core_09.000_system_alignment_certification_evaluation.md#chapter-nine-system-alignment-certification); [Chapitre neuf](../../core_10_standing_assessment.md#chapter-ten-contribution-violation-and-standing-model--measurement); [Chapitre douze](../../core_13_forum.md#chapter-thirteen-forums-and-jurisdiction); [Chapitre treize](../../core_14_governance.md#chapter-fourteen-constitutional-contract-legitimacy-authorization-and-stewardship).
- Lire avec : [Pile d'autorité et hiérarchie interne](core_05_band_integrative.md#owner-non-relocation) et le [Registre des titulaires définis dans le préambule](core_00_preamble.md#4-principles-definitions-and-rights).

</details>

<br>

*En termes simples : les chapitres suivants indiquent à chaque processus ce qu'il faut évaluer, enregistrer, décider et remédier. Ce chapitre explique à ces processus comment le pouvoir doit être séparé pendant qu'ils le font.*

Chaque processus constitutionnel ultérieur doit expliquer comment il attribue et utilise les quatre sièges et comment il suit ce chapitre. En pratique:

- Son propre enregistrement de processus peut servir d'enregistrement d'acte ou y ajouter des détails spécifiques au processus.
- Si un enregistrement de processus couvre plusieurs actes matériellement contraignants, il peut être lié à un enregistrement d'acte distinct pour chaque acte.
- Un double d’enregistrement distinct n’est pas requis lorsque le chemin d’accès officiel reste complet et traçable.
- Donner un nom différent à un processus ne le dispense pas de [§4 Acheminement au mauvais siège](#4-wrong-seat-routing) ou [§8 Enregistrements d'actes et transferts attribuables](#8-act-records-and-attributable-handoffs), y compris leurs règles de transfert et de mauvais siège.

En particulier:

- **Chapitre huit — certification d'alignement du système :** l'opérateur du système ou le promoteur de la certification est un siège initiateur et non son propre vérificateur ; Les conclusions des composants limités, l'intégration du dossier de certification, la garde et les défis doivent rester dans leurs sièges légaux et dans leurs voies anti-auto-jugement.
- **Chapitre neuf — records permanents :** le demandeur, l'autorité d'ouverture du dossier, le dépositaire du dossier et l'itinéraire du concours appliquent le plancher de quatre sièges ainsi que les règles plus strictes du chapitre neuf en matière de garde, de demandeur, de dossier informel et de non-auto-garde.
- **Chapitre douze — forums :** le dépôt, l'enquête, l'examen du fond, la conservation des dossiers, l'appel et l'examen des allégations de partialité ou d'abus de procédure d'un forum doivent préserver le siège applicable et les limites anti-auto-jugement.
- **Chapitre treize — gouvernance :** les définitions de rôles, les plans de compétences, la délégation, la succession et la conception institutionnelle doivent placer et maintenir les sièges plutôt que de simplement répéter leurs noms.

Un chapitre ultérieur peut ajouter des exigences plus strictes en matière d’indépendance, de récusation, de séparation, de garde, de comité ou d’examen si son processus présente un risque plus élevé ou différent. Il ne peut pas réduire les exigences du présent chapitre, et un siège non attribué ne revient pas à l’acteur en vertu de [§5.3 Un siège laissé vacant par la carte, ou un titulaire qui ne peut pas exercer](../../core_08.000_functional_independence_separation_of_duties.md#53-a-seat-the-map-leaves-unplaced-or-a-holder-who-cannot-serve).

---

**Fichier précédent:** [core_07.000_charters.md](core_07_charters.md)

**Fichier suivant:** [core_09.000_system_alignment_certification_evaluation.md](core_09.000_system_alignment_certification_evaluation.md#chapter-nine-part-a-certification-evaluation)
