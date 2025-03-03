import pytest

from main import somar

@pytest.fixture
def massa_temporaria():
    massa = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7)
]
    yield massa



def test_soma (massa_temporaria):
    for num1, num2, resultado_esperado in massa_temporaria:
        assert somar(num1, num2) == resultado_esperado

