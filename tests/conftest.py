# pyrefly: ignore [missing-import]
import pytest
# pyrefly: ignore [missing-import]
from playwright.sync_api import Page

@pytest.fixture
def login_saucedemo(page: Page) -> Page:
    """Fixture para realizar login automático no SauceDemo e retornar a página logada."""
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    
    # O yield entrega a página pronta para o teste.
    yield page


# ==============================================================================
# 🏆 DESAFIO TÉCNICO - MÓDULO 4
# ------------------------------------------------------------------------------
# Objetivo: Criar uma fixture para o site TodoMVC.
#
# Dicas do Mentor:
# 1. Crie uma fixture com o decorador `@pytest.fixture` chamada `todomvc_page`.
# 2. Ela deve receber a fixture nativa `page` do Playwright como argumento.
# 3. Use `page.goto("https://demo.playwright.dev/todomvc/")` para abrir o site.
# 4. Use `yield page` para passar a página inicial do site pronta para os testes.
# ==============================================================================

# ESCREVA SEU CÓDIGO DO DESAFIO AQUI EMBAIXO:

@pytest.fixture
def todomvc_page(page: Page) -> Page:
    page.goto("https://demo.playwright.dev/todomvc/")
    yield page