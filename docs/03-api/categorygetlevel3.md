---
title: "categoryGetLevel3"
slug: "categorygetlevel3"
doc_type: "reference"
summary: "Função API que recupera apenas categorias de nível 3 (sub-subcategorias) disponíveis na loja virtual. Ideal para estruturas profundas de navegação e refinamento avançado de categorias."
tags:
  - api
  - categorias
  - server-side
  - twig
  - nível-3
  - profundidade
related:
  - 03-api/categorygetall.md
  - 03-api/categorygetlevel1.md
  - 03-api/categorygetlevel2.md
  - 03-api/visao-geral-api.md
---

## O que faz

A função `categoryGetLevel3()` busca na API apenas as categorias de **nível 3** (sub-subcategorias/categorias terciárias) disponíveis na loja virtual. Completa a hierarquia de categorias para lojas com estrutura profunda de taxonomia.

Ideal para renderizar o nível mais profundo de navegação, filtragem de terceiro nível e detalhes específicos de categoria.

## Sintaxe

```twig
{# Sem parâmetros - retorna todas as categorias de nível 3 #}
{% set tercnivel = api.categoryGetLevel3() %}

{# Com parâmetros de consulta - filtra resultados #}
{% set tercnivel = api.categoryGetLevel3({id:'1', q:'eletronicos'}) %}
```

### Parâmetros

A função aceita parâmetros no formato JSON dentro de chaves `{}`:

- `id` — ID da categoria pai para filtrar apenas seus filhos (string ou número)
- `q` — Query de busca para filtrar por nome/descrição (string)

Todos os parâmetros possíveis estão documentados na [API Postman](https://documenter.getpostman.com/view/4141833/RWTsquyN).

### Retorno

Retorna um array com objetos de categoria nível 3. Cada objeto contém:
- ID, nome, slug, descrição
- Referência à categoria pai (parent_id, breadcrumb)
- URLs e metadados
- **Sem categorias aninhadas abaixo** (nível 3 é o mais profundo)

## Quando usar

- Renderizar **menu em cascata com 3 níveis**
- Criar **refinadores de categoria** em página de busca
- Listar **subcategorias mais específicas** de um grupo
- Quando navegação precisa de **granularidade máxima**
- Lojas com **catálogo muito profundo**

### Pré-condições

- Categorias nível 3 devem estar cadastradas como filhas de nível 2
- Deve haver acesso ao objeto `api` no contexto Twig
- Para navegar, usar hierarquia: nível 1 → nível 2 → nível 3

### Limitações

- Retorna **apenas nível 3** — não inclui níveis anteriores
- Sem filtro de categoria pai, retorna todas as nível 3 da loja (pode ser muito)
- Considerar performance se houver muitas categorias nível 3

## Exemplo

```twig
{# Arquivo: templates/category-breadcrumb.twig #}
<div class="category-breadcrumb">
  <h2>Categorias Disponíveis</h2>
  
  {% set parent_id = subcat.id %}
  {% set level3_categories = api.categoryGetLevel3({id: parent_id}) %}
  
  {% if level3_categories|length > 0 %}
    <div class="level3-grid">
      {% for cat3 in level3_categories %}
        <div class="category-card level3">
          <h4>{{ cat3.name }}</h4>
          <p>{{ cat3.description }}</p>
          <a href="/categoria/{{ cat3.slug }}" class="btn">
            Ver produtos
          </a>
        </div>
      {% endfor %}
    </div>
  {% else %}
    <p>Nenhuma subcategoria disponível</p>
  {% endif %}
</div>
```

Saída esperada (HTML):
```html
<div class="category-breadcrumb">
  <h2>Categorias Disponíveis</h2>
  
  <div class="level3-grid">
    <div class="category-card level3">
      <h4>Smartphones</h4>
      <p>Telefones inteligentes de diversas marcas</p>
      <a href="/categoria/celulares-smartphones" class="btn">
        Ver produtos
      </a>
    </div>
    <div class="category-card level3">
      <h4>Telefones Básicos</h4>
      <p>Telefones simples sem recursos avançados</p>
      <a href="/categoria/celulares-basicos" class="btn">
        Ver produtos
      </a>
    </div>
  </div>
</div>
```

## Observações

### Performance

- `categoryGetLevel3()` pode retornar **muitos resultados** dependendo da estrutura da loja
- Sem filtro `id`, a resposta pode ser grande — sempre passar `id` da categoria pai quando possível
- Use **cache agressivo** (30-120 minutos) — mudanças em nível 3 são raras

### Cache

- Resultado é **candidato para cache long-term** (1-24 horas)
- Invalidar cache quando: categorias nível 3 são criadas, deletadas ou modificadas
- Usar **cache por parent_id** para granularidade de cache eficiente

### Segurança

- Dados públicos — sem risco de expor informações sensíveis
- Nenhuma autenticação necessária

### Impacto SEO e Mobile

- Renderizado **server-side** — crawlable por bots
- Estrutura profunda de 3+ níveis pode prejudicar **mobile UX** — considerar collapse/tabs
- Boa para **rich snippets** e navegação estruturada (schema.org)

## Erros comuns

### Erro frequente 1: "Sem filtro, retorna muitas categorias"
**Problema**: `api.categoryGetLevel3()` sem parâmetro retorna milhares de categorias, lentificando página.
**Diagnóstico**: Performance degradada, timeout, ou DOM muito grande.
**Solução**: **Sempre passar `id` da categoria pai**: `api.categoryGetLevel3({id: parent_id})` para reduzir resultado.

### Erro frequente 2: "Categorias de outros pais aparecem"
**Problema**: Resultado contém categorias nível 3 de múltiplas categorias pai.
**Diagnóstico**: Sem filtro `id`, função retorna todas. Precisa ser mais específico.
**Solução**: Passar `id` correto: `api.categoryGetLevel3({id: category_nível_2.id})`.

### Erro frequente 3: "Template não consegue renderizar muitas categorias"
**Problema**: Loop Twig tenta renderizar centenas/milhares de items, travando renderização.
**Diagnóstico**: Página fica muito lenta ou timeout de renderização.
**Solução**: 
- Limitar resultado com parâmetro de API (se suportado): `{id: X, limit: 50}`
- Usar **paginação**: dividir categorias em páginas
- Usar **AJAX lazy-loading**: carregar apenas o que está visível

## Veja também

- [categoryGetAll](./categorygetall.md) — Todas as categorias em hierarquia completa
- [categoryGetLevel1](./categorygetlevel1.md) — Apenas categorias nível 1 (raiz)
- [categoryGetLevel2](./categorygetlevel2.md) — Apenas categorias nível 2
- [Visão geral da API](./visao-geral-api.md) — Contexto e diferenças server-side vs client-side
