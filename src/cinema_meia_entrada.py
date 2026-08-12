#!/usr/bin/env python3
"""Bilheteria de Cinema — Verificação de Direito à Meia-Entrada
Interativo: pergunta idade e se é estudante; valida entradas e informa se tem direito à meia-entrada.
"""

def ler_idade():
    while True:
        try:
            s = input("Idade do cliente: ").strip()
            idade = int(s)
            if 0 <= idade <= 120:
                return idade
            print("Idade inválida. Informe um valor entre 0 e 120.")
        except ValueError:
            print("Idade inválida. Informe um número inteiro.")


def ler_estudante():
    while True:
        r = input("O cliente é estudante? (S/N): ").strip().upper()
        if r in ("S", "N"):
            return r == "S"
        print("Resposta inválida. Digite S ou N.")


def tem_direito(idade, estudante):
    return (idade < 18) or estudante


def main():
    print("========================================")
    print("       BILHETERIA - MEIA-ENTRADA        ")
    print("========================================")
    idade = ler_idade()
    estudante = ler_estudante()
    direito = tem_direito(idade, estudante)

    print("\n----------------------------------------")
    print(f"Idade informada .....: {idade} anos")
    print(f"É estudante? ........: {'S' if estudante else 'N'}")
    print("----------------------------------------")
    if direito:
        print("Cliente TEM direito à meia-entrada.")
    else:
        print("Cliente NÃO tem direito à meia-entrada. Pagará inteira.")
    print("========================================")


if __name__ == '__main__':
    main()
