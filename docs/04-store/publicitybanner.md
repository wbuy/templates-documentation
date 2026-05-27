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
{% set banner = store.publicityBanner() %}
{# com parâmetro #}
{% set banner = store.publicityBanner({tipo: '21', limit: '1'}) %}
```

### Retorno

```json
[
  {
    "id": 0,
    "tipo": 0,
    "formato": 0,
    "identificacao": "",
    "arquivo": "",
    "url": "",
    "target": "",
    "codigo": "",
    "raw": ""
  }
]
```

## Quando usar

- Para exibir banners de promoção/publicidade
- Em barras laterais ou espaços dedicados
- Para rotacionar banners de diferentes campanhas
- Em rodapé ou áreas de destaque secundárias

## Exemplo

```twig
{% set bannerTopo = store.publicityBanner({tipo: '21', limit: '1'}) %}
{% if bannerTopo|length > 0 %}
	<div class="central">
		<div class="b_header mb-4">
			{{ bannerTopo[0].raw|raw }}
		</div>
	</div>
{% endif %}
```

Saída esperada:
```
Banners publicitários exibidos nas áreas definidas
```

## Retorno dos dados

**id** - ID do banner
**tipo** - Tipo do banner (conforme lista de parâmetros)
**formato** - Formato: 1 = imagem; 2 = código/script
**identificacao** - Identificador do banner
**arquivo** - URL da imagem do banner
**url** - Link para abertura no clique
**target** - Target do link
**codigo** - Script do banner quando `formato` for 2
**raw** - Banner pronto para inserção no código

## Parâmetros de consulta

| Parâmetro | Padrão | Descrição |
|-----------|---------|-------------|
| tipo | '' | Filtra pelo tipo do item (ex.: 21, 22, 23...) |
| order | random | Ordenação dos resultados (posicao-asc, posicao-desc, random) |
| produto_id | '' | ID do produto para priorizar banner na página de detalhes |
| limit | 10 | Limita a quantidade de itens retornados |

## Observações

- Diferentes de banners principais (mainBanner)
- Usados para promoções secundárias e campanhas específicas
- `raw` já vem pronto para inserção no HTML com `|raw`
- O parâmetro `produto_id` é útil na página de detalhes do produto

## Erros comuns

### Erro 1: Não usar `|raw` no banner
**Problema**: O HTML do banner aparece como texto.
**Diagnóstico**: Tags renderizadas na página.
**Solução**: Renderizar com `{{ banner.raw|raw }}`.

### Erro 2: Não validar lista vazia
**Problema**: A área do banner fica vazia.
**Diagnóstico**: Retorno sem itens.
**Solução**: Verificar `if bannerTopo|length > 0` antes de renderizar.

## Veja também

- [Main Banner](04-store/mainbanner.md)
- [Visão geral store](04-store/visao-geral-store.md)
