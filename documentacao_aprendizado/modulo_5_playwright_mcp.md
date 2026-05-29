# Módulo 5: Integração Avançada e Automação Assistida por IA com Playwright MCP (Model Context Protocol)

Bem-vindo ao Módulo 5, o último e mais avançado módulo da nossa mentoria de QA! Parabéns por concluir o Módulo 4. O seu relatório HTML gerado e a execução em paralelo com o `pytest-xdist` mostram que você já dominou a base de uma arquitetura de testes profissional.

Hoje, vamos cruzar a fronteira tradicional do QA e entrar na era do **QA Agêntico (Agentic QA)**. Vamos aprender sobre o **Playwright MCP (Model Context Protocol)** e como as inteligências artificiais modernas interagem diretamente com navegadores para criar, executar e depurar testes.

---

## 📖 1. Explicação Teórica: O que é o Model Context Protocol (MCP)?

O **Model Context Protocol (MCP)** é um padrão aberto (desenvolvido originalmente pela Anthropic e adotado por plataformas líderes como o Antigravity, Claude Desktop e Cursor) que permite que Modelos de Linguagem (LLMs) se conectem de forma segura e padronizada a ferramentas locais ou APIs externas.

Antes do MCP, um modelo de IA vivia em uma "caixa isolada", limitada aos seus dados de treinamento. Com o MCP, a IA ganha "mãos e olhos" para interagir com o mundo real.

```
┌──────────────┐         MCP Protocol        ┌──────────────┐
│  AI Agent    │ ──────────────────────────> │ MCP Server   │
│ (Antigravity/│ <────────────────────────── │ (Playwright) │
│  Claude/etc) │     JSON-RPC over STDIO     └──────┬───────┘
└──────────────┘                                    │
                                                    ▼
                                            ┌──────────────┐
                                            │ Real Browser │
                                            │ (Playwright) │
                                            └──────────────┘
```

### O que é o Playwright MCP Server?
É um servidor local que expõe a API do Playwright diretamente para agentes de IA. Quando ativo, o agente de IA pode invocar ferramentas do tipo:
* `playwright_navigate`: Comanda o navegador para ir a uma URL.
* `playwright_click`: Clica em um seletor visual na tela.
* `playwright_fill`: Preenche um campo de texto.
* `playwright_screenshot`: Tira um print da tela atual para inspeção visual da IA.

### O Futuro do QA: Agentic QA e Self-Healing Tests
Como especialista em QA, entender o MCP te posiciona no topo do mercado. Os testes do futuro não serão apenas scripts estáticos. Teremos agentes de IA que:
1. **Criam testes sozinhos:** Navegam pela aplicação, compreendem as regras de negócio e escrevem os arquivos `.py` automaticamente.
2. **Auto-correção (Self-healing):** Se um desenvolvedor mudar o ID de um botão de `btn-login` para `submit-form`, a IA detectará a falha visualmente via MCP, corrigirá o código do teste e enviará um Pull Request sem intervenção humana.

---

## 🛠️ 2. Estrutura de Arquivos Final do Projeto

Ao final deste módulo, seu repositório estará completo e pronto para impressionar qualquer recrutador ou equipe de engenharia:

```text
jornada-playwright-python/
│
├── documentacao_aprendizado/
│   ├── comandos_iniciais_e_instalacoes.md
│   ├── modulo_2_primeiro_teste.md
│   ├── modulo_3_codegen_refatoracao.md
│   ├── modulo_4_organizacao_pytest.md
│   └── modulo_5_playwright_mcp.md         <-- Este guia
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_todo_app.py
│   └── test_saucedemo.py
│
├── mcp_config/                            <-- [NOVO] Configuração profissional de IA
│   └── claude_desktop_config.json         <-- Como habilitar a IA no seu PC
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 💻 3. Passo a Passo Prático: Configurando o Servidor Playwright MCP

Para mostrar no seu portfólio que seu projeto é "AI-Ready" (pronto para ser consumido por agentes de IA), vamos estruturar a configuração de integração do Playwright MCP.

### Passo 3.1: Como o servidor é iniciado
O servidor oficial do Playwright MCP é executado via Node.js utilizando o `npx`. Em uma máquina de desenvolvedor, ele é configurado no arquivo de configuração do agente (ex: Claude Desktop ou Cursor).

O comando de inicialização é:
```bash
npx -y @modelcontextprotocol/server-playwright
```

### Passo 3.2: Criando a pasta de configuração para IAs
Crie uma pasta chamada `mcp_config` na raiz do seu projeto e, dentro dela, um arquivo chamado `claude_desktop_config.json`. Esse arquivo servirá como documentação viva no seu repositório, ensinando como qualquer desenvolvedor (ou você mesmo) pode plugar uma IA de mercado para interagir com o seu projeto.

Adicione o seguinte conteúdo a ele:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-playwright"
      ],
      "env": {
        "PLAYWRIGHT_HEADLESS": "false"
      }
    }
  }
}
```

---

## 🏆 4. Desafio Técnico: Módulo 5 (O Toque de Mestre no Portfólio)

Como este é o último módulo e você já domina a automação de testes com Python e Playwright, faremos um desafio focado em **Integração Avançada** e na **Maturidade do Portfólio**.

### O que fazer:

1. **Crie a pasta e o arquivo de configuração de IA:**
   * Crie a pasta `mcp_config` no seu repositório.
   * Crie o arquivo `claude_desktop_config.json` com o conteúdo indicado no Passo 3.2.
2. **Atualização Geral de Portfólio:**
   * Seu repositório agora está completo. Para deixá-lo com cara de portfólio de engenheiro de QA sênior, atualize o `README.md` adicionando uma seção explicando que o repositório é **AI-Ready (Compatível com MCP)** e como rodar o servidor Playwright MCP. *(Eu preparei uma sugestão de README incrível para você, veja a resposta no chat!)*.
3. **Commit Final:**
   * Faça o commit final das alterações utilizando o Conventional Commits:
     ```bash
     git add .
     git commit -m "feat: adiciona configuracao de mcp e finaliza modulo 5"
     ```

---

## 📝 5. Atualização do README.md

Marque seu progresso como concluído no seu `README.md`:

```markdown
- [x] **Módulo 4:** Organizando testes com Pytest (fixtures, asserts, execução paralela e relatórios).
- [x] **Módulo 5:** Integração avançada e introdução ao Playwright MCP (Model Context Protocol).
```
