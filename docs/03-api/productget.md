---
title: "productGet"
slug: "productget"
doc_type: "reference"
summary: "Função API que recupera dados completos de produtos da loja virtual. Ideal para renderizar páginas de detalhes de produto, listagens customizadas e acesso a metadados como preço, estoque, descrição e imagens."
tags:
  - api
  - produtos
  - server-side
  - twig
  - detalhe-produto
  - catálogo
related:
  - 03-api/getvariations.md
  - 03-api/getcolors.md
  - 03-api/categorygetall.md
  - 03-api/visao-geral-api.md
  - 04-store/store-productdetail.md
---

## O que faz

A função `productGet()` busca na API dados completos de produtos cadastrados na loja virtual. Retorna informações detalhadas como nome, descrição, preço, estoque, imagens, categorias, variações, avaliações e metadados SEO.

Essencial para renderizar páginas de detalhes de produto, recomendações customizadas e listagens dinâmicas de produtos.

## Sintaxe

```twig
{# Sem parâmetros - retorna todos os produtos #}
{% set produtos = api.productGet() %}

{# Com parâmetros de consulta - filtra e busca #}
{% set produtos = api.productGet({id:'1', produto:'tv'}) %}
```

### Parâmetros

A função aceita parâmetros no formato JSON dentro de chaves `{}`:

- `id` — ID específico do produto (string ou número)
- `produto` — Query de busca por nome/descrição (string)

