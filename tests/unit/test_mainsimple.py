import pytest

from main import somar, subtrair, dividir

# Lista de tuplas
lista_de_valores = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7)
]

# Na função test_somar não é utilizado pytest. O assert é nativo do Python

def test_somar():
    # 1 - Configure
    num1 = 1
    num2 = 2
    resultado_esperado = 3

    # 2 - Execute
    resultado_obtido = somar(num1, num2)

    # 3 - Validate
    assert resultado_obtido == resultado_esperado

@pytest.mark.parametrize('num_a, num_b, resultado_esperado', lista_de_valores)
def test_somar_leitura_de_lista(num_a, num_b, resultado_esperado):
        # 1 - Configure
        # Utilizamos a lista como massa de teste

        # 2 - Execute
        resultado_obtido = somar(num_a, num_b)

        # 3 - Validate
        assert resultado_obtido == resultado_esperado

