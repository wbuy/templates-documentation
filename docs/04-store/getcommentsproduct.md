---
title: "getCommentsProduct()"
slug: "getcommentsproduct"
doc_type: "reference"
summary: "Método que retorna comentários e avaliações de um produto específico, incluindo nome, email, data e classificação."
tags:
  - store
  - comentários
  - avaliações
  - produtos
  - reviews
related:
  - 04-store/visao-geral-store.md
  - 04-store/getratings.md
  - 04-store/productdetail.md
---

## O que faz

O método `store.getCommentsProduct(productId)` recupera todos os comentários e avaliações para um produto específico. Retorna uma matriz com dados de cada comentário, incluindo informações do avaliador, classificação por estrelas, texto do comentário e data. Suporta paginação e filtros de ativação.

## Sintaxe

```twig
{% set comentarios = store.getCommentsProduct(productId) %}

{# Com parâmetros #}
{% set comentarios = store.getCommentsProduct(productId, {limit: '5'}) %}
```

**Parâmetro**: `limit` (string, padrão: 3) — Quantidade de comentários a retornar
**Filtro**: `ativo` (número, padrão: 1) — 1 para ativos, 0 para inativos

## Quando usar

- Exibir avaliações de um produto
- Mostrar comentários na página de detalhes do produto
- Criar seção de reviews com classificações
- Pré-condição: Produto deve ter ID válido

## Exemplo

```twig
{% set comentarios = store.getCommentsProduct(extra.id) %}
<h2>AVALIAÇÕES ({{ comentarios.total }})</h2>

{% if comentarios.total == 0 %}
<p>Nenhuma avaliação para este produto ainda.</p>
{% else %}
<div class="avaliacoes-lista">
  {% for comentario in comentarios.items %}
  <div class="avaliacao-item">
    <p><strong>{{ comentario.nome }}</strong> - {{ comentario.data|date('d/m/Y') }}</p>
    <div class="estrelas">{{ comentario.estrelas|raw }}</div>
    <p>{{ comentario.comentario }}</p>
  </div>
  {% endfor %}
</div>
{% endif %}

<a href="#" class="btn mymodal" data-include="avaliacao-form&id={{ extra.id }}">
  Deixe sua avaliação
</a>
```

Saída esperada:
```html
<h2>AVALIAÇÕES (2)</h2>
<div class="avaliacoes-lista">
  <div class="avaliacao-item">
    <p><strong>João Silva</strong> - 15/01/2024</p>
    <div class="estrelas">★★★★★</div>
    <p>Produto excelente, recomendo!</p>
  </div>
</div>
```

## Observações

- `total` retorna quantidade total de avaliações para o produto
- `items` contém array de comentários aprovados
- Classificação em estrelas vem em `comentario.estrelas` formatado em HTML
- Data vem em formato datetime; use filtro Twig `date()` para formatar
- Performance: Dados em cache

## Erros comuns

### Erro 1: Não verificar if comentarios vazio
**Problema**: Loop em array vazio causa erros
**Diagnóstico**: Página em branco ou lista vazia
**Solução**: Verificar `if comentarios.total > 0`

### Erro 2: Esquecer `|raw` em estrelas
**Problema**: `{{ comentario.estrelas }}` mostra HTML como texto
**Diagnóstico**: HTML renderizado como string
**Solução**: Usar `{{ comentario.estrelas|raw }}`

### Erro 3: ID de produto inválido
**Problema**: `store.getCommentsProduct(null)` ou ID inválido
**Diagnóstico**: Retorna array vazio
**Solução**: Verificar se `extra.id` existe e é válido

## Veja também

- [Visão geral store](04-store/visao-geral-store.md)
- [Get Ratings](04-store/getratings.md)
- [Store Product Detail](04-store/store-productdetail.md)
