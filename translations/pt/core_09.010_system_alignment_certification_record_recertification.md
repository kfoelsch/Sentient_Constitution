<!-- AI-assisted translation draft; unreviewed. Complete current-source Chapter Nine Part C §§8–11. Source SHA-256 514660246137f474b92cc37a717a64e0dd4f4890aca64cc95a0176b92ce28ec1. Baseline commit 247e2180509e5e029c1106878cf225067339e010; baseline SHA-256 faadaac887372f28f9b38ad506da505372ce40936796288c73d5f33f9c5317d9. Draft only; do not synchronize into translations/. -->

<a id="chapter-nine-part-c-certification-record-recertification-and-standing"></a>

# CHAPTER NINE, PART C: SYSTEM ALIGNMENT CERTIFICATION — RECORD, RECERTIFICATION, AND STANDING

<a id="8-system-certification-record"></a>

### 8. Registro de certificação do sistema

<details>
<summary><strong>Rastreabilidade</strong></summary>

- A montante:
  - [Parte B §6](core_09.005_system_alignment_certification_record_process.md#6-processo-do-fórum) (*constatações dos componentes do fórum integradas ao Registro de Certificação do Sistema*);
  - [Parte B §7](core_09.005_system_alignment_certification_record_process.md#7-resultados-da-certificação) (*o resultado e as preocupações levantadas para alcançá-lo*);
  - [Parte A §1](core_09.000_system_alignment_certification_evaluation.md#1-finalidade-e-papel) (9.000 §1) (*finalidade e visão geral do processo de certificação*);
  - [Parte A §2](core_09.000_system_alignment_certification_evaluation.md#2-avaliação-da-classe-do-sistema) (*Avaliação da Classe do Sistema*) (9.000 §2) até
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-avaliações-do-piso-de-direitos-e-de-domínio) (*resultados de avaliação refletidos no Registro de Certificação do Sistema*);
  - [Capítulos Dois a Quatro](../../core_04.000_burden_traceability_verification.md#chapter-four-burden-of-proof-traceability-and-verification) (*base de definição, ônus, rastreabilidade e verificação*);
  - [Registro de Certificação do Sistema](../../core_05.040_band_continuity.md#system-certification-record) (*significado no Capítulo Cinco*);
  - [Registro de Atos Materialmente Vinculantes](../../core_05.035_band_accountability.md#materially-binding-act-record);
  - [Integridade do Registro](../../core_05.035_band_accountability.md#record-integrity) (*regra de confiabilidade aplicada ao Registro de Certificação do Sistema*);
  - [Capítulo Oito §8 Registros de Atos e Transferências Atribuíveis](../../core_08.000_functional_independence_separation_of_duties.md#8-act-records-and-attributable-handoffs) (8.000 §8); família de medição de supervisão: verdade e integridade epistêmica como medição constitucional;
  - [**Def.O1** *Artigo XVI: Auditoria, Transparência e Verificação Independente*](../../core_05.050_band_oversight.md#defo1-transparency-auditability-and-verification).
- A jusante: [§9](#9-recertificação-e-reabertura) (*recertificação e reabertura*); [§11.3](#113-porta-de-insumo-verificado-um-registro-de-certificação-só-pode-alimentar-a-trajetória-do-capítulo-oito-quando-for-delimitado-rastreável-impugnável-e-verificado-sob) (*controle de entrada verificada*); [Capítulo Quinze §2.3](../../core_15.000_forum.md#23-forum-case-records-standing-records-and-contests) (*registros de casos do fórum e contestações de registros de standing*) (15.000 §2.3).
- Ler também:
  - [Artigo XVI: Auditoria, Transparência e Verificação Independente](../../core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification);
  - [Preservação de Evidências](../../core_05.050_band_oversight.md#evidence-preservation);
  - **[CS-6.305](../../corpus_systems/cs_06.305_information_types_and_handling.md#cs-6305-part-a-information-types-and-handling) (*Tipos de informação e tratamento*) e [CS-6.310 — Classificações de dados](../../corpus_systems/cs_06.310_data_classifications.md#cs-6310-part-b-data-classifications)**;
  - **[CS-9.305](../../corpus_systems/cs_09.305_system_classification_machinery.md#cs-9305-part-a-system-classification-machinery) (*Mecanismos de classificação de sistemas*) e [CS-9.310 — Classificações de impacto do sistema](../../corpus_systems/cs_09.310_system_impact_classifications.md#cs-9310-part-b-system-impact-classifications)**;
  - **CS-6.345** (*Ciclo de vida do sistema*);
  - **CJS-5.110 §4** (*níveis de transparência e termos de acesso à auditoria*).
- Subseções:
  - [§8.1](#81-conteúdo-mínimo-do-registro) (*Conteúdo mínimo do registro*), com
  - [§8.1.1](#811-identidade-do-sistema-escopo-e-registro-de-certificação-do-sistema-anterior) (*Identidade, escopo e registro anterior*);
  - [§8.1.2](#812-classificação-e-conclusões-sobre-o-sistema-inteiro) (*Classificação e constatações de todo o sistema*);
  - [§8.1.3](#813-registro-de-tipos-de-dados-do-sistema) (*Registro de tipos de dados do sistema*);
  - [§8.1.4](#814-piso-de-direitos-e-conclusões-de-domínio) (*Piso de Direitos e constatações de domínio*);
  - [§8.1.5](#815-evidência-técnica-e-conclusões-de-revisão) (*Evidências técnicas e constatações de revisão*);
  - [§8.1.6](#816-supervisão-independência-e-caminhos-de-contestação) (*Supervisão, independência e vias de contestação*);
  - [§8.1.7](#817-preocupações-causa-e-prontidão-para-remediação) (*Preocupações, causa e prontidão para remediação*);
  - [§8.1.8](#818-resultado-e-limites-de-confiança) (*Resultado e limites de confiança*);
  - [§8.1.9](#819-plano-operacional) (*Plano operacional*); e
  - [§8.1.10](#8110-completude) (*Completude*);
  - [§8.2](#82-transparência-e-auditabilidade-do-registro-de-certificação-do-sistema) (*Transparência e auditabilidade do Registro de Certificação do Sistema*).

</details>


*Em termos simples: um registro de certificação é o dossiê auditável de um sistema sob revisão — quem o opera, o que foi conferido, o que se achou, o que se decidiu e como impugná-lo. Não é um pacote de marketing nem um carimbo de uma linha. A profundidade do registro, a divulgação e o ônus de impugnação escalam com a classe do sistema sob o [§2.1](core_07_a_system_alignment_certification_evaluation.md) — um sistema crítico para a sobrevivência de **Class A** exige um dossiê mais pleno e mais impugnável do que uma camada de coordenação de **Class C**, embora ambos devam enunciar a classe com honestidade e refletir as avaliações exigidas.*

Um **Registro de certificação do sistema** é um registro delimitado e revisável relativo a um sistema, versão, operador ou administrador responsável, alcance, janela temporal, perfil de impacto material e contexto de decisão particulares — delimitado em alcance, delimitado no tempo e impugnável sob o significado do Capítulo Cinco em [Registro de certificação do sistema](../../core_05.040_band_continuity.md#system-certification-record).

<a id="81-minimum-record-contents"></a>

#### 8.1 Conteúdo mínimo do registro

<a id="811-system-identity-scope-and-prior-system-certification-record"></a>
##### 8.1.1 Identidade do sistema, escopo e Registro de Certificação do Sistema anterior

O registro deve identificar, no mínimo:
- o Sistema, sua Versão do Sistema, operador ou responsável, escopo certificado; a System Charter aplicável (ou a razão fundamentada para sua ausência quando imaterial); comunidades afetadas e dependências; status da revisão e, se houver Charter, se o escopo certificado coincide com o declarado nela.
- se o operador/responsável for uma Institution com Institutional Certification Record, um link por versão para rastrear os fatos institucionais usados; e o status do sistema.
- em rodada posterior, link por versão ao Registro de Certificação do Sistema concluído que o precede, mantido segundo Capítulo Oito §8, e o que mudou desde então.

<a id="812-classification-and-whole-system-findings"></a>
##### 8.1.2 Classificação e conclusões sobre o sistema inteiro

O registro deve identificar o Registro de Classificação do Sistema (ou o conteúdo exigido por CS-9.305 e CS-9.310) e os resultados das avaliações conforme [Part A §3 Whole-System Certification Evaluation](core_09.000_system_alignment_certification_evaluation.md#3-avaliação-integral-da-certificação-do-sistema): classe atribuída; justificativa; pressupostos principais, inclusive de impacto material; tipos de dependência presentes; avaliação de criticidade operacional, quando material; incerteza; intervalo de certificação escalado à classe para cada status; e, se a classificação for incerta ou contestada, a classe cautelar adotada e as condições pendentes.

Inclua os resultados materiais das avaliações de sistema inteiro: escopo sistêmico, invocação conjunta de privacidade, saída, assembleia e dissenso, consistência temporal, governança, incentivos e contestabilidade quando implicados. Se o risco sistêmico estiver no escopo, registre os resultados da avaliação de risco e pressupostos; a postura de divulgação (destinatário/roteamento, momento frente a decisões materiais e retenções justificadas com substitutos utilizáveis); e defeitos ou condições quando a avaliação/divulgação estiver incompleta. Esses resultados ficam neste registro; não criam registro separado de divulgação de risco nem um quinto registro obrigatório de componente.

<a id="813-system-data-types-record"></a>
##### 8.1.3 Registro de tipos de dados do Sistema

Identifique o Registro de Tipos de Dados do Sistema, ou o conteúdo exigido por CS-6.305/CS-6.310, produzido ou verificado sob [Part A §3.4 Data Types and Handling Evaluation](core_09.000_system_alignment_certification_evaluation.md#34-avaliação-de-tipos-e-tratamento-de-dados), incluindo tipos materiais; justificativa para dados ambíguos ou de múltiplos tipos; controles de separação e de vínculo entre domínios; postura de tratamento, retenção, ciclo de vida e garantia de infraestrutura; capacidade de atribuição suficiente para Attributable Action e Attribution Integrity; e a reavaliação programada mais recente conforme CS-6.305 §§5 e 8 (data/ciclo, cadência proporcional à classe e ao impacto, e reclassificações materiais). Registre restrições justificadas de divulgação/acesso de auditoria e substitutos públicos requeridos. Se a linha de base Type O se aplicar, explique como a Public Oversight Baseline Disclosure cobre o escopo certificado, campos da System Charter utilizados, conclusões de fronteira e lacunas ou condições.

<a id="814-rights-floor-and-domain-findings"></a>
##### 8.1.4 Piso de Direitos e conclusões de domínio

Para cada proteção da tabela [Part A §5 Rights-Floor and Domain Evaluations](core_09.000_system_alignment_certification_evaluation.md#5-avaliações-do-piso-de-direitos-e-de-domínio) cujo gatilho se aplique, indique o gatilho de materialidade, escopo e conclusões: se certificação/confiança contínua exclui ou enfraquece materialmente essenciais à sobrevivência, acesso educacional ou Safe Conditions; pegada ecológica (pressupostos de atribuição, limites de ciclo de vida/dependência, ônus, divulgação e conclusões ambientais exigidas); apoio entre sistemas (escopo do mapa/fluxos, integridade e atualidade do mapa/registro e disponibilidade de auditoria, extração e retornos, adequação do apoio e justiça distributiva); não discriminação (padrões de ônus/benefício, características protegidas, discriminação por proxy e justiça substantiva); acessibilidade (participação substantiva, acomodação e prevenção de negação por proxy); capacidade educacional (construção de capacidade, retreinamento, transparência/contestabilidade de avaliação e prevenção de proxy/manipulação); confiabilidade (falsa confiança, incentivos perversos, caminho de contestação e integridade da recuperação). Registre ainda incerteza, conclusões de componentes atribuídos, limites justificados de divulgação com substitutos públicos e condições/limites de confiança/gatilhos de reabertura ligados a dano persistente.

<a id="815-technical-evidence-and-review-findings"></a>
##### 8.1.5 Evidência técnica e conclusões de revisão

Identifique padrões, testes, medições, incerteza, margens de segurança, modos de falha, testes de segurança e bases de evidência materiais. Inclua resultados de regressão de cada recertificação (escopo, suítes padrão/personalizadas, resultados, falhas conhecidas, correções e risco residual aceito com justificativa) e o pacote de evidências do ciclo exigido por CS-6.345: escopo, classificação, testes, risco residual, prontidão para remediação, monitoramento e mudanças materiais desde o registro anterior. Registre também considerações de partes interessadas, Piso de Direitos, acessibilidade, dependência e participação; exposição/atribuição ecológica, dependência de precondições ambientais, ônus de ciclo de vida, dever de restauração e revisão ambiental quando materiais; e riscos de captura, autorrevisão, incentivos desalinhados, controle de evidências e obstrução de contestação.

<a id="816-supervision-independence-and-challenge-paths"></a>
##### 8.1.6 Supervisão, independência e caminhos de contestação

Identifique a família de fóruns/autoridade que emitiu, adotou, encaminhou, enviou para decisão, suspendeu ou revisou cada componente, e a sequência supervisora da Parte B §6.2. Registre os quatro assentos exigidos pelo Capítulo Oito (iniciador, verificador/autorizador, registro e contestação), titulares, autoridade e versão vigente do Charter Role Map; toda recusa, delegação, substituto, fusão permitida ou desvio emergencial; e informação suficiente sobre linhas de controle para demonstrar que operador/proponente não verificou a própria alegação nem controlou sua contestação. Nomeie os caminhos de contestabilidade de §10 e a cadeia da Parte B §6.3, mostrando como partes afetadas podem contestar em cada etapa.

<a id="817-concerns-cause-and-remediation-readiness"></a>
##### 8.1.7 Preocupações, causa e prontidão para remediação

Registre toda objeção, dissenso, preocupação ou contestação levantada na revisão ou ao decidir o resultado, independentemente de quem a levantou e do caminho usado. Para cada uma, indique autor (ou anonimato/confidencialidade), conteúdo, resolução ou razão para permanecer aberta, e condição/limite/gatilho resultante. Publique o log de manifestações da Parte B §6.2.4. Quando houver desalinhamento/defeito, indique se a causa é de projeto, operação ou ainda não determinada e as evidências. Quando houver remediação, registre conclusões de disposição e capacidade com evidências, etapa de comprovação, prazo, verificação independente e conclusão sob §7.3. Em recusa/revogação, registre razões, proteção provisória e limites de confiança sob §7.4.

<a id="818-outcome-and-reliance-limits"></a>
##### 8.1.8 Resultado e limites de confiança

Identifique, no mínimo: o resultado sob [Part B §7 Certification Outcomes](core_09.005_system_alignment_certification_record_process.md#7-resultados-da-certificação); se o sistema tem certificação provisória ou plena, ou está Não Certificado; o intervalo aplicável; gatilhos de reabertura; limites de confiança.

<a id="819-operating-plan"></a>
##### 8.1.9 Plano operacional

O mesmo Registro de Certificação do Sistema deve conter plano operacional conciso, proporcional à classe e ao impacto material; não se exige documento separado. Deve indicar o escopo, população e duração autorizados; vencimento, próxima recertificação e prazo da auditoria intermediária ([Chapter Fifteen §6 Timely resolution, materiality tiers, and anti-delay discipline](../../core_15.000_forum.md#review-cadence)); para primeiro go-live/expansão material, go-live mais cedo permitido, intervalo de aviso e justificativa ([Part B §7.1 Go-Live Gate](core_09.005_system_alignment_certification_record_process.md#71-barreira-de-entrada-em-operação)); para cada condição, prazo, responsável, evidência de conclusão/continuidade, verificador independente e consequência do descumprimento; responsáveis por monitorar resultados e salvaguardas, evidências/indicadores, frequência de verificação e achados/limites que exigem ação ou reabertura; quem responde a incidentes, contestações e condições não cumpridas, janelas aplicáveis e autoridade para proteção provisória, contenção, reversão ou limites de confiança; e, para defeitos, correção, critérios/resultados de verificação, incerteza restante e confiança provisória permitida. Para sistema Não Certificado, declarar go-live proibido, eventual confiança provisória autorizada separadamente, correções e pré-requisitos de nova revisão; sem sugerir permissão de operação certificada.

Evidências operacionais e achados posteriores de cumprimento de condições são acrescentados como links conforme [Chapter Eight §8 Act Records and Attributable Handoffs](../../core_08.000_functional_independence_separation_of_duties.md#8-act-records-and-attributable-handoffs); não alteram no lugar um registro concluído. Métodos detalhados continuam com seus responsáveis, inclusive [CS-6.345 — System lifecycle](../../corpus_systems/cs_06.345_design_testing_verification_deployment.md#cs-6345-system-lifecycle).

<a id="8110-completeness"></a>
##### 8.1.10 Completude

O registro é incompleto se omitir conclusões de qualquer avaliação aplicável: Part A §§2, 3 e 3.4 para todo sistema com impacto material; cada subseção de §4 cujo locus ou princípio esteja implicado; e cada domínio de §5 cujo gatilho se cumpra. As conclusões devem refletir o que a avaliação realmente encontrou, não títulos de seção nem declaração do operador. Também é incompleto se omitir preocupação, objeção ou dissenso levantado durante a revisão ou ao decidir o resultado, mesmo que não o tenha alterado.

<a id="82-transparency-and-auditability-of-the-system-certification-record"></a>
#### 8.2 Transparência e auditabilidade do Registro de Certificação do Sistema
*Em termos simples: o Registro de Certificação do Sistema só funciona se os sencientes puderem lê-lo e verificá-lo. Esta seção aplica transparência e auditabilidade ao próprio registro como requisitos concretos, não ideais abstratos. No eixo de **supervisão** da Tétrade, supervisão exige auditoria. A certificação de alinhamento do sistema é um processo de auditoria especialmente grande e deve cumprir aqui esses patamares. Ela não assume nem substitui o [Artigo XVI](../../core_06.010_rights_part_c.md#article-xvi-audit-transparency-and-independent-verification) (*Auditoria, Transparência e Verificação Independente*) ou outros modos de auditoria. O terceiro requisito, de que sencientes possam contestar, consta em [§10 Contestação de uma Certificação](#10-contestação-da-certificação).*
Esta seção aplica [Transparência](../../core_05.050_band_oversight.md#transparency) e [Auditabilidade](../../core_05.050_band_oversight.md#auditability) aos Registros de Certificação do Sistema. São as partes “acessível” e “reconstruível” da [Integridade do Registro](../../core_05.035_band_accountability.md#record-integrity), que abrange todo o Registro de Certificação do Sistema ([§8 Registro de Certificação do Sistema](#8-registro-de-certificação-do-sistema)). Os locais canônicos dos termos e os limites de responsabilidade estão no [Preâmbulo — registro de responsáveis constitucionais](../../core_00.000_preamble.md#4-principles-definitions-and-rights) e na [Hierarquia de Autoridade e Interna](../../core_05.045_band_integrative.md#owner-non-relocation). Conforme a [Tétrade Constitucional](../../core_00.000_preamble.md#constitutional-tetrad):
**Auditabilidade** — os sencientes devem poder reconstruir e verificar o Registro de Certificação do Sistema:
  - o que mudou entre as Versões do Registro, quem fez cada mudança, com que autoridade e a pedido de quem; e, para um novo registro, o que mudou desde o Registro de Certificação do Sistema concluído que ele sucede;
  - [§8](#8-registro-de-certificação-do-sistema) (*o Registro de Certificação do Sistema concluído que cada recertificação ou revisão reaberta sucede*);
- Desdobramentos: [§11.3](#113-porta-de-insumo-verificado-um-registro-de-certificação-só-pode-alimentar-a-trajetória-do-capítulo-oito-quando-for-delimitado-rastreável-impugnável-e-verificado-sob) e [§11.5](#115-registro-de-standing-por-violação) (*filtro de entrada verificada quando os fatos dão suporte a conclusões adversas*); [Capítulo Quinze](../../core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction) (15.000) (*supervisão de fórum reaberta*); [Capítulo Onze](../../core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened) (11.000).
  - [§9.1](#91-calendário-de-recertificação-e-novo-registro-de-certificação-do-sistema) (*calendário de recertificação e novo Registro de Certificação do Sistema*);

<a id="9-recertification-and-reopening"></a>

### 9. Recertificação e reabertura

<details>
<summary><strong><span style="color: #2563eb;">Rastreabilidade</span></strong></summary>

- Fontes anteriores:
  - [Parte B §7](core_09.005_system_alignment_certification_record_process.md#7-resultados-da-certificação) (*o resultado em vigor*);
  - [§8](#8-registro-de-certificação-do-sistema) (*o Registro de Certificação do Sistema concluído que cada recertificação ou revisão reaberta segue*);
  - [Parte A §2](core_09.000_system_alignment_certification_evaluation.md#2-avaliação-da-classe-do-sistema) (9.000 §2) até
  - [§5](core_09.000_system_alignment_certification_evaluation.md#5-avaliações-do-piso-de-direitos-e-de-domínio) (*classificação incorreta, desalinhamento e defeitos encontrados na avaliação*);
  - [§10](#10-contestação-da-certificação) (*contestação confiável*);
  - [Dois Objetivos Constitucionais](../../core_00.000_preamble.md#two-constitutional-aims);
  - [Capítulo Três §1](../../core_03.000_definition_integrity.md#1-definition-integrity-and-anti-evasion-constraints) (3.000 §1) e
  - [§2](../../core_03.000_definition_integrity.md#2-non-compliance-from-observable-system-behavior) (*integridade das definições e evasão*);
  - [Carta do Sistema](../../core_05.040_band_continuity.md#system-charter) (*divergência entre a Carta do Sistema e o comportamento, e revisão vencida*).
- Efeitos posteriores: [§11.3](#113-porta-de-insumo-verificado-um-registro-de-certificação-só-pode-alimentar-a-trajetória-do-capítulo-oito-quando-for-delimitado-rastreável-impugnável-e-verificado-sob) e [§11.5](#115-registro-de-standing-por-violação) (*porta de entrada verificada quando os fatos sustentam conclusões adversas*); [Capítulo Quinze](../../core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction) (15.000) (*supervisão do fórum reaberto*); [Capítulo Onze](../../core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened) (11.000).
- Leia junto com: **[CS-6.305 §5](../../corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Reclassificação e governança do ciclo de vida*) e **[CS-9.305 §3](../../corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)** (*Requisito de reclassificação*).
- Subseções:
  - [§9.1](#91-calendário-de-recertificação-e-novo-registro-de-certificação-do-sistema) (*calendário de recertificação e o novo Registro de Certificação do Sistema*);
  - [§9.2](#92-gatilhos-para-reabertura) (*gatilhos para reabertura*);
  - [§9.3](#93-certificação-provisória-e-plena) (*certificação provisória e plena*, incluindo
  - [§9.3.1 Os dois status](#931-os-dois-status),
  - [§9.3.2 Falha e rebaixamento](#932-falha-e-redução-de-status),
  - [§9.3.3 Causa do desalinhamento](#933-causa-do-desalinhamento),
  - [§9.3.4 Prazos por nível](#934-prazos-por-nível),
  - [§9.3.5 Dependência da Classe A](#935-confiança-em-classe-a), e
  - [§9.3.6 Verificação, não afirmação](#936-verificação-não-afirmação));
  - [§9.4](#94-não-evasão) (*não evasão*).

</details>


*Em termos simples: nenhum resultado dura para sempre. Enquanto o sistema opera, responsáveis identificados monitoram resultados reais e salvaguardas, respondem a incidentes e contestações e cumprem as condições de certificação do registro. Um sistema certificado é recertificado segundo calendário definido por sua classe, com auditoria no ponto médio de cada intervalo. A revisão reabre quando fatos materiais mudam ou uma contestação confiável exige. Defeitos levam a proteção, correção e verificação independente. Cada rodada de revisão inicia um novo Registro de Certificação do Sistema ligado ao anterior; o novo não apaga o anterior nem as contestações contra ele. Uma aprovação antiga não substitui a conformidade atual com o Piso de Direitos.*
**Validação.** O Capítulo Quinze chama a revisão de fórum de um sistema existente de *validação contínua de alinhamento*. Neste capítulo, validação não é processo separado. É uma rodada de certificação de sistema já em operação: recertificação, revisão reaberta ou nova revisão. Ela segue [Parte B §6 Processo do Fórum](core_09.005_system_alignment_certification_record_process.md#6-processo-do-fórum), como qualquer rodada, e termina em resultado nos termos de [Parte B §7 Resultados da Certificação](core_09.005_system_alignment_certification_record_process.md#7-resultados-da-certificação).
**Monitoramento e resposta.** Operadores e responsáveis devem executar o plano operacional do Registro de Certificação do Sistema conforme [§8.1 Conteúdo mínimo do registro](#81-conteúdo-mínimo-do-registro). Os responsáveis identificados devem:

- preservar evidências de monitoramento;
- investigar incidentes e indicadores materiais;
- encaminhar desafios à autoridade designada; e
- executar a proteção provisória e o trabalho corretivo exigidos.

Qualquer item abaixo que questione materialmente o alinhamento exige revisão tempestiva do fórum nos termos desta seção; não pode esperar a próxima recertificação programada:

- um incidente;
- uma condição de certificação não cumprida;
- uma etapa probatória perdida nos termos de [Parte B §7.3 Prontidão para remediação: disposição e capacidade de corrigir](core_09.005_system_alignment_certification_record_process.md#73-prontidão-para-remediação-disposição-e-capacidade-de-corrigir);
- evidência falsa de prontidão; ou
- um desafio crível.

Correção, cumprimento e liberação de condições de certificação seguem os requisitos de verificação independente de [Parte B §7 Resultados da certificação](core_09.005_system_alignment_certification_record_process.md#7-resultados-da-certificação).

<a id="91-recertification-schedule-and-the-new-system-certification-record"></a>
#### 9.1 Calendário de recertificação e novo Registro de Certificação do Sistema
*Em termos simples: a certificação não dura para sempre. A recertificação vence conforme calendário definido pela classe do sistema, com auditoria no meio de cada intervalo. Cada rodada abre um novo Registro de Certificação do Sistema ligado ao anterior.*
Um **Registro de Certificação do Sistema** deve ser recertificado na cadência definida para sua classe em [Capítulo Quinze §6 Resolução tempestiva, níveis de materialidade e disciplina contra atrasos](../../core_15.000_forum.md#review-cadence) (*Cadência de revisão*) e auditado no ponto médio dessa cadência.
**Novo registro a cada rodada de certificação.** Cada rodada posterior (recertificação, revisão reaberta ou nova revisão) abre um novo Registro de Certificação do Sistema. O novo registro:
- liga-se ao Registro de Certificação do Sistema concluído que o precede e informa o que mudou desde então ([§8.1.1 Identidade do sistema, escopo e Registro de Certificação do Sistema anterior](#811-identidade-do-sistema-escopo-e-registro-de-certificação-do-sistema-anterior)); e
O Registro de Certificação do Sistema concluído permanece como estava ([§8 Registro de Certificação do Sistema](#8-registro-de-certificação-do-sistema)). Continua sendo o registro do período abrangido e sujeito a contestação conforme [Parte B §6.3 Cadeia de contestabilidade](core_09.005_system_alignment_certification_record_process.md#63-cadeia-de-contestabilidade). O status da certificação, a quantidade de recertificações sem falhas e os indicadores de monitoramento são carregados pelo vínculo. São verificados no novo Registro de Certificação do Sistema conforme [§9.3 Certificação provisória e plena](#93-certificação-provisória-e-plena).

<a id="92-reopening-triggers"></a>

#### 9.2 Gatilhos para reabertura

Um **Registro de certificação do sistema** é **delimitado em alcance** e **delimitado no tempo**. A revisão reabre sob o Capítulo Quinze e os deveres de implementação de sistema incorporados quando qualquer dos seguintes for material:

- **Gatilhos gerais:**
  - mudança material no sistema, no seu uso ou no seu contexto de operação;
  - conduta oculta;
  - crescimento da dependência, incluindo maior confiança no sistema e maior extração das bases compartilhadas, inclusive concentração acima do limite definido pelo adotante em [Chapter One §11.4](../../core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (a elevação de nível não espera esse limite; Parte A §2.2);
  - queda significativa nos fluxos de retorno do sistema às bases compartilhadas, conforme Apoio Proporcional entre Sistemas;
  - risco novo;
  - histórico de incidentes;
  - evidência de partes afetadas;
  - impugnação credível sob o [§14](#10-contestação-da-certificação);
  - objeção ecológica;
  - desalinhamento de classe do sistema ou reavaliação vencida sob **[CS-3 §3.5](../../corpus_systems/cs_09.305_system_classification_machinery.md#35-reclassification-requirement)**;
  - desalinhamento de tipo de dados ou de manejo, reavaliação periódica de tipos de dados vencida ou pulada sob **[CS-2 §5.2](../../corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)**;
  - desalinhamento de classificação;
  - emenda de [Carta](../../core_05.040_band_continuity.md), descompasso carta–conduta, operação materialmente fora do alcance da Carta, ou revisão periódica da Carta vencida;
  - violação de governança de uma Instituição cujo portfólio inclui o Sistema (determinação de falha de governança, negativa ou revogação por fundamento de governança, ou conclusão causal que atribui à Instituição o desalinhamento de outro Sistema); só reabre se material, conforme [Capítulo Dez §9.6](../../core_10.000_institutional_alignment_certification.md#96-reopening-the-institutions-systems);
- **Desalinhamento de domínio** refletido no registro de certificação, inclusive:
  - defeito ou desalinhamento material de avaliação de risco ou de divulgação de risco sob o [§3.1](core_07_a_system_alignment_certification_evaluation.md#31-escopo-sistêmico-e-fatores-de-risco);
  - deturpação ou desalinhamento material de pegada sob o [§5](core_07_a_system_alignment_certification_evaluation.md#51-avaliação-da-pegada-ecológica);
  - desalinhamento material de padrão de discriminação ou evasão por proxy sob o [§7](core_07_a_system_alignment_certification_evaluation.md#54-avaliação-da-não-discriminação);
  - desalinhamento material de acessibilidade ou acomodação só de papel sob o [§8](core_07_a_system_alignment_certification_evaluation.md#55-avaliação-de-acessibilidade);
  - desalinhamento material de opacidade de avaliação, portaria por credencial ou obsolescência imposta sob o [§9](core_07_a_system_alignment_certification_evaluation.md#52-avaliação-da-capacidade-educacional-e-da-integridade-do-sistema-de-aprendizagem);
  - desalinhamento material de confiança falsa, incentivo perverso ou integridade de recuperação sob o [§10](core_07_a_system_alignment_certification_evaluation.md#56-avaliação-da-confiabilidade-e-da-integridade-da-dependência-do-sistema);
  - outro desalinhamento de avaliação da Parte A onde o gatilho de materialidade correspondente se aplica — inclusive [§2](core_07_a_system_alignment_certification_evaluation.md#2-avaliação-da-classe-do-sistema), [§4](core_07_a_system_alignment_certification_evaluation.md#34-avaliação-de-tipos-e-tratamento-de-dados) e [§6](core_07_a_system_alignment_certification_evaluation.md#53-avaliação-do-apoio-proporcional-entre-sistemas).

**Por que a reabertura importa.** Reabrir por desalinhamento, crescimento de dependência ou impugnação credível protege o fim **Continuidade** sob os [Dois Fins Constitucionais](core_00_preamble.md#two-constitutional-aims) onde sistemas compartilhados portam o suprimento durável de essenciais de sobrevivência, acesso educacional, vias de construção de capacidade, confiança digna ou segurança. Certificação velha não deve substituir a conformidade atual do Piso de Direitos.

<a id="93-provisional-and-full-certification"></a>
#### 9.3 Certificação provisória e plena

*Em termos simples: um sistema conquista confiança por etapas. Sistemas novos e sistemas que falharam uma avaliação começam sob controle mais rigoroso e são verificados com frequência. Só um sistema sem problema atual nem sinal de problema iminente passa à certificação plena e a um intervalo maior. Uma avaliação malsucedida o devolve ao controle mais rigoroso.*

<a id="931-the-two-statuses"></a>
##### 9.3.1 Os dois status

A certificação tem um de dois status. Cada um possui intervalo próprio, indicado no Registro de Certificação do Sistema segundo [§8.1 Minimum record contents](#81-conteúdo-mínimo-do-registro):

- **[Provisional certification](../../core_05.040_band_continuity.md#provisional-certification)** é o status da primeira certificação do sistema (inclusive sistema recém-implantado) e de sistema certificado após recertificação malsucedida, revisão reaberta ou nova revisão que encontrou desalinhamento. O intervalo provisório é menor que o intervalo pleno para a mesma classe; os limites de confiança constam do registro.
- **[Full certification](../../core_05.040_band_continuity.md#full-certification)** só é obtida na recertificação de sistema com certificação provisória e quando todos estes requisitos são satisfeitos:
  1. concluir o número exigido de recertificações provisórias limpas consecutivas: pelo menos uma, e mais para classes superiores, conforme o documento adotado;
  2. não haver desalinhamento atual: sem desalinhamento aberto, defeito não corrigido, verificação vencida ou regressão reprovada; e
  3. nenhum indicador apontar desalinhamento iminente: gatilhos e métricas de tendência do registro não mostram limite ultrapassado nem tendência nessa direção.

A certificação plena usa intervalo ajustado à classe. Continua limitada no tempo, não é aprovação permanente. Uma recertificação é **limpa** quando cumpre os requisitos 2 e 3.

<details>
<summary><strong>Guia do leitor (não operativo): status de certificação</strong></summary>

> Esta tabela resume §9.3; em caso de diferença, prevalece o texto.
>
> | | Provisória | Plena |
> |---|---|---|
> | **Quem a possui** | Primeira certificação, inclusive sistema recém-implantado; ou sistema após recertificação malsucedida/revisão que encontrou desalinhamento | Sistema que a obteve em recertificação enquanto tinha status provisório |
> | **Como se obtém** | Concedida com um resultado de certificação | Número exigido de recertificações limpas, sem desalinhamento atual nem indicador iminente |
> | **Intervalo** | Menor que o intervalo pleno da mesma classe | Ajustado à classe; ainda limitado no tempo |
> | **Se a recertificação falhar** | Aplica-se Parte B §7; próxima certificação é provisória e contagem limpa recomeça em zero | Igual |
> | **Se surgir indicador iminente** | Permanece provisória; contagem não avança | Regride para provisória |
>
</details>

<a id="932-failure-and-step-down"></a>
##### 9.3.2 Falha e redução de status

O que a recertificação, revisão reaberta ou nova revisão constata determina o status:

- Recertificação que encontra desalinhamento atual **falhou**. Aplicam-se as consequências de [Part B §7 Certification Outcomes](core_09.005_system_alignment_certification_record_process.md#7-resultados-da-certificação). A próxima certificação possível é provisória, por mais limpa que seja a verificação seguinte; a contagem limpa recomeça em zero.
- Se não há desalinhamento atual, mas há indicador de desalinhamento iminente, a recertificação não falhou, mas não é limpa. Status provisório permanece e a contagem não avança; status pleno cai para provisório.
- Revisão reaberta sob [§9 Recertification and Reopening](#9-recertificação-e-reabertura) que encontra desalinhamento tem o efeito de recertificação falha.
- Nova revisão de sistema certificado que encontra desalinhamento atual tem o mesmo efeito. Se não houver status de certificação, aplicam-se as regras de [Part B §7.4 Denial and Revocation](core_09.005_system_alignment_certification_record_process.md#74-recusa-e-revogação).

<a id="933-cause-of-misalignment"></a>
##### 9.3.3 Causa do desalinhamento

Quando avaliação, recertificação, revisão reaberta ou nova revisão encontra desalinhamento, o registro declara uma causa: **de projeto** (sistema/processo produz resultado desalinhado mesmo quando usado como previsto); **operacional** (projeto parece correto, mas a maneira de operar, alimentar ou manter gera desalinhamento); ou **ainda não determinada** (remédios para projeto e operação permanecem abertos até o fórum apurar a causa).

A conclusão causal não altera estas regras: resultados desalinhados repetidos significam desalinhamento, ainda que o projeto pareça correto no papel; projeto que produziria resultados desalinhados já é desalinhamento antes de aparecer o resultado; a causa define correção e escopo da revisão reaberta, mas nunca decide se há desalinhamento.

Se a causa for de projeto:
- a contagem de recertificações limpas permanece zero até redesign implantado e verificado;
- o fórum que encontrou a causa, ou o seguinte designado conforme [Part B §6.2 Supervisory sequence](core_09.005_system_alignment_certification_record_process.md#62-sequência-supervisora), verifica o redesign dentro da [matching intake target](../../core_05.040_band_continuity.md#tier-window), inclusive na primeira recertificação provisória;
- avaliação de componente anterior à verificação do redesign não conta para o total limpo; e
- mudar o modo de operar o sistema não satisfaz essa etapa.

Essas regras complementam os itens de redução de status acima. Operador ou senciente afetado pode pedir revisão da conclusão causal; se ela mudar, estas regras deixam de se aplicar.

<a id="934-tier-windows"></a>
##### 9.3.4 Prazos por nível

Quando avaliação inicial, recertificação, revisão reaberta ou nova revisão encontra desalinhamento: classifique o caso pelos níveis de materialidade de [Chapter Fifteen §6 Timely resolution, materiality tiers, and anti-delay discipline](../../core_15.000_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline); presuma o nível correspondente à classe (por exemplo, sistema A desalinhado presume Nível A); intake, preservação de provas, proteção provisória e decisão seguem os prazos/limites externos desse nível; e atrasos são revistos conforme essa seção.

<a id="935-class-a-reliance"></a>
##### 9.3.5 Confiança em Classe A

Em comparação com a certificação plena, a provisória tem intervalo menor e, portanto, recertificação mais cedo ([§9.3.1 Os dois status](#931-os-dois-status)); seus limites de confiança constam do registro ([§8.1 Minimum record contents](#81-conteúdo-mínimo-do-registro)). A interrupção é tratada assim:
- a certificação provisória, por si só, não exige interromper sistema cuja interrupção cortaria essenciais à sobrevivência antes de haver substitutos;
- proteção provisória e condições da Parte B §7 tratam do caso;
- o mesmo vale enquanto a contagem estiver suspensa após desalinhamento de projeto: a suspensão da contagem não interrompe por si só sistema de que sencientes dependem; e
- enquanto durar a suspensão, o fórum declara proteção provisória, condições de confiança e aviso aos dependentes.

<a id="936-verification-not-assertion"></a>
##### 9.3.6 Verificação, não afirmação

Status, contagem de recertificações limpas e indicadores de monitoramento devem ser verificados, com revisão independente aberta; a mera declaração do sistema não basta:
- indicadores não podem ser definidos de modo que desalinhamento nunca apareça;
- redesign também se verifica por evidências que outros possam conferir;
- certificação plena não elimina motivo para reabrir revisão: todos os gatilhos de [§9 Recertification and Reopening](#9-recertificação-e-reabertura) continuam; e
- evasão segue [§9.4 Non-evasion](#94-não-evasão).

<a id="94-non-evasion"></a>

#### 9.4 Não evasão

**Não evasão:** A evasão das obrigações deste capítulo é governada pelo Capítulo Três — este capítulo não reitera essa disciplina:

- [Capítulo Três §1 — Integridade da definição e restrições antievasão](core_03_definition_integrity.md#1-integridade-da-definição-e-restrições-antievasão);
- [Capítulo Três §2 — Não conformidade a partir de conduta observável do sistema](core_03_definition_integrity.md#2-não-conformidade-a-partir-de-conduta-observável-do-sistema);
- inclusive evasão de alcance e de fronteira sob [§2.1 Padrões comuns de evasão](core_03_definition_integrity.md#21-padrões-comuns-de-evasão).

*Nota de fechamento:* Nenhum passo sozinho neste processo da Parte B é novo ou radical por si — registros, divulgação, revisão, impugnação, papéis de fórum, reabertura e insumos de trajetória são ferramentas familiares de governança. O que é diferente é a **consistência**, a **supervisão** e a **prestação de contas** que as impulsionam juntas sob a [Tétrade Constitucional](core_00_preamble.md#constitutional-tetrad): a mesma disciplina se aplica entre classes de sistema e famílias de fóruns, o trabalho permanece visível e reconstruível, e os atores continuam a responder quando a certificação está errada, velha ou evasiva.

<a id="10-challenging-a-certification"></a>

### 10. Contestação da certificação

<details>
<summary><strong><span style="color: #2563eb;">Rastreabilidade</span></strong></summary>

- A montante:
  - [Parte B §6.3 Cadeia de contestabilidade](core_09.005_system_alignment_certification_record_process.md#63-cadeia-de-contestabilidade) (*a ordem de execução das vias de contestação*);
  - [Parte B §7](core_09.005_system_alignment_certification_record_process.md#7-resultados-da-certificação) (*o resultado que a contestação pode impugnar*);
  - [§8](#8-registro-de-certificação-do-sistema) (*o Registro de Certificação do Sistema que indica as vias*);
  - [Tétrade Constitucional](../../core_00.000_preamble.md#constitutional-tetrad);
  - [Artigo XXVI-C](../../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) (*Resolução tempestiva e piso contra atrasos*).
- A jusante: [§9](#9-recertificação-e-reabertura) (*uma contestação crível reabre a revisão*); [Capítulo Quinze](../../core_15.000_forum.md#chapter-fifteen-forums-and-jurisdiction) (15.000) (*as vias de fórum para o ponto contestado*).
- Subseções:
  - [§10.1](#101-quando-o-caminho-se-abre) (*quando a via se abre*); and
  - [§10.2](#102-caminhos-de-contestabilidade) (*vias de contestabilidade*).

</details>

<details>
<summary><strong><span style="color: #2563eb;">Definições · Avaliação · Conformidade</span></strong></summary>

- [contestabilidade](../../core_05.035_band_accountability.md#contestability) · [O](../../core_05.035_band_accountability.md#contestability) · [M](../../core_05.035_band_accountability.md#contestability-a) · [A](../../core_05.035_band_accountability.md#contestability-a) · [C](../../core_05.035_band_accountability.md#contestability-c)

</details>


Um Registro de Certificação do Sistema só funciona se os sencientes puderem contestá-lo quando estiver errado. A contestação deve ser real: capaz de reabrir a revisão, suspender a confiança e chegar ao fórum com autoridade sobre o ponto em disputa. Uma caixa de reclamações que nada muda não basta.

Esta seção integra a subfase VIa da Fase VI (Operar), junto com [§9 Recertificação e reabertura](#9-recertificação-e-reabertura). Explica como as partes afetadas contestam o Registro de Certificação do Sistema. A via de contestação do registro publicado abre quando o resultado é publicado, conforme [§10.1 Quando a via se abre](#101-quando-o-caminho-se-abre).

Sob a [Tétrade Constitucional](../../core_00.000_preamble.md#constitutional-tetrad), a [contestabilidade](../../core_05.035_band_accountability.md#contestability) põe a **responsabilização** em prática e mantém aberta a **participação**. Os prazos de contestação do [Artigo XXVI-C](../../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) concretizam a **tempestividade**.

As partes afetadas devem ter meios reais de contestar o Registro: ele deve indicar as [vias de contestação](#102-caminhos-de-contestabilidade) de §10.2, suficientes para contestar conteúdo, escopo, pressupostos de classificação, confiança em evidências, integridade da supervisão, resultado e confiança continuada. Os mecanismos devem funcionar e ser acessíveis, não cerimoniais. A contestação deve poder reabrir a revisão; suspender ou limitar a confiança quando houver prova crível de erro material ou risco à integridade; e chegar à família de fóruns com jurisdição legal sobre o ponto. As obrigações crescem conforme a classe do sistema e o impacto material. Não desaparecem porque o sistema é chamado experimental, interno, pessoal, isolado ou somente técnico quando há impacto material.

<a id="101-when-the-path-opens"></a>

#### 10.1 Quando o caminho se abre

*Em termos simples: o caminho de contestação deve estar aberto antes que alguém seja chamado a confiar numa certificação. Para um sistema ainda não em operação, ele se abre com o primeiro resultado. Para um sistema que já opera, já está aberto.*

Quando o caminho se abre e por quanto tempo permanece aberto:

- Para um sistema ainda não operacional, o caminho publicado de contestação do registro se abre quando o primeiro resultado de certificação é publicado, qualquer que seja o resultado. Isso permite apresentar uma contestação e suspender a confiança antes de o sistema entrar em operação, conforme [Part B §7.1 Go-Live Gate](core_09.005_system_alignment_certification_record_process.md#71-barreira-de-entrada-em-operação).
- Um sistema que já opera já tem partes interessadas. Portanto, seu caminho já está aberto ou se abre quando o registro do sistema é aberto. Isso abrange um sistema durante a janela de transição de adoção do [Article XXVIII-A](../../core_06.020_rights_part_e.md#xxviii-a-existing-instantiations-adoption-transition-window) (*Adoção faseada e continuidade do piso de direitos*) e uma certificação posterior.
- **Partes interessadas** são sentientes materialmente afetados pelo sistema ou que dependem materialmente dele, conforme apurado na avaliação, e não conforme identificados pelo operador.
- Até que o caminho se abra para um sistema ainda não operacional, o Registro de Certificação do Sistema ainda o identifica ([Part B §6.2 Supervisory sequence](core_09.005_system_alignment_certification_record_process.md#62-sequência-supervisora)). Os caminhos de componente, integridade da liderança e escalonamento em [§10.2 Contestability paths](#102-caminhos-de-contestabilidade) ficam disponíveis durante toda a revisão.
- O caminho permanece aberto enquanto o sistema tiver partes interessadas. Se surgirem partes interessadas após a certificação, a revisão reabre nos termos de [§9 Recertification and Reopening](#9-recertificação-e-reabertura).
- A alegação de que um sistema está alinhado não tem fundamento enquanto houver partes interessadas e não existir um caminho aberto para contestar o Registro de Certificação do Sistema.

<a id="102-contestability-paths"></a>

#### 10.2 Caminhos de contestabilidade

*Em termos simples: o Registro de Certificação do Sistema deve indicar onde apresentar objeções. Há uma etapa inicial ordinária, seguida de rotas ao fórum competente pela conclusão contestada, a uma instância alternativa quando a própria liderança do fórum está em questão e ao escalonamento. Se a espera puder causar dano, o contestante pode recorrer diretamente a um fórum.*

O Registro de Certificação do Sistema deve nomear os quatro caminhos de contestação abaixo, para que qualquer pessoa afetada saiba onde levar uma disputa. Eles aplicam a [Dispute sequencing](../../core_15.000_forum.md#dispute-sequencing) do Capítulo Quinze aos Registros de Certificação do Sistema. São rotas para os fóruns, não um novo fórum; o Capítulo Quinze continua determinando qual fórum tem competência. A ordem está em [Part B §6.3 Contestability chain](core_09.005_system_alignment_certification_record_process.md#63-cadeia-de-contestabilidade).

- **Caminho de contestação do registro publicado** — a primeira etapa ordinária para uma disputa ordinária sobre o Registro de Certificação do Sistema. O registro identifica a cadeira de contestação ([§6.1.1 Four seats in a certification](core_09.005_system_alignment_certification_record_process.md#611-quatro-vagas-em-uma-certificação)) e informa:
  - quem recebe a contestação;
  - como apresentá-la; e
  - que os prazos do [Article XXVI-C](../../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) (*Piso de Resolução Oportuna e Antiatraso*) começam no recebimento.

  A revisão interna do operador, a atestação do fornecedor ou a aprovação técnica não constituem esse caminho.
- **Caminho do fórum de componente** — para contestar uma conclusão do Registro de Certificação do Sistema. Segue para a família de fóruns do Capítulo Quinze competente por essa conclusão.
- **Caminho de integridade da liderança** — para contestar a condução do processo pelo fórum líder, por exemplo captura, informação oculta, revisão do próprio trabalho ou declaração prematura de conclusão da certificação. Segue o encaminhamento de Integridade, com um fórum substituto para impedir que o fórum líder julgue a si próprio.
- **Caminho de escalonamento** — para levar uma disputa a outro fórum ou a um fórum superior nos termos do Capítulo Quinze. Abrange transferência, envio de questão a outro fórum para decisão, encaminhamento substituto ou escalonamento entre famílias de fóruns. Aplica-se quando os principais interesses pertencem a outro lugar, a validade constitucional está em questão, é necessária uma correção estrutural, há impasse entre duas famílias de fóruns ou um fórum de outro modo julgaria a si próprio.

O acesso direto a um caminho de fórum continua disponível quando a demora puder pôr materialmente em risco direitos, provas, independência ou restauração prática. O uso ainda não concluído do caminho publicado de contestação do registro não pode bloquear esses caminhos nem consumir os prazos do [Article XXVI-C](../../core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) (*Piso de Resolução Oportuna e Antiatraso*).

<a id="11-relationship-to-standing"></a>

### 11. Relação com a trajetória

<details>
<summary><strong>Rastreabilidade</strong></summary>

- A montante:
  - [Part B §6](core_09.005_system_alignment_certification_record_process.md#6-processo-do-fórum) through
  - [Part B §7](core_09.005_system_alignment_certification_record_process.md#7-resultados-da-certificação) (*processo do fórum, Registro de Certificação do Sistema e resultados*);
  - [Constitutional Tetrad](../../core_00.000_preamble.md#constitutional-tetrad);
  - [Two Constitutional Aims](../../core_00.000_preamble.md#two-constitutional-aims);
  - [Verified Inputs for Standing](../../core_05.035_band_accountability.md#verified-inputs-for-standing).
- A jusante: [Capítulo Onze](../../core_11.000_standing_assessment.md#chapter-eleven-standing-records--question-1-what-happened) (*registros de trajetória e porta de insumo verificado*); [Capítulo Treze](../../core_13.000_standing_integration.md#chapter-thirteen-standing-effects-and-integration) (*efeitos e integração da trajetória*).
- Ler com: **Article III-A** (*acesso a essenciais de sobrevivência quando a certificação condiciona a entrega*).
- Subseções:
  - [§11.1](#111-o-que-a-certificação-pode-fornecer--sob-os-dois-fins-constitucionais-e-só-através-da-porta-de-insumo-verificado-do-capítulo-oito-abaixo) (*o que o Registro de Certificação do Sistema pode fornecer à trajetória*);
  - [§11.2](#112-qualquer-que-seja-o-resultado-o-sistema-fornece-insumo-de-trajetória-por-seu-registro-de-certificação-do-sistema-certificação-provisória-ou-plena-com-ou-sem-condições-certificação-condicional-ou-adiada-negativa-retirada-expiração-ou-outro-resultado-isso-inclui-a-primeira-certificação-e-um-sistema-que-nunca-teve-certificação-as-conclusões-do-processo-alimentam-a-trajetória-nos-mesmos-termos-na-primeira-rodada-e-nas-posteriores-retirada-expiração-ou-outra-perda-da-certificação-não-exclui-fatos-verificados-do-período-em-que-o-sistema-esteve-certificado-todos-os-insumos-continuam-sujeitos-à-porta-de-insumo-verificado-abaixo) (*cada resultado de certificação*);
  - [§11.3](#113-porta-de-insumo-verificado-um-registro-de-certificação-só-pode-alimentar-a-trajetória-do-capítulo-oito-quando-for-delimitado-rastreável-impugnável-e-verificado-sob) (*porta de insumo verificado*);
  - [§11.4](#114-registro-de-standing-por-contribuição) (*registro de trajetória de contribuição*); e
  - [§11.5](#115-registro-de-standing-por-violação) (*registro de trajetória de infração*).

</details>


*Em termos simples: a certificação pode alimentar a trajetória, mas não é trajetória. Um registro de certificação bom ou ruim pode fornecer fatos verificados ao Capítulo Oito — só através de uma porta estrita — e só os Capítulos Oito e Nove decidem registros e efeitos de trajetória.*

<a id="111-what-a-system-certification-record-can-pass-on-to-standing"></a>

#### 11.1 **O que a certificação pode fornecer** — sob os [Dois Fins Constitucionais](core_00_preamble.md#two-constitutional-aims), e só através da porta de insumo verificado do Capítulo Oito abaixo:

- Registros que verificam alinhamento compatível com o Piso de Direitos podem fornecer insumo verificado do lado **Florescimento**;
- Registros que documentam classificação errada, defeitos ocultos ou operação que derrota o piso podem fornecer insumo verificado do lado **Prestação de contas**.

<a id="112-every-certification-outcome"></a>

#### 11.2 Qualquer que seja o resultado, o sistema fornece insumo de trajetória por seu Registro de Certificação do Sistema: certificação (provisória ou plena, com ou sem condições), certificação condicional ou adiada, negativa, retirada, expiração ou outro resultado. Isso inclui a primeira certificação e um sistema que nunca teve certificação. As conclusões do processo alimentam a trajetória nos mesmos termos na primeira rodada e nas posteriores. Retirada, expiração ou outra perda da certificação não exclui fatos verificados do período em que o sistema esteve certificado. Todos os insumos continuam sujeitos à porta de insumo verificado abaixo.

A conclusão de que o sistema ainda não está alinhado não é, por si só, uma violação. A rodada de certificação existe para encontrar e corrigir problemas. Uma conclusão de violação é improvável quando o operador se esforça de forma consistente e honesta e não age com negligência. O insumo de trajetória requer fatos que sustentem classificação adversa e atribuição ao ator ([§11.5 Registro de trajetória de infração](#115-registro-de-standing-por-violação)); uma conclusão de prontidão de que o operador queria, mas não podia corrigir o problema, não fornece esses fatos ([Parte B §7.5 Efeitos da negativa e revogação](core_09.005_system_alignment_certification_record_process.md#75-efeitos-da-recusa-e-revogação)). Nada disso abrange negligência, ocultação ou evidência falsa.

<a id="113-verified-input-gate"></a>

#### 11.3 **Porta de insumo verificado.** Um registro de certificação só pode alimentar a trajetória do Capítulo Oito quando for delimitado, rastreável, impugnável e verificado sob:

- [§2](core_07_a_system_alignment_certification_evaluation.md#2-avaliação-da-classe-do-sistema) (*classe do sistema*);
- [§4](core_07_a_system_alignment_certification_evaluation.md#34-avaliação-de-tipos-e-tratamento-de-dados) (*tipos de dados e manejo*);
- [§5](core_07_a_system_alignment_certification_evaluation.md#51-avaliação-da-pegada-ecológica) onde for material;
- [§6](core_07_a_system_alignment_certification_evaluation.md#53-avaliação-do-apoio-proporcional-entre-sistemas) onde o gatilho de materialidade do **Artigo IV** (*Alocação de recursos, dependências e financiamento do ecossistema*) se aplica;
- [§7](core_07_a_system_alignment_certification_evaluation.md#54-avaliação-da-não-discriminação) onde o gatilho de materialidade do **Artigo V-B** (*Não discriminação*) se aplica;
- [§8](core_07_a_system_alignment_certification_evaluation.md#55-avaliação-de-acessibilidade) onde o gatilho de materialidade do **Artigo V-G** (*Acessibilidade*) se aplica;
- [§9](core_07_a_system_alignment_certification_evaluation.md#52-avaliação-da-capacidade-educacional-e-da-integridade-do-sistema-de-aprendizagem) onde o gatilho de materialidade do **Artigo VI** (*Direito à educação centrada no senciente*) se aplica;
- [§10](core_07_a_system_alignment_certification_evaluation.md#56-avaliação-da-confiabilidade-e-da-integridade-da-dependência-do-sistema) onde o gatilho de materialidade do **Artigo XIII** (*Direito a sistemas confiáveis e dignos de confiança*) se aplica;
- [§12](#82-transparência-e-auditabilidade-do-registro-de-certificação-do-sistema) e [§14](#10-contestação-da-certificação);
- Capítulos Dois a Quatro, e o processo aplicável do Capítulo Onze.

<a id="114-contribution-standing-record"></a>

#### 11.4 Registro de standing por contribuição

Uma certificação positiva, validação, recertificação, conclusão de remediação ou cumprimento ou liberação de uma condição de certificação pode fornecer entrada verificada para um **registro de standing por contribuição** quando demonstrar:

- benefício constitucional;
- gestão competente;
- prontidão para delegação segura;
- otimização do sistema;
- diligência; ou
- alinhamento constitucional.

<a id="115-violation-standing-record"></a>

#### 11.5 Registro de standing por violação

Os itens abaixo, no Registro de Certificação do Sistema, podem fornecer entrada verificada para um **registro de standing por violação** quando os fatos sustentarem classificação adversa e atribuição específica ao agente:

- retirada da certificação;
- classificação incorreta ocultada;
- recertificação malsucedida;
- teste de regressão malsucedido ou ausente na recertificação, quando exigido;
- evidência fraudulenta de certificação;
- violação material de uma condição de certificação;
- operação verificada fora do escopo certificado;
- fragilidade de infraestrutura inadequada à classe do sistema; e
- defeito material identificado em avaliação da Parte A exigida, incluindo:
  - defeito de tratamento de dados em [§3.4 Data Types and Handling Evaluation](core_09.000_system_alignment_certification_evaluation.md#34-avaliação-de-tipos-e-tratamento-de-dados);
  - defeito de avaliação ou divulgação de risco quando o risco sistêmico estava no escopo, em [§3.2.2 Defects and Misalignment](core_09.000_system_alignment_certification_evaluation.md#322-defeitos-e-incompatibilidade);
  - representação incorreta da pegada quando a divulgação era exigida, em [§5.1 Ecological Footprint Evaluation](core_09.000_system_alignment_certification_evaluation.md#51-avaliação-da-pegada-ecológica);
  - defeito de não discriminação ou discriminação por proxy em [§5.4 Nondiscrimination Evaluation](core_09.000_system_alignment_certification_evaluation.md#54-avaliação-de-não-discriminação);
  - defeito de acessibilidade ou participação substantiva em [§5.5 Accessibility Evaluation](core_09.000_system_alignment_certification_evaluation.md#55-avaliação-de-acessibilidade);
  - defeito de capacidade educacional, opacidade da avaliação, controle de acesso por credenciais ou obsolescência imposta em [§5.2 Educational Capability and Learning-System Integrity Evaluation](core_09.000_system_alignment_certification_evaluation.md#52-avaliação-da-capacidade-educacional-e-da-integridade-do-sistema-de-aprendizagem); ou
  - defeito de confiabilidade, confiança falsa, incentivo perverso, desafio inacessível ou integridade da recuperação em [§5.6 Trustworthiness and System-Reliance Integrity Evaluation](core_09.000_system_alignment_certification_evaluation.md#56-avaliação-de-confiabilidade-e-integridade-da-dependência-do-sistema).
