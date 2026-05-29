---
title: "geral.hasOpolen"
slug: "geral-hasopolen"
doc_type: "concept"
summary: "Recurso responsável por mostrar as instituições participantes do programa O Pólen exclusivamente na página de detalhes do produto."
tags:
  - geral
  - opolen
  - página-detalhe
  - instituições
related:
  - 04-store/visao-geral-store.md
  - 04-store/store-productdetail.md
---

## O que faz

Recurso responsável por mostrar as instituições participantes do programa O Pólen quando o lojista tem contato com eles. Exclusivamente deve ser mostrado na página de detalhes do produto.

## Sintaxe

```twig
{% if geral.hasOpolen %}
  <opolen></opolen>
{% endif %}
```

### Retorno

```json
false // ou true, dependendo do contrato do lojista
```

## Quando usar

- Na página de detalhes do produto
- Quando o lojista tem contato ativo com O Pólen
- Para exibir instituições participantes do programa

## Exemplo

```twig
{% if geral.hasOpolen %}
<div class="opolen-container">
  <opolen></opolen>
</div>
{% endif %}
```

Saída esperada:
```
Componente de O Pólen renderizado na página
```

## Observações

- Esta é uma verificação booleana que retorna verdadeiro ou falso
- O componente `<opolen></opolen>` é um web component que gerencia sua própria renderização
- Deve ser usado exclusivamente na página de detalhes do produto
- Não há parâmetros a serem passados para esta verificação

## Erros comuns

### Erro 1: Renderizar fora da página de detalhes
**Problema**: O componente é inserido em home, categoria ou busca.
**Diagnóstico**: O Pólen não aparece ou gera inconsistência de layout.
**Solução**: Usar o bloco apenas no template de detalhes do produto.

### Erro 2: Não verificar `geral.hasOpolen`
**Problema**: O componente é renderizado sem contrato ativo.
**Diagnóstico**: A seção fica vazia ou não carrega instituições.
**Solução**: Envolver o componente com `{% if geral.hasOpolen %}`.

## Veja também

- [Store Product Detail](04-store/store-productdetail.md)
- [Visão geral store](04-store/visao-geral-store.md)
