import pytest

def print_hi(name):
    print(f'Hi, {name}')

def somar(num1, num2):
    return num1+num2

def dividir(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return 'Não dividiras por zero'

if __name__ == '__main__':
    print_hi('PyCharm')

    resultado = somar(1, 1)
    print(f"A soma : {resultado}")
