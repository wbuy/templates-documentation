---
title: "getVariations"
slug: "getvariations"
doc_type: "reference"
summary: "Função API que recupera todas as variações (SKUs) disponíveis de um produto ou na loja. Ideal para renderizar seletores de tamanho, cor, e outras opções de variação em página de produto."
tags:
  - api
  - variações
  - sku
  - server-side
  - twig
  - produto
related:
  - 03-api/productget.md
  - 03-api/getcolors.md
  - 03-api/visao-geral-api.md
  - 04-store/producttobox.md
---

## O que faz

A função `getVariations()` busca na API todas as variações (SKUs) disponíveis de um produto ou na loja virtual. Cada variação representa uma combinação de atributos (cor, tamanho, material, etc) com seu próprio SKU, preço, estoque e especificações.

Essencial para renderizar seletores interativos de variação e atualizar preço/estoque baseado na seleção do usuário.

## Sintaxe

```twig
{# Sem parâmetros - retorna todas as variações de todos os produtos #}
{% set variacoes = api.getVariations() %}

{# Com parâmetros de consulta - filtra por produto específico #}
{% set variacoes = api.getVariations({id:'1'}) %}
```

### Parâmetros

A função aceita parâmetros no formato JSON dentro de chaves `{}`:

- `id` — ID do produto para filtrar apenas suas variações (string ou número)

