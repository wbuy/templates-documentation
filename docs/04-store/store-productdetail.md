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

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
