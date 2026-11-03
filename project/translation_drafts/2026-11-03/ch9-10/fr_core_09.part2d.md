##### 3.4.2 Discipline relative à la vie privée

La certification doit soumettre le traitement des données à la discipline suivante en matière de vie privée :

- *Types H, I, N, S et Y.* Pour les données de **type H**, **I**, **N**, **S** et **Y**, la certification doit vérifier que leur traitement respecte les [références en matière de vie privée](corpus_systems/cs_06.310_data_classifications.md#privacy-link) indiquées pour chaque type dans **CS-6.305 (*Types d’information et traitement*) et CS-6.310** (*Classifications des données*), y compris la [Nécessité](core_05.035_band_accountability.md#necessity), la [Proportionnalité](core_05.035_band_accountability.md#proportionality), la minimisation et le consentement ou une autre autorisation suffisante.
- *Invocation conjointe.* Lorsque plusieurs points de traitement de la vie privée sont en jeu, [§4.1 Invocation conjointe relative à la vie privée (informationnelle)](#41-privacy-informational-joint-invocation) s’applique également.
- *Les libellés ne suffisent pas.* Une étiquette de type correcte ne démontre pas à elle seule la conformité aux règles de vie privée.
- *Types W, U et T.* Pour les œuvres de **type W**, **U** et **T**, la certification doit vérifier que le contrôle du créateur est respecté, notamment :
  - le retrait d’une diffusion publique selon [CS-6.310 partie B §9.9](corpus_systems/cs_06.310_data_classifications.md#99-type-w-works-published) (*Type W : œuvres publiées*) ;
  - les limites de chaque autorisation consignée selon [CS-6.310 partie B §9.13](corpus_systems/cs_06.310_data_classifications.md#913-commercial-grants) (*Autorisations commerciales*) ; et
  - les [droits réservés](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights) du créateur.
- *Aucun consentement implicite.* Une autorisation ne couvre que les utilisations qu’elle nomme, dans le périmètre, pour la durée, le territoire et le support qu’elle précise. Tout ce qu’elle ne nomme pas reste au créateur. La certification ne doit pas considérer un paramètre par défaut, des conditions groupées, le silence ou une autorisation plus large comme un consentement à une utilisation non mentionnée. Par exemple, une licence générale de publication ou de vente d’une œuvre ne vaut pas consentement à son utilisation comme donnée d’entraînement ; celle-ci exige un consentement spécifique du créateur (voir les [droits réservés](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights)).

<a id="343-protective-storage-and-key-custody"></a>
##### 3.4.3 Stockage protecteur et garde des clés

Pour les données des catégories à accès restreint par défaut et non accessibles, la certification doit vérifier que le système respecte les exigences minimales de stockage protecteur et de garde des clés de [CS-6.305 partie A §5.0 Catégories de posture d’accès](corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands). Le dossier doit indiquer :
- où se trouvent réellement les données restreintes et leurs clés, notamment les copies de sauvegarde, caches, journaux et espaces d’échange ;
- que le texte en clair reste limité aux processus qui en ont besoin ; et
- que les voies d’audit, d’exportation et de dérogation légale restent fonctionnelles.

Une affirmation de chiffrement sans ces preuves ne satisfait pas à cette exigence.

<a id="344-scheduled-data-type-re-evaluation"></a>
<a id="344-periodic-data-type-re-evaluation"></a>
##### 3.4.4 Réévaluation programmée des types de données

À chaque certification ou recertification d’un système ayant un impact matériel, l’examen doit vérifier que ses jeux de données importants ont été :

- **réévalués** afin de vérifier la pertinence de leur classification selon **[CS-6.305 §5.2](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Reclassification et gouvernance du cycle de vie*) et **CJS-5.130 §18** (*modalités de conservation des données et d’intégrité du cycle de vie*) ; et
- **reclassifiés** lorsque cette réévaluation l’exigeait.

La réattribution d’un type déclenchée par un événement selon CS-6.305 (*Types d’information et traitement*) et CS-6.310 (*Classifications des données*) ne remplace pas cette vérification programmée dans le cadre de la certification.

<a id="345-system-class-scaled-infrastructure-assurance"></a>
##### 3.4.5 Garanties d’infrastructure proportionnées à la classe du système

Selon [§2.2 Comment la classe du système met à l’échelle chaque évaluation](#22-how-system-class-scales-every-evaluation), CS-9.305 (*Mécanisme de classification des systèmes*) et CS-9.310 (*Classifications de l’impact des systèmes*), les systèmes de classes supérieures exigent des preuves proportionnellement plus solides que les infrastructures de traitement, de stockage, de calcul, de transmission, de sauvegarde, de reprise et de surveillance peuvent préserver, sous contrainte :

- l’intégrité de la classification ;
- l’attribution ; et
- la contestabilité.

Lorsque les règles de visibilité d’intérêt public de CS-6.305 (*Types d’information et traitement*) et CS-6.310 (*Classifications des données*) s’appliquent par défaut, la certification doit vérifier que les restrictions sont :

- étroitement délimitées ;
- documentées et auditables ; et
- accompagnées du meilleur substitut public raisonnablement possible (par exemple, un résumé, des données agrégées, une version désidentifiée, une publication différée ou un accès d’audit qualifié), afin d’expliquer ce qui est retenu au lieu de simplement le cacher.

<a id="346-infrastructure-robustness-for-data"></a>
##### 3.4.6 Robustesse de l’infrastructure pour les données

La certification doit évaluer si l’infrastructure de traitement des données est adaptée aux types de données et à la classe du système concernés. Cette infrastructure comprend :

- les couches de persistance et les pipelines ;
- les contrôles d’accès ;
- les limites de chiffrement ou d’isolation ;
- les voies de sauvegarde et de restauration ; et
- les chaînes de délégation aux opérateurs ou aux fournisseurs.

Les lacunes matérielles en matière d’intégrité du cycle de vie, de robustesse face aux attaques, de portabilité ou de récupération doivent être consignées et prises en compte dans le résultat de certification, les conditions de certification ou les limites de confiance.

<a id="347-defects-and-misalignment"></a>
##### 3.4.7 Défauts et désynchronisation

Chacun des éléments suivants doit être traité comme un défaut de certification :

- classification erronée des données ;
- restructuration visant à contourner les règles ;
- liaison non sécurisée entre domaines ;
- traitement qui porte la bonne étiquette de type, mais enfreint malgré tout les protections de vie privée exigées pour ce type ;
- absence de dossier indiquant qui a accédé aux données, les a traitées ou modifiées, empêchant ainsi l’enquête sur un préjudice important ;
- **réévaluation programmée des types de données omise ou en retard** ;
- conservation de données restreintes en texte clair ou au-delà de leur limite de traitement autorisée, ou accessibilité des clés par des processus qui n’en ont pas besoin ; et
- fragilité de l’infrastructure qui compromet de manière prévisible les protections de CS-6.305 (*Types d’information et traitement*) et CS-6.310 (*Classifications des données*).

Leurs conséquences sont définies à [§7 Résultats de certification](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes).

<a id="4-evaluations-where-implicated"></a>
