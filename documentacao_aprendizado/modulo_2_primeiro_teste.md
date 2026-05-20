# Módulo 2: Meu Primeiro Teste Funcional e Estrutura do Playwright

Bem-vindo ao Módulo 2! Agora que seu ambiente virtual está configurado e as bibliotecas estão instaladas, vamos entender o motor por trás do Playwright e escrever nosso primeiro script de teste funcional automatizado.

---

## 📖 1. Explicação Teórica: A Arquitetura do Playwright

Para automatizar com excelência, você precisa entender o que acontece sob o capô. Diferente de ferramentas legadas (como o Selenium Webdriver, que usa protocolo HTTP via JSON Wire Protocol), o Playwright se conecta diretamente ao navegador usando a tecnologia de **WebSockets**. Isso o torna extremamente rápido, resiliente a *flakiness* (testes instáveis) e capaz de interceptar tráfego de rede nativamente.

No Playwright, a hierarquia de controle do navegador segue três conceitos essenciais:

```
  ┌────────────────────────────────────────────────────────┐
  │                        BROWSER                         │
  │  (Instância física do navegador - Chromium/Firefox/etc) │
  │                           │                            │
  │            ┌──────────────┴──────────────┐             │
  │            ▼                             ▼             │
  │     BROWSER CONTEXT               BROWSER CONTEXT      │
  │  (Sessão isolada/anônima)      (Sessão isolada/anônima)│
  │            │                             │             │
  │      ┌─────┴─────┐                 ┌─────┴─────┐       │
  │      ▼           ▼                 ▼           ▼       │
  │    PAGE        PAGE              PAGE        PAGE      │
  │   (Aba 1)     (Aba 2)           (Aba 1)     (Aba 2)    │
  └────────────────────────────────────────────────────────┘
```

1. **Browser (Navegador):** É o processo real do navegador (ex: Chromium, Firefox ou WebKit) rodando na máquina. Ele é pesado de inicializar, por isso é criado apenas uma vez no ciclo de testes.
2. **Browser Context (Contexto):** É uma sessão altamente isolada dentro do Browser, agindo como uma aba anônima. Cada teste ganha seu próprio `BrowserContext`, o que significa que cookies, localStorage e cache são 100% isolados entre os testes. Isso possibilita rodar testes em paralelo sem que um interfira na sessão do outro.
3. **Page (Página):** É a aba ou janela aberta dentro de um Contexto. É com a `Page` que interagimos diretamente: navegamos para URLs, clicamos em botões, preenchemos inputs e validamos elementos.

---

## 🛠️ 2. Estrutura de Arquivos Recomendada

Para manter o seu repositório profissional e escalável, usaremos a seguinte estrutura:

```text
jornada-playwright-python/
│
├── documentacao_aprendizado/
│   ├── comandos_iniciais_e_instalacoes.md
│   └── modulo_2_primeiro_teste.md
│
├── tests/                      <-- Pasta onde colocaremos todos os testes
│   ├── __init__.py             <-- Indica ao Python que é um pacote
│   └── test_todo_app.py        <-- Nosso primeiro arquivo de teste
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 💻 3. Passo a Passo Prático

### Passo 3.1: Criar a pasta de testes
Crie a pasta `tests` no diretório raiz do seu projeto e crie um arquivo chamado `test_todo_app.py` dentro dela.

### Passo 3.2: O código do teste
Copie e cole o código abaixo no arquivo `tests/test_todo_app.py`. Ele utiliza o site oficial de demonstração do Playwright (**TodoMVC**), focado em simular interações de listas de tarefas.

```python
import pytest
from playwright.sync_api import Page, expect

def test_deve_adicionar_uma_nova_tarefa(page: Page):
    # 1. Navegar até o site TodoMVC
    page.goto("https://demo.playwright.dev/todomvc/")

    # 2. Localizar o input de nova tarefa
    # Usamos localizadores semânticos (ex: pelo placeholder do input)
    campo_tarefa = page.get_by_placeholder("What needs to be done?")

    # 3. Interagir com o elemento (digitar a tarefa e pressionar Enter)
    campo_tarefa.fill("Aprender Playwright com Python")
    campo_tarefa.press("Enter")

    # 4. Validar se a tarefa foi realmente adicionada na lista
    # O localizador get_by_test_id busca pelo atributo data-testid no HTML
    item_tarefa = page.get_by_test_id("todo-title")
    
    # Assert do Playwright com asserções inteligentes (auto-wait embutido)
    expect(item_tarefa).to_have_text("Aprender Playwright com Python")
```

### Passo 3.3: Executando o teste

1. Com o seu ambiente virtual ativado no terminal, execute o Pytest com os seguintes parâmetros:
   ```bash
   pytest -v --headed
   ```
   * **`-v` (verbose):** Detalha no terminal quais testes passaram ou falharam.
   * **`--headed`:** Abre a interface gráfica do navegador. Por padrão, o Playwright roda em modo *headless* (sem interface visual), o que é ótimo para Integração Contínua (CI), mas ruim para depuração local.

---

## 🏆 4. Desafio Técnico

Agora é sua vez de colocar a mão na massa e praticar! Você deve modificar ou adicionar um novo teste no mesmo arquivo para validar a seguinte regra de negócio:

**Cenário:** Concluir uma tarefa na lista.
1. Adicione uma tarefa qualquer (ex: "Estudar Pytest").
2. Localize o checkbox redondo ao lado esquerdo da tarefa adicionada.
   * *Dica do Mentor:* Use o localizador `page.get_by_role("checkbox")` ou inspecione o elemento para encontrar o checkbox.
3. Marque o checkbox usando o método `.check()`.
4. Valide se o item da lista recebeu a classe CSS correspondente a concluído (`completed`).
   * *Dica do Mentor:* Use a asserção `expect(page.locator("li.completed")).to_be_visible()` ou `expect(page.get_by_test_id("todo-item")).to_have_class(["completed"])`.

---

## 📝 5. Atualização do README.md

Adicione a seguinte seção no final do seu arquivo `README.md` para destacar o progresso do seu aprendizado:

```markdown
## 📂 Progresso do Portfólio

- [x] **Módulo 1:** Configuração de Ambiente (Python, Virtualenv, Playwright e Pytest).
- [/] **Módulo 2:** Primeiro Teste Funcional (TodoMVC E2E) e Arquitetura do Playwright.
```

---

## 🐙 6. Boas Práticas de Git (Conventional Commits)

Ao final do exercício, quando concluir o desafio e testar localmente, faça o commit do seu progresso utilizando mensagens claras e semânticas. 

Exemplos de commits sugeridos para esta etapa:
1. `feat: adiciona primeiro teste funcional do TodoMVC`
2. `docs: adiciona guia de aprendizado do modulo 2`
