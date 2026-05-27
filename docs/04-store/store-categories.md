---
title: "store.categories()"
slug: "store-categories"
doc_type: "reference"
summary: "Método que retorna estrutura hierárquica de categorias de produtos com até 3 níveis para navegação e filtros."
tags:
  - store
  - categorias
  - hierarquia
  - navegação
related:
  - 04-store/visao-geral-store.md
  - 04-store/store-categoriesmenu.md
---

## O que faz

Retorna a estrutura hierárquica de categorias de produtos da loja. Este método recupera todas as categorias organizadas em níveis (nível 1, 2 e 3) com dados para navegação e filtros.

## Sintaxe

```twig
{% set categorias = store.categories() %}
{# com parâmetros #}
{% set categorias = store.categories({cid: 1}) %}
```

### Retorno

```json
[
  {
    "id": 0,
    "tabela": 0,
    "nome": "",
    "url": "",
    "target": "",
    "icone_tipo": 0,
    "icone": "",
    "cor": "",
    "posicao": 0,
    "menu": false,
    "ativo": false,
    "ordenar": "",
    "total_produtos": 0,
    "subs": [
      {
        "id": 0,
        "nome": "",
        "url": "",
        "posicao": 0,
        "total_produtos": 0,
        "subs": [
          {
            "id": 0,
            "nome": "",
            "url": "",
            "posicao": 0,
            "total_produtos": 0
          }
        ]
      }
    ]
  }
]
```

## Quando usar

- Para exibir menu de categorias
- Em filtros de produtos
- Para criação de sitemaps de categoria
- Em navegadores/breadcrumbs

## Exemplo

```twig
{% set categorias = store.categories() %}
<nav class="categories">
	<ul>
	{% for cat in categorias %}
		<li>
			<a href="{{ cat.url }}">{{ cat.nome }}</a>
			{% if cat.subcategorias %}
			<ul>
				{% for subcat in cat.subcategorias %}
				<li><a href="{{ subcat.url }}">{{ subcat.nome }}</a></li>
				{% endfor %}
			</ul>
			{% endif %}
		</li>
	{% endfor %}
	</ul>
</nav>
```

Saída esperada:
```
Menu hierarquizado de categorias com links
```

## Retorno dos dados

**Array** - Lista de categorias nível 1 (raiz)
- `[x].id` (int) - ID da categoria
- `[x].nome` (string) - Nome
- `[x].url` (string) - URL da categoria
- `[x].tabela` (int) - Identificador de tabela
- `[x].subcategorias` (array) - Categorias nível 2
  - Mesma estrutura, pode ter sub-categorias nível 3

## Parâmetros de consulta

| Parâmetro | Padrão | Descrição |
|-----------|---------|-------------|
| cid | '' | ID da categoria para retornar apenas subcategorias |

## Observações

- Estrutura hierárquica até 3 níveis
- URLs já vém formatadas
- Essencial para navegação da loja
- Dados geralmente em cache

## Erros comuns

### Erro 1: Renderizar sem validar retorno
**Problema**: Menu vazio quando não há categorias.
**Diagnóstico**: `categorias|length` é 0.
**Solução**: Condicionar o bloco com `if categorias|length > 0`.

### Erro 2: Ignorar flags de menu/ativo
**Problema**: Categorias ocultas aparecem no layout.
**Diagnóstico**: Itens com `menu` ou `ativo` desabilitados.
**Solução**: Filtrar categorias conforme `menu`/`ativo` quando necessário.

## Veja também

- [Store Categories Menu](04-store/store-categoriesmenu.md)
- [Visão geral store](04-store/visao-geral-store.md)
