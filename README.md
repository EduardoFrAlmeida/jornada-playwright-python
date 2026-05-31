# 🎭 Jornada Playwright + Python + Pytest

Repositório estruturado para demonstrar o aprendizado prático e o domínio de técnicas modernas de Engenharia de QA e Automação de Testes End-to-End (E2E) utilizando a stack **Playwright**, **Python** e **Pytest**.

Este projeto serve como um portfólio de engenharia de testes, evoluindo de um setup inicial básico para conceitos avançados de design de código de testes, paralelização, relatórios interativos e **automação agêntica assistida por IA (Model Context Protocol - MCP)**.

---

## 🚀 Tecnologias Utilizadas
- **Linguagem:** [Python 3.10+](https://www.python.org/)
- **Core E2E:** [Playwright para Python](https://playwright.dev/python/) (arquitetura resiliente baseada em WebSockets com auto-wait)
- **Framework de Testes:** [Pytest](https://docs.pytest.org/) (fixtures avançadas e parametrização)
- **Execução Paralela:** [pytest-xdist](https://pypi.org/project/pytest-xdist/)
- **Visual Reporting:** [pytest-html](https://pypi.org/project/pytest-html/)
- **IA & Agentic QA:** [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

---

## ⚙️ Como executar este projeto localmente

### 1. Clonar o repositório
```bash
git clone https://github.com/EduardoFrAlmeida/jornada-playwright-python
cd jornada-playwright-python
```

### 2. Criar e ativar o ambiente virtual (Virtualenv)
* **Linux/macOS:**
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```
* **Windows (PowerShell):**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

### 3. Instalar dependências e navegadores do Playwright
```bash
pip install -r requirements.txt
playwright install
```

---

## 🧪 Executando a Suíte de Testes

O projeto contém testes estruturados para aplicações reais (TodoMVC e SauceDemo), utilizando fixtures no centralizador `conftest.py`.

### Modo Interativo (Headed - com interface gráfica)
```bash
pytest -v --headed
```

### Modo Paralelo (Headless - ultra rápido)
```bash
pytest -n auto
```

### Gerando Relatório Visual HTML
```bash
pytest --html=reports/relatorio.html --self-contained-html
```
*(O relatório gerado ficará disponível em `reports/relatorio.html` contendo gráficos e métricas de sucesso dos testes).*

---

## ⚙️ Integração Contínua (CI/CD) com GitHub Actions

Este repositório utiliza **GitHub Actions** para automação de testes contínua!

Toda vez que você enviar um código para a branch `main` ou abrir um `Pull Request`, uma máquina virtual Linux é criada automaticamente no servidor do GitHub para:
1. Clonar o projeto.
2. Instalar dependências de sistema e bibliotecas (`requirements.txt`).
3. Baixar navegadores headless do Playwright.
4. Executar os testes em paralelo (`pytest -n auto`).
5. Armazenar o relatório de testes (`pytest-html`) como artefato para download.

O arquivo de configuração do workflow está localizado em [.github/workflows/playwright.yml](file:///.github/workflows/playwright.yml).

---

## 🤖 Integração com IA: Playwright MCP (Model Context Protocol)

Este repositório é **AI-Ready (Compatível com MCP)**! Isso significa que agentes de inteligência artificial de última geração (como Claude Desktop, Cursor e Antigravity) podem rodar este projeto e interagir diretamente com o navegador usando comandos em linguagem natural.

### Como plugar um Agente de IA neste projeto:
1. Instale o Node.js na sua máquina.
2. Na pasta [mcp_config/claude_desktop_config.json](file:///c:/Users/eduar/Downloads/jornada-playwright-python/jornada-playwright-python/mcp_config/claude_desktop_config.json), você encontrará a estrutura pronta do servidor Playwright MCP.
3. Copie o conteúdo da configuração para a pasta de configuração de IAs do seu sistema:
   * **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
   * **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
4. Reinicie o cliente da IA. O agente passará a interagir de forma nativa e agêntica com o browser do seu computador!

---

## 📂 Progresso da Jornada (Módulos de Aprendizado)

- [x] **Módulo 1:** Configuração de Ambiente (Python, Virtualenv, Playwright e Pytest).
- [x] **Módulo 2:** Primeiro Teste Funcional (TodoMVC E2E) e Arquitetura do Playwright.
- [x] **Módulo 3:** Utilizando o Playwright Codegen para inspecionar elementos e refatoração de código.
- [x] **Módulo 4:** Organizando testes com Pytest (fixtures, asserts, execução paralela e relatórios).
- [x] **Módulo 5:** Integração avançada e introdução ao Playwright MCP (Model Context Protocol).