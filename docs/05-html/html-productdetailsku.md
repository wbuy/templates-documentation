---
title: "html.productDetailSKU"
slug: "html-productdetailsku"
doc_type: "reference"
summary: "Retorna os elementos HTML dos dados dinâmicos da página de detalhes do produto para um SKU específico."
tags: ["html", "produto", "sku", "detalhes", "dinâmico"]
related: ["05-html/productbox.md", "04-store/store-productdetail.md", "02-twig/loops-for.md"]
---

## O que faz

Disponibiliza como retorno os elementos HTML dos dados dinâmicos da página de detalhes do produto. Este componente encapsula toda a lógica de renderização de informações do SKU como valores, descontos, parcelamento, disponibilidade, grade de cores/tamanhos e muito mais.

O componente retorna tanto as estruturas HTML prontas para exibição quanto um objeto `matriz` contendo todos os dados estruturados do SKU para uso em lógica customizada.

## Sintaxe

```twig
{% set html = html.productDetailSKU(sku, produto_id) %}
{{ html.campo }}
```

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `sku` | string | Sim | O SKU recebido na tela-pai (detalhes do produto) |
| `produto_id` | int | Sim | ID do produto da página atual (extra.id) |

**Obrigatoriedade**: Ambos os parâmetros são obrigatórios para que o componente funcione.

## Estrutura do retorno

O componente retorna um objeto com campos HTML pré-renderizados e um objeto `matriz` com dados estruturados:

### Campos HTML (string raw)

| Campo | Descrição |
|-------|-----------|
| `googletags` | `<div>` com tags montadas para Google Retargeting |
| `pontoswb` | `<div.clube-info-pontos>` com pontos de fidelização |
| `valor` | `<div.valores>` com informações de preço |
| `valor_atacado` | `<div.valor_atacado>` com valor de atacado (quando existente) |
| `desconto` | `<p.desconto>` com informações de desconto |
| `compra_minima` | `<p.compra_minima>` com quantidade mínima |
| `parcelamento` | `<div.parcelas>` com opções de parcelamento |
| `contador_regressivo` | `<div.countdown>` com contador de promoção |
| `disponibilidade` | `<p.disponibilidade>` com prazo de entrega |
| `ultimas_unidades` | `<p.ultimas_unidades>` quando estoque baixo |
| `frete_gratis` | `<p.frete_gratis>` com informativo de frete grátis |
| `grade` | `<div>` com a grade de cores/tamanhos |
| `campos_adicionais` | `<div.campos_adicionais>` com campos customizados |
| `botao_carrinho` | `<div.row-botao-carrinho>` para adicionar ao carrinho |
| `calculo_frete` | `<div#calculo_frete>` com script de cálculo de frete |
| `tabela_medidas` | `<button.tabela_medidas>` para abrir modal de medidas |
| `info_assinatura` | `<div>` com informações de assinatura/recorrência |

### Objeto matriz (dados estruturados)

O objeto `html.matriz` contém:

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | int | ID do SKU |
| `sku` | string | Código SKU |
| `quantidade_em_estoque` | int | Quantidade atual em estoque |
| `prazo_producao` | int | Prazo em dias úteis |
| `produto_url` | string | URL do produto |
| `grade_tipo` | string/int | Tipo de grade (grid, lista, etc) |
| `cor.id` | int | ID da cor selecionada (quando aplicável) |
| `tipo_fotos` | string | Tipo de foto do produto |

## Quando usar

- Na página de detalhes do produto para exibir informações do SKU selecionado
- Para renderizar dados dinâmicos sem necessidade de lógica customizada
- Quando precisa de valores, parcelamento, disponibilidade e grade de seleção

## Restrição importante

⚠️ **Obrigatoriamente coloque suas variáveis dinâmicas dentro de um `div#produto-sku`**, caso contrário não irão funcionar os elementos em JavaScript pré-programado.

## Exemplo

```twig
{% set html = html.productDetailSKU(sku, extra.id) %}

{% set setTagsEcommerceProductDetail = store.setTagsEcommerceProductDetail({
  id: extra.id,
  sku: sku,
  name: html.matriz.produto,
  quantity: 1,
  price: html.matriz.valor_cliente.valor,
}) %}

<div id="produto-sku" data-sku="{{ sku }}" data-widget="produto-sku-html.html" data-loadingwhenchange="false">
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

Saída esperada:
```html
<!-- Estrutura HTML completa com valores, parcelamento, grade, botões, etc -->
```

## Atributos data do div#produto-sku

| Atributo | Tipo | Obrigatório | Padrão | Descrição |
|----------|------|-------------|--------|-----------|
| `data-sku` | string | Sim | — | O SKU do produto setado na tela-pai |
| `data-widget` | string | Sim | — | Nome do seu widget dinâmico na árvore de widgets (ex: `produto-sku-html.html`) |
| `data-loadingwhenchange` | bool | Não | false | Mostra loading enquanto processa o carregamento do novo SKU |

## Observações

- O retorno é HTML raw e seguro para interpolação direta
- JavaScript pré-carregado da plataforma monitora mudanças de SKU no div#produto-sku
- Quando a grade é tipo 'grid', cliques em cores disparam carregamento de fotos via jQuery
- O cache segue regras globais; SKUs podem ter cache longo pois dados são estáticos
- Mobile: todos os elementos são responsivos conforme configuração da loja
- Compatível com sistemas de parcelamento múltiplos (múltiplos gateways)

## Erros comuns

### Elementos não funcionam após mudança de SKU

**Problema**: Grade, botão de carrinho ou outros elementos não respondem após selecionar novo SKU
**Diagnóstico**: O `div#produto-sku` pode não estar envolvendo corretamente todos os elementos
**Solução**: Verificar que TODOS os campos `{{ html.* }}` estão dentro do `div#produto-sku` com `id="produto-sku"` correto

### Fotos não mudam ao selecionar cor

**Problema**: Ao clicar em cores da grade, as fotos não atualizam
**Diagnóstico**: Funções `productLoadPhotosByColor` ou `mobileLoadPhotosByColor` podem não estar carregadas
**Solução**: Verificar que seu template carrega os scripts necessários e que `html.matriz.grade_tipo` retorna 'grid'

### Parcelamento mostra valor errado

**Problema**: Valores de parcelas não correspondem ao preço do SKU
**Diagnóstico**: Pode haver mismatch entre o sku passado e o product_id
**Solução**: Confirmar que `sku` corresponde ao SKU selecionado e `extra.id` é o ID correto do produto

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
