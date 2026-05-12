---
title: "Como usar esta documentacao"
slug: "como-usar-esta-documentacao"
doc_type: "how-to"
summary: "Guia de como usar esta documentação para desenvolvimento de templates wBuy. Este documento fornece orientações sobre a estrutura da documentação, como navegar pelos tópicos, e dicas para aproveitar ao máximo os recursos disponíveis para desenvolvedores de templates na plataforma wBuy."
tags:
  - guia
  - documentação
  - desenvolvimento de templates
  - wBuy
related:
  - 01-introducao/visao-geral.md
  - 01-introducao/por-onde-comecar.md
  - 02-twig/visao-geral-twig.md
  - 03-api/visao-geral-api.md
  - 04-store/visao-geral-store.md
---

## O que faz

Esta documentação é organizada seguindo a metodologia **AI-Ready IA-First**, onde cada arquivo cobre exatamente um conceito de forma auto-contida. O objetivo é permitir que você encontre respostas precisas sem ruído informacional — seja você um desenvolvedor humano navegando manualmente ou um agente de IA construindo respostas a partir de múltiplos arquivos relacionados.

A documentação está estruturada em **10 pastas temáticas** (numeradas `00` a `09`) que cobrem desde conceitos fundamentais até exemplos integrados completos. Este guia explica como navegar essa estrutura de forma eficiente.

## Sintaxe

Não se aplica. Este documento é um guia prático e não possui sintaxe de código.

## Quando usar

Leia este arquivo:

- **Primeira vez aqui**: Você acabou de começar e quer entender como a documentação funciona antes de mergulhar em detalhes técnicos.
- **Desenvolvedor experiente**: Você conhece os conceitos e quer saber como encontrar rapidamente a informação técnica específica que precisa.
- **Consultor de IA/agente**: Você está integrando esta base de conhecimento com um sistema de IA e quer entender a estrutura subjacente.
- **Contribuidor**: Você quer adicionar ou atualizar documentação e precisa seguir as convenções existentes.

## Exemplo

### Cenário 1: Desenvolvedor Iniciante

Você vai começar a desenvolver seu primeiro template wBuy:

1. Leia [Visão geral dos templates wBuy](./visao-geral.md) — vai entender como Twig, store e API funcionam juntos.
2. Siga [Por onde começar](./por-onde-comecar.md) — instruções passo a passo para configurar o ambiente.
3. Explore [Visão geral do Twig](./visao-geral-twig.md) e depois consulte tópicos específicos como `loops-for.md` conforme precisar.
4. Use [Checklist de módulos obrigatórios](./checklist-modulos-obrigatorios.md) antes de submeter.

**Dica:** Leia sempre os arquivos de "visão geral" (`visao-geral-*.md`) de cada pasta antes de consultar tópicos específicos.

### Cenário 2: Desenvolvedor com Experiência

Você já conhece Twig e quer usar a API wBuy para recuperar dados de produto:

1. Vá direto para [Documentação da API wBuy](./documentacao-api.md) — links rápidos para referência técnica.
2. Consulte especificamente a pasta [03-api](../03-api/) para a sintaxe exata.
3. Veja [Exemplo: Página de produto com SKU](../09-exemplos/) se precisar ver integração completa com seletor de variações.

**Dica:** Use a busca por tema (tags) para encontrar todos os arquivos relacionados a "produto" ou "carrinho" de uma vez.

### Cenário 3: Agente de IA / Consulta Programática

Você está respondendo a pergunta: *"Como renderizar dinamicamente as variações de um produto?"*

1. Consulte o arquivo [productGet](../03-api/productget.md) — obtém dados brutos do produto.
2. Siga o link em `related` para [getVariations](../03-api/getvariations.md) — método específico para variações.
3. Consulte [html-productdetailsku.md](../05-html/html-productdetailsku.md) — componente HTML pronto para renderizar seletor.
4. Finalize com [Página de produto com SKU](../09-exemplos/) — exemplo completo integrando todos os elementos.

**Dica:** Cada arquivo tem um campo `related` com 1-5 arquivos conexos — siga a cadeia para construir compreensão multi-hop.

## Observações

### Estrutura das 10 Pastas

