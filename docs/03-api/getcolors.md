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

#### Exemplo de estrutura retornada

```json
[
  {
    "id": 559381,
    "nome": "amarelo",
    "cor1": "#fff000",
    "cor2": "",
    "img": "",
    "ativo": 1,
    "tipo": 1,
    "grupo_id": 0,
    "grupo_cores": "",
    "total_produtos": 3
  },
  {
    "id": 559382,
    "nome": "azul",
    "cor1": "#0000ff",
    "cor2": "",
    "img": "",
    "ativo": 1,
    "tipo": 1,
    "grupo_id": 0,
    "grupo_cores": "",
    "total_produtos": 5
  }
]
```

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
{# Arquivo: widgets/product-listing-with-color-filter.twig #}
{% set cores = api.getColors() %}
{% set cor_selecionada = request.query.cor %}

<section class="products-with-filter">
  <aside class="filter-sidebar">
    <h3>Filtrar por Cor</h3>
    
    <form method="GET" class="color-filter-form">
      <div class="color-filter-group">
        {# Opção "Todas as cores" #}
        <div class="filter-item">
          <input type="radio" 
                 name="cor" 
                 value=""
                 id="filter-todas"
                 {% if not cor_selecionada %}checked{% endif %}>
          <label for="filter-todas">Todas as cores ({{ store.pageProducts.total }})</label>
        </div>
        
        {# Filtro de cores com paleta visual #}
        {% for cor in cores %}
          <div class="filter-item color-option">
            <input type="radio" 
                   name="cor" 
                   value="{{ cor.id }}"
                   id="filter-cor-{{ cor.id }}"
                   class="color-checkbox"
                   {% if cor_selecionada == cor.id %}checked{% endif %}
                   onchange="this.form.submit()">
            
            <label for="filter-cor-{{ cor.id }}">
              <span class="color-circle" 
                    style="background-color: {{ cor.cor1 }};"></span>
              <span class="color-name">{{ cor.nome }}</span>
              <span class="color-count">({{ cor.total_produtos }})</span>
            </label>
          </div>
        {% endfor %}
      </div>
      
      {# Limpar filtro #}
      {% if cor_selecionada %}
        <button type="reset" class="btn-clear-filter">Limpar filtros</button>
      {% endif %}
    </form>
  </aside>
  
  <main class="products-grid">
    <header class="products-header">
      <h2>Produtos{% if cor_selecionada %} - Cor: {{ cores[cor_selecionada].nome }}{% endif %}</h2>
      <p class="products-count">{{ store.pageProducts.total }} produto(s) encontrado(s)</p>
    </header>
    
    {# Lista de produtos (usando store.pageProducts) #}
    {% if store.pageProducts.product %}
      <div class="grid-products">
        {% for produto in store.pageProducts.product %}
          {% include 'widgets/product-card.twig' with {
            'product': produto,
            'available_colors': cores
          } only %}
        {% endfor %}
      </div>
    {% else %}
      <p class="no-products">Nenhum produto encontrado com essa cor.</p>
    {% endif %}
  </main>
</section>

<style>
  .products-with-filter {
    display: grid;
    grid-template-columns: 250px 1fr;
    gap: 30px;
    padding: 20px;
  }
  
  .filter-sidebar {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 20px;
    height: fit-content;
  }
  
  .color-filter-group {
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  
  .filter-item {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  
  .color-option label {
    display: flex;
    align-items: center;
    gap: 8px;
    cursor: pointer;
    flex: 1;
  }
  
  .color-circle {
    display: inline-block;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    border: 2px solid #ccc;
  }
  
  .color-option input:checked + label .color-circle {
    border-color: #000;
    box-shadow: inset 0 0 0 2px white, 0 0 0 3px #000;
  }
  
  .grid-products {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
  }
  
  .btn-clear-filter {
    width: 100%;
    padding: 10px;
    margin-top: 15px;
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    border-radius: 4px;
    cursor: pointer;
  }
  
  @media (max-width: 768px) {
    .products-with-filter {
      grid-template-columns: 1fr;
    }
  }
</style>
```

Saída esperada (HTML):

```html
<section class="products-with-filter">
  <aside class="filter-sidebar">
    <h3>Filtrar por Cor</h3>
    
    <form method="GET" class="color-filter-form">
      <div class="color-filter-group">
        <div class="filter-item">
          <input type="radio" name="cor" value="" id="filter-todas" checked>
          <label for="filter-todas">Todas as cores (24)</label>
        </div>
        
        <div class="filter-item color-option">
          <input type="radio" name="cor" value="559381" id="filter-cor-559381">
          <label for="filter-cor-559381">
            <span class="color-circle" style="background-color: #fff000;"></span>
            <span class="color-name">amarelo</span>
            <span class="color-count">(3)</span>
          </label>
        </div>
        
        <div class="filter-item color-option">
          <input type="radio" name="cor" value="559382" id="filter-cor-559382" checked>
          <label for="filter-cor-559382">
            <span class="color-circle" style="background-color: #0000ff;"></span>
            <span class="color-name">azul</span>
            <span class="color-count">(5)</span>
          </label>
        </div>
      </div>
      
      <button type="reset" class="btn-clear-filter">Limpar filtros</button>
    </form>
  </aside>
  
  <main class="products-grid">
    <header class="products-header">
      <h2>Produtos - Cor: azul</h2>
      <p class="products-count">5 produto(s) encontrado(s)</p>
    </header>
    
    <div class="grid-products">
      <!-- Cards de produtos filtrados por cor -->
    </div>
  </main>
</section>
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

**Problema**: `api.getColors()` retorna array vazio `[]`, seletor não renderiza.
**Diagnóstico**: Nenhuma cor cadastrada na loja, ou todas as cores estão desativadas.
**Solução**: Verificar painel wBuy se cores foram cadastradas e ativas. Debugar com `{{ pr(api.getColors()) }}` para ver resposta. Verificar campo `ativo: 1` em cada cor.

### Erro frequente 2: "Acesso a campo que não existe"

**Problema**: Tentando acessar `cor.hex_code` ou `cor.color_code` gera undefined no template.
**Diagnóstico**: Os campos reais retornados são `id`, `nome`, `cor1`, `cor2`, `ativo`, `tipo`, `grupo_id`, `grupo_cores`, `total_produtos`.
**Solução**: Usar os nomes corretos: `{{ cor.cor1 }}` para código hex da cor principal, `{{ cor.nome }}` para nome, `{{ cor.total_produtos }}` para quantidade de produtos.

### Erro frequente 3: "Cores desativadas aparecem no filtro"

**Problema**: Cores com `ativo: 0` são retornadas e aparecem no seletor de filtro.
**Diagnóstico**: `api.getColors()` retorna todas as cores, mesmo inativas.
**Solução**: Filtrar apenas cores ativas no template:

```twig
{% for cor in api.getColors({ativo: 1}) %}
  {# Renderizar cor #}
{% endfor %}
```

### Erro frequente 4: "Campo `total_produtos` sempre zero ou vazio"

**Problema**: Filtro mostra "(0)" ou "(undefined)" mesmo existindo produtos com essa cor.
**Diagnóstico**: Valor não é calculado automaticamente pela API — depende de quantos produtos estão marcados com aquela cor.
**Solução**: Esse campo reflete apenas produtos que têm a cor cadastrada. Se sempre retorna 0, verificar se os produtos foram vinculados corretamente às cores no painel.

## Veja também

- [getVariations](./getvariations.md) — Variações (SKU) de produtos por cor/tamanho
- [productGet](./productget.md) — Dados completos de produto incluindo cores disponíveis
- [Visão geral da API](./visao-geral-api.md) — Contexto e diferenças server-side vs client-side
