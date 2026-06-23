---
title: "productBoxDefault"
slug: "productboxdefault"
doc_type: "reference"
summary: "Método que retorna box de produto formatado com layout padrão wBuy pronto para renderização em HTML."
tags:
  - store
  - produtos
  - box
  - rendering
related:
  - 04-store/visao-geral-store.md
  - 04-store/producttobox.md
---

## O que faz

Disponibiliza como retorno os dados prontos do Box do Produto na loja virtual. Este método retorna um box de produto padrão wBuy montado, diferentemente de html.productBox() que retorna dados separados.

## Sintaxe

```twig
{{ store.productBoxDefault(produto) }}
{# com parâmetros #}
{{ store.productBoxDefault(produto, {total_fotos: 2}) }}
```

### Retorno

```json
"<div class=\"product-box\">...</div>"
```

## Quando usar

- Para exibir caixas de produtos de forma padronizada
- Em listas de produtos com layout padrão wBuy
- Quando usa store.productToBox() para recuperar produtos
- Para manter consistência visual em toda a loja

## Exemplo

```twig
{% set produtosBox = store.productToBox({limit:'4', order:'random'}) %}
<div class="row">
  {% for produto in produtosBox.data %}
  <div class="col-md-3">
  {{ store.productBoxDefault(produto) }}
  </div>
  {% endfor %}
</div>
```

Saída esperada:

```text
Boxes de produtos renderizadas com layout padrão wBuy
```

## Retorno dos dados

Este método retorna HTML já renderizado com a caixa do produto formatada com:

- Imagem do produto
- Título
- Preço
- Botão de compra
- Avaliações (se configurado)
- Frete grátis (se aplicável)

## Parâmetros de consulta

| Parâmetro | Padrão | Descrição |
| ---------- | --------- | ------------- |
| total_fotos | 2 | A quantidade total de fotos que deve ser retornado por produto |

## Observações

- É necessário passar um produto como parâmetro (recuperado de store.productToBox)
- Diferentemente de html.productBox(), este método retorna HTML completo
- Segue o layout padrão definido no painel de controle
- Os dados devem vir de store.productToBox() para compatibilidade

## Erros comuns

### Erro 1: Passar produto fora do formato esperado

**Problema**: O box quebra ou não renderiza detalhes.
**Diagnóstico**: Produto não veio de `store.productToBox()`.
**Solução**: Sempre usar itens de `produtosBox.data` como entrada.

### Erro 2: Não limitar a quantidade de fotos

**Problema**: Layout desalinhado com muitas imagens.
**Diagnóstico**: Galerias maiores que o esperado.
**Solução**: Ajustar `total_fotos` conforme o layout do template.

## Veja também

- [Product To Box](04-store/producttobox.md)
- [Visão geral store](04-store/visao-geral-store.md)
