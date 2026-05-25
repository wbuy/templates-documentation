---
title: "Agrupador de produtos"
slug: "agrupador-de-produtos"
doc_type: "reference"
summary: "Componente que retorna produtos relacionados configurados no módulo Upsell e Cross-sell."
tags: ["html", "agrupador", "upsell", "cross-sell", "produtos-relacionados"]
related: ["05-html/html-productdetailsku.md", "05-html/productbox.md", "04-store/store-productdetail.md"]
---

## O que faz

O Agrupador de produtos é um componente responsável por retornar todos os produtos relacionados e linkados através do módulo Upsell e Cross-sell da plataforma. Este recurso permite exibir sugestões de compra complementar de forma automática.

O componente busca automaticamente os produtos que foram configurados como relacionados a um produto específico, agrupados conforme as definições de Upsell e Cross-sell feitas no painel de controle.

## Sintaxe

```html
<component data-modulo="product-grouper" loading="false" data-pid="{{ produto.id }}"></component>
```

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
| ----------- | ------ | ------------- | ----------- |
| `data-modulo` | string | Sim | Deve ser sempre `"product-grouper"` |
| `data-pid` | int | Sim | ID do produto da página atual |
| `loading` | bool | Não | Mostra loading enquanto processa (padrão: false) |

## Quando usar

- Na página de detalhes do produto para sugerir complementos
- Para aumentar valor médio de pedido através de recomendações
- Quando o lojista configurou produtos relacionados via Upsell/Cross-sell

## Exemplo

```html
<div class="produtos-relacionados">
  <component data-modulo="product-grouper" loading="false" data-pid="{{ extra.id }}"></component>
</div>
```

Saída esperada:

```text
HTML renderizado com os produtos relacionados configurados no painel, mantendo o layout definido no componente.
```

## Observações

- O id do produto é obrigatório para que o componente busque seus relacionados
- A quantidade de produtos e layout são definidos na configuração da loja
- Este é um componente dinâmico que é processado pela plataforma
- Se nenhum produto relacionado estiver configurado, o componente não renderizará
- Compatível com mobile e desktop

## Erros comuns

### Componente não exibe produtos

**Problema**: O agrupador não mostra nenhum produto
**Diagnóstico**: Verificar se foram configurados produtos relacionados no painel de controle do módulo Upsell/Cross-sell para o produto em questão
**Solução**: Acessar o painel, ir ao módulo Upsell/Cross-sell e vincular produtos ao item desejado

### ID do produto incorreto

**Problema**: O componente renderiza mas com produtos errados
**Diagnóstico**: O `data-pid` pode estar recebendo um valor inválido
**Solução**: Verificar que `{{ extra.id }}` ou `{{ produto.id }}` está sendo passado corretamente no contexto da página

## Veja também

- [html.productDetailSKU](05-html/html-productdetailsku.md)
- [html.buyTogether(produtoId)](05-html/html-buytogether-produtoid.md)
- [productBox](05-html/productbox.md)
