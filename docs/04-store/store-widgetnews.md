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

### Retorno

```json
{
  "title": "",
  "subtitle1": "",
  "subtitle2": ""
}
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

## Erros comuns

### Erro 1: Renderizar sem dados configurados
**Problema**: Widget aparece vazio.
**Diagnóstico**: `widgetNews.title` ou subtítulos vazios.
**Solução**: Condicionar a renderização quando houver dados no painel.

### Erro 2: Não validar entrada de e-mail
**Problema**: Formulário aceita e-mails inválidos.
**Diagnóstico**: Cadastros com valores incorretos.
**Solução**: Manter `type="email"` e `required` no input.

## Veja também

- [Blog Posts](04-store/blogposts.md)
- [Visão geral store](04-store/visao-geral-store.md)
