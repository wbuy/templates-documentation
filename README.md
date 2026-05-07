# DOCUMENTATION_STRUCTURE

## Estrutura completa (tree)

```text
wbuy-docs-structure/
├── 00-indice/
    ├── README.md
    ├── manifest.json
    ├── sidebar.md
    └── taxonomia-documentacao.md
├── 01-introducao/
    ├── README.md
    ├── manifest.json
    ├── visao-geral.md
    ├── por-onde-comecar.md
    ├── wbuy-watcher-npm.md
    ├── encoding-iso-8859-1.md
    ├── telas-customizaveis.md
    ├── criacao-de-widgets-com-include.md
    ├── documentacao-api-postman.md
    ├── chamadas-auxiliares.md
    ├── checklist-modulos-obrigatorios.md
    └── como-usar-esta-documentacao.md
├── 02-twig/
    ├── README.md
    ├── manifest.json
    ├── visao-geral-twig.md
    ├── sintaxe-basica.md
    ├── loops-for.md
    ├── condicionais-if.md
    ├── include-no-twig.md
    ├── funcao-pr.md
    ├── funcao-separa.md
    ├── funcao-plural.md
    └── exemplo-loop-pr.md
├── 03-api/
    ├── README.md
    ├── manifest.json
    ├── visao-geral-api.md
    ├── categorygetall.md
    ├── categorygetlevel1.md
    ├── categorygetlevel2.md
    ├── categorygetlevel3.md
    ├── configuracoes-config-tema-json.md
    ├── getcolors.md
    ├── getlastorderuser.md
    ├── getvariations.md
    └── productget.md
├── 04-store/
    ├── README.md
    ├── manifest.json
    ├── visao-geral-store.md
    ├── detect-ismobile.md
    ├── listeners-readlistener.md
    ├── recursos-gerais.md
    ├── array-global.md
    ├── blogposts.md
    ├── cart.md
    ├── customerprofiles.md
    ├── featuredicon.md
    ├── footertext.md
    ├── formularios-dinamicos.md
    ├── getbrands.md
    ├── getcommentsproduct.md
    ├── getdynamicpages.md
    ├── getfiliaismultiloja.md
    ├── getinfopages.md
    ├── getratings.md
    ├── getstoredata.md
    ├── geturlcheckouttemp.md
    ├── mainbanner.md
    ├── pageproducts.md
    ├── paymentbrand.md
    ├── productboxdefault.md
    ├── productkit.md
    ├── producttobox.md
    ├── publicitybanner.md
    ├── securityseal.md
    ├── showcaseproduct.md
    ├── socialicons.md
    ├── store-categories.md
    ├── store-categoriesmenu.md
    ├── store-gettexttop.md
    ├── store-periodicoffers.md
    ├── store-productdetail.md
    ├── store-widgetinstagram.md
    ├── store-widgetnews.md
    ├── userstore.md
    ├── widgetfacebook.md
    ├── geral-hasopolen.md
    ├── geral-hasperformaai.md
    └── geral-hassmarthint.md
├── 05-html/
    ├── README.md
    ├── manifest.json
    ├── visao-geral-html.md
    ├── agrupador-de-produtos.md
    ├── html-buytogether-produtoid.md
    ├── html-productdetailsku.md
    └── productbox.md
├── 06-paginas/
    ├── README.md
    ├── manifest.json
    ├── visao-geral-paginas.md
    ├── detalhes-do-produto.md
    ├── pagina-da-vitrine-personalizada.md
    ├── pagina-de-busca.md
    ├── pagina-de-categorias.md
    ├── pagina-de-produtos-de-uma-filial-multiloja.md
    ├── pagina-de-produtos-de-uma-marca.md
    └── paginas-customizadas.md
├── 07-modelos/
    ├── README.md
    ├── manifest.json
    ├── visao-geral-modelos.md
    ├── carrinho-suspenso.md
    ├── pagina-de-busca.md
    ├── pagina-de-categorias-de-produtos.md
    ├── pagina-de-categorias-de-produtos-com-paginacao-dinamica.md
    ├── pagina-de-detalhes-da-filial-apenas-multiloja.md
    ├── pagina-de-detalhes-do-produto.md
    ├── pagina-de-marcas.md
    ├── pagina-de-perfil-do-cliente-vitrine-personalizada-do-cliente.md
    ├── pagina-de-vitrine-personalizada.md
    ├── pagina-inicial-modelo-01.md
    ├── pagina-inicial-modelo-02.md
    ├── rodape-modelo-01.md
    ├── topo-modelo-01.md
    ├── topo-modelo-02.md
    ├── topo-modelo-03.md
    ├── topo-modelo-04.md
    ├── topo-modelo-05.md
    ├── topo-modelo-06.md
    ├── variaveis-css-geral.md
    ├── variaveis-css-pagina-inicial-modelo-02.md
    ├── variaveis-css-rodape.md
    ├── variaveis-css-topo-modelo-01.md
    ├── variaveis-css-topo-modelo-02.md
    ├── variaveis-css-topo-modelo-03.md
    ├── variaveis-css-topo-modelo-04.md
    ├── variaveis-css-topo-modelo-05.md
    ├── variaveis-css-topo-modelo-06.md
    ├── widget-alertas-destaque.md
    ├── widget-box-do-produto.md
    ├── widget-de-avaliacoes-para-a-pagina-inicial.md
    ├── widget-de-banners-principais-slides-da-pagina-inicial.md
    ├── widget-de-kits-looks-para-a-pagina-inicial.md
    ├── widget-de-marcas-para-a-pagina-inicial.md
    ├── widget-de-ofertas-periodicas.md
    ├── widget-instagram-para-a-pagina-inicial.md
    ├── widget-posts-do-blog-para-a-pagina-inicial.md
    └── widget-produto-sku.md
├── 08-cache/
    ├── README.md
    ├── manifest.json
    └── cache-recursos-gerais.md
└── 09-exemplos/
    ├── README.md
    ├── manifest.json
    ├── home-com-banners-e-vitrine.md
    ├── pagina-produto-com-sku.md
    ├── busca-com-paginacao.md
    ├── categorias-com-menu-lateral.md
    └── carrinho-suspenso-assincrono.md
```

