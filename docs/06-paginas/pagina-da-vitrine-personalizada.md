---
title: "Página da Vitrine Personalizada"
slug: "pagina-da-vitrine-personalizada"
doc_type: "reference"
summary: "Página para exibir produtos de uma vitrine personalizada criada no painel de controle do wBuy."
tags: ["pagina", "vitrine", "produtos", "personalizada"]
related: ["04-store/pageproducts.md", "06-paginas/pagina-de-categorias.md"]
---

## O que faz

A página da vitrine personalizada é responsável por mostrar produtos de uma vitrine customizada criada em Painel de controle > Marketing > Vitrine personalizada. A página utiliza a variável global `page_custom_showcase` para acessar todos os dados sobre a vitrine, incluindo seus produtos, informações, banners e configurações de exibição.

## Sintaxe

### Acessar os dados da vitrine

```twig
{% set dados = page_custom_showcase %}
```

Os parâmetros disponíveis em `page_custom_showcase` são os mesmos encontrados em [`store.pageProducts()`](https://doc-templates.wbuy.com.br/post/pageproducts/) com a adição da variável `page` contendo:

```text
page.title                string   - Título recomendado da página
page.vitrine              array    - Dados da vitrine
page.vitrine.nome         string   - Nome da vitrine
page.vitrine.vitrine_url  string   - URL da vitrine
page.infotexto            string   - Texto informativo da página
page.hasMenuLateral       boolean  - Se true, exibe opções de filtragem
page.mobile.coluna_dupla  boolean  - Se true, mostrar 2 colunas por linha no mobile
page.banner_raw           html     - HTML dos banners desktop e mobile
```

## Quando usar

- Quando deseja exibir uma vitrine personalizada criada no painel de controle
- Quando precisa mostrar produtos com banners específicos da vitrine
- Quando a vitrine possui informações adicionais (textos, logos, etc.) que devem ser exibidas
- Quando necessita adaptar a exibição de produtos para dispositivos mobile (2 colunas)

## Exemplo

### Exemplo básico

```twig
{% set dados = page_custom_showcase %}

<h1>{{ dados.page.title }}</h1>

{% if dados.page.infotexto %}
<div class="info-texto">
    {{ dados.page.infotexto }}
</div>
{% endif %}

<div class="vitrine-header">
    <h2>{{ dados.page.vitrine.nome }}</h2>
</div>

{% if dados.page.banner_raw %}
<div class="banners">
    {{ dados.page.banner_raw|raw }}
</div>
{% endif %}

<div class="produtos">
    {% for produto in dados.produtos %}
        <div class="produto">
            <h3>{{ produto.nome }}</h3>
            <p>{{ produto.preco }}</p>
        </div>
    {% endfor %}
</div>
```

### Exemplo com menu lateral de filtros

```twig
{% set dados = page_custom_showcase %}

<div class="container">
    {% if dados.page.hasMenuLateral %}
    <aside class="filtros">
        <!-- Adicionar filtros disponíveis -->
    </aside>
    {% endif %}
    
    <main class="conteudo">
        <h1>{{ dados.page.title }}</h1>
        <!-- Exibir produtos -->
    </main>
</div>
```

## Observações

- A variável `page_custom_showcase` contém os mesmos dados de `store.pageProducts()` portanto consulte a documentação dessa função para informações completas sobre paginação e filtros
- O campo `page.banner_raw` já vem formatado como HTML pronto para inserção, utilize o filtro `|raw` para renderizá-lo
- A propriedade `page.mobile.coluna_dupla` indica se deve usar layout responsivo com 2 colunas no mobile
- Se `page.hasMenuLateral` for true, existem filtros disponíveis para exibição
- O texto informativo (`page.infotexto`) pode conter HTML formatado
- A vitrine pode estar vazia se nenhum produto foi associado a ela no painel

## Erros comuns

### Erro: Dados da vitrine não aparecem

**Problema**: A variável `page_custom_showcase` retorna valores vazios ou nulos
**Diagnóstico**: A vitrine pode não ter sido criada corretamente no painel ou não tem produtos associados
**Solução**: Verifique se a vitrine foi criada em Marketing > Vitrine personalizada e se possui produtos vinculados

### Erro: Banner não renderiza

**Problema**: O `page.banner_raw|raw` mostra HTML como texto
**Diagnóstico**: O filtro `|raw` pode estar ausente ou o HTML está incorreto
**Solução**: Certifique-se de usar `{{ dados.page.banner_raw|raw }}` e não apenas `{{ dados.page.banner_raw }}`

### Erro: Produtos não aparecem em 2 colunas no mobile

**Problema**: A variável `page.mobile.coluna_dupla` está true mas a exibição não segue esse padrão
**Diagnóstico**: CSS de media queries pode estar conflitando
**Solução**: Verifique se o CSS para mobile está aplicando corretamente as classes de coluna

## Veja também

- [04-store/pageproducts.md](04-store/pageproducts.md) - Método store.pageProducts() com dados completos
- [06-paginas/pagina-de-categorias.md](06-paginas/pagina-de-categorias.md) - Página de categorias (estrutura similar)
