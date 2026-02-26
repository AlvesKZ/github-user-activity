# GitHub Activity CLI 

Uma ferramenta de linha de comando feita em Python que exibe a atividade recente de qualquer usuário do GitHub diretamente no terminal, utilizando a API pública do GitHub.

## Funcionalidades

Busca e exibe os eventos mais recentes de um usuário, incluindo:

- **Push** — commits enviados para um repositório
- **Criação/Exclusão** de branches e tags
- **Stars** em repositórios
- **Forks**
- **Issues** — abertura, fechamento e comentários
- **Pull Requests** — abertura, fechamento, revisões e comentários
- **Releases** publicadas
- **Adição de colaboradores**
- **Repositório tornado público**
- **Atualizações de Wiki**

## Tecnologias

- Python 3
- [requests](https://pypi.org/project/requests/) — para chamadas à API do GitHub

## Como usar

### Pré-requisitos

- Python 3 instalado
- Biblioteca `requests` instalada:

```bash
pip install requests
```

### Executando

```bash
python script.py <username_do_github>
```

### Exemplo

```bash
python script.py octocat
```

Saída esperada:

```
=== Recent Activity for octocat ===

- Pushed 3 commit(s) to octocat/Hello-World (main)
- Starred octocat/Spoon-Knife
- Opened issue #42 in octocat/Hello-World
- Merged pull request #7 in octocat/linguist

=== Total events: 4 ===
```

## Tratamento de erros

| Situação | Mensagem exibida |
|---|---|
| Usuário não encontrado | `User '<username>' not found.` |
| Limite de requisições atingido | `Rate limit exceeded. Please try again later.` |
| Nenhum evento recente | `No recent events found for user: <username>` |
| Outros erros HTTP | `Error fetching events for <username>: <status_code>` |

> A API pública do GitHub permite até **60 requisições por hora** sem autenticação. Para aumentar esse limite, utilize um token de acesso pessoal.

## Licença

Este projeto é de código aberto e está disponível sob a licença **MIT**.
