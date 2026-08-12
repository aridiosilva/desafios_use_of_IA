# Controle Financeiro Pessoal
## Desenvolvimento criativo de algoritmo — linguagem natural, pseudocódigo modular e demonstrativo

---

## Sumário

1. [Enunciado e requisitos funcionais](#1-enunciado-e-requisitos-funcionais)
2. [Algoritmo em linguagem natural](#2-algoritmo-em-linguagem-natural)
3. [Arquitetura modular](#3-arquitetura-modular)
4. [Pseudocódigo modularizado](#4-pseudocódigo-modularizado)
5. [Exemplo de execução — demonstrativo em Markdown](#5-exemplo-de-execução--demonstrativo-em-markdown)
6. [Justificativas de projeto](#6-justificativas-de-projeto)

---

## 1. Enunciado e requisitos funcionais

Desenvolver um sistema simples de **controle financeiro pessoal** que permita ao usuário informar diversas despesas do mês (mercado, transporte, lazer etc.) e, ao final, apresentar um demonstrativo consolidado.

### Requisitos funcionais

| # | Requisito |
|:-:|:----------|
| RF01 | Somar automaticamente todos os valores informados, **por tipo**, sem que o usuário precise informar quantas despesas fez |
| RF02 | Contar as despesas realizadas **por tipo** |
| RF03 | O processo continua em laço até que o **valor digitado seja zero** ou o usuário digite **FIM** |
| RF04 | Exibir o título **CONTROLE FINANCEIRO** no topo do demonstrativo |
| RF05 | Listar os tipos de despesa **ordenados crescentemente por nome** |
| RF06 | Para cada tipo: nome, total gasto, menor valor, maior valor, valor médio, % sobre o total geral e contagem de lançamentos |
| RF07 | Linha final de resumo geral: total geral, tipo de maior gasto (nome **+ valor total**), tipo de menor gasto (nome **+ valor total**), contagem total geral e valor médio geral |
| RF08 | Indicar também o tipo de **maior valor médio** com o valor correspondente |

---

## 2. Algoritmo em linguagem natural

**Objetivo:** registrar despesas do mês sem saber antecipadamente quantas serão, acumulando estatísticas por tipo, e ao final exibir um demonstrativo ordenado por nome do tipo, mais uma linha de resumo geral.

### Fase 1 — Preparação

1. Criar cinco listas paralelas, todas alinhadas pelo mesmo índice, que representam cada **tipo distinto** de despesa encontrado:
   - `nomeTipo` — o nome do tipo (ex.: MERCADO, TRANSPORTE, LAZER);
   - `totalTipo` — soma acumulada dos valores daquele tipo;
   - `qtdTipo` — quantas despesas já foram lançadas naquele tipo;
   - `menorTipo` — menor valor individual já lançado naquele tipo;
   - `maiorTipo` — maior valor individual já lançado naquele tipo.
2. Zerar o contador de tipos distintos (`qtdTipos`), o total geral gasto (`totalGeral`) e a contagem geral de lançamentos (`qtdGeral`).

### Fase 2 — Entrada de dados (laço de repetição, sem quantidade prévia)

3. Repetir indefinidamente:
   1. Pedir ao usuário o **tipo da despesa** (ou a palavra `FIM` para encerrar).
   2. Converter o texto digitado para letras maiúsculas e remover espaços em excesso, para que "mercado", "Mercado" e "MERCADO" sejam tratados como o **mesmo** tipo.
   3. Se o texto for `FIM`, **encerrar o laço**.
   4. Pedir o **valor** da despesa.
   5. Se o valor for **zero**, **encerrar o laço** (o lançamento em andamento é descartado).
   6. Se o valor for **negativo**, avisar que é inválido e voltar ao início do laço, sem gravar nada.
   7. Procurar `nomeTipo` nas listas para descobrir se aquele tipo **já existe**:
      - **Se não existe:** abrir uma nova posição — incrementar `qtdTipos`, gravar o nome, iniciar o total com o valor informado, iniciar a contagem em 1, e iniciar tanto o menor quanto o maior com o próprio valor informado (é o único valor conhecido até agora).
      - **Se já existe:** somar o valor ao `totalTipo` daquela posição, somar 1 ao `qtdTipo`; se o valor for menor que `menorTipo`, substituir o menor; se for maior que `maiorTipo`, substituir o maior.
   8. Somar o valor ao `totalGeral` e somar 1 ao `qtdGeral`.
   9. Voltar ao passo 3.1.

### Fase 3 — Ordenação

4. Se nenhum lançamento foi feito (`qtdTipos == 0`), exibir a mensagem "Nenhuma despesa registrada." e terminar o programa.
5. Ordenar as listas em **ordem crescente pelo nome do tipo** (método da bolha ou equivalente). Sempre que dois nomes forem trocados de posição, trocar **também** os valores correspondentes de `totalTipo`, `qtdTipo`, `menorTipo` e `maiorTipo`, para não quebrar o alinhamento entre as listas.

### Fase 4 — Apuração dos extremos globais

6. Percorrer as listas guardando:
   - a posição do tipo com **maior total acumulado** (`posMaiorTotal`);
   - a posição do tipo com **menor total acumulado** (`posMenorTotal`);
   - a posição do tipo com **maior valor médio** (`posMaiorMedia`), onde a média de um tipo é `totalTipo ÷ qtdTipo`.
7. Calcular a **média geral** como `totalGeral ÷ qtdGeral`.

### Fase 5 — Saída

8. Exibir o título **CONTROLE FINANCEIRO** e o cabeçalho das colunas.
9. Para cada tipo, do primeiro ao último (já em ordem alfabética), exibir em uma linha: nome do tipo, total gasto, quantidade de lançamentos, menor valor, maior valor, valor médio (`total ÷ quantidade`) e o percentual sobre o total geral (`total ÷ totalGeral × 100`).
10. Exibir a linha de **RESUMO GERAL** contendo:
    - total geral gasto;
    - contagem total de despesas realizadas;
    - valor médio geral;
    - **maior gasto:** nome do tipo de maior total acumulado **seguido do seu valor total**;
    - **menor gasto:** nome do tipo de menor total acumulado **seguido do seu valor total**;
    - **maior média:** nome do tipo de maior valor médio seguido da média correspondente.
11. Encerrar.

---

## 3. Arquitetura modular

### Hierarquia de chamadas

```
PROGRAMA PRINCIPAL
│
├── Inicializar()
│
├── LerLancamentos()
│   └── RegistrarDespesa(tipo; valor)
│       ├── Normalizar(tipo)
│       ├── BuscarTipo(tipo)         -> posicao ou 0
│       ├── CriarTipo(tipo; valor)   [se posicao = 0]
│       └── AtualizarTipo(pos; valor)[se posicao > 0]
│
├── OrdenarPorNome()
│   └── Trocar(i; j)
│
└── EmitirDemonstrativo()
    ├── EscreverCabecalho()
    ├── EscreverLinhaTipo(i)          [para cada tipo]
    │   ├── MediaDoTipo(i)
    │   └── PercentualDoTipo(i)
    └── EscreverResumoGeral()
        ├── MediaGeral()
        ├── PosMaiorTotal()
        ├── PosMenorTotal()
        └── PosMaiorMedia()
              └── MediaDoTipo(i)
```

### Catálogo de módulos

| Módulo | Tipo | Parâmetros | Retorno | Responsabilidade |
|:-------|:-----|:-----------|:--------|:-----------------|
| `Inicializar` | Procedimento | — | — | Zera acumuladores globais |
| `Normalizar` | Função | `t: caractere` | `caractere` | Padroniza o nome do tipo (maiúsculas, sem espaços nas pontas) |
| `ValorValido` | Função | `v: real` | `logico` | Rejeita valores negativos |
| `BuscarTipo` | Função | `t: caractere` | `inteiro` | Índice do tipo, ou `0` se ainda não existe |
| `CriarTipo` | Procedimento | `t: caractere`, `v: real` | — | Abre nova posição nas listas paralelas |
| `AtualizarTipo` | Procedimento | `p: inteiro`, `v: real` | — | Acumula total/qtde e ajusta menor/maior |
| `RegistrarDespesa` | Procedimento | `t: caractere`, `v: real` | — | Decide entre criar e atualizar; soma nos totais gerais |
| `LerLancamentos` | Procedimento | — | — | Laço de entrada com sentinela dupla (`FIM` ou `0`) |
| `Trocar` | Procedimento | `a, b: inteiro` | — | Permuta as 5 listas paralelas simultaneamente |
| `OrdenarPorNome` | Procedimento | — | — | Ordenação crescente por nome (bolha) |
| `MediaDoTipo` | Função | `p: inteiro` | `real` | `total ÷ quantidade` do tipo |
| `PercentualDoTipo` | Função | `p: inteiro` | `real` | `total do tipo ÷ total geral × 100` |
| `MediaGeral` | Função | — | `real` | `total geral ÷ qtde geral` |
| `PosMaiorTotal` | Função | — | `inteiro` | Índice do tipo de maior total acumulado |
| `PosMenorTotal` | Função | — | `inteiro` | Índice do tipo de menor total acumulado |
| `PosMaiorMedia` | Função | — | `inteiro` | Índice do tipo de maior valor médio |
| `EscreverCabecalho` | Procedimento | — | — | Título e cabeçalho da tabela |
| `EscreverLinhaTipo` | Procedimento | `p: inteiro` | — | Formata uma linha do demonstrativo |
| `EscreverResumoGeral` | Procedimento | — | — | Linha final consolidada |
| `EmitirDemonstrativo` | Procedimento | — | — | Orquestra toda a saída |

---

## 4. Pseudocódigo modularizado

### Convenção de notação adotada

| Elemento | Símbolo | Exemplo |
|:---------|:--------|:--------|
| Atribuição | **`=`** | `taxaBase = 5,00` |
| Igualdade | **`==`** | `SE (resposta == "S") ENTÃO` |
| Diferença | **`!=`** | `SE (resposta != "S") ENTÃO` |
| Demais comparações | `<` `<=` `>` `>=` | `SE (media < 5) ENTÃO` |
| Estrutura condicional | **`SE ... ENTÃO ... SENÃO ... FIMSE`** | palavras-chave em maiúsculas |
| Separador decimal | **`,`** (vírgula) | `PRECO = 12,00` |
| Separador de argumentos na chamada | **`;`** (ponto e vírgula) | `Subtotal(qtd; preco)` |
| Separador de parâmetros na declaração | **`;`** (ponto e vírgula) | `FUNÇÃO f(a : real ; b : caractere)` |

> **`=` e `==` fazem coisas opostas.** `taxaBase = 5,00` **grava** um valor; `resposta == "S"` **pergunta** se são iguais. Escrever `SE (resposta = "S") ENTÃO` significaria atribuir dentro do teste — a condição perderia a função.
>
> **Por que ponto e vírgula nos argumentos:** a vírgula já é o separador decimal. Se também separasse argumentos, `f(1,5, 2,0)` ficaria ambíguo — dois argumentos ou quatro? Com `f(1,5; 2,0)` a leitura é única.
>
> **Sobre os acentos:** as palavras-chave usam `ENTÃO`, `SENÃO`, `ATÉ`, `INÍCIO`, `FUNÇÃO`, `FAÇA`. Se o interpretador utilizado recusar caracteres acentuados, basta removê-los (`ENTAO`, `SENAO`, `ATE`, `INICIO`, `FUNCAO`, `FACA`) — a lógica não muda.


```
ALGORITMO "CONTROLE_FINANCEIRO_PESSOAL_MODULAR"

// ============================================================
// AREA DE DADOS GLOBAIS (compartilhada pelos modulos)
// ============================================================
VAR
   // listas paralelas: uma posicao por TIPO distinto de despesa
   nomeTipo  : vetor[1..100] de caractere
   totalTipo : vetor[1..100] de real
   qtdTipo   : vetor[1..100] de inteiro
   menorTipo : vetor[1..100] de real
   maiorTipo : vetor[1..100] de real

   // acumuladores globais
   qtdTipos   : inteiro     // quantidade de tipos distintos
   totalGeral : real        // soma de todas as despesas
   qtdGeral   : inteiro     // quantidade total de lancamentos

   // variaveis do programa principal
   i : inteiro


// ============================================================
// MODULO 1 - INICIALIZACAO
// ============================================================
PROCEDIMENTO Inicializar()
INÍCIO
   qtdTipos   = 0
   totalGeral = 0
   qtdGeral   = 0
FIMPROCEDIMENTO


// ============================================================
// MODULO 2 - NORMALIZACAO DO NOME DO TIPO
// Garante que "mercado", "Mercado" e " MERCADO " sejam
// tratados como um unico tipo.
// ============================================================
FUNÇÃO Normalizar(t : caractere) : caractere
VAR
   texto : caractere
INÍCIO
   texto = MAIUSC(t)
   ENQUANTO (Compr(texto) > 0) E (Copia(texto; 1; 1) == " ") FAÇA
      texto = Copia(texto; 2; Compr(texto) - 1)          // remove espacos a esquerda
   FIMENQUANTO
   ENQUANTO (Compr(texto) > 0) E (Copia(texto; Compr(texto); 1) == " ") FAÇA
      texto = Copia(texto; 1; Compr(texto) - 1)          // remove espacos a direita
   FIMENQUANTO
   RETORNE texto
FIMFUNÇÃO


// ============================================================
// MODULO 3 - VALIDACAO DO VALOR
// ============================================================
FUNÇÃO ValorValido(v : real) : logico
INÍCIO
   RETORNE (v > 0)
FIMFUNÇÃO


// ============================================================
// MODULO 4 - BUSCA DE TIPO JA CADASTRADO
// Retorna o indice do tipo, ou 0 se ainda nao existir.
// ============================================================
FUNÇÃO BuscarTipo(t : caractere) : inteiro
VAR
   k : inteiro
INÍCIO
   PARA k DE 1 ATÉ qtdTipos FAÇA
      SE (nomeTipo[k] == t) ENTÃO
         RETORNE k
      FIMSE
   FIMPARA
   RETORNE 0
FIMFUNÇÃO


// ============================================================
// MODULO 5 - CRIACAO DE UM NOVO TIPO
// menor e maior nascem com o proprio valor: e o unico
// valor conhecido do tipo neste momento.
// ============================================================
PROCEDIMENTO CriarTipo(t : caractere ; v : real)
INÍCIO
   qtdTipos = qtdTipos + 1
   nomeTipo[qtdTipos]  = t
   totalTipo[qtdTipos] = v
   qtdTipo[qtdTipos]   = 1
   menorTipo[qtdTipos] = v
   maiorTipo[qtdTipos] = v
FIMPROCEDIMENTO


// ============================================================
// MODULO 6 - ACUMULO EM TIPO EXISTENTE
// ============================================================
PROCEDIMENTO AtualizarTipo(p : inteiro ; v : real)
INÍCIO
   totalTipo[p] = totalTipo[p] + v
   qtdTipo[p]   = qtdTipo[p] + 1

   SE (v < menorTipo[p]) ENTÃO
      menorTipo[p] = v
   FIMSE
   SE (v > maiorTipo[p]) ENTÃO
      maiorTipo[p] = v
   FIMSE
FIMPROCEDIMENTO


// ============================================================
// MODULO 7 - REGISTRO DE UMA DESPESA (regra de negocio)
// ============================================================
PROCEDIMENTO RegistrarDespesa(t : caractere ; v : real)
VAR
   pos : inteiro
INÍCIO
   pos = BuscarTipo(t)

   SE (pos == 0) ENTÃO
      CriarTipo(t; v)
   SENÃO
      AtualizarTipo(pos; v)
   FIMSE

   totalGeral = totalGeral + v
   qtdGeral   = qtdGeral + 1
FIMPROCEDIMENTO


// ============================================================
// MODULO 8 - ENTRADA DE DADOS EM LACO
// Sentinela dupla: tipo = "FIM" ou valor = 0.
// A quantidade de despesas nunca e perguntada ao usuario.
// ============================================================
PROCEDIMENTO LerLancamentos()
VAR
   tipo     : caractere
   valor    : real
   encerrar : logico
INÍCIO
   encerrar = FALSO

   ESCREVAL("=== LANCAMENTO DE DESPESAS ===")
   ESCREVAL("Digite FIM no tipo, ou 0 no valor, para encerrar.")
   ESCREVAL("")

   ENQUANTO (encerrar == FALSO) FAÇA
      ESCREVA("Tipo da despesa (ou FIM): ")
      LEIA(tipo)
      tipo = Normalizar(tipo)

      SE (tipo == "FIM") ENTÃO
         encerrar = VERDADEIRO
      SENÃO
         ESCREVA("Valor de "; tipo; ": R$ ")
         LEIA(valor)

         SE (valor == 0) ENTÃO
            encerrar = VERDADEIRO
         SENÃO
            SE (ValorValido(valor)) ENTÃO
               RegistrarDespesa(tipo; valor)
            SENÃO
               ESCREVAL(">> Valor invalido. Informe um valor positivo.")
            FIMSE
         FIMSE
      FIMSE
   FIMENQUANTO
FIMPROCEDIMENTO


// ============================================================
// MODULO 9 - TROCA DE DUAS POSICOES
// As 5 listas sao paralelas: a troca precisa mover todas,
// senao os totais passam a pertencer ao tipo errado.
// ============================================================
PROCEDIMENTO Trocar(a : inteiro ; b : inteiro)
VAR
   auxNome : caractere
   auxReal : real
   auxInt  : inteiro
INÍCIO
   auxNome     = nomeTipo[a]
   nomeTipo[a] = nomeTipo[b]
   nomeTipo[b] = auxNome

   auxReal      = totalTipo[a]
   totalTipo[a] = totalTipo[b]
   totalTipo[b] = auxReal

   auxInt     = qtdTipo[a]
   qtdTipo[a] = qtdTipo[b]
   qtdTipo[b] = auxInt

   auxReal      = menorTipo[a]
   menorTipo[a] = menorTipo[b]
   menorTipo[b] = auxReal

   auxReal      = maiorTipo[a]
   maiorTipo[a] = maiorTipo[b]
   maiorTipo[b] = auxReal
FIMPROCEDIMENTO


// ============================================================
// MODULO 10 - ORDENACAO CRESCENTE POR NOME DO TIPO
// ============================================================
PROCEDIMENTO OrdenarPorNome()
VAR
   a, b : inteiro
INÍCIO
   PARA a DE 1 ATÉ (qtdTipos - 1) FAÇA
      PARA b DE 1 ATÉ (qtdTipos - a) FAÇA
         SE (nomeTipo[b] > nomeTipo[b+1]) ENTÃO
            Trocar(b; b+1)
         FIMSE
      FIMPARA
   FIMPARA
FIMPROCEDIMENTO


// ============================================================
// MODULO 11 - CALCULOS ESTATISTICOS
// ============================================================
FUNÇÃO MediaDoTipo(p : inteiro) : real
INÍCIO
   RETORNE (totalTipo[p] / qtdTipo[p])
FIMFUNÇÃO

FUNÇÃO PercentualDoTipo(p : inteiro) : real
INÍCIO
   RETORNE ((totalTipo[p] / totalGeral) * 100)
FIMFUNÇÃO

FUNÇÃO MediaGeral() : real
INÍCIO
   RETORNE (totalGeral / qtdGeral)
FIMFUNÇÃO


// ============================================================
// MODULO 12 - APURACAO DOS EXTREMOS GLOBAIS
// ============================================================
FUNÇÃO PosMaiorTotal() : inteiro
VAR
   k, pos : inteiro
INÍCIO
   pos = 1
   PARA k DE 2 ATÉ qtdTipos FAÇA
      SE (totalTipo[k] > totalTipo[pos]) ENTÃO
         pos = k
      FIMSE
   FIMPARA
   RETORNE pos
FIMFUNÇÃO

FUNÇÃO PosMenorTotal() : inteiro
VAR
   k, pos : inteiro
INÍCIO
   pos = 1
   PARA k DE 2 ATÉ qtdTipos FAÇA
      SE (totalTipo[k] < totalTipo[pos]) ENTÃO
         pos = k
      FIMSE
   FIMPARA
   RETORNE pos
FIMFUNÇÃO

FUNÇÃO PosMaiorMedia() : inteiro
VAR
   k, pos : inteiro
INÍCIO
   pos = 1
   PARA k DE 2 ATÉ qtdTipos FAÇA
      SE (MediaDoTipo(k) > MediaDoTipo(pos)) ENTÃO
         pos = k
      FIMSE
   FIMPARA
   RETORNE pos
FIMFUNÇÃO


// ============================================================
// MODULO 13 - SAIDA: CABECALHO (formato Markdown)
// ============================================================
PROCEDIMENTO EscreverCabecalho()
INÍCIO
   ESCREVAL("")
   ESCREVAL("# CONTROLE FINANCEIRO")
   ESCREVAL("")
   ESCREVAL("### Demonstrativo por tipo de despesa")
   ESCREVAL("*(ordenado crescentemente por nome do tipo)*")
   ESCREVAL("")
   ESCREVAL("| Tipo da Despesa | Qtde | Total Gasto | Menor Valor | Maior Valor | Valor Medio | % do Total |")
   ESCREVAL("|:----------------|-----:|------------:|------------:|------------:|------------:|-----------:|")
FIMPROCEDIMENTO


// ============================================================
// MODULO 14 - SAIDA: UMA LINHA DO DEMONSTRATIVO
// ============================================================
PROCEDIMENTO EscreverLinhaTipo(p : inteiro)
INÍCIO
   ESCREVAL("| ";     nomeTipo[p];
            " | ";    qtdTipo[p];
            " | R$ "; totalTipo[p]:0:2;
            " | R$ "; menorTipo[p]:0:2;
            " | R$ "; maiorTipo[p]:0:2;
            " | R$ "; MediaDoTipo(p):0:2;
            " | ";    PercentualDoTipo(p):0:2; "% |")
FIMPROCEDIMENTO


// ============================================================
// MODULO 15 - SAIDA: RESUMO GERAL
// ============================================================
PROCEDIMENTO EscreverResumoGeral()
VAR
   pMaior, pMenor, pMedia : inteiro
INÍCIO
   pMaior = PosMaiorTotal()
   pMenor = PosMenorTotal()
   pMedia = PosMaiorMedia()

   ESCREVAL("")
   ESCREVAL("### Resumo geral")
   ESCREVAL("")
   ESCREVAL("| Indicador | Tipo correspondente | Valor |")
   ESCREVAL("|:----------|:--------------------|------:|")
   ESCREVAL("| **Total geral gasto** | - | **R$ "; totalGeral:0:2; "** |")
   ESCREVAL("| **Qtde total de despesas** | - | **"; qtdGeral; "** |")
   ESCREVAL("| **Valor medio geral** | - | **R$ "; MediaGeral():0:2; "** |")
   ESCREVAL("| **Despesa de maior gasto** | **"; nomeTipo[pMaior];
            "** | **R$ "; totalTipo[pMaior]:0:2; "** |")
   ESCREVAL("| **Despesa de menor gasto** | **"; nomeTipo[pMenor];
            "** | **R$ "; totalTipo[pMenor]:0:2; "** |")
   ESCREVAL("| **Despesa de maior valor medio** | **"; nomeTipo[pMedia];
            "** | **R$ "; MediaDoTipo(pMedia):0:2; "** |")
FIMPROCEDIMENTO


// ============================================================
// MODULO 16 - ORQUESTRADOR DA SAIDA
// ============================================================
PROCEDIMENTO EmitirDemonstrativo()
VAR
   k : inteiro
INÍCIO
   EscreverCabecalho()

   PARA k DE 1 ATÉ qtdTipos FAÇA
      EscreverLinhaTipo(k)
   FIMPARA

   EscreverResumoGeral()
FIMPROCEDIMENTO


// ============================================================
// PROGRAMA PRINCIPAL
// Apenas coordena os modulos - nenhuma regra de negocio aqui.
// ============================================================
INÍCIO
   Inicializar()
   LerLancamentos()

   SE (qtdTipos == 0) ENTÃO
      ESCREVAL("")
      ESCREVAL("Nenhuma despesa registrada.")
   SENÃO
      OrdenarPorNome()
      EmitirDemonstrativo()
   FIMSE

FIMALGORITMO
```

---

## 5. Exemplo de execução — demonstrativo em Markdown

### 5.1 Entrada digitada pelo usuário

| # | Tipo informado | Valor informado |
|:-:|:---------------|----------------:|
| 1 | MERCADO        | R$ 250,00 |
| 2 | TRANSPORTE     | R$ 40,00 |
| 3 | LAZER          | R$ 120,00 |
| 4 | MERCADO        | R$ 180,50 |
| 5 | TRANSPORTE     | R$ 15,00 |
| 6 | MERCADO        | R$ 90,00 |
| 7 | LAZER          | R$ 60,00 |
| 8 | TRANSPORTE     | R$ 25,00 |
| — | **FIM**        | *(encerra o laço)* |

### 5.2 Saída gerada

# CONTROLE FINANCEIRO

### Demonstrativo por tipo de despesa
*(ordenado crescentemente por nome do tipo)*

| Tipo da Despesa | Qtde | Total Gasto | Menor Valor | Maior Valor | Valor Médio | % do Total |
|:----------------|-----:|------------:|------------:|------------:|------------:|-----------:|
| LAZER           |    2 |  R$ 180,00 |   R$ 60,00 |  R$ 120,00 |   R$ 90,00 |  23,06% |
| MERCADO         |    3 |  R$ 520,50 |   R$ 90,00 |  R$ 250,00 |  R$ 173,50 |  66,69% |
| TRANSPORTE      |    3 |   R$ 80,00 |   R$ 15,00 |   R$ 40,00 |   R$ 26,67 |  10,25% |

### Resumo geral

| Indicador | Tipo correspondente | Valor |
|:----------|:--------------------|------:|
| **Total geral gasto**            | — | **R$ 780,50** |
| **Qtde total de despesas**       | — | **8** |
| **Valor médio geral**            | — | **R$ 97,56** |
| **Despesa de maior gasto**       | **MERCADO** | **R$ 520,50** |
| **Despesa de menor gasto**       | **TRANSPORTE** | **R$ 80,00** |
| **Despesa de maior valor médio** | **MERCADO** | **R$ 173,50** |

### 5.3 Conferência dos cálculos

| Verificação | Cálculo | Resultado |
|:------------|:--------|----------:|
| Total geral | 180,00 + 520,50 + 80,00 | R$ 780,50 |
| Qtde geral | 2 + 3 + 3 | 8 |
| Média geral | 780,50 ÷ 8 | R$ 97,56 |
| % LAZER | 180,00 ÷ 780,50 × 100 | 23,06% |
| % MERCADO | 520,50 ÷ 780,50 × 100 | 66,69% |
| % TRANSPORTE | 80,00 ÷ 780,50 × 100 | 10,25% |
| **Soma dos percentuais** | 23,06 + 66,69 + 10,25 | **100,00%** |

### 5.4 Código-fonte Markdown do demonstrativo

````markdown
# CONTROLE FINANCEIRO

### Demonstrativo por tipo de despesa
*(ordenado crescentemente por nome do tipo)*

| Tipo da Despesa | Qtde | Total Gasto | Menor Valor | Maior Valor | Valor Médio | % do Total |
|:----------------|-----:|------------:|------------:|------------:|------------:|-----------:|
| LAZER           |    2 |  R$ 180,00 |   R$ 60,00 |  R$ 120,00 |   R$ 90,00 |  23,06% |
| MERCADO         |    3 |  R$ 520,50 |   R$ 90,00 |  R$ 250,00 |  R$ 173,50 |  66,69% |
| TRANSPORTE      |    3 |   R$ 80,00 |   R$ 15,00 |   R$ 40,00 |   R$ 26,67 |  10,25% |

### Resumo geral

| Indicador | Tipo correspondente | Valor |
|:----------|:--------------------|------:|
| **Total geral gasto**            | — | **R$ 780,50** |
| **Qtde total de despesas**       | — | **8** |
| **Valor médio geral**            | — | **R$ 97,56** |
| **Despesa de maior gasto**       | **MERCADO** | **R$ 520,50** |
| **Despesa de menor gasto**       | **TRANSPORTE** | **R$ 80,00** |
| **Despesa de maior valor médio** | **MERCADO** | **R$ 173,50** |
````

**Observações sobre a saída em Markdown:**

- A linha de alinhamento (`|:---|---:|`) deve vir **imediatamente após o cabeçalho** — é ela que define o alinhamento (`:---` à esquerda para textos, `---:` à direita para números e valores monetários).
- A quantidade de colunas do cabeçalho, da linha de alinhamento e de cada linha de dados precisa ser **idêntica**, senão a tabela não renderiza.
- O laço `PARA` em `EmitirDemonstrativo` gera uma linha por tipo distinto, então a tabela cresce automaticamente conforme os tipos que o usuário cadastrar — nada é fixado no código.

---

## 6. Justificativas de projeto

### 6.1 Pontos de lógica do algoritmo

- **Não se pergunta a quantidade de despesas.** O laço `ENQUANTO` em `LerLancamentos` é controlado por sentinela dupla (`FIM` no tipo **ou** `0` no valor), e os contadores `qtdGeral` e `qtdTipo[]` são incrementados a cada lançamento válido.
- **Descoberta dinâmica de tipos.** A busca linear de `BuscarTipo` decide entre criar uma nova posição ou acumular numa existente — por isso o usuário nunca precisa declarar antecipadamente quais tipos vai usar.
- **Menor e maior inicializados com o próprio valor** no primeiro lançamento do tipo (`CriarTipo`). Inicializar `menorTipo` com 0 seria um erro clássico: nenhum valor positivo posterior ficaria abaixo de 0 e o menor jamais seria atualizado.
- **Troca em bloco na ordenação.** As cinco listas são paralelas, então toda troca precisa mover as cinco simultaneamente — daí o módulo `Trocar` existir isoladamente.
- **Normalização com `Normalizar`** evita que "Mercado" e "MERCADO" virem dois tipos distintos.
- **Proteção contra divisão por zero.** `MediaGeral` e `PercentualDoTipo` só são alcançadas por dentro do ramo `SENÃO` do teste `qtdTipos == 0` no programa principal, ou seja, quando existe ao menos um lançamento.

### 6.2 O que a modularização resolve

| Antes (sequencial) | Depois (modular) |
|:-------------------|:-----------------|
| Um bloco único de ~120 linhas com entrada, regra de negócio, ordenação e saída misturadas | 16 módulos, cada um com **uma** responsabilidade |
| Trocar o formato de saída exigia mexer no meio do algoritmo | Basta reescrever `EscreverCabecalho`, `EscreverLinhaTipo` e `EscreverResumoGeral` — **nenhum** outro módulo é tocado |
| A troca de 5 vetores aparecia inline dentro da bolha, com risco de esquecer um vetor | Isolada em `Trocar`, chamada de um único ponto |
| Cálculo de média repetido em 3 lugares diferentes | Centralizado em `MediaDoTipo`, reutilizado por `EscreverLinhaTipo` e `PosMaiorMedia` |
| Testar a regra "tipo novo × tipo existente" exigia rodar o programa inteiro | `BuscarTipo`, `CriarTipo` e `AtualizarTipo` podem ser verificados isoladamente |
| Trocar vetores paralelos por registros/matriz quebrava tudo | O impacto fica contido em `CriarTipo`, `AtualizarTipo`, `BuscarTipo` e `Trocar` |

### 6.3 Decisões de projeto

- **Dados globais + módulos sem parâmetros de estado.** Em Portugol/VisuAlg não há registros compostos nem passagem prática de vetores por referência em todos os interpretadores; manter as cinco listas na área global e passar apenas *índices* e *valores* como parâmetros é a solução idiomática. Em uma linguagem com estruturas (C, Java, Python), o passo seguinte natural seria substituir as listas paralelas por um vetor de registros `Despesa{nome, total, qtde, menor, maior}` — e a interface dos módulos permaneceria a mesma.
- **Funções puras para estatística.** `MediaDoTipo`, `PercentualDoTipo` e `MediaGeral` apenas leem e retornam, sem alterar nada. Isso permite chamá-las de qualquer ponto sem efeito colateral — inclusive dentro de comparações, como em `PosMaiorMedia`.
- **`RegistrarDespesa` como fronteira da regra de negócio.** `LerLancamentos` cuida só do diálogo com o usuário e da sentinela; toda a decisão sobre *como* armazenar está abaixo dela. Se amanhã as despesas vierem de um arquivo em vez do teclado, só `LerLancamentos` muda.
- **Limite de 100 tipos distintos.** Valor arbitrário e folgado para uso pessoal. Em uma implementação real, o vetor seria substituído por uma lista dinâmica ou dicionário, eliminando o limite e reduzindo a busca de linear para constante.
