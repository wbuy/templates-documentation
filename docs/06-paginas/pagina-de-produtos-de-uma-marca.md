---
title: "Página de produtos de uma Marca"
slug: "pagina-de-produtos-de-uma-marca"
doc_type: "reference"
summary: "Página que exibe todos os produtos de uma marca específica com suporte a filtros e navegação."
tags: ["pagina", "marca", "produtos", "filtros"]
related: ["04-store/pageproducts.md", "06-paginas/pagina-de-categorias.md", "06-paginas/pagina-de-busca.md"]
---

## O que faz

A página de produtos de uma marca é responsável por mostrar todos os produtos de uma marca específica. A página utiliza a variável global `page_brand` para acessar os dados sobre a marca, seus produtos e opções de filtragem.

## Sintaxe

### Acessar os dados da marca

```twig
{% set dados = page_brand %}
```

Os parâmetros disponíveis em `page_brand` são os mesmos encontrados em [`store.pageProducts()`](https://doc-templates.wbuy.com.br/post/pageproducts/) com a adição da variável `page` contendo:

```text
page.title                string   - Título recomendado da página
page.marca                array    - Detalhes da marca em questão
page.marca.nome           string   - Nome da marca
page.marca.marca_url      string   - URL da marca
page.marca.logo_url       string   - URL do logo da marca
page.hasMenuLateral       boolean  - Se true, existem opções para filtragem
page.mobile.coluna_dupla  boolean  - Se true, mostrar 2 colunas por linha
```

## Quando usar

- Quando deseja exibir todos os produtos de uma marca específica
- Quando precisa permitir filtragem de produtos dentro de uma marca
- Quando necessita criar uma página de marca com branding visual próprio
- Quando quer adaptar a exibição de produtos para dispositivos mobile (2 colunas)

## Exemplo

### Exemplo básico

```twig
{% set dados = page_brand %}

<h1>{{ dados.page.title }}</h1>

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
                        <img src="{{ produto.imagem }}" alt="{{ produto.nome }}">
                        <h3>{{ produto.nome }}</h3>
                        <span class="preco">{{ produto.preco }}</span>
                    </div>
                {% endfor %}
            </div>
        {% else %}
            <p>Nenhum produto encontrado desta marca.</p>
        {% endif %}
    </main>
</div>
```

### Exemplo com branding da marca

```twig
{% set dados = page_brand %}

<header class="marca-cabecalho">
    {% if dados.page.marca.logo_url %}
    <img src="{{ dados.page.marca.logo_url }}" alt="{{ dados.page.marca.nome }}" class="logo-marca">
    {% endif %}
    
    <h1>{{ dados.page.marca.nome }}</h1>
    <p class="descricao-marca">Todos os produtos de {{ dados.page.marca.nome }}</p>
</header>

<div class="layout-marca {% if dados.page.mobile.coluna_dupla %}duas-colunas-mobile{% endif %}">
    {% if dados.page.hasMenuLateral %}
    <aside class="sidebar-filtros">
        <!-- Filtros de categoria, preço, etc -->
    </aside>
    {% endif %}
    
    <section class="lista-produtos-marca">
        {% for produto in dados.produtos %}
            <article class="item-produto">
                <h3>{{ produto.nome }}</h3>
                <p class="preco">{{ produto.preco }}</p>
            </article>
        {% endfor %}
    </section>
</div>
```

## Observações

- A variável `page_brand` contém os mesmos dados de `store.pageProducts()` portanto consulte a documentação dessa função para paginação e filtros completos
- O campo `page.marca` contém informações identificáveis da marca incluindo logo
- Se `page.hasMenuLateral` for true, existem filtros disponíveis para refinamento de resultados (categorias, preço, etc.)
- A propriedade `page.mobile.coluna_dupla` indica se deve usar layout responsivo com 2 colunas no mobile
- Quando não há produtos da marca, `dados.produtos` será uma array vazia

## Erros comuns

### Erro: Marca não aparece no cabeçalho

**Problema**: `page_brand` ou `page.marca.nome` retorna valores vazios
**Diagnóstico**: A marca pode não ter sido configurada corretamente ou não possui produtos
**Solução**: Verifique se a marca foi criada e se possui produtos vinculados no painel de administração

### Erro: Logo da marca não aparece

**Problema**: `page.marca.logo_url` retorna null ou URL inválida
**Diagnóstico**: A marca pode não ter logo configurada
**Solução**: Faça upload do logo da marca no painel de controle ou remova a exibição do logo se não for obrigatória

### Erro: Produtos não aparecem

**Problema**: `dados.produtos` está vazio mesmo com produtos da marca cadastrados
**Diagnóstico**: Os produtos podem não estar vinculados à marca ou há restrição de visibilidade
**Solução**: Verifique se os produtos estão ativos e vinculados à marca no painel de controle

## Veja também

- [04-store/pageproducts.md](04-store/pageproducts.md) - Método store.pageProducts() com todos os parâmetros
- [06-paginas/pagina-de-categorias.md](06-paginas/pagina-de-categorias.md) - Página de categorias (estrutura similar)
- [06-paginas/pagina-de-busca.md](06-paginas/pagina-de-busca.md) - Página de busca (estrutura similar)
