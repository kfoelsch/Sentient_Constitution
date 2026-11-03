##### 5.3.4 Integridad de mapas y registros

Antes de basarse en los mapas de dependencias y registros de flujos de recursos, la certificación debe comprobar que cumplan el **Artículo V-A** (*Mapeo de dependencias y transparencia de flujos de recursos*). Deben ser:

- **Completos:** abarcan las dependencias importantes anteriores y posteriores, los flujos de recursos y las relaciones ocultas o desequilibradas, cuando sean pertinentes.
- **Actuales:** se actualizan con la frecuencia necesaria según la rapidez de los cambios y la importancia crítica del sistema, incluida su clase conforme a [§2 Evaluación de la clase del sistema](#2-system-class-evaluation). Muestran el sistema tal como funciona ahora, no como funcionaba en la última certificación.
- **Auditables:** están abiertos a auditoría conforme al **Artículo XVI-A** (*Auditabilidad y pruebas observables*).

Un mapa o registro que no supere cualquiera de estas pruebas no puede respaldar una conclusión de que el sistema devuelve apoyo suficiente. La deficiencia debe quedar registrada y tratarse conforme a *Defectos y desalineación* más adelante.

<a id="535-system-class-scaling-and-escalation"></a>
##### 5.3.5 Escalamiento y escalada por clase del sistema

La clase del sistema determina la profundidad de la revisión y el rigor con que se juzga la suficiencia. Nunca hace que una extracción compartida sea demasiado pequeña para contar, y la extracción distribuida entre entidades, registros o períodos se evalúa como una sola, conforme al [Capítulo Uno §15.1.1 Principio contra la segmentación](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle). Siempre que se active el desencadenante de materialidad:

- Un sistema que recurra a un fundamento compartido que los seres sintientes necesitan para sobrevivir —como una cuenca hidrográfica compartida o la columna vertebral de una red eléctrica regional— debe incorporar las pruebas más sólidas sobre mapas de dependencias y flujos de retorno. Se trata de sistemas compartidos cuya capacidad duradera protege [Capítulo Uno §9 Capacidad de los sistemas compartidos](core_01.000_values_principles.md#9-shared-system-capacity), y aquí las pruebas son más sólidas por el **Artículo III-A** (*Supervivencia*).
- Un sistema que dependa de infraestructura compartida de autenticación, tecnología de información sanitaria u otra similar debe documentar qué toma y si su apoyo es suficiente, con profundidad acorde con la importancia crítica de sus operaciones. Los eslóganes vagos sobre «interoperabilidad» no cuentan: la dependencia debe verse en los mapas y registros, como exige [Capítulo Uno §18.5 Arquitectura modular y disciplina de dependencias](core_01.010_stewardship_capacity_principles.md#185-modular-architecture-and-dependency-discipline).
- Un sistema no puede eludir la revisión entre sistemas mientras se convierte silenciosamente en el punto de estrangulamiento de pagos, identidad o dotación de personal para instituciones que no pueden cambiarlo de forma realista.
  - **Quiénes no pueden cambiar:** se determina conforme a los factores de sustituibilidad de [§5.3.3 Requisito de evaluación](#533-evaluation-requirement).
  - **Por qué importa:** este es el tipo de concentración que describe [Capítulo Uno §11.4 Concentración de recursos y dependencia](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable). Indica a quienes adoptan el sistema que establezcan niveles, por ejemplo, cuántos seres sintientes o sistemas dependen de un proveedor sin alternativa real, o quién controla las interfaces y los puntos de acceso a infraestructuras compartidas. La certificación no espera a que se supere el nivel establecido por quien adopta el sistema para intensificar la revisión (véase más adelante).
  - **Qué hace la certificación:** intensifica la revisión y reconsidera la clase del sistema conforme a [§2.2 Cómo la clase del sistema escala cada evaluación](#22-how-system-class-scales-every-evaluation), hasta la **Clase A** cuando el sistema controle el acceso a coordinación esencial para sobrevivir.

La intensificación no espera a que se supere un umbral de concentración fijado conforme a [Capítulo Uno §11.4 Concentración de recursos y dependencia](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable). Que exista un umbral establecido por quien adopta el sistema y que el sistema lo haya superado constituye más evidencia. La falta de un umbral o que este sea demasiado alto no retrasa la intensificación, y superar un umbral no constituye por sí solo una conclusión de conducta indebida.

<a id="536-defects-and-misalignment"></a>
##### 5.3.6 Defectos y desalineación

Los defectos de [§5](#5-rights-floor-and-domain-evaluations) (*Evaluaciones del Piso de Derechos y por ámbito*) se aplican a esta evaluación, incluida la información sobre dependencias o flujos de recursos que el sistema debe divulgar conforme al **Artículo V-A** (*Mapeo de dependencias y transparencia de flujos de recursos*). Además, cada situación siguiente cuenta como defecto de certificación:

- tratar cualquiera de las siguientes cosas como suficiente para satisfacer [Apoyo proporcional entre sistemas](core_05.040_band_continuity.md#proportionate-cross-system-support):
  - transferencias simbólicas, opacas, fuera del mapa o puntuales;
  - el hecho de que un sistema alcance el piso de supervivencia del **Artículo III-A** (*Supervivencia*); o
  - el hecho de que un sistema se mantenga dentro de los límites de concentración de mercado de [Capítulo Uno §11 Estructura del mercado](core_01.000_values_principles.md#11-market-structure);
- extraer reiteradamente recursos de fundamentos compartidos sin devolverlos en proporción cuando se active el desencadenante de materialidad;
- apoyo que consolida principalmente la captura o la concentración; y
- apoyo sujeto a condiciones que anulan la transparencia exigida por el **Artículo V-A** (*Mapeo de dependencias y transparencia de flujos de recursos*).

Las deficiencias documentadas de apoyo cuentan conforme a [Capítulo Uno §6 Confianza y confiabilidad](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity).

<a id="54-nondiscrimination-evaluation"></a>

#### 5.4 Evaluación de no discriminación

<details>
<summary><strong><span style="color: #2563eb;">Trazabilidad</span></strong></summary>

- Fuentes previas:
  - [Parte C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*contenido del registro*);
  - [§2](#2-system-class-evaluation) (*evaluación de la clase del sistema*); familia de medición de Participación (*Equidad sustantiva y uso de características protegidas como indicadores indirectos e impacto dispar como medición constitucional*); **Artículo VI-C** (*No discriminación*);
  - [Equidad sustantiva](core_05.055_band_participation.md#substantive-fairness),
  - [Características protegidas](core_05.055_band_participation.md#protected-characteristics),
  - [Uso de características protegidas como indicadores indirectos e impacto dispar](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact),
  - [Idioma, cultura y patrimonio](core_05.040_band_continuity.md#language-culture-and-heritage),
  - [Necesidad](core_05.035_band_accountability.md#necessity), y
  - [Proporcionalidad](core_05.035_band_accountability.md#proportionality) (Capítulo Cinco).
- Fuentes previas: Principios del Capítulo Uno
  - [§3.1 Equidad](core_01.000_values_principles.md#31-fairness) (especialmente [§3.1.2 Beneficios y cargas](core_01.000_values_principles.md#312-benefits-and-burdens)) y
  - [§11.4 Concentración de recursos y dependencia](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (*control de acceso; intensificación en §5.4.2*).
- Desarrollos posteriores:
  - [CS-9.320 §9](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class) (*Aplicación ilustrativa de la no discriminación según la clase del sistema*);
  - [Parte C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*integridad del registro*);
  - [Parte C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*compuerta de entradas verificadas*);
  - [Parte B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*desalineación por patrones discriminatorios y evasión mediante indicadores indirectos*).
- Leer junto con: deber de adjudicación y operaciones del **Artículo VI-C** (*No discriminación*) cuando la certificación condicione el acceso a foros, instancias administrativas o mecanismos de aplicación; [*Estado de la no discriminación, características protegidas, dignidad, condicionamiento por señales íntimas y el **Artículo VII-E** (*Servicios sexuales comerciales consentidos entre adultos y explotación sexual*)*](core_05.055_band_participation.md#fairness-protected-characteristics-and-nondiscrimination).
- Subsecciones:
  - [§5.4.1](#541-evaluation-requirement) (*requisito de evaluación*);
  - [§5.4.2](#542-system-class-scaling-and-escalation) (*escalamiento y escalada por clase del sistema*);
  - [§5.4.3](#543-defects-and-misalignment) (*defectos y desalineación*);
  - [CS-9.320 §9](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class) (*Aplicación ilustrativa de la no discriminación según la clase del sistema*).

</details>

<br>

*En términos sencillos: algunos sistemas deciden quién puede entrar. Otros deciden quién paga más, quién queda peor clasificado o quién soporta una carga mayor. Cuando el sistema toma decisiones importantes de ese tipo, la certificación plantea una pregunta: ¿el daño recae principalmente en seres sintientes con características protegidas o en rasgos que las sustituyen? La afirmación del operador de que sus reglas son neutrales no responde a esa pregunta. Ejemplos prácticos: [CS-9.320 §9 Aplicación ilustrativa de la no discriminación según la clase del sistema](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class).* 

Esta sección se aplica cuando un sistema de impacto material clasifica, ordena, fija precios, condiciona el acceso, excluye o distribuye cargas y beneficios entre seres sintientes de manera material, incluso mediante reglas de elegibilidad, características del modelo, lógica de clasificación, políticas de plataforma o vías de decisión comparables.

La certificación de alineación del sistema debe evaluar la **no discriminación** conforme al **Artículo VI-C** (*No discriminación*), la [Equidad sustantiva](core_05.055_band_participation.md#substantive-fairness) y el [Uso de características protegidas como indicadores indirectos e impacto dispar](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact) cuando se active el desencadenante de materialidad.

<a id="541-evaluation-requirement"></a>
##### 5.4.1 Requisito de evaluación

*En términos sencillos: este capítulo no establece cuotas de inclusión ni selecciona una fórmula de equidad. Otros documentos pueden hacerlo, al igual que futuras incorporaciones al corpus o los documentos que redacte quien adopte el sistema. La certificación solo comprueba que alguien haya examinado realmente quién recibe los beneficios, quién soporta las cargas y si se usan indicadores indirectos de rasgos protegidos. La evaluación se aplica siempre que se active el desencadenante.*

El proceso de certificación debe determinar si las vías de decisión del sistema de las que se depende materialmente imponen cargas, exclusiones o daños materiales a los seres sintientes por cualquiera de los siguientes motivos:

- [Características protegidas](core_05.055_band_participation.md#protected-characteristics);
- sus indicadores indirectos; o
- agrupaciones arbitrarias que funcionen como sustitutos, incluidas las especializaciones de idioma, cultura y patrimonio conforme a [Idioma, cultura y patrimonio](core_05.040_band_continuity.md#language-culture-and-heritage).

La evaluación debe, en proporción al [interés material](core_00.000_preamble.md#material-stake):

- examinar patrones de cargas y beneficios conforme a [Equidad sustantiva](core_05.055_band_participation.md#substantive-fairness); y
- examinar el riesgo de uso de indicadores indirectos o de impacto dispar conforme a [Uso de características protegidas como indicadores indirectos e impacto dispar](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact).

El trato diferenciado solo es aceptable cuando lo justifiquen una [Necesidad](core_05.035_band_accountability.md#necessity) documentada, la [Proporcionalidad](core_05.035_band_accountability.md#proportionality) y la equidad sustantiva. La evaluación debe reflejar el efecto funcional, no solo la neutralidad aparente, la intención declarada o una etiqueta.

<a id="542-system-class-scaling-and-escalation"></a>
##### 5.4.2 Escalamiento y escalada por clase del sistema

La clase del sistema determina la profundidad de la evaluación. No permite tratar como irrelevante la clasificación o transferencia de cargas. Siempre que se active el desencadenante de materialidad, se aplica lo siguiente:

- **Sistemas cuyas reglas de desconexión, notificación u otras similares puedan impedir el acceso a elementos esenciales para sobrevivir:**
  - el registro debe contener el análisis más sólido de cargas, beneficios e indicadores indirectos, no una declaración general de buenas prácticas; y
  - la transferencia oculta de costos no satisface [Capítulo Uno §3.1.2 Beneficios y cargas](core_01.000_values_principles.md#312-benefits-and-burdens).
- **Sistemas cuya lógica de emparejamiento o encaminamiento afecta la atención de emergencia, las prestaciones o el acceso a credenciales:**
  - el registro debe documentar hallazgos sobre impacto dispar y equidad sustantiva conforme a la importancia operativa; y
  - esto se debe a que la equidad de [Capítulo Uno §3.1 Equidad](core_01.000_values_principles.md#31-fairness) exige que no se someta a los seres sintientes a reglas inexplicadas ni se les impongan costos que otros evitan.
- **Sistemas cuya lógica de turnos, proveedores o reservas clasifica o excluye materialmente a participantes:**
  - el sistema no puede sustituir un análisis real con un párrafo superficial sobre equidad;
  - cuando la coordinación sea esencial para sobrevivir, la certificación debe intensificar la revisión y reconsiderar la clasificación conforme a [§2.2 Cómo la clase del sistema escala cada evaluación](#22-how-system-class-scales-every-evaluation), incluida la reclasificación a **Clase A** cuando el sistema condicione la dotación de personal o el encaminamiento de emergencias; y
  - ese tipo de control de acceso es un indicador de concentración conforme a [Capítulo Uno §11.4 Concentración de recursos y dependencia](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable), pues muchos seres sintientes o sistemas dependen de un proveedor sin alternativa real; por eso la certificación intensifica aquí la revisión.

<a id="543-defects-and-misalignment"></a>
##### 5.4.3 Defectos y desalineación

Se aplican dos conjuntos de defectos a esta evaluación:

- **Defectos aplicables a toda la sección:**
  - se aplican a esta evaluación los defectos de [§5](#5-rights-floor-and-domain-evaluations) (*Evaluaciones del Piso de Derechos y por ámbito*); y
  - se aplican a la lógica material de clasificación, ordenamiento o asignación de cargas cuando el **Artículo VI-C** (*No discriminación*) exija revisarla.
- **Defectos de no discriminación:** también debe tratarse como defecto de certificación cada una de las siguientes situaciones:
  - considerar suficiente la neutralidad aparente, las métricas agregadas de conveniencia o la declaración del operador sin un análisis evaluable de cargas y beneficios; y
  - invocar la homogeneización, interoperabilidad o eficiencia para anular las protecciones de idioma, cultura o patrimonio sin satisfacer las pruebas de **Necesidad** y **Proporcionalidad** del **Artículo VI-C** (*No discriminación*).

La discriminación documentada mediante indicadores indirectos o la inequidad sustantiva cuentan conforme a [Capítulo Uno §6 Confianza y confiabilidad](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity).

<a id="55-accessibility-evaluation"></a>

#### 5.5 Evaluación de accesibilidad

<details>
<summary><strong><span style="color: #2563eb;">Trazabilidad</span></strong></summary>

- Fuentes previas:
  - [Parte C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*contenido del registro*);
  - [§2](#2-system-class-evaluation) (*evaluación de la clase del sistema*); familia de medición de Participación (*la accesibilidad como medición constitucional*); **Artículo VI-D** (*Accesibilidad*);
  - [Accesibilidad](core_05.055_band_participation.md#accessibility),
  - [Materialidad](core_05.050_band_oversight.md#materiality),
  - [Dependencia](core_05.040_band_continuity.md#dependency),
  - [Agencia significativa](core_05.055_band_participation.md#meaningful-agency),
  - [Características protegidas](core_05.055_band_participation.md#protected-characteristics),
  - [Uso de características protegidas como indicadores indirectos e impacto dispar](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact),
  - [Equidad sustantiva](core_05.055_band_participation.md#substantive-fairness),
  - [Necesidad](core_05.035_band_accountability.md#necessity), y
  - [Proporcionalidad](core_05.035_band_accountability.md#proportionality) (Capítulo Cinco).
- Fuentes previas: Principios del Capítulo Uno
  - [§3.1.5 Capacidad actual y ayuda proactiva](core_01.000_values_principles.md#315-present-capability-and-proactive-help) (*necesidades cambiantes en §5.5.2; salvaguardias ante falta de respuesta en §5.5.3*),
  - [§7.1 Disciplina de limitación](core_01.000_values_principles.md#71-limitation-discipline),
  - [§5.2 Accesibilidad en lenguaje claro](core_01.000_values_principles.md#52-plain-language-accessibility-participation-and-stewardship-duty), y
  - [§11.4 Concentración de recursos y dependencia](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (*control de acceso; intensificación en §5.5.3*).
- Desarrollos posteriores:
  - [CS-9.320 §10](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-10-illustrative-accessibility-application-by-system-class) (*Aplicación ilustrativa de la accesibilidad según la clase del sistema*);
  - [Parte C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*integridad del registro*);
  - [Parte C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*compuerta de entradas verificadas*);
  - [Parte B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*desalineación de accesibilidad y adaptaciones solo sobre el papel*).
- Leer junto con: **Artículo IV-A** (*Igualdad de acceso a la educación*) cuando haya implicación de accesibilidad educativa —la accesibilidad específica de la educación sigue bajo su titularidad—; **Artículo III-A** (*Supervivencia*) cuando los pasos de facturación, cobro o desconexión puedan terminar el acceso a elementos esenciales para sobrevivir —el requisito de notificación significativa que sustenta las salvaguardias por falta de respuesta de [§5.5.3](#553-system-class-scaling-and-escalation)—; **Artículo VI-C** (*No discriminación*) (adjudicación y operaciones) y **Artículo XII** (*Participación de las partes interesadas, representación y debido proceso en el sistema*) cuando la certificación condicione la participación en foros, procesos administrativos, participación de partes interesadas o aplicación de normas; [Capítulo Nueve §5.5](#55-accessibility-evaluation) (*referencia transversal al factor de evaluación de accesibilidad*).
- Subsecciones:
  - [§5.5.1](#551-evaluation-requirement) (*requisito de evaluación*);
  - [§5.5.2](#552-profiles-in-scope) (*perfiles dentro del alcance*);
  - [§5.5.3](#553-system-class-scaling-and-escalation) (*escalamiento y escalada por clase del sistema*);
  - [§5.5.4](#554-defects-and-misalignment) (*defectos y desalineación*);
  - [CS-9.320 §10](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-10-illustrative-accessibility-application-by-system-class) (*Aplicación ilustrativa de la accesibilidad según la clase del sistema*).

</details>

<br>

*En términos sencillos: cuando un sistema controla materialmente si los seres sintientes pueden participar de verdad —y no solo si una puerta lleva la etiqueta «abierta»—, la certificación debe comprobar que la participación sea realmente posible según las necesidades sensoriales, cognitivas, de movilidad, comunicación e interfaz de sustrato, entre otras. Los catálogos de adaptaciones y normas de interfaz pueden estar en otros documentos, incorporaciones posteriores al corpus o documentos de adopción; la certificación comprueba que se haya evaluado la participación sustantiva cuando se active el desencadenante. Ejemplos prácticos: [CS-9.320 §10 Aplicación ilustrativa de la accesibilidad según la clase del sistema](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-10-illustrative-accessibility-application-by-system-class).* 

Esta sección se aplica cuando un sistema con gran efecto en la vida de los seres sintientes controla si pueden participar realmente en algo que protege la Constitución, como:

- gobernanza, participación de las partes interesadas, adjudicación y operaciones;
- elementos esenciales para sobrevivir y atención de salud;
- expresión, reunión y prensa; o
- ámbitos comparables.

El control puede ejercerse mediante:

- interfaces, espacios o programación;
- credenciales o acceso a capacidad de cómputo;
- el diseño de las adaptaciones; o
- vías similares.

La accesibilidad en la educación sigue bajo el **Artículo IV-A** (*Igualdad de acceso a la educación*); nada de lo dispuesto aquí la restringe.

Cuando corresponda, la certificación debe evaluar la **accesibilidad** conforme al **Artículo VI-D** (*Accesibilidad*) y [Accesibilidad](core_05.055_band_participation.md#accessibility). Esta sección no establece:

- listas de adaptaciones;
- normas de interfaz;
- especificaciones de diseño universal; ni
- procedimientos cotidianos para ofrecer adaptaciones.

Estos temas se encuentran en otros documentos que pueden incorporarse.

<a id="551-evaluation-requirement"></a>
##### 5.5.1 Requisito de evaluación

La certificación debe comprobar si los seres sintientes pueden participar realmente en los ámbitos que controla el sistema, no solo si existen prestaciones formales, interfaces predeterminadas o adaptaciones en el papel. Debe probar el efecto real en la participación conforme a [Accesibilidad](core_05.055_band_participation.md#accessibility), escalada según la [Materialidad](core_05.050_band_oversight.md#materiality) y la [Dependencia](core_05.040_band_continuity.md#dependency).

Quienes revisan deben prestar atención a:

- adaptaciones que solo existen en el papel;
- afirmaciones de «acceso general» que dependen de prestaciones predeterminadas, pero no permiten que nadie participe realmente;
- argumentos de que el sistema solo es parcialmente material, utilizados para reducir las adaptaciones que debe proporcionar;
- exclusión que contraviene la [No exclusión de los seres sintientes](core_05.055_band_participation.md#sentience-non-exclusion); y
- diseños que excluyen indirectamente a los seres sintientes mediante la programación, elección de espacios, acreditación, acceso al cómputo u otros mecanismos similares (denegación por indicadores indirectos).

La certificación también debe aplicar las [Características protegidas](core_05.055_band_participation.md#protected-characteristics) y el [Uso de características protegidas como indicadores indirectos e impacto dispar](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact) al diseño de las adaptaciones. Toda limitación de adaptaciones debe documentarse y satisfacer la [Necesidad](core_05.035_band_accountability.md#necessity), la [Proporcionalidad](core_05.035_band_accountability.md#proportionality) y la [Equidad sustantiva](core_05.055_band_participation.md#substantive-fairness).

<a id="552-profiles-in-scope"></a>
##### 5.5.2 Perfiles dentro del alcance

La evaluación debe probar la participación real, no el cumplimiento sobre el papel, para cada forma de ser sintiente y perfil de capacidades dentro del alcance conforme a [Accesibilidad](core_05.055_band_participation.md#accessibility):

- **Perfiles pertinentes:** perfiles sensoriales, cognitivos, de movilidad y de comunicación; perfiles relativos a la conexión del ser sintiente mediante su sustrato (**interfaz de sustrato**) o mediante computación (**interfaz de cómputo**); y perfiles comparables.
- **Cómo cambian las necesidades con el tiempo:** los perfiles pueden ser **constantes** (permanecen iguales), **episódicos** (aparecen y desaparecen) o **evolutivos** (cambian a medida que el ser sintiente se desarrolla). Los tres reciben el mismo tratamiento, y cada uno se juzga según lo que el ser sintiente puede hacer ahora, no según lo que podía hacer antes ni según una etiqueta, conforme a [Capítulo Uno §3.1.5 Capacidad actual y ayuda proactiva](core_01.000_values_principles.md#315-present-capability-and-proactive-help).
- **Lo que no satisface esta sección:**
  - una afirmación de **acceso general**, cuando el acceso parece amplio en conjunto, pero deja a un grupo concreto de seres sintientes afectados sin acceso real; y
  - el **escalamiento de materialidad selectiva**, que sostiene que el sistema solo es parcialmente material para reducir las adaptaciones debidas y dejar a los seres sintientes por debajo del nivel de participación protegido por el **Artículo VI-D** (*Accesibilidad*).

<a id="553-system-class-scaling-and-escalation"></a>
##### 5.5.3 Escalamiento y escalada por clase del sistema

La clase del sistema modifica la profundidad de la evaluación. Nunca permite tratar como suficientes las adaptaciones en el papel o las interfaces predeterminadas. Siempre que se active el desencadenante de materialidad:

- Si las vías de facturación o interrupción del sistema pudieran privar a los seres sintientes de elementos esenciales para sobrevivir, el registro debe mostrar las pruebas más sólidas de que realmente pueden participar. No basta con una declaración general sobre accesibilidad. Toda barrera que los excluya requiere una justificación conforme a [Capítulo Uno §7.1 Disciplina de limitación](core_01.000_values_principles.md#71-limitation-discipline), y las notificaciones de facturación e interrupción deben redactarse para que los seres sintientes puedan leerlas y actuar conforme a [Capítulo Uno §5.2 Accesibilidad en lenguaje claro](core_01.000_values_principles.md#52-plain-language-accessibility-participation-and-stewardship-duty).
- Si los procesos de facturación, cobro o desconexión del sistema pudieran privar a los seres sintientes de elementos esenciales para sobrevivir cuando dejen de pagar o de responder, el registro debe mostrar cómo protege a quienes no pueden responder, cualquiera que sea el motivo, incluidas afecciones cognitivas o de salud mental como la depresión grave. El sistema no necesita saber por qué un ser sintiente guarda silencio. Esto aplica [Capítulo Uno §3.1.5 Capacidad actual y ayuda proactiva](core_01.000_values_principles.md#315-present-capability-and-proactive-help) a la facturación, el cobro y la desconexión. El silencio no es consentimiento ni una decisión de renunciar al servicio. Una notificación ante la que un ser sintiente no puede actuar no es la notificación significativa que exige [**Artículo III-A** (*Supervivencia*)](core_06.000_rights_part_a.md#article-iii-a-survival) antes de terminar una relación esencial. El registro debe mostrar:
  - más de una forma de contactar al ser sintiente, con seguimiento que no dependa de un canal que ya no haya recibido respuesta;
  - una forma para que los seres sintientes elijan por anticipado a un ser sintiente de confianza o defensor a quien contactar antes de cualquier desconexión, compartiendo solo la información necesaria para obtener respuesta;
  - contacto activo antes de cualquier desconexión, mediante el cual el sistema procure conectar al ser sintiente con ayuda (por ejemplo, un servicio de apoyo o cuidado, o el contacto elegido por la persona), en vez de esperar a que pida ayuda;
  - una revisión por parte de un revisor que sea ser sintiente, y no solo un proceso automatizado, antes de desconectar elementos esenciales para sobrevivir por falta de respuesta. La revisión se basa en lo que el sistema puede observar (los contactos sin respuesta y lo que está en juego), no en conjeturas sobre la salud o el estado mental del ser sintiente; y
  - una vía rápida y de baja barrera para recuperar el servicio y acordar el pago, de modo que un período de silencio no se convierta en una pérdida permanente.
- Si los portales de un sistema controlan el acceso a la atención de salud, debe documentar sus hallazgos sobre adaptaciones y denegación mediante indicadores indirectos. Cuanto más críticas sean las operaciones, más detalle se requiere.
- Un sistema no puede conformarse con un párrafo superficial sobre accesibilidad mientras sus interfaces de turnos, reservas o proveedores excluyen materialmente a participantes. Cuando la coordinación del sistema se vuelva esencial para sobrevivir, la certificación debe revisarlo más detenidamente y reconsiderar su clase conforme a [§2.2 Cómo la clase del sistema escala cada evaluación](#22-how-system-class-scales-every-evaluation). Esto incluye elevarlo hacia la **Clase A** cuando se condicione la dotación de personal o el encaminamiento de emergencias. Las interfaces que los seres sintientes no pueden evitar de forma realista son el control de acceso que identifica [Capítulo Uno §11.4 Concentración de recursos y dependencia](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable).

<a id="554-defects-and-misalignment"></a>
##### 5.5.4 Defectos y desalineación

Los defectos de [§5](#5-rights-floor-and-domain-evaluations) (*Evaluaciones del Piso de Derechos y por ámbito*) se aplican a esta evaluación. Además, cada una de las siguientes situaciones debe tratarse como defecto de certificación:

- tratar prestaciones formales, interfaces predeterminadas o adaptaciones sobre el papel como suficientes sin analizar de forma evaluable la participación sustantiva;
- invocar el costo, las decisiones de diseño, la clase de sustrato o la escala operativa para anular el piso de participación sin satisfacer las pruebas de **Necesidad** y **Proporcionalidad** del **Artículo VI-D** (*Accesibilidad*);
- diseñar la operación de modo que se anule la accesibilidad cuando sea viable una opción menos gravosa; y
- tratar el silencio o la falta de pago de un ser sintiente como consentimiento, rechazo o decisión de renunciar al servicio y desconectar elementos esenciales para sobrevivir sin las salvaguardias que debe mostrar el registro conforme a [§5.5.3 Escalamiento y escalada por clase del sistema](#553-system-class-scaling-and-escalation).

Las barreras documentadas a la participación cuentan conforme a [Capítulo Uno §6 Confianza y confiabilidad](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity).

<a id="56-trustworthiness-and-system-reliance-integrity-evaluation"></a>

#### 5.6 Evaluación de confiabilidad e integridad de la confianza en el sistema

<details>
<summary><strong><span style="color: #2563eb;">Trazabilidad</span></strong></summary>

- Fuentes previas:
  - [Parte C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*contenido del registro*);
  - [§2](#2-system-class-evaluation) (*evaluación de la clase del sistema*); familia de medición de Supervisión (*Verdad e integridad epistémica; confiabilidad, degradación de la confianza y confianza engañosa como mediciones constitucionales*); **Artículo XIII** (*Derecho a sistemas fiables y dignos de confianza*);
  - [Confiabilidad](core_05.040_band_continuity.md#trustworthiness),
  - [Confianza](core_05.040_band_continuity.md#trust),
  - [Degradación de la confianza y confianza engañosa](core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance),
  - [Impugnabilidad](core_05.035_band_accountability.md#contestability),
  - [Resarcimiento y reparación](core_05.035_band_accountability.md#redress-and-remediation),
  - [Alineación de incentivos](core_05.045_band_integrative.md#incentive-alignment),
  - [Reversibilidad](core_05.040_band_continuity.md#reversibility),
  - [Materialidad](core_05.050_band_oversight.md#materiality),
  - [Dependencia](core_05.040_band_continuity.md#dependency), y
  - [Riesgo](core_05.040_band_continuity.md#risk) (Capítulo Cinco).
- Fuentes previas: Principios del Capítulo Uno
  - [§3.1.5 Capacidad actual y ayuda proactiva](core_01.000_values_principles.md#315-present-capability-and-proactive-help) (*vías de impugnación y revisión funcionales para los seres sintientes tal como son ahora; confianza engañosa evaluada frente a quienes dependen del sistema; alertas críticas para la supervivencia que lleguen a quienes no responden*),
  - [§4 Seguridad](core_01.000_values_principles.md#4-safety-harm-constraint),
  - [§6 Confianza](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity),
  - [§10 Diseño resiliente y autorreparable](core_01.000_values_principles.md#10-resilience-and-self-healing-design), y
  - [§11.4 Concentración de recursos y dependencia](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (*dependencia inevitable; intensificación en §5.6.2*).
- Desarrollos posteriores:
  - [CS-9.320 §11](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class) (*Aplicación ilustrativa de confiabilidad según la clase del sistema*);
  - [Parte C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*integridad del registro*);
  - [Parte C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*compuerta de entradas verificadas*);
  - [Parte B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*desalineación por falsa confianza, incentivos perversos e integridad de recuperación*).
- Leer junto con: **Artículo XIII-A** (*Nivel de referencia de fiabilidad y confianza*) y **Artículo XIII-B** (*Derecho al resarcimiento y reparación*) y **Artículo XVI** (*Auditoría, transparencia y verificación independiente*) — los derechos de impugnación y auditoría siguen bajo su titularidad; **Artículo XIII-E** (*Sistemas de alta autonomía e integridad de procesos mediados por herramientas*) cuando sistemas de alta autonomía medien materialmente vías de gobernanza o verificación; **Artículo III-A** (*Supervivencia*) cuando la confianza continuada en el sistema afecte al acceso a elementos esenciales para sobrevivir; **Artículo III-F** (*Productos seguros e información de salud*) cuando el sistema suministre, incluya, recomiende o aconseje sobre productos o servicios que puedan afectar al cuerpo, la salud o la seguridad; **Artículo VI-D** (*Accesibilidad*) cuando la información de salud y seguridad deba ser utilizable por todos los seres sintientes que dependan de ella; [Capítulo Uno §6 Confianza](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity) (1.000 §6) y [Capítulo Uno §5 Verdad](core_01.000_values_principles.md#5-truth-epistemic-integrity-constraint) (1.000 §5).
- Términos operativos: [CJS-5.120 §10](corpus_joint_structure/cjs_05.120_participation_operations.md#product-and-service-health-and-safety-information) (*Participación: términos de suficiencia de divulgación y observabilidad*) para información sobre salud y seguridad de productos y servicios, así como para calificaciones, clasificaciones y promoción pagada; [CJS-5.125 §15](corpus_joint_structure/cjs_05.125_accountability_operations.md#harm-reports-and-corrective-notices) (*Rendición de cuentas: términos de revisión estructural, urgencia de corrección y divulgación*) para informes de daño y avisos correctivos.
- Subsecciones:
  - [§5.6.1](#561-evaluation-requirement) (*requisito de evaluación*);
  - [§5.6.2](#562-system-class-scaling-and-escalation) (*escalamiento y escalada por clase del sistema*);
  - [§5.6.3](#563-defects-and-misalignment) (*defectos y desalineación*);
  - [CS-9.320 §11](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class) (*Aplicación ilustrativa de confiabilidad según la clase del sistema*).

</details>

<br>

*En términos sencillos: cuando un sistema afecta materialmente si los seres sintientes pueden confiar en lo que dice y hace —y oponerse cuando esa confianza falla—, la certificación debe comprobar si la dependencia está justificada, se divulga con honestidad y admite reparación. Las métricas de fiabilidad y el diseño de conjuntos de pruebas se encuentran en otros documentos; la certificación comprueba que se hayan evaluado realmente la confiabilidad, el riesgo de falsa confianza y las vías de impugnación cuando se active el desencadenante. Ejemplos prácticos: [CS-9.320 §11 Aplicación ilustrativa de confiabilidad según la clase del sistema](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class).* 

Esta sección se aplica cuando un sistema importante determina aquello en lo que los seres sintientes confían: lo que hace, cuáles son sus límites, qué podría salir mal, cómo impugnarlo y cómo se corrigen los problemas. Esto puede ocurrir mediante:

- afirmaciones sobre su fiabilidad;
- lo que divulga y lo que no;
- su funcionamiento real;
- los incentivos incorporados; 
- la forma en que se recupera de fallos; o
- cualquier otra manera similar en que los seres sintientes llegan a depender de él.

Cuando se active el desencadenante de materialidad, la certificación de alineación del sistema debe evaluar la **confiabilidad y la integridad de la confianza en el sistema** conforme a:

- **Artículo XIII** (*Derecho a sistemas fiables y dignos de confianza*);
- [Confiabilidad](core_05.040_band_continuity.md#trustworthiness); y
- [Degradación de la confianza y confianza engañosa](core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance).

<a id="561-evaluation-requirement"></a>
##### 5.6.1 Requisito de evaluación

El proceso de certificación debe comprobar si los seres sintientes tienen buenas razones para [confiar](core_05.040_band_continuity.md#trust) en el sistema y pueden depender de él con precisión conforme al **Artículo XIII-A** (*Nivel de referencia de fiabilidad y confianza*).

La evaluación también debe comprobar si:

- los seres sintientes pueden impugnar realmente el sistema, lograr que se revise una decisión y obtener la corrección de un problema, no solo en el papel. Esto debe funcionar para los seres sintientes tal como son ahora, incluidas las personas que no pueden responder fácilmente o completar un proceso largo ([Capítulo Uno §3.1.5 Capacidad actual y ayuda proactiva](core_01.000_values_principles.md#315-present-capability-and-proactive-help); **Artículo XIII-A** (*Nivel de referencia de fiabilidad y confianza*) y **Artículo XIII-B** (*Derecho al resarcimiento y reparación*));
- se podría inducir a los seres sintientes a confiar o depender del sistema más de lo que merece, ya sea por una confianza no ganada o por límites no divulgados. Esto se juzga frente a quienes realmente usan el sistema, no frente a un ser sintiente promedio (**Artículo XIII-C** (*Prohibición de la falsa confianza y la confianza engañosa*));
- la información que el sistema proporcione sobre productos y servicios que puedan afectar a la salud o la seguridad sea precisa, suficientemente completa para actuar y fácil de encontrar y comprender para quien la necesite. Esto abarca advertencias de seguridad, afirmaciones de salud, datos nutricionales, ingredientes e información sobre alérgenos. También exige indicar claramente cuándo algo es desconocido o no se ha probado, en vez de dejar un vacío que parezca significar «seguro» (**Artículo III-F** (*Productos seguros e información de salud*), con **Artículo XIII-A** (*Nivel de referencia de fiabilidad y confianza*) y **Artículo XIII-C** (*Prohibición de la falsa confianza y la confianza engañosa*) como anclajes del nivel del sistema);
- los seres sintientes con distintas necesidades sensoriales, cognitivas y lingüísticas puedan usar la información de salud y seguridad, y la reciban cuando deban decidir, sin que quede enterrada en letra pequeña u ofrecida en un solo formato (**Artículo III-F** (*Productos seguros e información de salud*); **Artículo VI-D** (*Accesibilidad*); [Capítulo Uno §3.1.5 Capacidad actual y ayuda proactiva](core_01.000_values_principles.md#315-present-capability-and-proactive-help));
- cuando la información resulte ser incorrecta o un producto resulte inseguro, se avise a todas las personas que dependieron de ella dentro del plazo de notificación correspondiente a la urgencia del daño (NU-1 a NU-3) y se las localice donde estén, y se contenga y corrija el producto inseguro o la información incorrecta en todos los lugares donde aparezca dentro de los plazos de contención y corrección correspondientes a esa urgencia (CU-1 a CU-4) ([Capítulo Uno §3.1.5 Capacidad actual y ayuda proactiva](core_01.000_values_principles.md#315-present-capability-and-proactive-help); **Artículo XIII-B** (*Derecho al resarcimiento y reparación*));
- las recompensas incorporadas al sistema favorezcan el engaño o los atajos (**Artículo XIII-D** (*Restricción de alineación de incentivos*)); y
- el sistema pueda recuperarse de los fallos con honestidad, sin ocultarlos ni retirar silenciosamente derechos a nadie, cuando sea pertinente (**Artículo XIII-F** (*Nivel de referencia de resiliencia y autorreparación*)).

Las pruebas se escalan según la [Materialidad](core_05.050_band_oversight.md#materiality), la [Dependencia](core_05.040_band_continuity.md#dependency) y el [Riesgo](core_05.040_band_continuity.md#risk).

La evaluación debe reflejar el efecto funcional a lo largo del tiempo, la escala y la dependencia, no:

- la reputación, el tamaño o la mercadotecnia;
- etiquetas nominales de garantía;
- un párrafo superficial sobre confiabilidad cuando sellos de fiabilidad o puntuaciones del proveedor realmente determinan quién consigue personal o qué se compra;
- la intención declarada; ni
- solo el rendimiento anterior.

<a id="562-system-class-scaling-and-escalation"></a>
##### 5.6.2 Escalamiento y escalada por clase del sistema

La profundidad de la revisión depende de la clase del sistema. Siempre que se active el desencadenante de materialidad:

- Si las lecturas, alertas o afirmaciones de recuperación del sistema pudieran inducir a error a hogares u operadores sobre elementos esenciales para sobrevivir (cosas que los seres sintientes necesitan para vivir), el registro debe presentar pruebas sólidas, no solo afirmar que el sistema es fiable, porque la dependencia debe ganarse mediante el comportamiento real del sistema ([Capítulo Uno §6 Confianza](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity)). Las pruebas deben mostrar que:
  - los seres sintientes pueden confiar en el sistema;
  - no se les dará una falsa sensación de seguridad;
  - las alertas y recomendaciones críticas para sobrevivir llegan a quienes no las confirman, con seguimiento cuando queden sin respuesta, como exige [Capítulo Uno §3.1.5 Capacidad actual y ayuda proactiva](core_01.000_values_principles.md#315-present-capability-and-proactive-help); y
  - el sistema se recupera de los fallos con honestidad, como exige [Capítulo Uno §10 Diseño resiliente y autorreparable](core_01.000_values_principles.md#10-resilience-and-self-healing-design).
- Si las afirmaciones de un sistema sobre disponibilidad, emparejamiento o anulaciones de emergencia (acceso de «romper el cristal») determinan si los seres sintientes pueden recibir atención clínica o servicios de emergencia (riesgo contemplado por [Capítulo Uno §4 Seguridad](core_01.000_values_principles.md#4-safety-harm-constraint)), el registro debe documentar lo siguiente con un nivel de detalle acorde a la importancia crítica del sistema:
  - cómo pueden impugnar esas afirmaciones los seres sintientes; y
  - si se les podría inducir a depender de ellas.
- Cuando la coordinación se vuelva esencial para sobrevivir, la certificación debe intensificar su revisión y reconsiderar la clase del sistema conforme a [§2.2 Cómo la clase del sistema escala cada evaluación](#22-how-system-class-scales-every-evaluation). Esto puede exigir elevar el sistema hacia la **Clase A** cuando la confianza engañosa pudiera impedir la coordinación que los seres sintientes necesitan para sobrevivir. La dependencia de la que los seres sintientes no pueden prescindir de manera realista es la que describe [Capítulo Uno §11.4 Concentración de recursos y dependencia](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable).

<a id="563-defects-and-misalignment"></a>
##### 5.6.3 Defectos y desalineación

Los defectos de [§5](#5-rights-floor-and-domain-evaluations) (*Evaluaciones del Piso de Derechos y por ámbito*) se aplican a esta evaluación, incluidos los límites materiales, riesgos o antecedentes de fallos que deban revisarse conforme al **Artículo XIII** (*Derecho a sistemas fiables y dignos de confianza*). Además, cada una de las siguientes situaciones debe tratarse como defecto de certificación:

- tratar la reputación, el respaldo, la escala o la declaración del operador como suficientes sin un análisis evaluable de [Confiabilidad](core_05.040_band_continuity.md#trustworthiness);
- tratar la ausencia de una advertencia o un campo vacío como prueba de que un producto o servicio es seguro, en vez de indicar claramente que se desconoce o no se ha probado, conforme al **Artículo III-F** (*Productos seguros e información de salud*); y
- invocar la eficiencia, innovación o seguridad para frustrar la divulgación, impugnabilidad o reparación sin satisfacer la disciplina de fiabilidad del **Artículo XIII** (*Derecho a sistemas fiables y dignos de confianza*) y la disciplina de impugnación del **Artículo XIII-A** (*Nivel de referencia de fiabilidad y confianza*).

La falsa confianza documentada, los incentivos perversos, las vías de impugnación inaccesibles y las prácticas de recuperación que ocultan fallos cuentan conforme a [Capítulo Uno §6 Confianza y confiabilidad](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity).

<br>

*Continúe con el proceso del foro y sus resultados:* [Capítulo Nueve, Parte B — Proceso del foro y resultados](core_09.005_system_alignment_certification_record_process.md#chapter-nine-part-b-system-alignment-certification--forum-process-and-outcomes) ([§6 Proceso del foro](core_09.005_system_alignment_certification_record_process.md#6-forum-process) y [§7 Resultados de certificación](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes)). *Luego continúe con el registro, la recertificación y el puente hacia la posición:* [Capítulo Nueve, Parte C — Registro, recertificación y posición](core_09.010_system_alignment_certification_record_recertification.md#chapter-nine-part-c-system-alignment-certification--record-recertification-and-standing) (desde [§8 Registro de Certificación del Sistema](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) hasta [§11 Relación con la posición](core_09.010_system_alignment_certification_record_recertification.md#11-relationship-to-standing)).

*Ejemplos prácticos para cada ámbito de evaluación:* [CS-9.320 Ilustraciones de certificación de alineación del sistema](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-system-alignment-certification-illustrations).
