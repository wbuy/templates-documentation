---
title: "productToBox"
slug: "producttobox"
doc_type: "reference"
summary: "Método que retorna array estruturado de produtos prontos para exibição em boxes com suporte a múltiplas ordenações."
tags:
  - store
  - produtos
  - array
  - galeria
related:
  - 04-store/visao-geral-store.md
  - 04-store/productboxdefault.md
  - 04-store/pageproducts.md
---

## O que faz

Retorna um array estruturado de produtos prontos para serem exibidos em caixas/boxes. Este método recupera dados formatados de produtos para uso em listagens, buscas e vitrines, sendo a base para construção de galerias de produtos.

## Sintaxe

```twig
{% set produtosBox = store.productToBox() %}
{# com parâmetros #}
{% set produtosBox = store.productToBox({limit: '4', order: 'random'}) %}
```

## Quando usar

- Para exibir galeria de produtos de forma padronizada
- Em listagens de produtos com filtros
- Para criar vitrines de destaque
- Com store.productBoxDefault() para renderizar caixas formatadas

## Exemplo

```twig
{% set produtosBox = store.productToBox({limit:'4', order:'lancamento'}) %}
<div class="row">
	{% for produto in produtosBox.data %}
	<div class="col-md-3">
		{{ store.productBoxDefault(produto) }}
	</div>
	{% endfor %}
</div>
```

Saída esperada:
```
Galeria de 4 produtos últimos lançamentos com informações completas
```

## Retorno dos dados

**data** - Array de produtos com estrutura completa
- `data[x].id` (int) - ID do produto
- `data[x].titulo` (string) - Título/nome
- `data[x].url` (string) - URL do produto
- `data[x].foto` (string) - URL da imagem principal
- `data[x].preco` (float) - Preço do produto
- `data[x].preco_desconto` (float) - Preço com desconto
- `data[x].descricao` (string) - Descrição breve
- E demais propriedades de produto

**total** - Total de produtos encontrados

## Parâmetros de consulta

| Parâmetro | Padrão | Descrição |
|-----------|---------|-------------|
| limit | 12 | Quantidade de produtos a retornar |
| order | valor-asc | Ordem (valor-asc, valor-desc, random, lancamento) |
| cid | '' | ID da categoria nível 1 |
| sid | '' | ID da categoria nível 2 |

## Observações

- Retorna dados estruturados prontos para rendering
- É usado frequentemente com store.productBoxDefault()
- Suporta múltiplas ordenações
- Performance otimizada para grandes listas

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