## O que vai em cada pasta

### 00-indice

- Objetivo: Mapa da documentação e critérios de organização IA-ready.
- Arquivos de conteúdo:
  - `sidebar.md`: Estrutura de navegação entre pastas e tópicos principais.
  - `taxonomia-documentacao.md`: Define os tipos concept, reference, how-to e example para padronização.

### 01-introducao

- Objetivo: Fundamentos para iniciar desenvolvimento de templates na plataforma wBuy.
- Arquivos de conteúdo:
  - `visao-geral.md`: Panorama de tecnologias e componentes da stack de templates.
  - `por-onde-comecar.md`: Sequência inicial para começar um template com boas práticas.
  - `wbuy-watcher-npm.md`: Configuração de ambiente local com pacote wbuy-watcher.
  - `encoding-iso-8859-1.md`: Regras de codificação obrigatória para arquivos de template.
  - `telas-customizaveis.md`: Lista de páginas da plataforma que suportam customização.
  - `criacao-de-widgets-com-include.md`: Passo a passo para criar widgets e incluir no Twig.
  - `documentacao-api-postman.md`: Referência oficial da API no Postman para consulta de endpoints.
  - `chamadas-auxiliares.md`: Métodos auxiliares AJAX para dinamismo do tema.
  - `checklist-modulos-obrigatorios.md`: Checklist para aprovação de templates pela equipe wBuy.
  - `como-usar-esta-documentacao.md`: Orienta a leitura por tipos de arquivo e ordem recomendada.

### 02-twig

- Objetivo: Conceitos e referências de Twig v2 para templates wBuy.
- Arquivos de conteúdo:
  - `visao-geral-twig.md`: Contexto de uso da engine Twig nos templates da plataforma.
  - `sintaxe-basica.md`: Sintaxe fundamental para variáveis, filtros e estruturas de controle.
  - `loops-for.md`: Iteração de coleções e estruturas com for no Twig.
  - `condicionais-if.md`: Controle condicional com if, elseif e else no Twig.
  - `include-no-twig.md`: Composição de templates e widgets com include().
  - `funcao-pr.md`: Inspeção e debug de variáveis no contexto Twig.
  - `funcao-separa.md`: Função utilitária para separação de conteúdos em Twig/PHP.
  - `funcao-plural.md`: Função utilitária para pluralização textual em Twig/PHP.
  - `exemplo-loop-pr.md`: Exemplo prático de iteração e inspeção de dados.

### 03-api

