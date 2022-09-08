# Configure
# Biblioteca / Imports

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Dados de Entrada
url = 'https://www.blazedemo.com'
origem = 'São Paolo'
destino = 'New York'
primeiro_nome = 'Juca'
bandeira = 'American Express'
lembrar_de_mim = True

# Resultados Esperados
titulos_passagens_esperado = 'Flights from São Paolo to New York:'
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
    def test_comprar_passagem(self):
        # E2E / Ent to End / ponta a ponta
        # Pagina Inicial (Home)
        # Executa / Valida
        # abrir o browser no endereço
        self.driver.get(url)
        # clicar na lista de cidades de origem
        lista = self.driver.find_element(By.NAME, 'fromPort')
        lista.click()
        # selecionar a cidade de origem desejada
        lista.find_element(By.XPATH, "//option[contains(text(),'São Paolo')]").click()
        # clicar na lista de cidades de destino
        lista = self.driver.find_element(By.NAME, 'toPort')
        lista.click()
        lista.find_element(By.XPATH, "//option[contains(text(),'New York')]").click()
        # clicar no botão de procurar voos
        self.driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
        # Pagina Lista de Passagens
        # Executa / Valida

        # Pagina de Compra
        # Executa / Valida

        # Pagina de Obrigado
        # Executa

        # Valida