| Pasta | Propósito | Comece por |
|-------|----------|-----------|
| `00-indice` | Mapa e taxonomia | `sidebar.md` — índice navegável completo |
| `01-introducao` | Fundamentos da plataforma | Qualquer visão geral, depois por onde começar |
| `02-twig` | Engine de templates Twig v2 | `visao-geral-twig.md` depois tópicos específicos |
| `03-api` | Métodos de API para templates | `visao-geral-api.md` depois métodos específicos |
| `04-store` | Objeto JavaScript global `store` | `visao-geral-store.md` depois recursos específicos |
| `05-html` | Componentes HTML prontos | Consultar conforme necessário para página específica |
| `06-paginas` | Páginas customizáveis e seus contextos | Consultar conforme tipo de página (produto, categoria, etc) |
| `07-modelos` | Modelos completos de páginas e CSS | Servem como referência visual e estrutural |
| `08-cache` | Estratégias de cache da plataforma | Essencial se desenvolvendo com cache ativo |
| `09-exemplos` | Casos integrados e completos | Consultar para ver vários recursos funcionando juntos |

### Padrão de Seções em Todo Arquivo

Cada arquivo `.md` segue o mesmo padrão de seções para facilitar a localização:

- **O que faz** — Explica o conceito/recurso em 2-3 parágrafos
- **Sintaxe** — Assinatura da função ou estrutura (se aplicável)
- **Quando usar** — Casos ideais, pré-condições, limitações
- **Exemplo** — Código ou passo a passo funcional
- **Observações** — Compatibilidade, performance, cache, SEO/mobile
- **Erros comuns** — Problemas recorrentes e soluções
- **Veja também** — Links para arquivos relacionados

Saber disso significa que você pode consultar sempre a mesma seção em qualquer arquivo.

### Tags e Busca Facetada

Cada arquivo tem tags como `twig`, `api`, `store`, `carrinho`, `produto`, `mobile`. Use tags para agrupar:

- Todos os arquivos sobre "carrinho": busque tag `carrinho`
- Todos os arquivos sobre "mobile": busque tag `mobile`
- Todos os exemplos: busque `doc_type:example`

## Erros comuns

### Erro 1: Pular direto para referências técnicas sem contexto conceitual

**Problema**: Você vai para `functionao-pr.md` sem ler `visao-geral-twig.md` primeiro e fica confuso sobre quando usar.  
**Diagnóstico**: Você consulta referências mas não consegue conectar com sua tarefa prática.  
**Solução**: Sempre leia o arquivo "visão-geral" da pasta primeiro. Ele constrói o contexto necessário para entender os tópicos específicos.

### Erro 2: Não seguir os links em `related`

**Problema**: Você consulta um método de API isoladamente e perde a visão de como ele se integra com o store ou componentes HTML.  
**Diagnóstico**: Sua solução fica incompleta ou você reinventa a roda.  
**Solução**: Quando consultar um arquivo, sempre verifique o campo `related` — aqueles links carregam contexto essencial que você pode precisar.

### Erro 3: Confundir `02-twig` (templates server-side) com JavaScript de `04-store` (client-side)

**Problema**: Você tenta usar `store.cart.items` dentro de um template Twig e fica confuso.  
**Diagnóstico**: Entender diferença entre server-side (Twig) e client-side (JavaScript).  
**Solução**: Leia [Visão geral dos templates wBuy](./visao-geral.md) — explica exatamente onde cada tecnologia atua.

### Erro 4: Ignorar o arquivo `08-cache`

**Problema**: Seu template funciona localmente mas quebra em produção quando cache está ativo.  
**Diagnóstico**: Consulte [Cache de recursos gerais](../08-cache/cache-recursos-gerais.md).  
**Solução**: Sempre revise cache antes de enviar para produção.

## Veja também

- [Visão geral dos templates wBuy](./visao-geral.md) — entenda a stack completa
- [Por onde começar](./por-onde-comecar.md) — primeiros passos
- [Sidebar navegável](../00-indice/sidebar.md) — mapa completo de todos os arquivos
- [Checklist de módulos obrigatórios](./checklist-modulos-obrigatorios.md) — prepare para aprovação
- [Exemplo: Home com banners e vitrine](../09-exemplos/) — veja tudo funcionando junto
