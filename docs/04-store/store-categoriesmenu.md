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

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
