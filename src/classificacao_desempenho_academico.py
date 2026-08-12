#!/usr/bin/env python3
"""Classificação de Desempenho Acadêmico
Lê média final (0.0 a 10.0) e exibe situação: Reprovado / Recuperação / Aprovado
"""

def ler_media():
    while True:
        try:
            s = input("Informe a média final (0,0 a 10,0): ").strip().replace(',', '.')
            m = float(s)
            if 0.0 <= m <= 10.0:
                return m
            print("Média inválida. Informe um valor entre 0,0 e 10,0.")
        except ValueError:
            print("Média inválida. Informe um número.")


def classificar(media):
    if media < 5.0:
        return "REPROVADO", "Você está reprovado."
    if media < 7.0:
        return "RECUPERACAO", "Você está de recuperação."
    return "APROVADO", "Parabéns! Você foi aprovado."


def main():
    media = ler_media()
    codigo, mensagem = classificar(media)
    print("\n=== RESULTADO ===")
    print(f"Média final: {media:.1f}")
    print(mensagem)

if __name__ == '__main__':
    main()
