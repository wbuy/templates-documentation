---
title: "Exemplo: Página de produto com SKU"
slug: "pagina-produto-com-sku"
doc_type: "example"
summary: "Widget para exibição de detalhes completos do produto com seleção de SKU."
tags:
  - exemplos
  - produto
  - sku
  - widget
  - detalhes
related:
  - 05-html/html-productdetailsku.md
  - 04-store/store-productdetail.md
  - 04-store/cart.md
---

## O que faz

Widget de exemplo para ser incluído na página de detalhes do produto. Responsável por exibir informações completas do SKU selecionado, incluindo valores, descontos, parcelamento, disponibilidade, grade de variações (cores, tamanhos) e opções de compra. Integra Google Analytics e sistema de pontos wBuy.

## Sintaxe

```twig
{% set html = html.productDetailSKU(sku, extra.id) %}
{%
 set setTagsEcommerceProductDetail = store.setTagsEcommerceProductDetail({
        id: extra.id,
  sku: sku,
  name: html.matriz.produto,
  quantity: 1,
  price: html.matriz.valor_cliente.valor,
 })
%}

<div id="produto-sku" data-sku="{{ sku }}" data-widget="produto-sku-html.html" data-loadingwhenchange="true">
 {{ html.googletags }}
 {{ html.pontoswb }}
 {{ html.valor }}
 {{ html.desconto }}
 {{ html.compra_minima }}
 {{ html.parcelamento }}
 {{ html.contador_regressivo }}
 {{ html.disponibilidade }}
 {{ html.valor_atacado }}
 {{ html.ultimas_unidades }}
 {{ html.frete_gratis }}
 {{ html.tabela_medidas }}
    {{ html.info_assinatura }}

 <div class="estoque">
  {{ html.grade }}
  {{ html.campos_adicionais }}
 </div>

 <div class="botoes">
  {{ html.botao_carrinho }}
  {{ html.calculo_frete }}
 </div>

 {{ html.caracteristicas }}
</div>

<script>
 var _cor_id = '{{ html.matriz.cor.id }}';
 $(function(){
  if(productPhotosColorSelected != _cor_id){
   mobileLoadPhotosByColor(_cor_id);
   productLoadPhotosByColor({
    cor_id: _cor_id,
    tipo_fotos: '{{ html.matriz.tipo_fotos }}',
   });
   productPhotosColorSelected = _cor_id;
  }

  {% if html.matriz.grade_tipo == 'grid' %}
  $('#geral, #mymodal').on('click', '.grade .l .cor .item', function(){
   let _th = $(this);
   let color = _th.data('cor');
   productLoadPhotosByColor({
    cor_id: color,
    tipo_fotos: '{{ html.matriz.tipo_fotos }}',
   });
   mobileLoadPhotosByColor(color);
  });
  {% endif %}
 });
</script>

{{ setTagsEcommerceProductDetail }}
```

## Variáveis Disponíveis

A função `html.productDetailSKU()` retorna um objeto contendo:

- `googletags` - Tags para Google Analytics
- `pontoswb` - Sistema de pontos wBuy
- `valor` - Preço do produto
- `desconto` - Informações de desconto
- `compra_minima` - Quantidade mínima de compra
- `parcelamento` - Opções de parcelamento
- `contador_regressivo` - Oferta com tempo limitado
- `disponibilidade` - Status de estoque
- `valor_atacado` - Preço para compras em quantidade
- `ultimas_unidades` - Aviso de produtos limitados
- `frete_gratis` - Indicador de frete grátis
- `tabela_medidas` - Tabela de medidas do produto
- `info_assinatura` - Informações de assinatura/recorrência
- `grade` - Seleção de variações (cores, tamanhos)
- `campos_adicionais` - Campos customizados
- `botao_carrinho` - Botão para adicionar ao carrinho
- `calculo_frete` - Widget de cálculo de frete
- `caracteristicas` - Especificações do produto
- `matriz` - Dados da matriz do SKU (cor, fotos, tipo_fotos, grade_tipo)

## Quando usar

- Página de detalhes de produto com múltiplas variações
- Quando há SKUs diferentes por cor/tamanho
- Para integração com Google Analytics (ecommerce tracking)
- Quando o sistema de pontos wBuy está ativo

## Exemplo

```twig
{% set sku = 'ABC123' %}
{% set html = html.productDetailSKU(sku, extra.id) %}

<div id="produto-sku" data-sku="{{ sku }}">
  {{ html.valor }}
  {{ html.parcelamento }}
  {{ html.disponibilidade }}
  {{ html.grade }}
  {{ html.botao_carrinho }}
</div>
```

Saída esperada:

```html
<div id="produto-sku" data-sku="ABC123">
  <!-- Renderização de preço -->
  <!-- Opções de parcelamento -->
  <!-- Status de disponibilidade -->
  <!-- Grade de cores/tamanhos -->
  <!-- Botão de adicionar ao carrinho -->
</div>
```

## Observações

- Carregamento dinâmico: Ao trocar SKU, a página atualiza com `data-loadingwhenchange="true"`
- Fotos do produto atualizam ao selecionar cor diferente
- Suporta grade em tipo "grid" ou "lista"
- Integração automática com Google Analytics para rastreamento de ecommerce
- Compatível com mobile e responsivo

## Erros comuns

### Erro 1: Fotos não atualizam ao trocar cor

**Problema**: Grade de cores selecionada mas imagens não mudam
**Diagnóstico**: Função `productLoadPhotosByColor()` não definida
**Solução**: Incluir script de carregamento de fotos antes do widget

### Erro 2: SKU não encontrado

**Problema**: Widget exibe erro ou não carrega dados
**Diagnóstico**: `extra.id` ou `sku` inválidos
**Solução**: Verificar se produto existe e se SKU está ativo no sistema

### Erro 3: Parcelamento não exibe

**Problema**: Campo `html.parcelamento` vazio
**Diagnóstico**: Configurações de parcelamento não ativas
**Solução**: Habilitar parcelamento nas configurações de pagamento da loja

## Veja também

- [html.productDetailSKU()](../05-html/html-productdetailsku.md) — Função de renderização SKU
- [store.productDetail()](../04-store/store-productdetail.md) — Dados completos do produto
- [cart()](../04-store/cart.md) — Gerenciar carrinho de compras
