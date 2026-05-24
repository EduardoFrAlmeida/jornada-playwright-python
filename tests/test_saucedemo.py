# pyrefly: ignore [missing-import]
from playwright.sync_api import Page, expect

def test_login_com_sucesso(page: Page):
    # 1. Navegar para a página inicial
    page.goto("https://www.saucedemo.com/")

    # 2. Preencher o formulário de login usando localizadores semânticos
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    
    # 3. Clicar no botão de login
    page.get_by_role("button", name="Login").click()

    # 4. Asserções profissionais
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    titulo_pagina = page.locator(".title")
    expect(titulo_pagina).to_have_text("Products")


# ==============================================================================
# 🏆 DESAFIO TÉCNICO - MÓDULO 3
# ------------------------------------------------------------------------------
# Objetivo: Testar o fluxo de adicionar um produto ao carrinho.
#
# Instruções:
# 1. Crie uma função de teste chamada: `test_deve_adicionar_produto_ao_carrinho(page: Page)`
# 2. Use o comando `playwright codegen https://www.saucedemo.com/` no terminal para 
#    interagir e gravar o fluxo.
# 3. Insira o código gravado aqui, mas REFATORE-O para o padrão do Pytest.
# 4. Use localizadores robustos e adicione validações com `expect`.
# ==============================================================================

# ESCREVA SEU CÓDIGO DO DESAFIO AQUI EMBAIXO:

def test_deve_adicionar_produto_ao_carrinho(page: Page) -> None:
    # 1. Navegar para a página inicial
    page.goto("https://www.saucedemo.com/")

    # 2. Fazer login usando localizadores semânticos mais limpos
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    # 3. Adicionar o produto "Sauce Labs Backpack" ao carrinho
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()

    # 4. Asserção 1: Validar que o badge do carrinho exibe "1" item adicionado
    # O seletor '.shopping_cart_badge' é a classe CSS do número vermelho do carrinho
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    # 5. Ir para o carrinho
    page.locator("[data-test=\"shopping-cart-link\"]").click()

    # 6. Asserção 2: Validar que o produto correto está listado na página do carrinho
    # '.inventory_item_name' é a classe do título do item dentro do carrinho
    expect(page.locator(".inventory_item_name")).to_have_text("Sauce Labs Backpack")

