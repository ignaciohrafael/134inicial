Feature: Testar a compra de uma passagem

  Scenario: Comprar uma passagem aérea
    Given que eu seleciono a origem "Paris" e destino "New York"
    When eu seleciono o primeiro voo e preencho os dados do passageiro
    Then a página de confirmação deve ser exibida
