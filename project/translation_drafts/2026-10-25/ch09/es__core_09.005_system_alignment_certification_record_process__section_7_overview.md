### 7. Resultados de certificación

<details>
<summary><strong><span style="color: #2563eb;">Trazabilidad</span></strong></summary>

- Antecedentes:
  - [§6](#6-forum-process) (*proceso del foro e impugnación creíble*);
  - [Parte A §2](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (9.000 §2) hasta
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*clasificación errónea, desalineación y defectos detectados en la evaluación*);
  - [Dos fines constitucionales](core_00.000_preamble.md#two-constitutional-aims);
  - [Capítulo Tres §1](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1) y
  - [§2](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*integridad de definiciones y evasión*);
  - [Capítulo Tres §2.1 Patrones comunes de evasión](core_03.000_definition_integrity.md#21-common-evasion-patterns) (3.000 §2.1) (*evasión del alcance y los límites*);
  - [Carta del sistema](core_05.040_band_continuity.md#system-charter) (*desajuste entre la conducta y la Carta del sistema, y revisión atrasada*).
- Derivaciones:
  - [Parte C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (*el resultado se consigna en el registro*);
  - [Parte C §9.1](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification) (*la vía de impugnación se abre con el resultado*);
  - [Parte C §9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) (*recertificación y reapertura*);
  - [Parte C §10](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing) (*barrera de entradas verificadas cuando los hechos respaldan hallazgos adversos*);
  - [Capítulo Trece](core_14.000_forum.md#chapter-fourteen-forums-and-jurisdiction) (13.000) (*supervisión de foros*);
  - [Capítulo Diez](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) (10.000).
- Léase junto con **[CS-6.305 §5](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Reclasificación y gobernanza del ciclo de vida*) para la reevaluación programada del tipo de datos y **[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*Requisito de reclasificación*) para los activadores de reevaluación de la clase del sistema y la verificación de SAC.
- Subsecciones:
  - [§7.1](#71-go-live-gate) (*barrera de puesta en marcha*, con
  - [§7.1.1 Sistemas ya en operación](#711-systems-already-operating) y
  - [§7.1.2 Pilotos](#712-pilots));
  - [§7.2](#72-certification-defects-and-correction) (*defectos de certificación y corrección*);
  - [§7.3](#73-remediation-readiness-willingness-and-capacity-to-correct) (*preparación para remediar: voluntad y capacidad de corregir*, con
  - [§7.3.1 Voluntad](#731-willingness),
  - [§7.3.2 Capacidad](#732-capacity),
  - [§7.3.3 Paso probatorio](#733-proof-step),
  - [§7.3.4 Hallazgos](#734-findings), y
  - [§7.3.5 Las mismas condiciones para cada operador](#735-same-terms-for-every-operator));
  - [§7.4](#74-denial-and-revocation) (*denegación y revocación*, con
  - [§7.4.1 Qué son la denegación y la revocación](#741-what-denial-and-revocation-are),
  - [§7.4.2 Cuándo se exige denegar o revocar](#742-when-denial-or-revocation-is-required),
  - [§7.4.3 Primero la protección](#743-protection-first),
  - [§7.4.4 Procedimiento](#744-process),
  - [§7.4.5 Efecto](#745-effect), y
  - [§7.4.6 No es una prohibición permanente](#746-not-a-permanent-bar)).

</details>

<br>

*En términos sencillos: toda revisión de certificación termina con un resultado declarado, respaldado por pruebas y por las inquietudes planteadas durante el proceso. Nada entra en funcionamiento hasta que se certifica, el resultado publicado da a los seres sintientes afectados una oportunidad práctica de impugnarlo y se verifican las protecciones requeridas antes de la puesta en marcha.*

Esta sección es la **Fase IV, Decidir**, después de [§6 Proceso del foro](#6-forum-process) (**Fase III, Revisión**). Trata el resultado al que llegan los foros. [§7.1 Barrera de puesta en marcha](#71-go-live-gate) establece dicha barrera y [§7.2 Defectos de certificación y corrección](#72-certification-defects-and-correction) determina qué ocurre cuando se detecta un defecto.

La decisión de certificación debe declarar el resultado en el registro, conforme a la [Parte C §8.1 Contenido mínimo del registro](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents), junto con las inquietudes planteadas para llegar a él. El resultado será uno de estos:

- certificación provisional;
- certificación plena;
- certificación condicional;
- certificación aplazada;
- no certificación;
- retiro;
- vencimiento; o
- levantamiento de condiciones.

Un sistema que no tiene certificación provisional ni plena está **No certificado**. Así ocurre cuando la certificación está:

- aplazada;
- denegada;
- retirada; o
- vencida.

La certificación provisional y la certificación plena son los dos **estados** de la certificación. La [Parte C §9.2 Certificación provisional y plena](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) explica cómo un sistema obtiene, conserva y pierde cada estado. Las condiciones de una certificación condicional pueden aplicarse a cualquiera de ellos.

<a id="71-go-live-gate"></a>
