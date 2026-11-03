#### 3.3 Contrainte de cohérence temporelle

La certification ne peut considérer aucun des éléments suivants comme suffisant tant que des violations prévisibles à moyen ou long terme ne sont pas traitées :

- indicateurs à court terme ;
- conformité locale ; ou
- efficacité sur un horizon court.

La recherche de résultats à court terme est inacceptable si elle risque raisonnablement de compromettre ultérieurement l’un des éléments suivants, même lorsque les dommages s’accumulent lentement, apparaissent tardivement ou se propagent entre différents systèmes :

- **Sécurité** ;
- **Vérité** ; ou
- **bien-être**.

<a id="34-data-types-and-handling-evaluation"></a>

#### 3.4 Évaluation des types de données et de leur traitement

<details>
<summary><strong><span style="color: #2563eb;">Traçabilité</span></strong></summary>

- Amont :
  - [§3](#3-whole-system-certification-evaluation) (*facteurs d’évaluation globale du système*) ;
  - [CS-9.320 §4](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-4-illustrative-whole-system-application-by-system-class) (*Application illustrative de l’évaluation globale selon la classe du système*) ;
  - [Partie C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*contenu du dossier*) ;
  - [§2](#2-system-class-evaluation) (*évaluation de la classe du système*) ; famille de mesure de la Supervision (*Vérité et intégrité épistémique en tant que mesure constitutionnelle*) ;
  - [Article XV : Intégrité de la sphère informationnelle](core_06.010_rights_part_c.md#article-xv-info-sphere-integrity) ;
  - [Article XVI : Audit, transparence et vérification indépendante](core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification) ;
  - [Article VII : Propriété de soi](core_06.005_rights_part_b.md#article-vii-self-ownership).
- Aval :
  - [CS-9.320 §5](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-5-illustrative-data-handling-application-by-system-class) (*Application illustrative du traitement des données selon la classe du système*) ;
  - [§5.1](#51-ecological-footprint-evaluation) et
  - [CS-9.320 §6](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-6-illustrative-ecological-footprint-application-by-system-class) (*Application illustrative de l’empreinte écologique selon la classe du système*) ;
  - [Partie C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*intégrité du dossier*) ;
  - [Partie C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*condition d’entrée vérifiée*) ;
  - [Partie B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*reclassification et désalignement du traitement*).
- À lire avec :
  - **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Types d’information et traitement*) et [CS-6.310 — Classifications des données](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** (y compris **
  - [CS-6.305 §5.2](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Reclassification et gouvernance du cycle de vie*) et **
  - [CS-6.305 §8](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-8-system-data-types-record-governance)** (*Gouvernance du dossier des types de données système*) ;
  - [Dossier des types de données système](core_05.040_band_continuity.md#system-data-types-record) ;
  - [Divulgation de référence pour la supervision publique](core_05.050_band_oversight.md#public-oversight-baseline-disclosure) ;
  - **CJS-5.130 §18** (*modalités de conservation des données et d’intégrité du cycle de vie*),
  - **CJS-5.130 §21** (*modalités de robustesse adversariale et de résistance aux abus*), et
  - **CJS-5.130 §17** (*modalités d’interopérabilité, de portabilité et d’intégrité de sortie*) lorsque matériellement applicables ;
  - [§4.1 Invocation conjointe relative à la vie privée (informationnelle)](#41-privacy-informational-joint-invocation) lorsqu’un point de traitement de la vie privée est en jeu.
- Sous-sections :
  - [§3.4.1](#341-type-o-baseline-disclosure) (*divulgation de référence de type O*) ;
  - [§3.4.2](#342-privacy-discipline) (*discipline relative à la vie privée*) ;
  - [§3.4.3](#343-protective-storage-and-key-custody) (*stockage protecteur et garde des clés*) ;
  - [§3.4.4](#344-scheduled-data-type-re-evaluation) (*réévaluation programmée des types de données*) ;
  - [§3.4.5](#345-system-class-scaled-infrastructure-assurance) (*garanties d’infrastructure proportionnées à la classe du système*) ;
  - [§3.4.6](#346-infrastructure-robustness-for-data) (*robustesse de l’infrastructure pour les données*) ;
  - [§3.4.7](#347-defects-and-misalignment) (*défauts et désynchronisation*) ;
  - [CS-9.320 §5](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-5-illustrative-data-handling-application-by-system-class) (*Application illustrative du traitement des données selon la classe du système*).

</details>

<br>

*En termes simples : la certification doit aussi examiner les types de données que le système manipule et vérifier qu’il les traite correctement — notamment si leur classification est toujours valable au cours du cycle d’examen actuel et si l’infrastructure sous-jacente est assez robuste pour ces données et cette classe de système. Les règles relatives aux types et le Dossier des types de données système se trouvent dans le corpus des systèmes ; la certification vérifie que les règles ont réellement été appliquées et que le dossier est honnête.*

La certification de l’alignement du système doit évaluer les **types de données et leur traitement** dans chaque dossier de certification d’un système ayant un impact matériel. Cette section précise les points à vérifier. La taxonomie des types et les mécanismes de traitement figurent dans **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Types d’information et traitement*) et [CS-6.310 — Classifications des données](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**, avec :

- les définitions canoniques des types d’information ;
- les règles de traitement et exigences de séparation ;
- les détails du cycle de vie ; et
- le [Dossier des types de données système](core_05.040_band_continuity.md#system-data-types-record) durable.

**Exigence d’évaluation.** Le processus de certification doit établir si le système :

- identifie les types de données relevant matériellement de son périmètre ; et
- les traite selon la classification applicable **la plus stricte**, y compris lors de transformations, d’agrégations, de délégations, du stockage, de la conservation et de liens entre domaines.

L’évaluation doit tenir compte des effets fonctionnels, et non du seul libellé, format ou stade du pipeline.

<a id="341-type-o-baseline-disclosure"></a>
##### 3.4.1 Divulgation de référence de type O

Lorsque le **[socle de type O de CS-6.305 §7](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-7-type-o-baseline-for-class-abc-systems)** s’applique, la certification doit aussi vérifier que la [Divulgation de référence pour la supervision publique](core_05.050_band_oversight.md#public-oversight-baseline-disclosure) publiée (**type O**) couvre le **périmètre certifié**, établi à partir :

- de la [Charte de système](core_05.040_band_continuity.md#system-charter) applicable ;
- de la classe de système attribuée ; et
- des [Limites du système](core_05.040_band_continuity.md#system-boundaries) observées.

Cette couverture doit inclure les conclusions sur la gouvernance, les incitations et la contestabilité, ainsi que les rôles attribués selon [§3.1 Discipline de gouvernance, d’incitation et de contestabilité](#31-governance-incentive-and-contestability-discipline).

Pour toutes les classes de systèmes, y compris L et P, la certification doit aussi vérifier que le Dossier de certification du système est publié comme donnée de certification de **type O** au titre de [CS-6.310 partie B §9.3 Type O](corpus_systems/cs_06.310_data_classifications.md#93-type-o-open-public-oversight-baseline-disclosure-data). Cette publication n’impose pas la divulgation complète de référence pour la supervision publique aux systèmes hors des classes A, B et C.

La communication du risque évalué peut aussi contribuer à ce socle lorsque le risque systémique est en jeu. Le droit du public à l’information de référence est plus large que la certification et n’exige pas un dossier distinct à côté du [Dossier de classification du système](core_05.040_band_continuity.md#system-classification-record) ou du [Dossier des types de données système](core_05.040_band_continuity.md#system-data-types-record).

Toute rétention justifiée doit s’accompagner du meilleur substitut public raisonnablement possible ([§3.4.5 Garanties d’infrastructure proportionnées à la classe du système](#345-system-class-scaled-infrastructure-assurance) en donne des exemples). Le terme relève du chapitre cinq ; CS-6.305 (*Types d’information et traitement*) et CS-6.310 (*Classifications des données*) définissent le contenu de référence et les mécanismes de diffusion.

<a id="342-privacy-discipline"></a>
