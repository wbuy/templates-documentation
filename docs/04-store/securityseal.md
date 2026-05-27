---
title: "securitySeal"
slug: "securityseal"
doc_type: "concept"
summary: "Recurso responsável por exibir selos e badges de segurança/confiança da loja para aumentar credibilidade junto aos clientes."
tags:
  - store
  - segurança
  - badges
  - credibilidade
  - confiança
related:
  - 04-store/visao-geral-store.md
  - 04-store/getstoredata.md
---

## O que faz

O método `store.securitySeal()` retorna os selos de segurança cadastrados na loja virtual. O retorno é uma lista de links/ícones prontos para renderização em HTML, usados para reforçar confiança no checkout, rodapé ou páginas de produto.

## Sintaxe

```twig
{% set selos = store.securitySeal() %}
```

Com parâmetro opcional:

```twig
{% set selos = store.securitySeal({ mono: true }) %}
```

### Retorno

Retorna um array de strings HTML prontas para renderizar:

```json
[
  "<a href=\"https://...\" target=\"_blank\"><img src=\"/img/selo.png\" alt=\"Selo\" /></a>"
]
```

## Quando usar

- Para exibir selos de segurança no rodapé, checkout ou páginas de produto
- Quando a loja possui selos configurados no painel
- Para reforçar credibilidade e reduzir objeções de compra

## Exemplo

```twig
{% set selos = store.securitySeal() %}
{% if selos|length > 0 %}
  <div class="seals">
    {% for selo in selos %}
      <span>{{ selo|raw }}</span>
    {% endfor %}
  </div>
{% endif %}
```

## Observações

- O retorno já vem preparado em HTML; use `|raw` para renderização correta
- O parâmetro `mono` busca versões brancas com fundo transparente quando disponíveis
- A ordem dos selos segue o cadastro na loja

## Erros comuns

### Erro 1: Esquecer `|raw` no selo
**Problema**: O HTML aparece como texto na página.
**Diagnóstico**: Tags `<a>`/`<img>` visíveis no conteúdo.
**Solução**: Renderizar com `{{ selo|raw }}`.

### Erro 2: Não validar retorno vazio
**Problema**: Loop em array vazio gera seção sem conteúdo.
**Diagnóstico**: Container vazio no layout.
**Solução**: Verificar `if selos|length > 0` antes de iterar.

## Veja também

- [Visão geral store](04-store/visao-geral-store.md)
- [Get Store Data](04-store/getstoredata.md)