Todos os parâmetros possíveis estão documentados na [API Postman](https://documenter.getpostman.com/view/4141833/RWTsquyN?version=latest#35e48b0c-9561-411f-9e71-2f65488f79aa).

### Retorno

Retorna um array com objetos de variação. Cada objeto contém:
- SKU único (identificador da variação)
- ID do produto pai
- Atributos (cor, tamanho, etc)
- Preço específico da variação
- Quantidade em estoque
- Peso, dimensões
- Status (disponível/indisponível)

## Quando usar

- Renderizar **seletor de tamanho/cor** em página de produto
- Exibir **todas as variações disponíveis** de um item
- Mostrar **preço e estoque por variação**
- Criar **tabela de variações** com comparação
- Quando produto tem **múltiplas SKUs com atributos diferentes**

### Pré-condições

- Variações devem estar cadastradas no painel de administração
- Cada variação deve ter SKU único e atributos definidos
- Deve haver acesso ao objeto `api` no contexto Twig
- Ao filtrar por produto, passar ID correto

### Limitações

- Retorna **apenas metadados de variação** — não inclui imagens por SKU
- Sem filtro `id`, retorna todas as variações da loja (pode ser muito)
- Atributos podem ter estrutura variável (não normalizados)

## Exemplo

```twig
{# Arquivo: templates/product-variations.twig #}
<div class="product-variations">
  {% set product_id = product.id %}
  {% set variações = api.getVariations({id: product_id}) %}
  
  {% if variações|length > 0 %}
    <table class="variations-table">
      <thead>
        <tr>
          <th>SKU</th>
          <th>Atributos</th>
          <th>Preço</th>
          <th>Estoque</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        {% for var in variações %}
          <tr class="variation-row" data-sku="{{ var.sku }}">
            <td class="sku-cell">{{ var.sku }}</td>
            <td class="attributes-cell">
              {% if var.color %}
                <span class="attribute">{{ var.color }}</span>
              {% endif %}
              {% if var.size %}
                <span class="attribute">{{ var.size }}</span>
              {% endif %}
            </td>
            <td class="price-cell">R$ {{ var.price|number_format(2, ',', '.') }}</td>
            <td class="stock-cell">
              {% if var.stock > 0 %}
                {{ var.stock }} unidade(s)
              {% else %}
                <span class="out-of-stock">Fora de estoque</span>
              {% endif %}
            </td>
            <td class="status-cell">
              <span class="badge status-{{ var.status }}">
                {{ var.status|capitalize }}
              </span>
            </td>
          </tr>
        {% endfor %}
      </tbody>
    </table>
  {% else %}
    <p>Nenhuma variação disponível para este produto.</p>
  {% endif %}
</div>

<style>
  .variations-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  
  .variations-table th,
  .variations-table td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #ddd;
  }
  
  .variations-table th {
    background-color: #f5f5f5;
    font-weight: bold;
  }
  
  .variation-row:hover {
    background-color: #f9f9f9;
  }
  
  .attribute {
    display: inline-block;
    margin-right: 8px;
    padding: 2px 8px;
    background-color: #e8e8e8;
    border-radius: 3px;
    font-size: 0.9em;
  }
  
  .out-of-stock {
    color: #d32f2f;
    font-weight: bold;
  }
</style>
```

Saída esperada (HTML):
```html
<div class="product-variations">
  <table class="variations-table">
    <thead>
      <tr>
        <th>SKU</th>
        <th>Atributos</th>
        <th>Preço</th>
        <th>Estoque</th>
        <th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr class="variation-row" data-sku="PROD-001-P-M">
        <td class="sku-cell">PROD-001-P-M</td>
        <td class="attributes-cell">
          <span class="attribute">Preto</span>
          <span class="attribute">Médio</span>
        </td>
        <td class="price-cell">R$ 89,90</td>
        <td class="stock-cell">12 unidade(s)</td>
        <td class="status-cell">
          <span class="badge status-ativo">Ativo</span>
        </td>
      </tr>
    </tbody>
  </table>
</div>
```

## Observações

### Performance

- `getVariations()` **sem filtro** retorna todas as variações da loja — pode ser grande
- **Sempre passar `id` do produto** quando possível: `api.getVariations({id: product_id})`
- Cache agressivo recomendado (variações mudam com frequência média)

### Cache

- Resultado é **candidato para cache medium-term** (30-120 minutos)
- Invalidar cache quando: SKU é criado, deletado ou modificado
- Usar **cache por product_id** para granularidade eficiente

### Segurança

- Dados públicos — sem risco de expor informações sensíveis
- SKUs e preços são visíveis em catálogo
- Nenhuma autenticação necessária

### Impacto SEO e Mobile

- Renderizado **server-side** — crawlable por bots (bom para SEO)
- Tabela de variações em mobile pode ser larga — considerar **scroll horizontal** ou **accordion**
- Seletores de variação melhoram **conversion rate** em mobile

## Erros comuns

### Erro frequente 1: "Sem filtro, retorna muitas variações"
**Problema**: `api.getVariations()` sem parâmetro retorna milhares de SKUs, lentificando página.
**Diagnóstico**: Performance degradada, timeout de renderização.
**Solução**: **Sempre passar `id` do produto**: `api.getVariations({id: product.id})` para retornar apenas variações relevantes.

### Erro frequente 2: "Atributos têm estrutura inconsistente"
**Problema**: `var.color` existe em algumas variações mas não em outras; nomes diferem (color vs cor).
**Diagnóstico**: API retorna atributos com nomes variáveis. Debugar com `{{ pr(var) }}` para ver estrutura.
**Solução**: Criar mapeamento de atributos ou usar template defensivo: `{% if var.color %}` antes de acessar.

### Erro frequente 3: "Preço ou estoque não atualizam"
**Problema**: Template renderiza preço/estoque da variação mas valores parecem desatualizados.
**Diagnóstico**: Cache pode estar obsoleto. Variação foi modificada mas HTML cacheado não reflete mudança.
**Solução**: 
- Invalidar cache quando SKU é atualizado
- Usar AJAX client-side para atualizar preço/estoque dinamicamente baseado em seleção

## Veja também

- [productGet](./productget.md) — Dados completos de produtos
- [getColors](./getcolors.md) — Paleta de cores da loja para variações
- [Visão geral da API](./visao-geral-api.md) — Contexto e diferenças server-side vs client-side
