---
title: "categoryGetLevel1"
slug: "categorygetlevel1"
doc_type: "reference"
summary: "Função API que recupera apenas categorias de nível 1 (categorias raiz) disponíveis na loja virtual. Ideal para menus principais e navegação de topo, quando sub-categorias são carregadas sob demanda."
tags:
  - api
  - categorias
  - server-side
  - twig
  - nível-1
  - raiz
related:
  - 03-api/categorygetall.md
  - 03-api/categorygetlevel2.md
  - 03-api/categorygetlevel3.md
  - 03-api/visao-geral-api.md
---

## O que faz

A função `categoryGetLevel1()` busca na API apenas as categorias de **nível 1** (categorias raiz) disponíveis na loja virtual. Diferencia-se de `categoryGetAll()` porque retorna apenas o primeiro nível da hierarquia, sem sub-categorias aninhadas.

Ideal para renderizar menus principais e navegação de topo, quando sub-categorias serão carregadas sob demanda (via AJAX ou em páginas separadas).

## Sintaxe

```twig
{# Sem parâmetros - retorna todas as categorias de nível 1 #}
{% set categorias = api.categoryGetLevel1() %}

{# Com parâmetros de consulta - filtra resultados #}
{% set categorias = api.categoryGetLevel1({id:'1', q:'eletronicos'}) %}
```

### Parâmetros

A função aceita parâmetros no formato JSON dentro de chaves `{}`:

- `id` — ID específico para filtrar categoria (string ou número)
- `q` — Query de busca para filtrar por nome/descrição (string)

