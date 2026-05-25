---
title: "Widget de Banners Principais (Slides da Página Inicial)"
slug: "widget-de-banners-principais-slides-da-pagina-inicial"
doc_type: "reference"
summary: "Carrossel de banners principais (slides) da página inicial controlados via Painel > Marketing > Banners principais (slide)."
tags: ["widget", "banners", "carousel", "slides", "twig"]
related:
  - 07-modelos/pagina-inicial-modelo-01.md
  - 04-store/mainbanner.md
---

## O que faz

Este widget implementa um carrossel de banners principais (slides) que aparecem no topo da página inicial. Os banners são gerenciados pelo lojista via Painel > Marketing > Banners principais (slide) e suportam imagens diferentes para desktop e mobile.

O widget utiliza a biblioteca Owl Carousel para transição suave entre slides, com navegação manual via setas e pontos indicadores que aparecem ao passar o mouse.

## Estrutura HTML

```twig
{% set slides = store.mainBanner() %}
{% if slides.raw|length >= 1 %}
<div class="{{ slides.width == 'block' ? 'block' : 'central' }}{{ slogan == '' ? ' mb-0' : '' }}">
  <div id="slider" class="mb-0 owl-carousel owl-theme">
    {% for slide in slides.items %}
    <div class="item">
      <div class="{{ slide.foto_mobile == '' ? 'block' : 'd-none d-md-block' }}">
        {{ slide.desktop_raw|raw }}
      </div>
      {% if slide.foto_mobile %}
      <div class="d-block d-md-none">
        {{ slide.mobile_raw|raw }}
      </div>
      {% endif %}
    </div>
    {% endfor %}
  </div>
</div>
{% endif %}
```

## Explicação do Código

| Parte | Descrição |
| ------- | ---------- |
| `store.mainBanner()` | Função que retorna array de banners configurados no painel |
| `slides.width` | Controla se banner é full-width ("block") ou centralizado ("central") |
| `slides.raw\|length` | Verifica se há banners antes de renderizar |
| `owl-carousel` | Classe que ativa o carrossel da biblioteca Owl Carousel |
| `slide.desktop_raw` | HTML do banner para desktop (imagem ou link) |
| `slide.mobile_raw` | HTML do banner para mobile (imagem ou link) |
| `d-none d-md-block` | Classes Bootstrap para ocultar em mobile, mostrar em desktop |
| `d-block d-md-none` | Classes Bootstrap para mostrar em mobile, ocultar em desktop |

## CSS/SCSS

```scss
#slider {
  width: 100%;
  float: left;
  text-align: center;

  .item {
    width: 100%;
    float: left;

    img {
      max-height: 800px;
    }
  }

  .owl-dots {
    position: absolute;
    width: 100%;
    margin: 0;
    bottom: 0;
    visibility: hidden;
    opacity: 0;
  }

  .owl-nav {
    visibility: hidden;
    opacity: 0;
    transition: all .25s ease;
    margin-top: 0;
  }

  .owl-prev,
  .owl-next {
    position: absolute;
    top: 0;
    left: 0;
    height: calc(100% - 10px);
    width: 30px;
    background-color: rgba(195,195,195,0.70);
    color: #000;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .owl-next {
    left: auto;
    right: 0;
  }

  .owl-pagination {
    line-height: normal;
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
  }

  &:hover .owl-nav,
  &:hover .owl-dots {
    visibility: visible;
    opacity: 1;
  }
}
```

## Funcionalidades

| Feature | Descrição |
| ------- | ---------- |
| **Responsividade** | Imagens diferentes para desktop e mobile via `foto_mobile` |
| **Navegação** | Setas (owl-prev/owl-next) para navegar manualmente |
| **Indicadores** | Pontos na base (owl-dots) mostram quantos slides existem |
| **Auto-play** | Carrossel pode fazer scroll automático (configurável na biblioteca) |
| **Hover Effects** | Setas e pontos aparecem ao passar o mouse sobre o slider |
| **Full Width** | Pode expandir para full-width (block) ou centralizado (central) |

## Quando usar

- Ao implementar página inicial com destaque em banners promocionais
- Para exibir promoções sazonais em carrossel
- Quando há múltiplos banners a mostrar em sequência
- Para direcionar tráfego a categorias ou produtos específicos

## Observações

- Requer biblioteca **Owl Carousel** carregada no template
- Suporta imagens e links clicáveis via HTML bruto (`_raw` no Twig)
- Máximo de altura de imagem é 800px (pode ser customizado via CSS)
- Setas aparecem com opacidade 70% cinza e aparecem ao hover
- O widget só renderiza se houver banners cadastrados
- Desktop e mobile podem ter imagens diferentes para otimização
- A classe `mb-0` remove margem inferior se não houver slogan

## Erros comuns

### Erro frequente 1

**Problema**: Carrossel não funciona, setas não aparecem
**Diagnóstico**: Biblioteca Owl Carousel não foi carregada
**Solução**: Verificar que a biblioteca Owl Carousel JS e CSS estão incluídas no template global

### Erro frequente 2

**Problema**: Banner mobile não aparece em telas pequenas
**Diagnóstico**: Campo `foto_mobile` está vazio no banner cadastrado
**Solução**: Ao criar banner no painel, preencher tanto desktop quanto mobile para melhor responsividade

## Veja também

- [07-modelos/pagina-inicial-modelo-01.md](../../07-modelos/pagina-inicial-modelo-01.md)
- [04-store/mainbanner.md](../../04-store/mainbanner.md)
