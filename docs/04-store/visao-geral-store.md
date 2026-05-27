---
title: "Visão geral do objeto store"
slug: "visao-geral-store"
doc_type: "concept"
summary: "O objeto store fornece acesso aos dados globais e funcionalidades da loja virtual, incluindo carrinho, categorias, produtos e configurações de apresentação."
tags:
  - store
  - objeto-global
  - dados-loja
  - twig
related:
  - 04-store/recursos-gerais.md
  - 04-store/array-global.md
  - 04-store/detect-ismobile.md
---

## O que faz

O `store` é um objeto global disponível em todos os templates Twig que oferece acesso centralizado aos dados e funcionalidades da loja virtual. Por meio dele, você pode recuperar informações sobre o carrinho de compras, categorias de produtos, dados de clientes, configurações visuais, widgets especiais e muito mais.

Este objeto é essencial para a construção de templates dinâmicos e responsivos, permitindo que você acesse dados em tempo real sem necessidade de chamadas AJAX adicionais para operações básicas. Cada método do `store` retorna dados estruturados prontos para uso nos templates Twig.

## Sintaxe

O `store` é acessado diretamente no Twig sem necessidade de importação. A sintaxe geral segue o padrão:

```twig
{% set dados = store.nomeMetodo() %}
{{ dados.propriedade }}

{# com parâmetros #}
{% set dados = store.nomeMetodo({param: valor}) %}
```

### Retorno

O retorno varia conforme o método chamado e pode ser objeto ou array. Consulte a documentação específica de cada método.

Principais métodos: `cart()`, `blogPosts()`, `categories()`, `getBrands()`, `getStoreData()`, `productDetail()`, `customerProfiles()`, entre muitos outros.

## Quando usar

- Recuperar dados de carrinho ou categorias de produtos
- Exibir informações dinâmicas de perfis de cliente
- Acessar dados de vitrines, banners e ofertas periódicas
- Detectar comportamento do usuário (mobile/desktop)
- Aplicar configurações de apresentação (logos, cores, texto de rodapé)
- Integrar widgets como Instagram, Facebook ou Smart Hint

## Exemplo

```twig
{# Acessar dados do carrinho #}
{% set carrinho = store.cart() %}
<div class="header-cart">
    <span class="qtd">{{ carrinho.total_items }}</span>
    <span class="total">R$ {{ carrinho.cart.amount.total }}</span>
</div>

{# Acessar categorias #}
{% set categorias = store.categories() %}
<ul class="menu-categorias">
    {% for cat in categorias %}
        <li><a href="{{ cat.url }}">{{ cat.nome }}</a></li>
    {% endfor %}
</ul>

{# Detectar dispositivo #}
{% if detect.isMobile() %}
    <link rel="stylesheet" href="mobile.css">
{% endif %}
```

Saída esperada:
```html
<div class="header-cart">
    <span class="qtd">3</span>
    <span class="total">R$ 150.50</span>
</div>
```

## Observações

- Métodos do `store` podem retornar dados em cache, melhorando performance de carregamento
- Alguns métodos aceitam parâmetros opcionais como `limit`, `pagina` para paginação
- Dados sensíveis (como dados de usuário) só retornam quando há sessão ativa
- Mobile-first: use `detect.isMobile()` para renderizar layouts específicos
- A estrutura de retorno varia por método; consulte a documentação específica de cada um

## Erros comuns

### Erro 1: Acessar dados sem verificar existência
**Problema**: Erro ao tentar acessar `carrinho.cart.amount.total` quando o carrinho está vazio
**Diagnóstico**: Verificar se o template trata carrinho vazio com condicional
**Solução**: Sempre usar condicionais antes de acessar propriedades aninhadas
```twig
{% if carrinho.total_items > 0 %}
    <span>{{ carrinho.cart.amount.total }}</span>
{% endif %}
```

### Erro 2: Parâmetros incorretos em métodos
**Problema**: `store.blogPosts({limit: 10})` não retorna posts (deveria ser string)
**Diagnóstico**: Verificar tipo de parâmetro aceito (string vs int)
**Solução**: Passar strings entre aspas: `store.blogPosts({limit: '10'})`

### Erro 3: Dados null em usuário deslogado
**Problema**: `store.customerProfiles()` retorna null quando usuário não está logado
**Diagnóstico**: Verificar se há verificação de autenticação
**Solução**: Envolver em condicional que verifica se usuário está logado

### Erro 4: Usar `store` fora do Twig
**Problema**: Referenciar `store` em JavaScript ou HTML estático.
**Diagnóstico**: Variável indefinida no navegador.
**Solução**: Usar o objeto apenas em templates Twig processados pela plataforma.

## Veja também

- [Recursos gerais](04-store/recursos-gerais.md)
- [Array global](04-store/array-global.md)
- [detect.isMobile()](04-store/detect-ismobile.md)
