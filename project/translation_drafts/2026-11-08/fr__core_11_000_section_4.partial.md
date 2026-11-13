<!-- Brouillon partiel de traduction française. Source : commit 9c2c8c10c871d91157bcd27b9f56ad6a1cec90d3. Brouillon assisté par IA ; non révisé. Couverture : chapitre onze, §4 et sous-sections 4.1–4.5 uniquement. -->

<a id="4-standing-record-operational-requirements"></a>

<a id="4-verification-and-record-requirements"></a>

### 4. Exigences de vérification et de consignation

<details>
<summary><strong><span style="color: #2563eb;">Traçabilité</span></strong></summary>

- En amont : [§2](#2-question-1--what-happened) (*registres de la Question 1 et guide des types d’événement*) ; [Chapitres deux à quatre](core_02.000_definition_structure.md) (*consignation, vérification et traçabilité des définitions jusqu’aux résultats*).
- En aval :
  - [§4.1](#41-minimum-record-contents) (*contenu minimal*) ;
  - [§4.2](#42-related-standing-record-cross-references) (*renvois croisés*) ;
  - [§5](#5-record-custody-and-opening-authority) (*garde du registre et autorité d’ouverture*) ;
  - [§6](#6-handling-a-standing-record) (*gestion d’un registre de position*) ;
  - [Chapitre douze §1](core_12.000_standing_measurement.md#1-question-2--how-good-or-bad-was-it) (*Question 2*).
- À lire avec : [CF-15.415 §8 Autorité en matière d’informations restreintes](corpus_forum/cf_15.415_routing_operations_transfer_certification_representative_treatment.md#cf-15415-8-restricted-information-authority) (*premier recours en cas de différend sur une limite de divulgation énoncée au titre de [§4.1](#41-minimum-record-contents)*).

</details>

<br>

*En termes simples : cette section précise ce que chaque registre de position doit contenir, comment les registres liés se renvoient les uns aux autres et comment ils sont versionnés. La [§5 Garde du registre et autorité d’ouverture](#5-record-custody-and-opening-authority) indique qui peut ouvrir et conserver un registre de position, ainsi que la manière de le contester ou de le corriger. Les mesures de la Question 2 ne peuvent être ajoutées qu’après consignation du fondement factuel vérifié.*

Le niveau de détail requis pour les preuves et les registres peut augmenter selon l’importance matérielle et la classe du système. Cette adaptation n’exclut aucun sentient, aucune institution ni aucun système couvert du processus de position.

<a id="41-minimum-record-contents"></a>

#### 4.1 Contenu minimal du registre

Un registre de position contient les champs ci-dessous, et les deux dernières sous-sections ajoutent des champs propres à chaque axe. Le filtre des éléments vérifiés, qui détermine ce qui peut alimenter un registre de position, est énoncé à la [§2.5 Filtre des éléments vérifiés](#25-verified-input-gate). La règle séparant les faits de la Question 1 de la mesure de la Question 2 est énoncée à la [§2.6 Limite entre étapes](#26-stage-boundary).

<a id="411-fields-every-standing-record-must-carry"></a>

##### 4.1.1 Champs obligatoires de tout registre de position

Tout registre de position doit comprendre au minimum :

- le type de registre de position — **registre de position de contribution** ou **registre de position de violation** ;
- qui ou quoi est évalué et le champ de l’évaluation, y compris les limites pertinentes du système, les limites de rôle, les communautés concernées et les relations de dépendance ;
- la conduite ou le constat évalué, notamment les actes, omissions, devoirs, effets, événement délimité, schéma compris dans le champ, registre de contribution ou constat de violation sur lequel repose le registre de position ;
- la période consignée et le statut actuel de révision — par exemple provisoire, définitif pour un objectif indiqué, contesté, remplacé ou en attente d’une réévaluation programmée ;
- tout registre de position lié auquel il est renvoyé conformément à la **section 4.2** ;
- les dossiers officiels, témoignages, mesures, audits, décisions de forum ou autres éléments de vérification qui rendent le registre de position démontrable, révisable et contestable selon les Chapitres deux à quatre ;
- l’**autorité d’ouverture du registre** qui a vérifié le fondement factuel et autorisé l’inscription, et le **dépositaire du registre** distinct qui a consigné et conserve le registre de position, chacun étant nommé conformément à la **section 5** ;
- les modalités de contestation du registre de position, notamment :
  - le forum ou l’autorité chargé de l’examiner ;
  - les limites de divulgation éventuelles ; et
  - les conditions de :
    - correction ;
    - rétablissement ;
    - expiration ; ou
    - révision programmée ;
- les champs de mesure de la Question 2 propres à chaque axe, exigés ci-dessous, une fois la mesure effectuée.

<a id="412-inspectable-attributable-action"></a>

##### 4.1.2 Action attribuable et inspectable

Les preuves d’actions attribuables se rapportent au registre de position comme suit :

- Pour le personnel ou les agents exerçant une Administration de systèmes critiques ou une autorité opérationnelle importante, [CS-16.305 §10 Action attribuable et inspectable](corpus_systems/cs_16.305_critical_system_stewardship.md#cs-16305-103-inspectable-attributable-action) définit des preuves reconstructibles d’actions attribuables comme contrat d’enregistrement par défaut pour les équipes mixtes.
- Ces preuves peuvent alimenter le présent registre de position.
- Elles ne remplacent pas le présent registre de position.
- Un registre de position ne comprend ni les poids d’un modèle d’IA (les nombres internes du modèle) ni son raisonnement privé. L’unique exception est le cas où il ne reste aucun autre moyen d’établir qui ou quoi était responsable.
- Une question ne sort pas du champ de la mesure de position simplement parce qu’elle concerne la vie privée d’une personne ou l’état interne protégé d’un système. Elle reste mesurée lorsqu’elle est pertinente pour une question de position.

<a id="413-no-privacy-or-opacity-exemption"></a>

##### 4.1.3 Aucune exception au titre de la vie privée ou de l’opacité

La vie privée, la confidentialité ou l’opacité des éléments internes d’un système ne dispense pas une question de la mesure de position. Lorsque ces considérations entrent en conflit avec l’exigence d’un registre vérifié, le conflit est résolu conformément aux [Principes fondamentaux d’arbitrage du Chapitre un §13.1](core_01.005_interaction_interpretation.md#131-core-tradeoff-principles) et à sa discipline de consignation des décisions, tout en préservant l’accès des réviseurs indépendants.

<a id="414-additional-fields-for-contribution-standing-records"></a>

##### 4.1.4 Champs supplémentaires des registres de position de contribution

Les **registres de position de contribution** doivent également indiquer :

- la mesure de contribution de la Question 2, notamment :
  - la bande principale ;
  - la case `s`, lorsqu’elle est attribuée (voir [Chapitre douze §4 Grammaire des cases et échelle commune](core_12.000_standing_measurement.md#4-slot-grammar-and-shared-scaling)) ;
  - le fondement probatoire ;
  - le raisonnement relatif à la matérialité ; et
  - toute calibration LEQU ou comparable adoptée et utilisée pour apporter un appui transparent ;
- lorsque la contribution est partagée, la répartition du crédit, en tenant compte :
  - du temps ;
  - des efforts ;
  - de la coordination ;
  - de la maintenance ;
  - de la contribution causale ; et
  - du travail de soutien moins visible ;
- la mesure de contribution consignée ici, sur laquelle doit reposer tout effet de position ultérieur au titre du Chapitre treize.

<a id="415-additional-fields-for-violation-standing-records"></a>

##### 4.1.5 Champs supplémentaires des registres de position de violation

Les **registres de position de violation** doivent également indiquer :

- la mesure de violation de la Question 2, notamment :
  - l’autorité ayant établi le constat ou le fondement du registre ;
  - l’impact LEQU ;
  - la case `s`, lorsqu’elle est attribuée (voir [Chapitre douze §4 Grammaire des cases et échelle commune](core_12.000_standing_measurement.md#4-slot-grammar-and-shared-scaling)) ;
  - le caractère du processus ou de la réponse, le cas échéant ; et
  - tout statut de désignation au titre du Chapitre quatorze ;
- lorsque plusieurs acteurs partagent ou se répartissent la responsabilité d’une violation, les motifs vérifiés de toute position défavorable consignée à l’encontre d’un acteur précis, notamment :
  - le rôle causal ;
  - le devoir ;
  - l’autorité ;
  - le contrôle ;
  - la prévisibilité ;
  - le bénéfice ;
  - la dissimulation ; ou
  - la capacité de prévention réalisable ;
- lorsque le constat de violation concerne une omission de divulgation devant un forum ou un manquement intentionnel au processus de récusation (pour les règles de mesure, lire la **§8.2.2** (*Consignation de la manière dont un préjudice a été causé*)) :
  - le fondement vérifié de l’omission ou du manquement ;
  - le devoir de divulgation ou de récusation non respecté ;
  - la connaissance, l’imprudence ou l’intention de l’acteur, lorsqu’elles ont été établies ; et
  - si la conduite a matériellement affecté :
    - la légalité du panel ;
    - l’indépendance ;
    - la contestation de la récusation ;
    - l’intégrité des preuves ;
    - le délai de réparation ;
    - l’orientation de remplacement ; ou
    - la possibilité pratique de contester ;
- la mesure de violation consignée ici, sur laquelle doit reposer tout effet de position ultérieur au titre du Chapitre treize.

<a id="42-related-standing-record-cross-references"></a>

#### 4.2 Renvois croisés entre registres de position liés

Si un registre de position de contribution et un registre de position de violation concernent le même sujet, se chevauchent dans le temps ou portent sur le même événement, schéma ou décision, chacun doit renvoyer à l’autre.

Chaque renvoi croisé doit identifier au minimum :

- le registre de position lié et s’il s’agit d’un registre de contribution ou de violation ;
- la raison du lien entre les deux registres de position, notamment lorsqu’un constat de violation réfute, corrige ou limite une contribution revendiquée conformément à la **section 2.4** ;
- leur élément commun : le sujet, l’événement, le schéma ou la décision ; et
- le chevauchement de leurs périodes ou des questions qu’ils couvrent.

Les renvois croisés :

- doivent rester auditables et contestables ;
- ne doivent pas remplacer une mesure distincte ;
- ne doivent pas créer de score fusionné ; et
- ne doivent pas laisser croire que les deux registres de position couvrent les mêmes questions ou périodes lorsque ce n’est pas le cas.

<a id="43-collective-and-actor-specific-records"></a>

#### 4.3 Registres collectifs et propres à chaque acteur

Lorsque plusieurs sentients ou entités partagent le même bénéfice ou la même violation, le système peut conserver à la fois un registre de position collectif et des registres distincts propres à chaque acteur. Les règles suivantes s’appliquent :

- Les constats de contribution et de violation doivent rester dans des registres de position distincts conformément à la **section 2.1**.
- Pour un crédit partagé, la reconnaissance devrait correspondre à la contribution réelle de chaque sentient, en tenant compte :
  - du rôle ;
  - du temps ;
  - des efforts ;
  - du risque ;
  - de la compétence ;
  - de la coordination ;
  - de la maintenance ; et
  - de l’impact causal.
- Lorsque de nombreux sentients ont apporté leur aide et que les parts individuelles ne peuvent être nettement séparées, une large répartition est privilégiée.
- En cas de violations partagées, la culpabilité ne doit pas être attribuée sur le seul fondement de l’appartenance à un groupe.
- Toute position défavorable propre à un acteur exige un lien vérifié avec :
  - le rôle causal ;
  - le devoir ;
  - l’autorité ;
  - le contrôle ;
  - la prévisibilité ;
  - le bénéfice ;
  - la dissimulation ; ou
  - la capacité de prévention réalisable.

<a id="44-versioning"></a>

#### 4.4 Gestion des versions

Les registres de position doivent être versionnés lorsque l’un des éléments suivants change :

- faits importants ;
- constats ;
- résultats de révision ;
- état des mesures correctives ;
- preuves de contribution ;
- calibration de mise en œuvre ; ou
- règles constitutionnelles.

Une version ultérieure peut :

- mettre à jour le registre de position pour l’avenir ;
- le corriger rétroactivement s’il était erroné ;
- le faire expirer pour un contexte décisionnel terminé ; ou
- le remplacer pour un nouveau contexte décisionnel.

La version ultérieure doit conserver la piste d’audit antérieure et expliquer ce qui a changé, qui a effectué le changement, sous quelle autorité d’ouverture ou de garde conformément à la **section 5**, sur la base de quels éléments de vérification et à la demande de qui.

<a id="45-implementation-tools"></a>

#### 4.5 Outils de mise en œuvre

Les équipes peuvent élaborer des outils pratiques pour les registres de position, notamment :

- champs de données ;
- balises ;
- seuils ;
- formulaires ;
- tableaux de bord ;
- étapes de révision ; et
- **mesures standard de contribution** publiées pour les tâches récurrentes conformément à la **section 13**.

Ces outils doivent rendre distincts, visibles et contestables les champs exigés par la **section 4.1**. Ils ne doivent pas dissimuler ces champs dans un score opaque ou une étiquette cachée.

