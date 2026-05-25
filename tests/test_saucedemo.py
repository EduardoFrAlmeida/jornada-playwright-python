from playwright.sync_api import Page, expect

def test_login_com_sucesso(login_saucedemo: Page):
    # O teste já começa logado graças à nossa fixture customizada!
    page = login_saucedemo
    
    # Fazemos apenas as asserções de sucesso
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    titulo_pagina = page.locator(".title")
    expect(titulo_pagina).to_have_text("Products")


def test_deve_adicionar_produto_ao_carrinho(login_saucedemo: Page) -> None:
    # O teste já começa logado graças à nossa fixture customizada!
    page = login_saucedemo

    # 1. Adicionar o produto "Sauce Labs Backpack" ao carrinho
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()

    # 2. Asserção 1: Validar que o badge do carrinho exibe "1" item adicionado
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    # 3. Ir para o carrinho
    page.locator("[data-test=\"shopping-cart-link\"]").click()

    # 4. Asserção 2: Validar que o produto correto está listado na página do carrinho
    expect(page.locator(".inventory_item_name")).to_have_text("Sauce Labs Backpack")
