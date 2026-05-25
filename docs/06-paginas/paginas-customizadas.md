---
title: "Páginas customizadas"
slug: "paginas-customizadas"
doc_type: "how-to"
summary: "Criar páginas personalizadas com conteúdo editável pelo tema através do painel de edição do wBuy."
tags: ["pagina", "customizacao", "criar", "url", "twig"]
related: ["06-paginas/visao-geral-paginas.md", "02-twig/visao-geral-twig.md"]
---

## O que faz

As páginas customizadas permitem criar páginas personalizadas cujo conteúdo seja editável apenas pelo tema. Diferentemente das páginas pré-definidas (categorias, busca, produto), as páginas customizadas oferecem total liberdade para estruturar conteúdo único na loja, como landing pages, páginas de promoções ou conteúdo editorial.

## Sintaxe

Não existe sintaxe específica padrão para páginas customizadas, pois cada página é totalmente customizável. A estrutura geral segue o padrão Twig:

```twig
{# Exemplo de página customizada básica #}
<html>
<head>
    <title>{{ page.title }}</title>
</head>
<body>
    <h1>{{ page.title }}</h1>
    <div class="conteudo">
        {{ page.conteudo|raw }}
    </div>
    
    {% for item in page.items %}
        <div class="item">
            <h2>{{ item.titulo }}</h2>
            <p>{{ item.descricao }}</p>
        </div>
    {% endfor %}
</body>
</html>
```

## Quando usar

- Para criar pages personalizadas com URLs customizadas
- Para landing pages de campanhas específicas
- Para páginas de conteúdo editorial ou informativo
- Para páginas de promoções sazonais
- Para páginas de contato, sobre nós ou similar
- Para vitrines personalizadas que não são as vitrines padrão
- Quando precisa combinar múltiplos recursos em uma única página

## Exemplo

### Passo 1: Criar a página no painel

Acesse o painel de edição do tema e siga estes passos:

1. Clique em **Novo**
2. Selecione **Nova Página Customizada**
3. Defina o **nome** da página
4. Defina a **URL** correspondente
5. Salve

### Passo 2: Estrutura da página

```twig
<div class="pagina-customizada">
    <h1>{{ page.titulo }}</h1>
    
    <div class="conteudo-principal">
        {{ page.conteudo|raw }}
    </div>
    
    {% if page.banner %}
    <div class="banner-secao">
        <img src="{{ page.banner }}" alt="Banner">
    </div>
    {% endif %}
</div>
```

### Exemplo: Página de promoção

```twig
<main class="promocao-page">
    <header class="hero">
        <h1>{{ page.titulo_promocao }}</h1>
        <p class="descricao">{{ page.descricao_promocao }}</p>
    </header>
    
    {% for produto_id in page.produtos_destacados %}
    {% set produto = api.productGet(produto_id) %}
    <div class="produto-destaque">
        <h2>{{ produto.nome }}</h2>
        <span class="preco">{{ produto.preco }}</span>
    </div>
    {% endfor %}
</main>
```

### Exemplo: Página com múltiplas seções

```twig
<article class="pagina-conteudo">
    {% for secao in page.secoes %}
    <section class="secao">
        <h2>{{ secao.titulo }}</h2>
        <p>{{ secao.descricao }}</p>
        
        {% if secao.imagem %}
        <img src="{{ secao.imagem }}" alt="{{ secao.titulo }}">
        {% endif %}
    </section>
    {% endfor %}
</article>
```

## Observações

- A URL escolhida **não pode entrar em conflito** com URLs já existentes (categorias, produtos, outras páginas customizadas)
- Use URLs únicas e descritivas em formato amigável (ex: `/promocao-verao-2024`)
- As páginas customizadas têm conteúdo **editável apenas pelo tema**, não são editáveis pelo usuário
- Você tem acesso a todas as variáveis e funções disponíveis do Twig (store, api, etc.)
- O arquivo deve estar em **codificação ISO-8859-1** quando salvo via wBuy Watcher
- Recomenda-se criar **widgets reutilizáveis** para componentes que se repetem
- Adicione metatags e dados estruturados para **SEO** quando necessário
- Certifique-se de testar a página em **diferentes dispositivos** para responsividade
- A página criada estará acessível na URL definida assim que salva

## Erros comuns

### Erro: Conflito de URL

**Problema**: Ao tentar criar a página, recebe erro sobre URL já existente
**Diagnóstico**: A URL escolhida já é utilizada por uma categoria, produto ou outra página
**Solução**: Escolha uma URL única que não conflite com URLs já existentes na loja

### Erro: Página não aparece no site

**Problema**: A página foi criada mas não abre quando acessa a URL
**Diagnóstico**: A página pode não ter sido salva corretamente ou a URL está incorreta
**Solução**: Verifique se a página foi salva no painel e acesse usando a URL exata definida

### Erro: Conteúdo dinâmico não carrega

**Problema**: Dados de API ou store não são exibidos
**Diagnóstico**: As funções podem estar retornando null ou a sintaxe Twig está incorreta
**Solução**: Use `pr(api.categoryGetAll())` para debugar os dados e verifique a sintaxe Twig

### Erro: Página responsiva não funciona no mobile

**Problema**: Layout correto no desktop mas quebrado no mobile
**Diagnóstico**: CSS não está sendo carregado ou media queries não estão definidas
**Solução**: Verifique se os estilos CSS estão incluídos corretamente e confirme breakpoints

## Veja também

- [06-paginas/visao-geral-paginas.md](06-paginas/visao-geral-paginas.md) - Visão geral de páginas customizáveis
- [02-twig/visao-geral-twig.md](02-twig/visao-geral-twig.md) - Introdução ao Twig
- [01-introducao/por-onde-comecar.md](01-introducao/por-onde-comecar.md) - Por onde começar
