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

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
