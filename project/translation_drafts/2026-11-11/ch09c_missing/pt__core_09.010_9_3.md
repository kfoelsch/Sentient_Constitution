<!-- AI-assisted translation draft; unreviewed. Current-source Chapter Nine Part C §9.3; source SHA-256 514660246137f474b92cc37a717a64e0dd4f4890aca64cc95a0176b92ce28ec1. Baseline commit 247e2180509e5e029c1106878cf225067339e010; baseline SHA-256 faadaac887372f28f9b38ad506da505372ce40936796288c73d5f33f9c5317d9. Draft only; do not synchronize into translations/. -->

<a id="93-provisional-and-full-certification"></a>
#### 9.3 Certificação provisória e plena

*Em termos simples: um sistema conquista confiança por etapas. Sistemas novos e sistemas que falharam uma avaliação começam sob controle mais rigoroso e são verificados com frequência. Só um sistema sem problema atual nem sinal de problema iminente passa à certificação plena e a um intervalo maior. Uma avaliação malsucedida o devolve ao controle mais rigoroso.*

<a id="931-the-two-statuses"></a>
##### 9.3.1 Os dois status

A certificação tem um de dois status. Cada um possui intervalo próprio, indicado no Registro de Certificação do Sistema segundo [§8.1 Minimum record contents](#81-minimum-record-contents):

- **[Provisional certification](core_05.040_band_continuity.md#provisional-certification)** é o status da primeira certificação do sistema (inclusive sistema recém-implantado) e de sistema certificado após recertificação malsucedida, revisão reaberta ou nova revisão que encontrou desalinhamento. O intervalo provisório é menor que o intervalo pleno para a mesma classe; os limites de confiança constam do registro.
- **[Full certification](core_05.040_band_continuity.md#full-certification)** só é obtida na recertificação de sistema com certificação provisória e quando todos estes requisitos são satisfeitos:
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

- Recertificação que encontra desalinhamento atual **falhou**. Aplicam-se as consequências de [Part B §7 Certification Outcomes](core_09.005_system_alignment_certification_record_process.md#7-certification-outcomes). A próxima certificação possível é provisória, por mais limpa que seja a verificação seguinte; a contagem limpa recomeça em zero.
- Se não há desalinhamento atual, mas há indicador de desalinhamento iminente, a recertificação não falhou, mas não é limpa. Status provisório permanece e a contagem não avança; status pleno cai para provisório.
- Revisão reaberta sob [§9 Recertification and Reopening](#9-recertification-and-reopening) que encontra desalinhamento tem o efeito de recertificação falha.
- Nova revisão de sistema certificado que encontra desalinhamento atual tem o mesmo efeito. Se não houver status de certificação, aplicam-se as regras de [Part B §7.4 Denial and Revocation](core_09.005_system_alignment_certification_record_process.md#74-denial-and-revocation).

<a id="933-cause-of-misalignment"></a>
##### 9.3.3 Causa do desalinhamento

Quando avaliação, recertificação, revisão reaberta ou nova revisão encontra desalinhamento, o registro declara uma causa: **de projeto** (sistema/processo produz resultado desalinhado mesmo quando usado como previsto); **operacional** (projeto parece correto, mas a maneira de operar, alimentar ou manter gera desalinhamento); ou **ainda não determinada** (remédios para projeto e operação permanecem abertos até o fórum apurar a causa).

A conclusão causal não altera estas regras: resultados desalinhados repetidos significam desalinhamento, ainda que o projeto pareça correto no papel; projeto que produziria resultados desalinhados já é desalinhamento antes de aparecer o resultado; a causa define correção e escopo da revisão reaberta, mas nunca decide se há desalinhamento.

Se a causa for de projeto:
- a contagem de recertificações limpas permanece zero até redesign implantado e verificado;
- o fórum que encontrou a causa, ou o seguinte designado conforme [Part B §6.2 Supervisory sequence](core_09.005_system_alignment_certification_record_process.md#62-supervisory-sequence), verifica o redesign dentro da [matching intake target](core_05.040_band_continuity.md#tier-window), inclusive na primeira recertificação provisória;
- avaliação de componente anterior à verificação do redesign não conta para o total limpo; e
- mudar o modo de operar o sistema não satisfaz essa etapa.

Essas regras complementam os itens de redução de status acima. Operador ou senciente afetado pode pedir revisão da conclusão causal; se ela mudar, estas regras deixam de se aplicar.

<a id="934-tier-windows"></a>
##### 9.3.4 Prazos por nível

Quando avaliação inicial, recertificação, revisão reaberta ou nova revisão encontra desalinhamento: classifique o caso pelos níveis de materialidade de [Chapter Fifteen §6 Timely resolution, materiality tiers, and anti-delay discipline](core_15.000_forum.md#6-timely-resolution-materiality-tiers-and-anti-delay-discipline); presuma o nível correspondente à classe (por exemplo, sistema A desalinhado presume Nível A); intake, preservação de provas, proteção provisória e decisão seguem os prazos/limites externos desse nível; e atrasos são revistos conforme essa seção.

<a id="935-class-a-reliance"></a>
##### 9.3.5 Confiança em Classe A

Em comparação com a certificação plena, a provisória tem intervalo menor e, portanto, recertificação mais cedo ([§9.3.1 Os dois status](#931-the-two-statuses)); seus limites de confiança constam do registro ([§8.1 Minimum record contents](#81-minimum-record-contents)). A interrupção é tratada assim:
- a certificação provisória, por si só, não exige interromper sistema cuja interrupção cortaria essenciais à sobrevivência antes de haver substitutos;
- proteção provisória e condições da Parte B §7 tratam do caso;
- o mesmo vale enquanto a contagem estiver suspensa após desalinhamento de projeto: a suspensão da contagem não interrompe por si só sistema de que sencientes dependem; e
- enquanto durar a suspensão, o fórum declara proteção provisória, condições de confiança e aviso aos dependentes.

<a id="936-verification-not-assertion"></a>
##### 9.3.6 Verificação, não afirmação

Status, contagem de recertificações limpas e indicadores de monitoramento devem ser verificados, com revisão independente aberta; a mera declaração do sistema não basta:
- indicadores não podem ser definidos de modo que desalinhamento nunca apareça;
- redesign também se verifica por evidências que outros possam conferir;
- certificação plena não elimina motivo para reabrir revisão: todos os gatilhos de [§9 Recertification and Reopening](#9-recertification-and-reopening) continuam; e
- evasão segue [§9.4 Non-evasion](#94-non-evasion).
