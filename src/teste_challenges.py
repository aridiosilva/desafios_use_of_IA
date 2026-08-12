import pytest
import sys
import os
from io import StringIO

# Add src to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import all challenges
import cinema_meia_entrada
import classificacao_desempenho_academico
import controle_financeiro_pessoal
import conversor_moedas
import delivery_taxa_entrega
import lanchonete_calculo_pedido
import simulador_cafeteria

# 1. Cinema Meia-Entrada tests
def test_cinema_tem_direito():
    # menos de 18 anos ou estudante
    assert cinema_meia_entrada.tem_direito(17, False) is True
    assert cinema_meia_entrada.tem_direito(17, True) is True
    assert cinema_meia_entrada.tem_direito(18, True) is True
    assert cinema_meia_entrada.tem_direito(18, False) is False
    assert cinema_meia_entrada.tem_direito(25, False) is False

def test_cinema_inputs(monkeypatch):
    # Test valid outputs and inputs
    inputs = iter(["17", "N"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert cinema_meia_entrada.ler_idade() == 17
    assert cinema_meia_entrada.ler_estudante() is False

    # Test invalid inputs followed by valid input
    inputs_invalid = iter(["-5", "150", "abc", "25", "invalid", "s"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_invalid))
    assert cinema_meia_entrada.ler_idade() == 25
    assert cinema_meia_entrada.ler_estudante() is True

def test_cinema_main(monkeypatch, capsys):
    inputs = iter(["20", "N"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    cinema_meia_entrada.main()
    captured = capsys.readouterr().out
    assert "Idade informada .....: 20 anos" in captured
    assert "É estudante? ........: N" in captured
    assert "Cliente NÃO tem direito à meia-entrada" in captured


# 2. Classificação Desempenho Acadêmico tests
def test_classificacao_rules():
    assert classificacao_desempenho_academico.classificar(4.9) == ("REPROVADO", "Você está reprovado.")
    assert classificacao_desempenho_academico.classificar(5.0) == ("RECUPERACAO", "Você está de recuperação.")
    assert classificacao_desempenho_academico.classificar(6.9) == ("RECUPERACAO", "Você está de recuperação.")
    assert classificacao_desempenho_academico.classificar(7.0) == ("APROVADO", "Parabéns! Você foi aprovado.")
    assert classificacao_desempenho_academico.classificar(10.0) == ("APROVADO", "Parabéns! Você foi aprovado.")

def test_classificacao_ler_media(monkeypatch):
    inputs = iter(["-1", "11", "abc", "7.5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert classificacao_desempenho_academico.ler_media() == 7.5

    inputs_comma = iter(["8,2"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_comma))
    assert classificacao_desempenho_academico.ler_media() == 8.2


# 3. Controle Financeiro Pessoal tests
def test_controle_financeiro_normalize():
    assert controle_financeiro_pessoal.normalize("  Aluguel  ") == "ALUGUEL"
    assert controle_financeiro_pessoal.normalize("ALIMENTAÇÃO ") == "ALIMENTAÇÃO"

def test_controle_financeiro_main(monkeypatch, capsys):
    # Simulate: Aluguel 1200.50, Alimentacao 450.00, FIM
    inputs = iter(["Aluguel", "1200.50", "Alimentacao", "450.00", "FIM"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    controle_financeiro_pessoal.main()
    captured = capsys.readouterr().out
    assert "ALUGUEL" in captured
    assert "ALIMENTACAO" in captured
    assert "1650.50" in captured  # Total general gasto

    # Test sentinel value 0
    inputs_zero = iter(["Transporte", "0"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_zero))
    controle_financeiro_pessoal.main()
    captured = capsys.readouterr().out
    assert "Nenhuma despesa registrada." in captured


# 4. Conversor Moedas tests
def test_conversor_converter():
    assert conversor_moedas.converter(100.0, 5.0) == 20.0
    assert conversor_moedas.converter(50.0, 2.0) == 25.0

def test_conversor_main(monkeypatch, capsys):
    # Option 1 (Dolar), then Option 0 (Exit)
    inputs = iter(["100.0", "1", "0"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    conversor_moedas.main()
    captured = capsys.readouterr().out
    assert "Valor original ......: R$       100.00" in captured
    assert "VALOR CONVERTIDO ....: US$        19.23" in captured # 100 / 5.2

    # Option 7 (All), then Option 0
    inputs_all = iter(["200.0", "7", "0"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_all))
    conversor_moedas.main()
    captured_all = capsys.readouterr().out
    assert "CONVERSAO PARA TODAS AS MOEDAS" in captured_all
    assert "EUR" in captured_all
    assert "GBP" in captured_all


# 5. Delivery Taxa Entrega tests
def test_delivery_taxa_base():
    assert delivery_taxa_entrega.taxa_base(3.0) == (5.0, "até 5 km")
    assert delivery_taxa_entrega.taxa_base(5.0) == (5.0, "até 5 km")
    assert delivery_taxa_entrega.taxa_base(5.1) == (8.0, "acima de 5 até 10 km")
    assert delivery_taxa_entrega.taxa_base(10.0) == (8.0, "acima de 5 até 10 km")
    assert delivery_taxa_entrega.taxa_base(10.1) == (10.0, "acima de 10 km")

def test_delivery_main(monkeypatch, capsys):
    # Distance 6km, Rain Yes
    inputs = iter(["6.0", "S"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    delivery_taxa_entrega.main()
    captured = capsys.readouterr().out
    assert "Distância informada .....: 6.0 km" in captured
    assert "Condicao do tempo .......: COM CHUVA" in captured
    assert "Taxa base ...............: R$    8.00" in captured
    assert "Adicional de chuva ......: R$    2.00" in captured
    assert "VALOR FINAL DA ENTREGA ..: R$   10.00" in captured


# 6. Lanchonete Cálculo Pedido tests
def test_lanchonete_main(monkeypatch, capsys):
    # Quantities: 1 Hambúrguer (item 0), 2 X-Salada (item 1), others 0
    inputs = iter(["1", "2", "0", "0", "0", "0", "0", "0"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    lanchonete_calculo_pedido.main()
    captured = capsys.readouterr().out
    # Hambúrguer R$ 12.00, X-Salada R$ 15.00 * 2 = R$ 30.00
    # Total = 12 + 30 = 42.00
    assert "Hambúrguer" in captured
    assert "X-Salada" in captured
    assert "TOTAL DE ITENS ..................: 3" in captured
    assert "VALOR TOTAL .....................: R$ 42.00" in captured


# 7. Simulador Cafeteria tests
def test_cafeteria_arred2():
    assert simulador_cafeteria.arred2(1.005) == 1.01
    assert simulador_cafeteria.arred2(1.004) == 1.00
    assert simulador_cafeteria.arred2(1.006) == 1.01

def test_cafeteria_main_ct01(monkeypatch, capsys):
    # CT01 — Caminho feliz: não cadastrado, 1 item
    inputs = iter(["1", "Café expresso", "5.00", "N"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    simulador_cafeteria.main()
    captured = capsys.readouterr().out
    assert "1) Café expresso .......... 5.00" in captured
    assert "Subtotal ................ 5.00" in captured
    assert "Cliente nao cadastrado: sem desconto" in captured
    assert "TOTAL A PAGAR ........... 5.00" in captured

def test_cafeteria_main_ct02(monkeypatch, capsys):
    # CT02 — Caminho feliz: cadastrado, 3 itens
    inputs = iter(["3", "Cappuccino", "9.50", "Pão de queijo", "6.00", "Suco de laranja", "8.00", "S"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    simulador_cafeteria.main()
    captured = capsys.readouterr().out
    assert "1) Cappuccino .......... 9.50" in captured
    assert "2) Pão de queijo .......... 6.00" in captured
    assert "3) Suco de laranja .......... 8.00" in captured
    assert "Subtotal ................ 23.50" in captured
    assert "Cliente cadastrado: desconto de 10%" in captured
    assert "Desconto ................ -2.35" in captured
    assert "TOTAL A PAGAR ........... 21.15" in captured

def test_cafeteria_main_ct11(monkeypatch, capsys):
    # CT11 — Arredondamento half-up do desconto
    inputs = iter(["2", "Pingado", "4.55", "Sonho", "5.50", "S"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    simulador_cafeteria.main()
    captured = capsys.readouterr().out
    assert "Subtotal ................ 10.05" in captured
    assert "Desconto ................ -1.01" in captured
    assert "TOTAL A PAGAR ........... 9.04" in captured
