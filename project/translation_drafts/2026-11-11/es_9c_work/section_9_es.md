<a id="9-recertification-and-reopening"></a>

### 9. Recertificación y reapertura

<details>
<summary><strong><span style="color: #2563eb;">Rastro</span></strong></summary>

- Antecedentes:
  - [Parte B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (*el resultado vigente*);
  - [§8](#8-system-certification-record) (*el Registro de Certificación del Sistema completado que sigue cada recertificación o revisión reabierta*);
  - [Parte A §2](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (9.000 §2) a
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*clasificación errónea, desalineación y defectos detectados en la evaluación*);
  - [§10](#10-challenging-a-certification) (*impugnación creíble*);
  - [Dos Finalidades Constitucionales](core_00.000_preamble.md#two-constitutional-aims);
  - [Capítulo Tres §1](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1) y
  - [§2](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*integridad de las definiciones y evasión*);
  - [Carta del Sistema](core_05.040_band_continuity.md#system-charter) (*desajuste entre la Carta del Sistema y la conducta, y revisión vencida*).
- Consecuencias: [§11.3](#113-verified-input-gate) y [§11.5](#115-violation-standing-record) (*control de entradas verificadas cuando los hechos respaldan hallazgos adversos*); [Capítulo Quince](core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction) (15.000) (*supervisión del foro reabierta*); [Capítulo Once](core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened) (11.000).
- Leer junto con: **[CS-6.305 §5](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Reclasificación y gobernanza del ciclo de vida*) y **[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*Requisito de reclasificación*).
- Subsecciones:
  - [§9.1](#91-recertification-schedule-and-the-new-system-certification-record) (*calendario de recertificación y nuevo Registro de Certificación del Sistema*);
  - [§9.2](#92-reopening-triggers) (*activadores de reapertura*);
  - [§9.3](#93-provisional-and-full-certification) (*certificación provisional y plena*, con
  - [§9.3.1 Los dos estados](#931-the-two-statuses),
  - [§9.3.2 Fallo y descenso de estado](#932-failure-and-step-down),
  - [§9.3.3 Causa de la desalineación](#933-cause-of-misalignment),
  - [§9.3.4 Plazos por nivel](#934-tier-windows),
  - [§9.3.5 Dependencia de clase A](#935-class-a-reliance), y
  - [§9.3.6 Verificación, no afirmación](#936-verification-not-assertion));
  - [§9.4](#94-non-evasion) (*no evasión*).

</details>

<br>

*En términos sencillos: ningún resultado dura para siempre. Mientras un sistema opera, las personas titulares designadas supervisan los resultados reales y las salvaguardias, responden a incidentes e impugnaciones y cumplen las condiciones de certificación incluidas en el Registro de Certificación del Sistema. Un sistema certificado se recertifica según el calendario que fija su clase, con una auditoría a mitad de cada intervalo. La revisión se reabre cuando cambian hechos materiales o cuando lo exige una impugnación creíble. Los defectos exigen protección, corrección y verificación independiente. Cada ronda de revisión inicia un nuevo Registro de Certificación del Sistema enlazado al anterior; el nuevo registro no borra el anterior ni las impugnaciones presentadas contra él. Una aprobación antigua no sustituye el cumplimiento vigente del Piso de Derechos.*

Esta sección es la subfase **VIa** de la Fase VI (*Operación*): operar y recertificar. Abarca la operación del sistema certificado, su actualización y la reapertura de la revisión.

**Validación.** El Capítulo Quince denomina *validación continua de la alineación* a la revisión que un foro realiza de un sistema existente. En este capítulo, la validación no es un proceso separado. Es una ronda de certificación de un sistema que ya opera: una recertificación, una revisión reabierta o una revisión nueva. Se lleva a cabo conforme a [Parte B §6 Proceso del foro](core_09.005_system_alignment_certification_record_process.md#6-forum-process), como cualquier otra ronda de certificación, y concluye con un resultado conforme a [Parte B §7 Resultados de certificación](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes).

**Supervisión y respuesta.** Los operadores y custodios deben ejecutar el plan operativo del Registro de Certificación del Sistema conforme a [§8.1 Contenido mínimo del registro](#81-minimum-record-contents). Las personas titulares designadas deben:

- conservar las pruebas de supervisión;
- investigar los incidentes e indicadores materiales;
- remitir las impugnaciones a la autoridad asignada; y
- ejecutar las medidas de protección provisional y corrección que se requieran.

Cualquiera de los siguientes hechos que ponga materialmente en duda la alineación exige una revisión oportuna del foro conforme a esta sección y no debe esperar a la próxima recertificación programada:

- un incidente;
- una condición de certificación incumplida;
- un paso probatorio omitido conforme a [Parte B §7.3 Preparación para la reparación: voluntad y capacidad para corregir](core_09.005_system_alignment_certification_record_process.md#73-remediation-readiness-willingness-and-capacity-to-correct);
- pruebas falsas de preparación; o
- una impugnación creíble.

La corrección, el cumplimiento de condiciones y su liberación siguen los requisitos de verificación independiente de [Parte B §7 Resultados de certificación](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes).

<a id="91-recertification-schedule-and-the-new-system-certification-record"></a>

#### 9.1 Calendario de recertificación y nuevo Registro de Certificación del Sistema

*En términos sencillos: una certificación no dura para siempre. Se recertifica según el calendario que fija la clase del sistema, con una auditoría a mitad de cada intervalo. Cada ronda de certificación abre un nuevo Registro de Certificación del Sistema enlazado al anterior.*

Un **Registro de Certificación del Sistema** debe recertificarse con la periodicidad que corresponda a su clase de sistema conforme a [Capítulo Quince §6 Resolución oportuna, niveles de materialidad y disciplina contra las demoras](core_15.000_forum.md#review-cadence) (*Cadencia de revisión*), y debe auditarse a mitad de cada intervalo.

**Un registro nuevo para cada ronda de certificación.** Cada ronda posterior de certificación —recertificación, revisión reabierta o revisión nueva— abre un nuevo Registro de Certificación del Sistema. El nuevo Registro de Certificación del Sistema:

- se enlaza con el Registro de Certificación del Sistema completado que le precede e indica qué cambió desde entonces ([§8.1.1 Identidad del sistema, alcance y Registro de Certificación del Sistema previo](#811-system-identity-scope-and-prior-system-certification-record)); y
- sigue desde el paso 1 la [Parte B §6.2 Secuencia de supervisión](core_09.005_system_alignment_certification_record_process.md#62-supervisory-sequence), igual que una primera certificación.

El Registro de Certificación del Sistema completado se conserva tal como estaba ([§8 Registro de Certificación del Sistema](#8-system-certification-record)). Sigue siendo el registro del periodo que cubre y permanece abierto a impugnación conforme a [Parte B §6.3 Cadena de impugnabilidad](core_09.005_system_alignment_certification_record_process.md#63-contestability-chain). El estado de certificación, el recuento de recertificaciones limpias y los indicadores de supervisión se transfieren mediante el enlace. Se verifican en el nuevo Registro de Certificación del Sistema conforme a [§9.3 Certificación provisional y plena](#93-provisional-and-full-certification).

<a id="92-reopening-triggers"></a>

#### 9.2 Activadores de reapertura

*En términos sencillos: una certificación puede reabrirse antes de la fecha programada cuando algo material cambia o falla, como una conducta ocultada, una dependencia creciente, un riesgo nuevo o una impugnación creíble.*

La revisión se reabre conforme al Capítulo Quince y a las obligaciones incorporadas de implementación del sistema cuando sea material cualquiera de los siguientes hechos:

- **Cambio en el sistema o su contexto:**
  - un cambio material en el sistema, su uso o su contexto operativo;
  - un aumento de dependencias, incluido el aumento de la dependencia del sistema y de la extracción de fundamentos compartidos, así como una concentración que supere un umbral que haya fijado quien adopta la Constitución conforme a [Capítulo Uno §11.4 Concentración de recursos y dependencias](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (el aumento de nivel no espera a que se alcance un umbral: [Parte A §2.2](core_09.000_system_alignment_certification_evaluation.md#22-how-system-class-scales-every-evaluation));
  - una caída significativa de los flujos de retorno del sistema (lo que devuelve a esos fundamentos), conforme a [Apoyo proporcional entre sistemas](core_05.040_band_continuity.md#proportionate-cross-system-support).
- **Algo observado o comunicado:**
  - conducta ocultada;
  - un riesgo nuevo;
  - antecedentes de incidentes;
  - pruebas de partes interesadas;
  - una impugnación creíble conforme a [§10 Impugnar una certificación](#10-challenging-a-certification);
  - una objeción ecológica.
- **Desalineación de clasificación o de tipos de datos:**
  - desalineación de la clase del sistema o una reevaluación vencida conforme a **[CS-9.305 §3 Factores de criticidad, concentración, temporales y adversariales](corpus_systems/cs_09.305_system_classification_machinery.md#cs-9305-3-criticality-concentration-temporal-and-adversarial-factors)**, en particular su [§3.5 Requisito de reclasificación](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement);
  - desalineación del tipo de datos o su tratamiento, o una reevaluación programada de tipos de datos vencida u omitida, conforme a **[CS-6.305 §5 Principios de gobernanza entre ámbitos](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-5-cross-domain-governance-principles)**, en particular su [§5.2 Reclasificación y gobernanza del ciclo de vida](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance);
  - desalineación de clasificación.
- **Carta del Sistema y gobernanza del operador:**
  - una modificación de la [Carta del Sistema](core_05.040_band_continuity.md#system-charter), un desajuste entre la Carta del Sistema y la conducta, la operación material fuera del alcance establecido por la Carta o una revisión programada de la Carta vencida;
  - una infracción de gobernanza de una Institución cuyo [portafolio](core_05.040_band_continuity.md#portfolio) incluya el Sistema (una determinación de que su gobernanza falló, una denegación o revocación de la Institución por motivos relacionados con su gobernanza, o un hallazgo de causa que atribuya a la Institución la desalineación de otro Sistema), según se define en [Capítulo Diez §9.6 Reapertura de los sistemas de la Institución](core_10.000_institutional_alignment_certification.md#96-reopening-the-institutions-systems). Solo una infracción material reabre la revisión.
- **Desalineación de evaluación:** una desalineación o un defecto reflejado en el Registro de Certificación del Sistema conforme a cualquier evaluación aplicable de la Parte A, desde [§2 Evaluación de la clase del sistema](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) hasta [§5 Evaluaciones del Piso de Derechos y por ámbito](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations). Esto incluye defectos en la evaluación o divulgación de riesgos conforme a [§3.2 Alcance sistémico y factores de riesgo](core_09.000_system_alignment_certification_evaluation.md#32-systemic-scope-and-risk-factors).

**Por qué importa la reapertura.** La reapertura por desalineación, aumento de dependencias o una impugnación creíble protege la finalidad de **Continuidad** conforme a [Dos Finalidades Constitucionales](core_00.000_preamble.md#two-constitutional-aims). Esto importa cuando los sistemas compartidos condicionan la provisión duradera de elementos esenciales para la supervivencia, el acceso a la educación, las vías para desarrollar capacidades, una dependencia confiable o la seguridad. Una certificación desactualizada no debe sustituir el cumplimiento actual del Piso de Derechos.

<a id="93-provisional-and-full-certification"></a>

#### 9.3 Certificación provisional y plena

*En términos sencillos: un sistema se gana la confianza por etapas. Los sistemas nuevos y los que no superan una evaluación empiezan con límites estrictos y se revisan con frecuencia. Solo un sistema que no tenga desalineaciones actuales ni indicios de que se aproximen obtiene la certificación plena y un intervalo más largo. Si una evaluación falla, vuelve a la certificación provisional.*

<a id="931-the-two-statuses"></a>

##### 9.3.1 Los dos estados

La certificación se mantiene en uno de dos estados. Cada estado tiene su propio intervalo de certificación, que se indica en el Registro de Certificación del Sistema conforme a [§8.1 Contenido mínimo del registro](#81-minimum-record-contents):

- La **[certificación provisional](core_05.040_band_continuity.md#provisional-certification)** es el estado de:
  - la primera certificación de un sistema, incluido un sistema recién desplegado; y
  - un sistema certificado después de una recertificación fallida o de una revisión reabierta o nueva que detectó desalineación.

  La certificación provisional tiene un intervalo más corto que el intervalo de certificación plena para la misma clase de sistema. Los límites de dependencia se indican en el Registro de Certificación del Sistema.
- La **[certificación plena](core_05.040_band_continuity.md#full-certification)** solo se obtiene en una recertificación de un sistema que ya tenga certificación provisional y únicamente si se cumplen las tres condiciones siguientes:
  1. el sistema completó la cantidad requerida de recertificaciones provisionales limpias consecutivas: al menos una, y más para las clases de sistema superiores, según lo establezca el documento adoptado;
  2. no existe desalineación actual: el Registro de Certificación del Sistema no muestra ninguna desalineación abierta, defecto sin corregir, comprobación vencida ni prueba de regresión fallida; y
  3. ningún indicador de supervisión señala una desalineación inminente: los activadores de supervisión y las métricas de tendencia que constan en el Registro de Certificación del Sistema no muestran que se haya superado un umbral ni una tendencia hacia él.

La certificación plena tiene el intervalo de certificación escalado a la clase del sistema. Sigue estando limitada en el tiempo y no constituye una aprobación permanente.

Una recertificación es **limpia** cuando cumple las condiciones 2 y 3.

<details>
<summary><strong><span style="color: #2563eb;">Guía para quien lee (no operativa): estado de certificación</span></strong></summary>

> Esta tabla resume la §9.3. Si difiere del texto, prevalece el texto.
>
> | | Certificación provisional | Certificación plena |
> |---|---|---|
> | **Quién la tiene** | Primera certificación, incluido un sistema recién desplegado; sistema certificado tras una recertificación fallida o una revisión reabierta o nueva que detectó desalineación | Sistema que la obtuvo en una recertificación mientras tenía certificación provisional |
> | **Cómo se obtiene** | Se concede mediante un resultado de certificación | Cantidad requerida de recertificaciones provisionales limpias consecutivas (al menos una), sin desalineación actual y sin indicadores de desalineación inminente |
> | **Intervalo de certificación** | Intervalo provisional, más corto que el intervalo de certificación plena para la misma clase de sistema | Intervalo escalado a la clase del sistema; sigue limitado en el tiempo |
> | **Si falla una recertificación** | Se aplican las consecuencias de la Parte B §7; la siguiente certificación será provisional y el recuento de rondas limpias vuelve a cero | Se aplican las consecuencias de la Parte B §7; la siguiente certificación será provisional y el recuento de rondas limpias vuelve a cero |
> | **Si aparece un indicador de desalineación inminente** | Se mantiene el estado provisional; el recuento no avanza | Desciende al estado provisional |

</details>

<a id="932-failure-and-step-down"></a>

##### 9.3.2 Fallo y descenso de estado

Lo que determine una recertificación, una revisión reabierta o una revisión nueva establece qué ocurre con el estado del sistema:

- Una recertificación que detecta una desalineación actual es una recertificación **fallida**. Se aplican las consecuencias de [Parte B §7 Resultados de certificación](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes). La siguiente certificación que puede obtener el sistema será provisional, aunque la siguiente comprobación resulte limpia. El recuento de recertificaciones limpias vuelve a cero.
- Una recertificación que no detecta desalineación actual, pero sí un indicador de desalineación inminente, no es fallida ni limpia. Un sistema con certificación provisional se mantiene en ese estado y su recuento no avanza. Un sistema con certificación plena desciende a la certificación provisional.
- Una revisión reabierta conforme a [§9 Recertificación y reapertura](#9-recertification-and-reopening) que detecta una desalineación tiene el mismo efecto que una recertificación fallida.
- Una revisión nueva de un sistema certificado que detecta desalineación actual tiene el mismo efecto que una recertificación fallida. Si el sistema no tiene ningún estado de certificación, se aplican las reglas de denegación de [Parte B §7.4 Denegación y revocación](core_09.005_system_alignment_certification_record_process.md#74-denial-and-revocation).

<a id="933-cause-of-misalignment"></a>

##### 9.3.3 Causa de la desalineación

Cuando una evaluación, recertificación, revisión reabierta o revisión nueva detecte desalineación, el Registro de Certificación del Sistema debe indicar una de estas causas:

- **causada por el diseño:** el sistema o su proceso está construido de modo que produce resultados desalineados incluso cuando se opera según lo previsto;
- **causada por la operación:** el diseño parece sólido, pero la forma en que se opera, alimenta o mantiene el sistema provoca resultados desalineados; o
- **aún no determinada:** los remedios para el diseño y la operación siguen disponibles hasta que el foro determine la causa.

El hallazgo de causa tiene estos límites:

- Si el Sistema sigue produciendo resultados desalineados, está desalineado, aunque su diseño parezca sólido en el papel. Un diseño que parece sólido no es una defensa.
- Un diseño que produciría resultados desalineados constituye desalineación antes de que aparezca uno de esos resultados.
- El hallazgo de causa determina el remedio buscado y el alcance de cualquier revisión reabierta. Nunca determina si el sistema está desalineado.

Cuando la desalineación es causada por el diseño:

- el recuento de recertificaciones limpias se mantiene en cero hasta que se implemente y verifique el rediseño;
- el foro que determinó la causa, o el siguiente foro asignado conforme a [Parte B §6.2 Secuencia de supervisión](core_09.005_system_alignment_certification_record_process.md#62-supervisory-sequence), verifica el rediseño dentro del [plazo de admisión correspondiente](core_05.040_band_continuity.md#tier-window), y puede hacerlo en la primera recertificación provisional;
- una **evaluación de componente** (la parte de una ronda de certificación que corresponde a un componente, según la define [Parte B §6.1 Supervisión del foro y funciones de los componentes](core_09.005_system_alignment_certification_record_process.md#61-forum-supervision-and-component-roles)) realizada antes de verificar el rediseño no cuenta para el total de rondas limpias, aunque resulte limpia; y
- un cambio en la forma de operar el sistema no satisface este requisito.

Esto se suma a las reglas anteriores de descenso de estado y no las reemplaza. El operador o cualquier senciente afectado puede pedir al foro que revise el hallazgo de causa. Si cambia la causa, estas reglas dejan de aplicarse.

<a id="934-tier-windows"></a>

##### 9.3.4 Plazos por nivel

Cuando una evaluación inicial, recertificación, revisión reabierta o revisión nueva detecta desalineación:

- el asunto se clasifica conforme a los niveles de materialidad de [Capítulo Quince §6 Resolución oportuna, niveles de materialidad y disciplina contra las demoras](core_15.000_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline);
- se presume que corresponde al nivel que coincide con la clase del sistema (por ejemplo, se presume que un sistema de clase A desalineado corresponde al nivel A);
- la admisión, preservación de pruebas, protección provisional y decisión siguen los plazos y límites máximos de ese nivel; y
- cualquier demora se revisa conforme a lo que exige esa sección.

<a id="935-class-a-reliance"></a>

##### 9.3.5 Dependencia de clase A

En comparación con la certificación plena, la certificación provisional tiene un intervalo más corto, por lo que exige una recertificación más temprana ([§9.3.1 Los dos estados](#931-the-two-statuses)), y límites de dependencia indicados en el Registro de Certificación del Sistema ([§8.1 Contenido mínimo del registro](#81-minimum-record-contents)). La interrupción se gestiona de este modo:

- Por sí sola, la certificación provisional no exige interrumpir un sistema cuya interrupción privaría a alguien de elementos esenciales para la supervivencia antes de que haya sustitutos;
- la protección provisional y las condiciones de certificación de [Parte B §7 Resultados de certificación](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) se ocupan de ese caso;
- lo mismo se aplica mientras se retiene el recuento después de un hallazgo de desalineación causada por el diseño: retener el recuento nunca interrumpe por sí solo un sistema del que dependen los sencientes; y
- mientras dure la retención, el foro indica la protección provisional, las condiciones de certificación sobre la dependencia y el aviso a las personas dependientes.

<a id="936-verification-not-assertion"></a>

##### 9.3.6 Verificación, no afirmación

El estado de un sistema, su recuento de recertificaciones limpias y sus indicadores de supervisión deben verificarse, y la verificación debe estar abierta a revisión independiente. No basta con que el propio sistema lo afirme:

- Los indicadores no pueden elegirse ni fijarse de modo que la desalineación nunca pueda aparecer.
- El rediseño se verifica de la misma forma: mediante pruebas que otras personas puedan comprobar.
- La certificación plena no elimina ningún motivo para reabrir la revisión. Se siguen aplicando todos los activadores de [§9 Recertificación y reapertura](#9-recertification-and-reopening).
- La evasión se trata conforme a [§9.4 No evasión](#94-non-evasion).

<a id="94-non-evasion"></a>

#### 9.4 No evasión

La evasión de las obligaciones de este capítulo se rige por el Capítulo Tres; este capítulo no vuelve a exponer esa disciplina:

- [Capítulo Tres §1 — Integridad de las definiciones y restricciones contra la evasión](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints);
- [Capítulo Tres §2 — Incumplimiento a partir de la conducta observable del sistema](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior);
- incluida la evasión de alcance y límites conforme a [Capítulo Tres §2.1 Patrones comunes de evasión](core_03.000_definition_integrity.md#21-common-evasion-patterns).

