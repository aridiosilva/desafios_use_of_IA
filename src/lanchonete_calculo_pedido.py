#!/usr/bin/env python3
"""Lanchonete — Cálculo do Valor Total do Pedido
Lê quantidades dos 8 itens do cardápio, valida entradas, calcula subtotais e imprime cupom.
"""

def ler_int(prompt):
    while True:
        s = input(prompt).strip()
        try:
            i = int(s)
            if i >= 0:
                return i
            print('Quantidade inválida. Informe zero ou mais.')
        except ValueError:
            print('Quantidade inválida. Informe um número inteiro.')


def main():
    precos = [12.00, 15.00, 9.00, 7.00, 10.00, 5.00, 6.00, 11.00]
    nomes = ['Hambúrguer','X-Salada','Cachorro-quente','Batata frita','Porção de nuggets','Refrigerante','Suco natural','Milk-shake']

    print('========================================')
    print('            CARDAPIO                    ')
    print('========================================')
    for nome, preco in zip(nomes, precos):
        print(f'{nome:20s} R$ {preco:0.2f}')
    print('========================================')
    print('Informe a quantidade de cada item (0 = nao quero).')

    qts = [0]*8
    for i, nome in enumerate(nomes):
        qts[i] = ler_int(f'{nome:16s} (R$ {precos[i]:0.2f}) - qtd: ')

    subtotais = [q*p for q,p in zip(qts, precos)]
    total_pedido = sum(subtotais)
    total_itens = sum(qts)

    print('\n========================================')
    print('            CUPOM DO PEDIDO             ')
    print('========================================')
    if total_itens == 0:
        print('Nenhum item foi solicitado.')
    else:
        print('ITEM              QTD    UNIT  SUBTOTAL')
        print('----------------------------------------')
        for nome, q, preco, sub in zip(nomes, qts, precos, subtotais):
            if q > 0:
                print(f'{nome:16s}{q:6d}{preco:8.2f}{sub:10.2f}')
        print('----------------------------------------')
        print(f'TOTAL DE ITENS ..................: {total_itens}')
        print(f'VALOR TOTAL .....................: R$ {total_pedido:0.2f}')
    print('========================================')

if __name__ == '__main__':
    main()
