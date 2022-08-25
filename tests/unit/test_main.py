import pytest

from main import somar, dividir

def test_somar():
    # 1 - Configure
    num_a = 9
    num_b = 1
    resultado_esperado = 10

    # 2 - Execute
    resultado_obtido = somar(num_a, num_b)

    # 3 - Validate
    assert resultado_obtido == resultado_esperado

def test_dividir_positivo():
    # 1 - Configure
    # 1.1 - Dados de Entrada
    num_a = 8
    num_b = 2

    # 1.2 - Resultados Esperados
    resultado_esperado = 4

    # 2 - Execute
    resultado_obtido = dividir(num_a, num_b)

    # 3 - Check
    assert resultado_obtido == resultado_esperado

def test_dividir_negativo():
        # 1 - Configure
        # 1.1 - Dados de Entrada
        num_a = 8
        num_b = 0

        # 1.2 - Resultados Esperados
        resultado_esperado = 'Não dividiras por zero'

        # 2 - Execute
        resultado_obtido = dividir(num_a, num_b)

        # 3 - Check
        assert resultado_obtido == resultado_esperado

# lista para uso como massa de teste
lista_de_valores = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7)
]

@pytest.mark.parametrize('num_a, num_b, resultado_esperado', lista_de_valores)
def test_somar_leitura_de_lista(num_a, num_b, resultado_esperado):
        # 1 - Configure
        # Utilizamos a lista como massa de teste

        # 2 - Execute
        resultado_obtido = somar(num_a, num_b)

        # 3 - Validate
        assert resultado_obtido == resultado_esperado