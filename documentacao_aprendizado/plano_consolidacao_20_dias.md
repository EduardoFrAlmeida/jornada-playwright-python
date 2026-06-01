# 📅 Cronograma de Consolidação e Prática: 20 Dias de Automação com Playwright + Python

Bem-vindo ao seu plano de treinamento intensivo de 20 dias! Este cronograma foi desenhado por seu mentor para consolidar tudo o que aprendemos e levar suas habilidades de automação do nível básico ao profissional. 

Como combinado, **eu não vou te dar as respostas prontas**. Eu estarei aqui diariamente para tirar dúvidas, dar dicas conceituais, explicar erros no console e guiar sua linha de raciocínio. A sua missão é colocar a mão na massa!

---

## 🎯 Estrutura do Plano

O plano é dividido em **4 fases de 5 dias**. Cada dia tem um foco de estudo específico e um pequeno desafio prático.

* **Fase 1 (Dias 1-5):** Domínio de Localizadores e Asserções (Seletores Semânticos, CSS e Estados).
* **Fase 2 (Dias 6-10):** Interações Avançadas (iFrames, Múltiplas Abas, Dialogs e Network).
* **Fase 3 (Dias 11-15):** Arquitetura e Organização (Custom Fixtures, Parametrização e Page Object Model).
* **Fase 4 (Dias 16-20):** CI/CD, Visual Testing e Integrações Agênticas (GitHub Actions e MCP).

---

## 📂 Pasta de Práticas Recomendada

Para não bagunçar seus testes principais, crie uma pasta separada para esses exercícios:
```text
jornada-playwright-python/
│
├── tests/                           <-- Testes principais do portfólio
│
├── tests_pratica_20_dias/           <-- [CRIE ESTA PASTA] Para seus exercícios diários
│   ├── __init__.py
│   ├── test_dia_01_a_05.py
│   └── ...
```

---

## 🚀 FASE 1: Domínio de Localizadores e Asserções (Dias 1 a 5)

### 📌 Dia 1: Seletores Semânticos vs Seletores CSS/XPath
* **Objetivo:** Entender quando usar os localizadores amigáveis da API do Playwright e quando recorrer a seletores clássicos.
* **Estudo:** Leia sobre `page.get_by_role()`, `page.get_by_label()`, `page.get_by_placeholder()`.
* **Desafio Prático:** Acesse `https://demo.playwright.dev/todomvc/`. Escreva um teste que adicione uma tarefa e a localize de 3 maneiras diferentes (uma por role, uma por texto e uma por classe CSS).
* **Git Commit Sugerido:** `docs: adiciona plano de 20 dias e inicia pratica do dia 1`

### 📌 Dia 2: Lidando com Elementos Dinâmicos e Estados
* **Objetivo:** Aprender a validar estados de elementos (visível, oculto, habilitado, desabilitado).
* **Estudo:** Leia sobre asserções como `.to_be_visible()`, `.to_be_disabled()`, `.to_be_empty()`.
* **Desafio Prático:** Crie um teste no site `https://the-internet.herokuapp.com/dynamic_controls`. Clique no botão "Remove", valide que o checkbox sumiu e que o input de texto foi habilitado.

### 📌 Dia 3: Formulários - Inputs, Checkboxes e Radio Buttons
* **Objetivo:** Manipular múltiplos tipos de campos de formulário comuns.
* **Estudo:** Métodos `.fill()`, `.check()`, `.uncheck()`, `.is_checked()`.
* **Desafio Prático:** Acesse `https://the-internet.herokuapp.com/checkboxes`. Escreva um teste que marque o primeiro checkbox, desmarque o segundo e valide seus estados finais usando asserções `expect`.

### 📌 Dia 4: Dropdowns e Caixas de Seleção Múltipla
* **Objetivo:** Interagir com dropdowns nativos do HTML (`<select>`).
* **Estudo:** Método `.select_option()`.
* **Desafio Prático:** Acesse `https://the-internet.herokuapp.com/dropdown`. Selecione a "Option 2" pelo valor, depois a "Option 1" pelo texto visível e valide que a seleção foi alterada com sucesso.

