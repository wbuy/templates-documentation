---
title: "Widget Produto SKU"
slug: "widget-produto-sku"
doc_type: "reference"
summary: "Widget de detalhes do SKU para a página de detalhes do produto, exibindo valores, variações, estoque, frete e componentes de compra."
tags: ["widget", "produto", "sku", "detalhes", "carrinho"]
related:
  - 05-html/html-productdetailsku.md
  - 04-store/store-productdetail.md
---

## O que faz

Este widget renderiza a seção de detalhes de um SKU (unidade de estoque) específico na página de detalhes do produto. Exibindo informações como preço, desconto, parcelamento, disponibilidade, variações de cor/tamanho, tabela de medidas e componentes de ação (carrinho, frete).

O widget integra rastreamento Google Tags Manager para e-commerce e é dinamicamente atualizado quando o usuário muda a cor (foto e preço são recarregados).

## Estrutura HTML

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

## Componentes Inclusos

| Componente | Função |
| ----------- | -------- |
| `html.googletags` | Configuração Google Tags Manager para rastreamento |
| `html.pontoswb` | Sistema de pontos wBuy (programa de fidelidade) |
| `html.valor` | Exibição do preço/valor do SKU |
| `html.desconto` | Exibição de badge de desconto percentual |
| `html.compra_minima` | Aviso de quantidade mínima |
| `html.parcelamento` | Opções de parcelamento |
| `html.contador_regressivo` | Timer para promoções com prazo |
| `html.disponibilidade` | Indicador de estoque/disponibilidade |
| `html.valor_atacado` | Tabela de preços por quantidade |
| `html.ultimas_unidades` | Aviso "Últimas unidades em estoque" |
| `html.frete_gratis` | Indicador de frete grátis |
| `html.tabela_medidas` | Tabela com dimensões do produto |
| `html.info_assinatura` | Informações de assinatura/recorrência |
| `html.grade` | Grade de variações (cores, tamanhos) |
| `html.campos_adicionais` | Campos customizados do produto |
| `html.botao_carrinho` | Botão "Adicionar ao carrinho" |
| `html.calculo_frete` | Calculadora de frete por CEP |
| `html.caracteristicas` | Listagem de características/especificações |

## Variáveis Principais

| Variável | Descrição |
| ---------- | ---------- |
| `sku` | SKU do produto (identificador único) |
| `extra.id` | ID interno do produto |
| `html.matriz` | Dados da matriz do produto (cores, fotos) |
| `html.matriz.cor.id` | ID da cor selecionada |
| `html.matriz.tipo_fotos` | Tipo de foto (simples, galeria, 360, vídeo) |
| `html.matriz.grade_tipo` | Tipo de grade (grid, lista) |
| `html.matriz.produto` | Nome do produto |
| `html.matriz.valor_cliente.valor` | Preço para o cliente |

## Funcionalidades JavaScript

```javascript
var _cor_id = '{{ html.matriz.cor.id }}';

// Carrega fotos ao mudar de cor
productLoadPhotosByColor({
    cor_id: color,
    tipo_fotos: '{{ html.matriz.tipo_fotos }}'
});

// Carrega fotos em mobile
mobileLoadPhotosByColor(color);

// Atualiza variável de rastreamento
productPhotosColorSelected = _cor_id;
```

## Quando usar

- Em cada página de detalhes do produto
- Para exibir informações detalhadas de estoque e variações
- Quando há necessidade de integração com Google Analytics (ecommerce)
- Para permitir seleção de variações antes de adicionar ao carrinho

## Observações

- O widget depende de funções JavaScript globais (`productLoadPhotosByColor`, `mobileLoadPhotosByColor`)
- Atributo `data-loadingwhenchange="true"` recarrega conteúdo quando SKU muda
- Google Tags Manager é configurado automaticamente para rastreamento de impressões de produto
- A grade de variações pode ser exibida em grid (visual) ou lista
- Mudança de cor recarrega fotos do produto dinamicamente
- Compatível com produtos com múltiplas variações (cores, tamanhos, etc)
- Suporta produtos com assinatura/recorrência

## Erros comuns

### Erro frequente 1

**Problema**: Ao mudar cor, fotos não atualizam
**Diagnóstico**: Função `productLoadPhotosByColor` não existe ou tem erro
**Solução**: Verificar que a função está definida no arquivo global JS do template

### Erro frequente 2

**Problema**: Grade de variações não aparece ou está vazia
**Diagnóstico**: Produto não tem variações cadastradas no painel
**Solução**: Cadastrar cores/tamanhos no painel > Produtos > Variações e associar ao SKU

## Veja também

- [05-html/html-productdetailsku.md](../../05-html/html-productdetailsku.md)
- [04-store/store-productdetail.md](../../04-store/store-productdetail.md)
