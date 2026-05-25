---
title: "Página de busca"
slug: "pagina-de-busca"
doc_type: "reference"
summary: "Página que exibe os produtos retornados pela busca realizada na loja virtual."
tags: ["pagina", "busca", "produtos", "filtros"]
related: ["04-store/pageproducts.md", "06-paginas/pagina-de-categorias.md"]
---

## O que faz

A página de busca é responsável por mostrar os produtos retornados quando um usuário realiza uma busca na loja virtual. A página utiliza a variável global `page_search` para acessar todos os dados sobre os resultados da busca, incluindo o termo de busca, produtos encontrados, opções de filtragem e configurações de exibição.

## Sintaxe

### Acessar os dados da busca

```twig
{% set dados = page_search %}
```

Os parâmetros disponíveis em `page_search` são os mesmos encontrados em [`store.pageProducts()`](https://doc-templates.wbuy.com.br/post/pageproducts/) com a adição da variável `page` contendo:

```text
page.title                string   - Termo que foi usado na busca
page.hasMenuLateral       boolean  - Se true, existem opções a serem exibidas para filtragem
page.mobile.coluna_dupla  boolean  - Se true, mostrar 2 colunas por linha no mobile
```

## Quando usar

- Quando deseja exibir resultados de uma busca realizada pelo usuário
- Quando precisa mostrar o termo de busca utilizado
- Quando necessita exibir filtros de refinamento de resultados
- Quando quer adaptar a exibição de produtos para dispositivos mobile (2 colunas)

## Exemplo

### Exemplo básico

```twig
{% set dados = page_search %}

<h1>Resultados para: <strong>{{ dados.page.title }}</strong></h1>

<div class="container">
    {% if dados.page.hasMenuLateral %}
    <aside class="filtros">
        <h3>Refinar busca</h3>
        <!-- Filtros disponíveis -->
    </aside>
    {% endif %}
    
    <main class="produtos-container">
        {% if dados.produtos|length > 0 %}
            <div class="produtos-grid">
                {% for produto in dados.produtos %}
                    <div class="produto">
                        <h2>{{ produto.nome }}</h2>
                        <p class="preco">{{ produto.preco }}</p>
                    </div>
                {% endfor %}
            </div>
        {% else %}
            <p class="sem-resultados">Nenhum produto encontrado para sua busca.</p>
        {% endif %}
    </main>
</div>
```

### Exemplo com responsivo para mobile

```twig
{% set dados = page_search %}

<div class="busca-resultados">
    <h1>{{ dados.page.title }}</h1>
    
    <div class="layout-container {% if dados.page.mobile.coluna_dupla %}duas-colunas-mobile{% endif %}">
        {% if dados.page.hasMenuLateral %}
        <aside class="filtros-sidebar">
            <!-- Menu de filtros -->
        </aside>
        {% endif %}
        
        <section class="lista-produtos">
            {% for produto in dados.produtos %}
                <article class="item-produto">
                    <img src="{{ produto.imagem }}" alt="{{ produto.nome }}">
                    <h3>{{ produto.nome }}</h3>
                </article>
            {% endfor %}
        </section>
    </div>
</div>
```

## Observações

- A variável `page_search` contém os mesmos dados de `store.pageProducts()` portanto consulte a documentação dessa função para informações completas sobre paginação e outros parâmetros
- O campo `page.title` contém o termo exato que foi buscado
- Se `page.hasMenuLateral` for true, existem filtros disponíveis que refinam os resultados da busca
- A propriedade `page.mobile.coluna_dupla` indica se deve usar layout responsivo com 2 colunas no mobile
- Quando não há resultados, a array `dados.produtos` será vazia
- A página deve informar ao usuário quando nenhum produto for encontrado

## Erros comuns

### Erro: Dados de busca não aparecem

**Problema**: A variável `page_search` retorna valores vazios ou o termo não aparece
**Diagnóstico**: A busca pode não ter sido realizada corretamente ou o parâmetro de busca não foi passado
**Solução**: Verifique se o formulário de busca está enviando corretamente o termo e se a página está recebendo os dados

### Erro: Produtos não aparecem mesmo com resultados

**Problema**: `dados.produtos` está vazio apesar da busca ter retornado resultados
**Diagnóstico**: Pode haver paginação ou limite de resultados
**Solução**: Verifique a paginação em `store.pageProducts()` e ajuste os parâmetros de limite de itens por página

### Erro: Filtros não aparecem

**Problema**: `page.hasMenuLateral` é false ou os filtros não são exibidos
**Diagnóstico**: A categoria ou busca pode não ter filtros disponíveis
**Solução**: Verifique se a busca retornou produtos de categorias que possuem filtros configurados no painel

## Veja também

- [04-store/pageproducts.md](04-store/pageproducts.md) - Método store.pageProducts() com todos os parâmetros
- [06-paginas/pagina-de-categorias.md](06-paginas/pagina-de-categorias.md) - Página de categorias (estrutura similar)
