#!/usr/bin/env python3
"""Delivery — Cálculo da Taxa de Entrega
Calcula taxa com base em distância e adicional em caso de chuva.
"""

def ler_distancia():
    while True:
        s = input("Distância até o cliente (km): ").strip().replace(',', '.')
        try:
            d = float(s)
            if d >= 0:
                return d
            print("Distância inválida. Informe zero ou mais.")
        except ValueError:
            print("Informe um número válido.")


def ler_chuva():
    while True:
        r = input("Está chovendo? (S/N): ").strip().upper()
        if r in ("S", "N"):
            return r == "S"
        print("Resposta inválida. Digite S ou N.")


def taxa_base(dist):
    if dist <= 5:
        return 5.00, "até 5 km"
    if dist <= 10:
        return 8.00, "acima de 5 até 10 km"
    return 10.00, "acima de 10 km"


def main():
    TAXA_CURTA = 5.00
    TAXA_MEDIA = 8.00
    TAXA_LONGA = 10.00
    ADICIONAL_CHUVA = 2.00

    distancia = ler_distancia()
    chuva = ler_chuva()

    base, faixa = taxa_base(distancia)
    adicional = ADICIONAL_CHUVA if chuva else 0.00
    final = base + adicional

    print('\n========================================')
    print('        COMPROVANTE DE ENTREGA          ')
    print('========================================')
    print(f'Distância informada .....: {distancia:0.1f} km')
    print(f'Faixa aplicada ..........: {faixa}')
    print('Condicao do tempo .......: ' + ('COM CHUVA' if chuva else 'SEM CHUVA'))
    print('----------------------------------------')
    print(f'Taxa base ...............: R$ {base:7.2f}')
    print(f'Adicional de chuva ......: R$ {adicional:7.2f}')
    print('----------------------------------------')
    print(f'VALOR FINAL DA ENTREGA ..: R$ {final:7.2f}')
    print('========================================')

if __name__ == '__main__':
    main()
