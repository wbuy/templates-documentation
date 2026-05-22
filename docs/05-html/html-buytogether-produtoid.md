---
title: "html.buyTogether(produtoId)"
slug: "html-buytogether-produtoid"
doc_type: "reference"
summary: "Componente que exibe o bloco 'Compre Junto' na página de detalhes do produto quando configurado."
tags: ["html", "compre-junto", "produto", "upsell"]
related: ["05-html/agrupador-de-produtos.md", "05-html/html-productdetailsku.md", "04-store/store-productdetail.md"]
---

## O que faz

Este recurso permite exibir o bloco "Compre Junto" na página de detalhes de um produto quando este tem configurado na plataforma. O componente retorna toda a estrutura HTML necessária para apresentar produtos que devem ser vendidos em conjunto.

## Sintaxe

```twig
{% set compreJunto = html.buyTogether(produto_id) %}
{{ compreJunto }}
```

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|-------------|-----------|
| `produto_id` | int | Sim | ID do produto que está sendo visualizado |

**Retorno:**

| Campo | Tipo | Descrição |
|-------|------|-----------|
| saída | string (raw HTML) | HTML formatado com o bloco Compre Junto pronto para renderizar |

## Quando usar

- Na página de detalhes do produto para sugerir compras em lote/pacote
- Quando o lojista configurou produtos no módulo "Compre Junto"
- Para aumentar ticket médio oferecendo kits de produtos

## Exemplo

```twig
{% set compreJunto = html.buyTogether(extra.id) %}

<section class="compre-junto">
  {{ compreJunto }}
</section>
```

Saída esperada:
```html
<!-- HTML da estrutura Compre Junto com produtos, valores e botões de compra -->
<div class="bloco-compre-junto">
  <!-- produtos configurados -->
</div>
```

## Observações

- O ID do produto é obrigatório para retornar os dados corretos
- Se nenhum "Compre Junto" estiver configurado para o produto, a função retorna vazio
- O HTML retornado é raw e pode ser interpolado diretamente
- Compatível com todas as variações de produto
- A estrutura visual é pré-definida pela plataforma

## Erros comuns

### Bloco Compre Junto não aparece

**Problema**: A função não retorna nada
**Diagnóstico**: O produto pode não ter configuração de Compre Junto no painel
**Solução**: Acessar o painel de controle, ir ao módulo "Compre Junto" e configurar produtos para este item

### ID do produto incorreto

**Problema**: Dados do Compre Junto aparecem errados
**Diagnóstico**: O `produto_id` passado pode estar inválido
**Solução**: Verificar que está usando `{{ extra.id }}` ou outra variável que contenha o ID correto do produto da página atual

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
