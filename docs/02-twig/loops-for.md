---
title: "Loops for"
slug: "loops-for"
doc_type: "concept"
summary: "Documentação de loops for no Twig v2 da plataforma wBuy. Explicação de sintaxe, uso e exemplos de loops para iterar sobre arrays e objetos em templates wBuy."
tags:
  - twig
  - loops
  - for
  - iteração
related:
  - 02-twig/sintaxe-basica.md
  - 02-twig/visao-geral-twig.md
---

## O que faz

Loops for são estruturas de controle no Twig que permitem iterar sobre arrays, objetos ou qualquer variável que seja iterável. Eles são usados para renderizar listas de produtos, categorias, banners ou qualquer conjunto de dados dinâmicos em templates wBuy. O loop for é essencial para criar templates dinâmicos que exibem múltiplos itens de forma eficiente e organizada.

## Sintaxe

### Estrutura básica

```twig
{% for item in collection %}
  {{ item }}
{% endfor %}
```

### Tratamento de coleções vazias

```twig
{% for item in collection %}
  {{ item }}
{% else %}
  <p>Nenhum item encontrado.</p>
{% endfor %}
```

Para mais detalhes sobre a sintaxe, variações e variáveis do loop for, consulte a [documentação oficial do Twig](https://twig.symfony.com/doc/2.x/tags/for.html).

## Quando usar

Use loops for em Twig quando precisar iterar sobre uma coleção de dados para renderizar múltiplos itens em um template wBuy. Exemplos comuns incluem:

- Listar produtos em uma categoria
- Exibir banners ou slides em um carrossel
- Mostrar avaliações ou comentários de clientes
- Renderizar categorias ou subcategorias em um menu

## Exemplo

Imagine que você tem uma coleção de produtos e deseja exibi-los em um template wBuy. Você pode usar um loop for para iterar sobre a coleção e renderizar cada produto:

```twig
{% set produtosBox = store.productToBox({limit:'4', order:'random'}) %}
{% for produto in produtosBox.data %}
  <div class="box">
    {{ produto }}
  </div>
{% endfor %}
```

## Observações

- O loop for é sensível a espaços e indentação, especialmente em blocos aninhados
- Use a cláusula `{% else %}` para lidar com casos onde a coleção está vazia, garantindo que o template não quebre e forneça feedback ao usuário
- Lembre-se de consultar a documentação wBuy para entender as variáveis e funções disponíveis no contexto do loop, como `store` e suas funções customizadas
- Para mais detalhes técnicos sobre o comportamento do loop for, como variáveis de controle (`loop.index`, `loop.first`, etc.) e manipulação de chaves e valores, consulte a [documentação oficial do Twig](https://twig.symfony.com/doc/2.x/tags/for.html)

## Erros comuns

### Erro 1: Sintaxe incorreta no loop for

**Problema**: Esquecer de fechar o bloco `{% endfor %}` ou usar sintaxe incorreta (ex: `{% for item in collection %}` sem `%}` no final).
**Diagnóstico**: Twig retornará um erro de sintaxe indicando a linha do template onde o problema ocorreu.
**Solução**: Revise a estrutura do loop for para garantir que todos os blocos estejam corretamente abertos e fechados, e que a sintaxe esteja correta. Use o wBuy Watcher para testar as alterações em tempo real.

### Erro 2: Coleção vazia não tratada

**Problema**: Não lidar com casos onde a coleção está vazia, resultando em template quebrado ou feedback inadequado ao usuário.
**Diagnóstico**: O template pode exibir conteúdo inesperado ou gerar erros ao tentar acessar elementos de uma coleção vazia.
**Solução**: Utilize a cláusula `{% else %}` para fornecer um feedback adequado quando a coleção estiver vazia.

## Veja também

- [Visão geral dos templates wBuy](../01-introducao/visao-geral.md)
- [Visão geral do Twig v2](./visao-geral-twig.md)
- [Sintaxe Básica do Twig](./sintaxe-basica.md)
- [Visão geral do objeto `store`](../04-store/visao-geral-store.md)
- [wBuy Watcher NPM](../01-introducao/wbuy-watcher-npm.md)
