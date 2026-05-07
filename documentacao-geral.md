# Estrutura de Documentação AI-Ready — wBuy Templates

**Versão:** 1.0 | **Data:** Abril 2026 | **Metodologia:** IA-First

---

## Sumário

1. [Resumo Executivo](#resumo-executivo)
2. [Estrutura Completa de Pastas](#estrutura-completa-de-pastas)
3. [Configurações manifest.json](#configurações-manifestjson)
4. [Definição do Conteúdo dos Arquivos](#definição-do-conteúdo-dos-arquivos)
5. [Diretrizes de Implementação](#diretrizes-de-implementação)
6. [Apêndices](#apêndices)

---

## Resumo Executivo

### 1.1 Visão Geral da Abordagem AI-Ready

A estrutura de documentação AI-Ready criada para a plataforma wBuy representa uma implementação sistemática da metodologia *Documentação IA First*, cujo objetivo central é produzir bases de conhecimento que agentes de inteligência artificial e assistentes de linguagem natural possam consumir com máxima eficiência, precisão e rastreabilidade.

A documentação foi organizada em **10 pastas principais** com prefixos numéricos (`00-indice` a `09-exemplos`), totalizando **140 arquivos Markdown** e **10 arquivos manifest.json**. Cada pasta cobre um domínio temático da plataforma de templates wBuy, desde conceitos fundamentais de Twig até modelos completos de páginas e exemplos integrados.

O princípio fundamental é a filosofia *"um conceito por arquivo"*: cada arquivo documenta exatamente um tópico, garantindo que consultas de IA retornem contexto preciso sem ruído informacional. Os arquivos utilizam YAML front matter padronizado para metadata estruturada e seções pré-definidas para uniformidade de conteúdo.

#### Estatísticas do Projeto

- **10** Pastas Temáticas
- **140** Arquivos .md
- **10** manifest.json
- **10** README.md
- **4** Tipos de documento
- **6** Seções padrão

### 1.2 Benefícios da Documentação IA First

A abordagem IA-First difere fundamentalmente de documentações tradicionais em vários aspectos críticos. Enquanto documentações convencionais são escritas para leitura linear humana, documentações IA-ready são otimizadas para recuperação semântica, indexação vetorial e raciocínio multi-hop de modelos de linguagem.

| Aspecto | Documentação Tradicional | Documentação IA-Ready (wBuy) |
|---------|-------------------------|------------------------------|
| **Granularidade** | Páginas longas com múltiplos tópicos | Um conceito por arquivo (max. 1200 palavras) |
| **Estrutura** | Formato livre, variável por autor | Seções padronizadas em todos os arquivos |
| **Metadata** | Ausente ou inconsistente | YAML front matter com 6 campos obrigatórios |
| **Navegação** | Links ad-hoc, sem padrão | Campo `related` para recuperação multi-hop |
| **Rastreabilidade** | Sem origem documentada | `source_url` em cada entrada do manifesto |
| **Taxonomia** | Nenhuma | 4 tipos: concept, reference, how-to, example |
| **Descoberta por IA** | Baixa precisão de recuperação | Alta precisão via slug, tags e resumo |

**Resultado esperado:** Com esta estrutura, assistentes de IA podem responder perguntas técnicas sobre templates wBuy com contexto preciso, links para arquivos relacionados e rastreabilidade total da fonte original — sem necessidade de acesso ao navegador ou interface gráfica.

---

## Estrutura Completa de Pastas

### 2.1 Árvore Visual de Diretórios

```
wbuy-docs-structure/
├── 00-indice/
│   ├── README.md
│   ├── manifest.json
│   ├── sidebar.md
│   └── taxonomia-documentacao.md
├── 01-introducao/
│   ├── README.md
│   ├── manifest.json
│   ├── visao-geral.md
│   ├── por-onde-comecar.md
│   ├── wbuy-watcher-npm.md
│   ├── encoding-iso-8859-1.md
│   ├── telas-customizaveis.md
│   ├── criacao-de-widgets-com-include.md
│   ├── documentacao-api-postman.md
│   ├── chamadas-auxiliares.md
│   ├── checklist-modulos-obrigatorios.md
│   └── como-usar-esta-documentacao.md
├── 02-twig/
│   ├── README.md
│   ├── manifest.json
│   ├── visao-geral-twig.md
│   ├── sintaxe-basica.md
│   ├── loops-for.md
│   ├── condicionais-if.md
│   ├── include-no-twig.md
│   ├── funcao-pr.md
│   ├── funcao-separa.md
│   ├── funcao-plural.md
│   └── exemplo-loop-pr.md
├── 03-api/
│   ├── README.md
│   ├── manifest.json
│   ├── visao-geral-api.md
│   ├── categorygetall.md
│   ├── categorygetlevel1.md
│   ├── categorygetlevel2.md
│   ├── categorygetlevel3.md
│   ├── configuracoes-config-tema-json.md
│   ├── getcolors.md
│   ├── getlastorderuser.md
│   ├── getvariations.md
│   └── productget.md
├── 04-store/
│   ├── README.md
│   ├── manifest.json
│   └── [41 arquivos de recursos store]
├── 05-html/
│   ├── README.md
│   ├── manifest.json
│   └── [5 arquivos de componentes HTML]
├── 06-paginas/
│   ├── README.md
│   ├── manifest.json
│   └── [8 arquivos de páginas customizáveis]
├── 07-modelos/
│   ├── README.md
│   ├── manifest.json
│   └── [38 arquivos de modelos]
├── 08-cache/
│   ├── README.md
│   ├── manifest.json
│   └── cache-recursos-gerais.md
└── 09-exemplos/
    ├── README.md
    ├── manifest.json
    └── [5 arquivos de exemplos integrados]
```

### 2.2 Resumo das 10 Pastas

| Pasta | Objetivo | Arquivos |
|-------|----------|----------|
| `00-indice` | Mapa da documentação e critérios de organização IA-ready | 2 tópicos + README + manifest |
| `01-introducao` | Fundamentos para iniciar desenvolvimento de templates na plataforma wBuy | 10 tópicos + README + manifest |
| `02-twig` | Conceitos e referências de Twig v2 para templates wBuy | 9 tópicos + README + manifest |
| `03-api` | Métodos da API consumidos nos templates | 10 tópicos + README + manifest |
| `04-store` | Métodos store, recursos globais e flags gerais | 41 tópicos + README + manifest |
| `05-html` | Componentes HTML prontos para reutilização | 5 tópicos + README + manifest |
| `06-paginas` | Páginas customizáveis e seus contextos de dados | 8 tópicos + README + manifest |
| `07-modelos` | Modelos completos de páginas, topo/rodapé, CSS e widgets | 38 tópicos + README + manifest |
| `08-cache` | Conteúdo específico de cache da plataforma | 1 tópico + README + manifest |
| `09-exemplos` | Casos aplicados unindo conceitos de diferentes seções | 5 tópicos + README + manifest |

---

## Configurações manifest.json

Cada pasta contém um arquivo `manifest.json` que serve como índice estruturado para ingestão por sistemas de IA, pipelines de RAG (Retrieval-Augmented Generation) e ferramentas de busca semântica. O manifesto lista todos os arquivos da pasta com título, caminho, ordem de leitura e URL de origem.

### 3.1 Schema do Manifesto

Todos os manifestos seguem o mesmo schema de entrada, com quatro campos obrigatórios:

```json
{
  "title":      "Titulo legivel do topico",
  "path":       "XX-pasta/nome-do-arquivo.md",
  "order":      1,
  "source_url": "https://doc-templates.wbuy.com.br/post/slug/"
}
```

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `title` | string | Nome legível do tópico, compatível com busca full-text e exibição em UI |
| `path` | string | Caminho relativo a raiz `wbuy-docs-structure/`, sempre em kebab-case |
| `order` | integer | Ordem recomendada de leitura dentro da pasta, começando em 1 |
| `source_url` | string (URL) | URL canônico da fonte original — preserva rastreabilidade e permite atualizações |

---

## Definição do Conteúdo dos Arquivos

Esta seção descreve a anatomia de cada arquivo `.md`, incluindo o YAML front matter obrigatório, as seções padrão de conteúdo e os guias de populamento por pasta da documentação.

### 4.1 YAML Front Matter Padrão

Todo arquivo `.md` da documentação inicia com um bloco YAML delimitado por `---`. Este bloco é o que permite que sistemas de IA e indexadores estruturem o conhecimento antes mesmo de ler o conteúdo principal.

#### Exemplo de YAML front matter completo

```yaml
---
title: "Função pr()"
slug: "funcao-pr"
doc_type: "reference"
summary: "Inspeção e debug de variáveis no contexto Twig."
tags:
  - twig
  - debug
  - pr
related:
  - 02-twig/exemplo-loop-pr.md
---
```

#### YAML front matter — tipo concept (introdução)

```yaml
---
title: "Visão geral dos templates wBuy"
slug: "visao-geral-templates-wbuy"
doc_type: "concept"
summary: "Panorama de tecnologias e componentes da stack de templates."
tags:
  - introducao
  - wbuy
  - templates
related:
  - 01-introducao/por-onde-comecar.md
---
```

#### YAML front matter — tipo example (09-exemplos)

```yaml
---
title: "Exemplo: Home com banners e vitrine"
slug: "exemplo-home-banners-vitrine"
doc_type: "example"
summary: "Exemplo integrado de home com widgets de banner e vitrine."
tags:
  - exemplo
  - home
related:
  - 07-modelos/pagina-inicial-modelo-01.md
  - 04-store/mainbanner.md
---
```

### 4.2 Seções Padrão dos Arquivos

Após o YAML front matter, cada arquivo segue um template de seções padronizadas que garantem uniformidade entre todos os 140 documentos. A IA pode localizar qualquer informação específica navegando por essas seções previsíveis:

| Seção | Descrição e Instruções de Populamento |
|-------|---------------------------------------|
| `## O que faz` | Definição objetiva do conceito, recurso ou função. Deve responder "o que é" e "para que serve" em no máximo 3 parágrafos curtos. Evitar jargão excessivo. |
| `## Sintaxe` | Assinatura da função/método, parâmetros aceitos, valores de retorno. Usar bloco de código com linguagem (twig, js, json). Opcional para arquivos do tipo *concept*. |
| `## Quando usar` | Cenários ideais de aplicação, pré-condições necessárias e limites de uso. Pode incluir lista de pontos ou comparativo com alternativas. |
| `## Exemplo` | Exemplo mínimo funcional com resultado esperado. Preferir exemplos que possam ser copiados diretamente. Incluir comentários inline para clareza. |
| `## Observações` | Notas de compatibilidade, implicações de performance, interação com cache total da plataforma, impacto em SEO, comportamento em mobile. |
| `## Erros comuns` | Problemas recorrentes observados por desenvolvedores, com diagnóstico e solução recomendada. Formato: problema em negrito + explicação. |
| `## Veja também` | Links internos para arquivos relacionados (usando paths relativos). Esta seção viabiliza a recuperação multi-hop de IA — é crítica para contexto encadeado. |

**Nota sobre placeholders:** Os arquivos criados contam com placeholders marcados como `> Placeholder IA-ready. Preencher com conteúdo definitivo mantendo um conceito por arquivo (300-1200 palavras).` O populamento do conteúdo real deve respeitar os campos de cada seção e manter o YAML front matter intacto.

### 4.3 Conteúdo por Seção

#### 00-indice — Mapa e Taxonomia

- **sidebar.md** — Estrutura de navegação entre pastas e tópicos. Funciona como sumário navegável da documentação inteira, com links internos para cada pasta e descrição resumida de cada seção.
- **taxonomia-documentacao.md** — Define os quatro tipos de documento (*concept*, *reference*, *how-to*, *example*) com critérios de classificação, exemplos de uso e diretrizes para atribuição do campo `doc_type`.

#### 01-introducao — Fundamentos da Plataforma

- **visao-geral.md** — Panorama da stack tecnológica: Twig v2, store object, API de templates, NPM watcher, encoding ISO-8859-1.
- **por-onde-comecar.md** — Sequência recomendada para iniciar um template: instalação do watcher, configuração do ambiente, criação da primeira tela customizável.
- **wbuy-watcher-npm.md** — Instruções de instalação do pacote NPM `wbuy-watcher`, configuração do `config.json` local e uso do comando `wbuy watch`.
- **encoding-iso-8859-1.md** — Regra de codificação obrigatória para todos os arquivos de template. Consequências de usar UTF-8 e como configurar editores.
- **telas-customizaveis.md** — Lista completa das telas da plataforma que suportam customização via template, com identificadores de contexto Twig.
- **criacao-de-widgets-com-include.md** — Passo a passo para criar um widget como arquivo separado e incluir no template pai via `include()` Twig.
- **documentacao-api-postman.md** — Como acessar a coleção Postman oficial e usar os endpoints de referência durante o desenvolvimento.
- **chamadas-auxiliares.md** — Métodos AJAX auxiliares disponibilizados pela plataforma para dinamismo do tema sem recarregamento de página.
- **checklist-modulos-obrigatorios.md** — Lista de verificação para aprovação de templates pela equipe wBuy, incluindo módulos, seções e validações obrigatórias.
- **como-usar-esta-documentacao.md** — Guia de leitura da documentação por perfil de usuário (iniciante, desenvolvedor experiente, consultor de IA).

#### 02-twig — Engine de Templates

- **visao-geral-twig.md** — Contexto histórico e arquitetural do Twig v2 nos templates wBuy. Diferença entre Twig puro e a implementação wBuy.
- **sintaxe-basica.md** — Variáveis `{{ variavel }}`, filtros `{{ val|upper }}`, tags de controle `{% ... %}` e comentários `{# ... #}`.
- **loops-for.md** — Iteração com `{% for item in coleção %}`, acesso a `loop.index`, `loop.first`, `loop.last` e tratamento de coleções vazias com `{% else %}`.
- **condicionais-if.md** — Estruturas `{% if %}`, `{% elseif %}`, `{% else %}` com operadores de comparação e operadores `and`/`or`/`not`.
- **include-no-twig.md** — Composição de templates com `{% include 'widgets/nome.html' %}`, passagem de variáveis e boas práticas de organização.
- **funcao-pr.md** — Função de debug `pr(variavel)` para inspecionar estrutura de arrays e objetos no contexto Twig durante desenvolvimento.
- **funcao-separa.md** — Função utilitária `separa()` para divisão e formatação de strings em Twig/PHP.
- **funcao-plural.md** — Função `plural()` para pluralização condicional de textos com base em quantidade numérica.
- **exemplo-loop-pr.md** — Exemplo prático: iteração sobre um array de produtos usando `for` e inspeção com `pr()` para visualizar a estrutura de dados disponível.

#### 03-api — Métodos de API

- **visao-geral-api.md** — Panorama dos métodos de API consumidos em templates — diferença entre chamadas server-side (Twig) e client-side (AJAX).
- **categorygetall.md** — Retorna todas as categorias da loja. Estrutura do retorno, campos disponíveis e uso em menus de navegação.
- **categorygetlevel1/2/3.md** — Retornam categorias filtradas por nível hierárquico (1=raiz, 2=subcategoria, 3=sub-subcategoria).
- **configuracoes-config-tema-json.md** — Leitura do arquivo `config_tema.json` via API para aplicar configurações personalizadas definidas pelo lojista.
- **getcolors.md** — Retorna as cores configuradas na plataforma para uso dinâmico em variáveis CSS do template.
- **getlastorderuser.md** — Recupera o último pedido do usuário logado para exibição em áreas personalizadas do template.
- **getvariations.md** — Retorna as variações (SKU) disponíveis para um produto específico.
- **productget.md** — Método principal para recuperar dados completos de um produto por ID ou slug.

#### 04-store — Objeto Global Store

A pasta `04-store` é a maior da documentação, com 41 arquivos cobrindo o objeto JavaScript global `store`, métodos auxiliares, recursos de detecção de dispositivo, listeners de eventos e flags de integrações de terceiros.

- **visao-geral-store.md** — Arquitetura do objeto `store` — quando é carregado, como acessar no JS do tema e relação com o objeto `geral`.
- **detect-ismobile.md** — Método `detect.isMobile()` para detecção de dispositivo móvel em runtime — base para renderização condicional de componentes.
- **listeners-readlistener.md** — Eventos customizados como `totalItensCarrinho` e `onAddProductCart` — como registrar listeners para reagir a mudanças no carrinho.
- **cart.md** — Objeto `cart` com dados do carrinho atual: itens, quantidades, totais e URL de checkout.
- **mainbanner.md** — Recurso `mainBanner` para exibição de banners principais (slider) na página inicial.
- **pageproducts.md** — Recurso `pageProducts` com lista de produtos paginados para páginas de categoria, busca e vitrine.
- **geral-hasopolen.md / geral-hasperformaai.md / geral-hassmarthint.md** — Flags booleanas no objeto `geral` que indicam se integrações de terceiros (Opolen, PerformaAI, SmartHint) estão ativas na loja.

#### 05-html — Componentes HTML

- **agrupador-de-produtos.md** — Componente que agrupa produtos relacionados ou variantes em um único bloco visual.
- **html-buytogether-produtoid.md** — Componente `html.buyTogether(produtoId)` para exibição de sugestões de "compre junto" na página de produto.
- **html-productdetailsku.md** — Componente `html.productDetailSKU` que renderiza o seletor completo de variações (cores, tamanhos) na página de produto.
- **productbox.md** — Componente `productBox` — card padrão de produto usado em listagens, vitrines e páginas de categoria.

#### 06-paginas — Páginas Customizáveis

- **detalhes-do-produto.md** — Contexto Twig disponível na página de produto: variáveis `product`, `variations`, `images`, `reviews` e integração com componentes HTML.
- **pagina-de-busca.md** — Variáveis de paginação, termo pesquisado (`search_term`), lista de resultados e recursos de ordenação/filtro disponíveis.
- **pagina-de-categorias.md** — Objeto `page_category` com dados da categoria atual, produtos filhos e suporte a paginação dinâmica.
- **pagina-de-produtos-de-uma-filial-multiloja.md** — Contexto específico para lojas com múltiplas filiais — variáveis de filial disponível e listagem de produtos por filial.
- **paginas-customizadas.md** — Como criar e registrar páginas personalizadas que não seguem estrutura padrão de categoria ou produto.

#### 07-modelos — Biblioteca de Modelos

A pasta `07-modelos` contém 38 arquivos de modelos prontos divididos em: páginas completas (10), estruturas de topo (6 modelos), rodapé (1 modelo), variáveis CSS por modelo (9 arquivos) e widgets de página inicial (11 widgets).

#### 08-cache — Estratégias de Cache

- **cache-recursos-gerais.md** — Estratégias para compatibilizar o tema com o cache total da plataforma wBuy: blocos de cache exclusivo, uso de AJAX para dados dinâmicos e padrões de invalidação de cache.

#### 09-exemplos — Casos Integrados

- **home-com-banners-e-vitrine.md** — Exemplo completo de página inicial integrando `mainBanner` (slider), `showcaseProduct` (vitrine) e `pageProducts` para produtos em destaque.
- **pagina-produto-com-sku.md** — Integração de `store.productDetail()`, `html.productDetailSKU` e `html.buyTogether()` na página de detalhes do produto.
- **busca-com-paginacao.md** — Listagem paginada com loop Twig sobre `pageProducts`, controles de paginação e ordenação dinâmica via AJAX.
- **categorias-com-menu-lateral.md** — Renderização de `page_category` com menu lateral usando `store.categoriesMenu()` e destaque da categoria ativa.
- **carrinho-suspenso-assincrono.md** — Carrinho lateral usando `cart` com `readListener` para atualização assíncrona — compatível com cache total da plataforma.

---

## Diretrizes de Implementação

As boas práticas a seguir garantem que a documentação permaneça IA-ready ao longo do tempo, mesmo com contribuições de múltiplos autores e evolução da plataforma wBuy.

### 5.1 Boas Práticas para Arquivos de Tópico

#### Princípio: Um Conceito por Arquivo

Este é o princípio mais importante da metodologia IA-First. Cada arquivo deve abordar exatamente um conceito, função, recurso ou exemplo. Arquivos com múltiplos tópicos degradam a precisão de recuperação semântica e aumentam o ruído nas respostas de IA.

**Regra prática:** Se você não consegue descrever o arquivo em uma frase curta (campo `summary` do YAML), o arquivo provavelmente precisa ser dividido.

#### Tamanho Recomendado: 300-1200 Palavras

O intervalo de 300 a 1200 palavras é ideal para que o contexto do arquivo caiba dentro da janela de contexto de modelos de linguagem sem truncamento, ao mesmo tempo em que é suficientemente rico para responder perguntas específicas.

- **Mínimo (300 palavras):** Arquivos de referência simples como flags booleanas (`geral.hasOpolen`)
- **Ideal (600-900 palavras):** Referências de métodos com sintaxe, exemplo e observações
- **Máximo (1200 palavras):** Guias de página ou exemplos integrados com múltiplos componentes

#### Uso de Links Internos (Campo related)

O campo `related` no YAML front matter é a espinha dorsal da recuperação multi-hop — a capacidade de IA de encadear múltiplas consultas para construir uma resposta completa. Diretrizes:

- Listar entre 1 e 5 arquivos relacionados no campo `related`
- Priorizar arquivos que são pré-requisito ou complemento direto do tópico
- Na seção `## Veja também`, usar o mesmo path relativo do YAML
- Evitar referências circulares (A aponta para B que aponta para A sem valor adicional)

#### Consistência de Tags

As tags no YAML front matter alimentam sistemas de busca facetada e agrupamento automático. Recomendações:

- Usar tags da pasta como base: `twig`, `api`, `store`, `html`, `pagina`, `modelo`, `cache`, `exemplo`
- Adicionar tags de funcionalidade específica: `carrinho`, `produto`, `categoria`, `banner`, `mobile`
- Não repetir o `doc_type` como tag (já é um campo separado)
- Usar letras minúsculas e kebab-case para tags compostas: `page-products`, `multi-hop`

### 5.2 Manutenção de Manifestos e README

#### Atualização do manifest.json

Ao adicionar ou remover arquivos de uma pasta, o `manifest.json` deve ser atualizado na mesma operação. Não deixar entradas órfãs (que apontam para arquivos inexistentes) nem arquivos sem entrada no manifesto.

| Operação | Ação no manifest.json |
|----------|----------------------|
| Adicionar novo arquivo | Adicionar entrada no final do array, com `order` incrementado |
| Remover arquivo | Remover entrada e renumerar `order` dos arquivos subsequentes |
| Renomear arquivo | Atualizar campo `path` na entrada correspondente |
| Reordenar leitura | Atualizar campo `order` de todas as entradas afetadas |
| Atualizar fonte | Atualizar campo `source_url` com a URL canônica atual |

#### README.md por Pasta

Cada `README.md` deve conter três elementos essenciais:

1. **Escopo da pasta:** Uma ou duas frases descrevendo o domínio coberto
2. **Ordem recomendada de leitura:** Lista numerada com os arquivos no `order` definido no manifesto
3. **Convenções específicas da pasta:** Nomenclatura, tipo predominante de `doc_type`, e eventuais dependências de outras pastas

### 5.3 Convenções de Nomenclatura

#### Arquivos: kebab-case Descritivo

Todos os arquivos usam kebab-case (letras minúsculas, hífens como separadores). O nome deve ser descritivo o suficiente para identificar o conteúdo sem abrir o arquivo:

| Padrão | Exemplo correto | Exemplo incorreto |
|--------|-----------------|------------------|
| Função/método | `funcao-pr.md` | `pr.md`, `funcaoPr.md` |
| Recurso store | `mainbanner.md` | `main-banner.md`, `MainBanner.md` |
| Página | `pagina-de-busca.md` | `busca.md`, `paginaDeBusca.md` |
| Modelo | `topo-modelo-01.md` | `topo1.md`, `header-model-01.md` |
| Exemplo | `home-com-banners-e-vitrine.md` | `exemplo1.md`, `home.md` |

#### Slugs: Identificadores Únicos e Estáveis

O campo `slug` no YAML deve ser único em toda a documentação e não deve mudar após publicação (é utilizado em URLs e referências externas). Usar o nome do arquivo sem extensão, exceto quando o nome for ambíguo entre pastas.

#### Prefixos Numéricos das Pastas

Os prefixos `00` a `09` definem a ordem lógica de onboarding: conceitos gerais primeiro (`00`, `01`), tecnologias core (`02`, `03`, `04`), componentes HTML (`05`), páginas (`06`), modelos completos (`07`), casos especiais (`08`) e exemplos integrados (`09`).

**Dica para atualizações:** Nunca renumerar as pastas existentes ao adicionar novas pastas — isso quebraria todos os paths nos campos `related` e nos manifestos. Novas pastas temáticas devem receber números maiores que `09`, como `10-integrações`.

---

## Apêndices

### A. Resumo do Guia Documentação IA-First Original

O guia de referência *Documentação IA First* estabelece os princípios fundamentais que orientaram a criação desta estrutura para a plataforma wBuy. A seguir, um resumo dos requisitos centrais do guia:

| Requisito do Guia | Implementação na Estrutura wBuy |
|-------------------|----------------------------------|
| Granularidade atômica de conteúdo | Um conceito por arquivo `.md`, máximo 1200 palavras |
| Metadata estruturada e padronizada | YAML front matter com 6 campos: title, slug, doc_type, summary, tags, related |
| Taxonomia de tipos de documentos | Quatro tipos: concept, reference, how-to, example (campo doc_type) |
| Rastreabilidade de origem | Campo source_url em cada entrada do manifest.json |
| Navegação multi-hop para IA | Campo related no YAML + seção "Veja também" com links internos |
| Índice de descoberta da documentação | Pasta 00-indice com sidebar.md e manifest.json em cada pasta |
| Nomenclatura previsível e consistente | kebab-case para arquivos, prefixos numéricos para pastas |
| Seções padronizadas em todos os arquivos | 7 seções fixas: O que faz, Sintaxe, Quando usar, Exemplo, Observações, Erros comuns, Veja também |
| Compatibilidade com RAG e busca semântica | Resumo no campo summary, tags para indexação facetada, tamanho controlado |
| Documentação da estrutura em si | Arquivo DOCUMENTATION_STRUCTURE.md com tree completa e instruções |

### B. Taxonomia dos Tipos de Conteúdo

Os quatro tipos de documento definem como o conteúdo deve ser estruturado e como a IA deve interpretar e usar o arquivo ao responder perguntas:

| Tipo | Uso | Características | Exemplos na estrutura wBuy |
|------|-----|-----------------|---------------------------|
| **concept** | Explicar *o que é* e *por que existe* | Prioriza compreensão. Menor ênfase em sintaxe. Pode ter subseções narrativas. Leitura linear. | `visao-geral.md`, `visao-geral-twig.md`, `visao-geral-store.md` |
| **reference** | Documentar *como funciona* um recurso específico | Prioriza completude. Sintaxe, parâmetros e retorno obrigatórios. Consulta não-linear. | `funcao-pr.md`, `categorygetall.md`, `cart.md`, `mainbanner.md` |
| **how-to** | Guiar *como realizar* uma tarefa específica | Sequência de passos numerados. Foco no resultado final. Pré-condições explícitas. | `por-onde-comecar.md`, `criacao-de-widgets-com-include.md`, `checklist-modulos-obrigatorios.md` |
| **example** | Demonstrar *como vários recursos funcionam juntos* | Cenário real completo. Código funcional. Múltiplos `related`. Pressupõe leitura dos references. | `home-com-banners-e-vitrine.md`, `carrinho-suspenso-assincrono.md`, `exemplo-loop-pr.md` |

#### Critérios de Classificação

Use as perguntas abaixo para determinar o tipo correto ao criar um novo arquivo:

- **"O arquivo explica o que algo é?"** → **concept**
- **"O arquivo documenta parâmetros, retornos e sintaxe de uma função?"** → **reference**
- **"O arquivo ensina como realizar uma tarefa passo a passo?"** → **how-to**
- **"O arquivo mostra um caso de uso completo com código funcional?"** → **example**

### C. Definição dos Campos de Metadados

A tabela abaixo define formalmente cada campo do YAML front matter, com tipo, obrigatoriedade, restrições e impacto em sistemas de IA:

| Campo | Tipo | Obrig. | Restrições | Uso pela IA |
|-------|------|--------|------------|-------------|
| `title` | string | Sim | Max. 80 chars. Deve ser legível por humanos. Pode ter caracteres especiais. | Exibido em resultados de busca; usado como título em respostas de IA |
| `slug` | string | Sim | kebab-case, sem acentos, único em toda a documentação. Imutável após publicação. | Identificador URL-safe para deep-link; chave de deduplicação |
| `doc_type` | enum | Sim | Valores válidos: `concept`, `reference`, `how-to`, `example` | Filtragem por tipo; instrui IA sobre como usar o conteúdo |
| `summary` | string | Sim | Max. 160 chars. Uma frase completa. Sem markdown. Deve funcionar como snippet autônomo. | Exibido sem abrir o arquivo; usado como contexto em buscas semânticas |
| `tags` | array<string> | Sim | Min. 2, max. 8 tags. Letras minúsculas. Termos do domínio wBuy (não genéricos). | Busca facetada; agrupamento de documentos por tema; sugestão de relacionados |
| `related` | array<path> | Sim | Paths relativos a raiz `wbuy-docs-structure/`. Min. 1 item. Max. 5 itens. | Recuperação multi-hop; expansão de contexto; navegação encadeada de IA |

#### Campos do manifest.json (complementares)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| `title` | string | Título do arquivo — pode diferir do título interno do `.md` para maior clareza no índice |
| `path` | string | Caminho relativo a raiz `wbuy-docs-structure/`, incluindo a pasta e nome do arquivo |
| `order` | integer | Ordem recomendada de leitura dentro da pasta. Inicia em 1. Deve ser único por pasta. |
| `source_url` | URL string | URL canônica da documentação original — permite rastrear a fonte e verificar atualizações |

**Compatibilidade RAG:** Esta estrutura é projetada para ingestão direta em pipelines de RAG (Retrieval-Augmented Generation). O campo `summary` serve como documento de busca de alta densidade, enquanto o conteúdo completo do arquivo serve como contexto de resposta. Os campos `tags` e `doc_type` permitem filtragem pré-recuperação para aumentar precisão.

---

## Informações Finais

**Projeto:** Estrutura de Documentação AI-Ready — wBuy Templates
**Metodologia:** IA First
**Versão:** 1.0
**Data de Criação:** Abril 2026
**Localização Padrão:** `/home/ubuntu/wbuy-docs-structure/`

**Estrutura:**
- 10 pastas principais
- 140 arquivos .md
- 10 manifest.json
- 10 README.md

Esta documentação é a referência definitiva para o desenvolvimento do projeto IA-Ready da plataforma wBuy.
