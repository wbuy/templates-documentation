---
title: "Include no Twig"
slug: "include-no-twig"
doc_type: "reference"
summary: "Como compor templates usando include no Twig, com passagem de variáveis e boas práticas de organização."
tags:
  - twig
  - include
  - templates
related:
  - 01-introducao/criacao-de-widgets-com-include.md
  - 02-twig/sintaxe-basica.md
  - 07-modelos/visao-geral-modelos.md
---

# Include no Twig

## O que faz

O `include` permite **compor templates** a partir de arquivos menores e reutilizáveis (ex.: widgets, partes de página, cards, componentes). Em vez de duplicar HTML/Twig em várias páginas, você extrai um trecho para um arquivo dedicado e o inclui onde precisar.

Isso melhora:

- manutenção (corrige em um lugar e reflete em todos);
- consistência visual;
- legibilidade (arquivos menores e com um propósito claro).

## Sintaxe

Forma básica:

```twig
{% include 'caminho/do/arquivo.twig' %}
```
Incluindo com passagem de variáveis (quando você quer controlar explicitamente o contexto que entra no componente):

```twig
{% include 'caminho/do/arquivo.twig' with { product: p } %}
```

Onde:

- `'caminho/do/arquivo.twig'`: caminho do arquivo do componente/widget no seu tema (mantenha organização previsível);
- `with { ... }`: objeto com as variáveis que você quer disponibilizar dentro do arquivo incluído;
- `product: p`: exemplo de “apelido” (product) apontando para a variável local (p).

> **Observação:** a extensão e o caminho exatos dependem da estrutura do tema. O importante é manter consistência de nomenclatura e localização.

## Quando usar

Use include quando:

- um bloco aparece em mais de uma página (ex.: card de produto, banner, selo, bloco de avaliação);
- você quer separar uma página grande em seções (ex.: topo, rodapé, vitrine, carrossel);
- você quer padronizar a renderização de um objeto (ex.: sempre renderizar product da mesma forma).

Evite include quando:

- o bloco é realmente único e pequeno (incluir pode reduzir legibilidade);
- você não tem um “contrato” de variáveis claro (muitos includes com variáveis implícitas viram fonte de bug).

## Exemplo

### Exemplo 1 — incluir um componente simples

Na página (pai):

```twig
<h2>Produtos em destaque</h2>

{% for p in pageProducts %}
  {% include 'widgets/product-card.twig' with { product: p } %}
{% endfor %}
```

No arquivo incluído (`widgets/product-card.twig`):

```twig
<div class="product-card">
  <h3>{{ product.name }}</h3>
</div>
```

Resultado esperado: cada item de `pageProducts` é renderizado por um componente único (`product-card`), reduzindo duplicação.

### Exemplo 2 — include com fallback de variável

Se o componente depende de uma variável opcional, defina um padrão:

```twig
{% set showPrice = showPrice is defined ? showPrice : true %}

<div class="product-card">
  <h3>{{ product.name }}</h3>
  {% if showPrice %}
    <span class="price">{{ product.price }}</span>
  {% endif %}
</div>
```

## Observações

- **Contrato de contexto:** trate cada arquivo incluído como um “mini-API”.
  - Documente (nem que seja em comentário no topo do arquivo incluído) quais variáveis ele espera (`product`, `items`, `title`, etc.).
- **Organização:** agrupe includes por finalidade (ex.: widgets/, components/, partials/) e use nomes em kebab-case.
- **Evite acoplamento invisível:** preferir with { ... } para tornar explícito o que o componente recebe, reduzindo dependência de variáveis globais/implícitas.
- **Performance e cache:** muitos includes não são necessariamente um problema, mas duplicação de lógica e renderização pesada pode ser. Em páginas críticas, mantenha componentes enxutos e bem definidos.
- **Conteúdo e SEO:** incluir componentes é só uma técnica de composição; o que importa é o HTML final. Garanta headings e estrutura semântica corretos no resultado renderizado.

## Erros comuns

- **Path incorreto no include**
  Diagnóstico: componente não aparece / erro de renderização.
  Correção: valide o caminho/nome do arquivo e padronize onde os componentes ficam.
- **Variável esperada não foi passada**
  Diagnóstico: dentro do componente, campos ficam vazios (ex.: product não existe).
  Correção: use with { product: p } (ou renomeie para bater com o que o componente espera).
- **Componente “mágico” dependente de variáveis implícitas**
  Diagnóstico: funciona em uma página, quebra em outra (porque o contexto muda).
  Correção: explicite o contexto via with { ... } e defina defaults com is defined.
- **Componente grande demais (vários conceitos no mesmo include)**
  Diagnóstico: difícil de reutilizar; qualquer mudança quebra vários cenários.
  Correção: quebre em 2–3 includes menores, mantendo “um conceito por arquivo”.

Veja também

- Criação de widgets com include
- Sintaxe básica do Twig
- Visão geral de modelos
