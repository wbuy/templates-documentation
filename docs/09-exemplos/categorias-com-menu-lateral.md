---
title: "Exemplo: Categorias com menu lateral"
slug: "categorias-com-menu-lateral"
doc_type: "example"
summary: "Página que exibe produtos de uma categoria com menu lateral de filtragem e navegação."
tags:
  - exemplos
  - categorias
  - menu
  - filtros
  - produtos
related:
  - 06-paginas/pagina-de-categorias.md
  - 04-store/pageproducts.md
  - 04-store/store-categoriesmenu.md
---

## O que faz

Página de exemplo que exibe produtos de uma categoria específica (nível 1, 2 ou 3) com menu lateral de filtragem e navegação. Inclui banner informativo, texto descritivo da categoria e lista de produtos em layout responsivo com suporte a paginação.

## Sintaxe

```twig
{% set dados = page_category %}
```

A variável fixa `page_category` contém:

- Todos os parâmetros de `store.pageProducts()`
- `page.title` (string) — Título da categoria
- `page.cl1`, `page.cl2`, `page.cl3` (array) — Dados das categorias de nível 1, 2 e 3
- `page.infotexto` (string) — Descrição da categoria (nível 1)
- `page.banner_raw` (string) — Banner formatado para renderização
- `page.hasMenuLateral` (boolean) — Indicador de filtros disponíveis
- `page.mobile.coluna_dupla` (boolean) — Layout duplo em mobile

## Quando usar

- Página de categoria de produtos
- Para exibir produtos com filtros por atributos
- Quando há banner promocional específico da categoria
- Para navegação hierárquica (nível 1, 2, 3)

## Exemplo

```twig
{% set dados = page_category %}

<div class="category-page">
  <h1>{{ dados.page.title }}</h1>
  
  {% if dados.page.banner_raw %}
    <div class="category-banner">
      {{ dados.page.banner_raw|raw }}
    </div>
  {% endif %}
  
  {% if dados.page.infotexto %}
    <div class="category-info">
      {{ dados.page.infotexto }}
    </div>
  {% endif %}
  
  <div class="category-content">
    {% if dados.page.hasMenuLateral %}
      <aside class="filters"><!-- Menu de filtros --></aside>
    {% endif %}
    
    <div class="products-grid">
      {% for produto in dados.produtos %}
        <!-- Renderizar produto -->
      {% endfor %}
    </div>
  </div>
</div>
```

Saída esperada:
```html
<div class="category-page">
  <h1>Eletrônicos</h1>
  <div class="category-banner"><!-- imagem do banner --></div>
  <div class="category-info">Descrição da categoria...</div>
  <div class="category-content"><!-- filtros e produtos --></div>
</div>
```

## Observações

- Página automática da plataforma
- Categorias hierárquicas: nível 1, 2 e 3
- Banner e descrição disponíveis apenas para categorias nível 1
- Menu lateral com filtros dinâmicos
- Mobile: Layout ajusta para 2 colunas quando `page.mobile.coluna_dupla` é true
- SEO: URL amigável com slug da categoria
- Performance: Cache de categoria configurável

## Erros comuns

### Erro 1: Banner não aparece

**Problema**: `page.banner_raw` vazio mesmo com banner cadastrado
**Diagnóstico**: Banner não associado a categoria ou URL inválida
**Solução**: Verificar configurações de banner no painel da categoria

### Erro 2: Subcategorias (nível 2 e 3) não exibem

**Problema**: `page.cl2` ou `page.cl3` estão vazios
**Diagnóstico**: Subcategorias não criadas ou não associadas
**Solução**: Criar e associar subcategorias no painel de controle

### Erro 3: Menu lateral de filtros não funciona

**Problema**: `page.hasMenuLateral = true` mas filtros não aplicam
**Diagnóstico**: Atributos não configurados como filtráveis
**Solução**: Habilitar atributos como filtros na configuração da loja

## Veja também

- [Página de categorias](06-paginas/pagina-de-categorias.md) — Documentação completa
- [store.pageProducts()](04-store/pageproducts.md) — Estrutura de dados
- [store.categoriesmenu()](04-store/store-categoriesmenu.md) — Menu de categorias
