# ToDo: 3 - criar uma venda de um pet para um usuário
# ToDo: 4 - Consultar os dados do pet que foi vendido
import os

import requests

url = 'https://petstore.swagger.io/v2/'
headers = {'Content-Type': 'application/json'}

def test_vender_pet():
    #Configura
    #Dados de entrada
    #virão do arquivo pedido1.json
    #root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    #file_dir = os.path.join(root_dir, 'vendors', 'json', 'pedido1.json')
    with open('C:\\Users\\rigna\\PycharmProjects\\134inicial\\vendors\\json\\pedido1.json', 'r') as file:
        data = file.read()
    #https://towardsdatascience.com/simple-trick-to-work-with-relative-paths-in-python-c072cdc9acb9

    #pode ser feito como: caminho = os.path.abspath(__file__ + "/../../../") + os.sep + 'vendors' + os.sep + 'json' + os.sep

    # Resultados esperados
    status_code_esperado = 200
    pedido_id_esperado = 41511
    pet_id_esperado = 4358369
    status_pedido_esperado = 'placed'

    #Executa
    resultado_obtido = requests.post(
        url=url + 'store/order',
        headers=headers,
        data=data
    )
    #Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pedido_id_esperado
    assert corpo_do_resultado_obtido['petId'] == pet_id_esperado
    assert corpo_do_resultado_obtido['status'] == status_pedido_esperado

    #Extrai
    pet_id_extraido = corpo_do_resultado_obtido.get('petId')

    #Realizar a 2² transação

    #Configura
    #Dados de entrada
    #Extraidos da 1² transição acima

    #Resultados esperados
    pet_name_esperado = 'Snoopy'
    status_code_esperado = 200

    #Executa
    resultado_obtido = requests.get(
        url=url + 'pet/' + str(pet_id_extraido),
        headers=headers
    )

    #Valida
    assert resultado_obtido.status_code == status_code_esperado
    corpo_do_resultado_obtido = resultado_obtido.json()
    assert corpo_do_resultado_obtido['name'] == pet_name_esperado

def test_deletar_pedido():
    #Dados de entrada
    orderId = 41511

    #Resultados esperados
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    mensagem_esperada = '41511'

    #Executa
    resultado_obtido = requests.delete(
        url = url + 'store/order/' + str(orderId),
        headers=headers
    )

    #Valida
    assert resultado_obtido.status_code == status_code_esperado
    corpo_do_resultado_obtido = resultado_obtido.json()
    assert corpo_do_resultado_obtido['code'] == code_esperado
    assert corpo_do_resultado_obtido['type'] == type_esperado
    assert corpo_do_resultado_obtido['message'] == mensagem_esperada

def test_consultar_pedido_deletado():
    #Dados de Entrada
    orderId = 41511

    #Resultados esperados
    status_code_esperado = 404

    #Executa
    resultado_obtido = requests.get(
        url=url + 'store/order/' + str(orderId),
        headers=headers
    )

    #Valida
    assert resultado_obtido.status_code == status_code_esperado