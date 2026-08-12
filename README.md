[![CI](https://github.com/aridiosilva/desafios_use_of_IA/actions/workflows/ci.yml/badge.svg)](https://github.com/aridiosilva/desafios_use_of_IA/actions)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

# Desafios — Uso de IA

Este repositório reúne os desafios desenvolvidos na Pós-Graduação — Trilha de ESPECIALISTA DE IA. Cada documento contém a especificação do problema, a regra de negócio, descrições em linguagem natural, fluxogramas, pseudocódigo (versões direta e, quando aplicável, modular) e conjuntos de testes/execuções que demonstram o comportamento esperado.

## Sumário

- [Desafios atendidos](#desafios-atendidos)
- [1 - cinema-meia-entrada.md](./cinema-meia-entrada.md)
  - [Especificação](./cinema-meia-entrada.md#1-especificação)
  - [Pseudocódigo](./cinema-meia-entrada.md#4-pseudocódigo--versão-direta)
  - [Teste de mesa](./cinema-meia-entrada.md#6-teste-de-mesa)
- [2 - classificacao-desempenho-academico.md](./classificacao-desempenho-academico.md)
  - [Enunciado e regra de negócio](./classificacao-desempenho-academico.md#1-enunciado-e-regra-de-negócio)
  - [Pseudocódigo / Fluxograma](./classificacao-desempenho-academico.md#3-fluxograma)
- [3 - controle-financeiro-pessoal.md](./controle-financeiro-pessoal.md)
  - [Arquitetura e módulos](./controle-financeiro-pessoal.md#3-arquitetura-modular)
  - [Exemplo de execução](./controle-financeiro-pessoal.md#5-exemplo-de-execução--demonstrativo-em-markdown)
- [4 - conversor-moedas.md](./conversor-moedas.md)
  - [Função de conversão](./conversor-moedas.md#2-a-função-de-conversão--o-coração-do-algoritmo)
  - [Menu e exemplos](./conversor-moedas.md#8-teste-de-mesa-e-exemplo-de-execução)
- [5 - delivery-taxa-entrega.md](./delivery-taxa-entrega.md)
  - [Regras por faixa](./delivery-taxa-entrega.md#1-especificação)
  - [Pseudocódigo & fluxograma](./delivery-taxa-entrega.md#6-pseudocódigo--versão-direta)
- [6 - lanchonete-calculo-pedido.md](./lanchonete-calculo-pedido.md)
  - [Cardápio e leitura de quantidades](./lanchonete-calculo-pedido.md#1-especificação)
  - [Versões: direta / modular / vetores](./lanchonete-calculo-pedido.md#6-pseudocódigo--versão-com-vetores)
- [7 - simulador-cafeteria.md](./simulador-cafeteria.md)
  - [Regras (RN01–RN12)](./simulador-cafeteria.md#2-regras-de-negócio)
  - [Pseudocódigo modularizado](./simulador-cafeteria.md#7-pseudocódigo-modularizado)
- [8 - simulador-cafeteria-saidas.md](./simulador-cafeteria-saidas.md)
  - [Saídas simuladas CT01–CT12](./simulador-cafeteria-saidas.md#ct01--ct12)

## Desafios atendidos

- [1 - cinema-meia-entrada.md](./cinema-meia-entrada.md) — Projeto de um sistema de bilheteria que determina o direito à meia-entrada. Contém especificação, dicionário de variáveis, validações de entrada, fluxogramas (Mermaid), pseudocódigo (direto e modular) e testes de mesa cobrindo fronteiras, com decisões de projeto documentadas.

- [2 - classificacao-desempenho-academico.md](./classificacao-desempenho-academico.md) — Classificação pedagógica por média final: regras, validação, fluxogramas, pseudocódigo (direto e modular), testes de mesa e justificativas sobre faixas e limites.

- [3 - controle-financeiro-pessoal.md](./controle-financeiro-pessoal.md) — Registro de despesas por tipo, apuração estatística (totais, menor/maior, média, percentuais), ordenação por nome e emissão de demonstrativo. Inclui versão modular e exemplos em Markdown.

- [4 - conversor-moedas.md](./conversor-moedas.md) — Conversor com função pura de conversão, menu interativo, opção de converter para todas as moedas, tabela de taxas fixas, fluxogramas e testes de mesa; projetado para ser testável e extensível.

- [5 - delivery-taxa-entrega.md](./delivery-taxa-entrega.md) — Cálculo de taxa por faixa de distância e adicional por chuva; documentação das regras, pseudocódigo modular/direto, fluxogramas e exemplos de casos.

- [6 - lanchonete-calculo-pedido.md](./lanchonete-calculo-pedido.md) — Cálculo do pedido com 8 itens: leitura de quantidades, subtotais, total de itens e cupom; apresenta versões direta, modular e com vetores para escalabilidade.

- [7 - simulador-cafeteria.md](./simulador-cafeteria.md) — Simulador de pedidos por balcão com validações robustas, desconto para cliente cadastrado (10%) com arredondamento half-up, pseudocódigo modular e casos de teste detalhados.

- [8 - simulador-cafeteria-saidas.md](./simulador-cafeteria-saidas.md) — Saídas de tela simuladas para os 12 casos de teste do simulador de cafeteria, úteis para validar UX textual, mensagens e alinhamento.
