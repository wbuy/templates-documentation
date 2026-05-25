---
title: "Detalhes do produto"
slug: "detalhes-do-produto"
doc_type: "reference"
summary: "Página responsável por exibir detalhes do produto e permitir sua adição ao carrinho com opções de personalização HTML."
tags: ["pagina", "produto", "detalhes", "dinamico", "include"]
related: ["04-store/store-productdetail.md", "04-store/getcommentsproduct.md", "05-html/html-productdetailsku.md"]
---

## O que faz

A página de detalhes do produto é responsável por mostrar as informações completas do produto e permitir sua adição ao carrinho. Existem duas opções para implementar a seção dinâmica:

1. **Modelo dinâmico padrão wBuy**: Carrega automaticamente o conteúdo dinâmico sem possibilidade de personalização do HTML
2. **Modelo dinâmico personalizado**: Permite adicionar blocos customizados seguindo regras pré-estabelecidas

## Sintaxe

### Obtendo informações do produto

```twig
{% set produto = store.productDetail(productId) %}
```

O parâmetro `productId` é obrigatório. Para obter o ID da rota (URL), utilize `extra.id`:

```twig
{% set produto = store.productDetail(extra.id) %}
```

### Opção 1 - Modelo dinâmico padrão

```twig
{{ dynamic_include|raw }}
```

### Opção 2 - Modelo dinâmico personalizado

```twig
{% set sku = extra.sku ? extra.sku : produto.sku %}
<div id="inc_sku">
    {{ include('caminho-do-seu-widget.html') }}
</div>
```

## Quando usar

- Use a opção 1 (modelo dinâmico padrão) quando desejar rapidez na implementação sem customização avançada
- Use a opção 2 (modelo dinâmico personalizado) quando precisar de maior controle sobre o HTML e funcionalidades
- Inclua comentários do produto quando desejar mostrar avaliações
- Inclua compartilhamento social quando a estratégia de marketing incluir redes sociais
- Use TrustVox quando a loja estiver integrada com essa solução

## Exemplo

### Exemplo básico com conteúdo dinâmico padrão

```twig
{% set produto = store.productDetail(extra.id) %}
<h1>{{ produto.nome }}</h1>
<p>{{ produto.descricao }}</p>
{{ dynamic_include|raw }}
```

### Exemplo com comentários

```twig
{{ include('includes/product_comments.html') }}
```

### Exemplo com compartilhamento

```twig
<div class="row">
    <div class="col">
        <p class="text-muted mb-1">Compartilhe</p>
        {{ include('includes/share.html') }}
    </div>
</div>
```

### Exemplo com produtos curtidos

```twig
{% set session = store.getSession() %}

{% if extra.id not in session.curtidos %}
<a href="" class="btn btn-light curtir">
    <i class="fa fa-fw fa-heart-o text-danger"></i> Curtir
</a>
{% else %}
<span class="btn btn-light disabled">
    <i class="fa fa-fw fa-heart text-success"></i> Curtiu!
</span>
{% endif %}
```

## Observações

- O parâmetro `productId` é obrigatório para consultar dados do produto
- O widget personalizado deve seguir as instruções e parâmetros descritos em [html.productDetailSKU(sku, extra.id)](https://doc-templates.wbuy.com.br/post/html-productdetailsku)
- O conteúdo padrão do `product_comments.html` pode ser alterado criando um novo widget e referenciando-o
- A variável `session` fornece acesso aos produtos curtidos na sessão atual
- Avaliações TrustVox (quando disponível) podem ser incluídas usando as tags apropriadas
- Todas as variáveis disponíveis através de `store.productDetail()` podem ser consultadas na documentação da função

## Erros comuns

### Erro: Conteúdo dinâmico não aparece

**Problema**: O `dynamic_include|raw` não mostra preço, quantidade ou botão de adicionar ao carrinho
**Diagnóstico**: Pode haver conflito na div #inc_sku ou falha na inicialização do JavaScript
**Solução**: Certifique-se de que a div existe, está vazia antes do include, e o JavaScript do widget está sendo executado

### Erro: Comentários não aparecem

**Problema**: O include de `product_comments.html` não mostra avaliações
**Diagnóstico**: O método `store.getCommentsProduct()` pode não estar retornando dados
**Solução**: Verifique se o produto possui comentários ativos no painel de controle e use `pr(store.getCommentsProduct(extra.id))` para debugar

### Erro: Session de curtidos não funciona

**Problema**: A verificação `extra.id not in session.curtidos` sempre retorna true
**Diagnóstico**: A sessão pode não estar corretamente inicializada
**Solução**: Use `pr(store.getSession())` para verificar a estrutura dos dados disponíveis

## Veja também

- [04-store/store-productdetail.md](04-store/store-productdetail.md) - Variáveis completas disponíveis
- [04-store/getcommentsproduct.md](04-store/getcommentsproduct.md) - Método para obter comentários
- [05-html/html-productdetailsku.md](05-html/html-productdetailsku.md) - Widget de detalhes personalizado
