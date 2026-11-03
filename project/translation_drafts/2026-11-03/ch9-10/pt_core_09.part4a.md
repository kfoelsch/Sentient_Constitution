##### 5.3.4 Integridade do Mapa e do Registro

Antes de confiar em mapas de dependências e registros de fluxos de recursos, a certificação deve verificar se eles cumprem **Article V-A** (*Mapeamento de Dependências e Transparência dos Fluxos de Recursos*). Devem ser:

- **Completos:** abrangem dependências significativas a montante e a jusante, fluxos de recursos e relações ocultas ou desequilibradas, quando forem relevantes.
- **Atuais:** são atualizados com frequência compatível com a velocidade das mudanças e a criticidade do sistema, inclusive sua classe nos termos de [§2 Avaliação da Classe do Sistema](#2-system-class-evaluation). Mostram o sistema como opera agora, não como operava na última certificação.
- **Auditáveis:** estão abertos à auditoria nos termos de **Article XVI-A** (*Auditabilidade e Evidências Observáveis*).

Um mapa ou registro que não passar em qualquer um desses testes não pode fundamentar a conclusão de que o sistema devolve o suficiente. A lacuna deve ser registrada e tratada nos termos de *Defeitos e incompatibilidade* abaixo.

<a id="535-system-class-scaling-and-escalation"></a>
##### 5.3.5 Escalonamento e Escalada por Classe de Sistema

A classe do sistema define a profundidade da revisão e o rigor da avaliação de suficiência. Ela nunca torna irrelevante uma extração compartilhada, e a extração dividida entre entidades, registros ou períodos é avaliada como um todo nos termos de [Capítulo Um §15.1.1 Princípio Antifragmentação](core_01.005_interaction_interpretation.md#1511-anti-segmentation-principle). Sempre que o gatilho de materialidade se aplicar:

- Um sistema que se baseie em uma infraestrutura comum da qual os sencientes precisam para sobreviver — como uma bacia hidrográfica compartilhada ou a espinha dorsal de uma rede elétrica regional — deve registrar as provas mais fortes do mapa de dependências e dos fluxos de retorno. São esses os sistemas compartilhados cuja capacidade duradoura é protegida por [Capítulo Um §9 Capacidade de Sistemas Compartilhados](core_01.000_values_principles.md#9-shared-system-capacity), e **Article III-A** (*Sobrevivência*) é a razão para exigir aqui as provas mais fortes.
- Um sistema que dependa de autenticação compartilhada, TI de saúde ou infraestrutura semelhante deve documentar o que retira e se o apoio que fornece é suficiente, com profundidade compatível com a criticidade de suas operações. Slogans vagos sobre “interoperabilidade” não contam: a dependência deve estar visível nos mapas e registros, conforme exige [Capítulo Um §18.5 Arquitetura Modular e Disciplina de Dependência](core_01.010_stewardship_capacity_principles.md#185-modular-architecture-and-dependency-discipline).
- Um sistema não pode escapar à revisão entre sistemas enquanto se torna discretamente um ponto de estrangulamento de pagamentos, identidade ou pessoal para instituições que não conseguem trocar de fornecedor de forma realista.
  - **Quem não consegue trocar:** determinado pelos fatores de substituibilidade em [§5.3.3 Requisito de Avaliação](#533-evaluation-requirement).
  - **Por que importa:** trata-se do tipo de concentração descrito em [Capítulo Um §11.4 Concentração de Recursos e Dependência](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable). Ele orienta quem adota sistemas a definir níveis para isso, como quantos sencientes ou sistemas dependem de um só provedor sem alternativa real, ou quem controla interfaces e pontos de acesso à infraestrutura compartilhada. A certificação não espera que o nível definido por quem adota o sistema seja ultrapassado para aumentar o rigor da revisão (veja abaixo).
  - **O que a certificação faz:** aumenta o rigor da revisão e reconsidera a classe do sistema nos termos de [§2.2 Como a classe do sistema escalona cada avaliação](#22-how-system-class-scales-every-evaluation), até a **Classe A** quando o sistema controla o acesso à coordenação essencial à sobrevivência.

O aumento de rigor não espera que um limite de concentração definido segundo [Capítulo Um §11.4 Concentração de Recursos e Dependência](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) seja ultrapassado. Ultrapassar um limite definido por quem adota o sistema é evidência adicional. Um limite não definido ou alto demais não adia o aumento de rigor, e ultrapassá-lo não constitui, por si só, uma constatação de conduta indevida.

<a id="536-defects-and-misalignment"></a>
##### 5.3.6 Defeitos e Incompatibilidade

Os defeitos de [§5](#5-rights-floor-and-domain-evaluations) (*Avaliações do Piso de Direitos e de Domínio*) aplicam-se a esta avaliação, inclusive às informações sobre dependência ou fluxo de recursos que o sistema deve divulgar nos termos de **Article V-A** (*Mapeamento de Dependências e Transparência dos Fluxos de Recursos*). Além disso, cada item abaixo conta como defeito de certificação:

- tratar qualquer um dos itens abaixo como suficiente para cumprir [Apoio Proporcional entre Sistemas](core_05.040_band_continuity.md#proportionate-cross-system-support):
  - transferências simbólicas, opacas, fora do mapa ou pontuais;
  - o fato de o sistema cumprir o piso de sobrevivência de **Article III-A** (*Sobrevivência*); ou
  - o fato de o sistema permanecer dentro dos limites de concentração de mercado em [Capítulo Um §11 Estrutura de Mercado](core_01.000_values_principles.md#11-market-structure);
- retirar repetidamente recursos de bases compartilhadas sem devolução proporcional, quando o gatilho de materialidade se aplicar;
- apoio que principalmente consolide captura ou concentração; e
- apoio condicionado a exigências que frustrem a transparência exigida por **Article V-A** (*Mapeamento de Dependências e Transparência dos Fluxos de Recursos*).

Lacunas documentadas no apoio contam nos termos de [Capítulo Um §6 Confiança e Confiabilidade](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity).

<a id="54-nondiscrimination-evaluation"></a>

#### 5.4 Avaliação de Não Discriminação

<details>
<summary><strong><span style="color: #2563eb;">Rastreio</span></strong></summary>

- A montante:
  - [Parte C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*conteúdo do registro*);
  - [§2](#2-system-class-evaluation) (*avaliação da classe do sistema*); família de medição da Participação (*Justiça Substantiva e Uso de Proxy de Características Protegidas e Impacto Desproporcional como medição constitucional*); **Article VI-C** (*Não Discriminação*);
  - [Justiça Substantiva](core_05.055_band_participation.md#substantive-fairness),
  - [Características Protegidas](core_05.055_band_participation.md#protected-characteristics),
  - [Uso de Proxy de Características Protegidas e Impacto Desproporcional](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact),
  - [Idioma, Cultura e Herança](core_05.040_band_continuity.md#language-culture-and-heritage),
  - [Necessidade](core_05.035_band_accountability.md#necessity), e
  - [Proporcionalidade](core_05.035_band_accountability.md#proportionality) (Capítulo Cinco).
- A montante: Princípios: Capítulo Um
  - [§3.1 Justiça](core_01.000_values_principles.md#31-fairness) (especialmente [§3.1.2 Benefícios e Ônus](core_01.000_values_principles.md#312-benefits-and-burdens)) e
  - [§11.4 Concentração de Recursos e Dependência](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (*controle de acesso; aumento de rigor em §5.4.2*).
- A jusante:
  - [CS-9.320 §9](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class) (*Aplicação ilustrativa da não discriminação por classe de sistema*);
  - [Parte C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*integridade do registro*);
  - [Parte C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*entrada verificada*);
  - [Parte B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*incompatibilidade por padrão discriminatório e evasão por proxy*).
- Leia junto com: dever de decisão e operação de **Article VI-C** (*Não Discriminação*) quando a certificação condicionar acesso a fóruns, administração ou aplicação da lei; [*Não Discriminação, Características Protegidas, Dignidade, Condicionamento por Sinais Íntimos e Status de **Article VII-E** (*Serviços sexuais comerciais consensuais entre adultos e exploração sexual*)*](core_05.055_band_participation.md#fairness-protected-characteristics-and-nondiscrimination).
- Subseções:
  - [§5.4.1](#541-evaluation-requirement) (*requisito de avaliação*);
  - [§5.4.2](#542-system-class-scaling-and-escalation) (*escalonamento e escalada por classe de sistema*);
  - [§5.4.3](#543-defects-and-misalignment) (*defeitos e incompatibilidade*);
  - [CS-9.320 §9](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class) (*Aplicação ilustrativa da não discriminação por classe de sistema*).

</details>

<br>

*Em termos simples: alguns sistemas decidem quem entra. Outros decidem quem paga mais. Outros ainda decidem quem fica em posição inferior ou carrega o maior ônus. Quando um sistema toma decisões assim de forma relevante, a certificação faz uma pergunta: o dano recai principalmente sobre sencientes com características protegidas ou sobre traços que as substituem? A afirmação do operador de que suas regras são neutras não responde à pergunta. Exemplos detalhados: [CS-9.320 §9 Aplicação ilustrativa da não discriminação por classe de sistema](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-9-illustrative-nondiscrimination-application-by-system-class).*

Esta seção se aplica quando um sistema de impacto material classifica, ordena, cobra, condiciona, exclui ou distribui materialmente ônus e benefícios entre sencientes — inclusive por meio de regras de elegibilidade, características do modelo, lógica de classificação, política de plataforma ou vias de decisão comparáveis.

A certificação de alinhamento de sistemas deve avaliar **a não discriminação** nos termos de **Article VI-C** (*Não Discriminação*), [Justiça Substantiva](core_05.055_band_participation.md#substantive-fairness) e [Uso de Proxy de Características Protegidas e Impacto Desproporcional](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact), quando o gatilho de materialidade se aplicar.

<a id="541-evaluation-requirement"></a>
##### 5.4.1 Requisito de Avaliação

*Em termos simples: este capítulo não define cotas de inclusão nem escolhe uma fórmula de justiça. Outros documentos podem tratar disso, assim como futuras adições ao corpus ou documentos elaborados por quem adota o sistema. A certificação apenas verifica se alguém realmente examinou quem recebe os benefícios, quem arca com os ônus e se há substitutos de características protegidas em funcionamento. Essa avaliação se aplica sempre que o gatilho se aplicar.*

O processo de certificação deve determinar se as vias de decisão do sistema das quais há dependência material impõem ônus, exclusões ou danos materiais a sencientes com base em qualquer um dos seguintes:

- [Características Protegidas](core_05.055_band_participation.md#protected-characteristics);
- seus proxies; ou
- agrupamentos arbitrários usados como substitutos funcionais, inclusive especializações de idioma, cultura e herança nos termos de [Idioma, Cultura e Herança](core_05.040_band_continuity.md#language-culture-and-heritage).

A avaliação deve, em escala compatível com a [aposta material](core_00.000_preamble.md#material-stake):

- testar padrões de ônus e benefícios segundo [Justiça Substantiva](core_05.055_band_participation.md#substantive-fairness); e
- testar riscos de proxy ou impacto desproporcional segundo [Uso de Proxy de Características Protegidas e Impacto Desproporcional](core_05.055_band_participation.md#protected-characteristic-proxying-and-disparate-impact).

Tratamento diferenciado só é aceitável quando justificado por [Necessidade](core_05.035_band_accountability.md#necessity), [Proporcionalidade](core_05.035_band_accountability.md#proportionality) documentadas e justiça substantiva. A avaliação deve refletir o efeito funcional, não apenas neutralidade nominal, intenção declarada ou rótulo.

<a id="542-system-class-scaling-and-escalation"></a>
##### 5.4.2 Escalonamento e Escalada por Classe de Sistema

A classe do sistema define a profundidade da avaliação. Ela não permite que alguém trate classificação ou transferência de ônus como imaterial. Sempre que o gatilho de materialidade se aplicar, valem os itens a seguir:

- **Sistemas cujas regras de desligamento, notificação ou similares podem impedir o acesso a recursos essenciais à sobrevivência:**
  - o registro deve conter a análise mais robusta de ônus, benefícios e proxies, não uma declaração genérica de boas práticas; e
  - a transferência oculta de custos não satisfaz [Capítulo Um §3.1.2 Benefícios e Ônus](core_01.000_values_principles.md#312-benefits-and-burdens).
- **Sistemas cuja lógica de correspondência ou encaminhamento afeta atendimento emergencial, benefícios ou acesso a credenciais:**
  - o registro deve documentar conclusões de impacto desproporcional e justiça substantiva de acordo com a criticidade operacional; e
  - isso importa porque a justiça prevista em [Capítulo Um §3.1 Justiça](core_01.000_values_principles.md#31-fairness) significa que os sencientes não são submetidos a regras sem explicação nem deixados com custos que outros evitam.
- **Sistemas cuja lógica de turnos, fornecedores ou reservas classifica ou exclui participantes de modo material:**
  - o sistema não pode manter um parágrafo simbólico sobre justiça no lugar de uma análise real;
  - quando a coordenação se tornar essencial à sobrevivência, a certificação deve aumentar o rigor da revisão e reclassificar segundo [§2.2 Como a classe do sistema escalona cada avaliação](#22-how-system-class-scales-every-evaluation), inclusive reclassificar para a **Classe A** quando o sistema condicionar acesso a pessoal ou encaminhamento de emergência; e
  - esse controle de acesso é um indicador de concentração nos termos de [Capítulo Um §11.4 Concentração de Recursos e Dependência](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable), porque muitos sencientes ou sistemas dependem de um único provedor sem alternativa real; por isso a certificação aumenta aqui o rigor da revisão.

<a id="543-defects-and-misalignment"></a>
##### 5.4.3 Defeitos e Incompatibilidade

Dois conjuntos de defeitos se aplicam a esta avaliação:

- **Defeitos aplicáveis à seção inteira:**
  - os defeitos de [§5](#5-rights-floor-and-domain-evaluations) (*Avaliações do Piso de Direitos e de Domínio*) se aplicam a esta avaliação; e
  - eles se aplicam à lógica material de classificação, ordenação ou alocação de ônus quando **Article VI-C** (*Não Discriminação*) exigir revisão.
- **Defeitos de não discriminação:** cada item abaixo também deve ser tratado como defeito de certificação:
  - tratar neutralidade aparente, métricas agregadas de conveniência ou autorrelato do operador como suficientes sem análise avaliável de ônus e benefícios; e
  - usar argumentos de homogeneização, interoperabilidade ou eficiência para frustrar proteções de idioma, cultura ou herança sem cumprir os testes de **Necessidade** e **Proporcionalidade** de **Article VI-C** (*Não Discriminação*).

Discriminação documentada por proxy ou injustiça substantiva conta nos termos de [Capítulo Um §6 Confiança e Confiabilidade](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity).

<a id="55-accessibility-evaluation"></a>
