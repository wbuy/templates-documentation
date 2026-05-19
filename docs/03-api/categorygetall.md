---
title: "categoryGetAll"
slug: "categorygetall"
doc_type: "reference"
summary: "Função API que recupera todas as categorias e sub-categorias (níveis 2 e 3) disponíveis na loja virtual. Ideal para populações de menus hierárquicos e seleções de categorias em templates server-side."
tags:
  - api
  - categorias
  - server-side
  - twig
  - hierarquia
related:
  - 03-api/categorygetlevel1.md
  - 03-api/categorygetlevel2.md
  - 03-api/categorygetlevel3.md
  - 03-api/visao-geral-api.md
---

## O que faz

A função `categoryGetAll()` busca na API todas as categorias e sub-categorias (níveis 2 e 3) disponíveis na loja virtual. Retorna uma estrutura hierárquica completa de categorias que pode ser usada para renderizar menus, navegação e listas de categorias em templates Twig.

Diferencia-se de `categoryGetLevel1()`, `categoryGetLevel2()` e `categoryGetLevel3()` porque agrega múltiplos níveis hierárquicos em uma única chamada, reduzindo requisições quando toda a taxonomia é necessária.

## Sintaxe

```twig
{# Sem parâmetros - retorna todas as categorias #}
{% set categorias = api.categoryGetAll() %}

{# Com parâmetros de consulta - filtra resultados #}
{% set categorias = api.categoryGetAll({id:'1', q:'eletronicos'}) %}
```

### Parâmetros

A função aceita parâmetros no formato JSON dentro de chaves `{}`:

- `id` — ID específico para filtrar categoria (string ou número)
- `q` — Query de busca para filtrar por nome/descrição (string)
- `url` — Filtrar por slug/url da categoria (string)
- `ativo` — Filtrar por status ativo/inativo (number 0 ou 1)
- `order` — Ordenação dos resultados. Valores possíveis: `id,asc`, `id,desc`, `nome,asc`, `nome,desc`, `posicao,asc`, `posicao,desc`. Valor padrão: `posicao,asc`
- `limit` — Limitar número de resultados retornados (number). Valor padrão: `0,100` sendo: `0` (inicia-se do índice zero) `100` (retornam 100 resultados)

### Retorno

Retorna um array com objetos de categoria. Cada objeto contém:

- Dados da categoria (`id`, `nome`, `url`, `ordenar` etc)
- Sub-categorias aninhadas - array `subs` (para níveis 2 e 3)
- URLs e metadados associados

#### Exemplo de estrutura retornada

```json
[
  {
    "id": "1",
    "nome": "Categoria um",
    "url": "categoria-um",
    "icone_tipo": "1",
    "icone": "",
    "cor": "",
    "posicao": "0",
    "menu": "1", // 1 para mostrar no menu, 0 para ocultar
    "ordenar": "valor-asc",
    "total_produtos": "0",
    "subs": [
      {
        "id": 1,
        "nome": "Nível 02",
        "url": "nivel-02",
        "subs": [
          {
            "id": 1,
            "nome": "Nível 03",
            "url": "nivel-03"
          }
        ]
      }
    ]
  }
]
```

## Quando usar

- Renderizar **menu de navegação completo** com hierarquia de categorias
- Criar **sidebar de categorias** que mostra múltiplos níveis
- Filtros de busca que precisam de **toda taxonomia disponível**
- Quando a performance permite uma **única chamada consolidada**

### Pré-condições

- Categorias devem estar cadastradas e ativas no painel de administração
- Deve haver acesso ao objeto `api` no contexto Twig
- Cache deve estar configurado (recomendado para esta operação pesada)

### Limitações

- Retorna **todos os níveis de uma vez**, podendo ser mais pesada que chamadas específicas de nível
- Grande volume de dados se loja tem muitas categorias — considere paginação em APIs client-side
- Sem parâmetros, retorna o catálogo completo da loja

## Exemplo

```twig
{% set categories = api.categoryGetAll() %}

{# Arquivo: widgets/navigation.html #}
<nav class="categories-menu">
  {% for category in categories %}
    <div class="category-item">
      <a href="/categoria/{{ category.url }}">
        {{ category.nome }}
      </a>
      {% if category.subs %}
        <ul class="subcategories">
          {% for sub in category.subs %}
            <li>
              <a href="/categoria/{{ sub.url }}">
                {{ sub.nome }}
              </a>
            </li>
          {% endfor %}
        </ul>
      {% endif %}
    </div>
  {% endfor %}
</nav>
```

