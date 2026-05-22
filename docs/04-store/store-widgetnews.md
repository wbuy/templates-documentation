---
title: "store.widgetNews()"
slug: "store-widgetnews"
doc_type: "reference"
summary: "Método que retorna widget de notícias e blog posts com suporte a filtros e paginação para conteúdo editorial."
tags:
  - store
  - widget
  - blog
  - notícias
related:
  - 04-store/visao-geral-store.md
  - 04-store/blogposts.md
---

## O que faz

Disponibiliza um widget de notícias/blog configurado para a loja virtual. Este método integra posts de blog ou notícias diretamente no template.

## Sintaxe

```twig
{% set noticias = store.widgetNews() %}
{# com parâmetros #}
{% set noticias = store.widgetNews({limit: '5'}) %}
```

## Quando usar

- Para exibir últimas notícias/blog posts
- Em rodapé ou áreas de conteúdo
- Para criar seções "Notícias Recentes"
- Em sidebars com conteúdo relevante

## Exemplo

```twig
{% set noticias = store.widgetNews({limit: '4'}) %}
{% if noticias.items|length > 0 %}
<section class="news-widget">
	<h3>{{ noticias.titulo }}</h3>
	<ul class="news-list">
	{% for noticia in noticias.items %}
		<li>
			<a href="{{ noticia.url }}">
				<strong>{{ noticia.titulo }}</strong>
				<small>{{ noticia.data|date('d/m/Y') }}</small>
			</a>
		</li>
	{% endfor %}
	</ul>
</section>
{% endif %}
```

Saída esperada:
```
Lista de últimas notícias/blog posts
```

## Retorno dos dados

**items** - Array de posts/notícias
- `items[x].id` (int) - ID do post
- `items[x].titulo` (string) - Título
- `items[x].resumo` (string) - Resumo/exceréto
- `items[x].url` (string) - Link para post completo
- `items[x].data` (date) - Data de publicação
- `items[x].autor` (string) - Autor do post

**titulo** (string) - Título do widget

## Parâmetros de consulta

| Parâmetro | Padrão | Descrição |
|-----------|---------|-------------|
| limit | 3 | Quantidade de posts a retornar |
| destaque | false | Se deve retornar apenas posts em destaque |

## Observações

- Requer posts/blog cadastrados no painel
- Excelente para SEO e engajamento
- Suporta filtros de destaque
- Dados ordenados por data de publicação

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
