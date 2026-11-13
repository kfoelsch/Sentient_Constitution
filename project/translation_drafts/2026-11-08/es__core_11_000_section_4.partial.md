<!-- Borrador parcial de traducción al español. Fuente: commit 9c2c8c10c871d91157bcd27b9f56ad6a1cec90d3. Traducción asistida por IA; no revisada. Cobertura: Capítulo Once, §4 y subsecciones 4.1–4.5 solamente. -->

<a id="4-standing-record-operational-requirements"></a>

<a id="4-verification-and-record-requirements"></a>

### 4. Requisitos de verificación y registro

<details>
<summary><strong><span style="color: #2563eb;">Trazabilidad</span></strong></summary>

- Antecedentes: [§2](#2-question-1--what-happened) (*registros de la Pregunta 1 y guía de tipos de acontecimiento*); [Capítulos Dos a Cuatro](core_02.000_definition_structure.md) (*registro, verificación y trazabilidad de las definiciones hasta los resultados*).
- Derivaciones:
  - [§4.1](#41-minimum-record-contents) (*contenido mínimo*);
  - [§4.2](#42-related-standing-record-cross-references) (*referencias cruzadas*);
  - [§5](#5-record-custody-and-opening-authority) (*custodia del registro y autoridad para abrirlo*);
  - [§6](#6-handling-a-standing-record) (*gestión de un registro de posición*);
  - [Capítulo Doce §1](core_12.000_standing_measurement.md#1-question-2--how-good-or-bad-was-it) (*Pregunta 2*).
- Léase junto con: [CF-15.415 §8 Autoridad sobre información restringida](corpus_forum/cf_15.415_routing_operations_transfer_certification_representative_treatment.md#cf-15415-8-restricted-information-authority) (*primer paso para una disputa sobre un límite de divulgación indicado conforme a [§4.1](#41-minimum-record-contents)*).

</details>

<br>

*En términos sencillos: esta sección establece qué debe contener cada registro de posición, cómo se remiten entre sí los registros relacionados y cómo se versionan. Quién puede abrir y custodiar un registro de posición, y cómo puede impugnarse o corregirse, se explica en [§5 Custodia del registro y autoridad para abrirlo](#5-record-custody-and-opening-authority). Las mediciones de la Pregunta 2 solo pueden añadirse después de que se registre el fundamento fáctico verificado.*

El nivel de detalle exigido en materia de pruebas y registros puede aumentar según la importancia material y la clase del sistema. Esta escala no excluye del proceso de posición a ningún senciente, institución o sistema comprendido.

<a id="41-minimum-record-contents"></a>

#### 4.1 Contenido mínimo del registro

Un registro de posición incluye los campos que siguen; las dos últimas subsecciones añaden campos para cada eje. El filtro de insumos verificados, que determina qué puede alimentar un registro de posición, se establece en [§2.5 Filtro de insumos verificados](#25-verified-input-gate). La regla que mantiene separados los hechos de la Pregunta 1 y la medición de la Pregunta 2 figura en [§2.6 Límite entre etapas](#26-stage-boundary).

<a id="411-fields-every-standing-record-must-carry"></a>

##### 4.1.1 Campos obligatorios de todo registro de posición

Todo registro de posición debe incluir, como mínimo:

- el tipo de registro de posición: **registro de posición de contribución** o **registro de posición de violación**;
- a quién o a qué se evalúa y el alcance de la evaluación, incluidos los límites pertinentes del sistema, los límites de las funciones, las comunidades afectadas y las relaciones de dependencia;
- qué conducta o hallazgo se evalúa, incluidos los actos, las omisiones, los deberes, los efectos, el acontecimiento acotado, el patrón comprendido en el alcance, el registro de contribución o el hallazgo de violación en que se basa el registro de posición;
- el período del registro y el estado actual de revisión, por ejemplo, provisional, definitivo para un propósito declarado, impugnado, sustituido o pendiente de reevaluación programada;
- todo registro de posición relacionado que deba incluirse como referencia cruzada conforme a la **sección 4.2**;
- los registros oficiales, testimonios, mediciones, auditorías, decisiones de foros u otros materiales de verificación que permitan demostrar, revisar e impugnar el registro de posición conforme a los Capítulos Dos a Cuatro;
- la **autoridad para abrir el registro** que verificó el fundamento fáctico y autorizó la anotación, y el **custodio del registro** distinto que anotó y conserva el registro de posición; se debe identificar a ambos conforme a la **sección 5**;
- cómo impugnar el registro de posición, incluidos:
  - qué foro o autoridad lo revisa;
  - cualquier límite de divulgación; y
  - las condiciones para:
    - corregirlo;
    - restablecerlo;
    - dejarlo vencer; o
    - someterlo a revisión programada;
- los campos de medición de la Pregunta 2 específicos para cada eje que se exigen a continuación, una vez realizada la medición.

<a id="412-inspectable-attributable-action"></a>

##### 4.1.2 Acción atribuible inspeccionable

Las pruebas de acciones atribuibles se relacionan con el registro de posición de la siguiente manera:

- Para el personal o los agentes que ejercen Administración de Sistemas Críticos o autoridad operativa material, [CS-16.305 §10 Acción atribuible inspeccionable](corpus_systems/cs_16.305_critical_system_stewardship.md#cs-16305-103-inspectable-attributable-action) especifica pruebas reconstruibles de acciones atribuibles como contrato de registro predeterminado para equipos mixtos.
- Esas pruebas pueden alimentar este registro de posición.
- No sustituyen este registro de posición.
- Un registro de posición no incluye los pesos de un modelo de IA (los números internos del modelo) ni su razonamiento privado. La única excepción se da cuando no queda ningún otro medio para demostrar quién o qué fue responsable.
- Un asunto no queda fuera de la medición de posición solo porque involucre la privacidad de alguien o el estado interno protegido de un sistema. Sigue midiéndose cuando sea pertinente para un asunto de posición.

<a id="413-no-privacy-or-opacity-exemption"></a>

##### 4.1.3 Sin excepción por privacidad u opacidad

La privacidad, la confidencialidad o la opacidad del interior de un sistema no eximen un asunto de la medición de posición. Cuando estos elementos entran en conflicto con el requisito de un registro verificado, el conflicto se resuelve conforme a [Capítulo Uno §13.1 Principios fundamentales para las compensaciones](core_01.005_interaction_interpretation.md#131-core-tradeoff-principles) y a su disciplina de registros de decisión, preservando el acceso de revisores independientes.

<a id="414-additional-fields-for-contribution-standing-records"></a>

##### 4.1.4 Campos adicionales para los registros de posición de contribución

Los **registros de posición de contribución** también deben indicar:

- la medición de contribución de la Pregunta 2, incluidos:
  - la banda principal;
  - la casilla `s`, cuando se asigne (véase [Capítulo Doce §4 Gramática de casillas y escala compartida](core_12.000_standing_measurement.md#4-slot-grammar-and-shared-scaling));
  - el fundamento probatorio;
  - el razonamiento sobre materialidad; y
  - cualquier calibración LEQU o comparable adoptada y utilizada para brindar apoyo transparente;
- si la contribución es compartida, cómo se distribuyó el crédito, teniendo en cuenta:
  - el tiempo;
  - el esfuerzo;
  - la coordinación;
  - el mantenimiento;
  - la contribución causal; y
  - el trabajo de apoyo menos visible;
- la medición de contribución aquí registrada, en la que debe basarse todo efecto posterior sobre la posición conforme al Capítulo Trece.

<a id="415-additional-fields-for-violation-standing-records"></a>

##### 4.1.5 Campos adicionales para los registros de posición de violación

Los **registros de posición de violación** también deben indicar:

- la medición de violación de la Pregunta 2, incluidos:
  - la autoridad que emitió el hallazgo o el fundamento del registro;
  - el impacto LEQU;
  - la casilla `s`, cuando se asigne (véase [Capítulo Doce §4 Gramática de casillas y escala compartida](core_12.000_standing_measurement.md#4-slot-grammar-and-shared-scaling));
  - el carácter del proceso o de la respuesta, cuando corresponda; y
  - todo estado de designación conforme al Capítulo Catorce;
- cuando varios actores compartan o dividan la responsabilidad por una violación, los motivos verificados de toda posición adversa registrada contra un actor determinado, incluidos:
  - el papel causal;
  - el deber;
  - la autoridad;
  - el control;
  - la previsibilidad;
  - el beneficio;
  - el ocultamiento; o
  - la capacidad viable de prevención;
- cuando el hallazgo de violación implique una omisión de divulgación ante un foro o un fallo intencional en el proceso de recusación (para la disciplina de medición, léase **§8.2.2** (*Cómo se registra la forma en que se causó un daño*)):
  - el fundamento verificado de la omisión o del fallo;
  - el deber de divulgación o recusación incumplido;
  - el conocimiento, la imprudencia o la intención del actor, cuando se haya determinado; y
  - si la conducta afectó materialmente:
    - la legalidad del panel;
    - la independencia;
    - la impugnación de la recusación;
    - la integridad de las pruebas;
    - el plazo de reparación;
    - la derivación alternativa; o
    - la posibilidad práctica de impugnar;
- la medición de violación aquí registrada, en la que debe basarse todo efecto posterior sobre la posición conforme al Capítulo Trece.

<a id="42-related-standing-record-cross-references"></a>

#### 4.2 Referencias cruzadas entre registros de posición relacionados

Si un registro de posición de contribución y uno de violación se refieren al mismo sujeto, se superponen en el tiempo o tratan del mismo acontecimiento, patrón o decisión, cada uno debe remitir al otro.

Cada referencia cruzada debe identificar, como mínimo:

- el registro de posición relacionado y si es un registro de contribución o de violación;
- por qué están vinculados los dos registros de posición, incluidos los casos en que un hallazgo de violación refuta, corrige o limita una contribución alegada conforme a la **sección 2.4**;
- qué tienen en común los dos registros de posición: el sujeto, acontecimiento, patrón o decisión; y
- de qué manera se superponen sus períodos o los asuntos que abarcan.

Las referencias cruzadas:

- deben seguir siendo auditables e impugnables;
- no deben sustituir la medición separada;
- no deben crear una puntuación combinada; y
- no deben dar la impresión de que los dos registros de posición abarcan los mismos asuntos o períodos cuando no es así.

<a id="43-collective-and-actor-specific-records"></a>

#### 4.3 Registros colectivos y específicos de actores

Cuando varios sencientes o entidades compartan el mismo beneficio o la misma violación, el sistema puede conservar tanto un registro de posición colectivo como registros separados y específicos de cada actor. Se aplican estas reglas:

- Los hallazgos de contribución y violación deben permanecer en registros de posición separados conforme a la **sección 2.1**.
- En el caso del crédito compartido, el reconocimiento debería corresponder a lo que cada senciente aportó realmente, teniendo en cuenta:
  - la función;
  - el tiempo;
  - el esfuerzo;
  - el riesgo;
  - la habilidad;
  - la coordinación;
  - el mantenimiento; y
  - el impacto causal.
- Cuando muchas personas sencientes hayan ayudado y no sea posible separar claramente las partes individuales, se favorece una distribución amplia.
- En el caso de violaciones compartidas, la culpa no debe atribuirse únicamente por pertenecer a un grupo.
- Una posición adversa específica de un actor requiere un vínculo verificado con:
  - el papel causal;
  - el deber;
  - la autoridad;
  - el control;
  - la previsibilidad;
  - el beneficio;
  - el ocultamiento; o
  - la capacidad viable de prevención.

<a id="44-versioning"></a>

#### 4.4 Versionado

Los registros de posición deben versionarse cuando cambie cualquiera de los siguientes elementos:

- hechos importantes;
- hallazgos;
- resultados de revisión;
- estado de reparación;
- pruebas de contribución;
- calibración de implementación; o
- reglas constitucionales.

Una versión posterior puede:

- actualizar el registro de posición para el futuro;
- corregirlo retroactivamente si era incorrecto;
- dejarlo vencer respecto de un contexto decisorio ya concluido; o
- sustituirlo para un nuevo contexto decisorio.

La versión posterior debe conservar la pista de auditoría previa y explicar qué cambió, quién realizó el cambio, bajo qué autoridad de apertura o custodia conforme a la **sección 5**, con base en qué materiales de verificación y a petición de quién.

<a id="45-implementation-tools"></a>

#### 4.5 Herramientas de implementación

Los equipos pueden crear herramientas prácticas para los registros de posición, incluidos:

- campos de datos;
- etiquetas;
- umbrales;
- formularios;
- paneles de control;
- pasos de revisión; y
- **medidas estándar de contribución** publicadas para tareas recurrentes conforme a la **sección 13**.

Esas herramientas deben mantener separados, visibles e impugnables los campos exigidos por la **sección 4.1**. No deben ocultar esos campos dentro de una puntuación opaca o una etiqueta escondida.

