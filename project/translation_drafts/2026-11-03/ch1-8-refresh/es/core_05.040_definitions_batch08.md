# Borrador de traducción — Capítulo Cinco, definiciones adicionales
**Fuente:** `core_05.040_band_continuity.md`, texto vigente de las entradas indicadas. Anclas conservadas literalmente.

<a id="certification-denial"></a>
#### Denegación de Certificación

*En términos sencillos: negar la certificación a un sistema que aún no la tiene porque el operador no demostró voluntad y capacidad para corregir un problema. Es un resultado real que modifica el estado de certificación, no una amenaza; por sí sola no cierra el sistema.*

- **Incluye:** no certificar un sistema que carece de estado de certificación, en la primera certificación, revisión nueva u otro ciclo, porque la evaluación de preparación para remediar no demuestra que el operador pueda y quiera corregir una desalineación o defecto.
- **No incluye:** revocar una certificación ya concedida; aplazar la decisión por un plazo acotado; ordenar el cese operativo, que se decide aparte según la protección de supervivencia esencial del Capítulo Nueve, Parte C, §9.3.5; ni decidir efectos de condición o infracción, que corresponden al Capítulo Once.
- **Depende de:** Certificación de Alineación del Sistema. Los criterios y el proceso están en el Capítulo Nueve, Parte B, §7.4; los efectos, en §7.5.
- **Evaluación primaria:** verificar que la denegación se base en una conclusión registrada sobre falta de voluntad o capacidad correctiva, no en tamaño, antigüedad, riqueza o intereses rivales del operador; que se hayan fijado protección provisional y límites de dependencia antes de su efecto y se haya avisado a quienes dependen del sistema; y que el operador haya recibido aviso y oportunidad de responder o presentar la prueba requerida.
- **Incumplimiento primario:** denegar sin conclusión registrada de preparación o por motivo ajeno a la corrección; conceder certificación condicional cuando corresponde denegar; usar la denegación para cortar esenciales de supervivencia antes de tener sustitutos; o no informar a quienes dependen del sistema.

<a id="certification-revocation"></a>
#### Revocación de Certificación

*En términos sencillos: retirar la certificación que ya tiene un sistema porque el operador no demostró voluntad o capacidad para corregir un problema, actuó deshonestamente o incumplió condiciones. Cambia el estado de certificación, pero no ordena por sí sola cerrar el sistema.*

- **Incluye:** retirar una certificación en recertificación o revisión reabierta por falta de preparación correctiva, incumplimiento repetido o material de una condición, o por pruebas falsas, fabricadas u ocultadas sobre preparación, corrección o liberación de una condición.
- **No incluye:** denegación a un sistema aún no certificado; aplazamiento de una decisión; cascada a una Institución citante, regida por el Capítulo Diez §9.5; ni efecto de condición o conclusión de infracción, exclusivos del Capítulo Once.
- **Depende de:** Certificación de Alineación del Sistema y Recertificación. Proceso y efectos: Capítulo Nueve, Parte B, §§7.4–7.5.
- **Evaluación primaria:** confirmar que hubo aviso y oportunidad de responder, que la causa consta en el expediente y no depende de tamaño, antigüedad, riqueza o intereses concurrentes; que se fijaron protecciones provisionales y límites de dependencia antes de la revocación y se informó a quienes dependen; y que, si interrumpir el sistema cortaría esenciales antes de contar con sustitutos, el estado cambió de inmediato pero la operación continuó únicamente bajo autorización provisional separada.
- **Incumplimiento primario:** revocar sin aviso de causa y pruebas o sin oportunidad de responder; mantener certificación condicional cuando el expediente requiere revocación; usar la revocación para cortar esenciales antes de existir sustitutos; o no avisar a quienes dependen del sistema.

<a id="full-certification"></a>
#### Certificación Plena

*En términos sencillos: estado de certificación de intervalo más largo que un sistema obtiene tras recertificaciones limpias consecutivas, sin problemas actuales ni señales de problemas próximos. No es permanente; una evaluación fallida o una señal de advertencia la retira.*

- **Incluye:** estado de un sistema certificado provisionalmente que completó el número requerido de recertificaciones provisionales limpias consecutivas y cuya recertificación más reciente no encontró desalineación actual ni indicadores de desalineación inminente. El intervalo se escala según la clase, es temporal y admite reapertura.
- **No incluye:** certificación provisional; certificación condicional, que puede acompañar cualquiera de los estados; permiso permanente, reputación o efecto de condición (el Capítulo Once decide la condición).
- **Depende de:** Certificación Provisional y Recertificación. El mínimo de ciclos limpios, el descenso de categoría y las ventanas por nivel están en el Capítulo Nueve, Parte C, §9.3.
- **Evaluación primaria:** comprobar que se completó el número de recertificaciones limpias que exige la clase; que no hay desalineación actual (incluidos defectos sin reparar, controles vencidos o pruebas de regresión fallidas); y que los disparadores y tendencias de monitoreo registrados no cruzan ni se aproximan a umbrales, son revisables independientemente y no están definidos para ocultar la desalineación.
- **Incumplimiento primario:** concederla antes del mínimo o pese a desalineación/señales inminentes; mantenerla tras recertificación fallida o revisión reabierta con hallazgos de desalineación; definir indicadores tan estrechos que nada advierta de un problema; o usarla para omitir o retrasar un disparador de reapertura.

<a id="go-live"></a>
#### Puesta en Servicio (Go-Live)

*En términos sencillos: momento en que el sistema deja de estar en construcción o pruebas y empieza a afectar materialmente a entidades sintientes o a ser objeto de dependencia material. Importa lo que hace, no el nombre del lanzamiento.*

- **Incluye:** primera operación con efecto material o dependencia material, como piloto o despliegue completo. Cada piloto, despliegue completo posterior y ampliación material más allá del alcance, población o duración certificados constituye su propia puesta en servicio para la parte ampliada. Se determina por operación y efecto reales, no por etiquetas como beta, prueba, vista previa, acceso anticipado, lanzamiento suave o experimental, ni por fecha de anuncio o hito interno.
- **No incluye:** desarrollo, pruebas, validación, entorno de preparación o simulación sin efectos vivos ni dependencia; un sistema sin efecto/dependencia material; sistemas ya operativos al entrar en vigor el documento de adopción, sujetos a la ventana de Transición de Adopción del Artículo XXVIII-A y no a un segundo lanzamiento; ni cambios ordinarios que no sean ampliación material.
- **Depende de:** Impacto Material y Dependencia. La puerta, aviso previo y verificación de condiciones se rigen por el Capítulo Nueve, Parte B, §7.1.
- **Evaluación primaria:** identificar la fecha por el inicio del efecto o dependencia material real, no por etiqueta o anuncio; confirmar que no hubo efectos ni dependencia antes de la primera fecha permitida del Registro de Certificación del Sistema; y tratar piloto, despliegue completo y expansión material como puestas en servicio distintas.
- **Incumplimiento primario:** operar en vivo antes de superar la puerta; rebautizar operación real como beta/prueba; dividir la publicación en incrementos para eludir la puerta; o tratar una expansión material como continuación del lanzamiento anterior o fecharlo retroactivamente.
