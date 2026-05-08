import pytest
from desconto.desconto import calcular_desconto

@pytest.mark.parametrize(("valor_total", "desconto", "resultado"),
                         [
                        (100, 20, 80.00),
                        (100.75, 15.5, 85.13),
                        (100, 75.83, 24.17),
                        (100.34, 10, 90.31),
                        (100, 0, 100.00),
                        (200, 100, 0.00),
                        (0.0, 24, 0.00),
                        (10, 20, 8.00)
                        ], ids=[
                        "Teste com ambos os valores positivos inteiros",
                        "Teste com ambos os valores positivos decimais",
                        "Teste com valor_total inteiro e desconto decimal",
                        "Teste com valor_total decimal e desconto inteiro",
                        "Teste com desconto igual a 0",
                        "Teste com desconto igual a 100",
                        "Teste com ValorTotal igual a 0",
                        "Teste com ValorTotal menor que desconto"
                        ])
def test_calcular_desconto_happypatch(valor_total, desconto, resultado):
    assert calcular_desconto(valor_total, desconto) == resultado
