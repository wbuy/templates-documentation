---
title: "publicityBanner"
slug: "publicitybanner"
doc_type: "reference"
summary: "Método que retorna banners publicitários para promoções e campanhas especiais em múltiplas posições da loja."
tags:
  - store
  - banners
  - publicidade
  - promoções
related:
  - 04-store/visao-geral-store.md
  - 04-store/mainbanner.md
---

## O que faz

Disponibiliza como retorno banners publicitários da loja virtual. Estes são banners especiais para promoções e publicidade, diferentes dos banners principais (mainBanner).

## Sintaxe

```twig
{% set banners_pub = store.publicityBanner() %}
{# com parâmetro #}
{% set banners_pub = store.publicityBanner({posicao: 1}) %}
```

## Quando usar

- Para exibir banners de promoção/publicidade
- Em barras laterais ou espaços dedicados
- Para rotacionar banners de diferentes campanhas
- Em rodapé ou áreas de destaque secundárias

## Exemplo

```twig
{% set banners_pub = store.publicityBanner() %}
{% for banner in banners_pub.items %}
<div class="publicity-banner">
	<a href="{{ banner.link }}">
		<img src="{{ banner.foto }}" alt="{{ banner.titulo }}" />
	</a>
</div>
{% endfor %}
```

Saída esperada:
```
Banners publicitários exibidos nas áreas definidas
```

## Retorno dos dados

**items** - Array de banners publicitários
- `items[x].id` (string) - ID do banner
- `items[x].titulo` (string) - Título
- `items[x].foto` (string) - URL da imagem
- `items[x].link` (string) - URL do link
- `items[x].target` (string) - Target do link
- `items[x].posicao` (int) - Posição de exibição

## Parâmetros de consulta

| Parâmetro | Padrão | Descrição |
|-----------|---------|-------------|
| posicao | '' | Filtrar por posição do banner |

## Observações

- Diferentes de banners principais
- Usados para promoções secundárias
- Podem estar em múltiplas posições da loja
- Suportam imagens e links personalizados

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
