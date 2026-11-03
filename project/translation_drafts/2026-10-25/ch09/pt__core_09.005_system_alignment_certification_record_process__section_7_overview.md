### 7. Resultados da certificação

<details>
<summary><strong><span style="color: #2563eb;">Rastreio</span></strong></summary>

- A montante:
  - [§6](#6-forum-process) (*processo do fórum e contestação confiável*);
  - da [Parte A §2](core_09.000_system_alignment_certification_evaluation.md#2-system-class-evaluation) (9.000 §2) até
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-rights-floor-and-domain-evaluations) (*classificação incorreta, desalinhamento e defeitos encontrados na avaliação*);
  - [Dois Objetivos Constitucionais](core_00.000_preamble.md#two-constitutional-aims);
  - [Capítulo Três §1](core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1) e
  - [§2](core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*integridade de definição e evasão*);
  - [Capítulo Três §2.1 Padrões comuns de evasão](core_03.000_definition_integrity.md#21-common-evasion-patterns) (3.000 §2.1) (*evasão de escopo e limites*);
  - [Carta do sistema](core_05.040_band_continuity.md#system-charter) (*divergência entre a Carta do sistema e o comportamento, e revisão em atraso*).
- A jusante:
  - [Parte C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (*o resultado é declarado no registro*);
  - [Parte C §9.1](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification) (*a via de contestação se abre com o resultado*);
  - [Parte C §9](core_09.010_system_alignment_certification_record_recertification.md#9-recertification-and-reopening) (*recertificação e reabertura*);
  - [Parte C §10](core_09.010_system_alignment_certification_record_recertification.md#10-relationship-to-standing) (*barreira de entradas verificadas quando os fatos sustentam achados adversos*);
  - [Capítulo Treze](core_14.000_forum.md#chapter-fourteen-forums-and-jurisdiction) (13.000) (*supervisão do fórum*);
  - [Capítulo Dez](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement) (10.000).
- Leia também: **[CS-6.305 §5](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Reclassificação e governança do ciclo de vida*) para a reavaliação programada dos tipos de dados, e **[CS-9.305 §3](corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*Requisito de reclassificação*) para os gatilhos de reavaliação da classe do sistema e a verificação SAC.
- Subseções:
  - [§7.1](#71-go-live-gate) (*barreira de entrada em operação*, com
  - [§7.1.1 Sistemas já em operação](#711-systems-already-operating) e
  - [§7.1.2 Projetos-piloto](#712-pilots));
  - [§7.2](#72-certification-defects-and-correction) (*defeitos de certificação e correção*);
  - [§7.3](#73-remediation-readiness-willingness-and-capacity-to-correct) (*prontidão para remediação: disposição e capacidade de corrigir*, com
  - [§7.3.1 Disposição](#731-willingness),
  - [§7.3.2 Capacidade](#732-capacity),
  - [§7.3.3 Etapa de comprovação](#733-proof-step),
  - [§7.3.4 Achados](#734-findings), e
  - [§7.3.5 Mesmos termos para todos os operadores](#735-same-terms-for-every-operator));
  - [§7.4](#74-denial-and-revocation) (*recusa e revogação*, com
  - [§7.4.1 O que são recusa e revogação](#741-what-denial-and-revocation-are),
  - [§7.4.2 Quando a recusa ou revogação é obrigatória](#742-when-denial-or-revocation-is-required),
  - [§7.4.3 Proteção primeiro](#743-protection-first),
  - [§7.4.4 Processo](#744-process),
  - [§7.4.5 Efeito](#745-effect), e
  - [§7.4.6 Não é uma proibição permanente](#746-not-a-permanent-bar)).

</details>

<br>

*Em termos simples: toda revisão de certificação termina com um resultado declarado, respaldado por evidências e pelas preocupações levantadas ao longo do processo. Nada entra em operação até ser certificado, até que o resultado publicado tenha dado aos sencientes afetados uma oportunidade prática de contestá-lo, e até que as proteções exigidas antes da entrada em operação tenham sido verificadas.*

Esta seção é a **Fase IV, Decidir**, após [§6 Processo do fórum](#6-forum-process) (**Fase III, Revisão**). Ela abrange o resultado alcançado pelos fóruns. [§7.1 Barreira de entrada em operação](#71-go-live-gate) estabelece essa barreira, e [§7.2 Defeitos de certificação e correção](#72-certification-defects-and-correction) estabelece o que ocorre quando um defeito é encontrado.

Uma decisão de certificação deve declarar seu resultado no registro segundo a [Parte C §8.1 Conteúdo mínimo do registro](core_09.010_system_alignment_certification_record_recertification.md#81-minimum-record-contents), junto com as preocupações levantadas para alcançá-lo. O resultado é um dos seguintes:

- certificação provisória;
- certificação plena;
- certificação condicional;
- certificação diferida;
- não certificação;
- retirada;
- expiração; ou
- liberação das condições.

Um sistema sem certificação provisória nem plena está **Não Certificado**. É o caso quando a certificação está:

- diferida;
- recusada;
- retirada; ou
- expirada.

Certificação provisória e certificação plena são os dois **status** da certificação. A [Parte C §9.2 Certificação provisória e plena](core_09.010_system_alignment_certification_record_recertification.md#92-provisional-and-full-certification) explica como um sistema obtém, mantém e perde cada status. As condições da certificação condicional podem se aplicar a qualquer um dos status.

<a id="71-go-live-gate"></a>

