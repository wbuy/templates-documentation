---
title: "geral.hasPerformaAI"
slug: "geral-hasperformaai"
doc_type: "concept"
summary: "Recurso responsável por mostrar vitrines dinâmicas do serviço PerformaAI quando o lojista tem contrato ativo."
tags:
  - geral
  - performaai
  - vitrines-dinâmicas
  - ia
related:
  - 04-store/visao-geral-store.md
  - 04-store/showcaseproduct.md
---

## O que faz

Recurso responsável por mostrar vitrines dinâmicas do serviço PerformaAI quando o lojista tem contrato com eles.

## Sintaxe

```twig
{% if geral.hasPerformaAI %}
	<performa></performa>
{% endif %}
```

### Retorno

```json
false
```

## Quando usar

- Quando o lojista tem contrato ativo com PerformaAI
- Para exibir vitrines dinâmicas geradas por IA
- Em seções de destaque de produtos

## Exemplo

```twig
{% if geral.hasPerformaAI %}
	<section class="performa-vitrines">
		<performa></performa>
	</section>
{% endif %}
```

Saída esperada:
```
Vitrines dinâmicas renderizadas pelo componente PerformaAI
```

## Observações

- Esta é uma verificação booleana que retorna verdadeiro ou falso
- O componente `<performa></performa>` gerencia sua própria renderização
- As vitrines são geradas dinamicamente de forma inteligente
- Não há parâmetros a serem passados para esta verificação

## Erros comuns

### Erro 1: Renderizar sem validar `geral.hasPerformaAI`
**Problema**: O componente é exibido quando não há contrato ativo.
**Diagnóstico**: A vitrine não carrega ou fica vazia.
**Solução**: Envolver o bloco com `{% if geral.hasPerformaAI %}`.

### Erro 2: Não prever fallback quando o recurso está indisponível
**Problema**: A área de vitrine fica vazia quando o recurso não está ativo.
**Diagnóstico**: Seções sem conteúdo em lojas sem PerformaAI.
**Solução**: Adicionar fallback visual ou ocultar a seção quando `geral.hasPerformaAI` for false.

## Veja também

- [Showcase Product](04-store/showcaseproduct.md)
- [Visão geral store](04-store/visao-geral-store.md)
