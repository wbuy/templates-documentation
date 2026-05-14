---
title: "Condicionais if"
slug: "condicionais-if"
doc_type: "concept"
summary: "Documentação de condicionais if no Twig v2 da plataforma wBuy. Explicação de sintaxe, uso e exemplos de condicionais para controle de fluxo em templates wBuy."
tags:
  - twig
  - condicionais
  - if
  - controle de fluxo
related:
  - 02-twig/sintaxe-basica.md
  - 02-twig/visao-geral-twig.md
  - 04-store/visao-geral-store.md
---

## O que faz

Condicionais if são estruturas de controle no Twig que permitem executar blocos de código com base em condições lógicas. Eles são usados para controlar o fluxo de renderização em templates wBuy, permitindo exibir ou ocultar conteúdo dinamicamente com base em variáveis, estados do objeto `store` ou resultados de funções. As condicionais if são essenciais para criar templates flexíveis e responsivos que se adaptam ao contexto do usuário e aos dados disponíveis.

## Sintaxe

A sintaxe básica de uma condicional if em Twig é:

```twig
{% if condition %}
  {# Código a ser executado se a condição for verdadeira #}
{% elseif another_condition %}
  {# Código a ser executado se a outra condição for verdadeira #}
{% else %}
  {# Código a ser executado se nenhuma das condições anteriores for verdadeira #}
{% endif %}
```

Para mais detalhes sobre a sintaxe, operadores lógicos e variações de condicionais if, consulte a [documentação oficial do Twig](https://twig.symfony.com/doc/2.x/tags/if.html).

## Quando usar

Use condicionais if em Twig quando precisar controlar a renderização de conteúdo com base em condições lógicas. Exemplos comuns incluem:

- Exibir ou ocultar elementos com base em permissões do usuário
- Mostrar diferentes conteúdos dependendo do estado de um objeto
- Aplicar estilos ou classes CSS com base em condições
- Renderizar mensagens de erro ou sucesso com base em resultados de ações

## Exemplo

Imagine que você deseja exibir um banner promocional apenas para usuários que estão navegando em um dispositivo móvel. Você pode usar uma condicional if para verificar o estado do dispositivo e renderizar o banner apenas quando a condição for verdadeira:

```twig
{% if detect.isMobile() %}
  <div class="mobile-banner">
    Aproveite nossa promoção exclusiva para dispositivos móveis!
  </div>
{% endif %}
```

## Observações

- As condicionais if são sensíveis a espaços e indentação, especialmente em blocos aninhados
- Use operadores lógicos (`and`, `or`, `not`) para combinar múltiplas condições em uma única expressão if
- Lembre-se de consultar a documentação wBuy para entender as variáveis e funções disponíveis no contexto das condicionais if, como `store`, `detect`, e suas funções customizadas
- Para mais detalhes técnicos sobre o comportamento das condicionais if, como avaliação de expressões e manipulação de variáveis, consulte a [documentação oficial do Twig](https://twig.symfony.com/doc/2.x/tags/if.html)

## Erros comuns

### Erro 1: Sintaxe incorreta em condicionais if

**Problema**: Esquecer de fechar um bloco `{% if %}` com `{% endif %}`, ou usar sintaxe incorreta (ex: `{% if condition %}` sem `%}` no final).
**Diagnóstico**: Twig retornará um erro de sintaxe indicando a linha do template onde o problema ocorreu.
**Solução**: Revise a estrutura da condicional if para garantir que todos os blocos estejam corretamente abertos e fechados, e que a sintaxe esteja correta.

### Erro 2: Uso incorreto de operadores lógicos ou variáveis

**Problema**: Tentar usar operadores lógicos de forma incorreta (ex: `and` em vez de `&&`), ou usar variáveis que não existem ou que não estão disponíveis no contexto da condicional if.
**Diagnóstico**: Twig pode retornar um erro indicando que a variável ou operador não foi encontrado, ou pode simplesmente não renderizar o conteúdo esperado.
**Solução**: Revise a expressão da condicional if para garantir que os operadores lógicos estejam corretos e que as variáveis usadas  estejam disponíveis no contexto. Use o wBuy Watcher para testar as alterações em tempo real e verificar o comportamento da condicional if.

## Veja também

- [Visão geral dos templates wBuy](../01-introducao/visao-geral.md)
- [Visão geral do Twig v2](./visao-geral-twig.md)
- [Sintaxe Básica do Twig](./sintaxe-basica.md)
- [Visão geral do objeto `store`](../04-store/visao-geral-store.md)
- [wBuy Watcher NPM](../01-introducao/wbuy-watcher-npm.md)