- Objetivo: Métodos da API consumidos nos templates.
- Arquivos de conteúdo:
  - `visao-geral-api.md`: Panorama dos métodos de API usados em templates e consultas.
  - `categorygetall.md`: Referência do método categoryGetAll.
  - `categorygetlevel1.md`: Referência do método categoryGetLevel1.
  - `categorygetlevel2.md`: Referência do método categoryGetLevel2.
  - `categorygetlevel3.md`: Referência do método categoryGetLevel3.
  - `configuracoes-config-tema-json.md`: Referência do método Configurações config_tema.json.
  - `getcolors.md`: Referência do método getColors.
  - `getlastorderuser.md`: Referência do método getLastOrderUser.
  - `getvariations.md`: Referência do método getVariations.
  - `productget.md`: Referência do método productGet.

### 04-store

- Objetivo: Métodos store, recursos globais e flags gerais.
- Arquivos de conteúdo:
  - `visao-geral-store.md`: Panorama do objeto store, global e flags gerais.
  - `detect-ismobile.md`: Detecção de dispositivo para comportamento responsivo.
  - `listeners-readlistener.md`: Eventos JS como totalItensCarrinho e onAddProductCart.
  - `recursos-gerais.md`: Referência do recurso Recursos gerais.
  - `array-global.md`: Referência do recurso Array global.
  - `blogposts.md`: Referência do recurso blogPosts.
  - `cart.md`: Referência do recurso cart.
  - `customerprofiles.md`: Referência do recurso customerProfiles.
  - `featuredicon.md`: Referência do recurso featuredIcon.
  - `footertext.md`: Referência do recurso footerText.
  - `formularios-dinamicos.md`: Referência do recurso Formulários dinâmicos.
  - `getbrands.md`: Referência do recurso getBrands.
  - `getcommentsproduct.md`: Referência do recurso getCommentsProduct.
  - `getdynamicpages.md`: Referência do recurso getDynamicPages.
  - `getfiliaismultiloja.md`: Referência do recurso getFiliaisMultiloja.
  - `getinfopages.md`: Referência do recurso getInfoPages.
  - `getratings.md`: Referência do recurso getRatings.
  - `getstoredata.md`: Referência do recurso getStoreData.
  - `geturlcheckouttemp.md`: Referência do recurso getURLCheckoutTemp.
  - `mainbanner.md`: Referência do recurso mainBanner.
  - `pageproducts.md`: Referência do recurso pageProducts.
  - `paymentbrand.md`: Referência do recurso paymentBrand.
  - `productboxdefault.md`: Referência do recurso productBoxDefault.
  - `productkit.md`: Referência do recurso productKit.
  - `producttobox.md`: Referência do recurso productToBox.
  - `publicitybanner.md`: Referência do recurso publicityBanner.
  - `securityseal.md`: Referência do recurso securitySeal.
  - `showcaseproduct.md`: Referência do recurso showcaseProduct.
  - `socialicons.md`: Referência do recurso socialIcons.
  - `store-categories.md`: Referência do recurso store.categories().
  - `store-categoriesmenu.md`: Referência do recurso store.categoriesMenu().
  - `store-gettexttop.md`: Referência do recurso store.getTextTop().
  - `store-periodicoffers.md`: Referência do recurso store.periodicOffers().
  - `store-productdetail.md`: Referência do recurso store.productDetail().
  - `store-widgetinstagram.md`: Referência do recurso store.widgetInstagram().
  - `store-widgetnews.md`: Referência do recurso store.widgetNews().
  - `userstore.md`: Referência do recurso userStore.
  - `widgetfacebook.md`: Referência do recurso widgetFacebook.
  - `geral-hasopolen.md`: Referência do recurso geral.hasOpolen.
  - `geral-hasperformaai.md`: Referência do recurso geral.hasPerformaAI.
  - `geral-hassmarthint.md`: Referência do recurso geral.hasSmartHint.

### 05-html

- Objetivo: Componentes HTML prontos para reutilização.
- Arquivos de conteúdo:
  - `visao-geral-html.md`: Introduz componentes HTML reutilizáveis da plataforma.
  - `agrupador-de-produtos.md`: Referência do componente Agrupador de produtos.
  - `html-buytogether-produtoid.md`: Referência do componente html.buyTogether(produtoId).
  - `html-productdetailsku.md`: Referência do componente html.productDetailSKU.
  - `productbox.md`: Referência do componente productBox.

### 06-paginas

