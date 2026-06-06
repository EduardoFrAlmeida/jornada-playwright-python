# pyrefly: ignore [missing-import]
from playwright.sync_api import Page, expect

# Passo 1: Como iniciamos um teste no Pytest?
# Toda função de teste deve obrigatoriamente começar com o nome "test_"
# Usamos a fixture "page" na assinatura para abrir o navegador automaticamente.

def test_desafio_dia_01(page: Page):
    # ==========================================
    # 🎯 PARTE 1: NAVEGAÇÃO E AÇÃO
    # ==========================================
    
    # 1. Navegue até o site do TodoMVC:
    # (Dica: Use page.goto("URL-DO-SITE"))
    page.goto("https://demo.playwright.dev/todomvc/")
    
    # 2. Localize o campo de texto pelo placeholder "What needs to be done?"
    # (Dica: Use page.get_by_placeholder("What needs to be done?"))
    campo_de_tarefas = page.get_by_placeholder("What needs to be done?")
    
    # 3. Digite a tarefa "Estudar Playwright" e pressione a tecla "Enter":
    # (Dica: Use .fill() para digitar e .press("Enter") para enviar)
    campo_de_tarefas.fill("Estudar Playwright")
    campo_de_tarefas.press("Enter")
    
    # ==========================================
    # 🎯 PARTE 2: A BUSCA DA TAREFA (O Desafio!)
    # ==========================================
    
    # Agora que a tarefa foi adicionada na lista, sua missão é localizá-la
    # de 3 formas diferentes para treinar seus olhos de QA:
    
    # --- MÉTODO A: Localizar pelo TEXTO exato na tela ---
    # Escreva uma variável chamada 'localizador_por_texto' que encontre a palavra "Estudar Playwright".
    # (Dica: Use page.get_by_text("Estudar Playwright"))
    
    localizador_por_texto = page.get_by_text("Estudar Playwright")
    
    # --- MÉTODO B: Localizar usando a classe CSS do elemento ---
    # Ao inspecionar a tarefa adicionada no HTML, você verá que o texto fica dentro de um elemento
    # com a classe CSS chamada '.todo-list li label' ou simplesmente '[data-testid="todo-title"]'.
    # Escreva uma variável chamada 'localizador_por_css' usando o método page.locator()
    # (Dica: Use page.locator("[data-testid='todo-title']"))
    
    localizador_por_css = page.locator("[data-testid='todo-title']")
    
    # --- MÉTODO C: Localizar pelo seu papel semântico (Role) ---
    # Elementos visuais na tela possuem "papéis" no HTML (como botões, caixas de diálogo, listas).
    # O item da tarefa adicionada pode ser buscado por seu papel semântico.
    # Vamos usar o 'get_by_label' para buscar o checkbox da tarefa ou o próprio item de lista 'listitem'.
    # Escreva uma variável chamada 'localizador_por_role' que busque pelo papel de lista.
    # (Dica: Use page.get_by_role("listitem").filter(has_text="Estudar Playwright"))
    
    localizador_por_role = page.get_by_role("listitem").filter(has_text="Estudar Playwright")

    
    # ==========================================
    # 🎯 PARTE 3: AS VALIDAÇÕES (Asserts)
    # ==========================================
    
    # Para provar que os 3 caminhos diferentes encontraram o mesmo botão/texto na tela,
    # crie três validações 'expect' para garantir que os três localizadores estão visíveis!
    # Exemplo: expect(seu_localizador).to_be_visible()
    
    expect(localizador_por_texto).to_be_visible()
    expect(localizador_por_css).to_be_visible()
    expect(localizador_por_role).to_be_visible()
    
