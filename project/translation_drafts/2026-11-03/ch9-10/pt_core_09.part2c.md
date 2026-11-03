#### 3.3 Restrição de Consistência Temporal

A certificação não pode tratar nenhum dos itens a seguir como suficiente quando violações previsíveis de médio ou longo prazo continuarem sem resposta:

- métricas de curto prazo;
- conformidade local; ou
- eficiência em horizonte curto.

A busca por resultados de curto prazo não é aceitável se for razoável esperar que, adiante, ela prejudique qualquer um dos itens abaixo, mesmo quando o dano se acumular lentamente, aparecer tarde ou se espalhar por sistemas diferentes:

- **Segurança**;
- **Verdade**; ou
- **bem-estar**.

<a id="34-data-types-and-handling-evaluation"></a>

#### 3.4 Avaliação de Tipos e Tratamento de Dados

<details>
<summary><strong><span style="color: #2563eb;">Rastreio</span></strong></summary>

- A montante:
  - [§3](#3-whole-system-certification-evaluation) (*fatores de avaliação integral do sistema*);
  - [CS-9.320 §4](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-4-illustrative-whole-system-application-by-system-class) (*Aplicação ilustrativa da avaliação integral do sistema por classe de sistema*);
  - [Parte C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*conteúdo do registro*);
  - [§2](#2-system-class-evaluation) (*avaliação da classe do sistema*); família de medição de Supervisão (*Verdade e integridade epistêmica como medição constitucional*);
  - [Article XV: Integridade da Esfera Informacional](core_06.010_rights_part_c.md#article-xv-info-sphere-integrity);
  - [Article XVI: Auditoria, Transparência e Verificação Independente](core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification);
  - [Article VII: Autopropriedade](core_06.005_rights_part_b.md#article-vii-self-ownership).
- A jusante:
  - [CS-9.320 §5](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-5-illustrative-data-handling-application-by-system-class) (*Aplicação ilustrativa do tratamento de dados por classe de sistema*);
  - [§5.1](#51-ecological-footprint-evaluation) e
  - [CS-9.320 §6](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-6-illustrative-ecological-footprint-application-by-system-class) (*Aplicação ilustrativa da pegada ecológica por classe de sistema*);
  - [Parte C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*integridade do registro*);
  - [Parte C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*entrada verificada*);
  - [Parte B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*reclassificação e incompatibilidade no tratamento*).
- Leia junto com:
  - **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Tipos e tratamento de informações*) e [CS-6.310 — Classificações de dados](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)** (inclusive **
  - [CS-6.305 §5.2](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Governança da reclassificação e do ciclo de vida*) e **
  - [CS-6.305 §8](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-8-system-data-types-record-governance)** (*Governança do Registro de Tipos de Dados do Sistema*));
  - [Registro de Tipos de Dados do Sistema](core_05.040_band_continuity.md#system-data-types-record);
  - [Divulgação Pública de Referência da Supervisão](core_05.050_band_oversight.md#public-oversight-baseline-disclosure);
  - **CJS-5.130 §18** (*termos de retenção de dados e integridade do ciclo de vida*),
  - **CJS-5.130 §21** (*termos de robustez adversarial e resistência a abusos*), e
  - **CJS-5.130 §17** (*termos de interoperabilidade, portabilidade e integridade da saída*) quando materialmente aplicáveis;
  - [§4.1 Invocação Conjunta de Privacidade (Informacional)](#41-privacy-informational-joint-invocation) quando houver envolvimento de um ponto de privacidade.
- Subseções:
  - [§3.4.1](#341-type-o-baseline-disclosure) (*divulgação da referência Tipo O*);
  - [§3.4.2](#342-privacy-discipline) (*disciplina de privacidade*);
  - [§3.4.3](#343-protective-storage-and-key-custody) (*armazenamento protetivo e custódia de chaves*);
  - [§3.4.4](#344-scheduled-data-type-re-evaluation) (*reavaliação programada dos tipos de dados*);
  - [§3.4.5](#345-system-class-scaled-infrastructure-assurance) (*garantia de infraestrutura escalonada por classe de sistema*);
  - [§3.4.6](#346-infrastructure-robustness-for-data) (*robustez da infraestrutura para dados*);
  - [§3.4.7](#347-defects-and-misalignment) (*defeitos e incompatibilidade*);
  - [CS-9.320 §5](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-5-illustrative-data-handling-application-by-system-class) (*Aplicação ilustrativa do tratamento de dados por classe de sistema*).

</details>

<br>

*Em termos simples: a certificação também precisa examinar que tipos de dados o sistema acessa e se os trata adequadamente — inclusive se os tipos continuam corretos no ciclo de revisão atual e se a infraestrutura subjacente é robusta o bastante para esses dados naquela classe de sistema. As regras de tipos e o Registro de Tipos de Dados do Sistema estão no corpus de sistemas; a certificação verifica se as regras foram realmente aplicadas e se o registro é honesto.*

A certificação de alinhamento de sistemas deve avaliar **tipos e tratamento de dados** como parte de todo Registro de Certificação do Sistema de impacto material. Esta seção declara o que a certificação deve verificar. A taxonomia de tipos e a mecânica de tratamento estão em **[CS-6.305](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Tipos e tratamento de informações*) e [CS-6.310 — Classificações de dados](corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**, em conjunto com:

- as definições canônicas de tipos de informação;
- as regras de tratamento e os requisitos de separação;
- os detalhes do ciclo de vida; e
- o duradouro [Registro de Tipos de Dados do Sistema](core_05.040_band_continuity.md#system-data-types-record).

**Requisito de avaliação.** O processo de certificação deve determinar se o sistema:

- identifica os tipos de dados materialmente em escopo; e
- os trata segundo a classificação **aplicável mais restritiva**, inclusive durante transformação, agregação, delegação, armazenamento, retenção e vinculação entre domínios.

A avaliação deve refletir o efeito funcional, e não apenas o rótulo, formato ou etapa do fluxo de processamento.

<a id="341-type-o-baseline-disclosure"></a>
##### 3.4.1 Divulgação da Referência Tipo O

Quando se aplicar a **[referência Tipo O de CS-6.305 §7](corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-7-type-o-baseline-for-class-abc-systems)**, a certificação também deve verificar se a [Divulgação Pública de Referência da Supervisão](core_05.050_band_oversight.md#public-oversight-baseline-disclosure) (**Tipo O**) publicada abrange o **escopo certificado**, mapeado a partir de:

- a [Carta do Sistema](core_05.040_band_continuity.md#system-charter) que o rege;
- a classe de sistema atribuída; e
- os [Limites do Sistema](core_05.040_band_continuity.md#system-boundaries) observados.

Essa cobertura deve incluir as conclusões de governança, incentivos e impugnabilidade, e as funções atribuídas nos termos de [§3.1 Disciplina de Governança, Incentivos e Impugnabilidade](#31-governance-incentive-and-contestability-discipline).

Para todas as classes de sistema, inclusive Classe L e Classe P, a certificação também deve verificar se o Registro de Certificação do Sistema é publicado como dado de certificação **Tipo O** nos termos de [CS-6.310 Parte B §9.3 Tipo O](corpus_systems/cs_06.310_data_classifications.md#93-type-o-open-public-oversight-baseline-disclosure-data). A publicação não exige a Divulgação Pública de Referência da Supervisão completa fora das Classes A, B e C.

O compartilhamento de riscos avaliados também pode contar para essa referência quando houver risco sistêmico em jogo. O direito do público à referência é mais amplo que a certificação e não exige um registro separado ao lado do [Registro de Classificação do Sistema](core_05.040_band_continuity.md#system-classification-record) ou do [Registro de Tipos de Dados do Sistema](core_05.040_band_continuity.md#system-data-types-record).

Cada retenção justificada deve vir acompanhada da substituição pública mais forte que for razoavelmente possível ([§3.4.5 Garantia de Infraestrutura Escalonada por Classe de Sistema](#345-system-class-scaled-infrastructure-assurance) dá exemplos). O Capítulo Cinco é titular do termo; CS-6.305 (*Tipos e tratamento de informações*) e CS-6.310 (*Classificações de dados*) são titulares do conteúdo da referência e da mecânica de divulgação.

<a id="342-privacy-discipline"></a>
