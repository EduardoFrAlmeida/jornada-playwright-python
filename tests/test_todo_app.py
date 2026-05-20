# pyrefly: ignore [missing-import]
import pytest
# pyrefly: ignore [missing-import]
from playwright.sync_api import Page, expect

def test_deve_adicionar_uma_nova_tarefa(page: Page):
    # 1. Navegar até o site TodoMVC
    page.goto("https://demo.playwright.dev/todomvc/")

    # 2. Localizar o input de nova tarefa pelo placeholder
    campo_tarefa = page.get_by_placeholder("What needs to be done?")

    # 3. Interagir com o elemento (digitar a tarefa e pressionar Enter)
    campo_tarefa.fill("Aprender Playwright com Python")
    campo_tarefa.press("Enter")

    # 4. Validar se a tarefa foi realmente adicionada na lista
    item_tarefa = page.get_by_test_id("todo-title")
    
    # Assert do Playwright com asserções inteligentes (auto-wait)
    expect(item_tarefa).to_have_text("Aprender Playwright com Python")


# ==============================================================================
# 🏆 DESAFIO TÉCNICO - MÓDULO 2
# ------------------------------------------------------------------------------
# Objetivo: Criar um teste para validar a conclusão de uma tarefa.
#
# Dicas do Mentor:
# 1. Crie uma função de teste chamada: `test_deve_marcar_tarefa_como_concluida(page: Page)`
# 2. Navegue até o site TodoMVC.
# 3. Adicione uma nova tarefa (ex: "Estudar Pytest").
# 4. Localize o checkbox redondo correspondente e marque-o usando o método .check().
# 5. Faça a validação (assert) de que a tarefa está com o estilo concluído.
# ==============================================================================

# ESCREVA SEU CÓDIGO DO DESAFIO AQUI EMBAIXO:

