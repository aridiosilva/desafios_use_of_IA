# Simulador de Pedidos — Cafeteria
## Saídas de tela dos 12 casos de teste (CT01 a CT12)

Execuções simuladas do algoritmo descrito em `simulador-cafeteria.md`. Cada bloco reproduz a
sessão completa no terminal: prompts, entradas do atendente, mensagens de erro e o cupom final.

**Convenções de leitura**

- O texto após cada prompt (`? `, `: `, `R$ `) é o que o **atendente digitou**.
- `‹enter›` representa uma entrada **vazia** (o atendente apenas pressionou Enter).
- As mensagens do sistema saem sem acentuação, conforme os literais do pseudocódigo;
  os **nomes dos itens** preservam a acentuação porque são dados digitados pelo atendente.
- O separador `..........` do cupom é fixo (10 pontos), exatamente como o procedimento
  `ExibirCupom` o escreve.

---

## CT01 — Caminho feliz: não cadastrado, 1 item

```text
=======================================
   CAFETERIA - ATENDIMENTO NO BALCAO
=======================================
Quantos itens o cliente vai pedir? 1
Item 1 - nome: Café expresso
Item 1 (Café expresso) - preco: R$ 5,00
O cliente e cadastrado? (S/N): N
---------------------------------------
                CUPOM
---------------------------------------
1) Café expresso .......... R$ 5,00
---------------------------------------
Subtotal ................ R$ 5,00
Cliente nao cadastrado: sem desconto
---------------------------------------
TOTAL A PAGAR ........... R$ 5,00
=======================================
```

---

## CT02 — Caminho feliz: cadastrado, 3 itens

```text
=======================================
   CAFETERIA - ATENDIMENTO NO BALCAO
=======================================
Quantos itens o cliente vai pedir? 3
Item 1 - nome: Cappuccino
Item 1 (Cappuccino) - preco: R$ 9,50
Item 2 - nome: Pão de queijo
Item 2 (Pão de queijo) - preco: R$ 6,00
Item 3 - nome: Suco de laranja
Item 3 (Suco de laranja) - preco: R$ 8,00
O cliente e cadastrado? (S/N): S
---------------------------------------
                CUPOM
---------------------------------------
1) Cappuccino .......... R$ 9,50
2) Pão de queijo .......... R$ 6,00
3) Suco de laranja .......... R$ 8,00
---------------------------------------
Subtotal ................ R$ 23,50
Cliente cadastrado: desconto de 10%
Desconto ................ -R$ 2,35
---------------------------------------
TOTAL A PAGAR ........... R$ 21,15
=======================================
```

---

## CT03 — Quantidade zero rejeitada (RN02)

```text
=======================================
   CAFETERIA - ATENDIMENTO NO BALCAO
=======================================
Quantos itens o cliente vai pedir? 0
[ERRO] A quantidade deve estar entre 1 e 50.
Quantos itens o cliente vai pedir? 2
Item 1 - nome: Café
Item 1 (Café) - preco: R$ 5,00
Item 2 - nome: Bolo de cenoura
Item 2 (Bolo de cenoura) - preco: R$ 7,50
O cliente e cadastrado? (S/N): N
---------------------------------------
                CUPOM
---------------------------------------
1) Café .......... R$ 5,00
2) Bolo de cenoura .......... R$ 7,50
---------------------------------------
Subtotal ................ R$ 12,50
Cliente nao cadastrado: sem desconto
---------------------------------------
TOTAL A PAGAR ........... R$ 12,50
=======================================
```

---

## CT04 — Quantidade não inteira rejeitada (RN01)

```text
=======================================
   CAFETERIA - ATENDIMENTO NO BALCAO
=======================================
Quantos itens o cliente vai pedir? 2,5
[ERRO] Informe um numero inteiro.
Quantos itens o cliente vai pedir? 1
Item 1 - nome: Latte
Item 1 (Latte) - preco: R$ 11,00
O cliente e cadastrado? (S/N): S
---------------------------------------
                CUPOM
---------------------------------------
1) Latte .......... R$ 11,00
---------------------------------------
Subtotal ................ R$ 11,00
Cliente cadastrado: desconto de 10%
Desconto ................ -R$ 1,10
---------------------------------------
TOTAL A PAGAR ........... R$ 9,90
=======================================
```

---

## CT05 — Preço negativo rejeitado; nome **não** é relido (RN04)

```text
=======================================
   CAFETERIA - ATENDIMENTO NO BALCAO
=======================================
Quantos itens o cliente vai pedir? 2
Item 1 - nome: Água
Item 1 (Água) - preco: R$ -3,00
[ERRO] O preco deve ser maior que zero.
Item 1 (Água) - preco: R$ 4,00
Item 2 - nome: Croissant
Item 2 (Croissant) - preco: R$ 12,00
O cliente e cadastrado? (S/N): S
---------------------------------------
                CUPOM
---------------------------------------
1) Água .......... R$ 4,00
2) Croissant .......... R$ 12,00
---------------------------------------
Subtotal ................ R$ 16,00
Cliente cadastrado: desconto de 10%
Desconto ................ -R$ 1,60
---------------------------------------
TOTAL A PAGAR ........... R$ 14,40
=======================================
```

