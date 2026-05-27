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

### Retorno

O método retorna um objeto com a seguinte estrutura:

```json
{
  "pagination": {
    "_comment": "pagination array",
    "page_total": 0, // Total de páginas encontradas para o filtro
    "page_atual": 0, // Página atual sendo exibida
    "page_prev": "", // Link direto para a página anterior caso exista
    "page_next": "", // Link direto para a próxima página caso exista
    "page_all": [ // Matriz com links diretos para todas as páginas. Exemplo de uso: Como <option> de um <select>
      {
        "page": 0,
        "url": ""
      }
    ]
  },
  "categories": {
    "cl1": [ // Lista de categorias de nível 1 encontradas na página de exibição
      {
        "id": 0,
        "nome": "",
        "url": "",
        "tabela": 0
      }
    ],
    "cl2": [ // Lista de categorias de nível 2 encontradas na página de exibição
      {
        "id": 0,
        "nome": "",
        "url": "",
        "parent": { // Dados da categoria de nível 1 "pai" desta
          "id": 0,
          "nome": "",
          "url": ""
        }
      }
    ],
    "cl3": [ // Lista de categorias de nível 3 encontradas na página de exibição
      {
        "id": 0,
        "nome": "",
        "url": "",
        "parent": { // Dados da categoria de nível 2 "pai" desta
          "id": 0,
          "nome": "",
          "url": "",
          "parent": { // Dados da categoria de nível 1 "pai" desta
            "id": 0,
            "nome": "",
            "url": "",
            "tabela": 0
          }
        }
      }
    ]
  },
  "categories_l1": [ // Disponível apenas quando usa-se o filtro por categoria de nível 1
    {
      "id": 0,
      "tabela": 0,
      "nome": "",
      "url": "",
      "icone_tipo": 0,
      "icone": "",
      "cor": "#FFFFFF",
      "posicao": 0,
      "menu": true,
      "ordenar": "",
      "total_produtos": 0,
      "total_produtos_ativos": 0,
      "total_level2": 0
    }
  ],
  "categories_l2": [ // Disponível apenas quando usa-se o filtro por categoria de nível 1
    {
      "id": 0,
      "cid": 0,
      "nome": "",
      "url": "",
      "posicao": 0,
      "total_produtos": 0,
      "total_produtos_ativos": 0,
      "total_level3": 0
    }
  ],
  "categories_l3": [ // Disponível apenas quando usa-se o filtro por categoria de nível 2
    {
      "id": 0,
      "cid": 0,
      "nome": "",
      "url": "",
      "posicao": 0,
      "total_produtos": 0,
      "total_produtos_ativos": 0
    }
  ],
  "colors": {
    "url_all": "", // URL usada para fazer a filtragem de todos os produtos na tela, removendo a cor selecionada
    "items": [
      {
        "id": 0,
        "nome": "",
        "primaria": "#hex",
        "secundaria": "#hex",
        "img": "",
        "ativo": true,
        "posicao": 0,
        "estoque": 0,
        "url": "" // URL direta filtrando já com o código da cor na querystring
      }
    ]
  },
  "variations": [
    {
      "nome": "", // Nome da variação
      "url_all": "", // URL usada para remover a variação selecionada do filtro
      "items": [
        {
          "id": 0,
          "variacao_id": 0,
          "nome": "",
          "valor": "",
          "posicao": 0,
          "ativo": true,
          "estoque": 0,
          "url": "" // URL direta filtrando com o código da var na querystring
        }
      ]
    }
  ],
  "attributes": [
    {
      "nome": "", // Nome do atributo
      "url_all": "", // URL usada para remover o atributo selecionado do filtro
      "items": [
        {
          "id": 0,
          "nome": "",
          "url": "" // URL direta filtrando com o código da attr na querystring
        }
      ]
    }
  ],
  "filters": [ // Filtros de ordenação para a página em exibição
    {
      "value": "",
      "name": "",
      "data_url": "", // URL direta filtrando com o valor do order na querystring
      "selected": false
    }
  ],
  "products": [], // Os dados são os mesmos que podem ser encontrados em store.productToBox()
  "page": {} // Disponível apenas em algumas páginas com elementos importantes para funcionamento
}
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

```text
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