- Objetivo: Páginas customizáveis e seus contextos.
- Arquivos de conteúdo:
  - `visao-geral-paginas.md`: Panorama de contextos de dados por tipo de página.
  - `detalhes-do-produto.md`: Guia de implementação da página Detalhes do produto.
  - `pagina-da-vitrine-personalizada.md`: Guia de implementação da página Página da Vitrine Personalizada.
  - `pagina-de-busca.md`: Guia de implementação da página Página de busca.
  - `pagina-de-categorias.md`: Guia de implementação da página Página de categorias.
  - `pagina-de-produtos-de-uma-filial-multiloja.md`: Guia de implementação da página Página de produtos de uma Filial (Multiloja).
  - `pagina-de-produtos-de-uma-marca.md`: Guia de implementação da página Página de produtos de uma Marca.
  - `paginas-customizadas.md`: Guia de implementação da página Páginas customizadas.

### 07-modelos

- Objetivo: Modelos completos de páginas, topo/rodapé, CSS e widgets.
- Arquivos de conteúdo:
  - `visao-geral-modelos.md`: Biblioteca de modelos prontos para aceleração de desenvolvimento.
  - `carrinho-suspenso.md`: Placeholder para o modelo Carrinho suspenso.
  - `pagina-de-busca.md`: Placeholder para o modelo Página de busca.
  - `pagina-de-categorias-de-produtos.md`: Placeholder para o modelo Página de categorias de produtos.
  - `pagina-de-categorias-de-produtos-com-paginacao-dinamica.md`: Placeholder para o modelo Página de categorias com paginação dinâmica.
  - `pagina-de-detalhes-da-filial-apenas-multiloja.md`: Placeholder para o modelo Página de detalhes da Filial (Multiloja).
  - `pagina-de-detalhes-do-produto.md`: Placeholder para o modelo Página de detalhes do produto.
  - `pagina-de-marcas.md`: Placeholder para o modelo Página de Marcas.
  - `pagina-de-perfil-do-cliente-vitrine-personalizada-do-cliente.md`: Placeholder para o modelo Página de perfil do cliente.
  - `pagina-de-vitrine-personalizada.md`: Placeholder para o modelo Página de vitrine personalizada.
  - `pagina-inicial-modelo-01.md`: Placeholder para o modelo Página inicial - Modelo 01.
  - `pagina-inicial-modelo-02.md`: Placeholder para o modelo Página inicial - Modelo 02.
  - `rodape-modelo-01.md`: Placeholder para o modelo Rodapé - Modelo 01.
  - `topo-modelo-01.md`: Placeholder para o modelo Topo - Modelo 01.
  - `topo-modelo-02.md`: Placeholder para o modelo Topo - Modelo 02.
  - `topo-modelo-03.md`: Placeholder para o modelo Topo - Modelo 03.
  - `topo-modelo-04.md`: Placeholder para o modelo Topo - Modelo 04.
  - `topo-modelo-05.md`: Placeholder para o modelo Topo - Modelo 05.
  - `topo-modelo-06.md`: Placeholder para o modelo Topo - Modelo 06.
  - `variaveis-css-geral.md`: Placeholder para o modelo Variáveis CSS - Geral.
  - `variaveis-css-pagina-inicial-modelo-02.md`: Placeholder para o modelo Variáveis CSS - Página inicial modelo 02.
  - `variaveis-css-rodape.md`: Placeholder para o modelo Variáveis CSS - Rodapé.
  - `variaveis-css-topo-modelo-01.md`: Placeholder para o modelo Variáveis CSS - Topo modelo 01.
  - `variaveis-css-topo-modelo-02.md`: Placeholder para o modelo Variáveis CSS - Topo modelo 02.
  - `variaveis-css-topo-modelo-03.md`: Placeholder para o modelo Variáveis CSS - Topo modelo 03.
  - `variaveis-css-topo-modelo-04.md`: Placeholder para o modelo Variáveis CSS - Topo modelo 04.
  - `variaveis-css-topo-modelo-05.md`: Placeholder para o modelo Variáveis CSS - Topo modelo 05.
  - `variaveis-css-topo-modelo-06.md`: Placeholder para o modelo Variáveis CSS - Topo modelo 06.
  - `widget-alertas-destaque.md`: Placeholder para o modelo Widget Alertas Destaque.
  - `widget-box-do-produto.md`: Placeholder para o modelo Widget Box do Produto.
  - `widget-de-avaliacoes-para-a-pagina-inicial.md`: Placeholder para o modelo Widget de Avaliações (home).
  - `widget-de-banners-principais-slides-da-pagina-inicial.md`: Placeholder para o modelo Widget de Banners Principais.
  - `widget-de-kits-looks-para-a-pagina-inicial.md`: Placeholder para o modelo Widget de Kits/Looks.
  - `widget-de-marcas-para-a-pagina-inicial.md`: Placeholder para o modelo Widget de Marcas.
  - `widget-de-ofertas-periodicas.md`: Placeholder para o modelo Widget de Ofertas Periódicas.
  - `widget-instagram-para-a-pagina-inicial.md`: Placeholder para o modelo Widget Instagram.
  - `widget-posts-do-blog-para-a-pagina-inicial.md`: Placeholder para o modelo Widget Posts do Blog.
  - `widget-produto-sku.md`: Placeholder para o modelo Widget Produto SKU.

