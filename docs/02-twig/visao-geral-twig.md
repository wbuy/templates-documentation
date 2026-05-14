---
title: "Visão geral do Twig v2"
slug: "visao-geral-twig"
doc_type: "concept"
summary: "Contexto histórico e arquitetural do Twig v2 nos templates wBuy. Diferenças entre Twig puro e a implementação wBuy."
tags:
  - twig
  - visão-geral
  - arquitetura
  - wbuy
related:
  - 01-introducao/visao-geral.md
  - 02-twig/sintaxe-basica.md
  - 04-store/visao-geral-store.md
---

## O que faz

Twig v2 é a engine de templates escolhida pela plataforma wBuy para renderizar páginas de forma server-side. Este arquivo contextualiza o papel histórico e arquitetural do Twig dentro da stack de desenvolvimento wBuy, explicando como a engine foi integrada e adaptada para as necessidades específicas da plataforma.

### Contexto Histórico

Twig é uma engine de templates PHP criada pela Symfony que ganhou popularidade por sua sintaxe clara, segura e extensível. A plataforma wBuy adotou Twig v2 como a base da camada de templates após avaliar alternativas, devido à sua robustez, performance e comunidade ativa. A escolha por Twig v2 (em vez de versões mais recentes) reflete a necessidade de compatibilidade e estabilidade em uma plataforma de produção com centenas de lojas ativas.

### Arquitetura no wBuy

Na plataforma wBuy, Twig atua como intermediário entre os dados da loja (armazenados em APIs backend e no objeto global `store`) e a camada HTML final enviada ao navegador. O fluxo arquitetural é:

1. **Dados** — Recuperados via API backend ou objeto `store` (dados em tempo real)
2. **Template Twig** — Desenvolvedores escrevem lógica de apresentação usando sintaxe Twig
3. **Renderização Server-Side** — Twig processa o template e gera HTML
4. **Browser** — HTML é enviado e renderizado no navegador do usuário

Esse modelo garante que toda lógica de negócio permanece no servidor, enquanto o template Twig funciona como orquestrador de dados e renderização.

### Twig Puro vs. Implementação wBuy

A implementação wBuy estende o Twig puro com recursos e contextos específicos:

#### Twig Puro (Symfony padrão)

- Acesso a dados via variáveis genéricas passadas manualmente
- Sintaxe padrão: `{{ variavel }}`, `{% for %}`, `{% if %}`
- Filtros e funções do core Twig
- Sem contexto de domínio específico

#### Twig no wBuy (Implementação Adaptada)

- **Objeto `store` global** — Dados da loja acessíveis diretamente: `{{ store.name }}`, `{{ store.categories }}`
- **Variáveis de contexto pré-definidas** — Cada página recebe contexto automático (ex: `page_category`, `product`, `cart`)
- **Funções customizadas** — `pr()` para debug, `plural()` para pluralização, `separa()` para formatação
- **Compatibilidade com cache total** — Blocos de cache exclusivo e estratégias de invalidação integradas
- **Encoding ISO-8859-1 obrigatório** — Todos os templates devem usar encoding específico (confira em [encoding-iso-8859-1.md](../01-introducao/encoding-iso-8859-1.md))
- **Sincronização com wBuy Watcher** — CLI NPM que sincroniza templates em tempo real com a plataforma

#### Exemplo de Diferença

**Twig puro:**

```twig
{% for item in items %}
  <li>{{ item.name }}</li>
{% endfor %}
```

**Twig no wBuy:**

```twig
{% set produtosBox = store.productToBox({limit:'4', order:'random'}) %}
{% for produto in produtosBox.data %}
    {{ store.productBoxDefault(produto) }}
{% endfor %}
```

Neste exemplo, o template wBuy utiliza uma função customizada `store.productToBox` para obter produtos de forma dinâmica, enquanto o Twig puro dependeria de uma variável `items` passada manualmente.

## Quando usar este documento

- Você está iniciando no desenvolvimento de templates wBuy e quer entender por que Twig foi escolhido e como é implementado
- Você precisa entender a relação entre Twig puro (referência online) e as adaptações específicas do wBuy
- Você quer contextualizar como Twig se encaixa na stack técnica geral da plataforma

## Observações

- A versão Twig utilizada é a **v2**, não a v1 ou v3, por questões de compatibilidade retroativa
- Toda renderização acontece **server-side** — não há processamento de templates no navegador do cliente
- A documentação de Twig oficial em <https://twig.symfony.com/doc/2.x/template.html> é referência complementar, mas foque na documentação wBuy para contextos específicos
- O wBuy Watcher é essencial para desenvolvimento local — consulte [wbuy-watcher-npm.md](../01-introducao/wbuy-watcher-npm.md)

## Veja também

- [Visão geral dos templates wBuy](../01-introducao/visao-geral.md)
- [Sintaxe Básica do Twig](./sintaxe-basica.md)
- [Visão geral do objeto `store`](../04-store/visao-geral-store.md)
- [wBuy Watcher NPM](../01-introducao/wbuy-watcher-npm.md)
