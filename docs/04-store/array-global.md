---
title: "Array global"
slug: "array-global"
doc_type: "reference"
summary: "Array global que armazena configurações diversas e estados da loja virtual, indicando se é mostruário, bloqueios de cadastro e outras bandeiras de funcionalidades."
tags:
  - array
  - global
  - configuração
  - mostruário
  - loja
related:
  - 04-store/visao-geral-store.md
  - 04-store/recursos-gerais.md
  - 04-store/geral-hasopolen.md
---

## O que faz

O array `global` é uma matriz associativa que armazena configurações gerais da loja virtual, bandeiras (flags) que indicam estados especiais e propriedades relacionadas ao tipo de operação da loja. Ele contém informações sobre limitações, restrições e funcionalidades da loja que afetam a apresentação e comportamento do template.

Este array é essencial para determinar se a loja está em modo mostruário, se permite novos cadastros de usuários, e outras configurações críticas que influenciam o template.

## Sintaxe

```twig
{{ global.var_mostruario }}         {# boolean - loja em modo mostruário #}
{{ global.var_bloquear_cadastros }} {# boolean - novos cadastros bloqueados #}

{# Mais propriedades disponíveis - consulte documentação específica #}
```

**Tipos de retorno**: Geralmente booleanos e strings, dependendo da configuração.

## Quando usar

- Verificar se loja está em modo mostruário (somente visualização)
- Desabilitar checkout em lojas mostruário
- Verificar se cadastros de novos usuários estão bloqueados
- Renderizar mensagens diferentes baseado em estado da loja
- Aplicar lógica condicional de funcionalidades
- Pré-condição: Deve estar no contexto Twig

## Exemplo

```twig
{# Ocultar botão de compra em loja mostruário #}
{% if not global.var_mostruario %}
  <button class="btn-comprar">Adicionar ao Carrinho</button>
{% else %}
  <p class="alerta">Loja em modo mostruário - visualização apenas</p>
{% endif %}

{# Mostrar formulário de cadastro apenas se permitido #}
{% if not global.var_bloquear_cadastros %}
  <form method="POST" action="/usuario/novo">
    <input type="email" name="email" placeholder="Email">
    <button type="submit">Criar Conta</button>
  </form>
{% else %}
  <p>Novos cadastros estão desabilitados no momento.</p>
{% endif %}

{# Condicional combinada #}
{% if global.var_mostruario or global.var_bloquear_cadastros %}
  <div class="alert alert-info">
    Algumas funcionalidades estão limitadas nesta loja.
  </div>
{% endif %}
```

Saída esperada (em loja normal):

```html
<button class="btn-comprar">Adicionar ao Carrinho</button>
<form method="POST" action="/usuario/novo">
  <input type="email" name="email" placeholder="Email">
  <button type="submit">Criar Conta</button>
</form>
```

Saída esperada (em loja mostruário):

```html
<p class="alerta">Loja em modo mostruário - visualização apenas</p>
<p>Novos cadastros estão desabilitados no momento.</p>
```

## Observações

- Array é definido durante inicialização da loja no servidor
- Valores não mudam durante a sessão (a menos que cache seja limpo)
- Mostruário é uma funcionalidade destinada para catálogos sem vendas
- Bloqueio de cadastros é independente de mostruário
- Performance: Acesso muito rápido, sem impacto

## Erros comuns

### Erro 1: Esquecer de negar com `not`

**Problema**: `if global.var_mostruario` mostra botão em loja mostruário
**Diagnóstico**: Botão aparece quando deveria estar oculto
**Solução**: Usar `if not global.var_mostruario` para invertir lógica

```twig
{# Errado: mostra botão em mostruário #}
{% if global.var_mostruario %}
  <button>Comprar</button>
{% endif %}

{# Correto: oculta em mostruário #}
{% if not global.var_mostruario %}
  <button>Comprar</button>
{% endif %}
```

### Erro 2: Acessar propriedade não existente

**Problema**: Tentar acessar `global.propriedade_inexistente`
**Diagnóstico**: Retorna null sem erro (Twig é permissivo)
**Solução**: Consultar documentação de quais propriedades existem

### Erro 3: Confundir com `store.` vs `global.`

**Problema**: Usar `store.var_mostruario` em vez de `global.var_mostruario`
**Diagnóstico**: Valor não é encontrado
**Solução**: Usar `global.` para flags de configuração, `store.` para métodos

## Veja também

- [Visão geral store](04-store/visao-geral-store.md)
- [Recursos gerais](04-store/recursos-gerais.md)
- [geral.hasOpolen](04-store/geral-hasopolen.md)
