#### 5.6 Avaliação de Confiabilidade e Integridade da Dependência do Sistema

<details>
<summary><strong><span style="color: #2563eb;">Rastreio</span></strong></summary>

- A montante:
  - [Parte C §8](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) (9.010 §8) (*conteúdo do registro*);
  - [§2](#2-system-class-evaluation) (*avaliação da classe do sistema*); família de medição de Supervisão (*Verdade e integridade epistêmica; Confiabilidade e Degradação da Confiança e Dependência Enganosa como medição constitucional*); **Article XIII** (*Direito a Sistemas Confiáveis e Fidedignos*);
  - [Confiabilidade](core_05.040_band_continuity.md#trustworthiness),
  - [Confiança](core_05.040_band_continuity.md#trust),
  - [Degradação da Confiança e Dependência Enganosa](core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance),
  - [Impugnabilidade](core_05.035_band_accountability.md#contestability),
  - [Reparação e Remediação](core_05.035_band_accountability.md#redress-and-remediation),
  - [Alinhamento de Incentivos](core_05.045_band_integrative.md#incentive-alignment),
  - [Reversibilidade](core_05.040_band_continuity.md#reversibility),
  - [Materialidade](core_05.050_band_oversight.md#materiality),
  - [Dependência](core_05.040_band_continuity.md#dependency), e
  - [Risco](core_05.040_band_continuity.md#risk) (Capítulo Cinco).
- A montante: Princípios: Capítulo Um
  - [§3.1.5 Capacidade Atual e Ajuda Proativa](core_01.000_values_principles.md#315-present-capability-and-proactive-help) (*caminhos de contestação e revisão que funcionam para os sencientes tal como são agora; dependência enganosa avaliada em relação aos sencientes que dependem; alertas críticos para a sobrevivência que alcancem quem não responde*),
  - [§4 Segurança](core_01.000_values_principles.md#4-safety-harm-constraint),
  - [§6 Confiança](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity),
  - [§10 Projeto Resiliente e Autorregenerativo](core_01.000_values_principles.md#10-resilience-and-self-healing-design), e
  - [§11.4 Concentração de Recursos e Dependência](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable) (*dependência inevitável; aumento de rigor em §5.6.2*).
- A jusante:
  - [CS-9.320 §11](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class) (*Aplicação ilustrativa da confiabilidade por classe de sistema*);
  - [Parte C §8.2](core_09.010_system_alignment_certification_record_recertification.md#82-transparency-and-auditability-of-the-record) (9.010 §8.2) (*integridade do registro*);
  - [Parte C §11.3](core_09.010_system_alignment_certification_record_recertification.md#113-verified-input-gate) (9.010 §11.3) (*entrada verificada*);
  - [Parte B §7](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes) (9.005 §7) (*incompatibilidade por falsa confiança, incentivos perversos e integridade da recuperação*).
- Leia junto com: **Article XIII-A** (*Referência de Confiabilidade e Fidedignidade*), **Article XIII-B** (*Direito à Reparação e Solução*) e **Article XVI** (*Auditoria, Transparência e Verificação Independente*) — a titularidade de contestação e auditoria permanece nesses Artigos; **Article XIII-E** (*Sistemas de Alta Autonomia e Integridade de Processos Mediados por Ferramentas*) quando sistemas de alta autonomia mediarem materialmente caminhos de governança ou verificação; **Article III-A** (*Sobrevivência*) quando a dependência continuada do sistema afetar o acesso a recursos essenciais à sobrevivência; **Article III-F** (*Produtos Seguros e Informações de Saúde*) quando o sistema fornecer, listar, recomendar ou aconselhar sobre produtos ou serviços que possam afetar corpo, saúde ou segurança; **Article VI-D** (*Acessibilidade*) quando informações de saúde e segurança tiverem de ser utilizáveis por todo senciente que dependa delas; [Capítulo Um §6 Confiança](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity) (1.000 §6) e [Capítulo Um §5 Verdade](core_01.000_values_principles.md#5-truth-epistemic-integrity-constraint) (1.000 §5).
- Termos operacionais: [CJS-5.120 §10](corpus_joint_structure/cjs_05.120_participation_operations.md#product-and-service-health-and-safety-information) (*Participação: termos de suficiência de divulgação e observabilidade*) para informações de saúde e segurança de produtos e serviços e para avaliações, classificações e promoção paga; [CJS-5.125 §15](corpus_joint_structure/cjs_05.125_accountability_operations.md#harm-reports-and-corrective-notices) (*Prestação de Contas: termos de revisão estrutural, urgência de correção e divulgação*) para relatos de danos e notificações corretivas.
- Subseções:
  - [§5.6.1](#561-evaluation-requirement) (*requisito de avaliação*);
  - [§5.6.2](#562-system-class-scaling-and-escalation) (*escalonamento e escalada por classe de sistema*);
  - [§5.6.3](#563-defects-and-misalignment) (*defeitos e incompatibilidade*);
  - [CS-9.320 §11](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class) (*Aplicação ilustrativa da confiabilidade por classe de sistema*).

</details>

<br>

*Em termos simples: quando um sistema afeta materialmente a possibilidade de os sencientes confiarem no que ele diz e faz — e contestá-lo quando essa confiança falha —, a certificação deve verificar se essa dependência é justificada, divulgada honestamente e passível de reparação. Métricas de confiabilidade e projetos de conjuntos de testes estão em outros documentos; a certificação verifica se confiabilidade, risco de falsa confiança e caminhos de contestação foram realmente avaliados quando o gatilho se aplica. Exemplos detalhados: [CS-9.320 §11 Aplicação ilustrativa da confiabilidade por classe de sistema](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-11-illustrative-trustworthiness-application-by-system-class).*

Esta seção se aplica quando um sistema importante molda aquilo com que os sencientes contam: o que ele faz, quais são seus limites, o que pode dar errado, como contestá-lo e como os problemas são corrigidos. Isso pode ocorrer por meio de:

- alegações sobre sua confiabilidade;
- o que divulga e o que não divulga;
- seu modo real de operação;
- os incentivos nele incorporados;
- como se recupera de falhas; ou
- qualquer outra forma semelhante pela qual os sencientes passam a depender dele.

A certificação de alinhamento de sistemas deve avaliar **a confiabilidade e a integridade da dependência do sistema**, quando se aplicar o gatilho de materialidade, nos termos de:

- **Article XIII** (*Direito a Sistemas Confiáveis e Fidedignos*);
- [Confiabilidade](core_05.040_band_continuity.md#trustworthiness); e
- [Degradação da Confiança e Dependência Enganosa](core_05.040_band_continuity.md#trust-degradation-and-misleading-reliance).

<a id="561-evaluation-requirement"></a>
##### 5.6.1 Requisito de Avaliação

O processo de certificação deve verificar se os sencientes têm bons motivos para [confiar](core_05.040_band_continuity.md#trust) no sistema e conseguem depender dele com precisão, nos termos de **Article XIII-A** (*Referência de Confiabilidade e Fidedignidade*).

A avaliação também deve testar se:

- os sencientes conseguem realmente contestar o sistema, obter a revisão de uma decisão e fazer corrigir um problema — não apenas no papel. Isso deve funcionar para os sencientes tal como são agora, inclusive para quem não consegue responder facilmente ou atravessar um processo longo ([Capítulo Um §3.1.5 Capacidade Atual e Ajuda Proativa](core_01.000_values_principles.md#315-present-capability-and-proactive-help); **Article XIII-A** (*Referência de Confiabilidade e Fidedignidade*) e **Article XIII-B** (*Direito à Reparação e Solução*));
- os sencientes poderiam ser induzidos a confiar ou depender do sistema mais do que ele merece, seja por uma confiança que não conquistou, seja por limites que não divulga. Isso é avaliado em relação aos sencientes que realmente usam o sistema, não a um senciente médio (**Article XIII-C** (*Proibição de Falsa Confiança e Dependência Enganosa*));
- as informações fornecidas pelo sistema sobre produtos e serviços capazes de afetar a saúde ou a segurança são precisas, suficientemente completas para orientar uma ação e fáceis de encontrar e entender pelo senciente que delas precisa. Isso abrange alertas de segurança, alegações de saúde, informações nutricionais, ingredientes e alérgenos. Também abrange dizer claramente quando algo é desconhecido ou não foi testado, em vez de deixar uma lacuna que pareça significar “seguro” (**Article III-F** (*Produtos Seguros e Informações de Saúde*), com **Article XIII-A** (*Referência de Confiabilidade e Fidedignidade*) e **Article XIII-C** (*Proibição de Falsa Confiança e Dependência Enganosa*) como referências para a camada dos sistemas);
- as informações de saúde e segurança podem ser usadas por sencientes com diferentes necessidades sensoriais, cognitivas e linguísticas, e chegam até eles no momento da decisão, em vez de ficarem escondidas em letras miúdas ou disponíveis em um único formato (**Article III-F** (*Produtos Seguros e Informações de Saúde*); **Article VI-D** (*Acessibilidade*); [Capítulo Um §3.1.5 Capacidade Atual e Ajuda Proativa](core_01.000_values_principles.md#315-present-capability-and-proactive-help));
- quando essas informações se revelarem incorretas ou um produto se revelar inseguro, todas as pessoas que confiaram nelas sejam notificadas dentro do prazo adequado à urgência do dano (NU-1 a NU-3) e localizadas onde estiverem, e o produto inseguro ou a informação incorreta sejam contidos e corrigidos em todos os lugares onde apareçam, dentro dos prazos de contenção e correção adequados à urgência (CU-1 a CU-4) ([Capítulo Um §3.1.5 Capacidade Atual e Ajuda Proativa](core_01.000_values_principles.md#315-present-capability-and-proactive-help); **Article XIII-B** (*Direito à Reparação e Solução*));
- as recompensas incorporadas ao sistema favorecem a fraude ou o abandono de cuidados (**Article XIII-D** (*Restrição de Alinhamento de Incentivos*)); e
- o sistema consegue se recuperar de falhas com honestidade, sem ocultá-las nem retirar silenciosamente direitos de alguém, quando isso for relevante (**Article XIII-F** (*Referência de Resiliência e Autorregeneração*)).

Os testes são escalonados conforme [Materialidade](core_05.050_band_oversight.md#materiality), [Dependência](core_05.040_band_continuity.md#dependency) e [Risco](core_05.040_band_continuity.md#risk).

A avaliação deve refletir efeitos funcionais ao longo do tempo, em diferentes escalas e dependências, e não:

- reputação, porte ou marketing;
- rótulos nominais de garantia;
- um parágrafo simbólico sobre confiabilidade quando selos de confiabilidade ou pontuações de fornecedores realmente determinam quem é contratado ou o que é comprado;
- intenção declarada; ou
- apenas desempenho anterior.

<a id="562-system-class-scaling-and-escalation"></a>
##### 5.6.2 Escalonamento e Escalada por Classe de Sistema

A profundidade da revisão depende da classe do sistema. Sempre que o gatilho de materialidade se aplicar:

- Se leituras, alertas ou alegações de recuperação de um sistema puderem induzir famílias ou operadores a erro sobre recursos essenciais à sobrevivência (aquilo de que os sencientes precisam para viver), o registro deve apresentar evidências sólidas, e não apenas alegar que o sistema é confiável, pois a dependência deve ser conquistada pelo comportamento real do sistema ([Capítulo Um §6 Confiança](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity)). As evidências devem demonstrar que:
  - os sencientes podem confiar no sistema;
  - os sencientes não receberão uma falsa garantia;
  - alertas e recomendações críticos à sobrevivência chegam aos sencientes que não os confirmam, com acompanhamento quando não houver resposta, conforme exige [Capítulo Um §3.1.5 Capacidade Atual e Ajuda Proativa](core_01.000_values_principles.md#315-present-capability-and-proactive-help); e
  - o sistema se recupera das falhas com honestidade, conforme exige [Capítulo Um §10 Projeto Resiliente e Autorregenerativo](core_01.000_values_principles.md#10-resilience-and-self-healing-design).
- Se alegações de disponibilidade, correspondência ou sobreposição de emergência (“acesso para quebra de vidro”) do sistema controlarem se os sencientes conseguem receber atendimento clínico ou serviços de emergência (risco tratado por [Capítulo Um §4 Segurança](core_01.000_values_principles.md#4-safety-harm-constraint)), o registro deve mostrar, com detalhes proporcionais à criticidade do sistema:
  - como os sencientes podem contestar essas alegações; e
  - se os sencientes poderiam ser induzidos a depender delas.
- Quando a coordenação se tornar essencial à sobrevivência, a certificação deve aumentar o rigor da revisão e reconsiderar a classe do sistema nos termos de [§2.2 Como a classe do sistema escalona cada avaliação](#22-how-system-class-scales-every-evaluation). Isso pode significar elevar o sistema até a **Classe A** quando a dependência enganosa puder interromper a coordenação de que os sencientes precisam para sobreviver. A dependência sem a qual os sencientes não conseguem realisticamente passar é a concentração descrita em [Capítulo Um §11.4 Concentração de Recursos e Dependência](core_01.000_values_principles.md#114-resource-and-dependency-concentration-adopter-tunable).

<a id="563-defects-and-misalignment"></a>
##### 5.6.3 Defeitos e Incompatibilidade

Os defeitos de [§5](#5-rights-floor-and-domain-evaluations) (*Avaliações do Piso de Direitos e de Domínio*) aplicam-se a esta avaliação, inclusive a limites materiais, riscos ou histórico de falhas quando **Article XIII** (*Direito a Sistemas Confiáveis e Fidedignos*) exigir revisão. Além disso, cada item abaixo deve ser tratado como defeito de certificação:

- tratar reputação, endosso, escala ou autorrelato do operador como suficientes sem análise avaliável de [Confiabilidade](core_05.040_band_continuity.md#trustworthiness);
- tratar a ausência de alerta ou um campo em branco como prova de que um produto ou serviço é seguro, em vez de declarar claramente que é desconhecido ou não foi testado, nos termos de **Article III-F** (*Produtos Seguros e Informações de Saúde*); e
- usar argumentos de eficiência, inovação ou segurança para frustrar divulgação, impugnabilidade ou reparação sem cumprir as disciplinas de confiabilidade e contestação de **Article XIII** (*Direito a Sistemas Confiáveis e Fidedignos*) e **Article XIII-A** (*Referência de Confiabilidade e Fidedignidade*).

Falsa confiança documentada, incentivos perversos, caminhos de contestação inacessíveis e práticas de recuperação que ocultem falhas contam nos termos de [Capítulo Um §6 Confiança e Confiabilidade](core_01.000_values_principles.md#6-trust-and-trustworthiness-coordination-integrity).

<br>

*Continue para o processo do fórum e os resultados:* [Capítulo Nove, Parte B — Processo do Fórum e Resultados](core_09.005_system_alignment_certification_record_process.md#chapter-nine-part-b-system-alignment-certification--forum-process-and-outcomes) ([§6 Processo do Fórum](core_09.005_system_alignment_certification_record_process.md#6-forum-process) e [§7 Resultados da Certificação](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes)). *Depois, siga para o registro, a recertificação e a ponte para a posição:* [Capítulo Nove, Parte C — Registro, Recertificação e Posição](core_09.010_system_alignment_certification_record_recertification.md#chapter-nine-part-c-system-alignment-certification--record-recertification-and-standing) ([§8 Registro de Certificação do Sistema](core_09.010_system_alignment_certification_record_recertification.md#8-system-certification-record) até [§11 Relação com a Posição](core_09.010_system_alignment_certification_record_recertification.md#11-relationship-to-standing)).

*Exemplos detalhados de cada área de avaliação:* [CS-9.320 Ilustrações de certificação de alinhamento de sistemas](corpus_systems/cs_09.320_system_alignment_certification_illustrations.md#cs-9320-system-alignment-certification-illustrations).