Todos os parâmetros possíveis estão documentados na [API Postman](https://documenter.getpostman.com/view/4141833/RWTsquyN?version=latest#adc4aac5-0b03-4844-abdb-e782e04f51ce).

### Retorno

Retorna um array com objetos de produto. Cada objeto contém:
- ID, nome, slug, descrição
- Preço (varejo, custo, especial)
- Estoque total
- Imagens (URL da capa, galeria)
- Categorias associadas
- SKUs/Variações
- Avaliações e comentários
- Palavras-chave e metadados SEO
- Data de criação e modificação

## Quando usar

- Renderizar **página de detalhes de produto** (product detail page)
- Criar **listagens customizadas** de produtos (busca, filtros)
- Gerar **recomendações** (produtos relacionados, sugestões)
- Exibir **carrousel de best sellers** ou **promoções**
- Quando precisa de **dados completos de um ou múltiplos produtos**

### Pré-condições

- Produtos devem estar cadastrados e ativos no painel de administração
- Deve haver acesso ao objeto `api` no contexto Twig
- Para detalhe, produto precisa existir com ID válido

### Limitações

- Retorna **apenas produtos ativos** — produtos deletados/inativos não aparecem
- Sem parâmetros, retorna todos os produtos (pode ser pesado para lojas grandes)
- Sempre passar filtro quando possível para reduzir dados transferidos
- Para histórico completo (incluindo inativos), seria necessário acesso admin

## Exemplo

```twig
{# Arquivo: templates/product-detail.twig #}
<div class="product-detail">
  {% set product = api.productGet({id: product_id})|first %}
  
  {% if product %}
    <div class="product-container">
      <div class="product-image">
        <img src="{{ product.image_url }}" 
             alt="{{ product.name }}"
             class="main-image">
        
        {% if product.gallery %}
          <div class="thumbnail-gallery">
            {% for img in product.gallery %}
              <img src="{{ img.url }}" alt="Galeria" class="thumbnail">
            {% endfor %}
          </div>
        {% endif %}
      </div>
      
      <div class="product-info">
        <h1>{{ product.name }}</h1>
        
        <div class="product-rating">
          <span class="stars">★★★★★ ({{ product.ratings|length }} avaliações)</span>
        </div>
        
        <div class="product-price">
          {% if product.discount_price %}
            <span class="original-price">R$ {{ product.price|number_format(2, ',', '.') }}</span>
            <span class="discount-price">R$ {{ product.discount_price|number_format(2, ',', '.') }}</span>
          {% else %}
            <span class="price">R$ {{ product.price|number_format(2, ',', '.') }}</span>
          {% endif %}
        </div>
        
        <div class="product-description">
          <h3>Descrição</h3>
          <p>{{ product.description }}</p>
        </div>
        
        <div class="product-stock">
          {% if product.stock > 0 %}
            <span class="in-stock">✓ Em estoque ({{ product.stock }} unidades)</span>
          {% else %}
            <span class="out-of-stock">✗ Fora de estoque</span>
          {% endif %}
        </div>
        
        <div class="product-actions">
          <button class="btn btn-primary btn-add-to-cart" data-product-id="{{ product.id }}">
            Adicionar ao Carrinho
          </button>
          <button class="btn btn-secondary btn-wishlist" data-product-id="{{ product.id }}">
            ♡ Favoritar
          </button>
        </div>
        
        <div class="product-meta">
          <p><strong>Categorias:</strong> 
            {% for cat in product.categories %}
              <a href="/categoria/{{ cat.slug }}">{{ cat.name }}</a>{{ not loop.last ? ', ' : '' }}
            {% endfor %}
          </p>
          <p><strong>SKU:</strong> {{ product.sku }}</p>
        </div>
      </div>
    </div>
  {% else %}
    <div class="product-not-found">
      <p>Produto não encontrado.</p>
      <a href="/produtos" class="btn btn-primary">Voltar ao Catálogo</a>
    </div>
  {% endif %}
</div>
```

Saída esperada (HTML):
```html
<div class="product-detail">
  <div class="product-container">
    <div class="product-image">
      <img src="https://cdn.example.com/products/tv-123.jpg" 
           alt="TV 55 polegadas Smart 4K"
           class="main-image">
      
      <div class="thumbnail-gallery">
        <img src="https://cdn.example.com/products/tv-123-thumb-1.jpg" alt="Galeria" class="thumbnail">
        <img src="https://cdn.example.com/products/tv-123-thumb-2.jpg" alt="Galeria" class="thumbnail">
      </div>
    </div>
    
    <div class="product-info">
      <h1>TV 55 polegadas Smart 4K</h1>
      
      <div class="product-rating">
        <span class="stars">★★★★★ (42 avaliações)</span>
      </div>
      
      <div class="product-price">
        <span class="original-price">R$ 2.499,90</span>
        <span class="discount-price">R$ 1.999,90</span>
      </div>
      
      <div class="product-stock">
        <span class="in-stock">✓ Em estoque (5 unidades)</span>
      </div>
    </div>
  </div>
</div>
```

## Observações

### Performance

- `productGet()` **sem filtro** retorna todos os produtos — pode ser muito pesado
- **Sempre passar filtro**: `{id: X}` ou `{produto: 'query'}` para reduzir dados
- Use **cache agressivo** — dados de produto mudam com frequência baixa

### Cache

- Resultado é **candidato para cache long-term** (2-24 horas)
- Invalidar cache quando: produto é criado, deletado, preço muda ou estoque atualizado
- Usar **cache por product_id** para granularidade máxima

### Segurança

- Dados públicos — sem risco de expor informações sensíveis
- Nenhuma autenticação necessária
- Preços e estoque são visíveis em catálogo

### Impacto SEO e Mobile

- Renderizado **server-side** — excelente para SEO
- HTML com dados de produto é crawlable por bots
- Estruturado com **schema.org/Product** para rich snippets
- Em mobile, imagem responsiva melhora **Core Web Vitals**

## Erros comuns

### Erro frequente 1: "Sem filtro, página fica muito lenta"
**Problema**: `api.productGet()` sem parâmetro causa timeout ou lentidão extrema.
**Diagnóstico**: Loja tem muitos produtos (1000+). Todos são retornados e renderizados.
**Solução**: 
- **Sempre passar filtro**: `{id: product_id}` ou `{produto: 'query'}`
- Se precisa de todos, implementar **paginação no template** ou **AJAX lazy-loading**

### Erro frequente 2: "Produto retorna mas dados estão incompletos"
**Problema**: `product.image_url` ou outros campos vêm nulos/vazios.
**Diagnóstico**: Campos podem ter nome diferente ou não foram preenchidos no cadastro.
**Solução**: Debugar com `{{ pr(product) }}` para ver estrutura exata. Usar nome correto do campo.

### Erro frequente 3: "Preço/estoque desatualizado"
**Problema**: Template renderiza valor antigo, mesmo após mudança no painel.
**Diagnóstico**: Cache de página está velho. Página não foi invalidada quando produto foi atualizado.
**Solução**: 
- Implementar **webhook no painel** para invalidar cache quando produto muda
- Usar **AJAX client-side** para atualizar preço/estoque dinamicamente sem reload

## Veja também

- [getVariations](./getvariations.md) — SKUs e variações específicas de produto
- [getColors](./getcolors.md) — Paleta de cores para filtros
- [categoryGetAll](./categorygetall.md) — Categorias para navegação
- [Visão geral da API](./visao-geral-api.md) — Contexto e diferenças server-side vs client-side
- [Store Product Detail](../04-store/store-productdetail.md) — Contexto de variável de produto global
