---
title: "Visão geral da API"
slug: "visao-geral-api"
doc_type: "concept"
summary: "Panorama dos métodos de API consumidos em templates wBuy. Explicação das diferenças arquiteturais entre chamadas server-side (Twig) e client-side (AJAX), casos de uso e orientações de implementação."
tags:
  - api
  - visão-geral
  - arquitetura
  - server-side
  - client-side
  - ajax
  - twig
related:
  - 01-introducao/visao-geral.md
  - 02-twig/visao-geral-twig.md
  - 04-store/visao-geral-store.md
  - 01-introducao/documentacao-api.md
---

## O que faz

A plataforma wBuy expõe funcionalidades através de dois modelos de chamadas de API: **server-side** (processadas em Twig no servidor) e **client-side** (executadas via AJAX no navegador). Este arquivo contextualiza ambas as abordagens, explicando quando usar cada uma, arquitetura subjacente, diferenças de performance e segurança.

### Arquitetura em Duas Camadas

As APIs wBuy são acessadas em dois momentos distintos do ciclo de vida da página:

1. **Server-Side (Twig)** — Chamadas executadas no servidor durante a renderização do template
   - Dados disponíveis no contexto Twig como variáveis globais (`store`, `product`, `category`)
   - Funções helper (ex: `productGet()`, `categoryGetAll()`) permitem consultas adicionais
   - Resultado é "baked" no HTML, enviado pronto ao navegador
   
2. **Client-Side (AJAX)** — Chamadas executadas no navegador do usuário via JavaScript
   - Endpoints RESTful padrão retornam JSON
   - Ideal para interações dinâmicas e atualizações em tempo real
   - Requer controle de CORS e autenticação via token/session

### Quando Usar Cada Abordagem

| Aspecto | Server-Side (Twig) | Client-Side (AJAX) |
|---------|-------------------|-------------------|
| **Timing** | Template render | Interação do usuário |
| **Dados na página** | Pré-renderizados (SEO-friendly) | Carregados dinamicamente |
| **Performance inicial** | Mais lento (server processing) | Mais rápido (HTML menor) |
| **JavaScript required** | Não | Sim |
| **Cache** | Full page cache | Browser cache + CDN |
| **Exemplos** | Listar categorias, dados de produto | Filtros, busca, carrinho |

## Sintaxe

### Sintaxe Server-Side (Twig)

Chamadas em Twig usam o objeto global `store` ou funções helper especializadas:

```twig
{# Acesso direto ao objeto store #}
{{ store.name }}
{{ store.categories }}
{{ store.getColors() }}

{# Funções helper para consultas adicionais #}
{{ productGet(product_id, template) }}
{{ categoryGetAll() }}
{{ categoryGetLevel1() }}
```

### Sintaxe Client-Side (AJAX)

Endpoints RESTful retornam JSON e podem ser chamados via AJAX:

```javascript
// Padrão de URL
GET /api/v1/category/
GET /api/v1/product/
GET /api/v1/product/?id=123
POST /api/v1/customer/

// Exemplo com jQuery AJAX
$.ajax({
  url: '/api/v1/categories/',
  type: 'GET',
  dataType: 'json',
  success: function(data) {
    console.log(data);
  },
  error: function(xhr, status, error) {
    console.error('Erro:', error);
  }
});
```

## Quando usar

### Usar Server-Side (Twig) quando:

- Os dados são **necessários para renderizar a página inicial** (SEO crítico)
- Você precisa de **cache full-page** (performance ao máximo)
- Os dados **não mudam frequentemente** durante a sessão do usuário
- O usuário **não possui JavaScript** ou você precisa de fallback
- Exemplos: listagem de categorias, detalhes de produto, configurações da loja

### Usar Client-Side (AJAX) quando:

- Os dados são **carregados após a interação do usuário**
- Você precisa de **atualizações em tempo real** (carrinho, filtros)
- Os dados **variam muito** entre usuários ou sessões
- Você quer **reduzir o tamanho inicial do HTML**
- JavaScript **está garantido** no navegador (aplicação moderna)
- Exemplos: busca com autocomplete, filtros dinâmicos, adicionar ao carrinho

### Pré-condições

- **Server-Side**: Template Twig precisa ter acesso ao contexto correto (variáveis passadas pelo backend)
- **Client-Side**: Servidor deve permitir requisições CORS da origem do frontend; autenticação deve estar configurada

### Limitações

- **Server-Side**: Não pode ser atualizado sem reload de página; lógica complexa torna template difícil de manter
- **Client-Side**: Sem JavaScript, dados não aparecem; requer tratamento de erros e loading states

## Exemplo

### Server-Side (Twig)

