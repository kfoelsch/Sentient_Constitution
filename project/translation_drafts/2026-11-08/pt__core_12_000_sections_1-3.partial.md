<!-- Rascunho parcial de tradução para português brasileiro. Instantâneo da fonte: commit 9c2c8c10c871d91157bcd27b9f56ad6a1cec90d3. Redigido por IA, não revisado. Escopo: Capítulo Doze, §§1–3 apenas. -->

### 1. Questão 2 — quão bom ou ruim foi?
<details>
<summary><strong><span style="color: #2563eb;">Rastreabilidade</span></strong></summary>

- Origem: [Capítulo Onze §2](core_11.000_standing_assessment.md#2-question-1--what-happened) (*Questão 1 — registros de posição e fatos verificados*); [Capítulo Onze §2.5](core_11.000_standing_assessment.md#25-verified-input-gate) (*critério de dados verificados*); [Capítulo Onze §4](core_11.000_standing_assessment.md#4-standing-record-operational-requirements) (*requisitos do registro*); [Capítulo Onze §1](core_11.000_standing_assessment.md#1-the-three-questions) (*estrutura das três perguntas*).
- Destino:
  - [§2](#2-magnitude-and-severity-input-dimensions) (*dimensões de entrada da medição para ambos os eixos*);
  - [§3](#3-route-descriptor-catalogs-and-measurement-roles) (*catálogos de descritores de via*);
  - [§4](#4-slot-grammar-and-shared-scaling) (*gramática dos slots e escala comum*);
  - [§5](#5-constitutional-inputs-to-axis-assignment) (*encaminhamento a fontes constitucionais*);
  - [§6](#6-unified-proportional-lequ-scale--contribution-and-violation-axes) (*atribuição aos Eixos de Contribuição e Violação pela escala LEQU proporcional unificada*);
  - [§7](#7-standard-contribution-measures) (*medidas padrão de contribuição publicadas pelo adotante*);
  - [§8](#8-measurement-illustrations) (*exemplos detalhados de medição*);
  - [§9](#9-hand-off-to-question-3--cross-question-measurement-hooks) (*encaminhamento para a Questão 3*);
  - [Capítulo Treze §6.2](core_13.000_standing_integration.md#62-competency-bars-and-clearances) (13.000 §6.2) (*Questão 3 sobre contribuição — delegação segura*);
  - [Capítulo Treze §4.2](core_13.000_standing_integration.md#42-prevention--general-standing-locks) (13.000 §4.2) (*travas preventivas*);
  - [Capítulo Treze §5](core_13.000_standing_integration.md#5-lock-design-and-enforcement) (13.000 §5) (*projeto e aplicação de travas*).
- Leia também: [Capítulo Onze §4.1](core_11.000_standing_assessment.md#41-minimum-record-contents) (*campos do registro de posição verificado; não há efeitos de posição no Capítulo Onze*).

</details>

<br>

*Em termos simples: a Questão 2 mede os fatos verificados pela Questão 1. Ela pergunta **quão boa foi a contribuição?** ou **quão ruim foi a violação?** É aqui que o capítulo introduz pela primeira vez os dois eixos formais de medição: o **Eixo de Contribuição**, para ajuda verificada, e o **Eixo de Violação**, para dano verificado. Os eixos continuam separados; não são dois lados de uma pontuação líquida.*

Para decidir em qual slot se enquadra a contribuição ou violação de alguém, este capítulo mede o impacto usando uma **Unidade Equivalente à Vida (Lifespan Equivalent Unit, LEQU)**. Um LEQU equivale aproximadamente a salvar ou destruir o bem-estar de toda a vida de um senciente. Não se trata de contar corpos ou dinheiro; a pergunta é se uma ação alterou de modo significativo o bem-estar da comunidade constitucional. A mesma unidade funciona para qualquer ser senciente, humano ou não.

#### 1.1 Referência LEQU

Uma **Unidade Equivalente à Vida** (**LEQU**) é a unidade abreviada para o benefício ou perda constitucional equivalente a uma vida completa, quando uma implementação adotada precisa de uma calibração numérica.

- A unidade não depende do substrato.
- Um adotante atual pode usar uma vida humana comum como exemplo de calibração em contextos de seres humanos biológicos, mas a referência vinculante diz respeito a sencientes e à Constituição, não a uma espécie específica.

**Benefício constitucional equivalente a uma vida completa** significa um benefício verificado comparável a preservar, restaurar ou liberar toda a vida de um senciente em condições de bem-estar não trivial e compatível com direitos. **Perda constitucional equivalente a uma vida completa** significa dano, desperdício, destruição, fechamento de possibilidades, privação ou concretização de risco verificados, comparáveis a destruir, consumir indevidamente ou impedir um benefício constitucional equivalente a uma vida completa.

#### 1.2 Limites do uso de LEQU

Os limites a seguir se aplicam sempre que se usa LEQU.

- **Não é uma regra de pontuação líquida:** Não se pode «compensar» violações com contribuições nem o contrário. Cada eixo permanece independente.
- **Não é uma métrica obrigatória de vida humana:** LEQU é genérico para sencientes; aplica-se a qualquer ser consciente, não apenas a seres humanos.
- **Não é uma métrica de acusação:** Alegações, etiquetas de entrada, decisões de encaminhamento, reputação, condição desfavorecida ou desaprovação moral não fornecem benefício para o Eixo de Contribuição nem gravidade para o Eixo de Violação sem dados verificados conforme **Capítulo Onze §2.5** e calibração conforme **§6**.
- **Não é autorização para negociar direitos:** Alegações formuladas como eficiência, capacidade produtiva, inovação, redução de encargos, segurança, retaliação, resposta a emergências ou necessidade institucional devem ser reduzidas ou rejeitadas quando dependerem de:
  - coerção;
  - transferência discriminatória de encargos;
  - esgotamento ecológico;
  - trabalho não remunerado oculto;
  - falta de transparência evitável;
  - redução do Piso de Direitos;
  - captura;
  - indicadores substitutos enganosos;
  - perda de impugnabilidade; ou
  - agregação impossível de revisar.

#### 1.3 Escopo e encaminhamento exclusivos da Questão 2

Esta parte cobre somente a Questão 2, a etapa de medição. Ela recebe fatos que já foram verificados (Questão 1) e pergunta quão boa foi uma contribuição ou quão ruim foi uma violação.

- Comece pelos fatos já verificados conforme **Capítulo Onze §2** e inscritos no registro de posição conforme **Capítulo Onze §4**, e meça-os usando as dimensões da **seção 2**.
- Em seguida, atribua a cada tipo de ajuda ou dano seu nome padrão nos catálogos: o catálogo de **via de benefício** para ajuda (**seção 3.1**) e o catálogo de **via de dano** para dano (**seção 3.2**).
- Cada nome também informa quanto aquele tipo de ajuda ou dano conta para determinar *quão bom* ou *quão ruim* foi.
- As regras sobre o que decorre de um benefício estão no [lado do benefício](core_13.000_standing_integration.md#62-competency-bars-and-clearances), e as regras sobre o que decorre de um dano estão no [lado do dano](core_13.000_standing_integration.md#42-prevention--general-standing-locks).
- A Questão 3 decide o que acontece depois. Comece pelo [Capítulo Treze §3 Integração de descritores e normalização de anexos](core_13.000_standing_integration.md#3-descriptor-integration-and-attachment-normalization).

#### 1.4 Ponte para a situação de senciência

A medição da posição **não** decide se uma entidade é **senciente**.

- Disputas sobre a situação seguem para [Julgamento da Situação de Senciência](core_05.055_band_participation.md#sentience-status-adjudication) e para o [Artigo VI-B](core_06.005_rights_part_b.md#article-vi-b-sentience-status-adjudication-floor) (*Piso de Julgamento da Situação de Senciência*). Não são decididas por pontuações LEQU ou registros de classificação.
- Enquanto uma disputa de situação estiver aberta conforme [Vida Senciente Contestada](core_05.055_band_participation.md#contested-sentient-life), o **Artigo VI-B** (*Piso de Julgamento da Situação de Senciência*) inclui a entidade por padrão: ela ainda pode ser medida e apresentar um registro de posição até que a disputa seja decidida, e os operadores não podem tratar a disputa em aberto, por si só, como motivo para negar sua posição.
- Se a entidade for considerada [Senciente](core_05.055_band_participation.md#sentient), ou se sua situação for restringida ou restaurada após julgamento por uma decisão que também possa ser revisada:
  - o sujeito do registro de posição é atualizado a partir daquele momento; e
  - uma exclusão indevida não pode ser retrodatada para apagar a elegibilidade da entidade à medição nesse intervalo, salvo por meio de [Reparação e Remediação](core_05.035_band_accountability.md#redress-and-remediation).

### 2. Dimensões de entrada de magnitude e gravidade

*Em termos simples: esta seção explica o que a Questão 2 produz (**seção 2.1**) e, em seguida, lista o que deve ser examinado para medir uma contribuição verificada ou uma violação verificada (**seção 2.2**). Cada eixo é medido por conta própria. As regras de escala comum estão na **seção 4.2**, e o slot vem da escala da **seção 6**.*

A escala de slots mede a dimensão de um resultado constitucional e seu tipo. Só conta resultados verificados.

**O que a escala conta e como isso se relaciona aos testes centrais da Constituição:**

- **[Dois Fins Constitucionais](core_00.000_preamble.md#two-constitutional-aims):** ambos os eixos medem os efeitos sobre **Florescimento** e **Continuidade**. O Eixo de Contribuição os promove; o Eixo de Violação os prejudica.
- **[Duas Perguntas Fundamentais](core_00.000_preamble.md#two-fundamental-questions):** cada eixo fornece os fatos verificados para uma pergunta. Responder a uma não responde à outra; portanto, os dois eixos nunca são compensados entre si.
  - **Primeira pergunta:** o Eixo de Contribuição fornece os fatos verificados. O sistema recompensa condutas que ajudam os sencientes a florescer e perdurar, dizem a verdade e reparam danos?
    - **Conta:** benefício constitucional verificado, inclusive redução de risco verificada.
    - **Não conta:** produção bruta, prestígio, riqueza, volume de uso, velocidade ou tamanho da instituição.
  - **Segunda pergunta:** o Eixo de Violação fornece os fatos verificados. O sistema recompensa condutas que causam dano injustificável, enganam, excluem, atrasam, desperdiçam ou transferem custos a terceiros?
    - **Conta:** perda constitucional verificada, dano, desperdício, perda de opções (fechamento de possibilidades), perigo ou aumento de risco.
    - **Não conta, por si só:** situação desfavorecida, alegações ou desaprovação moral.
- **[Tétrade Constitucional](core_00.000_preamble.md#constitutional-tetrad):**
  - **Supervisão e prestação de contas:** «verificado» significa que um ator nomeado responde pela constatação e nenhuma parte verifica a própria alegação.
  - **Atuação em tempo:** atrasos evitáveis são registrados como fato separado, sem serem incorporados à dimensão da perda.

#### 2.1 O que a Questão 2 produz

Para cada eixo, a Questão 2 inscreve os seguintes elementos no registro de posição. São medições, não efeitos de posição (as consequências decididas pela Questão 3):

| **Resultado** | **Eixo de Contribuição** | **Eixo de Violação** |
| --- | --- | --- |
| **Onde é inscrito** | Registro de posição da contribuição. | Registro de posição da violação. |
| **Slot** | O slot mais alto aplicável do **Eixo de Contribuição** (`s` = 1–9). | O slot mais alto aplicável do **Eixo de Violação** (`s` = 1–9). |
| **Descritores de via** | Os **descritores de via de benefício** aplicáveis, empilhados. | Os **descritores de via de dano** aplicáveis, empilhados. |
| **Dados encaminhados à Questão 3** | Dados que definem o ponto de partida para o reconhecimento da contribuição, conforme [Capítulo Treze §6 Consequências da contribuição em segundo lugar](core_13.000_standing_integration.md#6-contribution-consequences-second). | Dados que definem a faixa padrão da trava (ponto de partida para sua intensidade), conforme [Capítulo Treze §5 Projeto e aplicação de travas](core_13.000_standing_integration.md#5-lock-design-and-enforcement). |
| **Total LEQU** | Avalie separadamente cada tipo pertinente de benefício (ecológico, sistêmico ou de recursos) e depois inscreva um total LEQU para toda a contribuição. | Avalie separadamente cada tipo pertinente de dano (ecológico, sistêmico ou perda de recursos) e depois inscreva um total LEQU para toda a violação. |

Lembrete: nada disso compensa um registro de violação em aberto. A regra de não compensação está no [Capítulo Onze §2.4 Registros de posição vinculados e regra de não compensação](core_11.000_standing_assessment.md#24-linked-standing-records-and-no-offset-bridge).

#### 2.2 Dimensões de entrada da magnitude da contribuição e da gravidade da violação

<a id="contribution-table-q1-magnitude-input-dimensions"></a>
<a id="contribution-table-q2-magnitude-input-dimensions"></a>

**Questão 2 — quão bom ou ruim foi?** Para decidir onde uma contribuição se enquadra no Eixo de Contribuição, ou onde uma violação se enquadra no Eixo de Violação (seu **slot**, de 1 a 9), e quais descritores de benefício ou dano se aplicam, examine três partes. Vários descritores podem se aplicar ao mesmo tempo e são empilhados. Inscreva os resultados no registro de posição correspondente ao eixo, como indicado na **seção 2.1**. A **seção 6** contém a escala unificada para a parte 2, igual para benefício e dano. Ela explica como estimar o benefício ou perda total em LEQU (Unidade Equivalente à Vida, aproximadamente o bem-estar de uma vida inteira) e em qual slot cada valor se enquadra. No Eixo de Contribuição, os slots estão agrupados em quatro faixas.

**1. Verifique como foi produzido.** Os dois eixos tratam disso de forma diferente:

- **Contribuição (qualidade da conduta):** pode aumentar ou limitar o benefício reconhecido: foi rastreável, evitou transferir custos a terceiros, foi realizada com cuidado e está de acordo com a Constituição? Os cinco critérios estão em [§2.2.1 Efeito da forma de produção do benefício sobre o que conta](#221-how-the-way-a-benefit-was-produced-affects-what-counts).
- **Violação (caráter da conduta):** é registrada separadamente da dimensão do impacto. Dever, negligência, engano, ocultação, obstrução da prestação de contas, coerção, violência, intenção, crueldade e facilitação estrutural determinam quem é responsável, quais salvaguardas são necessárias e como responder, mas não alteram o slot LEQU. As regras de registro de cada uma estão em [§2.2.2 Registro da forma como o dano foi causado](#222-how-the-way-a-harm-was-caused-is-recorded).

**2. Dimensione: qual é o tamanho do benefício ou da perda?** Isso determina o slot.

| **O que observar** | **Efeito** | **Onde consta** |
| --- | --- | --- |
| **Dimensão total (LEQU)** | É a medição principal e determina o slot. Para uma contribuição, é o benefício verificado total realizado, contabilizado em LEQU. Para uma violação, é a perda constitucional verificada total. A designação de má conduta do Capítulo Quatorze é decidida separadamente. | [§6 Escala LEQU proporcional unificada](#6-unified-proportional-lequ-scale--contribution-and-violation-axes) |
| **Quem é alcançado (quantidade, profundidade, vulnerabilidade)** | Ajusta a estimativa LEQU e o grau de importância do benefício ou dano (sua materialidade). | [§4.2 Regras comuns de escala de impacto](#42-shared-impact-scaling-rules); [Materialidade](core_05.050_band_oversight.md#materiality) |
| **Quanto dura (duração; durabilidade do benefício, irreversibilidade do dano)** | Ajusta a estimativa LEQU. Para contribuições, administração responsável duradoura, benefícios entre gerações ou reparação institucional duradoura apontam para os slots superiores. Para violações, traumas duradouros, perdas irreversíveis e danos duradouros à capacidade dos sencientes de agir por conta própria elevam a estimativa da perda total. | [§4.2 Regras comuns de escala de impacto](#42-shared-impact-scaling-rules) |
| **Até onde alcança (entre lugares ou instituições)** | Ajusta a estimativa LEQU. Para contribuições, por exemplo, benefício entre comunidades ou instituições, ou em escala civilizacional. Para violações, danos que se espalhem entre comunidades ou instituições, ou por uma civilização, podem elevar a estimativa da perda total. | [§4.2 Regras comuns de escala de impacto](#42-shared-impact-scaling-rules) |

**3. Nomeie os tipos de benefício ou dano (vias).** Nomeie as formas como o benefício ou dano verificado ocorreu. Mais de uma pode se aplicar e elas se empilham. As listas estão no [**Catálogo de descritores de via de benefício**](#31-contribution-route-descriptor-catalog-and-measurement-roles) e no [**Catálogo de descritores de via de dano**](#32-violation-route-descriptor-catalog-and-measurement-roles).

##### 2.2.1 Efeito da forma de produção do benefício sobre o que conta

Verifique isto antes de escolher um slot do Eixo de Contribuição:

| **O que foi constatado** | **Efeito sobre o benefício** |
| --- | --- |
| Correção rápida e verificada de um problema após a notificação | Pode contar como **diligência** (conduta cuidadosa e responsável) quando produzir benefício real e demonstrável. |
| Dano transferido a terceiros ou encargo ocultado | Limita o benefício atribuído à via contestada (a via específica à qual o benefício foi atribuído) ou o exclui. |
| Risco de captura verificado (o arranjo pode ser tomado por interesses restritos), dependência estrutural (sencientes são levados a depender dele) ou projeto de saída e aprisionamento (é difícil sair) | Limita o crédito por administração responsável. |
| Reparação verificada de uma barreira de acessibilidade ou participação | Pode elevar a importância do benefício (sua materialidade) e fundamentar o descritor de via de benefício **Acesso e Inclusão**, conforme a **seção 3.1**. |
| Recompensa significativa originada por um arranjo de incentivos contrário à Constituição, por conduta anticonstitucional ou por um processo materialmente falho | Por padrão, não conta como benefício. Nesse caso, aplique as [Regras especiais de violação do Capítulo Treze §5.4](core_13.000_standing_integration.md#54-special-violation-rules) e o limite da Transição de Adoção do [Artigo XXVIII-A](core_06.020_rights_part_e.md#incentive-alignment-adoption-transition-carve-out) (*Adoção em Etapas e Continuidade do Piso de Direitos*). |

##### 2.2.2 Registro da forma como o dano foi causado

A dimensão do dano (seu total LEQU, da parte 2 acima) determina o slot. A forma como o dano foi causado não o determina; portanto, cada tipo de conduta abaixo é registrado separadamente:

**Condutas que acrescentam perda, contabilizadas uma vez na dimensão:**

| **O que foi constatado** | **Como registrar** |
| --- | --- |
| Atraso evitável na resposta ou no encaminhamento a instância superior, quando havia dever e capacidade de agir | Registre como fato separado sobre a conduta. Qualquer perda adicional causada pelo atraso é contabilizada uma vez na estimativa LEQU. |
| Dano à integridade de um fórum (à sua imparcialidade) verificado de forma independente | Conte exatamente uma vez na estimativa LEQU. Omissão desonesta, descumprimento deliberado do processo de impedimento, coerção, perigo à liberdade e outros fatos de conduta continuam como descritores separados e não alteram o slot. |
| **Obstrução da prestação de contas** (interferência verificada nos mecanismos que permitem responsabilizar quem deve responder, como integridade das evidências, verificação, processo do fórum, registros de posição, prazos de reparação ou vias de contestação e reparação) | Continua sendo um fato de conduta registrado separadamente. Qualquer perda adicional que causar na via nomeada é contabilizada uma vez na estimativa LEQU, mas a própria etiqueta de obstrução não altera o slot. |

**Fatos de conduta registrados à parte da dimensão do dano:**

| **O que foi constatado** | **Como registrar** |
| --- | --- |
| Engano, ocultação, evasão, repetição da conduta após notificação, desconsideração imprudente, facilitação estrutural (organizar as condições para tornar o dano fácil ou provável) ou abuso de forte desequilíbrio de dependência (explorar alguém que depende muito de você) | Cada elemento permanece como fato de conduta registrado separadamente. |
| Violência, coerção, manipulação ou perigo à liberdade | Permanece registrado separadamente e pode exigir salvaguardas mais fortes, qualquer que seja o slot. |
| [Crueldade](core_05.035_band_accountability.md#cruelty) (sofrimento verificado como fim em si mesmo, ou dano gratuito ou degradante além do necessário e proporcional) | Continua como fato de conduta registrado separadamente. Pode exigir salvaguardas mais fortes e limites a reparações degradantes conforme [Capítulo Treze §4 Violação, correção e prevenção](core_13.000_standing_integration.md#4-violation-correction-and-prevention), mas não altera o slot. |

**Responsabilidade e atribuição:**

| **O que foi constatado** | **Como registrar** |
| --- | --- |
| Difusão (como a responsabilidade é distribuída: quem teve qual papel causal, autoridade ou controle; podia prever o dano; beneficiou-se dele; ocultou-o; ou podia tê-lo evitado) | Não integra o **escopo senciente** e não permite culpar ninguém por pertencer a um grupo. |
| Anuir com o dano ou deixar de resistir a ele | Só pode fundamentar uma constatação de caráter baseado em dever, agravado ou de prestação de contas coletiva quando for verificada a conexão com o ator específico exigida pelo **Capítulo Onze §§4.1 e 4.3**. |

**Recompensas desalinhadas:**

| **O que foi constatado** | **Como registrar** |
| --- | --- |
| Aceitar ou manter conscientemente uma recompensa significativa contrária à Constituição sem fazer uma denúncia protegida em tempo oportuno (denúncia protegida contra retaliação) | Registre conforme as [Regras especiais de violação do Capítulo Treze §5.4](core_13.000_standing_integration.md#54-special-violation-rules), sujeitas ao [Artigo XXVIII-A](core_06.020_rights_part_e.md#incentive-alignment-adoption-transition-carve-out) (*Adoção em Etapas e Continuidade do Piso de Direitos*). Somente a perda constitucional verificada que causar afeta o slot. |

**Limite das recompensas desalinhadas.** Este capítulo mede somente como uma recompensa desalinhada verificada (uma recompensa contrária à Constituição) afeta o Eixo de Contribuição ou o Eixo de Violação. As [Regras especiais de violação do Capítulo Treze §5.4](core_13.000_standing_integration.md#54-special-violation-rules) definem o dever de denunciar, as exclusões, as consequências de abrir mão da recompensa (perdimento), os deveres de correção e as regras de encaminhamento.

### 3. Catálogos de descritores de via e funções de medição

*Em termos simples: os dois catálogos abaixo nomeiam os tipos de ajuda verificada (**seção 3.1**) e dano (**seção 3.2**) que podem constar em um registro de posição. Um descritor informa como o benefício ou dano ocorreu; os descritores podem ser empilhados e são subordinados ao slot.*

**Regra dos descritores.** Os dois catálogos abaixo — [§3.1 Catálogo de descritores de via de contribuição e funções de medição](#31-contribution-route-descriptor-catalog-and-measurement-roles) e [§3.2 Catálogo de descritores de via de violação e funções de medição](#32-violation-route-descriptor-catalog-and-measurement-roles) — são a lista oficial de descritores para ambos os eixos. Um descritor informa **como** ocorreu o benefício ou dano verificado. Aplicam-se estas regras:

- Os descritores são empilhados e nenhum exclui outro: um registro de posição pode conter vários quando os fatos verificados justificarem.
- Eles são subordinados ao slot: o slot indica a dimensão do benefício ou dano; os descritores detalham como ocorreu, mas nunca o substituem.
- Os descritores listados são uma base, não a lista completa; o catálogo não exclui outros tipos de benefício ou dano.
- Implementações podem usar identificadores estáveis (IDs próprios e fixos) mapeados ao catálogo, mas não podem criar uma taxonomia conflitante com categorias mutuamente exclusivas que permita apenas um descritor por registro.
- Antes da verificação dos fatos, um descritor alegado pode apoiar a preservação lícita de evidências, a classificação do caso ou salvaguardas temporárias.
- Somente um descritor verificado pode ser registrado como resultado da Questão 2 ou afetar a posição.

#### 3.1 Catálogo de descritores de via de contribuição e funções de medição

<a id="benefit-route-descriptors-q1-measurement-role"></a>
<a id="benefit-route-descriptors-q1-classification-role"></a>
<a id="benefit-route-descriptors-q2-measurement-role"></a>

Estes são os descritores de via de benefício e o que cada um mede na Questão 2 (quão bom foi?). Eles se dividem em cinco domínios, com uma tabela para cada um; o catálogo de Violações em [§3.2 Catálogo de descritores de via de violação e funções de medição](#32-violation-route-descriptor-catalog-and-measurement-roles) usa os mesmos cinco domínios, na mesma ordem. A função correspondente à Questão 3, delegação segura, consta no [Capítulo Treze §6.2 Critérios de competência e autorizações](core_13.000_standing_integration.md#62-competency-bars-and-clearances).

**Completude do catálogo.** Se uma implementação mostrar vários descritores em uma linha ou sob uma etiqueta, essa linha ou etiqueta deve corresponder a todos os descritores aplicáveis. Este catálogo define somente os nomes dos descritores e o que cada um mede na Questão 2. As regras da Questão 3 (anexação, reparações, travas, autorizações e outros efeitos de posição) constam somente no Capítulo Treze.

##### 3.1.1 Segurança corporal, relações, cuidado e agência

| **Descritor de via de benefício** | **O que mede na Questão 2** |
| --- | --- |
| **Paz do corpo, da mente e/ou da comunidade** | Benefício decorrente da tranquilidade física, psicológica e comunitária. Ajusta a importância do benefício (sua materialidade). |
| **Relações Confiáveis** | Benefício de relações confiáveis, inclusive as baseadas em um dever de confiança em contextos de desigualdade entre as partes. |
| **Cuidado e Apoio à Dependência** | Cuidado verificado de sencientes que dependem de terceiros. O cuidado informal conta quando pode ser demonstrado. |
| **Acesso e Inclusão** | Benefício de participação efetiva e acessibilidade. Ajusta a importância do benefício em contextos nos quais uma parte depende muito da outra. |

##### 3.1.2 Reparação, propriedade e recursos

| **Descritor de via de benefício** | **O que mede na Questão 2** |
| --- | --- |
| **Benefício reparador e restaurador** | Benefício decorrente de reparação, compensação e redução de danos. |
| **Administração Responsável de Recursos** | Cuidado atento dos recursos materiais e compartilhamento (alocação) confiável deles. |

##### 3.1.3 Conhecimento, educação, registros e descobertas

| **Descritor de via de benefício** | **O que mede na Questão 2** |
| --- | --- |
| **Integridade da Esfera da Informação** | Fortalecimento de registros, transparência e comunicações. |
| **Educação e Desenvolvimento de Capacidades** | Benefício de aprendizagem, alfabetização e ampliação da capacidade dos sencientes de agir por conta própria. O slot segue o benefício LEQU total. |
| **Contribuição para STEM e Descobertas** | Descobertas reproduzíveis por outras pessoas e pesquisas que aumentam a segurança. |

##### 3.1.4 Sistemas e operação constitucional

| **Descritor de via de benefício** | **O que mede na Questão 2** |
| --- | --- |
| **Otimização de Sistemas** | Correção de processos que atravessam instituições e redução de riscos. |
| **Alinhamento Constitucional** | Fortalecimento do Piso de Direitos e facilitação da contestação de decisões. |

##### 3.1.5 Ecologia e diligência

| **Descritor de via de benefício** | **O que mede na Questão 2** |
| --- | --- |
| **Administração Responsável da Ecologia** | Benefício para habitats e biodiversidade e ações responsáveis em relação ao clima. |
| **Diligência** | Prevenção de riscos previsíveis e supervisão competente. |

#### 3.2 Catálogo de descritores de via de violação e funções de medição

Estes são os descritores de via de dano e o que cada um mede na Questão 2 (quão ruim foi?). Eles se dividem em cinco domínios, com uma tabela para cada um, usando os mesmos cinco domínios e a mesma ordem do [§3.1 Catálogo de descritores de via de contribuição e funções de medição](#31-contribution-route-descriptor-catalog-and-measurement-roles). Para a Questão 3, as regras de integração e anexação constam no [Capítulo Treze §3 Integração de descritores e normalização de anexos](core_13.000_standing_integration.md#3-descriptor-integration-and-attachment-normalization); as regras de prevenção e projeto das travas, no [Capítulo Treze §4.2 Prevenção — travas gerais de posição](core_13.000_standing_integration.md#42-prevention--general-standing-locks) e no [Capítulo Treze §5 Projeto e aplicação de travas](core_13.000_standing_integration.md#5-lock-design-and-enforcement).

**Completude do catálogo.** Se uma implementação mostrar vários descritores em uma linha ou sob uma etiqueta, essa linha ou etiqueta deve corresponder a todos os descritores aplicáveis. Este catálogo define somente os nomes dos descritores e o que cada um mede na Questão 2. As regras da Questão 3 (anexação, reparações, travas, autorizações e outros efeitos de posição) constam somente no Capítulo Treze.

##### 3.2.1 Segurança corporal, relações, cuidado e agência

| **Descritor de via de dano** | **O que mede na Questão 2** |
| --- | --- |
| **Má Conduta Violenta** | Violência, coerção ou perigo à liberdade são registrados separadamente do slot de impacto LEQU. Podem exigir salvaguardas reforçadas. |
| **Má Conduta em Relações Interpessoais / Dever de Cuidado** | O dano tem maior importância (maior materialidade) quando uma parte depende muito da outra. |
| **Má Conduta de Acessibilidade e Barreiras à Participação** | O dano tem maior importância (maior materialidade) quando uma parte depende muito da outra, e fatores agravantes podem ser empilhados. |
| **Má Conduta de Privacidade e Autopropriedade** | Aplicam-se fatores agravantes quando ocultação ou exploração for verificada; eles podem ser empilhados. |
| **Má Conduta de Agência e Manipulação** | Coerção, manipulação ou perigo à liberdade são registrados separadamente do slot de impacto. |

##### 3.2.2 Reparação, propriedade e recursos

| **Descritor de via de dano** | **O que mede na Questão 2** |
| --- | --- |
| **Má Conduta Corrigível por Reparação** | Registra o caráter da correção (se e como o dano pode ser reparado). O slot segue a perda LEQU total. |
| **Má Conduta Patrimonial** | Via para perda de propriedade. O slot segue a perda LEQU total. |

##### 3.2.3 Conhecimento, educação, registros e descobertas

| **Descritor de via de dano** | **O que mede na Questão 2** |
| --- | --- |
| **Má Conduta na Esfera da Informação** | Dano à Segurança ou à Verdade. Ocultação e engano permanecem fatos separados sobre como o dano foi causado (seu caráter). |
| **Má Conduta Educacional** | Dano à aprendizagem ou à capacidade dos sencientes de agir por conta própria (suas capacidades). O slot segue a perda LEQU total. |
| **Má Conduta em Pesquisa e Descobertas** | Dano à pesquisa ou às descobertas. O slot segue a perda LEQU total. |

##### 3.2.4 Sistemas e operação constitucional

| **Descritor de via de dano** | **O que mede na Questão 2** |
| --- | --- |
| **Má Conduta Sistêmica** | A difusão (responsabilidade distribuída entre atores) e a facilitação estrutural são registradas separadamente. O slot segue a perda LEQU total. |
| **Má Conduta de Obstrução da Prestação de Contas** | Abrange obstruir a prestação de contas: impedir que alguém responda por um dano. É registrada como forma de ocorrência do dano. O modo como a obstrução foi praticada (por exemplo, ocultação ou negligência) é registrado como fato separado; o slot deriva da perda LEQU total. Quando o slot estiver entre os mais altos (veja [§4.1 Tabela 1 — rótulos de exibição dos slots](#41-table-1--slot-display-labels)), o caso também pode ser registrado como **Má Conduta Anticonstitucional** e encaminhado à [Revisão de Má Conduta Anticonstitucional](core_05.035_band_accountability.md#anti-constitutional-misconduct-review) no Capítulo Quatorze. O encaminhamento não equivale à designação por má conduta anticonstitucional, que o Capítulo Quatorze decide separadamente. |
| **Má Conduta de Saída e Aprisionamento** | Inclui os aspectos da Má Conduta Sistêmica e também a difusão ou captura quando forem estruturais (inerentes ao funcionamento do sistema). |
| **Má Conduta de Ciclo de Vida e Irreversibilidade** | A irreversibilidade afeta a dimensão da perda LEQU. Ocultação ou negligência continua registrada separadamente como caráter. |
| **Má Conduta Anticonstitucional** (descritor) | Encaminha violações nos slots mais altos (veja [§4.1 Tabela 1 — rótulos de exibição dos slots](#41-table-1--slot-display-labels)) à revisão de designação do Capítulo Quatorze, sem alterar o slot de impacto. |

##### 3.2.5 Ecologia e diligência

| **Descritor de via de dano** | **O que mede na Questão 2** |
| --- | --- |
| **Má Conduta Ecológica** | A perda LEQU é ponderada pela perda da [Capacidade de Recuperação Ecológica](core_05.040_band_continuity.md#ecological-recovery-capacity) (capacidade de um ecossistema se regenerar após um dano). Pode ser empilhada com a via violenta (Má Conduta Violenta). |
| **Má Conduta Negligente** | Dever, previsibilidade e possibilidade de prevenção são registrados separadamente do slot de impacto. |
