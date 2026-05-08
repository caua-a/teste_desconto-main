import pytest
from desconto.desconto import calcular_desconto

def test_valores_NaN():
    with pytest.raises(TypeError, match="Erro: O valor total e o desconto devem ser numéricos"):
        calcular_desconto("casa", None)

def test_valor_total_NaN():
    with pytest.raises(TypeError, match="Erro: O valor total e o desconto devem ser numéricos"):
        calcular_desconto('casa', 10)

def test_desconto_NaN():
    with pytest.raises(TypeError, match="Erro: O valor total e o desconto devem ser numéricos"):
        calcular_desconto(10, 'senai')

def test_valor_total_menor_0():
    with pytest.raises(ValueError, match="Erro: O valor do produto não pode ser negativo."):
        calcular_desconto(-10, 25.6)

def test_desconto_maior_100():
    with pytest.raises(ValueError, match="Erro: O desconto deve estar entre 0 e 100."):
        calcular_desconto(105, 110)

def test_desconto_menor_0():
    with pytest.raises(ValueError, match="Erro: O desconto deve estar entre 0 e 100."):
        calcular_desconto(105, -0.1)