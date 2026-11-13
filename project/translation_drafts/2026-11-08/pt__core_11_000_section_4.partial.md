> Rascunho de tradução assistida por IA — idioma: português brasileiro; fonte: commit 9c2c8c10c871d91157bcd27b9f56ad6a1cec90d3; status: não revisado; escopo parcial: Capítulo Onze, §4 apenas. Não é uma tradução completa do capítulo.

### 4. Requisitos de verificação e registro

<details>
<summary><strong><span style="color: #2563eb;">Rastreabilidade</span></strong></summary>

- A montante: [§2](#2-question-1--what-happened) (*registros da Pergunta 1 e guia de tipos de evento*); [Capítulos Dois a Quatro](core_02.000_definition_structure.md) (*registro, verificação e rastreabilidade das definições até os resultados*).
- A jusante:
  - [§4.1](#41-minimum-record-contents) (*conteúdo mínimo*);
  - [§4.2](#42-related-standing-record-cross-references) (*referências cruzadas*);
  - [§5](#5-record-custody-and-opening-authority) (*custódia do registro e autoridade para abri-lo*);
  - [§6](#6-handling-a-standing-record) (*tratamento de um registro de posição*);
  - [Capítulo Doze §1](core_12.000_standing_measurement.md#1-question-2--how-good-or-bad-was-it) (*Pergunta 2*).
- Leia junto com: [CF-15.415 §8 Autoridade sobre informações restritas](corpus_forum/cf_15.415_routing_operations_transfer_certification_representative_treatment.md#cf-15415-8-restricted-information-authority) (*primeiro recurso para uma disputa sobre um limite de divulgação indicado em [§4.1](#41-minimum-record-contents)*).

</details>

<br>

*Em termos simples: esta seção diz o que cada registro de posição deve conter, como registros de posição relacionados se referenciam e como os registros recebem versões. Quem pode abrir e custodiar um registro de posição, e como ele pode ser contestado ou corrigido, está em [§5 Custódia do registro e autoridade para abri-lo](#5-record-custody-and-opening-authority). As medições da Pergunta 2 só podem ser acrescentadas depois que a base factual verificada estiver registrada.*

O nível de detalhe exigido para as provas e os registros pode aumentar conforme a aposta material e a classe do sistema. Essa escala não exclui do fluxo de posição nenhum senciente, instituição ou sistema abrangido.

<a id="41-minimum-record-contents"></a>

#### 4.1 Conteúdo mínimo do registro

Um registro de posição contém os campos abaixo, e as duas últimas subseções acrescentam campos para cada eixo. O portão de dados verificados, que determina o que pode alimentar um registro de posição, está em [§2.5 Portão de dados verificados](#25-verified-input-gate). A regra que separa os fatos da Pergunta 1 da medição da Pergunta 2 está em [§2.6 Limite entre etapas](#26-stage-boundary).

<a id="411-fields-every-standing-record-must-carry"></a>

##### 4.1.1 Campos que todo registro de posição deve conter

Todo registro de posição deve incluir, no mínimo:

- o tipo de registro de posição — **registro de posição de contribuição** ou **registro de posição de violação**;
- quem ou o que está sendo avaliado e o escopo da avaliação, inclusive limites relevantes do sistema, limites de função, comunidades afetadas e relações de dependência;
- qual conduta ou constatação está sendo avaliada, incluindo os atos, omissões, deveres, impactos, evento delimitado, padrão dentro do escopo, registro de contribuição ou constatação de violação em que o registro de posição se baseia;
- o período abrangido pelo registro e o status atual da revisão — por exemplo, provisório, final para uma finalidade declarada, sob contestação, substituído ou com reavaliação periódica pendente;
- quaisquer registros de posição relacionados, com referências cruzadas conforme exigido em **§4.2**;
- os registros oficiais, testemunhas, medições, auditorias, decisões de fóruns ou outros materiais de verificação que tornem o registro de posição demonstrável, revisável e contestável de acordo com os Capítulos Dois a Quatro;
- a **autoridade que abre o registro**, que verificou a base factual e autorizou a inclusão, e o **custodiante do registro**, separado, que o incluiu e mantém, cada qual identificado conforme **§5**;
- como contestar o registro de posição, inclusive:
  - qual fórum ou autoridade o revisa;
  - quaisquer limites de divulgação; e
  - as condições para:
    - correção;
    - restauração;
    - expiração; ou
    - revisão periódica;
- os campos de medição da Pergunta 2 específicos para cada eixo, exigidos abaixo, assim que a medição ocorrer.

<a id="412-inspectable-attributable-action"></a>

##### 4.1.2 Ação atribuível e inspecionável

As provas de ação atribuível se relacionam com o registro de posição da seguinte forma:

- Para pessoal/agentes que exercem Administração de Sistema Crítico ou autoridade operacional material, as provas reconstituíveis de ação atribuível são especificadas em **[CS-16.305 §10 ação atribuível inspecionável](corpus_systems/cs_16.305_critical_system_stewardship.md#cs-16305-103-inspectable-attributable-action)** como contrato padrão de registro para equipes mistas.
- Essas provas podem alimentar este registro de posição.
- Elas não substituem este registro de posição.
- Um registro de posição não inclui os pesos de um modelo de IA (os números dentro do modelo) nem seu raciocínio privado. A única exceção ocorre quando nada mais resta para mostrar quem ou o que foi responsável.
- Uma questão não fica fora da medição de posição só por envolver a privacidade de alguém ou um estado interno protegido do sistema. Ela ainda é medida quando for relevante para uma questão de posição.

<a id="413-no-privacy-or-opacity-exemption"></a>

##### 4.1.3 Não há isenção por privacidade ou opacidade

A privacidade, a confidencialidade ou a opacidade dos componentes internos de um sistema não isenta uma questão da medição de posição. Quando esses aspectos colidirem com o requisito de registro verificado, o conflito será resolvido conforme [Capítulo Um §13.1 Princípios fundamentais de trade-off](core_01.005_interaction_interpretation.md#131-core-tradeoff-principles) e a disciplina de registro de decisões ali prevista, preservando o acesso do revisor independente.

<a id="414-additional-fields-for-contribution-standing-records"></a>

##### 4.1.4 Campos adicionais para registros de posição de contribuição

Os **registros de posição de contribuição** também devem indicar:

- a medição de contribuição da Pergunta 2, incluindo:
  - a faixa principal;
  - o slot `s`, quando atribuído (ver [Capítulo Doze §4 Gramática de slots e escala comum](core_12.000_standing_measurement.md#4-slot-grammar-and-shared-scaling));
  - a base probatória;
  - a justificativa de materialidade; e
  - qualquer calibração LEQU ou comparável adotada e usada para dar suporte transparente;
- quando a contribuição for compartilhada, como o crédito foi distribuído, considerando:
  - tempo;
  - esforço;
  - coordenação;
  - manutenção;
  - contribuição causal; e
  - trabalho de apoio menos visível;
- a medição de contribuição registrada aqui, que deverá servir de base a qualquer efeito de posição posterior do Capítulo Treze.

<a id="415-additional-fields-for-violation-standing-records"></a>

##### 4.1.5 Campos adicionais para registros de posição de violação

Os **registros de posição de violação** também devem indicar:

- a medição da violação da Pergunta 2, incluindo:
  - a autoridade responsável pela constatação ou a base do registro;
  - o impacto LEQU;
  - o slot `s`, quando atribuído (ver [Capítulo Doze §4 Gramática de slots e escala comum](core_12.000_standing_measurement.md#4-slot-grammar-and-shared-scaling));
  - o caráter do processo / da resposta, quando aplicável; e
  - qualquer status de designação do Capítulo Quatorze;
- quando vários agentes compartilham ou dividem a responsabilidade por uma violação, as razões verificadas para qualquer posição adversa registrada contra um agente específico, incluindo:
  - papel causal;
  - dever;
  - autoridade;
  - controle;
  - previsibilidade;
  - benefício;
  - ocultação; ou
  - capacidade viável de prevenção;
- quando a constatação de violação envolver omissão de divulgação ao fórum ou falha intencional no processo de impedimento (leia **§8.2.2** (*Como registrar a forma pela qual o dano foi causado*) para a disciplina de medição):
  - a base verificada da omissão ou falha;
  - o dever de divulgação ou impedimento não cumprido;
  - o conhecimento, a imprudência ou a intenção do agente, quando constatados; e
  - se a conduta afetou materialmente:
    - a legalidade do painel;
    - a independência;
    - o desafio ao impedimento;
    - a integridade das provas;
    - o prazo do recurso;
    - o roteamento de contingência; ou
    - a contestabilidade prática;
- a medição da violação registrada aqui, que deverá servir de base a qualquer efeito de posição posterior do Capítulo Treze.

<a id="42-related-standing-record-cross-references"></a>

#### 4.2 Referências cruzadas entre registros de posição relacionados

Se um registro de posição de contribuição e um registro de posição de violação disserem respeito ao mesmo sujeito, se sobrepuserem no tempo ou tratarem do mesmo evento, padrão ou decisão, cada um deverá apontar para o outro.

Cada referência cruzada deve identificar, no mínimo:

- o registro de posição relacionado e se é um registro de contribuição ou de violação;
- por que os dois registros de posição estão vinculados, inclusive quando uma constatação de violação refuta, corrige ou limita uma contribuição alegada, conforme **§2.4**;
- o que os dois registros de posição têm em comum: sujeito, evento, padrão ou decisão; e
- como seus períodos ou assuntos abrangidos se sobrepõem.

As referências cruzadas:

- devem continuar auditáveis e abertas a contestação;
- não devem substituir a medição separada;
- não devem criar uma pontuação consolidada; e
- não devem dar a entender que os dois registros de posição abrangem os mesmos assuntos ou períodos quando isso não ocorrer.

<a id="43-collective-and-actor-specific-records"></a>

#### 4.3 Registros coletivos e específicos por agente

Quando vários sencientes ou entidades compartilham o mesmo benefício ou a mesma violação, o sistema pode manter tanto um registro de posição coletivo quanto registros separados específicos por agente. Aplicam-se estas regras:

- As constatações de contribuição e violação devem permanecer em registros de posição separados, conforme **§2.1**.
- Para créditos compartilhados, o reconhecimento deve acompanhar o que cada senciente realmente contribuiu, considerando:
  - função;
  - tempo;
  - esforço;
  - risco;
  - habilidade;
  - coordenação;
  - manutenção; e
  - impacto causal.
- Quando muitos sencientes ajudaram e não for possível separar claramente as parcelas individuais, deve-se favorecer uma distribuição ampla.
- Em violações compartilhadas, a culpa não deve ser atribuída apenas pela participação no grupo.
- Uma posição adversa específica por agente exige vínculo verificado com:
  - papel causal;
  - dever;
  - autoridade;
  - controle;
  - previsibilidade;
  - benefício;
  - ocultação; ou
  - capacidade viável de prevenção.

<a id="44-versioning"></a>

#### 4.4 Versionamento

Os registros de posição devem receber versões quando qualquer um dos seguintes itens mudar:

- fatos importantes;
- constatações;
- resultados da revisão;
- status da reparação;
- provas de contribuição;
- calibração da implementação; ou
- regras constitucionais.

Uma versão posterior pode:

- atualizar o registro de posição dali em diante;
- corrigi-lo retroativamente quando estiver errado;
- fazê-lo expirar para um contexto de decisão concluído; ou
- substituí-lo para um novo contexto de decisão.

A versão posterior deve preservar o histórico de auditoria anterior e explicar o que mudou, quem fez a mudança, sob qual autoridade de abertura ou custódia de registro conforme **§5**, com base em quais materiais de verificação e a pedido de quem.

<a id="45-implementation-tools"></a>

#### 4.5 Ferramentas de implementação

As equipes podem criar ferramentas práticas para registros de posição, incluindo:

- campos de dados;
- tags;
- limiares;
- formulários;
- painéis;
- etapas de revisão; e
- **medidas padrão de contribuição** publicadas para tarefas recorrentes conforme **§13**.

Essas ferramentas devem manter os campos exigidos em **§4.1** visíveis separadamente e sujeitos a contestação. Não devem ocultá-los em uma única pontuação opaca ou rótulo escondido.
