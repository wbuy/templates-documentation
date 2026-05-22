---
title: "showcaseProduct"
slug: "showcaseproduct"
doc_type: "reference"
summary: "Método que retorna vitrines de produtos curadas com coleções temáticas para destacar produtos especiais."
tags:
  - store
  - produtos
  - vitrines
  - coleções
related:
  - 04-store/visao-geral-store.md
  - 04-store/producttobox.md
---

## O que faz

Retorna dados de vitrines (showcases) de produtos criadas para destaque especial na loja. Vitrines são coleções curadas de produtos exibidas em seções especiais.

## Sintaxe

```twig
{% set vitrines = store.showcaseProduct() %}
{# com parâmetros #}
{% set vitrines = store.showcaseProduct({id: 1, limit: '6'}) %}
```

## Quando usar

- Para exibir vitrines de produtos em destaque
- Em seções templáticas da loja
- Para criar coleções curadas de produtos
- Em áreas de maior visibilidade

## Exemplo

```twig
{% set vitrines = store.showcaseProduct({limit: '8'}) %}
{% if vitrines.items %}
<section class="showcase">
	<h2>{{ vitrines.titulo }}</h2>
	<div class="showcase-grid">
		{% for produto in vitrines.items %}
		<div class="showcase-item">
			{{ store.productBoxDefault(produto) }}
		</div>
		{% endfor %}
	</div>
</section>
{% endif %}
```

Saída esperada:
```
Vitrine de produtos com título e produtos formatados
```

## Retorno dos dados

**items** - Array de produtos da vitrine
- Dados completos de produto (similar a store.productToBox)

**titulo** (string) - Título da vitrine

**descricao** (string) - Descrição da vitrine

## Parâmetros de consulta

| Parâmetro | Padrão | Descrição |
|-----------|---------|-------------|
| id | '' | ID específico da vitrine |
| limit | 6 | Quantidade de produtos |

## Observações

- Vitrines são configuráveis no painel de controle
- Contém coleções curadas de produtos
- Ideais para criar seções templáticas
- Suportam título e descrição personalizados

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
