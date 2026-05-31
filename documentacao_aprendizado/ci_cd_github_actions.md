# Bônus: Integração Contínua (CI/CD) com GitHub Actions

Parabéns por dar este passo extra! Configurar a integração contínua (CI) é o que separa um testador manual ou automatizador júnior de um **Engenheiro de QA profissional**. 

Neste guia prático, vamos destrinchar como funciona o **GitHub Actions** e como criamos uma esteira automática que roda todos os seus testes do Playwright sempre que você envia código para o GitHub.

---

## 📖 1. O que é CI/CD e GitHub Actions?

* **CI (Continuous Integration - Integração Contínua):** É a prática de integrar alterações de código ao repositório principal de forma frequente. No nosso contexto, significa rodar a suíte de testes E2E automaticamente a cada `git push` ou `Pull Request` para garantir que o novo código não "quebrou" nenhuma funcionalidade existente (regressão).
* **GitHub Actions:** É a ferramenta nativa do GitHub para criar esteiras de automação (workflows). O GitHub disponibiliza um servidor virtual gratuito na nuvem (chamado de Runner) para executar os comandos do nosso projeto.

---

## 🛠️ 2. Como as Esteiras são Estruturadas (Arquivos YAML)

Toda a configuração de uma esteira no GitHub Actions é descrita em um arquivo escrito em formato **YAML** (extensão `.yml`). Esse arquivo deve ser obrigatoriamente criado em um diretório específico na raiz do seu projeto: `.github/workflows/`.

O fluxo segue a seguinte estrutura:

```
                  ┌───────────────────────┐
                  │   GATILHO (Trigger)   │
                  │   git push / PR       │
                  └───────────┬───────────┘
                              ▼
                  ┌───────────────────────┐
                  │    SERVER RUNNER      │
                  │    (ubuntu-latest)    │
                  └───────────┬───────────┘
                              ▼
                 PASSOS DO JOB (Steps):
                  1. Copia o repositório
                  2. Configura o Python
                  3. Instala dependências
                  4. Instala navegadores
                  5. Executa os testes (pytest)
                  6. Salva relatório HTML
```

---

## 💻 3. Entendendo a anatomia do nosso arquivo `.github/workflows/playwright.yml`

Acabamos de criar o arquivo `.github/workflows/playwright.yml` no seu projeto. Veja o que cada bloco dele significa:

1. **`name: Playwright E2E Tests`:** É o nome amigável que aparecerá na aba "Actions" do seu GitHub.
2. **`on:` (Gatilhos):** Define quais eventos disparam a esteira. No nosso caso, ela rodará sempre que houver um `push` ou `pull_request` nas branches principais (`main` ou `master`).
3. **`runs-on: ubuntu-latest`:** Indica que o GitHub criará uma máquina virtual rodando a versão estável mais recente do sistema operacional Linux Ubuntu para rodar os testes.
4. **`steps:` (Passos):** É a sequência lógica de ações que o servidor vai executar:
   * **`uses: actions/checkout@v4`:** Entra na pasta do seu repositório e copia os arquivos do código para dentro da máquina virtual.
   * **`uses: actions/setup-python@v5`:** Instala e configura a versão do Python especificada no servidor. O parâmetro `cache: 'pip'` ajuda a acelerar execuções futuras guardando pacotes em cache.
   * **`pip install -r requirements.txt`:** Executa a instalação de todas as bibliotecas listadas nas nossas dependências.
   * **`playwright install --with-deps`:** Além de baixar os navegadores do Playwright na nuvem, o parâmetro `--with-deps` instala dependências nativas necessárias do sistema operacional Linux para rodar navegadores WebKit/Chromium em servidores sem tela de vídeo de forma headless.
   * **`run: pytest -n auto`:** Executa a suíte de testes em paralelo na máquina virtual.
   * **`upload-artifact@v4`:** O comando `if: always()` garante que, mesmo se algum teste falhar (deixando o status em vermelho), o relatório HTML gerado pelo Pytest será capturado e disponibilizado para download no site do GitHub, permitindo que você descubra exatamente qual assert falhou.

---

## 🏆 4. Passo a Passo Prático para Ver a Mágica Acontecer

Agora é a hora de colocar o seu conhecimento à prova e ver os seus testes rodando sozinhos na nuvem! Siga esses passos exatos:

### Passo 4.1: Salvar e Comitar as Mudanças
No seu terminal do VS Code, registre as alterações da esteira de CI/CD:
```bash
git add .
git commit -m "feat: adiciona esteira de CI com GitHub Actions para execucao automatica"
```

### Passo 4.2: Enviar para o GitHub
Envie as alterações para a sua branch principal no repositório remoto:
```bash
git push origin main
```
*(Nota: Se sua branch principal se chamar `master`, use `git push origin master`)*.

### Passo 4.3: Acompanhar a Execução na Nuvem
1. Abra o navegador e acesse a página do seu repositório no GitHub: `https://github.com/EduardoFrAlmeida/jornada-playwright-python`.
2. Clique na aba **"Actions"** (localizada no menu superior, ao lado de Pull Requests).
3. Você verá uma execução em andamento chamada **"Playwright E2E Tests"** com uma bolinha amarela girando.
4. Clique na execução e depois no job **"run-tests"** para ver em tempo real o console do Linux instalando o Python, as dependências e rodando seus testes!
5. Quando tudo terminar com sucesso, a bolinha ficará verde! 

### Passo 4.4: Baixar os Relatórios
Ao término do job (seja com sucesso ou falha), desça até o final da página de execução. Na seção **"Artifacts"**, você verá um arquivo para download chamado `pytest-html-report`. Baixe-o e extraia o arquivo `.html` para ver o relatório de testes gerado diretamente pelo servidor do GitHub!
