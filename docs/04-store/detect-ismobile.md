---
title: "detect.isMobile()"
slug: "detect-ismobile"
doc_type: "reference"
summary: "Método que detecta se o acesso está sendo realizado por um dispositivo móvel, retornando um boolean."
tags:
  - store
  - detecção
  - mobile
  - responsivo
  - javascript
related:
  - 04-store/visao-geral-store.md
  - 04-store/recursos-gerais.md
---

## O que faz

O método `detect.isMobile()` é responsável pela detecção do tipo de dispositivo do usuário que está acessando a loja virtual. Ele analisa o User-Agent enviado pelo navegador para determinar se o acesso está acontecendo via dispositivo móvel (smartphone ou tablet) ou desktop.

Este método retorna um valor booleano (`true` ou `false`), permitindo que você implemente lógica condicional nos templates Twig para adaptar a apresentação e funcionalidades conforme o tipo de dispositivo.

## Sintaxe

```twig
{% if detect.isMobile() %}
  {# código executado em dispositivos móveis #}
{% else %}
  {# código executado em desktop #}
{% endif %}
```

**Tipo de retorno**: `boolean`

- `true` — Acesso via dispositivo móvel
- `false` — Acesso via desktop

## Quando usar

- Renderizar layouts diferentes para mobile vs desktop
- Carregar folhas de estilo específicas por tipo de dispositivo
- Mostrar/ocultar componentes com base no tipo de tela
- Aplicar eventos JavaScript diferentes para mobile e desktop
- Definir tamanhos de imagem otimizados para cada dispositivo

## Exemplo

```twig
{# Carregar CSS específico #}
{% if detect.isMobile() %}
  <link rel="stylesheet" href="/css/mobile.css">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
{% else %}
  <link rel="stylesheet" href="/css/desktop.css">
{% endif %}

{# Menu adaptativo #}
{% set menu_class = detect.isMobile() ? 'menu-mobile' : 'menu-desktop' %}
<nav class="{{ menu_class }}">
  {% include 'nav-' ~ menu_class ~ '.html' %}
</nav>
```

Saída esperada:

```html
{# Em mobile: #}
<link rel="stylesheet" href="/css/mobile.css">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<nav class="menu-mobile"><!-- menu mobile --></nav>

{# Em desktop: #}
<link rel="stylesheet" href="/css/desktop.css">
<nav class="menu-desktop"><!-- menu desktop --></nav>
```

## Observações

- Detecção baseada em User-Agent do servidor, não em tamanho de tela
- Use CSS media queries como complemento para layouts mais flexíveis
- Performance: Chamada muito leve, pode ser usada múltiplas vezes
- SEO: Google mobile crawler detecta corretamente o layout mobile

## Erros comuns

### Erro 1: Confundir com media queries CSS

**Problema**: Usar apenas `detect.isMobile()` esperando detectar responsividade
**Diagnóstico**: Tablets em paisagem aparecem com layout mobile
**Solução**: Combinar com CSS media queries para breakpoints reais

### Erro 2: Tratar como string em condicionais

**Problema**: `if detect.isMobile == 'true'` em vez de método
**Diagnóstico**: Condicional sempre true
**Solução**: Usar `detect.isMobile()` como boolean

## Veja também

- [Recursos gerais](04-store/recursos-gerais.md)
- [Visão geral store](04-store/visao-geral-store.md)