Todos os parâmetros possíveis estão documentados na [API Postman](https://documenter.getpostman.com/view/4141833/RWTsquyN).

### Retorno

Retorna um array com objetos de categoria nível 1. Cada objeto contém:

- Dados da categoria (`id`, `nome`, `url`, `ordenar` etc)
- URLs e metadados da categoria
- **Sem sub-categorias aninhadas** (apenas nível 1)

#### Exemplo de estrutura retornada

```json
// Retorna uma lista de objetos, como o seguinte:
[
  {
    "id": 343564,
    "tipo": 2,
    "tabela": 1,
    "nome": "coleções",
    "url": "colecoes",
    "icone_tipo": 1,
    "icone": "",
    "cor": "",
    "posicao": 0,
    "menu": 1,
    "menu_mobile": 1,
    "ativo": 1,
    "oculto": 0,
    "ordenar": "lancamento",
    "categoria_link": "http://www.loja.com.br/link/da/categoria",
    "google_category": "",
    "categoria_target": "_self",
    "total_produtos": 0,
    "filtro_preco": 50,
    "subtitulo": "",
    "seo_title": "",
    "seo_description": "",
    "seo_metatags": "",
    "seo_info": "",
    "seo_scripts": "",
    "total_level2": 0,
    "total_produtos_ativos": 0
  },
]
```

## Quando usar

- Renderizar **menu de navegação principal** (header/top menu)
- Criar **abas de categorias** no topo da página
- Listar **categorias de primeiro nível** sem sub-itens
- Quando sub-categorias serão **carregadas depois via AJAX**
- Performance é crítica — reduz tamanho de dados retornados

### Pré-condições

- Categorias nível 1 devem estar cadastradas e ativas
- Deve haver acesso ao objeto `api` no contexto Twig
- Para menus interativos, prepare AJAX para carregar níveis 2/3 sob demanda

### Limitações

- Retorna **apenas nível 1** — não inclui sub-categorias
- Para estrutura completa, use `categoryGetAll()` em vez disso
- Sub-categorias precisam ser carregadas em chamadas separadas

## Exemplo

```twig
{# Arquivo: templates/header-menu.twig #}
<header class="main-header">
  <nav class="main-menu">
    {% for category in api.categoryGetLevel1() %}
      <div class="menu-item">
        <a href="/categoria/{{ category.slug }}" class="menu-link">
          {{ category.name }}
        </a>
        {# Sub-menu será carregado via AJAX ao hover #}
        <ul class="submenu" data-category-id="{{ category.id }}"></ul>
      </div>
    {% endfor %}
  </nav>
</header>

<script>
// Carregar nível 2 sob demanda ao hover
$('.menu-item').on('mouseover', function() {
  var categoryId = $(this).find('.submenu').data('category-id');
  if ($(this).find('.submenu li').length === 0) {
    $.ajax({
      url: '/api/v1/category/level2',
      data: { parent_id: categoryId },
      success: function(data) {
        // Renderizar sub-menu
      }
    });
  }
});
</script>
```

Saída esperada (HTML):

```html
<header class="main-header">
  <nav class="main-menu">
    <div class="menu-item">
      <a href="/categoria/eletronicos" class="menu-link">
        Eletrônicos
      </a>
      <ul class="submenu" data-category-id="1"></ul>
    </div>
    <div class="menu-item">
      <a href="/categoria/livros" class="menu-link">
        Livros
      </a>
      <ul class="submenu" data-category-id="2"></ul>
    </div>
  </nav>
</header>
```

## Observações

### Performance

- `categoryGetLevel1()` é **muito leve** comparado a `categoryGetAll()` — retorna apenas nível 1
- Ideal para renderizar **header menu rápido** sem esperar sub-categorias
- Use **short-lived cache** (5-10 minutos) pois categorias raiz mudam raramente

### Cache

- Resultado é **candidato para cache de curta duração** (5-60 minutos)
- Invalidar cache quando: categorias nível 1 são criadas, deletadas ou modificadas
- Combinar com **AJAX lazy-loading** de níveis 2/3 para otimização

### Segurança

- Dados públicos — sem risco de expor dados sensíveis
- Nenhuma autenticação necessária

### Impacto SEO e Mobile

- Renderizado **server-side** — crawlable por bots
- Em mobile, considere **vertical menu com collapse** em vez de horizontal
- Boa para **breadcrumb schema** e navegação estruturada

## Erros comuns

### Erro frequente 1: "Menu fica vazio ou sem categorias"

**Problema**: `api.categoryGetLevel1()` retorna array vazio, menu não renderiza.
**Diagnóstico**: Nenhuma categoria nível 1 cadastrada, ou API está retornando erro silencioso.
**Solução**: Verificar no painel wBuy se existem categorias. Se sim, debugar com `{{ pr(api.categoryGetLevel1()) }}` para ver resposta real.

### Erro frequente 2: "Sub-categorias aparecem mas não deviam aparecer"

**Problema**: Resultado de `categoryGetLevel1()` contém sub-categorias aninhadas.
**Diagnóstico**: API pode estar retornando mais dados que esperado. Verificar estrutura com `{{ pr(category.subcategories) }}`.
**Solução**: Usar template para ignorar sub-categorias: `{% if not category.subcategories %}` ou usar `categoryGetLevel1()` que deve retornar apenas nível 1 puro.

### Erro frequente 3: "AJAX de sub-menu falha ou não carrega"

**Problema**: Ao passar mouse sobre item do menu, sub-menu não carrega via AJAX.
**Diagnóstico**: Verificar console do navegador para erros de CORS, URL incorreta ou dados inválidos.
**Solução**: Usar DevTools > Network para inspecionar requisição. Garantir que URL de AJAX coincide com endpoint real. Validar se categoria_id está sendo passado corretamente.

## Veja também

- [categoryGetAll](./categorygetall.md) — Todas as categorias e sub-categorias
- [categoryGetLevel2](./categorygetlevel2.md) — Apenas categorias nível 2
- [categoryGetLevel3](./categorygetlevel3.md) — Apenas categorias nível 3
- [Visão geral da API](./visao-geral-api.md) — Contexto e diferenças server-side vs client-side
