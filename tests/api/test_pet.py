# bibliotecas
import pytest
import requests
import json

from tests.utils.file_manager import ler_csv


# variaveis publicas
url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}


# definições das funções (defs)

def test_incluir_pet():
    #Configure
    #Dados de entrada provém do pet1.json

    #Resultados esperados
    status_code_esperado = 200
    pet_id_esperado = 4358369
    pet_nome_esperado = "Snoopy"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_tag_esperado = "vacinado"


    #Execute
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\RafaelPx\\PycharmProjects\\134inicial\\vendors\\json\\pet1.json')
    )

    #Check
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado

def test_consultar_pet():
    #Configure
    #Entradas
    pet_id = '4358369'

    #Resultados esperados
    # Resultados esperados
    status_code_esperado = 200
    pet_id_esperado = 4358369
    pet_nome_esperado = "Snoopy"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_tag_esperado = "vacinado"

    #Execute
    resultado_obtido = requests.get(
        url=url + '/' + pet_id,
        headers=headers
    )

    #Check
    corpo_do_resultado_obtido = resultado_obtido.json()
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado

def test_alterar_pet():
    # Configure
    # Dados de entrada do pet2.json

    # Resultados esperados
    '''
    status_code_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '4358369'
    '''
    status_code_esperado = 200
    pet_id_esperado = 4358369
    pet_nome_esperado = "Snoopy"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_tag_esperado = "vacinado"
    pet_status = "pending"

    # Execute
    resultado_obtido = requests.put(
        url=url,
        headers=headers,
        data=open('C:\\Users\\RafaelPx\\PycharmProjects\\134inicial\\vendors\\json\\pet2.json')
    )
    # Check
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)
    '''
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == str(status_code_esperado)
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert corpo_do_resultado_obtido['message'] == mensagem_esperada 
    '''
    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado
    assert corpo_do_resultado_obtido['status'] == pet_status


def test_excluir_pet():
    # Configure
    # Dados de entrada
    pet_id = '4358369'

    # Resultados esperados
    status_code_esperado = 200
    type_esperado = 'unknown'
    mensagem_esperada = '4358369'

    # Execute
    resultado_obtido = requests.delete(
        url=url + '/' + pet_id,
        headers=headers

    )

    # Check
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == status_code_esperado
    assert corpo_do_resultado_obtido['type'] == type_esperado
    assert corpo_do_resultado_obtido['message'] == mensagem_esperada


@pytest.mark.parametrize('pet_id,category_id,category_name,pet_name,tags_id,tags_name,status', ler_csv('C:\\Users\\RafaelPx\\PycharmProjects\\134inicial\\vendors\\csv\\massa_incluir_pet.csv'))
def test_incluir_pet_em_massa(pet_id, category_id, category_name, pet_name, tags_id, tags_name, status):
    #Configure
    #Dados de entrada
    #Os dados de entrada proveem do arquivo massa_incluir.pet.csv
    #Montagem do JSON dinâmico
    corpo_json = '{'
    corpo_json += f'  "id": {pet_id},'
    corpo_json += '  "category": {'
    corpo_json += f'    "id": {category_id},'
    corpo_json += f'    "name": "{category_name}"'
    corpo_json += '  },'
    corpo_json += f'  "name": "{pet_name}",'
    corpo_json += '  "photoUrls": ['
    corpo_json += '    "string"'
    corpo_json += '  ],'
    corpo_json += '  "tags": ['
    corpo_json += '    {'
    corpo_json += f'      "id": {tags_id},'
    corpo_json += f'      "name": "{tags_name}"'
    corpo_json += '    }'
    corpo_json += '  ],'
    corpo_json += f'  "status": "{status}"'
    corpo_json += '}'

    #Resultados Esperados
    #os dados de entrada também servirão como resultados esperados, visto que o retorno é um eco
    status_code_esperado = 200

    #Execute
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=corpo_json
    )
    #Check
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == int(pet_id)
    assert corpo_do_resultado_obtido['name'] == pet_name
    assert corpo_do_resultado_obtido['category']['name'] == category_name
    assert corpo_do_resultado_obtido['tags'][0]['name'] == tags_name