---
title: "Página de categorias"
slug: "pagina-de-categorias"
doc_type: "reference"
summary: "Página que exibe produtos de uma categoria específica (nível 1, 2 ou 3) com suporte a filtros e banners."
tags: ["pagina", "categorias", "produtos", "filtros", "banner"]
related: ["04-store/pageproducts.md", "06-paginas/pagina-de-busca.md"]
---

## O que faz

A página de categorias é responsável por mostrar produtos de uma determinada categoria (nível 1, 2 ou 3). A página utiliza a variável global `page_category` para acessar todos os dados sobre a categoria, incluindo informações hierárquicas, produtos, banners e opções de filtragem.

## Sintaxe

### Acessar os dados da categoria

```twig
{% set dados = page_category %}
```

Os parâmetros disponíveis em `page_category` são os mesmos encontrados em [`store.pageProducts()`](https://doc-templates.wbuy.com.br/post/pageproducts/) com a adição da variável `page` contendo:

```text
page.title                string   - Título recomendado da página
page.cl1                  array    - Informações da categoria de nível 1
page.cl1.id               int      - ID da categoria nível 1
page.cl1.nome             string   - Nome da categoria nível 1
page.cl1.url              string   - URL da categoria nível 1
page.cl1.ordenar          string   - Campo de ordenação padrão
page.cl2                  array    - Informações da categoria de nível 2 (quando selecionada)
page.cl2.id               int      - ID da categoria nível 2
page.cl2.nome             string   - Nome da categoria nível 2
page.cl2.url              string   - URL da categoria nível 2
page.cl3                  array    - Informações da categoria de nível 3 (quando selecionada)
page.cl3.id               int      - ID da categoria nível 3
page.cl3.nome             string   - Nome da categoria nível 3
page.cl3.url              string   - URL da categoria nível 3
page.infotexto            string   - Texto informativo (disponível para nível 1)
page.banner               string   - URL do banner da página (nível 1)
page.banner_link          string   - URL de acesso do banner (nível 1)
page.banner_raw           html     - HTML pronto para inserção do banner
page.hasMenuLateral       boolean  - Se true, existem opções de filtragem
page.mobile.coluna_dupla  boolean  - Se true, mostrar 2 colunas por linha
page.seo_scripts          string   - Scripts de SEO
```

## Quando usar

- Quando deseja exibir produtos de uma categoria específica
- Quando precisa mostrar informações hierárquicas da categoria (nível 1, 2, 3)
- Quando necessita exibir filtros de refinamento de produtos
- Quando quer mostrar banners específicos da categoria
- Quando a categoria possui textos informativos que devem ser exibidos

## Exemplo

### Exemplo básico

```twig
{% set dados = page_category %}

<h1>{{ dados.page.title }}</h1>

{% if dados.page.infotexto %}
<div class="info-categoria">
    {{ dados.page.infotexto }}
</div>
{% endif %}

{% if dados.page.banner_raw %}
<div class="banner-categoria">
    {{ dados.page.banner_raw|raw }}
</div>
{% endif %}

<div class="container">
    {% if dados.page.hasMenuLateral %}
    <aside class="filtros">
        <h3>Refinar</h3>
        <!-- Opções de filtro -->
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

### Exemplo com navegação de categorias

```twig
{% set dados = page_category %}

<nav class="breadcrumb">
    <a href="/">Home</a>
    <span>/</span>
    <a href="{{ dados.page.cl1.url }}">{{ dados.page.cl1.nome }}</a>
    
    {% if dados.page.cl2 %}
    <span>/</span>
    <a href="{{ dados.page.cl2.url }}">{{ dados.page.cl2.nome }}</a>
    {% endif %}
    
    {% if dados.page.cl3 %}
    <span>/</span>
    <a href="{{ dados.page.cl3.url }}">{{ dados.page.cl3.nome }}</a>
    {% endif %}
</nav>

<h1>{{ dados.page.title }}</h1>
<!-- Conteúdo da página -->
```

## Observações

- A variável `page_category` contém os mesmos dados de `store.pageProducts()` portanto consulte a documentação dessa função para informações completas sobre paginação
- O campo `page.infotexto` está disponível apenas para categorias de nível 1
- Banners (`page.banner`, `page.banner_link`, `page.banner_raw`) estão disponíveis apenas para categorias de nível 1
- Use `page.banner_raw|raw` para renderizar o HTML do banner corretamente
- A estrutura de níveis de categoria (cl1, cl2, cl3) ajuda a criar breadcrumbs ou menus de navegação
- Se `page.hasMenuLateral` for true, existem filtros disponíveis para refinamento de resultados
- O campo `page.seo_scripts` pode conter marcações estruturadas para SEO

## Erros comuns

### Erro: Categorias não aparecem na navegação

**Problema**: Os campos `page.cl2` ou `page.cl3` estão vazios quando deveriam ter dados
**Diagnóstico**: Pode ser que o usuário acessou a categoria sem subcategorias
**Solução**: Use condicionais `{% if dados.page.cl2 %}` para verificar a existência dos dados antes de exibir

### Erro: Banner não renderiza corretamente

**Problema**: O banner aparece como texto HTML em vez de imagem formatada
**Diagnóstico**: O filtro `|raw` pode estar ausente no template
**Solução**: Certifique-se de usar `{{ dados.page.banner_raw|raw }}` para renderizar corretamente

### Erro: Filtros não aparecem apesar de `hasMenuLateral` ser true

**Problema**: `page.hasMenuLateral` indica que há filtros, mas nenhum é exibido
**Diagnóstico**: Os filtros podem estar em estrutura diferente ou requerem JavaScript específico
**Solução**: Verifique a documentação sobre filtros dinâmicos e a estrutura de dados esperada

## Veja também

- [04-store/pageproducts.md](04-store/pageproducts.md) - Método store.pageProducts() com todos os parâmetros
- [06-paginas/pagina-de-busca.md](06-paginas/pagina-de-busca.md) - Página de busca (estrutura similar)
