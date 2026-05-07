---
title: "Visão geral dos templates wBuy"
slug: "visao-geral-templates-wbuy"
doc_type: "concept"
summary: "Panorama da stack de templates wBuy: Twig v2, objeto store, API de templates, NPM watcher e encoding ISO-8859-1."
tags:
  - introducao
  - wbuy
  - templates
  - twig
  - store
related:
  - 01-introducao/por-onde-comecar.md
  - 01-introducao/telas-customizaveis.md
  - 02-twig/visao-geral-twig.md
  - 04-store/visao-geral-store.md
---

# Visão geral dos templates wBuy

A plataforma wBuy permite que desenvolvedores criem temas visuais personalizados para lojas virtuais.
A customização é feita por meio de templates que combinam HTML, CSS, JavaScript e a engine
de templates Twig v2 — com acesso a dados da loja via objeto global `store` e métodos de API.

## O que faz

A stack de templates wBuy é composta por quatro camadas principais que trabalham juntas:

**1. Twig v2 (engine de templates)**
Responsável pela renderização server-side das páginas. É no Twig que você acessa variáveis
da loja, escreve loops, condicionais e inclui componentes reutilizáveis (widgets).
Toda a lógica de exibição de dados — produtos, categorias, banners — passa pelo Twig.

**2. Objeto `store` (dados da loja em runtime)**
Objeto JavaScript global disponível no contexto do tema. Contém dados dinâmicos da loja
como carrinho, produtos, categorias, banners e configurações. É a principal fonte de dados
para interações client-side (sem recarregar a página).

**3. API de templates**
Conjunto de métodos consumidos nos templates para recuperar dados específicos da loja,
como categorias (`categoryGetAll`), variações de produto (`getVariations`) e dados do
último pedido (`getLastOrderUser`). Alguns métodos são chamados server-side (Twig),
outros client-side (AJAX).

**4. wBuy Watcher (NPM)**
Ferramenta de desenvolvimento local que observa alterações nos arquivos do tema e
sincroniza com a plataforma em tempo real. É o ponto de partida para qualquer
desenvolvimento de template.

## Sintaxe

Não se aplica. Este documento é uma visão geral conceitual e não documenta funções ou métodos.
Consulte os arquivos de referência de cada camada para detalhes de sintaxe.

## Quando usar

Leia este arquivo quando:

- você está começando a desenvolver um template wBuy pela primeira vez;
- você precisa entender como as partes da stack se relacionam antes de consultar
  documentações específicas;
- você quer orientar um agente de IA sobre o contexto geral da plataforma.

## Exemplo

Fluxo típico de uma página de categoria renderizada pela plataforma:

1. O servidor processa o template Twig da página de categorias
2. O Twig acessa variáveis como `pageProducts` e `page_category` para montar o HTML
3. O HTML é entregue ao navegador já com os dados renderizados (server-side)
4. O JavaScript do tema usa o objeto `store` para interações dinâmicas
   (ex.: adicionar ao carrinho sem recarregar a página)

## Observações

- **Encoding obrigatório**: todos os arquivos de template devem ser salvos em
  ISO-8859-1. Usar UTF-8 pode causar problemas de caracteres especiais na renderização.
  Veja `encoding-iso-8859-1.md` para detalhes.
- **Twig v2, não v3**: a plataforma usa especificamente a versão 2 do Twig.
  Algumas funcionalidades do Twig v3 não estão disponíveis.
- **Cache total**: a plataforma possui cache de página completa. Dados dinâmicos
  (ex.: carrinho, usuário logado) devem ser carregados via AJAX para não serem
  armazenados em cache. Veja `08-cache/cache-recursos-gerais.md`.

## Erros comuns

- **Usar sintaxe do Twig v3**  
  Diagnóstico: filtros ou funções não reconhecidos pelo template engine.  
  Correção: consultar a documentação do Twig v2 e ajustar a sintaxe.

- **Salvar arquivos em UTF-8**  
  Diagnóstico: caracteres especiais (acentos, ç) aparecem corrompidos na loja.  
  Correção: configurar o editor para salvar em ISO-8859-1.

- **Renderizar dados dinâmicos diretamente no Twig**  
  Diagnóstico: dados de carrinho ou usuário ficam "presos" no cache e não atualizam.  
  Correção: carregar esses dados via AJAX usando o objeto `store`.

## Veja também

- [Por onde começar](./por-onde-comecar.md)
- [Telas customizáveis](./telas-customizaveis.md)
- [Visão geral do Twig v2](../02-twig/visao-geral-twig.md)
- [Visão geral do objeto store](../04-store/visao-geral-store.md)
- [Cache - Recursos gerais](../08-cache/cache-recursos-gerais.md)