<!-- AI-assisted translation draft; unreviewed. §2 evaluation requirements, source lines 311–335; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §2 evaluation requirements (ru)

## English source (lines 311–335)

This section states what certification must verify:

- **Evaluation requirement:**
  - whether the assigned system class reflects observed and reasonably foreseeable **impact**, **dependency**, and **risk** under CS-9.305 (*System classification machinery*) and CS-9.310 (*System impact classifications*), including:
    - aggregate effects;
    - interaction effects;
    - adversarial effects;
    - threshold effects;
  - that classification is determined by actual system behavior and impacts, not from:
    - declared intent;
    - nominal scope;
    - [System Charter](core_05.040_band_continuity.md#system-charter) text alone; or
    - self-description alone;
  - that the system's class was re-checked under the **[CS-9.305 §3.5 reclassification requirement](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** whenever a significant change called for it; and
  - that the [System Classification Record](core_05.040_band_continuity.md#system-classification-record) shows the **highest system class that applies** under current conditions.
- **Assurance and regression testing:**
  - that system-class-scaled assurance, infrastructure robustness, and regression coverage match the assigned system class under:
    - CS-9.305 (*System classification machinery*) and CS-9.310 (*System impact classifications*); and
    - CS-6.345 (*System lifecycle*), read with these shared operational terms where materially applicable:
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c) (*Continuity: graceful degradation and failure-mode integrity terms*);
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c) (*Continuity: reversibility and containment terms*);
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c) (*Continuity: adversarial robustness and abuse-resistance terms*);
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms) (*Integrative: constrained-secrecy and protected-investigation terms*), where the system's class or function makes it materially applicable; and
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms) (*Integrative: intervention and override integrity terms*), where the system's class or function makes it materially applicable; and
  - that regression testing was run for each recertification, as CS-6.345 (*System lifecycle*) requires, with its results on the record under [§8.1 Minimum record contents](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents).

## Translation draft

В этом разделе указано, что должна проверять сертификация:

- **Требование к оценке:**
  - отражает ли присвоенный класс системы наблюдаемые и разумно предвидимые **воздействие**, **зависимость** и **риск** согласно CS-9.305 (*Механизм классификации систем*) и CS-9.310 (*Классификации воздействия системы*), включая:
    - совокупные эффекты;
    - эффекты взаимодействия;
    - враждебные эффекты;
    - пороговые эффекты;
  - определяется ли классификация фактическим поведением и воздействиями системы, а не:
    - заявленным намерением;
    - номинальным охватом;
    - только текстом [Хартии системы](core_05.040_band_continuity.md#system-charter); или
    - только самоописанием;
  - перепроверялся ли класс системы согласно **[требованию переклассификации CS-9.305 §3.5](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** всякий раз, когда этого требовало существенное изменение; и
  - указывает ли [Запись классификации системы](core_05.040_band_continuity.md#system-classification-record) **наивысший применимый класс системы** в текущих условиях.
- **Обеспечение и регрессионное тестирование:**
  - соответствуют ли обеспечение с учетом класса системы, устойчивость инфраструктуры и охват регрессионного тестирования присвоенному классу согласно:
    - CS-9.305 (*Механизм классификации систем*) и CS-9.310 (*Классификации воздействия системы*); и
    - CS-6.345 (*Жизненный цикл системы*) с учетом следующих общих эксплуатационных терминов, когда они имеют существенное значение:
      - [**CJS-5.130 §19**](corpus_joint_structure/cjs_05.130_continuity_operations.md#right-to-exit-pathway-integrity-c) (*Непрерывность: термины о постепенной деградации и целостности режимов отказа*);
      - [**CJS-5.130 §20**](corpus_joint_structure/cjs_05.130_continuity_operations.md#transparency-disclosures-and-stakeholder-legibility-c) (*Непрерывность: термины об обратимости и локализации*);
      - [**CJS-5.130 §21**](corpus_joint_structure/cjs_05.130_continuity_operations.md#signaling-integrity-and-anti-silent-failure-controls-c) (*Непрерывность: термины об устойчивости к противодействию и сопротивлении злоупотреблениям*);
      - [**CJS-5.135 §22**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-22-integrative-constrained-secrecy-and-protected-investigation-terms) (*Интеграция: термины об ограниченной секретности и защищенном расследовании*), когда класс или функция системы делают их существенно применимыми; и
      - [**CJS-5.135 §23**](corpus_joint_structure/cjs_05.135_integrative_operations.md#cjs-5135-23-integrative-intervention-and-override-integrity-terms) (*Интеграция: термины о целостности вмешательства и переопределения*), когда класс или функция системы делают их существенно применимыми; и
  - проводилось ли регрессионное тестирование при каждой повторной сертификации, как требует CS-6.345 (*Жизненный цикл системы*), и внесены ли результаты в запись согласно [§8.1 Минимальное содержание записи](core_09.005_system_alignment_certification_record_process.md#81-minimum-record-contents).
