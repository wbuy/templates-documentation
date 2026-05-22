---
title: "store.periodicOffers()"
slug: "store-periodicoffers"
doc_type: "reference"
summary: "Método que retorna ofertas periódicas e sazonais com datas de vigência definidas para promoções especiais."
tags:
  - store
  - ofertas
  - promoções
  - descontos
related:
  - 04-store/visao-geral-store.md
  - 04-store/producttobox.md
---

## O que faz

Retorna as ofertas periódicas/sazonais cadastradas na loja virtual. Estas são promocional e descontos especiais com datas de vigência definidas.

## Sintaxe

```twig
{% set ofertas = store.periodicOffers() %}
{# com parâmetros #}
{% set ofertas = store.periodicOffers({limit: '5'}) %}
```

## Quando usar

- Para exibir ofertas sazonais/periódicas
- Em seções de promoções
- Para criar vitrines de ofertas limitadas
- Em carrosséis de produtos em promoção

## Exemplo

```twig
{% set ofertas = store.periodicOffers({limit: '6'}) %}
{% if ofertas.items|length > 0 %}
<section class="periodic-offers">
	<h2>Ofertas Periódicas</h2>
	<div class="offer-grid">
	{% for oferta in ofertas.items %}
		<div class="offer-item">
			<span class="badge">{{ oferta.desconto }}% OFF</span>
			{{ store.productBoxDefault(oferta.produto) }}
		</div>
	{% endfor %}
	</div>
</section>
{% endif %}
```

Saída esperada:
```
Vitrines de ofertas periódicas com descontos
```

## Retorno dos dados

**items** - Array de ofertas
- `items[x].id` (int) - ID da oferta
- `items[x].titulo` (string) - Título
- `items[x].produto` (object) - Dados do produto
- `items[x].desconto` (float) - Percentual de desconto
- `items[x].data_inicio` (date) - Data de início
- `items[x].data_fim` (date) - Data de fim

## Parâmetros de consulta

| Parâmetro | Padrão | Descrição |
|-----------|---------|-------------|
| limit | 6 | Quantidade de ofertas a retornar |

## Observações

- Retorna apenas ofertas ativas (dentro do período)
- Dados configuráveis no painel de controle
- Excelente para criar seções de promoções
- Suporta múltiplas ofertas simultaneáneas

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
