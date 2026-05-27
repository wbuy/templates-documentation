---
title: "store.categoriesMenu()"
slug: "store-categoriesmenu"
doc_type: "reference"
summary: "Método que retorna categorias formatadas especificamente para uso em menus de navegação e megamenus interativos."
tags:
  - store
  - categorias
  - menu
  - navegação
related:
  - 04-store/visao-geral-store.md
  - 04-store/store-categories.md
---

## O que faz

Retorna as categorias formatadas especificamente para uso em menus de navegação. Este método é similar ao store.categories() mas otimizado para renderização em menus interativos.

## Sintaxe

```twig
{% set menu_categorias = store.categoriesMenu() %}
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

- Para exibir menu de categorias na navegação principal
- Em menus drop-down/expansores
- Para navegadores interativos
- Em megamenus de categoria

## Exemplo

```twig
{% set menu_categorias = store.categoriesMenu() %}
<ul class="main-menu">
	{% for categoria in menu_categorias %}
	<li class="menu-item">
		<a href="{{ categoria.url }}">{{ categoria.nome }}</a>
		{% if categoria.subcategorias %}
		<ul class="submenu">
			{% for subcat in categoria.subcategorias %}
			<li><a href="{{ subcat.url }}">{{ subcat.nome }}</a></li>
			{% endfor %}
		</ul>
		{% endif %}
	</li>
	{% endfor %}
</ul>
```

Saída esperada:
```
Menu interativo de categorias com submenus
```

## Retorno dos dados

Mesma estrutura de store.categories():
- `[x].id` (int) - ID da categoria
- `[x].nome` (string) - Nome
- `[x].url` (string) - URL
- `[x].subcategorias` (array) - Subcategorias
- Propriedades adicionais para menu (ativo, classe, etc)

## Parâmetros de consulta

Nenhum parâmetro obrigatório.

## Observações

- Otimizado para renderização em menus
- Dados já vém formatados para li/ul
- Suporta árvore hierárquica de níveis
- Excelente para megamenus e navegações complexas

## Erros comuns

### Erro 1: Esquecer `|raw` em ícone ou banner
**Problema**: Ícones/banners aparecem como texto.
**Diagnóstico**: Tags HTML visíveis no menu.
**Solução**: Renderizar `{{ cat.icone_categoria|raw }}` e `{{ cat.banner|raw }}` quando existirem.

### Erro 2: Não validar subcategorias
**Problema**: Submenu vazio ou quebrado.
**Diagnóstico**: `cat.subs|length` igual a 0.
**Solução**: Condicionar a renderização de submenus com `if cat.subs|length >= 1`.

## Veja também

- [Store Categories](04-store/store-categories.md)
- [Visão geral store](04-store/visao-geral-store.md)
