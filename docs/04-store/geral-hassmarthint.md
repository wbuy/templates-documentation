---
title: "geral.hasSmartHint"
slug: "geral-hassmarthint"
doc_type: "concept"
summary: "Recurso do serviço SmartHint responsável por administrar vitrines dinâmicas quando o lojista tem contrato ativo."
tags:
  - geral
  - smarthint
  - vitrines-dinâmicas
  - ia
related:
  - 04-store/visao-geral-store.md
  - 04-store/showcaseproduct.md
---

## O que faz

Recurso do serviço SmartHint responsável por administrar vitrines dinâmicas na loja virtual caso o lojista tenha contrato ativo com eles.

## Sintaxe

```twig
{% if geral.hasSmartHint %}
	<div id="smarthint-position-1"></div>
	<div id="smarthint-position-2"></div>
	<div id="smarthint-position-3"></div>
	<div id="smarthint-position-4"></div>
	<div id="smarthint-position-5"></div>
{% endif %}
```

## Quando usar

- Quando o lojista tem contrato ativo com SmartHint
- Para exibir vitrines dinâmicas em posições específicas
- Para incrementar recomendações inteligentes de produtos

## Exemplo

```twig
{% if geral.hasSmartHint %}
	<div id="smarthint-position-1"></div>
	<div id="smarthint-position-2"></div>
	<script>
	$(function(){
		SmartHint.Call('setPage',{type:'home', data: {} });
	});
	</script>
{% endif %}
```

Saída esperada:
```
Vitrines SmartHint renderizadas nas posições definidas
```

## Observações

- Suporta até 5 posições (smarthint-position-1 até smarthint-position-5)
- Requer a biblioteca JavaScript do SmartHint carregada
- Na variável "type" do método SmartHint.Call, informe a qual página está sendo inserido o código
- As posições renderizam vitrines inteligentes baseadas em IA

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
