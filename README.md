# Desafios — Uso de IA

Este repositório reúne os desafios desenvolvidos na Pós-Graduação — Trilha de ESPECIALISTA DE IA. Cada documento contém a especificação do problema, a regra de negócio, descrições em linguagem natural, fluxogramas, pseudocódigo (versões direta e, quando aplicável, modular) e conjuntos de testes/execuções que demonstram o comportamento esperado.

## Desafios atendidos

- [1 - cinema-meia-entrada.md](./cinema-meia-entrada.md) — Projeto de um sistema de bilheteria que determina o direito à meia-entrada. O documento traz a especificação de entrada/processamento/saída, o dicionário de variáveis, algoritmo em linguagem natural com validação de entrada, fluxogramas renderizáveis (Mermaid), duas versões de pseudocódigo (direta e modularizada), testes de mesa cobrindo as fronteiras e uma seção com decisões de projeto e justificativas técnicas.

- [2 - classificacao-desempenho-academico.md](./classificacao-desempenho-academico.md) — Classificação do desempenho escolar com base na média final: reprovado, recuperação ou aprovado. Contém a regra pedagógica detalhada, validações de entrada, fluxograma, pseudocódigo e variantes modularizadas, além de justificativas sobre a escolha das faixas, testes de mesa e recomendações de implementação para garantir exaustividade e eficiência.

- [3 - controle-financeiro-pessoal.md](./controle-financeiro-pessoal.md) — Sistema para registro de despesas por tipo e emissão de demonstrativo mensal. O documento descreve a modelagem com listas paralelas, operações de criação/atualização de tipos, ordenação alfabética por tipo, apuração de totais, menores/maiores, cálculo de médias e percentuais, além de uma versão modular, pseudocódigo completo, exemplo de execução em Markdown e considerações sobre limites e extensões (por ex., limites fixos vs. estruturas dinâmicas).

- [4 - conversor-moedas.md](./conversor-moedas.md) — Conversor de moedas pensado para uma agência de viagens: definição de uma função pura de conversão, tabela de taxas fixas, menu interativo, opção de "converter para todas as moedas" e variantes modularizadas. Inclui discussão sobre a convenção de taxas (R$ por unidade), testes de mesa, fluxogramas Mermaid e exemplos de saída formatada, além de recomendações para manter a função testável e extensível.

- [5 - delivery-taxa-entrega.md](./delivery-taxa-entrega.md) — Cálculo da taxa de entrega baseado em faixas de distância e adicional por chuva. Contém a tabela de regras (faixas mutuamente exclusivas), validação de entrada, pseudocódigo direto e modular, fluxogramas, exemplos de casos de teste cobrindo combinações distância × chuva e decisões de projeto que garantem clareza entre a regra de faixa e a condição independente do adicional.

- [6 - lanchonete-calculo-pedido.md](./lanchonete-calculo-pedido.md) — Implementação do cálculo do valor total de um pedido em lanchonete: cardápio, leitura de quantidades, cálculo de subtotais por item, total de itens e emissão de cupom. Apresenta versões direta (uma variável por item), modular e com vetores (para escalabilidade), fluxogramas, validações por item e exemplos de execução que ilustram a diferença entre implementação literal e implementações mais reutilizáveis.

- [7 - simulador-cafeteria.md](./simulador-cafeteria.md) — Simulador de pedidos para atendimento no balcão: registro de N itens (nome e preço), validações rigorosas (nome obrigatório, preço > 0, limite de itens), aplicação de desconto para cliente cadastrado com arredondamento comercial (half-up) e emissão de cupom. O repositório inclui especificação das regras RN01–RN12, pseudocódigo modular, funções utilitárias (arredondamento e formatação) e casos de teste que cobrem caminhos felizes e validações.

- [8 - simulador-cafeteria-saidas.md](./simulador-cafeteria-saidas.md) — Conjunto de saídas de tela simuladas para os 12 casos de teste do simulador de cafeteria (CT01–CT12). Cada bloco reproduz a sessão completa no terminal, com prompts, entradas, mensagens de erro e cupom final; útil para validar a UX textual e conferir alinhamento, mensagens de erro e arredondamentos.