### 📌 Dia 5: Revisão da Fase 1 e Refatoração
* **Objetivo:** Consolidar os aprendizados dos primeiros 4 dias.
* **Desafio Prático:** Junte os testes anteriores na pasta `tests_pratica_20_dias/test_fase_1.py`. Refatore os seletores para deixá-los o mais limpos e semânticos possível.

---

## 🌊 FASE 2: Interações Avançadas e Resiliência (Dias 6 a 10)

### 📌 Dia 6: Lidando com Modais, JavaScript Alerts e Prompts
* **Objetivo:** Aprender a interceptar caixas de diálogo nativas do navegador (Alert, Confirm, Prompt).
* **Estudo:** O evento `page.on("dialog", handler)`.
* **Desafio Prático:** Acesse `https://the-internet.herokuapp.com/javascript_alerts`. Clique no botão "Click for JS Prompt", faça seu script preencher seu nome na caixa que subir, clique em OK e valide a mensagem de sucesso na página.

### 📌 Dia 7: Trabalhando com iFrames (Quadros Incorporados)
* **Objetivo:** Interagir com elementos que estão dentro de outros documentos HTML incorporados.
* **Estudo:** Métodos `page.frame_locator()` e `page.frame()`.
* **Desafio Prático:** Acesse `https://the-internet.herokuapp.com/iframe`. Limpe o texto padrão escrito dentro do editor de texto WYSIWYG e escreva "Playwright domina iFrames!" usando localizadores de frame.

### 📌 Dia 8: Múltiplas Janelas, Abas e Contextos
* **Objetivo:** Navegar e testar fluxos que abrem novas abas no navegador.
* **Estudo:** O gerenciador de contexto `context.expect_page()`.
* **Desafio Prático:** Acesse `https://the-internet.herokuapp.com/windows`. Crie um teste que clique no link "Click Here", capture a nova aba aberta, valide que o título da nova aba está correto e depois retorne para a aba principal.

### 📌 Dia 9: Interceptação e Monitoramento de Rede (Mocking/Network)
* **Objetivo:** Aprender a monitorar requisições HTTP em segundo plano para testes ultra estáveis.
* **Estudo:** Métodos `page.route()` e `page.wait_for_response()`.
* **Desafio Prático:** Acesse o SauceDemo. Escreva um teste que monitore se, ao clicar no login, a requisição de autenticação retorna com status HTTP 200.

### 📌 Dia 10: Upload e Download de Arquivos
* **Objetivo:** Automatizar fluxos de envio e recebimento de arquivos.
* **Estudo:** Métodos `page.set_input_files()` e `page.expect_download()`.
* **Desafio Prático:** Acesse `https://the-internet.herokuapp.com/upload`. Escreva um teste que crie um arquivo temporário `.txt` localmente na pasta `scratch`, faça o upload dele e valide que o nome do arquivo aparece na tela de sucesso.

---

## 🏛️ FASE 3: Arquitetura, Fixtures e Page Objects (Dias 11 a 15)

### 📌 Dia 11: Criação de Custom Fixtures Avançadas
* **Objetivo:** Criar setups complexos compartilhados via `conftest.py`.
* **Desafio Prático:** Crie uma fixture chamada `authenticated_saucedemo` que já faça o login, adicione 3 produtos específicos ao carrinho e entregue a página pronta no carrinho de compras para o teste.

### 📌 Dia 12: Parametrização de Testes com Pytest
* **Objetivo:** Rodar o mesmo teste com diferentes conjuntos de dados de forma automática.
* **Estudo:** Decorador `@pytest.mark.parametrize`.
* **Desafio Prático:** Crie um teste de login parametrizado para o SauceDemo testando 3 usuários diferentes (usuário válido, usuário bloqueado e usuário com senha incorreta), validando a mensagem de erro específica de cada um.