Saída esperada:

```html
<nav class="categories-menu">
  <div class="category-item">
    <a href="/categoria/eletronicos">
      Eletrônicos
    </a>
    <ul class="subcategories">
      <li>
        <a href="/categoria/eletronicos-celulares">
          Celulares
        </a>
      </li>
      <li>
        <a href="/categoria/eletronicos-notebooks">
          Notebooks
        </a>
      </li>
    </ul>
  </div>
</nav>
```

## Observações

### Performance

- `categoryGetAll()` é uma operação custosa — use **cache agressivo** (full-page cache com invalidação por webhook)
- Se houver muitas categorias, considere `categoryGetLevel1()` e carregar níveis subsequentes apenas quando necessário
- Ideal para ser executada uma vez por renderização de página

### Cache

- Resultado é **candidato ideal para cache full-page** (cache em Varnish/Redis por horas)
- Invalidar cache quando: categorias são criadas, modificadas ou deletadas (via webhook no backend)
- Browser caching não é aplicável (dados específicos da loja)

### Segurança

- Dados de categorias são públicos — sem risco de expor dados sensíveis
- Nenhuma autenticação necessária (endpoint público)

### Impacto SEO e Mobile

- Renderizado **server-side** — HTML é crawlable por bots de busca
- Estrutura hierárquica é benéfica para **SEO estruturado** (schema markup)
- Em mobile, considere **collapse/expand** da hierarquia via CSS/JS para não criar menu muito grande

## Erros comuns

### Erro frequente 1: "Parâmetros `limit` e `order` retornam erro ou não funcionam"

**Problema**: Passar `{limit: 50, order: 'nome,asc'}` causa erro ou os resultados não são limitados/ordenados.
**Diagnóstico**: Sintaxe de parâmetros pode estar incorreta. Formato esperado: `limit` como string `"0,50"` (índice inicial, quantidade) e `order` com vírgula separando campo e direção.
**Solução**: Usar sintaxe correta:

- Correto: `api.categoryGetAll({limit: '0,50', order: 'posicao,asc'})`
- Errado: `api.categoryGetAll({limit: 50, order: 'nome'})`
- Valores válidos para `order`: `id,asc` | `id,desc` | `nome,asc` | `nome,desc` | `posicao,asc` | `posicao,desc`

### Erro frequente 2: "Menu fica muito grande no mobile com muitas subcategorias"

**Problema**: Quando há muitas categorias e subcategorias, o menu renderizado ocupa muita altura na tela mobile.
**Diagnóstico**: Verificar no mobile (DevTools) que menu em cascata mostra todos os níveis de uma vez, tornando a navegação lenta e confusa.
**Solução**: Implementar collapse/expand para subcategorias via CSS + JavaScript:

- Usar `hidden` attribute ou CSS `display: none` por padrão em mobile
- Adicionar toggle via data attribute: `data-toggle="subcategories"`
- Com jQuery: `$('[data-toggle="subcategories"]').on('click', function() { $(this).toggleClass('expanded'); })`
- Considerar usar `categoryGetLevel1()` e carregar subcategorias via AJAX ao clicar (menos dados no HTML inicial)

### Erro frequente 3: "Parâmetros não filtram nenhum resultado"

**Problema**: Passar `{q: 'eletronicos'}` ou `{id: 5}` retorna array vazio, mesmo sabendo que existem categorias correspondentes.
**Diagnóstico**: Provavelmente não existem categorias que correspondam exatamente ao filtro.
**Solução**: Verificar no painel wBuy se as categorias existem e correspondem ao filtro. Testar com `{{ pr(api.categoryGetAll({q: 'eletronicos'})) }}` para ver resposta real. Ajustar filtro para ser mais genérico ou verificar se campo de busca é o correto (pode ser `nome` em vez de `q`, por exemplo).

## Veja também

- [categoryGetLevel1](./categorygetlevel1.md) — Apenas categorias nível 1 (raiz)
- [categoryGetLevel2](./categorygetlevel2.md) — Apenas categorias nível 2
- [categoryGetLevel3](./categorygetlevel3.md) — Apenas categorias nível 3
- [Visão geral da API](./visao-geral-api.md) — Contexto e diferenças server-side vs client-side