---

## CT06 — Preço zero rejeitado (RN04)

```text
=======================================
   CAFETERIA - ATENDIMENTO NO BALCAO
=======================================
Quantos itens o cliente vai pedir? 1
Item 1 - nome: Espresso
Item 1 (Espresso) - preco: R$ 0,00
[ERRO] O preco deve ser maior que zero.
Item 1 (Espresso) - preco: R$ 3,50
O cliente e cadastrado? (S/N): N
---------------------------------------
                CUPOM
---------------------------------------
1) Espresso .......... R$ 3,50
---------------------------------------
Subtotal ................ R$ 3,50
Cliente nao cadastrado: sem desconto
---------------------------------------
TOTAL A PAGAR ........... R$ 3,50
=======================================
```

---

## CT07 — Nome vazio rejeitado (RN03)

```text
=======================================
   CAFETERIA - ATENDIMENTO NO BALCAO
=======================================
Quantos itens o cliente vai pedir? 1
Item 1 - nome: ‹enter›
[ERRO] O nome do item e obrigatorio.
Item 1 - nome: Chá de hortelã
Item 1 (Chá de hortelã) - preco: R$ 7,00
O cliente e cadastrado? (S/N): S
---------------------------------------
                CUPOM
---------------------------------------
1) Chá de hortelã .......... R$ 7,00
---------------------------------------
Subtotal ................ R$ 7,00
Cliente cadastrado: desconto de 10%
Desconto ................ -R$ 0,70
---------------------------------------
TOTAL A PAGAR ........... R$ 6,30
=======================================
```

---

## CT08 — Resposta de cadastro inválida (RN06)

```text
=======================================
   CAFETERIA - ATENDIMENTO NO BALCAO
=======================================
Quantos itens o cliente vai pedir? 2
Item 1 - nome: Mocha
Item 1 (Mocha) - preco: R$ 13,90
Item 2 - nome: Cookie
Item 2 (Cookie) - preco: R$ 6,10
O cliente e cadastrado? (S/N): X
[ERRO] Responda apenas S (sim) ou N (nao).
O cliente e cadastrado? (S/N): S
---------------------------------------
                CUPOM
---------------------------------------
1) Mocha .......... R$ 13,90
2) Cookie .......... R$ 6,10
---------------------------------------
Subtotal ................ R$ 20,00
Cliente cadastrado: desconto de 10%
Desconto ................ -R$ 2,00
---------------------------------------
TOTAL A PAGAR ........... R$ 18,00
=======================================
```

---

## CT09 — Resposta minúscula aceita (RN06)

```text
=======================================
   CAFETERIA - ATENDIMENTO NO BALCAO
=======================================
Quantos itens o cliente vai pedir? 1
Item 1 - nome: Café coado
Item 1 (Café coado) - preco: R$ 6,00
O cliente e cadastrado? (S/N): s
---------------------------------------
                CUPOM
---------------------------------------
1) Café coado .......... R$ 6,00
---------------------------------------
Subtotal ................ R$ 6,00
Cliente cadastrado: desconto de 10%
Desconto ................ -R$ 0,60
---------------------------------------
TOTAL A PAGAR ........... R$ 5,40
=======================================
```

---

## CT10 — Recusa explícita: valor cheio (RN07)

```text
=======================================
   CAFETERIA - ATENDIMENTO NO BALCAO
=======================================
Quantos itens o cliente vai pedir? 2
Item 1 - nome: Torta de limão
Item 1 (Torta de limão) - preco: R$ 15,00
Item 2 - nome: Café
Item 2 (Café) - preco: R$ 5,00
O cliente e cadastrado? (S/N): n
---------------------------------------
                CUPOM
---------------------------------------
1) Torta de limão .......... R$ 15,00
2) Café .......... R$ 5,00
---------------------------------------
Subtotal ................ R$ 20,00
Cliente nao cadastrado: sem desconto
---------------------------------------
TOTAL A PAGAR ........... R$ 20,00
=======================================
```

---

## CT11 — Arredondamento *half-up* do desconto (RN09)

```text
=======================================
   CAFETERIA - ATENDIMENTO NO BALCAO
=======================================
Quantos itens o cliente vai pedir? 2
Item 1 - nome: Pingado
Item 1 (Pingado) - preco: R$ 4,55
Item 2 - nome: Sonho
Item 2 (Sonho) - preco: R$ 5,50
O cliente e cadastrado? (S/N): S
---------------------------------------
                CUPOM
---------------------------------------
1) Pingado .......... R$ 4,55
2) Sonho .......... R$ 5,50
---------------------------------------
Subtotal ................ R$ 10,05
Cliente cadastrado: desconto de 10%
Desconto ................ -R$ 1,01
---------------------------------------
TOTAL A PAGAR ........... R$ 9,04
=======================================
```

