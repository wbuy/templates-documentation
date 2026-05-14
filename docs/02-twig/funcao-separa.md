---
title: "Função separa()"
slug: "funcao-separa"
doc_type: "reference"
summary: "Função para unir duas palavras ou variáveis com um separador condicional, renderizando o separador apenas se o segundo valor existir."
tags:
  - twig
  - funcao
  - separador
  - concatenacao
related:
  - 02-twig/sintaxe-basica.md
  - 02-twig/visao-geral-twig.md
  - 04-store/store-categories.md
---

# Função separa()

> Use `separa()` para concatenar valores com um separador que só aparece quando o segundo valor existe, evitando separadores desnecessários.

## O que faz

A função `separa()` serve para **unir duas palavras ou variáveis com um separador condicional**. Ela renderiza o separador apenas se o segundo parâmetro existir (não estiver vazio), simplificando a exibição de dados agrupados ou hierárquicos sem deixar separadores órfãos.

Na prática, é especialmente útil para:

- exibir categorias de produtos (ex.: "Informática - Acessórios");
- concatenar nomes de níveis hierárquicos (ex.: categoria principal + subcategoria);
- evitar lógica condicional repetitiva no template (`{% if %}`).

## Sintaxe

A chamada é:

```twig
{{ primeiro_valor ~ separa(segundo_valor, separador) }}
```

Onde:

- `primeiro_valor`: a string ou variável base (ex.: `categoria_level1.nome`);
- `segundo_valor`: a string ou variável condicional (ex.: `categoria_level2.nome`);
- `separador`: a string usada para separar os valores **apenas se o segundo existir** (ex.: `' - '`, `' / '`, `' > '`).

> **Observação:** a função retorna apenas `primeiro_valor` se `segundo_valor` estiver vazio, nulo ou falso.

## Quando usar

Use `separa()` quando:

- você precisa exibir uma hierarquia (ex.: "Categoria Principal - Subcategoria");
- dois valores podem existir independentemente e você quer evitar separadores soltos;
- você quer simplificar templates e evitar condicionais aninhadas;
- você trabalha com categorias em múltiplos níveis (ex.: `categoria_level1`, `categoria_level2`, `categoria_level3`).

Evite usar `separa()` quando:

- você precisa de lógica mais complexa (ex.: concatenar 3+ valores com separadores diferentes — considere usar múltiplas chamadas ou estruturas condicionais);
- o separador deve ter um comportamento dinâmico (ex.: mudar conforme o tipo de valor);
- o valor condicional precisa ser tratado de forma especial (ex.: validação, transformação de formato).

## Exemplo

Exemplo prático usando dados de categorias:

- **Exemplo 1 — concatenar dois níveis de categoria**

  ```twig
  {{ categoria_level1.nome ~ separa(categoria_level2.nome, ' - ') }}
  ```

  Resultado esperado quando ambos existem:
  `Informática - Acessórios`

- **Exemplo 2 - quando o segundo valor não existe**

  ```twig
  {# Exemplo 2: Quando apenas o primeiro valor existe #}
  {{ categoria_level1.nome ~ separa(categoria_level2.nome, ' - ') }}
  ```

  Resultado esperado quando `categoria_level2.nome` está vazio:
  `Informática` (sem o separador)

- **Exemplo 3 - Uso completo em um template (com mais níveis)**

  ```twig
  <h2>
    {{ categoria_level1.nome ~ separa(categoria_level2.nome, ' - ') ~ separa(categoria_level3.nome, ' - ') }}
  </h2>
  ```

  Resultado esperado:
  `Informática - Acessórios - Mouses`


## Observações

- **Comportamento com valores vazios**: se `segundo_valor` for vazio, nulo, `false` ou `0`, o separador não é renderizado. Apenas `primeiro_valor` é retornado.
- **Chaining (múltiplas chamadas)**: você pode encadear múltiplas chamadas `separa()` para concatenar mais de dois valores:

  ```twig
  {{ valor1 ~ separa(valor2, ' - ') ~ separa(valor3, ' - ') }}
  ```

- **Performance**: a função é leve e não impacta performance; pode ser usada sem restrições, inclusive em loops.
- **Cache**: o resultado é determinístico (depende apenas dos parâmetros), então é seguro para estratégias de cache de template.
- **SEO/Acessibilidade**: útil para breadcrumbs e navegação hierárquica, facilitando a estruturação de títulos descritivos para SEO.

## Erros comuns

- **Esquecer de verificar se o valor existe antes**
  Diagnóstico: separador aparece mesmo quando deveria estar ausente.
  Correção: `separa()` já faz essa verificação automaticamente; se não funcionar, verifique se o valor realmente está vazio (use `pr()` para debugar).

- **Usar separadores com espaços inconsistentes**
  Diagnóstico: renderização fica: `Informática-Acessórios` (sem espaços) ou `Informática  -  Acessórios` (espaços demais).
  Correção: defina o separador claramente: `' - '` (com espaços) ou `-` (sem espaços).

- **Aplicar a função ao contrário (segundo ~ separa(primeiro, ...))**
  Diagnóstico: ordem dos valores invertida na saída.
  Correção: sempre coloque o valor base primeiro, depois `~ separa(valor_condicional, separador)`.

- **Assumir que zero (`0`) é vazio**
  Diagnóstico: quando `segunda_valor` é `0`, o separador desaparece.
  Correção: isso é por design. Se precisar incluir zero, converta para string explicitamente ou use uma condicional (`{% if %}`).

## Veja também

- [Sintaxe básica do Twig](./sintaxe-basica.md)
- [Visão geral do Twig](./visao-geral-twig.md)
- [Categorias de Loja](../04-store/store-categories.md)
