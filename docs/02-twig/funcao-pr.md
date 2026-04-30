---
title: "Função pr()"
slug: "funcao-pr"
doc_type: "reference"
summary: "Função de debug para inspecionar variáveis (arrays/objetos) no contexto Twig durante o desenvolvimento."
tags:
  - twig
  - debug
  - templates
related:
  - 02-twig/exemplo-loop-pr.md
  - 02-twig/loops-for.md
  - 02-twig/sintaxe-basica.md
---

# Função pr()

> Use `pr()` como ferramenta de inspeção durante o desenvolvimento para entender a estrutura de dados disponível no contexto do template.

## O que faz

A função `pr()` serve para **inpecionar o conteúdo de uma variável** (ex.: arrays e objetos) diretamente no template no formato `var_dump()` encapsulado em uma tag `<pre>`, facilitando o entendimento do "shape" dos dados que você recebe em cada página/componente do template.

Na prática, ela é usada para:

- descobrir quais campos existem em um objeto/array;
- confirmar se uma variável está chegando com o valor esperado;
- acelerar o desenvolvimento de loops e condicionais, quando você não conhece a estrutura completa do retorno.

## Sintaxe

A chamada básica é:

```twig
{{ pr(variavel) }}
```

Onde:

- `variavel`: qualquer valor disponível no contexto Twig (ex.: `product`, `cart`, `pageProducts`, etc.)

> **Observação:** dependendo do ambiente/implementação, `pr()` **pode renderizar saída no HTML**. Trate como debug visual e remova antes de publicar.

## Quando usar

Use `pr()` quando:

- estiver desenvolvendo um template e precisar entender a estrutura de dados disponível;
- você vai escrever um loop `{% for %}` e precisa ver quais campos existem em cada item;
- você suspeita que um campo não existe, está vazio ou com formato diferente do esperado.

Evite usar `pr()` quando:

- você está em produção ou em um ambiente onde a saída de debug pode ser exposta a usuários finais (risco de poluir o HTML e expor dados sensíveis);
- você está debugando algo que depende de performance/SEO (qualquer saída extra pode afetar o HTML e impactar negativamente);
- a página tem comportamento sensível a cache (saída de debug pode "vazar" para usuários se o HTML final for reaproveitado).

## Exemplo

Exemplo mínimo para inspecionar uma variável e, em seguida, construir um loop corretamente.

```twig
{# 1) Ispecione a variável para entender os campos disponíveis #}
{{ pr(pageProducts) }}

{# 2) Depois, use os campos identificados para renderizar a lista #}
{% for p in pageProducts %}
  <div>
    <h3>{{ p.name }}</h3>
    {# ajuste os campos conforme o que você viu no pr() #}
  </div>
{% else %}
  <p>Nenhum produto encontrado.</p>
{% endfor %}
```

Resultado esperado: você consegue visualizar a estrutura de `pageProducts` e adaptar os campos do loop conforme o retorno real.

## Observações

- **Remova antes de publicar**: `pr()` é um recurso de debug. Deixar no template pode:
  - quebrar o layout (injetar blocos inesperados no HTML);
  - afetar o SEO (HTML com ruído);
  - expor dados sensíveis (dependendo do que é impresso).
- **Prefira debug "local"**: use `pr()` em trechos específicos, não em grandes estruturas repetidas (ex.: dentro de loops grandes), para evitar excesso de saída.
- **Use junto com loops/condicionais:** geralmente o fluxo é “`pr()` → entender → aplicar `{% for %}` / `{% if %}`”.

## Erros comuns

- **Esquecer `pr()` no template final**
Diagnóstico: o HTML final tem blocos de debug visíveis no site.
Correção: remova todas as chamadas `pr()` antes de publicar.
- **Usar `pr()` dentro de loops grandes**
Diagnóstico: saída repetida dezenas/centenas de vezes, página pesada.
Correção: aplique `pr()` uma vez fora do loop ou em um item específico (ex.: apenas no primeiro).
- **Assumir campos sem confirmar o retorno**
Diagnóstico: campos renderizam vazio/erro lógico (ex.: `p.title` quando o retorno usa `p.name`).
Correção: rode `pr()` (ou `pr(pageProducts)`) e ajuste o template aos campos reais.

## Veja também

- [Exemplo de loop com pr()](./exemplo-loop-pr.md)
- [Loops for](./loops-for.md)
- [Sintaxe básica do Twig](./sintaxe-basica.md)