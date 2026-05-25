---
title: "Página de produtos de uma Filial (Multiloja)"
slug: "pagina-de-produtos-de-uma-filial-multiloja"
doc_type: "reference"
summary: "Página que exibe produtos de uma filial específica em ambiente de multiloja, com informações e branding da filial."
tags: ["pagina", "filial", "multiloja", "produtos", "filtros"]
related: ["04-store/pageproducts.md", "06-paginas/pagina-de-categorias.md"]
---

## O que faz

A página de produtos de uma filial é responsável por mostrar os produtos de uma determinada filial ligada à matriz em um ambiente de multiloja. A página utiliza a variável global `page_filial` para acessar todos os dados sobre a filial, seus produtos, informações de contato e banners específicos.

## Sintaxe

### Acessar os dados da filial

```twig
{% set dados = page_filial %}
```

Os parâmetros disponíveis em `page_filial` são os mesmos encontrados em [`store.pageProducts()`](https://doc-templates.wbuy.com.br/post/pageproducts/) com a adição da variável `page` contendo:

```text
page.title                string   - Título recomendado da página
page.filial               array    - Detalhes da filial
page.filial.logo          string   - Logo da filial
page.filial.banner        string   - Banner desktop da filial
page.filial.banner_mobile string   - Banner mobile da filial
page.filial.nome          string   - Nome da filial
page.filial.cidade        string   - Cidade da filial
page.filial.uf            string   - Estado (UF) da filial
page.filial.url           string   - URL do site da Matriz dentro da wBuy
page.filial.url_interna_matriz string - URL da página da filial dentro da loja matriz
page.hasMenuLateral       boolean  - Se true, existem opções para filtragem
page.mobile.coluna_dupla  boolean  - Se true, mostrar 2 colunas por linha
```

## Quando usar

- Quando deseja exibir produtos de uma filial específica em um ambiente multiloja
- Quando precisa mostrar informações e branding da filial
- Quando necessita exibir localização (cidade e estado) da filial
- Quando quer permitir filtros de produtos por filial
- Quando a filial possui banners e logos específicos

## Exemplo

### Exemplo básico com informações da filial

```twig
{% set dados = page_filial %}

<div class="filial-header">
    {% if dados.page.filial.logo %}
    <img src="{{ dados.page.filial.logo }}" alt="{{ dados.page.filial.nome }}" class="filial-logo">
    {% endif %}
    
    <h1>{{ dados.page.title }}</h1>
    
    <div class="filial-info">
        <p><strong>{{ dados.page.filial.nome }}</strong></p>
        <p>{{ dados.page.filial.cidade }}, {{ dados.page.filial.uf }}</p>
    </div>
</div>

{% if dados.page.filial.banner %}
<div class="filial-banner">
    <img src="{{ dados.page.filial.banner }}" alt="Banner da {{ dados.page.filial.nome }}">
</div>
{% endif %}

<div class="container">
    {% if dados.page.hasMenuLateral %}
    <aside class="filtros">
        <h3>Refinar busca</h3>
        <!-- Filtros disponíveis -->
    </aside>
    {% endif %}
    
    <main class="produtos-container">
        <div class="produtos-grid">
            {% for produto in dados.produtos %}
                <div class="produto">
                    <h3>{{ produto.nome }}</h3>
                    <span class="preco">{{ produto.preco }}</span>
                </div>
            {% endfor %}
        </div>
    </main>
</div>
```

### Exemplo com responsivo para mobile

```twig
{% set dados = page_filial %}

<header class="filial-cabecalho">
    <div class="filial-branding">
        {% if dados.page.filial.logo %}
        <img src="{{ dados.page.filial.logo }}" alt="{{ dados.page.filial.nome }}" class="logo-filial">
        {% endif %}
        <h1>{{ dados.page.title }}</h1>
    </div>
    
    {% if dados.page.filial.banner_mobile %}
    <img src="{{ dados.page.filial.banner_mobile }}" alt="Banner" class="banner-mobile">
    {% else if dados.page.filial.banner %}
    <img src="{{ dados.page.filial.banner }}" alt="Banner" class="banner-desktop">
    {% endif %}
</header>

<div class="layout {% if dados.page.mobile.coluna_dupla %}duas-colunas-mobile{% endif %}">
    {% if dados.page.hasMenuLateral %}
    <aside class="sidebar-filtros">
        <!-- Filtros -->
    </aside>
    {% endif %}
    
    <section class="lista-produtos">
        {% for produto in dados.produtos %}
            <article class="item-produto">
                <h3>{{ produto.nome }}</h3>
            </article>
        {% endfor %}
    </section>
</div>
```

## Observações

- A variável `page_filial` contém os mesmos dados de `store.pageProducts()` portanto consulte a documentação dessa função para paginação e filtros completos
- O campo `page.filial` contém informações importantes para identificar e divulgar a filial
- Banners específicos para desktop (`banner`) e mobile (`banner_mobile`) podem ser utilizados para criar layouts responsivos
- A propriedade `page.mobile.coluna_dupla` indica se deve usar layout com 2 colunas no mobile
- Se `page.hasMenuLateral` for true, existem filtros disponíveis para refinamento de resultados
- As URLs fornecidas (`url` e `url_interna_matriz`) podem ser utilizadas para navegação entre filiais ou volta à matriz

## Erros comuns

### Erro: Informações da filial não aparecem

**Problema**: Os dados de `page.filial` estão vazios ou não são exibidos
**Diagnóstico**: A filial pode não ter sido configurada corretamente no painel de multiloja
**Solução**: Verifique se a filial foi criada e vinculada corretamente no painel de controle

### Erro: Banner não exibe corretamente

**Problema**: Imagem do banner não carrega ou aparece quebrada
**Diagnóstico**: A URL da imagem pode estar incorreta ou a imagem foi removida
**Solução**: Verifique a URL do banner no painel e confirme se a imagem existe e está acessível

### Erro: Layout responsivo não funciona

**Problema**: `page.mobile.coluna_dupla` é true mas as 2 colunas não aparecem no mobile
**Diagnóstico**: CSS de media queries pode estar com conflito ou não estar aplicado
**Solução**: Verifique se as classes CSS para mobile estão definidas corretamente

## Veja também

- [04-store/pageproducts.md](04-store/pageproducts.md) - Método store.pageProducts() com todos os parâmetros
- [06-paginas/pagina-de-categorias.md](06-paginas/pagina-de-categorias.md) - Página de categorias (estrutura similar)
