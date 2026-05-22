---
title: "Visao geral dos componentes HTML"
slug: "visao-geral-html"
doc_type: "concept"
summary: "Componentes HTML pré-construídos que retornam elementos dinâmicos prontos para uso em templates."
tags: ["html", "componentes", "templates"]
related: ["05-html/agrupador-de-produtos.md", "05-html/html-buytogether-produtoid.md", "05-html/html-productdetailsku.md", "05-html/productbox.md"]
---

## O que faz

Os componentes HTML da plataforma wBuy disponibilizam elementos pré-construídos que retornam estruturas HTML completas e prontas para uso direto em seus templates. Esses componentes encapsulam a lógica de apresentação de dados dinâmicos, permitindo que você insira dados complexos de forma simples e padronizada.

Os principais componentes disponíveis são:

- **html.productDetailSKU** — retorna os elementos HTML dos dados dinâmicos da página de detalhes do produto para um SKU específico
- **html.productBox** — retorna os dados prontos para o box do produto em listagens
- **html.buyTogether** — exibe o bloco "Compre Junto" quando configurado
- **Agrupador de produtos** — exibe produtos relacionados através do módulo Upsell/Cross-sell

## Quando usar

- Quando você precisa exibir dados dinâmicos de produtos de forma padronizada
- Para manter consistência visual com a plataforma
- Quando a complexidade da estrutura HTML justifica reutilização de componentes
- Em listagens de produtos, detalhes e vitrines

## Limitações

- A estrutura HTML retornada é pré-definida pela plataforma
- Customizações profundas requerem criação de widgets personalizados
- Alguns componentes possuem dependências de JavaScript pré-carregado

## Exemplo de uso

A maioria dos componentes segue o padrão:

```twig
{% set dados = html.componente(parametros) %}
{{ dados }}
```

## Observações

- Todos os componentes retornam HTML raw (seguro para interpolação direta)
- A documentação individual de cada componente detalha seus parâmetros e retorno
- Alguns componentes requerem JavaScript pré-configurado para funcionar corretamente
- O comportamento em cache segue as regras gerais da plataforma

## Veja também

- [Agrupador de produtos](05-html/agrupador-de-produtos.md)
- [html.buyTogether(produtoId)](05-html/html-buytogether-produtoid.md)
- [html.productDetailSKU](05-html/html-productdetailsku.md)
- [productBox](05-html/productbox.md)
