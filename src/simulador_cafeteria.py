#!/usr/bin/env python3
"""Simulador de Pedidos — Cafeteria
Registra N itens (nome e preço), aplica desconto para cliente cadastrado e emite cupom.
Arredondamento comercial (half-up) para 2 casas decimais usado no desconto e total.
"""
from decimal import Decimal, ROUND_HALF_UP


def arred2(v):
    d = Decimal(str(v)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return float(d)


def ler_int(prompt, minv=1, maxv=50):
    while True:
        s = input(prompt).strip()
        try:
            n = int(s)
            if minv <= n <= maxv:
                return n
            print(f'Quantidade inválida. Informe entre {minv} e {maxv}.')
        except ValueError:
            print('Informe um número inteiro.')


def ler_nome(i):
    while True:
        nome = input(f'Item {i} - nome: ').strip()
        if len(nome) == 0:
            print('Erro: nome obrigatório.')
            continue
        return nome


def ler_preco(i, nome):
    while True:
        s = input(f'Item {i} ({nome}) - preco: R$ ').strip().replace(',', '.')
        try:
            p = float(s)
            if p > 0:
                return p
            print('O preco deve ser maior que zero.')
        except ValueError:
            print('Informe um valor numerico.')


def ler_cadastrado():
    while True:
        r = input('O cliente e cadastrado? (S/N): ').strip().upper()
        if r in ('S','N'):
            return r == 'S'
        print('Responda apenas S (sim) ou N (nao).')


def main():
    print('=======================================')
    print('   CAFETERIA - ATENDIMENTO NO BALCAO   ')
    print('=======================================')

    qtd = ler_int('Quantos itens o cliente vai pedir? ')
    nomes = []
    precos = []
    for i in range(1, qtd+1):
        nome = ler_nome(i)
        preco = ler_preco(i, nome)
        nomes.append(nome)
        precos.append(preco)

    subtotal = round(sum(precos), 2)
    cadastrado = ler_cadastrado()

    desconto = arred2(subtotal * 0.10) if cadastrado else 0.0
    total = arred2(subtotal - desconto)

    print('---------------------------------------')
    print('                CUPOM                  ')
    print('---------------------------------------')
    for i, (n, p) in enumerate(zip(nomes, precos), start=1):
        print(f'{i}) {n} .......... {arred2(p):.2f}')
    print('---------------------------------------')
    print(f'Subtotal ................ {arred2(subtotal):.2f}')
    if cadastrado:
        print('Cliente cadastrado: desconto de 10%')
        print(f'Desconto ................ -{desconto:.2f}')
    else:
        print('Cliente nao cadastrado: sem desconto')
    print('---------------------------------------')
    print(f'TOTAL A PAGAR ........... {total:.2f}')
    print('=======================================')

if __name__ == '__main__':
    main()
