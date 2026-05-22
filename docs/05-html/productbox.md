---
title: "productBox"
slug: "productbox"
doc_type: "reference"
summary: "Componente que retorna os dados prontos para o Box do Produto em listagens e vitrines."
tags: ["html", "box", "produto", "listagem", "vitrine"]
related: ["05-html/html-productdetailsku.md", "04-store/producttobox.md", "04-store/pageproducts.md"]
---

## O que faz

Disponibiliza como retorno os dados prontos para o Box do Produto na loja virtual. Este componente é utilizado em listagens, buscas e vitrines para renderizar o card/box visual do produto com todas as informações essenciais: foto, título, valor, parcelamento, botões de ação, etc.

É necessário passar como parâmetro um produto obtido através de um laço for a partir da consulta em `store.productToBox()`.

## Sintaxe

```twig
{% set box = html.productBox(produto) %}

# para retornar com 3 fotos por produto
{% set box = html.productBox(produto, {total_fotos: '3'}) %}
```

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `produto` | object | Sim | Objeto produto retornado de `store.productToBox()` |
| `opcoes` | object | Não | Objeto com opções adicionais |
| `opcoes.total_fotos` | int | Não | Quantidade total de fotos a retornar (padrão: 2) |

## Estrutura do retorno

O objeto retornado contém os seguintes campos HTML (todos string raw):

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `url_relative` | string | URL que leva aos detalhes do produto |
| `fotos` | string raw | Contendo as fotos do produto |
| `selos` | string raw | Com os selos selecionados para o produto pelo lojista |
| `titulo` | string raw | Com o título do produto |
| `codigo` | string raw | Com o código do produto |
| `avaliacoes` | string raw | Com o código sobre as avaliações (estrelinhas) |
| `valor` | string raw | Com valores possíveis (à vista/parcelado) |
| `valor_atacado` | string raw | Com valores de atacado (quando existentes) |
| `parcelamento` | string raw | Com informações sobre parcelas |
| `recorrencia` | string raw | Com informações de assinatura/recorrência |
| `countdown` | string raw | Com contador regressivo para promoção |
| `frete_gratis` | string raw | Com informação de Frete Grátis |
| `html_cores` | string raw | Com as cores disponíveis para o produto |
| `html_variacoes` | string raw | Com as variações disponíveis |
| `html_atributos` | string raw | Com os atributos definidos |
| `categorias` | string raw | Com as categorias do produto |
| `desconto` | string raw | Com a porcentagem de desconto |
| `has_botoes` | bool | Indica se há botões para renderizar |
| `botao_olhar` | string raw | Com configuração para abertura da "espiadinha" (preview) |
| `botao_comprar` | string raw | Com configuração para detalhes/carrinho direto |

## Quando usar

- Em listagens de produtos (busca, categorias, vitrines)
- Para renderizar cards/boxes de produtos de forma padronizada
- Em qualquer contexto onde você percorre um array de produtos com `store.productToBox()`

## Exemplo

```twig
{% set box = html.productBox(produto) %}

<div class="item" data-id="{{ produto.id }}" data-sku="{{ produto.url_sku }}">
  <a href="{{ box.url_relative }}">
    {{ box.fotos }}
  </a>
  {{ box.selos }}
  {{ box.titulo }}
  {{ box.codigo }}
  {{ box.avaliacoes }}
  {{ box.valor }}
  {{ box.parcelamento }}
  {{ box.recorrencia }}
  {{ box.countdown }}
  {{ box.valor_atacado }}
  {{ box.frete_gratis }}
  {{ box.html_cores }}
  {{ box.html_variacoes }}
  {{ box.html_atributos }}
  {{ box.categorias }}
  {{ box.desconto }}

  {% if box.has_botoes %}
    <div class="botoes">
      {{ box.botao_olhar }}
      {{ box.botao_comprar }}
    </div>
  {% endif %}
</div>
```

Saída esperada:
```html
<!-- Card/box do produto com foto, título, valor, botões etc -->
<div class="item" data-id="123" data-sku="ABC123">
  <a href="/produto-exemplo">
    <!-- fotos renderizadas -->
  </a>
  <!-- selos, titulo, valor, botoes, etc -->
</div>
```

## Opções de parâmetros

| Parâmetro | Tipo | Padrão | Descrição |
|-----------|------|--------|-----------|
| `total_fotos` | int | 2 | A quantidade total de fotos que deve ser retornado por produto |

## Observações

- O retorno é HTML raw e seguro para interpolação direta
- Padrão de 2 fotos pode ser aumentado conforme necessidade de layout
- Todos os campos HTML são pré-renderizados pela plataforma
- Campos como `has_botoes` ajudam a renderizar condicionalmente
- Mobile: estrutura é responsiva conforme configuração da loja
- Cores e variações retornam elementos HTML prontos para seleção
- Compatível com sistemas de avaliação quando habilitado

## Erros comuns

### Fotos não aparecem

**Problema**: O campo `{{ box.fotos }}` retorna vazio
**Diagnóstico**: O produto pode não ter fotos cadastradas ou o objeto produto pode estar vazio
**Solução**: Verificar que `store.productToBox()` retornou produtos válidos e que possuem fotos

### Botões não aparecem

**Problema**: Mesmo com `has_botoes == true`, não há renderização dos botões
**Diagnóstico**: Os campos `botao_olhar` e `botao_comprar` podem estar condicionados à configuração
**Solução**: Confirmar que `{% if box.has_botoes %}` está envolvendo a div de botões e verificar configuração da loja

### total_fotos não funciona

**Problema**: Passa opção `total_fotos: 3` mas retorna só 2 fotos
**Diagnóstico**: O produto pode ter apenas 2 fotos cadastradas
**Solução**: Verificar quantidade de fotos do produto no painel; a função não retorna mais fotos do que existem

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
