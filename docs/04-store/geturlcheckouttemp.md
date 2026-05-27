---
title: "getURLCheckoutTemp()"
slug: "geturlcheckouttemp"
doc_type: "reference"
summary: "Gera URL temporária de checkout para adicionar produto dinâmico ao carrinho, útil para cotações e produtos customizados."
tags:
  - store
  - checkout
  - url
  - carrinho
  - customizado
related:
  - 04-store/visao-geral-store.md
  - 04-store/cart.md
---

## O que faz

O método `store.getURLCheckoutTemp()` gera uma URL de checkout completa com token, permitindo adicionar produtos dinâmicos ao carrinho sem que estejam cadastrados no banco. Recebe parâmetros como SKU, valor, peso, dimensões e prazo de produção, retornando uma URL pronta para usar em links ou redirecionamentos.

## Sintaxe

```twig
{% set url = store.getURLCheckoutTemp({
  sku: '1234abc',
  qtd_minima: '1',
  valor: 100,
  produto: 'Produto Custom',
  peso: 1,
  comprimento: 10,
  largura: 15,
  altura: 10,
  prazo_producao: 1,
  frete_gratis: true
}) %}
<a href="{{ url }}">Adicionar ao Carrinho</a>
```

### Retorno

Retorna uma URL completa de checkout com token temporário para adicionar o item ao carrinho.

## Quando usar

- Produtos customizados dinâmicos
- Cotações com valores variáveis
- Integração com calculadoras
- Produtos não catalogados

## Exemplo

```twig
{% set valor_final = 100 + desconto %}
{% set url = store.getURLCheckoutTemp({
  sku: 'CUSTOM-' ~ random(),
  valor: valor_final,
  produto: 'Serviço Customizado',
  frete_gratis: true
}) %}
<button onclick="window.location='{{ url }}'">Comprar Agora</button>
```

## Observações

- URL contém token temporário
- Válida por sessão/período definido
- Todos os parâmetros são obrigatórios
- Peso e dimensões em KG e CM

## Erros comuns

### Erro 1: Falta de parâmetro obrigatório
**Problema**: Esquecer `sku` ou `valor`
**Solução**: Incluir todos os campos

### Erro 2: Tipo errado de valor
**Problema**: `valor: "100"` (string) em vez de número
**Solução**: Usar `valor: 100` (número)

## Veja também

- [Visão geral store](04-store/visao-geral-store.md)
- [Cart](04-store/cart.md)
