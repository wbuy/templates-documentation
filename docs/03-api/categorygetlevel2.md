---
title: "categoryGetLevel2"
slug: "categorygetlevel2"
doc_type: "reference"
summary: "Função API que recupera apenas categorias de nível 2 (sub-categorias) disponíveis na loja virtual. Ideal para menus em cascata, páginas de categoria e navegação secundária."
tags:
  - api
  - categorias
  - server-side
  - twig
  - nível-2
  - subcategorias
related:
  - 03-api/categorygetall.md
  - 03-api/categorygetlevel1.md
  - 03-api/categorygetlevel3.md
  - 03-api/visao-geral-api.md
---

## O que faz

A função `categoryGetLevel2()` busca na API apenas as categorias de **nível 2** (sub-categorias/categorias secundárias) disponíveis na loja virtual. Complementa `categoryGetLevel1()` para criar estruturas em cascata onde cada categoria nível 1 possui múltiplas sub-categorias.

Ideal para renderizar menus em cascata, sidebars de filtros e navegação secundária em páginas de categoria.

## Sintaxe

```twig
{# Sem parâmetros - retorna todas as categorias de nível 2 #}
{% set subcategorias = api.categoryGetLevel2() %}

{# Para retornar as subcategorias de uma categoria específica #}
{% set subcategorias = api.categoryGetLevel2({categoria_id: 1}) %}

{# Com parâmetros de consulta - filtra resultados #}
{% set subcategorias = api.categoryGetLevel2({id:'1', q:'eletronicos'}) %}
```

### Parâmetros

A função aceita parâmetros no formato JSON dentro de chaves `{}`:

- `id` — ID da categoria pai para filtrar apenas seus filhos (string ou número)
- `q` — Query de busca para filtrar por nome/descrição (string)

Todos os parâmetros possíveis estão documentados na [API Postman](https://documenter.getpostman.com/view/4141833/RWTsquyN).

### Retorno

Retorna um array com objetos de categoria nível 2. Cada objeto contém:

- Dados da categoria (`id`, `nome`, `url`, `ordenar` etc)
- Referência à categoria pai (parent_id)
- URLs e metadados
- **Sem categorias nível 3 aninhadas** (apenas nível 2)

#### Exemplo de estrutura retornada

```json
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

- Renderizar **menu em cascata** (categoria > subcategoria)
- Criar **sidebar de subcategorias** em páginas de categoria
- Filtros onde usuário seleciona **categoria secundária**
- Páginas de **listagem de produtos por subcategoria**
- Quando estrutura hierárquica de 2 níveis é suficiente

### Pré-condições

- Categorias nível 2 devem estar cadastradas como filhas de nível 1
- Deve haver acesso ao objeto `api` no contexto Twig
- Para menus em cascata, usar `categoryGetLevel1()` como pai

### Limitações

- Retorna **apenas nível 2** — não inclui categorias nível 3
- Para estrutura completa com 3 níveis, usar `categoryGetAll()`
- Sem filtro de categoria pai, retorna todas as subcategorias da loja

## Exemplo

```twig
{# Arquivo: templates/sidebar-categories.twig #}
<aside class="categories-sidebar">
  {% set parentCategory = product.category_parent_id %}
  
  <h3>Subcategorias</h3>
  <ul class="category-list">
    {% for subcat in api.categoryGetLevel2({id: parentCategory}) %}
      <li class="category-item">
        <a href="/categoria/{{ subcat.slug }}"
           class="category-link {% if subcat.id == product.category_id %}active{% endif %}">
          {{ subcat.name }}
        </a>
      </li>
    {% endfor %}
  </ul>
</aside>
```

Saída esperada (HTML):

```html
<aside class="categories-sidebar">
  <h3>Subcategorias</h3>
  <ul class="category-list">
    <li class="category-item">
      <a href="/categoria/eletronicos-celulares" class="category-link active">
        Celulares
      </a>
    </li>
    <li class="category-item">
      <a href="/categoria/eletronicos-tablets" class="category-link">
        Tablets
      </a>
    </li>
    <li class="category-item">
      <a href="/categoria/eletronicos-acessorios" class="category-link">
        Acessórios
      </a>
    </li>
  </ul>
</aside>
```

## Observações

### Performance

- `categoryGetLevel2()` retorna mais dados que `categoryGetLevel1()` mas menos que `categoryGetAll()`
- Performance é boa desde que não haja milhares de subcategorias
- Use **cache de 10-30 minutos** — mudanças em nível 2 são raras

### Cache

- Resultado é **candidato para cache medium-term** (15-60 minutos)
- Invalidar cache quando: categorias nível 2 são criadas, deletadas ou modificadas
- Usar **cache por parent_id** se possível (cache específico por categoria pai)

### Segurança

- Dados públicos — sem risco de expor informações sensíveis
- Nenhuma autenticação necessária

### Impacto SEO e Mobile

- Renderizado **server-side** — crawlable por bots
- Boa para **faceted search** e navegação de refino
- Em mobile, considere **accordion** ou **collapse** para não sobrecarregar tela

## Erros comuns

### Erro frequente 1: "Filtro por categoria pai não funciona"

**Problema**: Passar `{id: 5}` não retorna apenas filhas da categoria 5.
**Diagnóstico**: Parâmetro `id` pode funcionar diferente ou API pode precisar de nome diferente (ex: `parent_id`).
**Solução**: Consultar [API Postman](https://documenter.getpostman.com/view/4141833/RWTsquyN) para sintaxe exata. Debugar com `{{ pr(api.categoryGetLevel2({id: 5})) }}`.

### Erro frequente 2: "Categorias de outros pais aparecem misturadas"

**Problema**: Resultado contém subcategorias de múltiplas categorias pai.
**Diagnóstico**: Sem filtro, função retorna todas as nível 2. Precisa-se passar parâmetro correto.
**Solução**: Sempre passar ID da categoria pai: `api.categoryGetLevel2({id: category.id})`.

### Erro frequente 3: "Nível 3 aparece nos resultados"

**Problema**: Algumas categorias retornadas têm sub-categorias aninhadas (nível 3).
**Diagnóstico**: Pode haver confusão entre nível 2 e estrutura aninhada.
**Solução**: Verificar estrutura com `{{ pr(subcat) }}` para confirmar que são nível 2. Se houver nível 3 aninhado, ignorar em template.

## Veja também

- [categoryGetAll](./categorygetall.md) — Todas as categorias em hierarquia completa
- [categoryGetLevel1](./categorygetlevel1.md) — Apenas categorias nível 1 (raiz)
- [categoryGetLevel3](./categorygetlevel3.md) — Apenas categorias nível 3
- [Visão geral da API](./visao-geral-api.md) — Contexto e diferenças server-side vs client-side
