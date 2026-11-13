<!-- Borrador parcial de traducción al español. Fuente: core_12.000_standing_measurement.md; snapshot de origen: 9c2c8c10c871d91157bcd27b9f56ad6a1cec90d3. Traducción asistida por IA; no revisada. Cobertura parcial: §§1–3. -->

### 1. Pregunta 2 — ¿qué tan bueno o malo fue?
<details>
<summary><strong><span style="color: #2563eb;">Traza</span></strong></summary>

- Anterior: [Capítulo Once §2](core_11.000_standing_assessment.md#2-question-1--what-happened) (*Pregunta 1 — registros de posición y hechos verificados*); [Capítulo Once §2.5](core_11.000_standing_assessment.md#25-verified-input-gate) (*puerta de datos verificados*); [Capítulo Once §4](core_11.000_standing_assessment.md#4-standing-record-operational-requirements) (*requisitos del registro*); [Capítulo Once §1](core_11.000_standing_assessment.md#1-the-three-questions) (*marco de las tres preguntas*).
- Posterior:
  - [§2](#2-magnitude-and-severity-input-dimensions) (*dimensiones de entrada de medición para ambos ejes*);
  - [§3](#3-route-descriptor-catalogs-and-measurement-roles) (*catálogos de descriptores de ruta*);
  - [§4](#4-slot-grammar-and-shared-scaling) (*gramática de casillas y escala compartida*);
  - [§5](#5-constitutional-inputs-to-axis-assignment) (*derivación constitucional para asignar ejes*);
  - [§6](#6-unified-proportional-lequ-scale--contribution-and-violation-axes) (*asignación a los ejes de Contribución y Violación*);
  - [§7](#7-standard-contribution-measures) (*medidas estándar de contribución publicadas por adoptantes*);
  - [§8](#8-measurement-illustrations) (*ejemplos prácticos de medición*);
  - [§9](#9-hand-off-to-question-3--cross-question-measurement-hooks) (*traspaso a la Pregunta 3*);
  - [Capítulo Trece §6.2](core_13.000_standing_integration.md#62-competency-bars-and-clearances) (13.000 §6.2) (*Pregunta 3 de contribución — delegación segura*);
  - [Capítulo Trece §4.2](core_13.000_standing_integration.md#42-prevention--general-standing-locks) (13.000 §4.2) (*bloqueos de prevención*);
  - [Capítulo Trece §5](core_13.000_standing_integration.md#5-lock-design-and-enforcement) (13.000 §5) (*diseño y aplicación de bloqueos*).
- Leer junto con: [Capítulo Once §4.1](core_11.000_standing_assessment.md#41-minimum-record-contents) (*campos verificados del registro de posición; sin efectos de posición en el Capítulo Once*).
</details>

<br>

*En términos sencillos: la Pregunta 2 mide los hechos verificados de la Pregunta 1. Pregunta **qué tan buena fue la contribución** o **qué tan grave fue la violación**. Aquí se presentan por primera vez los dos ejes formales de medición: el **Eje de Contribución** para la ayuda verificada y el **Eje de Violación** para el daño verificado. Los ejes permanecen separados; no son dos lados de una puntuación neta.*

Para decidir en qué casilla ubicar la contribución o violación de alguien, este capítulo mide el impacto mediante una **Unidad Equivalente a una Vida (LEQU, por sus siglas en inglés)**. Una LEQU equivale aproximadamente a salvar o destruir toda una vida de bienestar de un senciente. No se trata de contar cuerpos ni dólares, sino de determinar si una acción cambió de forma significativa el bienestar de la comunidad constitucional. La misma unidad sirve para cualquier ser senciente, humano o no.

#### 1.1 Referencia LEQU

Una **Unidad Equivalente a una Vida** (**LEQU**) es la unidad abreviada de ese beneficio o pérdida constitucional equivalente a una vida completa, cuando la implementación adoptada requiere una calibración numérica.

- La unidad no depende del sustrato.
- Un adoptante actual puede usar una vida humana ordinaria como ejemplo de calibración en contextos biológicos humanos, pero la referencia vinculante es senciente y constitucional, no está ligada a una especie.

Un **beneficio constitucional equivalente a una vida completa** significa un beneficio verificado comparable a preservar, restaurar o liberar una vida senciente completa de bienestar no trivial y compatible con los derechos. Una **pérdida constitucional equivalente a una vida completa** significa daño, desperdicio, destrucción, cierre de opciones, privación o materialización de un riesgo verificados y comparables a destruir, consumir injustamente o impedir un beneficio constitucional equivalente a una vida completa.

#### 1.2 Límites para el uso de LEQU

Se aplican los siguientes límites siempre que se use LEQU.

- **No es una regla de puntuación neta:** no se pueden «compensar» violaciones con contribuciones ni viceversa. Cada eje se sostiene por separado.
- **No es una métrica obligatoria de vida humana:** LEQU es genérica para los sencientes; se aplica a cualquier ser consciente, no solo a los humanos.
- **No es una métrica de acusación:** las alegaciones, etiquetas de admisión, decisiones de derivación, reputación, estatus desfavorecido o desaprobación moral no aportan beneficio al Eje de Contribución ni gravedad al Eje de Violación sin datos verificados conforme al **Capítulo Once sección 2.5** y calibración conforme a la **sección 6**.
- **No es una licencia para intercambiar derechos:** las afirmaciones que se presenten como eficiencia, capacidad productiva, innovación, reducción de cargas, seguridad, represalia, respuesta a emergencias o necesidad institucional deben descontarse o rechazarse cuando dependan de:
  - coacción;
  - traslado discriminatorio de cargas;
  - agotamiento ecológico;
  - trabajo no remunerado oculto;
  - opacidad evitable;
  - reducción del Piso de Derechos;
  - captura;
  - indicadores indirectos engañosos;
  - pérdida de impugnabilidad; o
  - agregación no revisable.

#### 1.3 Solo Pregunta 2 — alcance y derivación

Esta parte cubre únicamente la Pregunta 2, el paso de medición. Toma hechos ya verificados (Pregunta 1) y pregunta qué tan buena fue una contribución o qué tan grave fue una violación.

- Parta de los hechos ya verificados conforme al **Capítulo Once sección 2** e incorporados al registro de posición conforme al **Capítulo Once sección 4**, y mídalos usando las dimensiones de la **sección 2**.
- Luego asigne a cada tipo de ayuda o daño su nombre estándar de los catálogos: el catálogo de **ruta de beneficio** para la ayuda (**sección 3.1**) y el de **ruta de daño** para el daño (**sección 3.2**).
- Cada nombre también indica cuánto cuenta ese tipo de ayuda o daño para determinar *qué tan bueno* o *qué tan grave* fue.
- Las reglas sobre lo que se deriva de un beneficio están en el [lado de beneficio](core_13.000_standing_integration.md#62-competency-bars-and-clearances), y las reglas sobre lo que se deriva de un daño, en el [lado de daño](core_13.000_standing_integration.md#42-prevention--general-standing-locks).
- La Pregunta 3 decide qué ocurre después. Comience con [Capítulo Trece §3 Integración de descriptores y normalización de adjuntos](core_13.000_standing_integration.md#3-descriptor-integration-and-attachment-normalization).

#### 1.4 Puente con el estatus de senciencia

La medición de la posición **no** decide si una entidad es **senciente**.

- Las disputas de estatus se remiten a [Adjudicación del estatus de senciencia](core_05.055_band_participation.md#sentience-status-adjudication) y al [Artículo VI-B](core_06.005_rights_part_b.md#article-vi-b-sentience-status-adjudication-floor) (*Piso de Adjudicación del Estatus de Senciencia*). No se remiten a puntuaciones LEQU ni a registros de clasificación.
- Mientras siga abierta una disputa de estatus conforme a [Vida Senciente en Disputa](core_05.055_band_participation.md#contested-sentient-life), el **Artículo VI-B** (*Piso de Adjudicación del Estatus de Senciencia*) incluye por defecto a la entidad: esta puede seguir midiéndose y presentar un registro de posición hasta que se resuelva la disputa, y los operadores no deben tratar la disputa abierta, por sí sola, como motivo para negarle posición.
- Si se determina que la entidad es [Senciente](core_05.055_band_participation.md#sentient), o su estatus se restringe o restablece tras una adjudicación en una decisión que puede revisarse:
  - el sujeto del registro de posición se actualiza a partir de ese momento; y
  - no se debe retrotraer una exclusión injusta para borrar la elegibilidad de la entidad a ser medida durante el período intermedio, salvo mediante [Reparación y Remediación](core_05.035_band_accountability.md#redress-and-remediation).

### 2. Dimensiones de entrada de magnitud y gravedad

*En términos sencillos: esta sección explica qué produce la Pregunta 2 (**sección 2.1**) y luego enumera qué se debe examinar al medir una contribución verificada o una violación verificada (**sección 2.2**). Cada eje se mide por separado. Las reglas de escala compartida están en la **sección 4.2**, y la casilla se obtiene de la escala de la **sección 6**.*

La escala de casillas mide la magnitud y el tipo de un resultado constitucional. Solo cuenta los resultados verificados.

**Qué cuenta la escala y cómo se relaciona con las pruebas centrales de la Constitución:**

- **[Dos Finalidades Constitucionales](core_00.000_preamble.md#two-constitutional-aims):** ambos ejes miden el efecto sobre el **Florecimiento** y la **Continuidad**. El Eje de Contribución los impulsa. El Eje de Violación los hace retroceder.
- **[Dos Preguntas Fundamentales](core_00.000_preamble.md#two-fundamental-questions):** cada eje aporta los hechos verificados para una pregunta. Responder una no responde la otra; por ello, los dos ejes nunca se compensan entre sí.
  - **Primera pregunta:** el Eje de Contribución aporta los hechos verificados. ¿El sistema recompensa conductas que ayudan a los sencientes a florecer y perdurar, dicen la verdad y reparan el daño?
    - **Cuenta:** el beneficio constitucional verificado, incluida la reducción verificada de riesgos.
    - **No cuenta:** el volumen de producción bruto, el prestigio, la riqueza, cuánto se usa algo, la rapidez ni el tamaño de la institución.
  - **Segunda pregunta:** el Eje de Violación aporta los hechos verificados. ¿El sistema recompensa conductas que dañan, engañan, excluyen, demoran, desperdician o trasladan injustificadamente costos a otros?
    - **Cuenta:** pérdida constitucional, daño, desperdicio, opciones perdidas (cierre de opciones), peligro o aumento del riesgo verificados.
    - **No cuenta por sí solos:** el estatus desfavorecido, las alegaciones o la desaprobación moral.
- **[Tétrada Constitucional](core_00.000_preamble.md#constitutional-tetrad):**
  - **Supervisión y rendición de cuentas:** «verificado» significa que un actor identificado responde por el hallazgo y que ninguna parte verifica su propia afirmación.
  - **Actuación a tiempo:** la demora evitable se registra como hecho independiente, no se incorpora al tamaño de la pérdida.

#### 2.1 Qué produce la Pregunta 2

La Pregunta 2 consigna lo siguiente en el registro de posición de cada eje. Son mediciones, no efectos de posición (las consecuencias que decide la Pregunta 3):

| **Qué se produce** | **Eje de Contribución** | **Eje de Violación** |
| --- | --- | --- |
| **Dónde se consigna** | El registro de posición de contribución. | El registro de posición de violación. |
| **Casilla** | La casilla aplicable más alta del **Eje de Contribución** (`s` = 1–9). | La casilla aplicable más alta del **Eje de Violación** (`s` = 1–9). |
| **Descriptores de ruta** | Los **descriptores de ruta de beneficio** aplicables, acumulados. | Los **descriptores de ruta de daño** aplicables, acumulados. |
| **Datos que se entregan a la Pregunta 3** | Los datos que fijan el punto de partida para reconocer la contribución, conforme a [Capítulo Trece §6 Consecuencias de contribución en segundo lugar](core_13.000_standing_integration.md#6-contribution-consequences-second). | Los datos que fijan la banda predeterminada de bloqueo (el punto de partida para determinar cuán estricto es un bloqueo), conforme a [Capítulo Trece §5 Diseño y aplicación de bloqueos](core_13.000_standing_integration.md#5-lock-design-and-enforcement). |
| **Total LEQU** | Evalúe por separado cada tipo pertinente de beneficio (ecológico, sistémico o de recursos) y luego consigne un total LEQU para toda la contribución. | Evalúe por separado cada tipo pertinente de daño (daño ecológico, daño sistémico o pérdida de recursos) y luego consigne un total LEQU para toda la violación. |

Recordatorio: nada de esto cancela un registro de violación abierto. La regla de no compensación está en [Capítulo Once §2.4 Registros de posición vinculados y puente de no compensación](core_11.000_standing_assessment.md#24-linked-standing-records-and-no-offset-bridge).

#### 2.2 Dimensiones de entrada de magnitud de contribución y gravedad de violación

<a id="contribution-table-q1-magnitude-input-dimensions"></a>
<a id="contribution-table-q2-magnitude-input-dimensions"></a>

**Pregunta 2 — ¿qué tan bueno o grave fue?** Para decidir dónde queda una contribución en el Eje de Contribución o una violación en el Eje de Violación (su **casilla**, de 1 a 9), y qué descriptores de beneficio o daño corresponden, examine tres partes. Pueden aplicarse varios descriptores a la vez y se acumulan. Consigne los resultados en el registro de posición del eje, como se indica en la **sección 2.1**. La **sección 6** contiene la escala unificada para la parte 2, que es la misma para beneficios y daños. Explica cómo estimar en LEQU el beneficio o la pérdida totales (una Unidad Equivalente a una Vida, aproximadamente el bienestar de una vida entera) y qué casilla corresponde a cada cantidad. En el Eje de Contribución, las casillas se agrupan en cuatro bandas.

**1. Compruebe cómo se produjo.** Los dos ejes lo tratan de manera distinta:

- **Contribución (calidad de la conducta):** puede aumentar o limitar cuánto beneficio cuenta: ¿fue trazable?, ¿evitó trasladar costos a otros?, ¿se realizó con cuidado?, ¿es compatible con la Constitución? Las cinco comprobaciones están en [§2.2.1 Cómo afecta al cómputo la manera en que se produjo un beneficio](#221-how-the-way-a-benefit-was-produced-affects-what-counts).
- **Violación (carácter de la conducta):** se registra por separado de la magnitud del impacto. El deber, la negligencia, el engaño, la ocultación, la obstrucción de la rendición de cuentas, la coacción, la violencia, la intención, la crueldad y la habilitación estructural determinan quién responde, qué salvaguardias se necesitan y cómo responder, pero no modifican la casilla LEQU. Las reglas para registrar cada elemento están en [§2.2.2 Cómo se registra la manera en que se causó un daño](#222-how-the-way-a-harm-was-caused-is-recorded).

**2. Determine la magnitud: ¿cuán grande es el beneficio o la pérdida?** Esto determina la casilla.

| **Qué examinar** | **Qué efecto tiene** | **Dónde se establece** |
| --- | --- | --- |
| **Magnitud total (LEQU)** | La medida principal y la que determina la casilla. En una contribución, es el beneficio total verificado realizado, contado en LEQU. En una violación, es la pérdida constitucional total verificada. La designación de conducta indebida del Capítulo Catorce se decide por separado. | [§6 Escala proporcional LEQU unificada](#6-unified-proportional-lequ-scale--contribution-and-violation-axes) |
| **A quiénes alcanza (cuántos, con qué profundidad y cuán vulnerables)** | Ajusta la estimación LEQU y cuánto importa el beneficio o daño (su materialidad). | [§4.2 Reglas compartidas de escala del impacto](#42-shared-impact-scaling-rules); [Materialidad](core_05.050_band_oversight.md#materiality) |
| **Cuánto dura (duración; perdurabilidad de un beneficio, irreversibilidad de un daño)** | Ajusta la estimación LEQU. En una contribución, la administración responsable duradera, el beneficio intergeneracional o la reparación perdurable de una institución apuntan a las casillas superiores. En una violación, el trauma duradero, la pérdida irreversible y el daño duradero a la capacidad de los sencientes para actuar por sí mismos aumentan la estimación de la pérdida total. | [§4.2 Reglas compartidas de escala del impacto](#42-shared-impact-scaling-rules) |
| **Hasta dónde llega (a través de lugares o instituciones)** | Ajusta la estimación LEQU. En una contribución, por ejemplo, por el beneficio extendido a comunidades o instituciones, o a escala de una civilización. En una violación, el daño que se extiende a comunidades o instituciones, o a toda una civilización, puede aumentar la estimación de la pérdida total. | [§4.2 Reglas compartidas de escala del impacto](#42-shared-impact-scaling-rules) |

**3. Nombre los tipos de beneficio o daño (rutas).** Nombre las maneras en que se produjo el beneficio o daño verificado. Puede aplicarse más de una y se acumulan. Las listas están en el [**Catálogo de descriptores de rutas de beneficio**](#31-contribution-route-descriptor-catalog-and-measurement-roles) y el [**Catálogo de descriptores de rutas de daño**](#32-violation-route-descriptor-catalog-and-measurement-roles).

##### 2.2.1 Cómo afecta al cómputo la manera en que se produjo un beneficio

Compruebe esto antes de elegir una casilla del Eje de Contribución:

| **Qué se determina** | **Efecto en el beneficio** |
| --- | --- |
| Corrección pronta y verificada de un problema después de haber sido notificado | Puede contar como **Diligencia** (conducta cuidadosa y responsable) cuando produce un beneficio real y demostrable. |
| Daño trasladado a otros o carga ocultada | Limita el beneficio atribuido a la vía controvertida (la ruta específica a la que se atribuye el beneficio) o lo excluye. |
| Riesgo de captura verificado (el arreglo podría quedar bajo el control de intereses estrechos), dependencia estructural (los sencientes quedan integrados de modo que dependen de él) o diseño de salida y bloqueo (es difícil abandonarlo) | Limita el reconocimiento de la administración responsable. |
| Reparación verificada de una barrera de accesibilidad o participación | Puede aumentar cuánto importa el beneficio (su materialidad) y respaldar el descriptor de ruta de beneficio **Acceso e Inclusión** conforme a la **sección 3.1**. |
| Recompensa significativa procedente de un esquema de incentivos contrario a la Constitución, de conducta anticonstitucional o de un proceso materialmente defectuoso | Por defecto, no cuenta como beneficio. En ese caso, aplique [Capítulo Trece §5.4 Reglas especiales sobre violaciones](core_13.000_standing_integration.md#54-special-violation-rules) y el límite de transición de adopción del [Artículo XXVIII-A](core_06.020_rights_part_e.md#incentive-alignment-adoption-transition-carve-out) (*Adopción gradual y continuidad del Piso de Derechos*). |

##### 2.2.2 Cómo se registra la manera en que se causó un daño

La magnitud de un daño (su total LEQU, de la parte 2 anterior) determina la casilla. La manera en que se causó no la determina; por eso, cada tipo de conducta siguiente se registra por separado:

**Conducta que añade pérdida, contabilizada una sola vez en la magnitud:**

| **Qué se determina** | **Cómo se registra** |
| --- | --- |
| Demora evitable en responder o elevar el asunto, cuando existían el deber y la capacidad de actuar | Se registra como hecho de conducta separado. Toda pérdida adicional causada por la demora se cuenta una vez en la estimación LEQU. |
| Daño verificado de forma independiente a la integridad de un foro (perjuicio a la imparcialidad del foro) | Se cuenta exactamente una vez en la estimación LEQU. La omisión deshonesta, el incumplimiento deliberado del proceso de recusación, la coacción, el peligro para la libertad y otros hechos de conducta permanecen como descriptores separados y no modifican la casilla. |
| **Obstrucción de la rendición de cuentas** (interferencia verificada con los mecanismos que permiten exigir responsabilidad a quien corresponda, como la integridad de las pruebas, la verificación, el proceso del foro, los registros de posición, los plazos de reparación o las vías de impugnación y reparación) | Permanece como hecho de conducta registrado por separado. Toda pérdida adicional que cause en la vía identificada se cuenta una vez en la estimación LEQU, pero la etiqueta de obstrucción en sí no modifica la casilla. |

**Hechos de conducta registrados aparte de la magnitud del daño:**

| **Qué se determina** | **Cómo se registra** |
| --- | --- |
| Engaño, ocultación, evasión, repetición de la conducta tras recibir aviso, desprecio temerario, habilitación estructural (configurar las cosas para que el daño sea fácil o probable) o abuso de un desequilibrio importante de dependencia (explotar a quien depende mucho de uno) | Cada uno permanece como hecho de conducta registrado por separado. |
| Violencia, coacción, manipulación o peligro para la libertad | Permanece registrado por separado y puede requerir salvaguardias más estrictas cualquiera que sea la casilla. |
| [Crueldad](core_05.035_band_accountability.md#cruelty) (sufrimiento verificado como fin en sí mismo, o daño gratuito o degradante que excede lo necesario y proporcionado) | Permanece como hecho de conducta registrado por separado. Puede requerir salvaguardias más estrictas y límites a las reparaciones degradantes conforme al [Capítulo Trece §4 Violación, corrección y prevención](core_13.000_standing_integration.md#4-violation-correction-and-prevention), pero no modifica la casilla. |

**Responsabilidad y atribución:**

| **Qué se determina** | **Cómo se registra** |
| --- | --- |
| Difusión (cómo se distribuye la responsabilidad: quién cumplió qué función causal, tuvo qué autoridad o control, pudo prever el daño, se benefició, lo ocultó o pudo prevenirlo) | No forma parte del **alcance senciente** ni permite culpar a alguien por pertenecer a un grupo. |
| Colaborar con un daño o no oponerse a él | Puede respaldar una determinación de carácter basado en el deber, agravado o de rendición de cuentas colectiva solo si se verifica el vínculo con ese actor específico exigido por el **Capítulo Once secciones 4.1 y 4.3**. |

**Recompensas desalineadas:**

| **Qué se determina** | **Cómo se registra** |
| --- | --- |
| Aceptar o conservar a sabiendas una recompensa significativa contraria a la Constitución, sin informar oportunamente y con protección (informe protegido contra represalias) | Se registra conforme al [Capítulo Trece §5.4 Reglas especiales sobre violaciones](core_13.000_standing_integration.md#54-special-violation-rules), sujeto al [Artículo XXVIII-A](core_06.020_rights_part_e.md#incentive-alignment-adoption-transition-carve-out) (*Adopción gradual y continuidad del Piso de Derechos*). Solo la pérdida constitucional verificada que cause afecta la casilla. |

**Límite relativo a recompensas desalineadas.** Este capítulo solo mide cómo afecta una recompensa desalineada verificada (una recompensa contraria a la Constitución) al Eje de Contribución o al Eje de Violación. [Capítulo Trece §5.4 Reglas especiales sobre violaciones](core_13.000_standing_integration.md#54-special-violation-rules) establece el deber de informar, las exclusiones, las consecuencias de renunciar a la recompensa (decomiso), los deberes de corrección y las reglas de derivación.

### 3. Catálogos de descriptores de ruta y funciones de medición

*En términos sencillos: los dos catálogos siguientes nombran los tipos de ayuda verificada (**sección 3.1**) y de daño verificado (**sección 3.2**) que puede contener un registro de posición. Un descriptor indica cómo ocurrió el beneficio o el daño; los descriptores se acumulan y están subordinados a la casilla.*

**Regla de descriptores.** Los dos catálogos siguientes, [§3.1 Catálogo de descriptores de rutas de contribución y funciones de medición](#31-contribution-route-descriptor-catalog-and-measurement-roles) y [§3.2 Catálogo de descriptores de rutas de violación y funciones de medición](#32-violation-route-descriptor-catalog-and-measurement-roles), constituyen la lista oficial de descriptores para ambos ejes. Un descriptor indica **cómo** ocurrió el beneficio o daño verificado. Se aplican estas reglas:

- Los descriptores se acumulan y ninguno excluye a otro: un registro de posición puede incluir varios cuando los hechos verificados lo justifiquen.
- Están subordinados a la casilla: la casilla indica la magnitud del beneficio o daño; los descriptores añaden detalles sobre cómo ocurrió, pero nunca la reemplazan.
- Los descriptores enumerados constituyen una base, no la lista completa; el catálogo no descarta otros tipos de beneficio o daño.
- Las implementaciones pueden usar identificadores estables (IDs propios y fijos) asociados al catálogo, pero no deben crear una taxonomía incompatible cuyas categorías sean excluyentes, de manera que un registro de posición solo pueda llevar una.
- Antes de verificar los hechos, un descriptor alegado puede respaldar la preservación lícita de pruebas, la clasificación del caso o salvaguardias temporales.
- Solo puede consignarse un descriptor verificado como resultado de la Pregunta 2 o usarse para afectar la posición.

#### 3.1 Catálogo de descriptores de rutas de contribución y funciones de medición

<a id="benefit-route-descriptors-q1-measurement-role"></a>
<a id="benefit-route-descriptors-q1-classification-role"></a>
<a id="benefit-route-descriptors-q2-measurement-role"></a>

Estos son los descriptores de rutas de beneficio y lo que mide cada uno en la Pregunta 2 (¿qué tan bueno fue?). Se organizan en cinco ámbitos, con una tabla para cada uno; el catálogo de Violación de la [§3.2 Catálogo de descriptores de rutas de violación y funciones de medición](#32-violation-route-descriptor-catalog-and-measurement-roles) usa los mismos cinco ámbitos en el mismo orden. Su función en la Pregunta 3, la delegación segura, se establece en [Capítulo Trece §6.2 Umbrales de competencia y habilitaciones](core_13.000_standing_integration.md#62-competency-bars-and-clearances).

**Integridad del catálogo.** Si una implementación muestra varios descriptores en una fila o bajo una etiqueta, esa fila o etiqueta debe corresponder a cada descriptor aplicable. Este catálogo establece únicamente los nombres de los descriptores y lo que mide cada uno en la Pregunta 2. Las reglas de la Pregunta 3 (adjuntos, reparaciones, bloqueos, habilitaciones y otros efectos de posición) se encuentran únicamente en el Capítulo Trece.

##### 3.1.1 Seguridad corporal, relaciones, cuidados y capacidad de actuar

| **Descriptor de ruta de beneficio** | **Qué mide en la Pregunta 2** |
| --- | --- |
| **Paz corporal, mental o comunitaria** | Beneficio derivado de la calma corporal, psicológica y comunitaria. Ajusta cuánto importa el beneficio (su materialidad). |
| **Relaciones confiables** | Beneficio derivado de relaciones confiables, incluidas las basadas en un deber de confianza en contextos de desigualdad entre las partes. |
| **Cuidados y apoyo a la dependencia** | Cuidados verificados para sencientes que dependen de otros. También cuentan los cuidados informales cuando pueden demostrarse. |
| **Acceso e Inclusión** | Beneficio derivado de la participación efectiva y la accesibilidad. Ajusta cuánto importa el beneficio en contextos donde una parte depende mucho de la otra. |

##### 3.1.2 Reparación, propiedad y recursos

| **Descriptor de ruta de beneficio** | **Qué mide en la Pregunta 2** |
| --- | --- |
| **Beneficio reparador y restaurativo** | Beneficio derivado de reparar, compensar y reducir daños. |
| **Administración responsable de recursos** | Cuidado diligente de los recursos materiales y distribución confiable de estos. |

##### 3.1.3 Conocimiento, educación, registros y descubrimientos

| **Descriptor de ruta de beneficio** | **Qué mide en la Pregunta 2** |
| --- | --- |
| **Integridad de la infosfera** | Fortalecimiento de registros, transparencia y comunicaciones. |
| **Educación y desarrollo de capacidades** | Beneficio derivado del aprendizaje, la alfabetización y el crecimiento de la capacidad de los sencientes para actuar por sí mismos. La casilla depende del beneficio LEQU total. |
| **Contribución a STEM y los descubrimientos** | Descubrimientos que otros pueden reproducir e investigación que aumenta la seguridad. |

##### 3.1.4 Sistemas y funcionamiento constitucional

| **Descriptor de ruta de beneficio** | **Qué mide en la Pregunta 2** |
| --- | --- |
| **Optimización de sistemas** | Corrección de procesos que abarcan instituciones y reducción de riesgos. |
| **Alineación constitucional** | Fortalecimiento del Piso de Derechos y facilitación de la impugnación de decisiones. |

##### 3.1.5 Ecología y diligencia

| **Descriptor de ruta de beneficio** | **Qué mide en la Pregunta 2** |
| --- | --- |
| **Administración ecológica responsable** | Beneficio para los hábitats y la biodiversidad, y acciones responsables frente al clima. |
| **Diligencia** | Prevención de riesgos previsibles y supervisión competente. |

#### 3.2 Catálogo de descriptores de rutas de violación y funciones de medición

Estos son los descriptores de rutas de daño y lo que mide cada uno en la Pregunta 2 (¿qué tan grave fue?). Se organizan en cinco ámbitos, con una tabla para cada uno, usando los mismos cinco ámbitos y el mismo orden que en la [§3.1 Catálogo de descriptores de rutas de contribución y funciones de medición](#31-contribution-route-descriptor-catalog-and-measurement-roles). Para la Pregunta 3, las reglas de integración y adjuntos están en [Capítulo Trece §3 Integración de descriptores y normalización de adjuntos](core_13.000_standing_integration.md#3-descriptor-integration-and-attachment-normalization), y las reglas de prevención y diseño de bloqueos, en [Capítulo Trece §4.2 Prevención — bloqueos generales de posición](core_13.000_standing_integration.md#42-prevention--general-standing-locks) y [Capítulo Trece §5 Diseño y aplicación de bloqueos](core_13.000_standing_integration.md#5-lock-design-and-enforcement).

**Integridad del catálogo.** Si una implementación muestra varios descriptores en una fila o bajo una etiqueta, esa fila o etiqueta debe corresponder a cada descriptor aplicable. Este catálogo establece únicamente los nombres de los descriptores y lo que mide cada uno en la Pregunta 2. Las reglas de la Pregunta 3 (adjuntos, reparaciones, bloqueos, habilitaciones y otros efectos de posición) se encuentran únicamente en el Capítulo Trece.

##### 3.2.1 Seguridad corporal, relaciones, cuidados y capacidad de actuar

| **Descriptor de ruta de daño** | **Qué mide en la Pregunta 2** |
| --- | --- |
| **Conducta indebida violenta** | La violencia, la coacción o el peligro para la libertad se registran por separado de la casilla de impacto LEQU. Puede requerir salvaguardias reforzadas. |
| **Conducta indebida interpersonal o por incumplimiento del deber de cuidado** | El daño importa más (mayor materialidad) cuando una parte depende mucho de la otra. |
| **Conducta indebida por barreras de accesibilidad y participación** | El daño importa más (mayor materialidad) cuando una parte depende mucho de la otra; pueden acumularse factores agravantes. |
| **Conducta indebida sobre privacidad y autonomía personal** | Se aplican factores agravantes cuando se verifican ocultación o explotación, y pueden acumularse. |
| **Conducta indebida sobre capacidad de actuar y manipulación** | La coacción, la manipulación o el peligro para la libertad se registran por separado de la casilla de impacto. |

##### 3.2.2 Reparación, propiedad y recursos

| **Descriptor de ruta de daño** | **Qué mide en la Pregunta 2** |
| --- | --- |
| **Conducta indebida susceptible de corrección reparadora** | Registra el carácter corregible del daño (si puede subsanarse y cómo). La casilla depende de la pérdida LEQU total. |
| **Conducta indebida sobre la propiedad** | La ruta correspondiente a la pérdida de propiedad. La casilla depende de la pérdida LEQU total. |

##### 3.2.3 Conocimiento, educación, registros y descubrimientos

| **Descriptor de ruta de daño** | **Qué mide en la Pregunta 2** |
| --- | --- |
| **Conducta indebida contra la infosfera** | Daño a la Seguridad o la Verdad. La ocultación y el engaño siguen siendo hechos separados sobre cómo se causó el daño (su carácter). |
| **Conducta indebida educativa** | Daño al aprendizaje o a la capacidad de los sencientes para actuar por sí mismos (sus capacidades). La casilla depende de la pérdida LEQU total. |
| **Conducta indebida en investigación y descubrimientos** | Daño a la investigación o los descubrimientos. La casilla depende de la pérdida LEQU total. |

##### 3.2.4 Sistemas y funcionamiento constitucional

| **Descriptor de ruta de daño** | **Qué mide en la Pregunta 2** |
| --- | --- |
| **Conducta indebida sistémica** | La difusión (responsabilidad distribuida entre actores) y la habilitación estructural se registran por separado. La casilla depende de la pérdida LEQU total. |
| **Conducta indebida por obstrucción de la rendición de cuentas** | Abarca obstruir la rendición de cuentas: impedir que se exija responder por un daño. Se registra como una manera en que ocurrió el daño. La forma de llevar a cabo la obstrucción (por ejemplo, mediante ocultación o negligencia) se registra como hecho separado, y la casilla deriva de la pérdida LEQU total. Cuando la casilla está entre las más altas (véase [§4.1 Tabla 1 — etiquetas de visualización de casillas](#41-table-1--slot-display-labels)), el caso también puede registrarse como **Conducta Indebida Anticonstitucional** para remitirlo a la [Revisión de Conducta Indebida Anticonstitucional](core_05.035_band_accountability.md#anti-constitutional-misconduct-review) del Capítulo Catorce. La remisión no equivale a una designación de conducta indebida anticonstitucional: el Capítulo Catorce la decide por separado. |
| **Conducta indebida por salida y confinamiento** | Incluye las características de la Conducta Indebida Sistémica, además de difusión o captura cuando estas son estructurales (integradas en el funcionamiento del sistema). |
| **Conducta indebida por ciclo de vida e irreversibilidad** | La irreversibilidad afecta la magnitud de la pérdida LEQU. La ocultación o negligencia se registra por separado como carácter. |
| **Conducta Indebida Anticonstitucional** (descriptor) | Remite las violaciones de las casillas más altas (véase [§4.1 Tabla 1 — etiquetas de visualización de casillas](#41-table-1--slot-display-labels)) a la revisión de designación del Capítulo Catorce, sin cambiar su casilla de impacto. |

##### 3.2.5 Ecología y diligencia

| **Descriptor de ruta de daño** | **Qué mide en la Pregunta 2** |
| --- | --- |
| **Conducta indebida ecológica** | La pérdida LEQU se pondera según la pérdida de [Capacidad de Recuperación Ecológica](core_05.040_band_continuity.md#ecological-recovery-capacity) (capacidad de un ecosistema para regenerarse después de un daño). Puede acumularse con la ruta violenta (Conducta Indebida Violenta). |
| **Conducta indebida negligente** | El deber, la previsibilidad y la posibilidad de prevención se registran por separado de la casilla de impacto. |
