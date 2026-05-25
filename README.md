# Jornada Playwright + Python

Repositório destinado ao aprendizado prático de automação de testes E2E (End-to-End) utilizando **Playwright**, **Python** e **Pytest**. 
Este projeto servirá como portfólio demonstrando a evolução de um setup básico até conceitos avançados de automação estruturada.

## 🚀 Tecnologias Utilizadas
- [Python](https://www.python.org/)
- [Playwright para Python](https://playwright.dev/python/)
- [Pytest](https://docs.pytest.org/)

## ⚙️ Como executar este projeto localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/EduardoFrAlmeida/jornada-playwright-python
   ```
2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Linux/Mac
   .\venv\Scripts\activate   # No Windows
  ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```

## 📂 Progresso do Portfólio

- [x] **Módulo 1:** Configuração de Ambiente (Python, Virtualenv, Playwright e Pytest).
- [x] **Módulo 2:** Primeiro Teste Funcional (TodoMVC E2E) e Arquitetura do Playwright.
- [x] **Módulo 3:** Utilizando o Playwright Codegen para inspecionar elementos e refatoração de código.
- [/] **Módulo 4:** Organizando testes com Pytest (fixtures, asserts, execução paralela e relatórios).
- [ ] **Módulo 5:** Integração avançada e introdução ao Playwright MCP (Model Context Protocol).

## 🧪 Como rodar os testes

### Executar todos os testes de forma tradicional (Headed):
```bash
pytest -v --headed
```

### Executar testes em paralelo (Headless - ultra rápido):
```bash
pytest -n auto
```

### Gerar relatório HTML de execução:
```bash
pytest --html=reports/relatorio.html --self-contained-html
```