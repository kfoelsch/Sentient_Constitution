<!-- Locale: fr | Source: origin/main current working copy | AI-drafted, unreviewed | Traduction complète du §9.3 actuel; le texte anglais prévaut. -->

<a id="93-provisional-and-full-certification"></a>

#### 9.3 Certification provisoire et complète

*En termes simples : un système gagne la confiance par étapes. Les nouveaux systèmes et ceux qui ont échoué à une évaluation commencent sous certification provisoire, avec un intervalle court et des contrôles fréquents. Seul un système sans problème actuel ni signe de problème imminent accède à la certification complète et à un intervalle plus long. Un échec à l’évaluation le ramène au régime provisoire.*

<a id="931-the-two-statuses"></a>

##### 9.3.1 Les deux statuts

La certification prend l’un de deux statuts. Chacun a son propre intervalle, inscrit au Dossier de certification du système conformément à [§8.1 Contenu minimal du dossier](#81-minimum-record-contents) :

- **[Certification provisoire](core_05.040_band_continuity.md#provisional-certification)** :
  - première certification d’un système, y compris un système nouvellement déployé ; ou
  - certification d’un système après l’échec d’une recertification, ou après un examen rouvert ou nouveau ayant constaté un désalignement.

  L’intervalle provisoire est plus court que l’intervalle complet pour la même classe de système. Les limites de dépendance figurent au Dossier de certification du système.
- **[Certification complète](core_05.040_band_continuity.md#full-certification)** ne peut être acquise que lors de la recertification d’un système provisoirement certifié, et seulement si les trois conditions suivantes sont réunies :
  1. le système a accompli le nombre requis de recertifications provisoires propres consécutives : au moins une, et davantage pour les classes supérieures, selon le document adopté ;
  2. aucun désalignement n’est actuel : le Dossier ne montre aucun désalignement ouvert, défaut non corrigé, contrôle en retard ni test de régression échoué ; et
  3. aucun indicateur de surveillance ne signale un désalignement imminent : les déclencheurs et mesures de tendance du Dossier ne montrent aucun seuil franchi ni aucune tendance vers un seuil.

La certification complète suit l’intervalle adapté à la classe du système. Elle reste limitée dans le temps et ne constitue pas une approbation permanente.

Une recertification est **propre** lorsqu’elle satisfait aux conditions 2 et 3.

<details>
<summary><strong>Guide de lecture (sans effet opératoire) : statut de certification</strong></summary>

> Ce tableau résume le §9.3. En cas de différence, le texte prévaut.
>
> | | Certification provisoire | Certification complète |
> |---|---|---|
> | **Qui la détient** | Première certification, système nouvellement déployé, ou système certifié après un échec ou un examen rouvert/nouveau constatant un désalignement | Système qui l’a acquise lors d’une recertification alors qu’il était provisoirement certifié |
> | **Comment l’obtenir** | Accordée avec une décision de certification | Nombre requis de recertifications provisoires propres consécutives (au moins une), aucun désalignement actuel et aucun indicateur d’imminence |
> | **Intervalle** | Intervalle provisoire, plus court que l’intervalle complet de la même classe | Intervalle adapté à la classe ; reste limité dans le temps |
> | **En cas d’échec d’une recertification** | Conséquences de la Partie B §7 ; prochaine certification provisoire et compteur remis à zéro | Conséquences de la Partie B §7 ; prochaine certification provisoire et compteur remis à zéro |
> | **Si un indicateur d’imminence apparaît** | Reste provisoire ; le compteur n’avance pas | Redescend au statut provisoire |

</details>

<a id="932-failure-and-step-down"></a>

##### 9.3.2 Échec et déclassement

Les résultats d’une recertification, d’un examen rouvert ou d’un nouvel examen déterminent le statut du système :

- Une recertification constatant un désalignement actuel est une recertification **échouée**. Les conséquences de [Partie B §7 Résultats de certification](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) s’appliquent. La prochaine certification accessible est provisoire, même si le contrôle suivant est propre ; le compteur de recertifications propres repart de zéro.
- Si aucun désalignement actuel n’est constaté mais qu’un indicateur de désalignement imminent apparaît, la recertification n’est ni échouée ni propre. Le système provisoire le reste et son compteur n’avance pas ; le système complet redescend au provisoire.
- Un examen rouvert au titre de [§9 Recertification et réouverture](#9-recertification-and-reopening) qui constate un désalignement produit le même effet qu’une recertification échouée.
- Un nouvel examen d’un système certifié qui constate un désalignement actuel produit le même effet. Si le système n’a aucun statut de certification, les règles de [Partie B §7.4 Refus et révocation](core_09.005_system_alignment_certification_record_process.md#74-denial-and-revocation) s’appliquent.

<a id="933-cause-of-misalignment"></a>

##### 9.3.3 Cause du désalignement

Tout désalignement constaté lors d’une évaluation, d’une recertification, d’un examen rouvert ou nouveau est attribué dans le Dossier à l’une de ces causes :

- **cause de conception :** le système ou son processus est construit de façon à produire des résultats désalignés même lorsqu’il est utilisé comme prévu ;
- **cause d’exploitation :** la conception paraît correcte, mais la façon d’exploiter, d’alimenter ou d’entretenir le système rend ses résultats désalignés ; ou
- **cause non encore déterminée :** les remèdes de conception et d’exploitation restent tous deux ouverts jusqu’à ce que le forum établisse la cause.

Cette attribution est limitée comme suit :

- Si le système continue de produire des résultats désalignés, il est désaligné, même si sa conception paraît correcte sur le papier. Cette apparence ne constitue pas une défense.
- Une conception qui produirait des résultats désalignés constitue un désalignement avant même qu’un tel résultat apparaisse.
- L’attribution de la cause détermine le remède recherché et le périmètre d’un examen rouvert ; elle ne décide jamais si le système est désaligné.

En cas de cause de conception :

- le compteur de recertifications propres reste à zéro jusqu’à ce que la nouvelle conception soit en place et vérifiée ;
- le forum qui a établi la cause, ou le prochain forum désigné selon la [Partie B §6.2 Séquence de supervision](core_09.005_system_alignment_certification_record_process.md#62-supervisory-sequence), vérifie la nouvelle conception dans le [délai d’admission correspondant](core_05.040_band_continuity.md#tier-window), éventuellement dès la première recertification provisoire ;
- une **évaluation de composant** effectuée avant cette vérification (la part d’un composant dans une étape de certification, définie à la [Partie B §6.1 Supervision du forum et rôles des composants](core_09.005_system_alignment_certification_record_process.md#61-forum-supervision-and-component-roles)) ne compte pas dans le total propre, même si elle est propre ; et
- modifier la manière d’exploiter le système ne satisfait pas cette étape.

Ces règles s’ajoutent aux règles de déclassement ci-dessus et ne les remplacent pas. L’opérateur ou tout être sentient touché peut demander au forum de réexaminer l’attribution de la cause. Si la cause change, ces règles cessent de s’appliquer.

<a id="934-tier-windows"></a>

##### 9.3.4 Délais par niveau

Lorsqu’une évaluation initiale, une recertification, un examen rouvert ou un nouvel examen constate un désalignement :

- l’affaire est classée selon les niveaux de matérialité du [Chapitre quinze §6 Résolution en temps utile, niveaux de matérialité et discipline anti-retard](core_15.000_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline) ;
- elle est présumée relever du niveau correspondant à la classe du système (par exemple, un système de classe A désaligné relève en principe du niveau A) ;
- la réception, la préservation des preuves, la protection provisoire et la décision suivent les délais et limites maximales de ce niveau ; et
- tout dépassement est examiné comme l’exige cette section.

<a id="935-class-a-reliance"></a>

##### 9.3.5 Dépendance de classe A

Par rapport à la certification complète, la certification provisoire a un intervalle plus court, donc la recertification arrive plus tôt ([§9.3.1 Les deux statuts](#931-the-two-statuses)), et le Dossier fixe des limites de dépendance ([§8.1 Contenu minimal du dossier](#81-minimum-record-contents)). Si l’interruption d’un système couperait des nécessités de survie avant l’arrivée de solutions de remplacement :

- la certification provisoire n’impose pas, à elle seule, l’interruption du système ;
- les protections provisoires et conditions de certification de la [Partie B §7 Résultats de certification](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) traitent ce cas ;
- la même règle s’applique lorsque le compteur est suspendu après un constat de désalignement de conception : cette suspension n’interrompt jamais à elle seule un système dont dépendent des êtres sentients ; et
- tant que la suspension dure, le forum précise la protection provisoire, les conditions de certification de la dépendance et l’avis aux personnes dépendantes.

<a id="936-verification-not-assertion"></a>

##### 9.3.6 Vérification, pas affirmation

Le statut du système, le nombre de recertifications propres et les indicateurs de surveillance doivent être vérifiés, et cette vérification doit pouvoir faire l’objet d’un examen indépendant. L’affirmation du système ne suffit pas :

- les indicateurs ne peuvent être choisis ou définis de façon à empêcher toute détection d’un désalignement ;
- une nouvelle conception est vérifiée de la même manière, à partir de preuves contrôlables par d’autres ;
- la certification complète n’écarte aucun motif de réouverture : tous les déclencheurs de [§9 Recertification et réouverture](#9-recertification-and-reopening) restent applicables ; et
- l’évasion est traitée conformément à [§9.4 Non-évasion](#94-non-evasion).