### 08-cache

- Objetivo: Conteúdo específico de cache da plataforma.
- Arquivos de conteúdo:
  - `cache-recursos-gerais.md`: Estratégias para compatibilizar tema com cache total da plataforma.

### 09-exemplos

- Objetivo: Casos aplicados unindo conceitos de diferentes seções.
- Arquivos de conteúdo:
  - `home-com-banners-e-vitrine.md`: Exemplo integrado de home com widgets de banner e vitrine.
  - `pagina-produto-com-sku.md`: Integração entre dados de produto, HTML SKU e widget dedicado.
  - `busca-com-paginacao.md`: Listagem paginada de busca com filtros e ordenação.
  - `categorias-com-menu-lateral.md`: Renderização de categorias usando page_category e menu lateral.
  - `carrinho-suspenso-assincrono.md`: Abordagem assíncrona para carrinho compatível com cache.

## Configuração de `manifest.json` por pasta

### 00-indice/manifest.json

- Estrutura de entrada:

```json
{
  "title": "...",
  "path": "<pasta>/<arquivo>.md",
  "order": 1,
  "source_url": "https://..."
}
```

- Entradas totais: 2

### 01-introducao/manifest.json

- Estrutura de entrada:

```json
{
  "title": "...",
  "path": "<pasta>/<arquivo>.md",
  "order": 1,
  "source_url": "https://..."
}
```

- Entradas totais: 10

### 02-twig/manifest.json

- Estrutura de entrada:

```json
{
  "title": "...",
  "path": "<pasta>/<arquivo>.md",
  "order": 1,
  "source_url": "https://..."
}
```

- Entradas totais: 9

### 03-api/manifest.json

- Estrutura de entrada:

```json
{
  "title": "...",
  "path": "<pasta>/<arquivo>.md",
  "order": 1,
  "source_url": "https://..."
}
```

- Entradas totais: 10

### 04-store/manifest.json

- Estrutura de entrada:

```json
{
  "title": "...",
  "path": "<pasta>/<arquivo>.md",
  "order": 1,
  "source_url": "https://..."
}
```

- Entradas totais: 41

### 05-html/manifest.json

- Estrutura de entrada:

```json
{
  "title": "...",
  "path": "<pasta>/<arquivo>.md",
  "order": 1,
  "source_url": "https://..."
}
```

- Entradas totais: 5

### 06-paginas/manifest.json

- Estrutura de entrada:

```json
{
  "title": "...",
  "path": "<pasta>/<arquivo>.md",
  "order": 1,
  "source_url": "https://..."
}
```

- Entradas totais: 8

### 07-modelos/manifest.json

- Estrutura de entrada:

```json
{
  "title": "...",
  "path": "<pasta>/<arquivo>.md",
  "order": 1,
  "source_url": "https://..."
}
```

- Entradas totais: 38

### 08-cache/manifest.json

- Estrutura de entrada:

```json
{
  "title": "...",
  "path": "<pasta>/<arquivo>.md",
  "order": 1,
  "source_url": "https://..."
}
```

- Entradas totais: 1

### 09-exemplos/manifest.json

- Estrutura de entrada:

```json
{
  "title": "...",
  "path": "<pasta>/<arquivo>.md",
  "order": 1,
  "source_url": "https://..."
}
```

- Entradas totais: 5

## Diretrizes para populamento dos arquivos

### Arquivos de tópico (`*.md`)

- Manter 1 conceito por arquivo (filosofia IA-first).
- Expandir placeholder para 300-1200 palavras com seções padrão.
- Preservar YAML com campos: `title`, `slug`, `doc_type`, `summary`, `tags`, `related`.
- Usar links internos em `## Veja também` para recuperação multi-hop.

### README.md por pasta

- Descrever escopo da pasta.
- Informar ordem recomendada de leitura.
- Apontar convenções de nomenclatura e metadados.

### manifest.json por pasta

- Atualizar `order` quando arquivos forem adicionados/removidos.
- Manter `source_url` rastreável para cada tópico.
- Evitar entradas duplicadas de `path`.
