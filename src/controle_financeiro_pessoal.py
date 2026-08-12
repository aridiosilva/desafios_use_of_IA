#!/usr/bin/env python3
"""Controle Financeiro Pessoal (interativo)
Registra despesas por tipo até entrada sentinel (FIM ou valor 0) e emite demonstrativo ordenado por nome.
"""
from collections import defaultdict


def normalize(tipo: str) -> str:
    return ' '.join(tipo.strip().upper().split())


def ler_tipo():
    t = input("Tipo da despesa (ou FIM): ").strip()
    return t


def ler_valor():
    while True:
        s = input("Valor (R$): ").strip().replace(',', '.')
        try:
            v = float(s)
            return v
        except ValueError:
            print("Valor inválido. Digite um número (ex: 12.50)")


def main():
    print("=== LANCAMENTO DE DESPESAS ===")
    print("Digite FIM no tipo, ou 0 no valor, para encerrar.")

    dados = {}  # nome -> {total, qtd, menor, maior}
    total_geral = 0.0
    qtd_geral = 0

    while True:
        tipo = ler_tipo()
        if tipo.strip().upper() == 'FIM':
            break
        tipo_norm = normalize(tipo)
        valor = ler_valor()
        if valor == 0:
            break
        if valor < 0:
            print('>> Valor inválido. Informe um valor positivo.')
            continue
        if tipo_norm not in dados:
            dados[tipo_norm] = {'total': valor, 'qtd': 1, 'menor': valor, 'maior': valor}
        else:
            rec = dados[tipo_norm]
            rec['total'] += valor
            rec['qtd'] += 1
            rec['menor'] = min(rec['menor'], valor)
            rec['maior'] = max(rec['maior'], valor)
        total_geral += valor
        qtd_geral += 1

    if not dados:
        print('\nNenhuma despesa registrada.')
        return

    # ordenar por nome
    itens = sorted(dados.items(), key=lambda x: x[0])

    print('\n# CONTROLE FINANCEIRO')
    print('\n### Demonstrativo por tipo de despesa')
    print('| Tipo da Despesa | Qtde | Total Gasto | Menor Valor | Maior Valor | Valor Medio | % do Total |')
    print('|:----------------|-----:|------------:|------------:|------------:|------------:|-----------:|')
    for nome, rec in itens:
        total = rec['total']
        qtd = rec['qtd']
        menor = rec['menor']
        maior = rec['maior']
        media = total / qtd
        perc = (total / total_geral) * 100
        print(f"| {nome} | {qtd:5d} |  R$ {total:8.2f} |   R$ {menor:7.2f} |  R$ {maior:7.2f} |   R$ {media:7.2f} |  {perc:6.2f}% |")

    # resumo geral
    pos_maior = max(itens, key=lambda x: x[1]['total'])
    pos_menor = min(itens, key=lambda x: x[1]['total'])
    pos_media = max(itens, key=lambda x: x[1]['total']/x[1]['qtd'])

    def media_geral():
        return total_geral / qtd_geral if qtd_geral else 0.0

    print('\n### Resumo geral')
    print('\n| Indicador | Tipo correspondente | Valor |')
    print('|:----------|:--------------------|------:|')
    print(f"| **Total geral gasto** | - | **R$ {total_geral:0.2f}** |")
    print(f"| **Qtde total de despesas** | - | **{qtd_geral}** |")
    print(f"| **Valor medio geral** | - | **R$ {media_geral():0.2f}** |")
    print(f"| **Despesa de maior gasto** | **{pos_maior[0]}** | **R$ {pos_maior[1]['total']:0.2f}** |")
    print(f"| **Despesa de menor gasto** | **{pos_menor[0]}** | **R$ {pos_menor[1]['total']:0.2f}** |")
    print(f"| **Despesa de maior valor medio** | **{pos_media[0]}** | **R$ {pos_media[1]['total']/pos_media[1]['qtd']:0.2f}** |")


if __name__ == '__main__':
    main()
