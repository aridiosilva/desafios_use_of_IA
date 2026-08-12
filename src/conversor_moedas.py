#!/usr/bin/env python3
"""Conversor de Moedas — Agência de Viagens
Leitura de valor em R$ e menu para conversão usando taxas fixas. Opcional: converter para todas as moedas.
"""

def converter(valor_reais, taxa):
    return valor_reais / taxa


def ler_valor():
    while True:
        s = input("Valor em reais (R$): ").strip().replace(',', '.')
        try:
            v = float(s)
            if v >= 0:
                return v
            print("Valor inválido. Informe zero ou mais.")
        except ValueError:
            print("Informe um número válido.")


def menu():
    taxas = [5.2, 5.65, 6.6, 3.8, 0.006, 0.035]
    nomes = ["Dólar americano", "Euro", "Libra esterlina", "Dólar canadense", "Peso argentino", "Iene japonês"]
    simbolos = ["US$", "EUR", "GBP", "CAD", "AR$", "JPY"]
    return taxas, nomes, simbolos


def ler_opcao():
    while True:
        s = input("Opção desejada (0 encerrar): ").strip()
        if not s.isdigit():
            print("Opção inválida. Escolha de 0 a 7.")
            continue
        op = int(s)
        if 0 <= op <= 7:
            return op
        print("Opção inválida. Escolha de 0 a 7.")


def main():
    TAXA_DOLAR, TAXA_EURO, TAXA_LIBRA, TAXA_CAD, TAXA_PESO, TAXA_IENE = menu()[0]
    taxas, nomes, simbolos = menu()

    valor = ler_valor()
    while True:
        print("\n------------------------------------------")
        print("  MOEDA DE DESTINO            TAXA (R$)   ")
        for i in range(6):
            print(f"  {i+1} - {nomes[i]:18} ({simbolos[i]})  {taxas[i]:10.4f}")
        print("  7 - Converter para TODAS as moedas")
        print("  0 - Encerrar")
        print("------------------------------------------")

        op = ler_opcao()
        if op == 0:
            break
        if op == 7:
            print('\n==========================================')
            print(f'     CONVERSAO PARA TODAS AS MOEDAS       ') 
            print(f'     Valor original: R$ {valor:12.2f}')
            print('==========================================')
            print('MOEDA                 TAXA     CONVERTIDO ')
            print('------------------------------------------')
            for i in range(6):
                conv = converter(valor, taxas[i])
                print(f"{simbolos[i]:4} {nomes[i]:18} {taxas[i]:9.4f} {conv:13.2f}")
            print('==========================================')
        else:
            idx = op - 1
            taxa = taxas[idx]
            conv = converter(valor, taxa)
            print('\n==========================================')
            print('       COMPROVANTE DE CONVERSAO           ')
            print('==========================================')
            print(f'Valor original ......: R$ {valor:12.2f}')
            print(f'Moeda de destino ....: {nomes[idx]} ({simbolos[idx]})')
            print(f'Taxa aplicada .......: R$ {taxa:8.4f} por 1 {simbolos[idx]}')
            print('------------------------------------------')
            print(f'VALOR CONVERTIDO ....: {simbolos[idx]} {conv:12.2f}')
            print('==========================================')

    print('\nConversão encerrada. Boa viagem!')

if __name__ == '__main__':
    main()
