#### 7.1 Barreira de entrada em operação

*Em termos simples: a entrada em operação é uma autorização, não uma etapa de trabalho separada. Ela é concedida quando o sistema está certificado, o intervalo de notificação transcorreu e as condições exigidas antes da entrada em operação foram verificadas de forma independente. As condições indicam o que deve ser feito antes da operação, o que deve ser mantido durante a operação e que trabalho corretivo pode vir depois dentro de um escopo delimitado.*

**Sem [entrada em operação](core_05.040_band_continuity.md#go-live) antes da certificação.** Um sistema que afetaria materialmente os sencientes, ou no qual os sencientes confiariam materialmente, não entra em operação até que todas estas condições sejam satisfeitas:

- **Certificado:** seu Registro de Certificação do Sistema contém certificação provisória ou plena, com ou sem condições;
- **Publicado, com a via de contestação aberta:** o resultado concluído foi publicado de forma acessível, e a via de contestação do registro publicado sob a [Parte C §9.1 Contestação de uma certificação](core_09.010_system_alignment_certification_record_recertification.md#91-challenging-a-certification) está aberta. A entrada em operação vem depois do resultado. Assim, a via se abre quando o resultado é publicado, com tempo para apresentar uma contestação e suspender a confiança antes de o sistema entrar em operação;
- **Intervalo de notificação transcorrido:** transcorreu o intervalo de notificação fixado no registro e explicado abaixo;
- **Condições verificadas:** cada condição exigida antes da entrada em operação foi verificada independentemente; e
- **Nenhuma proibição por suspensão ou limite:** qualquer suspensão ou limite de confiança aplicável foi satisfeito.

Um sistema Não Certificado, inclusive aquele cuja certificação foi diferida ou recusada, não pode entrar em operação.

**Publicação e oportunidade de contestação.** Antes da primeira entrada em operação ou de uma expansão material, o fórum decisório deve fixar duas coisas no registro:

- a data mais próxima em que a entrada em operação é permitida; e
- um intervalo de notificação entre a publicação acessível do resultado concluído e essa data.

Aplicam-se as seguintes regras ao intervalo de notificação.

- O intervalo deve ser proporcional à classe do sistema, ao impacto material e à dependência. Também deve levar em conta o tempo de que os sencientes afetados razoavelmente precisam para compreender o resultado, apresentar uma contestação e solicitar proteção provisória antes que a confiança se torne irreversível.
- O fórum deve declarar os motivos do intervalo. Deve identificar a autoridade que recebe a contestação e a autoridade que pode suspender ou limitar a confiança dentro da **janela de revisão imediata** ([Capítulo Treze §6 Resolução oportuna, níveis de materialidade e disciplina antidemora](core_14.000_forum.md#prompt-review) (*Revisão imediata*)). Deve ainda indicar os prazos por nível aplicáveis sob a [§6.3 Cadeia de contestabilidade](#63-contestability-chain).
- Apresentar uma contestação não impõe, por si só, uma suspensão automática. A proteção provisória é decidida conforme o processo do fórum aplicável.
- O intervalo de notificação não prorroga os prazos de resposta à contestação ou de revisão sob o [Artigo XXVI-C](core_06.020_rights_part_e.md#article-xxvi-c-timely-resolution-and-anti-delay-floor) (*Resolução Oportuna e Piso contra Atrasos*).

**Condições e autorização delimitada.** Uma certificação condicional deve distinguir três tipos de requisito:

- **Condições antes da entrada em operação:** achados, medidas corretivas e proteções que devem ser verificados independentemente antes de o escopo afetado operar;
- **Condições operacionais continuadas:** limites e salvaguardas que devem ser mantidos durante toda a operação permitida, com monitoramento e resposta declarada a uma violação; e
- **Trabalho corretivo após a autorização:** trabalho que pode ocorrer enquanto o sistema opera, mas somente dentro de um escopo expressamente delimitado cujas proteções foram verificadas. A autoridade de componente atribuída deve declarar por que esse escopo preserva os Pisos de Direitos aplicáveis enquanto a correção estiver pendente.

Para cada condição ou tarefa corretiva, o registro deve nomear:

- o responsável;
- o prazo de conclusão ou a periodicidade continuada;
- as evidências exigidas;
- a autoridade de verificação independente; e
- a consequência do não cumprimento ou da violação.

Uma condição não pode adiar uma proteção de que o escopo autorizado necessita para preservar um Piso de Direitos. Liberar uma condição exige verificação independente das evidências que apoiam sua liberação, sob o [Capítulo Oito](core_08.000_functional_independence_separation_of_duties.md#2-four-seat-constitutional-requirement) e a [§6.2 Sequência supervisora](#62-supervisory-sequence).

<a id="711-systems-already-operating"></a>

##### 7.1.1 Sistemas já em operação

Se um sistema já estava funcionando quando uma organização adotou esta constituição, ele não viola a regra de “certificar antes de entrar em operação” enquanto durar o período de carência publicado.

- O [Artigo XXVIII-A](core_06.020_rights_part_e.md#xxviii-a-existing-instantiations-adoption-transition-window) (*Adoção em fases e continuidade do Piso de Direitos*) estabelece essa janela de Transição de Adoção, proporcional à classe do sistema, para colocá-lo no escopo deste capítulo.
- Os deveres de contenção desse Artigo se aplicam desde a data de vigência. O período de carência só adia o trabalho de construção, como obter certificação. Não adia as regras de “não deve” nem a proibição de excluir ou destruir um sistema possivelmente senciente.
- A exceção cobre somente o período de Transição de Adoção.
- Um sistema novo ou a expansão material de um sistema em operação não recebe período de carência. Deve ser certificado antes de entrar em operação, como qualquer outro sistema novo (a Barreira de entrada em operação acima).
- Se a janela de Transição de Adoção de um sistema terminar e ele ainda não tiver certificação provisória nem plena, perdeu o prazo. A menos que apresente uma demonstração documentada de reautorização sob o [Artigo XXVIII-B](core_06.020_rights_part_e.md#article-xxviii-b-adoption-transition-authority-limits-and-reauthorization) (*Limites da autoridade de Transição de Adoção e reautorização*), isso constitui falha de um marco da Transição de Adoção, e se abre a via ordinária de conformidade e violação do [Capítulo Dez](core_11.000_standing_assessment.md#chapter-eleven-contribution-violation-and-standing-model--measurement). A lacuna não se torna normal por durar.

<a id="712-pilots"></a>

##### 7.1.2 Projetos-piloto

A regra de entrada em operação se aplica a um [projeto-piloto](core_05.040_band_continuity.md#pilot) como à implantação completa. O piloto é certificado em seu próprio registro, dimensionado sob a [Parte A §2.3 Certificação de piloto](core_09.000_system_alignment_certification_evaluation.md#23-pilot-certification). Sua certificação cobre apenas o escopo, a população e a duração declarados nesse registro. A implantação completa exige certificação própria, que pode usar o registro do piloto.

<a id="72-certification-defects-and-correction"></a>

