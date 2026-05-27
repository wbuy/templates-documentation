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

### Retorno

```json
[
  {
    "vitrine": {
      "id": 0,
      "titulo": "",
      "data_limite": "YYYY-MM-DD",
      "tipo": "1",
      "banner_superior": "",
      "banner_inferior": ""
    },
    "produtos": []
  }
]
```

## Quando usar

- Para exibir vitrines de produtos em destaque
- Em seções templáticas da loja
- Para criar coleções curadas de produtos
- Em áreas de maior visibilidade

## Exemplo

```twig
{% set vitrines = store.showcaseProduct() %}
{% for vitrine in vitrines %}
<section class="showcase">
	{% if vitrine.vitrine.banner_superior %}
		{{ vitrine.vitrine.banner_superior|raw }}
	{% endif %}
	<h2>{{ vitrine.vitrine.titulo }}</h2>
	<div class="showcase-grid">
		{% for produto in vitrine.produtos %}
		<div class="showcase-item">
			{{ store.productBoxDefault(produto) }}
		</div>
		{% endfor %}
	</div>
	{% if vitrine.vitrine.banner_inferior %}
		{{ vitrine.vitrine.banner_inferior|raw }}
	{% endif %}
</section>
{% endfor %}
```

Saída esperada:
```
Vitrine de produtos com título e produtos formatados
```

## Retorno dos dados

Retorna uma matriz de vitrines configuradas.

**[x].vitrine** - Dados da vitrine
- `vitrine.id` (int)
- `vitrine.titulo` (string)
- `vitrine.data_limite` (date)
- `vitrine.tipo` (string) - 1 = Carrossel; 2 = Livre
- `vitrine.banner_superior` (string raw)
- `vitrine.banner_inferior` (string raw)

**[x].produtos** - Produtos da vitrine (mesma estrutura de `store.productToBox()`)

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

## Erros comuns

### Erro 1: Esquecer `|raw` nos banners
**Problema**: O HTML do banner aparece como texto.
**Diagnóstico**: Tags renderizadas no layout.
**Solução**: Usar `{{ vitrine.vitrine.banner_superior|raw }}` e `{{ vitrine.vitrine.banner_inferior|raw }}`.

### Erro 2: Não validar vitrines vazias
**Problema**: Seções vazias na página inicial.
**Diagnóstico**: Retorno sem itens.
**Solução**: Condicionar o bloco quando `vitrines|length > 0`.

## Veja também

- [Product To Box](04-store/producttobox.md)
- [Visão geral store](04-store/visao-geral-store.md)
