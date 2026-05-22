---
title: "widgetFacebook"
slug: "widgetfacebook"
doc_type: "reference"
summary: "Método que disponibiliza widget do Facebook com Page Plugin para integração de página do lojista na loja virtual."
tags:
  - store
  - widget
  - facebook
  - redes-sociais
related:
  - 04-store/visao-geral-store.md
  - 04-store/widgetinstagram.md
  - 04-store/socialicons.md
---

## O que faz

Disponibiliza um widget do Facebook configurado para a loja virtual. Este método integra elementos do Facebook (página, plugin social, etc) diretamente no template.

## Sintaxe

```twig
{% set facebook = store.widgetFacebook() %}
```

## Quando usar

- Para exibir Page Plugin do Facebook
- Em rodapé ou áreas de redes sociais
- Para integração com página do Facebook
- Em seções "Siga-nos no Facebook"

## Exemplo

```twig
{% set facebook = store.widgetFacebook() %}
{% if facebook.enabled %}
<section class="facebook-widget">
	<h3>{{ facebook.titulo }}</h3>
	<div id="facebook-plugin"
	     data-href="{{ facebook.pagina_url }}"
	     data-width="300"
	     data-height="500"
	     data-small-header="false"
	     data-adapt-container-width="true"
	     data-hide-cover="false"
	     data-show-facepile="true">
	</div>
	<script async defer crossorigin="anonymous"
		src="https://connect.facebook.net/pt_BR/sdk.js#xfbml=1&version=v12.0"></script>
</section>
{% endif %}
```

Saída esperada:
```
Widget do Facebook renderizado com página integrada
```

## Retorno dos dados

**enabled** (bool) - Se o widget está ativado

**titulo** (string) - Título do widget

**pagina_url** (string) - URL da página do Facebook

**pagina_id** (string) - ID da página

**largura** (int) - Largura do widget

**altura** (int) - Altura do widget

## Parâmetros de consulta

Nenhum parâmetro obrigatório.

## Observações

- Requer configuração de página do Facebook no painel
- O widget é renderizado pelo script oficial do Facebook
- Ideal para integração social e engajamento
- Suporta customização de tamanho e opções

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
