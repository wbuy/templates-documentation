---
title: "getColors"
slug: "getcolors"
doc_type: "reference"
summary: "Função API que recupera a paleta de cores definidas na loja virtual. Ideal para renderizar seletores de cores de produtos e manter consistência visual com branding da loja."
tags:
  - api
  - cores
  - server-side
  - twig
  - variações
  - branding
related:
  - 03-api/getvariations.md
  - 03-api/productget.md
  - 03-api/visao-geral-api.md
  - 04-store/visao-geral-store.md
---

## O que faz

A função `getColors()` busca na API a paleta de cores disponíveis cadastradas na loja virtual. Retorna lista com identificadores de cores que podem ser usados como filtros em listagens de produtos, seletores de variação ou exibição de cores disponíveis de um produto.

Essencial para renderizar interfaces de seleção de cor e manter consistência visual com a paleta de branding da loja.

## Sintaxe

```twig
{# Sem parâmetros - retorna todas as cores #}
{% set cores = api.getColors() %}

{# Com parâmetros de consulta - filtra resultados #}
{% set cores = api.getColors({id:'1'}) %}
```

### Parâmetros

A função aceita parâmetros no formato JSON dentro de chaves `{}`:

- `id` — ID específico para filtrar cor (string ou número)

Todos os parâmetros possíveis estão documentados na [API Postman](https://documenter.getpostman.com/view/4141833/RWTsquyN?version=latest#0a66c2c4-42aa-46d1-94d2-4d6f8876e26d).

### Retorno

Retorna um array com objetos de cor. Cada objeto contém:
- ID da cor (identificador único)
- Nome da cor (ex: "Preto", "Azul", "Vermelho")
- Código hexadecimal (ex: "#000000", "#0000FF")
- Slug ou identificador interno para URLs

## Quando usar

- Renderizar **seletor de cores em página de produto**
- Criar **filtros de cor em listagem de produtos**
- Exibir **variações de cor disponível** de um item
- Mostrar **paleta de cores da loja** em página de configurações
- Quando precisa de **paleta consistente com loja**

### Pré-condições

- Cores devem estar cadastradas no painel de administração wBuy
- Deve haver acesso ao objeto `api` no contexto Twig
- Produtos com variações de cor precisam referenciar IDs retornados

### Limitações

- Retorna **apenas cores cadastradas** — não gera automaticamente variações
- Sem ligação direta com produtos — use `productGet()` para produtos específicos
- Combinado com `getVariations()` para produtos multi-cor

## Exemplo

```twig
{# Arquivo: templates/product-color-selector.twig #}
<div class="product-colors">
  <label>Escolha uma cor:</label>
  
  <div class="color-grid">
    {% for cor in api.getColors() %}
      <div class="color-option">
        <input type="radio" 
               name="product-color" 
               value="{{ cor.id }}"
               id="color-{{ cor.id }}"
               {% if loop.first %}checked{% endif %}>
        
        <label for="color-{{ cor.id }}" 
               class="color-swatch"
               style="background-color: {{ cor.hex_code }};"
               title="{{ cor.name }}">
          {{ cor.name }}
        </label>
      </div>
    {% endfor %}
  </div>
</div>

<style>
  .color-grid {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
  }
  
  .color-swatch {
    display: inline-block;
    width: 40px;
    height: 40px;
    border-radius: 4px;
    cursor: pointer;
    border: 2px solid transparent;
  }
  
  .color-option input:checked + .color-swatch {
    border-color: #333;
    box-shadow: 0 0 5px rgba(0,0,0,0.3);
  }
</style>
```

Saída esperada (HTML):
```html
<div class="product-colors">
  <label>Escolha uma cor:</label>
  
  <div class="color-grid">
    <div class="color-option">
      <input type="radio" 
             name="product-color" 
             value="1"
             id="color-1"
             checked>
      
      <label for="color-1" 
             class="color-swatch"
             style="background-color: #000000;"
             title="Preto">
        Preto
      </label>
    </div>
    <div class="color-option">
      <input type="radio" 
             name="product-color" 
             value="2"
             id="color-2">
      
      <label for="color-2" 
             class="color-swatch"
             style="background-color: #FFFFFF;"
             title="Branco">
        Branco
      </label>
    </div>
  </div>
</div>
```

## Observações

### Performance

- `getColors()` retorna **dados leves** — geralmente poucas cores (10-100)
- Ideal renderizar **uma vez por página** e reutilizar em template
- Use **cache long-term** (dias/semanas) — cores mudam raramente

### Cache

- Resultado é **candidato para cache very-long-term** (1-4 semanas)
- Invalidar cache quando: nova cor é criada, deletada ou modificada no painel
- Usar **cache global** — cores são iguais para toda a loja

### Segurança

- Dados públicos — sem risco de expor informações sensíveis
- Nenhuma autenticação necessária

### Impacto SEO e Mobile

- Renderizado **server-side** — crawlable por bots
- Swatches de cores melhora **user experience** em mobile
- Cores com código hexadecimal válido garantem **acessibilidade**

## Erros comuns

### Erro frequente 1: "Cores retornam vazio"
**Problema**: `api.getColors()` retorna array vazio, seletor não renderiza.
**Diagnóstico**: Nenhuma cor cadastrada na loja, ou API com erro.
**Solução**: Verificar painel wBuy se cores foram cadastradas. Se sim, debugar com `{{ pr(api.getColors()) }}` para ver resposta real.

### Erro frequente 2: "Código hexadecimal inválido"
**Problema**: Cores retornam mas `cor.hex_code` não é código hex válido (ex: não começa com `#`).
**Diagnóstico**: Campo pode ter nome diferente ou valor em formato não-esperado.
**Solução**: Debugar com `{{ pr(cor) }}` para ver estrutura exata. Usar nome correto do campo (pode ser `hex`, `color_code`, `hex_code`, etc).

### Erro frequente 3: "Cores de um produto não correspondem às cores da API"
**Problema**: Produto tem cor cadastrada que não aparece em `getColors()`.
**Diagnóstico**: Cores podem estar deletadas ou desativadas na loja.
**Solução**: Filtrar por produto específico: usar `productGet(id)` para ver quais cores estão associadas àquele produto, depois comparar com `getColors()`.

## Veja também

- [getVariations](./getvariations.md) — Variações (SKU) de produtos por cor/tamanho
- [productGet](./productget.md) — Dados completos de produto incluindo cores disponíveis
- [Visão geral da API](./visao-geral-api.md) — Contexto e diferenças server-side vs client-side
