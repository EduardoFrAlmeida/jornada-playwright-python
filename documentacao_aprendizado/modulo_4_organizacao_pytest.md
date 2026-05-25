# Módulo 4: Organizando Testes com Pytest (Fixtures, Conftest, Paralelismo e Relatórios)

Bem-vindo ao Módulo 4! Você está avançando rapidamente e já tem testes funcionais de alto nível. Agora, é hora de dar um salto de maturidade arquitetural. Vamos transformar um conjunto de scripts de teste individuais em um **framework de testes robusto e profissional**, pronto para rodar em esteiras de CI/CD.

---

## 📖 1. Explicação Teórica: O Poder do Pytest

O Pytest não é apenas um executor de testes; ele é um motor extensível por meio de **Fixtures** e plugins.

### O que são Fixtures?
Pense em Fixtures como auxiliares de preparação de ambiente (*Setup*) e desmontagem (*Teardown*). Elas preparam o terreno para o teste rodar (ex: abrir o banco de dados, fazer login em um site) e depois limpam a sujeira (ex: fechar conexões, limpar cookies). 

A fixture nativa `page` do Playwright que você já usou é um exemplo de fixture gerenciada.

### O Arquivo `conftest.py`
O `conftest.py` é um arquivo especial do Pytest. Ele funciona como uma central de compartilhamento. Qualquer fixture declarada dentro dele fica automaticamente disponível para **todos** os arquivos de testes do diretório, sem a necessidade de importação explícita!

### Execução Paralela (`pytest-xdist`)
Testes de UI costumam ser lentos. Para resolver isso, usamos o paralelismo. O plugin `pytest-xdist` divide seus testes entre os múltiplos núcleos (cores) do seu processador. Como o Playwright usa o conceito de `BrowserContext` isolado para cada teste, você pode rodar 4, 8 ou mais testes de UI ao mesmo tempo sem que um interfira na sessão ou cookies do outro!

### Relatórios Visuais (`pytest-html`)
Gerentes e desenvolvedores adoram dados. O plugin `pytest-html` gera relatórios interativos em HTML com gráficos mostrando quais testes passaram, falharam ou foram pulados, facilitando a depuração.

---

## 🛠️ 2. Nova Estrutura de Arquivos

```text
jornada-playwright-python/
│
├── documentacao_aprendizado/
│   ├── comandos_iniciais_e_instalacoes.md
│   ├── modulo_2_primeiro_teste.md
│   ├── modulo_3_codegen_refatoracao.md
│   └── modulo_4_organizacao_pytest.md   <-- Este guia
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py                      <-- [NOVO] Centralizador de Fixtures
│   ├── test_todo_app.py                 <-- Será refatorado no desafio
│   └── test_saucedemo.py                <-- Refatorado para usar Fixture de Login
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 💻 3. Passo a Passo Prático

### Passo 3.1: Instalar novas dependências do ecossistema
Ative seu ambiente virtual (`venv`) no terminal do Windows e instale os plugins de paralelismo e relatórios:

```bash
pip install pytest-xdist pytest-html
```

Depois, atualize seu `requirements.txt`:
```bash
pip freeze > requirements.txt
```

### Passo 3.2: Criar o arquivo `tests/conftest.py`
Crie o arquivo `tests/conftest.py` e escreva uma fixture customizada chamada `login_saucedemo`. Esta fixture recebe a fixture nativa `page`, executa o fluxo de login uma única vez e retorna a página já logada.

```python
import pytest
from playwright.sync_api import Page

@pytest.fixture
def login_saucedemo(page: Page) -> Page:
    """Fixture para realizar login automático no SauceDemo e retornar a página logada."""
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    
    # O yield entrega a página pronta para o teste.
    # Se precisássemos fazer um 'teardown' (ex: logout), faríamos depois do yield.
    yield page
```

### Passo 3.3: Refatorar o arquivo `tests/test_saucedemo.py`
Agora, substituímos o uso da fixture nativa `page` pela nossa fixture customizada `login_saucedemo` na assinatura dos testes do SauceDemo. Veja como o código fica incrivelmente limpo e sem repetição:

```python
from playwright.sync_api import Page, expect

def test_login_com_sucesso(login_saucedemo: Page):
    # O teste já começa logado! Basta validar se estamos na URL correta.
    page = login_saucedemo
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")

def test_deve_adicionar_produto_ao_carrinho(login_saucedemo: Page):
    page = login_saucedemo
    # O teste já começa logado! Pulamos direto para a ação de compra.
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(page.locator(".inventory_item_name")).to_have_text("Sauce Labs Backpack")
```

---

## 🏆 4. Desafio Técnico: Módulo 4

Sua missão de hoje é aplicar a mesma lógica de reutilização e organização no TodoMVC e rodar tudo em paralelo.

### O que fazer:
1. No arquivo [conftest.py](file:///c:/Users/eduar/Downloads/jornada-playwright-python/jornada-playwright-python/tests/conftest.py), crie uma nova fixture chamada `todomvc_page(page: Page)`.
   * Ela deve navegar automaticamente para `https://demo.playwright.dev/todomvc/`.
   * Ela deve usar o `yield page` para entregar a página na URL inicial do TodoMVC para o teste.
2. Refatore o arquivo [test_todo_app.py](file:///c:/Users/eduar/Downloads/jornada-playwright-python/jornada-playwright-python/tests/test_todo_app.py) para utilizar a fixture `todomvc_page` em vez de `page`.
   * Remova a linha `page.goto("https://demo.playwright.dev/todomvc/")` de ambos os testes (`test_deve_adicionar_uma_nova_tarefa` e `test_deve_marcar_tarefa_como_concluida`).
3. **Execução Paralela:** Rode todos os testes do projeto simultaneamente usando o paralelismo do `pytest-xdist`. Use o seguinte comando no terminal:
   ```bash
   pytest -n auto
   ```
   *(Note como o Pytest distribui os testes nos processadores e os roda de forma muito mais veloz em segundo plano!)*
4. **Geração de Relatório:** Gere um relatório visual interativo em HTML executando:
   ```bash
   pytest --html=reports/relatorio.html --self-contained-html
   ```
   *(Abra o arquivo HTML gerado na pasta `reports/` no seu navegador para ver o resultado incrível).*

---

## 📝 5. Atualização do README.md

Atualize o arquivo `README.md` marcando o progresso:

```markdown
- [x] **Módulo 3:** Utilizando o Playwright Codegen para inspecionar elementos e refatoração de código.
- [/] **Módulo 4:** Organizando testes com Pytest (fixtures, asserts, execução paralela e relatórios).
```

E atualize a seção de execução de testes explicando como rodar em paralelo e gerar relatórios:

```markdown
## 🧪 Como rodar os testes

### Executar todos os testes:
```bash
pytest -v --headed
```

### Executar em paralelo (Modo Headless super rápido):
```bash
pytest -n auto
```

### Gerar Relatório HTML de Execução:
```bash
pytest --html=reports/relatorio.html --self-contained-html
```
```

---

## 🐙 6. Boas Práticas de Git (Conventional Commits)

Exemplos de commits sugeridos:
1. `feat: adiciona centralizador conftest e refatora testes para usar fixtures`
2. `chore: instala pacotes pytest-xdist e pytest-html para paralelismo e relatorios`
3. `docs: adiciona guia de aprendizado do modulo 4`
