---
title: "Visão Geral de Modelos"
slug: "visao-geral-modelos"
doc_type: "concept"
summary: "Introdução aos modelos de templates customizáveis na plataforma wBuy, abrangendo modelos completos de páginas, topos, rodapés e widgets."
tags: ["modelos", "templates", "estrutura", "frontend"]
related: 
  - 07-modelos/topo-modelo-01.md
  - 07-modelos/pagina-inicial-modelo-01.md
  - 07-modelos/carrinho-suspenso.md
---

## O que faz

Os modelos wBuy são templates customizáveis que estruturam as principais páginas e componentes da loja virtual. Eles consistem em blocos de HTML, CSS e Twig que podem ser personalizados para atender às necessidades específicas de cada loja.

Os templates são desenvolvidos usando Twig 2 (engine de template) combinado com HTML e CSS. Isso permite criar estruturas dinâmicas que se integram com as APIs e dados disponíveis na plataforma wBuy, como categorias, produtos, carrinho de compras e informações de clientes.

A documentação completa de desenvolvimento e customização está disponível na plataforma, incluindo recursos, APIs, componentes HTML e exemplos de implementação.

## Quando usar

- Ao customizar a aparência visual de uma loja wBuy
- Ao criar layouts específicos para páginas principais (inicial, categorias, produtos)
- Ao implementar widgets e componentes de carrinho, banners ou promoções
- Ao desenvolver com wBuy Watcher para sincronização local de arquivos

## Estrutura de Desenvolvimento

Os templates utilizam:

- **Twig 2**: Engine de template para lógica dinâmica
- **HTML**: Estrutura semântica das páginas
- **CSS/SCSS**: Estilização e responsividade
- **JavaScript**: Interatividade (preferencialmente jQuery)
- **APIs wBuy**: Acesso a dados de categorias, produtos, clientes e carrinho

## Observações

- Todos os arquivos salvos via wBuy Watcher devem estar em codificação **ISO-8859-1**
- Os modelos devem ser desenvolvidos com abordagem responsiva para desktop e mobile
- Widgets podem ser criados separadamente e inclusos nos templates via função `include()` do Twig
- A função `pr()` permite visualizar dados do array durante desenvolvimento (similar a var_dump do PHP)

## Erros comuns

### Erro frequente 1

**Problema**: Arquivo salvo com encoding incorreto não aparece nas atualizações
**Diagnóstico**: Arquivo não sincroniza via wBuy Watcher
**Solução**: Verificar que o arquivo está salvo em **ISO-8859-1**, não UTF-8

### Erro frequente 2

**Problema**: Variáveis do Twig não aparecem renderizadas na página
**Diagnóstico**: HTML aparece com {{ variable }} literal
**Solução**: Verificar se a função ou objeto Twig existe; usar `pr()` para debugar os dados disponíveis

## Veja também

- [01-introducao/como-usar-esta-documentacao.md](../../01-introducao/como-usar-esta-documentacao.md)
- [01-introducao/por-onde-comecar.md](../../01-introducao/por-onde-comecar.md)
- [02-twig/visao-geral-twig.md](../../02-twig/visao-geral-twig.md)
