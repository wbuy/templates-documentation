---
title: "Formulários dinâmicos"
slug: "formularios-dinamicos"
doc_type: "how-to"
summary: "Sistema para trabalhar com formulários customizáveis criados no painel administrativo, incluindo recuperação de dados e HTML pronto."
tags:
  - store
  - formulários
  - dinâmico
  - customização
  - painel
related:
  - 04-store/visao-geral-store.md
  - 04-store/getdynamicpages.md
---

## O que faz

Formulários dinâmicos são questões e campos customizáveis criados no painel de controle da loja. A documentação fornece três métodos principais para trabalhar com eles: recuperar dados básicos do formulário, obter todas as perguntas agrupadas, e renderizar o HTML completo e funcional do formulário.

Essencial para implementar formulários de contato, feedback, inscrições e outras coletadas de dados customizadas sem necessidade de codificar a estrutura.

## Sintaxe

```twig
{# Método 1: Dados básicos do formulário #}
{% set formulario = store.getDynamicForm(FORM_ID) %}

{# Método 2: Perguntas agrupadas #}
{% set perguntas = store.getDynamicFormQuestions(FORM_ID) %}

{# Método 3: HTML completo pronto para usar #}
{% set html = store.getDynamicFormHTML(FORM_ID) %}
```

Onde `FORM_ID` é o ID do formulário encontrado no painel de controle.

### Retorno

- `getDynamicForm()`: Retorna um objeto com dados básicos do formulário:

  ```json
  {
    "id": 1966,
    "titulo": "Testando retorno do tema",
    "texto": "<p>Só to testando aqui</p>",
    "url": "testando-retorno-do-tema-form",
    "seo": {
      "title": null,
      "description": null
    },
    "scripts": "", // string com scripts customizados (prontos para renderizar) em HTML
    "banner": "https://cdn.sistemawbuy.com.br/arquivos/arquivo-anexado.jpg",
    "banner_mobile": "https://cdn.sistemawbuy.com.br/arquivos/arquivo-mobile-anexado.jpg",
    "mensagem_sucesso_tipo": 1,
    "mensagem_sucesso": "", // String com mensagem customizada para exibir após a confirmação do formulário
    "texto_botao_submit": "", // String com texto customizado para o botão de submit
    "require_login": 0,
    "ativo": 1,
    "created": "2026-05-28 11:17:29",
    "updated": "2026-05-28 11:17:29",
    "total_perguntas": 3,
    "total_respostas": 0,
    "url_completa": "https://tpt-wbamanda.lojawbuy.com.br/testando-retorno-do-tema-form"
  }
  ```

- `getDynamicFormQuestions()`: Retorna uma matriz de grupos e perguntas:

  ```json
  {
    "grupoX": [
      {
        "id": 1234,
        "form_id": 9999,
        "tipo": "input", // input | textarea | select | checkbox | radio
        "grupo": "dados",
        "pergunta": "Nome",
        "pergunta_text": "", // texto explicativo adicional
        "obrigatorio": 1,
        "inputtype": "text",
        "mascara": "", // Tipo de máscara (se ativo) - vlr | cpf | cnpj | cpf_cnpj | telefone
        "respostas": "",
        "inputsize": 12,
        "posicao": 0,
        "created": "2026-05-28 11:18:15",
        "updated": "2026-05-28 11:50:27",
        "class_type": "col-md-12",
        "open_row": 1,
        "close_row": 1
      }
    ],
    "grupoY": [
      {
        "id": 7372,
        "form_id": 1966,
        "tipo": "input",
        "grupo": "publicidade",
        "pergunta": "Titulo",
        "pergunta_text": "",
        "obrigatorio": 1,
        "inputtype": "text",
        "mascara": "",
        "respostas": "",
        "inputsize": 9,
        "posicao": 0,
        "created": "2026-05-28 11:51:43",
        "updated": "2026-05-28 11:51:43",
        "class_type": "col-md-9",
        "open_row": 1,
        "close_row": 0
      }
    ]
  }
  ```