```twig
{# Arquivo: templates/category-list.twig #}
<div class="category-list">
  {% for category in store.categories %}
    <div class="category-card">
      <h3>{{ category.name }}</h3>
      <p>{{ category.description }}</p>
      <a href="/categoria/{{ category.slug }}">Ver mais</a>
    </div>
  {% endfor %}
</div>
```

Saída esperada (HTML renderizado no servidor):

```html
<div class="category-list">
  <div class="category-card">
    <h3>Eletrônicos</h3>
    <p>Produtos eletrônicos em geral</p>
    <a href="/categoria/eletronicos">Ver mais</a>
  </div>
  <div class="category-card">
    <h3>Livros</h3>
    <p>Livros e publicações</p>
    <a href="/categoria/livros">Ver mais</a>
  </div>
</div>
```

### Client-Side (AJAX)

```javascript
// Arquivo: estruturas/center/search-filter.js
function loadFilteredProducts(query) {
  $.ajax({
    url: '/api/v1/search/',
    type: 'GET',
    data: { q: query },
    dataType: 'json',
    success: function(data) {
      // Renderizar resultados
      var html = data.products.map(function(p) {
        return '<div class="product-item">' +
               '<h4>' + p.name + '</h4>' +
               '<p class="price">R$ ' + p.price.toFixed(2) + '</p>' +
               '<button onclick="addToCart(' + p.id + ')">Adicionar</button>' +
               '</div>';
      }).join('');
      
      $('#results').html(html);
    },
    error: function(xhr, status, error) {
      console.error('Erro ao carregar produtos:', error);
    }
  });
}

// Event listener para input de busca
$('#search-input').on('input', function() {
  if ($(this).val().length > 2) {
    loadFilteredProducts($(this).val());
  }
});
```

## Observações

### Performance

- **Server-Side**: Reduz requisições do cliente, mas aumenta tempo de renderização no servidor. Ideal com cache full-page para evitar processamento repetido.
- **Client-Side**: Permite paralelização (múltiplas requisições simultâneas), mas cada usuário incorre latência de rede. Use CDN/caching agressivo para JSON.

### Cache

- **Server-Side**: Cache via reverse-proxy (Varnish/Redis) armazena HTML inteiro. Invalidar quando dados mudam (eventos de webhook no backend).
- **Client-Side**: Browser cache (headers `Cache-Control`, `ETag`) + CDN edge caching. Session-specific data não deve ser cacheado.

### Segurança

- **Server-Side**: Dados são confiáveis (servidor controla renderização). XSS é responsabilidade do template (usar `|escape` em Twig).
- **Client-Side**: Validar CORS, implementar rate-limiting em endpoints, evitar expor dados sensíveis em JSON.

### Impacto SEO e Mobile

- **Server-Side**: HTML renderizado server-side é crawlable por bots (Google, Bing). Melhor score de SEO.
- **Client-Side**: JavaScript precisa ser executado para conteúdo aparecer. Google indexa, mas mais lento; outros bots podem não conseguir.

## Erros comuns

### Erro frequente 1: "Mixing server-side e client-side sem coordenação"

**Problema**: Tentar carregar os mesmos dados via Twig E AJAX causa duplicação, inconsistência e confusão sobre qual versão é a "verdade".
**Diagnóstico**: Dados aparecem duas vezes, ou valores divergem entre página inicial e após clicar em filtro.
**Solução**: Definir claramente qual é a "fonte de verdade":

- Se página inicial precisa dos dados (SEO), use server-side + cache.
- Se dados só são usados após interação, use AJAX puro e não renderize server-side.
- Sincronizar via event listeners: quando AJAX carrega dados, atualizar estado no Twig via data attributes.

### Erro frequente 2: "Dados não aparecem após AJAX, mas não há erro"

**Problema**: Requisição retorna sucesso (status 200), mas DOM não atualiza.
**Diagnóstico**: Network tab mostra sucesso, console sem erros, mas página não muda.
**Solução**:

- Verificar se seletor do DOM existe: `$('#results')` pode ser null.
- Adicionar logging: `console.log(data)` para confirmar que dados estão chegando.
- Verificar se JavaScript está habilitado e bundle foi carregado.

## Veja também

- [Visão geral do Twig v2](../02-twig/visao-geral-twig.md) — Contexto e integração Twig em wBuy
- [Visão geral do objeto store](../04-store/visao-geral-store.md) — Dados globais disponíveis em templates
- [Documentação API (Postman)](../01-introducao/documentacao-api.md) — Referência técnica completa
- [categoryGetAll](./categorygetall.md) — Exemplo de função API server-side
- [productGet](./productget.md) — Exemplo de função API para dados de produto
