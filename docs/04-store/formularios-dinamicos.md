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