- `getDynamicFormHTML()`: Retorna uma string HTML completa do formulário, incluindo estrutura, banner, perguntas e botão de submit, pronta para renderizar:

  ```html
  <div class="central">
    <h2 class="titulo">[Título do Formulário]</h2>
    <div class="row">
        <div class="col">
          <div class="texto">
              <p>[Subtítulo do Formulário]</p>
          </div>
        </div>
    </div>
    <hr>
    <form action="modulos/paginas/formularios_func.php" method="post" class="post frm-dynamic" enctype="multipart/form-data" novalidate="novalidate">

        <h3 class="title-form mb-3">[grupoX]</h3>

        <div class="row">
          <div class="col-md-12">
              <p class="label i">Nome</p>
              <p class="text-muted mb-2"></p>
              <input type="text" name="7369" class="form-control" required="">
          </div>
        </div>

        <h3 class="title-form mb-3">[grupoY]</h3>

        <div class="row">
          <div class="col-md-9">
              <p class="label i">Titulo</p>
              <p class="text-muted mb-2"></p>
              <input type="text" name="7372" class="form-control" required="">
          </div>
        </div>
    </form>
  </div>
  ```

## Quando usar

- Exibir formulário de contato customizado
- Coletar feedback de clientes
- Inscrição em newsletters ou listas
- Formulários de enquete ou pesquisa
- Pré-condição: Formulário deve ser criado no painel administrativo

## Exemplo

```twig
{# Opção 1: Usar HTML pronto (mais simples) #}
{% set html = store.getDynamicFormHTML(123) %}
{{ html|raw }}

{# Opção 2: Customizar com as perguntas #}
{% set perguntas = store.getDynamicFormQuestions(123) %}
<form method="POST" action="/formulario/enviar">
  {% for grupo in perguntas %}
    <h3>{{ grupo.titulo }}</h3>
    {% for pergunta in grupo.perguntas %}
      <div class="form-group">
        <label>{{ pergunta.titulo }}</label>
        <input type="text" name="pergunta_{{ pergunta.id }}">
      </div>
    {% endfor %}
  {% endfor %}
  <button type="submit">Enviar</button>
</form>
```

Saída esperada:

```html
<form method="POST" action="/formulario/enviar">
  <h3>Informações Pessoais</h3>
  <div class="form-group">
    <label>Seu Nome</label>
    <input type="text" name="pergunta_1">
  </div>
  <button>Enviar</button>
</form>
```

## Observações

- `getDynamicFormHTML()` retorna o formulário completo com banner e botão
- `getDynamicFormQuestions()` retorna estrutura de grupo e perguntas
- `getDynamicForm()` retorna apenas dados básicos
- Formulários são configuráveis totalmente no painel
- Performance: Dados em cache, sem impacto

## Erros comuns

### Erro 1: ID de formulário inválido

**Problema**: `store.getDynamicFormHTML(999)` onde 999 não existe
**Diagnóstico**: Retorna vazio ou erro
**Solução**: Verificar ID correto no painel administrativo

### Erro 2: Esquecer `|raw` ao renderizar HTML

**Problema**: HTML aparece como texto `<form>...`
**Diagnóstico**: Estrutura do formulário exibida como string
**Solução**: Usar `{{ html|raw }}`

### Erro 3: Confundir os 3 métodos

**Problema**: Usar `getDynamicForm()` esperando HTML completo
**Diagnóstico**: Retorna apenas dados, não estrutura visual
**Solução**: Usar `getDynamicFormHTML()` para HTML, outros para dados

## Veja também

- [Visão geral store](04-store/visao-geral-store.md)
- [Get Dynamic Pages](04-store/getdynamicpages.md)
- [Get Info Pages](04-store/getinfopages.md)
