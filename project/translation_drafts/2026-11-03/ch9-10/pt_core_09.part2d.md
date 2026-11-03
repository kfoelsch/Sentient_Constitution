##### 3.4.2 Disciplina de Privacidade

A certificação deve exigir que o tratamento de dados siga a seguinte disciplina de privacidade:

- *Tipos H, I, N, S e Y.* Para dados dos **Tipos H**, **I**, **N**, **S** e **Y**, a certificação deve verificar se o tratamento cumpre as [bases de privacidade](corpus_systems/cs_06.310_data_classifications.md#privacy-link) indicadas para cada tipo em **CS-6.305 (*Tipos e tratamento de informações*) e CS-6.310** (*Classificações de dados*), inclusive [Necessidade](core_05.035_band_accountability.md#necessity), [Proporcionalidade](core_05.035_band_accountability.md#proportionality), minimização e consentimento ou outra autorização adequada.
- *Invocação conjunta.* Quando mais de um ponto de privacidade estiver envolvido, também se aplica [§4.1 Invocação Conjunta de Privacidade (Informacional)](#41-privacy-informational-joint-invocation).
- *Rótulos não bastam.* O rótulo correto de um tipo não comprova, por si só, conformidade com a privacidade.
- *Tipos W, U e T.* Para obras dos **Tipos W**, **U** e **T**, a certificação deve verificar se o controle do criador é respeitado, inclusive:
  - retirada de uma publicação pública nos termos de [CS-6.310 Parte B §9.9](corpus_systems/cs_06.310_data_classifications.md#99-type-w-works-published) (*Tipo W: Obras, publicadas*);
  - os limites de cada concessão registrada nos termos de [CS-6.310 Parte B §9.13](corpus_systems/cs_06.310_data_classifications.md#913-commercial-grants) (*Concessões comerciais*); e
  - os [direitos reservados](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights) do criador.
- *Consentimento não implícito.* Uma concessão abrange apenas os usos que nomeia, dentro do escopo, prazo, território e meio que declara. Tudo o que ela não nomeia permanece com o criador. A certificação não pode tratar uma configuração padrão, termos agrupados, silêncio ou concessão mais ampla como consentimento para um uso não nomeado na concessão. Por exemplo, uma licença geral para publicar ou vender uma obra não é consentimento para usá-la como dado de treinamento; esse uso exige consentimento específico do próprio criador (veja os [direitos reservados](corpus_systems/cs_06.310_data_classifications.md#9133-reserved-rights)).

<a id="343-protective-storage-and-key-custody"></a>
##### 3.4.3 Armazenamento Protetivo e Custódia de Chaves

Para dados nas faixas de acesso restrito por padrão e não acessíveis, a certificação deve verificar se o sistema cumpre o requisito mínimo de armazenamento protetivo e custódia de chaves em [CS-6.305 Parte A §5.0 Faixas de Postura de Acesso](corpus_systems/cs_06.305_information_types_and_handling.md#50-access-posture-bands). O registro deve mostrar:
- onde os dados restritos e suas chaves realmente ficam, inclusive cópias de segurança, caches, logs e memória de troca;
- se o texto simples está limitado aos processos que precisam dele; e
- se os caminhos de auditoria, exportação e sobreposição de controle legal continuam funcionando.

Uma alegação de criptografia sem essas evidências não satisfaz este requisito.

<a id="344-scheduled-data-type-re-evaluation"></a>
<a id="344-periodic-data-type-re-evaluation"></a>
##### 3.4.4 Reavaliação Programada dos Tipos de Dados

Toda vez que um sistema de impacto material for certificado ou recertificado, a revisão deve verificar se seus conjuntos de dados importantes foram:

- **reavaliados** para classificação adequada nos termos de **[CS-6.305 §5.2](corpus_systems/cs_06.305_information_types_and_handling.md#52-reclassification-and-lifecycle-governance)** (*Governança da reclassificação e do ciclo de vida*) e **CJS-5.130 §18** (*termos de retenção de dados e integridade do ciclo de vida*); e
- **reclassificados** quando essa revisão assim exigiu.

A reclassificação de tipos acionada por eventos, segundo CS-6.305 (*Tipos e tratamento de informações*) e CS-6.310 (*Classificações de dados*), não substitui esta verificação de certificação programada.

<a id="345-system-class-scaled-infrastructure-assurance"></a>
##### 3.4.5 Garantia de Infraestrutura Escalonada por Classe de Sistema

Segundo [§2.2 Como a classe do sistema escalona cada avaliação](#22-how-system-class-scales-every-evaluation), CS-9.305 (*Maquinaria de classificação de sistemas*) e CS-9.310 (*Classificações de impacto do sistema*), sistemas de classe superior exigem evidências proporcionalmente mais fortes de que a infraestrutura de tratamento, armazenamento, processamento, transmissão, cópia de segurança, recuperação e monitoramento consegue preservar, sob estresse:

- a integridade da classificação;
- a atribuição; e
- a impugnabilidade.

Quando se aplicarem as presunções de visibilidade de interesse público de CS-6.305 (*Tipos e tratamento de informações*) e CS-6.310 (*Classificações de dados*), a certificação deve verificar se as restrições:

- têm escopo estrito;
- estão documentadas e são auditáveis; e
- vêm acompanhadas da substituição pública mais forte que for razoavelmente possível (por exemplo, resumo, agregado, versão desidentificada, divulgação adiada ou acesso qualificado para auditoria), de modo que aquilo que foi retido seja explicado, e não simplesmente ocultado.

<a id="346-infrastructure-robustness-for-data"></a>
##### 3.4.6 Robustez da Infraestrutura para Dados

A certificação deve avaliar se a infraestrutura de tratamento de dados é adequada aos tipos de dados e à classe de sistema em questão. Essa infraestrutura inclui:

- camadas e fluxos de processamento persistentes;
- controles de acesso;
- limites de criptografia ou isolamento;
- caminhos de cópia de segurança e restauração; e
- cadeias de delegação a operadores ou fornecedores.

Lacunas materiais na integridade do ciclo de vida, robustez adversarial, portabilidade ou recuperabilidade devem ser registradas e refletidas no resultado da certificação, nas condições de certificação ou nos limites de confiança.

<a id="347-defects-and-misalignment"></a>
##### 3.4.7 Defeitos e Incompatibilidade

Cada um dos itens a seguir deve ser tratado como defeito de certificação:

- classificação incorreta de dados;
- reestruturação evasiva;
- vinculação insegura entre domínios;
- tratamento que usa o rótulo correto de tipo, mas ainda assim rompe as proteções de privacidade exigidas por esse tipo;
- ausência de registro de quem acessou, processou ou alterou dados, impedindo a investigação de um dano significativo;
- **reavaliação programada de tipos de dados atrasada ou omitida**;
- dados restritos mantidos em texto simples no armazenamento ou fora dos limites de processamento autorizados, ou chaves acessíveis a processos que não precisam delas; e
- fragilidade da infraestrutura que previsivelmente frustra as proteções de CS-6.305 (*Tipos e tratamento de informações*) e CS-6.310 (*Classificações de dados*).

As consequências estão definidas em [§7 Resultados da Certificação](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes).

<a id="4-evaluations-where-implicated"></a>