### 📌 Dia 13: Introdução ao Page Object Model (POM) - Estrutura
* **Objetivo:** Aprender a desacoplar seletores da lógica de testes.
* **Estudo:** Crie uma pasta chamada `pages/` e crie a classe `LoginPage`.
* **Desafio Prático:** Mapeie os seletores e interações de login do SauceDemo dentro da classe `LoginPage`. Instancie essa classe no seu teste.

### 📌 Dia 14: Evoluindo o POM - Encapsulamento
* **Objetivo:** Adicionar novas páginas ao fluxo POM.
* **Desafio Prático:** Crie a classe `InventoryPage` e mapeie a ação de adicionar produto. Escreva um teste de ponta a ponta no SauceDemo chamando apenas métodos das suas classes em `pages/`.

### 📌 Dia 15: Configurações do Pytest (`pytest.ini` e Tags)
* **Objetivo:** Organizar e categorizar a execução dos testes.
* **Estudo:** Arquivo `pytest.ini` e markers (`@pytest.mark.smoke`).
* **Desafio Prático:** Crie um arquivo `pytest.ini`. Marque um dos seus testes como `@pytest.mark.smoke` e crie um comando no terminal para executar apenas os testes marcados como smoke.

---

## 🤖 FASE 4: CI/CD, Visual Testing e IA (Dias 16 a 20)

### 📌 Dia 16: Depuração Avançada (Playwright Trace Viewer)
* **Objetivo:** Aprender a usar a ferramenta de gravação de passos do Playwright para rastrear bugs complexos na CI.
* **Estudo:** Flag `--tracing` do Pytest.
* **Desafio Prático:** Rode seus testes gravando o trace. Abra o Trace Viewer usando o comando `playwright show-trace` e explore a linha do tempo, a árvore do DOM e as chamadas de rede gravadas.

### 📌 Dia 17: Testes Visuais de Regressão (Visual Comparisons)
* **Objetivo:** Validar se o layout visual da página quebrou (pixels desalinhados).
* **Estudo:** Biblioteca `pytest-playwright-visual` ou asserção visual nativa.
* **Desafio Prático:** Tire um print de comparação da página inicial do TodoMVC e crie uma validação que garante que a estrutura gráfica (cores, logos, fontes) não mudou.

### 📌 Dia 18: Simulação de Self-Healing Tests com IA
* **Objetivo:** Entender na prática como IAs de teste corrigem códigos quebrados.
* **Desafio Prático:** Mude de propósito o seletor do botão de login em um teste de `Login` para algo incorreto (ex: `button-errado`). Execute o teste, copie o erro do terminal e simule como você instruiria um agente de IA (como eu) a analisar o erro e propor a linha corrigida.

### 📌 Dia 19: Esteira Multi-Ambiente no GitHub Actions
* **Objetivo:** Rodar a esteira de CI em diferentes ambientes (staging vs produção).
* **Desafio Prático:** Modifique seu arquivo `.github/workflows/playwright.yml` para aceitar uma variável de ambiente que mude a URL base dos testes dependendo da branch em que o push foi feito.

### 📌 Dia 20: Consolidação do Portfólio de Alta Maturidade
* **Objetivo:** A revisão final do seu trabalho e publicação.
* **Desafio Prático:** Revise todos os arquivos das práticas diárias, garanta que os Conventional Commits estão lindos no histórico do Git. Faça uma publicação no LinkedIn marcando seu mentor com um print do seu repositório impecável!

---

## 📢 Como começar hoje mesmo?

Você está pronto para o **Dia 1**? 
1. Crie a pasta `tests_pratica_20_dias` e o arquivo para seus primeiros testes.
2. Tente fazer o desafio do **Dia 1** (Acesse `https://demo.playwright.dev/todomvc/`, adicione uma tarefa e ache o elemento de 3 formas diferentes).
3. Quando terminar ou se encontrar alguma barreira, mande uma mensagem aqui descrevendo o que você fez e colando o trecho do código para analisarmos juntos. **Estou aqui para te mentorar!**
