---
title: "Exemplo: Busca com paginação"
slug: "busca-com-paginacao"
doc_type: "example"
summary: "Página responsável por exibir produtos retornados em busca com filtros e paginação."
tags:
  - exemplos
  - busca
  - paginação
  - filtros
  - produtos
related:
  - 04-store/pageproducts.md
  - 06-paginas/pagina-de-busca.md
  - 04-store/recursos-gerais.md
---

## O que faz

Página de exemplo responsável por exibir produtos retornados em uma busca na loja virtual com suporte a filtragem lateral, ordenação e paginação de resultados. Exibe produtos em layout responsivo que se adapta para mobile com colunas duplas quando necessário.

## Sintaxe

```twig
{% set dados = page_search %}
```

A variável fixa `page_search` contém:

- Todos os parâmetros de `store.pageProducts()`
- `page.title` (string) — Termo da busca
- `page.hasMenuLateral` (boolean) — Indicador de filtros disponíveis
- `page.mobile.coluna_dupla` (boolean) — Layout duplo em mobile

## Quando usar

- Página de resultados de busca na loja
- Quando há necessidade de filtros e paginação
- Para exibir múltiplos produtos em grid responsivo
- Quando usuário faz busca por texto ou palavras-chave

## Exemplo

```twig
{% set dados = page_search %}

<div class="search-results">
  <h1>Resultados para: {{ dados.page.title }}</h1>
  
  {% if dados.page.hasMenuLateral %}
  <aside class="filters">
    <!-- Filtros disponíveis -->
  </aside>
  {% endif %}
  
  <div class="products-grid">
    {% for produto in dados.produtos %}
      <!-- Renderizar produto -->
    {% endfor %}
  </div>
  
  <!-- Paginação -->
</div>
```

Saída esperada:

```html
<div class="search-results">
  <h1>Resultados para: camiseta</h1>
  <aside class="filters"><!-- filtros --></aside>
  <div class="products-grid"><!-- produtos --></div>
</div>
```

## Observações

- Página automática da plataforma
- Filtros laterais dinâmicos baseados em categorias e atributos
- Paginação automática de resultados
- Mobile: Layout ajusta para coluna dupla quando `page.mobile.coluna_dupla` é true
- SEO: URL de busca é indexada com parâmetros de query
- Performance: Cache de resultados pode ser configurado

## Erros comuns

### Erro 1: Filtros não aparecem

**Problema**: Menu lateral vazio mesmo com `page.hasMenuLateral = true`
**Diagnóstico**: Dados de filtros não carregados
**Solução**: Verificar se há categorias ou atributos filtráveis cadastrados

### Erro 2: Paginação não funciona

**Problema**: Links de página não navegam ou não há paginação
**Diagnóstico**: Total de produtos menor que limite por página
**Solução**: Adicionar mais produtos ou reduzir itens por página

### Erro 3: Layout não fica duplo em mobile

**Problema**: `page.mobile.coluna_dupla` = true mas layout continua em coluna única
**Diagnóstico**: CSS não aplicado corretamente
**Solução**: Verificar classes de grid responsivo e media queries

## Veja também

- [store.pageProducts()](04-store/pageproducts.md) — Estrutura completa de dados
- [Página de busca](06-paginas/pagina-de-busca.md) — Documentação completa da página
- [Recursos gerais](04-store/recursos-gerais.md) — Métodos auxiliares
