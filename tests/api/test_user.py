# Done: 1 - criar um teste que adicione um usuário
# Done: 2 - realizar o login e extrair o token da resposta
# ToDo: 3 - criar uma venda de um pet para um usuário
# ToDo: 4 - Consultar os dados do pet que foi vendido
import requests

url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}
token = ''

def test_incluir_usuario():
    #Configura
    #Dados de Entrada
    #Virão do arquivo usuario1.json

    #Resultados esperados
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '8369435'

    #Execute
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\RafaelPx\\PycharmProjects\\134inicial\\vendors\\json\\usuario1.json')
    )

    #Check
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == codigo_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert corpo_do_resultado_obtido['message'] == mensagem_esperada


def test_login():
    #Configure
    #Dados de entrada
    username = 'juca'
    password = 'bala'

    #Resultados esperados
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'logged in user session:'

    #Execute
    resultado_obtido = requests.get(
        url=f'{url}/login?username={username}&password={password}',
        headers=headers,
    )

    #Check
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == codigo_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert mensagem_esperada.find(corpo_do_resultado_obtido['message'])

    #Extrai
    mensagem_extraida = corpo_do_resultado_obtido.get('message')
    print(f'O token = {mensagem_extraida}')
    token = mensagem_extraida[23:]
    print(f'O token = {token}')