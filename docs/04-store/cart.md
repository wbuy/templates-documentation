---
title: "cart()"
slug: "cart"
doc_type: "reference"
summary: "Método que retorna dados completos do carrinho de compras, incluindo itens, valores, frete e descontos."
tags:
  - store
  - carrinho
  - compras
  - itens
  - frete
related:
  - 04-store/visao-geral-store.md
  - 04-store/blogposts.md
  - 04-store/listeners-readlistener.md
---

## O que faz

O método `store.cart()` recupera todos os dados do carrinho de compras do usuário, incluindo lista de produtos adicionados, quantidades, valores unitários e parciais, informações de frete, descontos aplicados, e totalizações. Essencial para exibir sacola de compras e cálculos dinâmicos de valores.

## Sintaxe

```twig
{% set carrinho = store.cart() %}
```

**Retorna**: Objeto com estrutura aninhada contendo:
- `total_product` (int) — Total de produtos
- `total_items` (int) — Total de itens (quantidade)
- `cart` (object) — Dados detalhados do carrinho
  - `items[]` (array) — Lista de produtos
  - `amount` (object) — Totalizações

## Quando usar

- Exibir sacola/carrinho de compras
- Mostrar resumo de valores em header
- Atualizar dinâmico de totais após adição/remoção
- Calcular fretes e descontos
- Processar checkout

## Exemplo

```twig
{% set carrinho = store.cart() %}
<div class="header-cart">
  <span class="qtd">{{ carrinho.total_items }} itens</span>
  <span class="total">R$ {{ carrinho.cart.amount.total }}</span>
</div>

{% if carrinho.total_items > 0 %}
<div class="cart-items">
  {% for item in carrinho.cart.items %}
  <div class="item">
    <img src="{{ item.foto }}" alt="{{ item.produto }}">
    <p>{{ item.produto }}</p>
    <span class="qty">{{ item.quantidade }}x</span>
    <span class="price">R$ {{ item.valor_parcial }}</span>
  </div>
  {% endfor %}
</div>

<div class="cart-summary">
  <p>Subtotal: <strong>R$ {{ carrinho.cart.amount.subtotal }}</strong></p>
  <p>Frete: <strong>R$ {{ carrinho.cart.amount.freight.valor }}</strong></p>
  <p>Desconto: <strong>-R$ {{ carrinho.cart.amount.discount }}</strong></p>
  <p class="total">Total: <strong>R$ {{ carrinho.cart.amount.total }}</strong></p>
</div>
{% else %}
<p>Seu carrinho está vazio</p>
{% endif %}
```

Saída esperada:
```html
<div class="header-cart">
  <span class="qtd">2 itens</span>
  <span class="total">R$ 150.50</span>
</div>
```

## Observações

- Carrinho persiste por sessão/cookie
- Atualiza dinamicamente com listeners JavaScript
- Pode incluir promoções, combos e brindes
- Disponível mesmo para usuário não-logado
- Performance: Operação rápida, sem impacto

## Erros comuns

### Erro 1: Acessar sem verificar se carrinho está vazio
**Problema**: `carrinho.cart.items[0]` quando carrinho vazio
**Diagnóstico**: Erro ao tentar acessar primeira posição
**Solução**: Verificar `if carrinho.total_items > 0`

### Erro 2: Confundir total_product com total_items
**Problema**: `total_product` (quantidade de produtos) vs `total_items` (quantidade de itens/unidades)
**Diagnóstico**: Quantidade incorreta exibida
**Solução**: Usar `total_items` para quantidade de unidades no carrinho

### Erro 3: Estrutura aninhada profunda sem verificação
**Problema**: Acessar `carrinho.cart.amount.freight.valor` sem verificar existência
**Diagnóstico**: Erro se valor não existe
**Solução**: Envolver em condicional `if carrinho.cart.amount.freight`

## Veja também

- [Visão geral store](04-store/visao-geral-store.md)
- [Listeners readListener](04-store/listeners-readlistener.md)
- [Blog Posts](04-store/blogposts.md)
