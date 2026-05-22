---
title: "store.widgetInstagram()"
slug: "store-widgetinstagram"
doc_type: "reference"
summary: "Método que disponibiliza widget de Instagram com feed de posts do lojista para integração social na loja."
tags:
  - store
  - widget
  - instagram
  - redes-sociais
related:
  - 04-store/visao-geral-store.md
  - 04-store/widgetfacebook.md
  - 04-store/socialicons.md
---

## O que faz

Disponibiliza um widget de Instagram configurado para a loja virtual. Este método integra o feed/posts do Instagram do lojista diretamente no template.

## Sintaxe

```twig
{% set instagram = store.widgetInstagram() %}
```

## Quando usar

- Para exibir feed de Instagram na loja
- Em rodapé ou áreas de destaque social
- Para integração com redes sociais
- Para criar seções de "Siga-nos no Instagram"

## Exemplo

```twig
{% set instagram = store.widgetInstagram() %}
{% if instagram.enabled %}
<section class="instagram-widget">
	<h3>{{ instagram.titulo }}</h3>
	<div id="instagram-feed" class="instagram-feed">
		{# O widget se autorenderiza via JavaScript #}
	</div>
	<script src="{{ instagram.script_url }}"></script>
</section>
{% endif %}
```

Saída esperada:
```
Widget de Instagram renderizado com posts
```

## Retorno dos dados

**enabled** (bool) - Se o widget está ativado

**titulo** (string) - Título do widget

**script_url** (string) - URL do script do widget

**conta** (string) - Nome da conta Instagram

**limite** (int) - Quantidade de posts a exibir

## Parâmetros de consulta

Nenhum parâmetro obrigatório.

## Observações

- Requer configuração de conta Instagram no painel
- O widget usa JavaScript para renderização
- Ideal para integração social
- Suporta customização de layout

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
