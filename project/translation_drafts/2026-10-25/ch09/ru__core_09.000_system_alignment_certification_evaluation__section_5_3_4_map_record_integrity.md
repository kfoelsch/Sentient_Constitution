<!-- AI-assisted translation draft; unreviewed. §5.3.4 map and record integrity, source lines 1209–1215; source SHA-256 4311e6ba74b7210f077c0bd4c8d21d8c9f517d2ada7b6d87288b39494dfeadd5. Draft only; do not synchronize into translations/. -->

# Chapter Nine Part A — §5.3.4 map and record integrity (ru)

## English source (lines 1209–1215)

Before relying on dependency maps and resource-flow records, certification must check that they meet **Article V-A** (*Dependency Mapping and Resource-Flow Transparency*). They must be:

- **Complete:** they cover significant upstream and downstream dependencies, resource flows, and any relationships that are hidden or lopsided, where those matter.
- **Current:** they are updated often enough given how fast things change and how critical the system is, including its system class under [§2 System Class Evaluation](#2-system-class-evaluation). They show the system as it runs now, not as it ran at the last certification.
- **Auditable:** they are open to audit under **Article XVI-A** (*Auditability and Observable Evidence*).

A map or record that fails any of these tests cannot support a finding that the system gives back enough. The gap must be written down and handled under *Defects and misalignment* below.

## Translation draft

##### 5.3.4 Целостность карт и записей

Прежде чем полагаться на карты зависимостей и записи потоков ресурсов, сертификация должна проверить их соответствие **Article V-A** (*Dependency Mapping and Resource-Flow Transparency*). Они должны быть:

- **Полными:** охватывать значимые зависимости выше и ниже по цепочке, потоки ресурсов и любые скрытые или несбалансированные отношения, если это важно.
- **Актуальными:** обновляться достаточно часто с учетом скорости изменений и критичности системы, включая ее класс по [§2 System Class Evaluation](#2-system-class-evaluation). Они должны отражать нынешнюю работу системы, а не ее состояние при последней сертификации.
- **Поддающимися аудиту:** открытыми для аудита согласно **Article XVI-A** (*Auditability and Observable Evidence*).

Карта или запись, не прошедшая любой из этих тестов, не может подтверждать вывод о достаточности возвращаемой системой поддержки. Пробел необходимо зафиксировать и устранить согласно приведенному ниже разделу *Defects and misalignment*.
