# Módulo 3: Playwright Codegen e a Arte da Refatoração

Bem-vindo ao Módulo 3! Parabéns por concluir o Módulo 2 com maestria. Sua solução do desafio usando o localizador de checkbox e a asserção `to_have_class` ficou excelente e seguiu perfeitamente as melhores práticas.

Hoje vamos falar de uma ferramenta fantástica e de extrema produtividade, mas que exige **cuidado e maturidade profissional**: o **Playwright Codegen**.

---

## 📖 1. Explicação Teórica: O que é o Codegen e por que devemos refatorá-lo?

O **Playwright Codegen** é um gerador de código baseado em gravação. Ao rodar o comando, ele abre uma janela dupla:
1. O navegador real onde você interage com o site.
2. O **Playwright Inspector**, que grava suas ações em tempo real e as traduz para código (em Python, JavaScript, Java ou C#).

### A Armadilha do Codegen
Muitos profissionais iniciantes caem no erro de "gravar o teste, copiar o código gerado, colar no projeto e achar que o trabalho está pronto". **Não faça isso!** O código gerado por ferramentas de gravação costuma ter vários problemas:
* **Seletores Frágeis:** Ele pode gerar caminhos absolutos (como XPath longos ou seletores CSS acoplados à estrutura visual, ex: `div > div > span > button`), que quebram facilmente ao menor ajuste de design.
* **Falta de Asserções Reais:** O Codegen foca em gravar cliques e preenchimentos, mas testes robustos precisam de asserções (`expect`) personalizadas para garantir que a regra de negócio foi atendida.
* **Código Poluído:** Ele costuma gravar movimentos e cliques redundantes.

> **💡 Regra de Ouro do QA Sênior:** Use o Codegen para descobrir seletores difíceis e entender fluxos rapidamente, mas **sempre refatore o código** para torná-lo limpo, legível e resiliente a mudanças.

---

## 🛠️ 2. Estrutura de Arquivos

Para este módulo, adicionaremos um novo arquivo focado em testar um fluxo de e-commerce real no clássico site de testes **SauceDemo**:

```text
jornada-playwright-python/
│
├── documentacao_aprendizado/
│   ├── comandos_iniciais_e_instalacoes.md
│   ├── modulo_2_primeiro_teste.md
│   └── modulo_3_codegen_refatoracao.md   <-- Este guia
│
├── tests/
│   ├── __init__.py
│   ├── test_todo_app.py
│   └── test_saucedemo.py                  <-- Novo arquivo do desafio
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 💻 3. Passo a Passo Prático: Rodando o Codegen

### Passo 3.1: Iniciando o Codegen
Certifique-se de que seu ambiente virtual (`venv`) está ativo e execute no seu terminal:

```bash
playwright codegen https://www.saucedemo.com/
```

Isso abrirá o navegador do Playwright e a janela do inspetor.

### Passo 3.2: O que o Codegen costuma gerar
Ao interagir com a tela de login preenchendo as credenciais de teste (`standard_user` e `secret_sauce`), o Codegen gravará algo assim:

```python
# CÓDIGO BRUTO GERADO PELO CODEGEN (Exemplo)
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

### Passo 3.3: Como refatorar de forma profissional
Para integrar esse fluxo ao nosso framework (Pytest) de forma limpa, removemos a inicialização manual do navegador (`sync_playwright`, `browser.close`, etc.) pois o Pytest gerencia isso via a fixture `page`.

Além disso, limpamos os cliques redundantes e inserimos asserções inteligentes:

```python
# CÓDIGO REFATORADO E PROFISSIONAL (Pytest style)
from playwright.sync_api import Page, expect

def test_login_com_sucesso(page: Page):
    # 1. Navegar
    page.goto("https://www.saucedemo.com/")

    # 2. Preencher credenciais (usando seletores de test-id nativos do site)
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    
    # 3. Clicar no botão de login
    page.get_by_role("button", name="Login").click()

    # 4. Asserção de Sucesso: Garantir que fomos para a página de produtos
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    # Verificar se o título da página de produtos está visível
    titulo_pagina = page.locator(".title")
    expect(titulo_pagina).to_have_text("Products")
```

---

## 🏆 4. Desafio Técnico: Módulo 3

Sua missão é testar o fluxo de **adicionar um produto ao carrinho** no **SauceDemo**.

### O que fazer:
1. Abra o terminal e use o `playwright codegen https://www.saucedemo.com/` para gravar o fluxo de:
   * Fazer login com o usuário `standard_user` e senha `secret_sauce`.
   * Adicionar o primeiro produto (**Sauce Labs Backpack**) ao carrinho de compras (clicando no botão "Add to cart").
   * Clicar no ícone do carrinho de compras (canto superior direito).
   * Validar se o produto está listado na página do carrinho.
2. Copie o código gerado pelo Codegen.
3. Crie o arquivo `tests/test_saucedemo.py` e cole o código.
4. **Refatore-o completamente**:
   * Adapte o código para o padrão do Pytest (usando a fixture `page` na assinatura da função e removendo o boilerplate de inicialização do browser).
   * Use localizadores semânticos legíveis e profissionais (ex: `page.get_by_role`, `page.get_by_text` ou seletores amigáveis como `.inventory_item_name`).
   * Adicione pelo menos **duas asserções robustas** com `expect`:
     * Uma garantindo que o ícone do carrinho exibe a quantidade corretora (ex: `"1"` item no badge).
     * Outra garantindo que o nome do item no carrinho de fato condiz com o produto adicionado ("Sauce Labs Backpack").

---

## 📝 5. Atualização do README.md

Atualize a seção de progresso no seu `README.md`:

```markdown
- [x] **Módulo 2:** Primeiro Teste Funcional (TodoMVC E2E) e Arquitetura do Playwright.
- [/] **Módulo 3:** Utilizando o Playwright Codegen para inspecionar elementos e refatoração de código.
```

---

## 🐙 6. Boas Práticas de Git (Conventional Commits)

Comite suas mudanças de forma limpa:
1. `feat: adiciona teste de fluxo de compra no saucedemo usando codegen refatorado`
2. `docs: adiciona guia de aprendizado do modulo 3`
