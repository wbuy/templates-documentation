---
title: "Telas customizaveis suportadas"
slug: "telas-customizaveis"
doc_type: "concept"
summary: "Visão geral das telas da plataforma wBuy que suportam customização através de templates"
tags:
  - "telas"
  - "customização"
  - "home"
  - "categorias"
  - "produto"
  - "carrinho"
  - "checkout"
related:
  - 01-introducao/por-onde-comecar.md
  - 01-introducao/wbuy-watcher-npm.md
  - 01-introducao/encoding-iso-8859-1.md
  - 01-introducao/visao-geral.md
  - 02-twig/visao-geral-twig.md
  - 04-store/visao-geral-store.md
---

## O que faz

Direciona os desenvolvedores para uma visão geral das telas da plataforma wBuy que suportam customização através de templates, incluindo a home, categorias, detalhes do produto, busca, vitrines internas dinâmicas e produtos de marca. Este guia ajuda os desenvolvedores a entender quais telas podem ser personalizadas e serve como ponto de partida para explorar os detalhes de cada tela em tópicos subsequentes.

## Sintaxe

Não se aplica. Este documento é um guia conceitual, não possui assinatura ou parâmetros.

## Quando usar

Use este guia quando:

- Você está começando a desenvolver templates para a plataforma wBuy e quer entender quais telas suportam customização.
- Você quer ter uma visão geral das possibilidades de customização de telas na plataforma wBuy antes de mergulhar nos detalhes de cada tela.
- Você está planejando a estrutura do seu template e quer saber quais telas você pode personalizar para criar uma experiência única para os usuários.
- Você quer explorar as diferentes telas disponíveis para customização e entender como elas se encaixam na arquitetura geral de templates da plataforma wBuy, para tomar decisões informadas sobre quais telas personalizar com base nas necessidades do seu projeto.

## Exemplo

A seguir, um exemplo de como as telas customizáveis podem ser organizadas em um projeto de template para a plataforma wBuy:

```md
my-template/
├── assets/
│   └── ...
├── estruturas/   
│   ├── bottom
│   │   ├── footer02.html
│   │   ├── footer03.html
│   │   ├── rodape.css
│   │   ├── rodape.html
│   │   └── rodape.min.css
│   ├── center
│   │   ├── categories-dynamic.css
│   │   ├── categories-dynamic.html
│   │   ├── categories-dynamic.min.css
│   │   ├── categories.css
│   │   ├── categories.html
│   │   ├── categories.min.css
│   │   ├── center.css
│   │   ├── center.html
│   │   ├── center.min.css
│   │   ├── home2.html
│   │   ├── home2.min.css
│   │   ├── home3.html
│   │   ├── pagina_filial.css
│   │   ├── pagina_filial.html
│   │   ├── pagina_filial.min.css
│   │   ├── product_brand.css
│   │   ├── product_brand.html
│   │   ├── product_brand.min.css
│   │   ├── product_detail.css
│   │   ├── product_detail.html
│   │   ├── product_detail.min.css
│   │   ├── product_search.css
│   │   ├── product_search.html
│   │   ├── product_search.min.css
│   │   ├── vitrine-cliente.html
│   │   ├── vitrine_personalizada.css
│   │   ├── vitrine_personalizada.html
│   │   └── vitrine_personalizada.min.css
│   └── top
│       ├── checkout.html
│       ├── topo1.css
│       ├── topo1.html
│       ├── topo1.min.css
│       ├── topo2.css
│       ├── topo2.html
│       ├── topo2.min.css
│       ├── topo3.css
│       ├── topo3.html
│       ├── topo3.min.css
│       ├── topo4.css
│       ├── topo4.html
│       ├── topo4.min.css
│       ├── topo5.css
│       ├── topo5.html
│       ├── topo5.min.css
│       ├── topo6.css
│       ├── topo6.html
│       ├── topo6.min.css
│       ├── topo7.css
│       ├── topo7.html
│       ├── topo7.min.css
│       ├── topo8.css
│       ├── topo8.html
│       ├── topo8.min.css
│       ├── topo9.css
│       ├── topo9.html
│       └── topo9.min.css
├── widgets/
│   └── ...
├── paginas/
│   └── ...
└── ...
```

## Observações

- As telas customizáveis são organizadas dentro do diretório `estruturas/`, com subdiretórios para `center`, `bottom` e `top`, cada um contendo arquivos HTML, CSS e minificados para as diferentes telas que podem ser personalizadas.
- A personalização de telas permite que os desenvolvedores criem experiências únicas para os usuários, adaptando a aparência e funcionalidade de cada tela de acordo com as necessidades do projeto.
- A plataforma wBuy suporta uma variedade de telas customizáveis, incluindo a home, categorias, detalhes do produto, busca, vitrines internas dinâmicas e produtos de marca, oferecendo ampla flexibilidade para os desenvolvedores criarem templates personalizados e envolventes.

## Erros comuns

- Tentar personalizar telas que não são suportadas pela plataforma wBuy, o que pode resultar em erros de renderização ou comportamento inesperado.
- Não seguir a estrutura de arquivos recomendada para as telas customizáveis, o que pode dificultar a manutenção e organização do projeto de template.
- Esquecer de incluir os arquivos CSS e JavaScript necessários para as telas customizáveis, o que pode levar a problemas de estilo e funcionalidade nas telas personalizadas.
- Não testar as telas customizáveis em diferentes dispositivos e navegadores, o que pode resultar em problemas de compatibilidade e experiência do usuário inconsistente.

## Veja também

- [Por onde começar](01-introducao/por-onde-comecar.md)
- [wBuy Watcher NPM](01-introducao/wbuy-watcher-npm.md)
- [Encoding ISO-8859-1](01-introducao/encoding-iso9-1.md)
- [Visão geral](01-introducao/visao-geral.md)
- [Visão geral do Twig](02-twig/visao-geral-twig.md)
- [Visão geral do Store](04-store/visao-geral-store.md)
