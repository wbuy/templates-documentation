---
title: "Sintaxe básica do Twig"
slug: "sintaxe-basica"
doc_type: "reference"
summary: "Referência de sintaxe básica do Twig v2 na plataforma wBuy. Documentação de variáveis, filtros, funções e estruturas de controle essenciais para desenvolvimento de templates."
tags: ["placeholder", "pendente"]
related: []
---

## O que faz

Twig é a engine de templates utilizada pela plataforma wBuy para renderizar páginas de forma server-side. Este documento serve como referência de sintaxe básica do Twig v2, cobrindo variáveis, filtros, funções e estruturas de controle essenciais para o desenvolvimento de templates na plataforma.

## Sintaxe

- Variáveis: `{{ variavel }}`
- Filtros: `{{ variavel|filtro }}`
- Funções: `{{ funcao(param1, param2) }}`
- Estruturas de controle: `{% if %}`, `{% for %}`, `{% include() %}`, etc.

## Quando usar

Use este documento como referência rápida para a sintaxe básica do Twig ao desenvolver templates wBuy. Ele é especialmente útil para:

- Consultar a sintaxe de variáveis, filtros e funções comuns
- Revisar estruturas de controle para loops e condicionais
- Entender as diferenças de sintaxe entre Twig puro e a implementação wBuy (ex: acesso ao objeto `store`)

## Exemplo

Exemplo de uso de variáveis, filtros e funções no Twig wBuy:

```twig
<div class="item">
  {{ detect.isMobile() ? slide.mobile_raw|raw : slide.desktop_raw|raw }}
  {% if slide.avancado.texto|length >= 1 %}
    <div class="overlay">
      <h2 class="title" style="color: {{ slide.avancado.cor_texto ?: '#FFF' }}">{{ slide.avancado.texto|split('</strong>')|first|replace({'<p>' : '', '<strong>': ''})|raw }}</h2>
        {% if slide.link %}
        <a href="{{ slide.link }}" target="{{ slide.target ? slide.target : '_self' }}" class="button">{{ slide.avancado.texto|split('<em>')|last|replace({'</em>' : '', '</p>': ''})|raw }}</a>
        {% endif %}
    </div>
  {% endif %}
</div>
```

## Observações

- A sintaxe do Twig é sensível a espaços e indentação, especialmente em estruturas de controle
- Filtros e funções customizadas do wBuy devem ser consultados na documentação específica da plataforma, pois podem diferir do Twig puro
- Lembre-se de usar encoding ISO-8859-1 em todos os templates, conforme exigido pela plataforma (veja [encoding-iso-8859-1.md](../01-introducao/encoding-iso-8859-1.md))

## Erros comuns

### Erro 1: Sintaxe incorreta em estruturas de controle

**Problema**: Esquecer de fechar um bloco `{% if %}` ou `{% for %}`, ou usar sintaxe incorreta (ex: `{% if condition %}` sem `%}` no final).
**Diagnóstico**: Twig retornará um erro de sintaxe indicando a linha do template onde o problema ocorreu.
**Solução**: Revise a estrutura de controle para garantir que todos os blocos estejam corretamente abertos e fechados, e que a sintaxe esteja correta. Use o wBuy Watcher para testar as alterações em tempo real.

### Erro 2: Uso incorreto de filtros ou funções

**Problema**: Tentar usar um filtro ou função que não existe ou que é específico do Twig puro, sem considerar as adaptações do wBuy. Por exemplo, usar `|length` em um contexto onde o objeto não é uma string ou array, ou tentar usar uma função que não está disponível na implementação wBuy.
**Diagnóstico**: Twig pode retornar um erro indicando que o filtro ou função não foi encontrado, ou pode simplesmente não renderizar o conteúdo esperado.
**Solução**: Consulte a documentação wBuy para verificar quais filtros e funções estão disponíveis e como usá-los corretamente. Lembre-se de que o objeto `store` e as funções customizadas do wBuy podem ter comportamentos específicos que diferem do Twig puro.

## Veja também

- [Visão geral dos templates wBuy](../01-introducao/visao-geral.md)
- [Visão geral do Twig v2](./visao-geral-twig.md)
- [Visão geral do objeto `store`](../04-store/visao-geral-store.md)
- [wBuy Watcher NPM](../01-introducao/wbuy-watcher-npm.md)
