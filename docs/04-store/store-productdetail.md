---
title: "store.productDetail()"
slug: "store-productdetail"
doc_type: "reference"
summary: "Método que retorna dados completos e detalhados de um produto específico incluindo galeria, variações e avaliações."
tags:
  - store
  - produtos
  - detalhe
  - página-produto
related:
  - 04-store/visao-geral-store.md
  - 04-store/producttobox.md
---

## O que faz

Retorna dados completos e detalhados de um produto específ ico. Este método é essencial para páginas de detalhe de produto, oferecendo todas as informações necessárias para apresentação completa.

## Sintaxe

```twig
{% set produto = store.productDetail({id: product_id}) %}
{# ou via extra para páginas dinâmicas #}
{% set produto = store.productDetail() %}
```

### Retorno

```json
{
  "product_id": 0,
  "sku": "",
  "category": {
    "cl1": {
      "id": 0,
      "nome": "",
      "url": "",
      "tabela": 0
    },
    "cl2": {
      "id": 0,
      "nome": "",
      "url": ""
    },
    "cl3": {
      "id": 0,
      "nome": "",
      "url": ""
    }
  },
  "breadcrumbs": [
    {
      "page": "",
      "url": ""
    }
  ],
  "photos_type": 0,
  "photos": [
    {
      "cor_id": 0,
      "foto": "",
      "foto_mini": "",
      "cor_count": 0,
      "video": "",
      "video_raw": ""
    }
  ],
  "badge": "",
  "product": "",
  "code": "",
  "description": "",
  "specification": "",
  "items": "",
  "warranty": "",
  "video": {
    "foto": "",
    "foto_mini": "",
    "video": "",
    "video_raw": ""
  },
  "brand": {
    "id": 0,
    "nome": "",
    "url": ""
  },
  "likes": 0,
  "rating": {
    "votes": {
      "total": 0,
      "pontos": 0
    },
    "percent": 0.0
  },
  "allow_comments": false,
  "attachments": [
    {
      "id": 0,
      "titulo": "",
      "arquivo": "",
      "filename_download": ""
    }
  ]
}
```

## Quando usar

- Em páginas de detalhe de produto
- Para exibir informações completas (descrição, galeria, variações)
- Para mostrar avaliações e comentários
- Em páginas de produto com cart dinâmico

## Exemplo

```twig
{% set produto = store.productDetail() %}
{% if produto %}
<div class="product-detail">
	<div class="product-gallery">
		{% for foto in produto.fotos %}
		<img src="{{ foto.url }}" alt="{{ produto.titulo }}" />
		{% endfor %}
	</div>
	<div class="product-info">
		<h1>{{ produto.titulo }}</h1>
		<p class="description">{{ produto.descricao|raw }}</p>
		<span class="preco">R$ {{ produto.preco }}</span>
	</div>
</div>
{% endif %}
```

Saída esperada:
```
Página completa de detalhe do produto com galeria
```

## Retorno dos dados

**id** (int) - ID do produto

**titulo** (string) - Título/nome

**descricao** (string) - Descrição detalhada (HTML)

**preco** (float) - Preço normal

**preco_desconto** (float) - Preço com desconto

**fotos** (array) - Galeria de imagens do produto

**variações** (array) - Variações (cores, tamanhos, etc)

**avaliacoes** (array) - Comentários e avaliações

## Parâmetros de consulta

| Parâmetro | Padrão | Descrição |
|-----------|---------|-------------|
| id | extra.id | ID do produto (via parâmetro ou extra) |

## Observações

- Retorna dados mais completos que store.productToBox()
- Inclui HTML na descrição (usar raw no Twig)
- Essencial para páginas de detalhe
- Inclui dados de avaliações e comentarios

## Erros comuns

### Erro 1: Esquecer `|raw` em campos HTML
**Problema**: Descrição, selos ou vídeo aparecem como texto.
**Diagnóstico**: Tags HTML visíveis no front.
**Solução**: Usar `|raw` em campos como `description`, `badge` e `video_raw`.

### Erro 2: Chamar sem ID em páginas fora do detalhe
**Problema**: Retorno vazio ao usar fora da página de produto.
**Diagnóstico**: `extra.id` não existe.
**Solução**: Passar `id` explicitamente: `store.productDetail({id: product_id})`.

## Veja também

- [Product To Box](04-store/producttobox.md)
- [Visão geral store](04-store/visao-geral-store.md)
