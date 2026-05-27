---
title: "blogPosts()"
slug: "blogposts"
doc_type: "reference"
summary: "Método que retorna uma matriz com posts marcados como destaque no blog da loja virtual, com limite configurável."
tags: 
  - store
  - blog
  - posts
  - destaque
  - conteúdo
related: 
  - 04-store/visao-geral-store.md
  - 04-store/cart.md
---

## O que faz

O método `store.blogPosts()` recupera posts do blog da loja que foram marcados como destaque. Retorna uma matriz de dados com informações sobre cada post (título, conteúdo, data, visualizações, imagem), permitindo exibir notícias e conteúdo relacionado nos templates.

Este método é essencial para criar seções de blog dinâmicas, vitrines de conteúdo e integrações de notícias no template.

## Sintaxe

```twig
{% set posts = store.blogPosts() %}

{# Com parâmetro de limite #}
{% set posts = store.blogPosts({limit: '10'}) %}
```

**Parâmetros:**
`limit` (string) — Quantidade de posts a retornar (padrão: 4)

### Retorno

```json
{
  "id": 0,
  "titulo": "",
  "blog_url": "",
  "texto": "",
  "imagem": "", // URL da imagem de exibição
  "visualizacao": "", // Número de visualizações do post
  "cadastro": "YYYY-MM-DD HH:MM:SS"
}
```

## Quando usar

- Exibir seção de novidades/blog na home
- Integrar conteúdo de blog em vitrines
- Listar posts em ordem de relevância
- Pré-condição: Blog deve estar criado e com posts marcados como destaque

## Exemplo

```twig
{% set blog_posts = store.blogPosts() %}
{% if blog_posts|length >= 1 %}
<section class="block blog-posts">
  <div class="central">
    <h2 class="titulo">NOVIDADES DO BLOG</h2>
    <section class="row">
    {% for post in blog_posts %}
      <article class="col-md-3">
        <div class="item">
          <a href="{{ post.blog_url }}/" target="_blank">
            <div class="foto">
              <img src="{{ post.imagem }}" alt="{{ post.titulo }}" class="img-cover">
            </div>
            <h4>{{ post.titulo }}</h4>
          </a>
          <p class="info">{{ post.visualizacao }} visualizações</p>
        </div>
      </article>
    {% endfor %}
    </section>
  </div>
</section>
{% endif %}
```

Saída esperada:

```html
<section class="block blog-posts">
  <h2>NOVIDADES DO BLOG</h2>
  <article><a href="...">Post Título</a></article>
  <article><a href="...">Outro Post</a></article>
</section>
```

## Observações

- Retorna apenas posts marcados como destaque
- Ordem pode variar; verifique com o painel
- Cache pode afetar quando novos posts aparecem
- Limite padrão é 4 posts se não especificado
- Performance: Integração leve, sem impacto

## Erros comuns

### Erro 1: Parâmetro como número em vez de string

**Problema**: `store.blogPosts({limit: 10})` (número)
**Diagnóstico**: Posts não são retornados
**Solução**: Passar como string: `{limit: '10'}`

### Erro 2: Acessar propriedade inexistente

**Problema**: `post.descricao` não existe
**Diagnóstico**: Propriedade retorna null
**Solução**: Usar propriedades corretas: `titulo`, `blog_url`, `texto`, `imagem`, `visualizacao`, `cadastro`

### Erro 3: Loop vazio quando não há posts

**Problema**: Página em branco ou seção vazia
**Diagnóstico**: Nenhum post marcado como destaque
**Solução**: Envolver em condicional `if blog_posts|length >= 1`

## Veja também

- [Visão geral store](04-store/visao-geral-store.md)
- [Cart](04-store/cart.md)
- [Featured Icon](04-store/featuredicon.md)
