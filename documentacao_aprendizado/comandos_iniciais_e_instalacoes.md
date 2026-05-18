# Comandos Iniciais e Instalações de Ferramentas

No mundo Python, a primeira regra de ouro é: nunca instale dependências globalmente no seu sistema operacional.

Para isso, usamos Ambientes Virtuais (Virtualenvs). Um virtualenv é como uma "caixa isolada" onde instalaremos o Playwright e o Pytest.

Python: A linguagem de programação.
Pytest: O framework que vai organizar, executar nossos testes e fazer as validações (asserts).
Playwright: A biblioteca (motor) que vai abrir o navegador, clicar em botões, preencher campos, etc.
pytest-playwright: Um plugin oficial que une o Pytest e o Playwright, nos dando "atalhos" incríveis chamados fixtures.

## Passo 1: Criar o ambiente virtual
   ```bash
    python -m venv venv
   ```

## Passo 2: Ativar o ambiente virtual (Windows)
   ```bash
    .\venv\Scripts\activate
   ```

(Você saberá que funcionou se aparecer um (venv) verdinho no início da linha do seu terminal. Se der erro de permissão de script no PowerShell, você pode precisar rodar Set-ExecutionPolicy Unrestricted -Scope CurrentUser antes).

## Passo 3: Atualizar o gerenciador de pacotes do Python
   ```bash
    pip install --upgrade pip
   ```

## Passo 4: Instalar as bibliotecas
   ```bash
    pip install pytest pytest-playwright
   ```

## Passo 5: Baixar os navegadores do Playwright 
   ```bash
    playwright install
   ```

## Passo 6: Gerar arquivo Requirements.txt

Esse comando "congela" todas as bibliotecas instaladas e as salva no arquivo `requirements.txt`.

Como usar:
   ```bash
    pip freeze > requirements.txt
   ```
## Passo 7: Git e Conventional Commits

Padrão **Conventional Commits** (um padrão muito usado no mercado para deixar o histórico limpo e profissional):
```bash
git add .
git commit -m "chore: setup do ambiente virtual e bibliotecas base do playwright"
