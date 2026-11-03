### 7. Результаты сертификации

<details>
<summary><strong><span style="color: #2563eb;">Трассировка</span></strong></summary>

- Вышестоящие положения:
  - [§6](#6-forum-process) (*процесс в форуме и заслуживающее доверия оспаривание*);
  - от [Части A §2](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (9.000 §2) до
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*ошибочная классификация, несогласованность и дефекты, выявленные при оценке*);
  - [Две конституционные цели](core_00.000_preamble.md#two-constitutional-aims);
  - [Глава Третья §1](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1) и
  - [§2](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*целостность определений и уклонение*);
  - [Глава Третья §2.1 Распространенные схемы уклонения](core_03.000_definition_integrity.md#21-common-evasion-patterns) (3.000 §2.1) (*уклонение от требований к охвату и границам*);
  - [Устав системы](core_05.040_band_continuity.md#system-charter) (*несоответствие Устава системы и поведения, а также просроченный пересмотр*).
- Нижестоящие положения:
  - [Часть C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (*результат указывается в записи*);
  - [Часть C §9.1](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification) (*путь оспаривания открывается вместе с результатом*);
  - [Часть C §9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) (*повторная сертификация и возобновление*);
  - [Часть C §10](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing) (*шлюз проверенных данных, если факты обосновывают неблагоприятные выводы*);
  - [Глава Тринадцать](core_14.000_forum.md#chapter-fourteen-forums-and-jurisdiction) (13.000) (*надзор форума*);
  - [Глава Десять](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) (10.000).
- Читать вместе с: **[CS-6.305 §5](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Переклассификация и управление жизненным циклом*) — для плановой переоценки типов данных, и **[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*Требование переклассификации*) — для триггеров переоценки класса системы и проверки SAC.
- Подразделы:
  - [§7.1](#71-go-live-gate) (*ворота допуска к запуску*, включая
  - [§7.1.1 Уже работающие системы](#711-systems-already-operating) и
  - [§7.1.2 Пилотные проекты](#712-pilots));
  - [§7.2](#72-certification-defects-and-correction) (*дефекты сертификации и исправление*);
  - [§7.3](#73-remediation-readiness-willingness-and-capacity-to-correct) (*готовность к исправлению: готовность действовать и способность исправить*, включая
  - [§7.3.1 Готовность действовать](#731-willingness),
  - [§7.3.2 Способность](#732-capacity),
  - [§7.3.3 Этап доказательства](#733-proof-step),
  - [§7.3.4 Выводы](#734-findings) и
  - [§7.3.5 Одинаковые условия для каждого оператора](#735-same-terms-for-every-operator));
  - [§7.4](#74-denial-and-revocation) (*отказ и отзыв*, включая
  - [§7.4.1 Что такое отказ и отзыв](#741-what-denial-and-revocation-are),
  - [§7.4.2 Когда требуется отказ или отзыв](#742-when-denial-or-revocation-is-required),
  - [§7.4.3 Защита прежде всего](#743-protection-first),
  - [§7.4.4 Процесс](#744-process),
  - [§7.4.5 Последствия](#745-effect) и
  - [§7.4.6 Это не постоянный запрет](#746-not-a-permanent-bar)).

</details>

<br>

*Простыми словами: каждый пересмотр сертификации заканчивается объявленным результатом, подтвержденным доказательствами и опасениями, высказанными в ходе процесса. Система не запускается, пока не сертифицирована, пока опубликованный результат не предоставит затронутым разумным существам практическую возможность оспорить его и пока не проверены меры защиты, необходимые до запуска.*

Этот раздел — **Этап IV, Решение**, следующий за [§6 Процесс в форуме](#6-forum-process) (**Этап III, Рассмотрение**). В нем рассматривается результат, к которому приходят форумы. [§7.1 Ворота допуска к запуску](#71-go-live-gate) устанавливает такие ворота, а [§7.2 Дефекты сертификации и исправление](#72-certification-defects-and-correction) определяет, что происходит при обнаружении дефекта.

Решение о сертификации должно указывать результат в записи согласно [Части C §8.1 Минимальное содержание записи](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents), вместе с опасениями, возникшими при его принятии. Результат может быть одним из следующих:

- предварительная сертификация;
- полная сертификация;
- условная сертификация;
- отложенная сертификация;
- отказ в сертификации;
- отзыв;
- истечение срока; или
- снятие условий.

Система, не имеющая ни предварительной, ни полной сертификации, считается **Не сертифицированной**. Это относится к случаям, когда сертификация:

- отложена;
- отклонена;
- отозвана; или
- срок ее действия истек.

Предварительная и полная сертификация — два **статуса** сертификации. [Часть C §9.2 Предварительная и полная сертификация](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) объясняет, как система получает, сохраняет и утрачивает каждый из них. Условия условной сертификации могут применяться к любому из этих статусов.

<a id="71-go-live-gate"></a>

