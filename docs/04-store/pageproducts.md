---
title: "pageProducts"
slug: "pageproducts"
doc_type: "reference"
summary: "Método que retorna página completa de produtos com paginação, categorias, cores, variações e filtros de ordenação."
tags:
  - store
  - produtos
  - paginação
  - filtros
related:
  - 04-store/visao-geral-store.md
  - 04-store/producttobox.md
  - 04-store/productboxdefault.md
---

## O que faz

Retorna uma página completa de produtos para a loja virtual. Este método facilita a criação de páginas dinâmicas (rotas) com paginação, filtros de categorias, cores, variações e ordenação dos produtos encontrados.

## Sintaxe

```twig
{% set conteudo = store.pageProducts({
	total_per_page: '15',
	page: extra.page,
	cor: extra.cor,
	var: extra.var,
	order: extra.order,
}) %}
```

## Quando usar

- Para criar páginas de listagem de produtos dinâmicas
- Em páginas de categoria com filtros
- Para paginação de resultados
- Quando precisa filtrar por cores, variações ou atributos

## Exemplo

```twig
{% set conteudo = store.pageProducts({
	total_per_page: '15',
	page: extra.page,
	cor: extra.cor,
	var: extra.var,
	order: extra.order,
}) %}

{% for produto in conteudo.products %}
	{{ store.productBoxDefault(produto) }}
{% endfor %}

{# Paginação #}
{% for pag in conteudo.pagination.page_all %}
	<a href="{{ pag.url }}">{{ pag.page }}</a>
{% endfor %}
```

Saída esperada:
```
Lista de produtos com filtros, categorias e paginação
```

## Retorno dos dados

**pagination** - Dados de paginação
- `pagination.page_total` (int) - Total de páginas
- `pagination.page_atual` (int) - Página atual
- `pagination.page_prev` (string) - Link para página anterior
- `pagination.page_next` (string) - Link para próxima página
- `pagination.page_all` (array) - Links para todas as páginas

**categories** - Categorias encontradas
- `categories.cl1` - Categorias nível 1
- `categories.cl2` - Categorias nível 2
- `categories.cl3` - Categorias nível 3

**categories_l1, categories_l2, categories_l3** - Categorias disponíveis nos filtros

**colors** - Array com cores disponíveis para filtro
- `colors.url_all` - URL para remover filtro de cor
- `colors.items` - Lista de cores com URLs de filtro

**variations** - Array com variações de produtos

**attributes** - Atributos de produtos para filtro

**filters** - Filtros de ordenação disponíveis

**products** - Array com produtos (dados de store.productToBox())

**page** - Variável com elementos importantes da página (quando disponível)

## Parâmetros de consulta

| Parâmetro | Padrão | Descrição |
|-----------|---------|-------------|
| page | 1 | Página em exibição |
| total_per_page | 15 | Total de resultados por página |
| order | valor-asc | Ordenação (valor-asc, valor-desc, produto, lancamento) |
| cor | '' | ID da cor |
| var | '' | ID da variação |
| attr | '' | ID do atributo |

## Observações

- Para recuperar as variáveis da querystring ($_GET) utilize a variável `extra`
- Os produtos retornados são os mesmos de store.productToBox()
- Suporta todos os parâmetros da API de produtos
- A variável `page` só está disponível em algumas páginas específicas

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
