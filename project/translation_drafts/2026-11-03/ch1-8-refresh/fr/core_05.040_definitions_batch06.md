# Chapitre cinq, Continuité — lot de définitions 6 (fr)

**Statut :** brouillon de traduction assistée par IA, non révisé, non synchronisé et non certifié. Le texte anglais numéroté fait autorité.
**Source :** `core_05.040_band_continuity.md`, entrées Reopened Review, Reopening Trigger et Tier Window, texte source actuel.

## Examen rouvert

<details><summary><strong>Traçabilité</strong></summary>

- Propriétaire canonique : [Chapitre neuf, partie C §9.2 Déclencheurs de réouverture](core_09.010_system_alignment_certification_record_recertification.md#92-reopening-triggers), à lire avec [§9 Recertification et réouverture](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening).
- Composante de cluster : aucune. À lire avec Passage de certification, Déclencheur de réouverture et Registre de certification du Système.

</details>

*En termes simples : un **examen rouvert** est un passage de certification concernant un Système ou une Institution déjà doté d’un registre. Il commence avant la prochaine recertification programmée lorsqu’un [Déclencheur de réouverture](core_05.040_band_continuity.md#reopening-trigger) est survenu et ouvre un nouveau registre lié au précédent.*

- **Définition**
  - **Champ d’application :** [Passage de certification](core_05.040_band_continuity.md#certification-pass) engagé avant la prochaine recertification programmée lorsqu’un Déclencheur de réouverture matériel s’est produit. Il suit la même procédure devant l’instance et se termine par un résultat.
  - **Hors champ :** une [Recertification](core_05.040_band_continuity.md#recertification), qui suit le calendrier ; ou un [Nouvel examen](core_05.040_band_continuity.md#fresh-review), ordonné par l’instance en réponse à un défaut de certification et énuméré à côté de la réouverture au chapitre neuf.
  - **Dépend de :** Passage de certification ; Déclencheur de réouverture ; Registre de certification du Système. Les déclencheurs et le nouveau registre sont définis au [chapitre neuf, partie C §§9.2 et 9](core_09.010_system_alignment_certification_record_recertification.md#92-reopening-triggers). La présente entrée définit uniquement le sens propre au chapitre cinq.
<a id="reopened-review-a"></a>
- **Mesure et évaluation :** vérifier que l’examen rouvert ouvre un nouveau registre lié au registre achevé ; et qu’il est ouvert lorsqu’un déclencheur matériel survient, sans attendre la prochaine recertification programmée.
<a id="reopened-review-c"></a>
- **Échec principal :** retarder un examen rouvert alors qu’un déclencheur est matériel ; ou remplacer l’examen rouvert par une recertification programmée après la survenance d’un déclencheur.

## Déclencheur de réouverture

<details><summary><strong>Traçabilité</strong></summary>

- Propriétaire canonique : [Chapitre neuf, partie C §9.2 Déclencheurs de réouverture](core_09.010_system_alignment_certification_record_recertification.md#92-reopening-triggers), à lire avec [chapitre dix §9.2](core_10.000_institutional_alignment_certification.md#92-reopening-triggers) pour une Institution.
- Composante de cluster : aucune. À lire avec Examen rouvert et Registre de certification du Système.

</details>

*En termes simples : un **déclencheur de réouverture** est un changement matériel ou un signalement qui justifie la réouverture d’une certification avant la date prévue. Les déclencheurs sont indiqués dans le registre.*

- **Définition**
  - **Champ d’application :** changement matériel ou signalement d’un type énuméré au [chapitre neuf, partie C §9.2](core_09.010_system_alignment_certification_record_recertification.md#92-reopening-triggers) (et, pour une Institution, au [chapitre dix §9.2](core_10.000_institutional_alignment_certification.md#92-reopening-triggers)) : changement du Système ou de son contexte ; observation ou signalement ; défaut d’alignement de classification ou de type de données ; question touchant la Charte du Système ou la gouvernance de l’opérateur ; ou défaut d’alignement constaté lors d’une évaluation. Seul un déclencheur matériel rouvre l’examen. Une [Violation de gouvernance](core_05.040_band_continuity.md#governance-violation) en est un exemple.
  - **Hors champ :** la date prévue de recertification, qui n’est pas un déclencheur.
  - **Dépend de :** Examen rouvert ; Registre de certification du Système. Les déclencheurs sont définis au [chapitre neuf, partie C §9.2](core_09.010_system_alignment_certification_record_recertification.md#92-reopening-triggers). La présente entrée définit uniquement le sens propre au chapitre cinq.
<a id="reopening-trigger-a"></a>
- **Mesure et évaluation :** vérifier que le registre énonce les déclencheurs de réouverture et qu’un déclencheur matériel entraîne un Examen rouvert.
<a id="reopening-trigger-c"></a>
- **Échec principal :** registre qui n’énonce aucun déclencheur de réouverture ; ou déclencheur matériel ignoré au motif que la prochaine recertification est proche.

## Fenêtre de niveau

<details><summary><strong>Traçabilité</strong></summary>

- Propriétaire canonique : [Chapitre neuf, partie C §9.3.4 Fenêtres de niveau](core_09.010_system_alignment_certification_record_recertification.md#934-tier-windows), à lire avec [chapitre quatorze §6 Résolution rapide, niveaux de matérialité et discipline anti-retard](core_14.000_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline).
- Composante de cluster : aucune. À lire avec Passage de certification et Protection provisoire.

</details>

*En termes simples : une **fenêtre de niveau** est un délai applicable à une étape d’une affaire de certification, fixé par le niveau de matérialité attribué. Le niveau correspond en principe à la classe. L’objectif de réception propre à ce niveau est l’**objectif de réception correspondant**.*

- **Définition**
  - **Champ d’application :** délais et bornes maximales du niveau de matérialité attribué à une affaire de certification. Le niveau correspond en principe à la classe du Système ou de l’Institution. L’objectif de réception du niveau est l’objectif correspondant.
  - **Hors champ :** délai de préavis avant mise en service, qui dépend de la classe et des besoins des sentients concernés ; intervalle de certification, qui fixe la fréquence de renouvellement ; ou objectifs et bornes du chapitre quatorze, qui ont leur propre définition.
  - **Dépend de :** Passage de certification ; Protection provisoire. L’utilisation des fenêtres de niveau figure au [chapitre neuf, partie C §9.3.4](core_09.010_system_alignment_certification_record_recertification.md#934-tier-windows) ; niveaux, objectifs et bornes sont définis au [chapitre quatorze §6](core_14.000_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline). La présente entrée définit uniquement le sens propre au chapitre cinq.
<a id="tier-window-a"></a>
- **Mesure et évaluation :** vérifier que l’affaire de certification est attribuée au niveau correspondant à la classe et que tout dépassement fait l’objet de l’examen prévu au chapitre quatorze.
<a id="tier-window-c"></a>
- **Échec principal :** automatisation ou filtre qui prolonge une fenêtre de niveau ou un objectif de réception ; ou dépassement qui n’est pas examiné comme l’exige le chapitre quatorze.