> **Nota de cálculo:** `10,05 × 0,10 = 1,005` → `Arredondar2` (*half-up*) → `1,01`.
> O total usa o desconto **já arredondado**: `10,05 − 1,01 = 9,04`. Assim as três linhas do
> cupom fecham entre si, sem centavo órfão.

---

## CT12 — Quantidade acima do limite rejeitada + pedido grande (RN02)

```text
=======================================
   CAFETERIA - ATENDIMENTO NO BALCAO
=======================================
Quantos itens o cliente vai pedir? 51
[ERRO] A quantidade deve estar entre 1 e 50.
Quantos itens o cliente vai pedir? 5
Item 1 - nome: Bandeja de salgados
Item 1 (Bandeja de salgados) - preco: R$ 45,00
Item 2 - nome: Bolo inteiro
Item 2 (Bolo inteiro) - preco: R$ 38,50
Item 3 - nome: Cesta de café especial
Item 3 (Cesta de café especial) - preco: R$ 52,80
Item 4 - nome: Kit lanche
Item 4 (Kit lanche) - preco: R$ 29,00
Item 5 - nome: Garrafa térmica de café
Item 5 (Garrafa térmica de café) - preco: R$ 22,00
O cliente e cadastrado? (S/N): S
---------------------------------------
                CUPOM
---------------------------------------
1) Bandeja de salgados .......... R$ 45,00
2) Bolo inteiro .......... R$ 38,50
3) Cesta de café especial .......... R$ 52,80
4) Kit lanche .......... R$ 29,00
5) Garrafa térmica de café .......... R$ 22,00
---------------------------------------
Subtotal ................ R$ 187,30
Cliente cadastrado: desconto de 10%
Desconto ................ -R$ 18,73
---------------------------------------
TOTAL A PAGAR ........... R$ 168,57
=======================================
```

---

## Quadro-resumo dos 12 cupons

| Caso | Itens | Erros disparados | Cadastrado | Subtotal | Desconto | **Total** |
|:----:|:-----:|------------------|:----------:|---------:|---------:|----------:|
| CT01 | 1 | — | Não | R$ 5,00 | R$ 0,00 | **R$ 5,00** |
| CT02 | 3 | — | Sim | R$ 23,50 | R$ 2,35 | **R$ 21,15** |
| CT03 | 2 | 1 (quantidade fora da faixa) | Não | R$ 12,50 | R$ 0,00 | **R$ 12,50** |
| CT04 | 1 | 1 (quantidade não inteira) | Sim | R$ 11,00 | R$ 1,10 | **R$ 9,90** |
| CT05 | 2 | 1 (preço negativo) | Sim | R$ 16,00 | R$ 1,60 | **R$ 14,40** |
| CT06 | 1 | 1 (preço zero) | Não | R$ 3,50 | R$ 0,00 | **R$ 3,50** |
| CT07 | 1 | 1 (nome vazio) | Sim | R$ 7,00 | R$ 0,70 | **R$ 6,30** |
| CT08 | 2 | 1 (resposta S/N inválida) | Sim | R$ 20,00 | R$ 2,00 | **R$ 18,00** |
| CT09 | 1 | — | Sim | R$ 6,00 | R$ 0,60 | **R$ 5,40** |
| CT10 | 2 | — | Não | R$ 20,00 | R$ 0,00 | **R$ 20,00** |
| CT11 | 2 | — | Sim | R$ 10,05 | R$ 1,01 | **R$ 9,04** |
| CT12 | 5 | 1 (quantidade acima do máximo) | Sim | R$ 187,30 | R$ 18,73 | **R$ 168,57** |

**Conferência das invariantes** — em todos os 12 cupons:
`total = subtotal − desconto` (RN08) · `0 ≤ total ≤ subtotal` (RN11) ·
`desconto = 0` ⟺ cliente não cadastrado (RN07) · todos os valores com 2 casas decimais (RN12) ·
nenhum erro de entrada abortou a execução (RN10).

---

## Observação sobre alinhamento

As saídas acima são **fiéis ao pseudocódigo**: `ExibirCupom` escreve um separador fixo de
10 pontos, então nomes de tamanhos diferentes produzem colunas desalinhadas (visível no CT12).
Se o alinhamento em coluna for desejável, basta trocar a linha de impressão do item por uma
versão com preenchimento:

```
ESCREVA i, ") ", PreencherDireita(nomes[i], 28, "."), " ",
        PreencherEsquerda(FormatarMoeda(precos[i]), 10, " ")
```

produzindo:

```text
1) Bandeja de salgados........   R$ 45,00
2) Bolo inteiro...............   R$ 38,50
3) Cesta de café especial.....   R$ 52,80
4) Kit lanche.................   R$ 29,00
5) Garrafa térmica de café....   R$ 22,00
```
