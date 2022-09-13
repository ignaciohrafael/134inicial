# Configure
# Biblioteca / Imports
import time

import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Dados de Entrada
url = 'https://www.blazedemo.com'
# origem = 'São Paolo'
# destino = 'New York'
lista_de_valores = [
    ('Paris', 'New York'),
    ('Philadelphia', 'New York'),
    ('Boston', 'New York')
]
primeiro_nome = 'Juca'
bandeira = 'American Express'
lembrar_de_mim = True

# Resultados Esperados
#titulos_passagens_esperado = 'Flights from São Paolo to New York:'
mensagem_agradecimento_esperada = 'Thank you for your purchase today!'
preco_passagem_esperado = '555 USD'

# Executa
class Testes:
    # Início
    def setup_method(self):
        # instanciar a biblioteca / motor / engine
        # informar onde esta o WebDriver
        self.driver = webdriver.Chrome(
            'C:\\Users\\RafaelPx\\PycharmProjects\\134inicial\\vendors\\drivers\\chromedriver105.exe'
        )

    # Fim
    def teardown_method(self):
        # destruir o objeto da bilbioteca utilizado
        self.driver.quit()

    # Meio
    @pytest.mark.parametrize('origem,destino', lista_de_valores)
    def test_comprar_passagem(self, origem, destino):
        # E2E / Ent to End / ponta a ponta
        # Pagina Inicial (Home)
        # Executa / Valida
        # abrir o browser no endereço
        self.driver.get(url)
        # clicar na lista de cidades de origem
        lista = self.driver.find_element(By.NAME, 'fromPort')
        lista.click()
        # selecionar a cidade de origem desejada
        lista.find_element(By.XPATH, f"//option[contains(text(),'{origem}')]").click()
        # clicar na lista de cidades de destino
        lista = self.driver.find_element(By.NAME, 'toPort')
        lista.click()
        lista.find_element(By.XPATH, f"//option[contains(text(),'{destino}')]").click()
        # clicar no botão de procurar voos
        self.driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
        # Pagina Lista de Passagens
        # Executa / Valida
        assert self.driver.find_element(By.TAG_NAME, "h3").text == f'Flights from {origem} to {destino}:'
        # Pagina de Compra
        # Executa / Valida
        # Limpar o campo de nome para evitar problemas ao digitar
        #self.driver.find_element(By.ID, "inputName").clear()
        # Preenche o nome do comprador
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn").click()
        self.driver.find_element(By.ID, "inputName").send_keys(primeiro_nome)

        # Seleciona a bandeira do cartão
        lista = self.driver.find_element(By.ID, 'cardType')
        lista.click()
        lista.find_element(By.XPATH, f"//option[contains(text(),'{bandeira}')]").click()

        # Marca o checkbox para ser lembrado
        self.driver.find_element(By.ID, 'rememberMe').click()

        # Aperta o botão Purchase flight
        self.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()


        # Pagina de Obrigado
        # Valida
        assert self.driver.find_element(By.TAG_NAME, 'h1').text == mensagem_agradecimento_esperada
        assert self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(3) > td:nth-child(2)').text == preco_passagem_esperado
        time.sleep(2)