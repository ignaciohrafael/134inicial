import time
import selenium
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

# DADOS DE ENTRADA

url = 'https://www.blazedemo.com'
primeiro_nome = 'Juca'
bandeira = 'American Express'
lembrar_de_mim = True

# RESULTADOS ESPERADOS
#titulos_passagens_esperado = 'Flights from Paris to New York:'
mensagem_agradecimento_esperada = 'Thank you for your purchase today!'
preco_passagem_esperado = '555 USD'


# EXECUÇÃO

@given('que eu seleciono a origem "{origem}" e destino "{destino}"')
def access_select(self, origem, destino):
    self.driver = webdriver.Chrome()
    self.driver.get(url)
    lista = self.driver.find_element(By.NAME, 'fromPort')
    lista.click()
    lista.find_element(By.XPATH, f"//option[contains(text(),'{origem}')]").click()
    lista = self.driver.find_element(By.NAME, 'toPort')
    lista.click()
    lista.find_element(By.XPATH, f"//option[contains(text(),'{destino}')]").click()
    self.driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
    assert self.driver.find_element(By.TAG_NAME, "h3").text == f'Flights from {origem} to {destino}:'


@when('eu seleciono o primeiro voo e preencho os dados do passageiro')
def flight_info(self):
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


@then('a página de confirmação deve ser exibida')
def final(self):
    assert self.driver.find_element(By.TAG_NAME, 'h1').text == mensagem_agradecimento_esperada
    assert self.driver.find_element(By.CSS_SELECTOR,'tr:nth-child(3) > td:nth-child(2)').text == preco_passagem_esperado
    time.sleep(2)
    self.driver.quit()