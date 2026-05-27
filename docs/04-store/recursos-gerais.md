---
title: "Recursos gerais"
slug: "recursos-gerais"
doc_type: "concept"
summary: "Compilação de recursos, métodos, variáveis e flags globais disponíveis para implementação de templates wBuy."
tags:
  - recursos
  - variáveis-globais
  - métodos
  - configurações
  - documentação
related:
  - 04-store/visao-geral-store.md
  - 04-store/detect-ismobile.md
  - 04-store/array-global.md
---

## O que faz

Recursos gerais é uma documentação centralizadora que lista todas as variáveis globais, métodos, funções e flags de configuração disponíveis ao desenvolver templates para a plataforma wBuy. Ela compreende strings de URL, dados de página, arrays de configuração, métodos de detecção, e flags de funcionalidades especiais.

Este compêndio é constantemente atualizado conforme novas funcionalidades são adicionadas à plataforma. Recomenda-se revisar regularmente para acompanhar novas possibilidades de integração.

## Sintaxe

Os recursos gerais são acessados diretamente no Twig ou JavaScript, sem necessidade de importação:

```twig
{{ base_system }}           {# string - URL do servidor #}
{{ base }}                  {# string - URL base da loja #}
{{ page }}                  {# string - nome da página atual #}
{{ extra.id }}              {# array - parâmetros da URL #}
{{ detect.isMobile() }}     {# boolean - detecção de mobile #}
{{ global.var_mostruario }} {# boolean - flag de mostruário #}
```

## Quando usar

- Construir URLs dinâmicas baseadas na estrutura da loja
- Identificar página atual para lógica condicional
- Detectar tipo de dispositivo do usuário
- Acessar parâmetros de query string (GET)
- Verificar se features especiais estão habilitadas
- Recuperar títulos SEO e informações de página

## Exemplo

```twig
{# Usar base para URLs relativas #}
<link rel="stylesheet" href="{{ base }}/css/style.css">

{# Detectar página atual #}
{% if page == 'principal' %}
  <h1>Bem-vindo à página inicial</h1>
{% elseif page == 'categorias' %}
  <h1>Categorias de produtos</h1>
{% endif %}

{# Acessar parâmetros GET #}
{% if extra.id %}
  <p>Você está visualizando o item: {{ extra.id }}</p>
{% endif %}

{# Aplicar lógica com flags #}
{% if geral.hasSmartHint %}
  {# Carregar script do Smart Hint #}
  <script src="https://cdn-smarthinit.wbuy.com/script.js"></script>
{% endif %}

{# Menu adaptativo por dispositivo #}
{% if detect.isMobile() %}
  <link rel="stylesheet" href="{{ base }}/css/mobile-menu.css">
{% else %}
  <link rel="stylesheet" href="{{ base }}/css/desktop-menu.css">
{% endif %}
```

Saída esperada:

```html
<link rel="stylesheet" href="https://www.loja.com.br/css/style.css">
<h1>Bem-vindo à página inicial</h1>
<p>Você está visualizando o item: 123</p>
<script src="https://cdn-smarthinit.wbuy.com/script.js"></script>
<link rel="stylesheet" href="https://www.loja.com.br/css/mobile-menu.css">
```

## Observações

- Valores são estabelecidos no servidor durante renderização do template
- Parâmetros GET são acessados via array `extra`
- Configurações especiais (flags) são definidas pelo lojista no painel administrativo
- Funções PHP como `pr()`, `plural()`, `separa()` estão em [`02-twig`](../02-twig/)
- Cache pode afetar valores globais; sempre verificar em tempo de debug

## Erros comuns

### Erro 1: Confundir variáveis locais com globais

**Problema**: Usar variável local com mesmo nome de global
**Diagnóstico**: Valor inesperado retornado
**Solução**: Evitar reatribuições; usar namespace diferente se necessário

```twig
{# Errado: sobrescreve variável global #}
{% set page = 'customizada' %}

{# Correto: criar variável nova #}
{% set current_page = page %}
```

### Erro 2: Acessar extra sem verificar existência

**Problema**: Erro ao acessar `extra.id` quando parâmetro não existe na URL
**Diagnóstico**: Retorna null/undefined
**Solução**: Sempre verificar com condicional

```twig
{% if extra.id %}
  Parâmetro existe: {{ extra.id }}
{% endif %}
```

### Erro 3: Usar flags antes de verificação

**Problema**: Assumir que `geral.hasSmartHint` existe sempre
**Diagnóstico**: Erro em templates antigos ou instalações sem feature
**Solução**: Sempre envolver em condicional

```twig
{% if geral.hasSmartHint is defined and geral.hasSmartHint %}
  {# renderizar Smart Hint #}
{% endif %}
```

## Veja também

- [Visão geral store](04-store/visao-geral-store.md)
- [Array global](04-store/array-global.md)
- [Detect isMobile](04-store/detect-ismobile.md)
