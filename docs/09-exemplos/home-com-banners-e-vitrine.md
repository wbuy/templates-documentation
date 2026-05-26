---
title: "Exemplo: Home com banners e vitrine"
slug: "home-com-banners-e-vitrine"
doc_type: "example"
summary: "Modelo de página inicial com banners promocionais e vitrines de produtos."
tags:
  - exemplos
  - home
  - banners
  - vitrine
  - kits
related:
  - 04-store/publicityBanner.md
  - 04-store/showcaseActiveIds.md
  - 04-store/geral-hassmarthint.md
---

## O que faz

Modelo completo de página inicial que apresenta banners promocionais, slogan da loja e vitrines de produtos. Inclui componentes como kits de produtos, produtos visitados, lançamentos e integrações com SmartHint e PerformaAI. Estrutura responsiva com múltiplas seções de destaque.

## Sintaxe

```twig
# HTML
{% set slogan = store.getSlogan() %}
{% set bannerTopo = store.publicityBanner({tipo:'21', limit:'1'}) %}
{% set bannerMainMedium = store.publicityBanner({tipo:'25', limit:'2'}) %}
{% set vitrines = store.showcaseActiveIds() %}

<section id="page_home" class="block">
  {% include('widgets/home-slides.html') %}

  {% if slogan %}
  <!-- SLOGAN -->
  <div id="slogan" class="mb-4">
    <div class="central">
      <p>{{ slogan }}</p>
    </div>
  </div>
  {% endif %}

  {% if geral.hasPerformaAI %}
  <performa></performa>
  {% endif %}

  {{ include('widgets/alertas-destaque.html') }}

  {% if bannerMainMedium|length > 0 %}
  <section class="banner-main-medium block mb-4 px-3 px-md-0">
    <div class="central">
      <div class="row justify-content-center">
        {% for banner in bannerMainMedium %}
    <div class="col text-center">
     {{ banner.raw|raw }}
    </div>
    {% endfor %}
   </div>
  </div>
 </section>
 {% endif %}

 {% if bannerTopo|length >= 1 %}
 <!-- BANNER HEADER -->
 <div class="central">
  <div class="b_header mb-4{{ page == 'principal' ? ' i' : '' }}">
   {{ bannerTopo[0].raw|raw }}
  </div>
 </div>
 {% endif %}

 <section class="block">
  <div class="central">
   <component data-modulo="kits" loading="false" data-shimmer="4"></component>
   {% if vitrines|length >= 1 %}
                {% if global.vitrine_visitados_posicao == '1' %}
     <component data-modulo="produtos-visitados" loading="false" data-shimmer="4"></component>
    {% endif %}
    {% for vitrine in vitrines %}
     <component data-modulo="vitrine" data-id="{{ vitrine.id }}" loading="false" data-shimmer="4"></component>
    {% endfor %}
                {% if global.vitrine_visitados_posicao == '2' %}
     <component data-modulo="produtos-visitados" loading="false" data-shimmer="4"></component>
    {% endif %}
   {% else %}
    <component data-modulo="lancamentos" loading="false" data-shimmer="4"></component>
    {% if geral.hasSmartHint %}
     <div id="smarthint-position-1"></div>
     <div id="smarthint-position-2"></div>
     <div id="smarthint-position-3"></div>
     <div id="smarthint-position-4"></div>
     <div id="smarthint-position-5"></div>
    {% endif %}
   {% endif %}
  </div>

  {{ include('widgets/avaliacoes.html') }}
  {{ include('widgets/marcas.html') }}
  {{ include('widgets/widget-instagram.html') }}
  {{ include('widgets/widget-blog-posts.html') }}
 </section>

 {% if geral.hasSmartHint %}
 <script>
 $(function(){
  SmartHint.Call('setPage',{type:'home', data: {} });
 });
 </script>
 {% endif %}

 {% if geral.hasPerformaAI %}
 <performa></performa>
 {% endif %}
</section>
```

## Quando usar

- Página inicial de loja virtual
- Quando há necessidade de exibir múltiplas promoções
- Com vitrines de produtos ativas no sistema
- Para integração com SmartHint ou PerformaAI

## Exemplo

```scss
.owl-carousel .owl-stage {
  display: flex !important;
  align-items: center !important;
}

#slider {
  width: 100%;
  float: left;
  text-align: center;

  .item {
    width: 100%;
    float: left;

    img {
      width: auto;
      max-width: 100%;
      max-height: 800px;
      display: inline-block;
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
    transition: all 0.25s ease;
    margin-top: 0;
  }

  .owl-prev,
  .owl-next {
    position: absolute;
    top: 0;
    left: 0;
    height: calc(100% - 10px);
    width: 30px;
    background-color: rgba(195, 195, 195, 0.7);
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

#slogan {
  width: 100%;
  float: left;
  background-color: #000;
  color: #fff;
  padding: 5px 0;
  text-align: center;
}

.titulo {
  width: 100%;
  float: left;
  margin: 30px 0 40px 0;
  padding: 10px;
  text-align: center;
  font-size: 30px;
  line-height: 30px;
  font-weight: 100;
  position: relative;

  &::after {
    content: "";
    position: absolute;
    left: 50%;
    top: 100%;
    width: 80px;
    height: 5px;
    background-color: #000;
    margin-left: -40px;
  }
}

#kits {
  .item {
    background: #fff;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
    border-radius: 3px;
    height: 100%;
    max-width: 260px;
    position: relative;
    overflow: hidden;
    display: block;
    margin: auto;
    float: none;

    .foto {
      height: 370px;
      display: flex;
      align-items: center;
      justify-content: center;
      background-color: #eee;

      img {
        max-height: 100%;
      }
    }

    &:hover {
      .det {
        bottom: 0;
      }
    }

    .det {
      width: 100%;
      padding: 10px;
      position: absolute;
      bottom: -250px;
      left: 0;
      background-color: rgba(0, 0, 0, 0.5);

      transition: all 0.25s;

      .t {
        font-size: 18px;
        line-height: 22px;
        margin-bottom: 10px;
        color: #fff;
      }

      .bt-comprar {
        display: inline-block;
        padding: 10px 15px;
        background-color: #53a412;
        color: #fff;
        border-radius: 3px;

        &:active {
          opacity: 0.7;
        }
      }
    }
  }
}

#widget_avaliacoes {
  .itens {
    width: 100%;
    float: left;

    .item {
      width: calc(100% - 6px);
      float: left;
      text-align: center;
      margin: 3px;
      box-shadow: 0 0 3px rgba(0, 0, 0, 0.2);
      background-color: #fff;
      padding: 10px;
      border-radius: 4px;
      height: 100%;

      .votos {
        font-size: 22px;
        margin-bottom: 10px;
        color: #ddd;

        .fa-star {
          color: #ffd700;
        }
      }

      .produto {
        font-size: 14px;
        line-height: 16px;
        margin-bottom: 10px;

        a {
          color: inherit;
          text-decoration: underline !important;
        }
      }

      .comentario {
        margin-bottom: 10px;
      }
    }
  }
}

#marcas {
  .item {
    width: 100%;
    height: 100px;
    overflow: hidden;
    border: solid 1px #f5f5f5;
    display: flex;

    a {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
      height: 100%;
    }

    img {
      max-width: 100%;
      max-height: 100%;
      width: auto;
      height: auto;
    }

    .marca {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100%;
      color: #444;
      font-size: 22px;
      line-height: 24px;
      padding: 10px;
    }
  }
}

#wid_instagram {
  .titulo {
    margin-bottom: 0;
  }
}

.blog-posts {
  background-color: #eee;
  padding: 20px;

  .item {
    height: 100%;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
    overflow: hidden;
    border-radius: 3px;
    transition: all 0.25s;

    .foto {
      height: 195px;
      overflow: hidden;
    }

    .t {
      padding: 10px;
      font-size: 20px;
      line-height: 26px;
      color: #000;
    }

    &:hover {
      background-color: #eee;
    }
  }
}

@media screen and (max-width: 1200px) {
}

@media screen and (max-width: 992px) {
}

@media screen and (max-width: 768px) {
}

@media screen and (max-width: 576px) {
}

@media screen and (max-width: 320px) {
}
```

Saída esperada:

```html
<section id="page_home" class="block">
  <!-- Slides -->
  <!-- Slogam -->
  <!-- Banners principais -->
  <!-- Kits -->
  <!-- Vitrines -->
  <!-- Avaliações, marcas, instagram, blog -->
</section>
```

## Observações

- PerformaAI renderiza dupla inserção (topo e rodapé) para ótimo desempenho
- Posição de "produtos visitados" é configurável via `global.vitrine_visitados_posicao`
- SmartHint requer inicialização com `type:'home'`
- Responsivo: adapta-se para mobile com classes Bootstrap
- Cache: Dados de vitrines podem ser cacheados por tempo configurável

## Erros comuns

### Erro 1: PerformaAI não renderiza

**Problema**: Bloco `<performa></performa>` não aparece
**Diagnóstico**: Verificar se `geral.hasPerformaAI` retorna true
**Solução**: Habilitar PerformaAI nas configurações da loja

### Erro 2: Vitrines não aparecem

**Problema**: Nenhuma vitrine exibida mesmo com dados disponíveis
**Diagnóstico**: `store.showcaseActiveIds()` retorna vazio
**Solução**: Ativar e configurar vitrines no painel de controle

### Erro 3: SmartHint posições não funcionam

**Problema**: `#smarthint-position-N` não carrega conteúdo
**Diagnóstico**: Script não inicializa corretamente
**Solução**: Verificar se SmartHint está habilitado e carregar script antes da inicialização

## Veja também

- [publicityBanner()](04-store/publicityBanner.md) — Recuperar banners promocionais
- [showcaseActiveIds()](04-store/showcaseActiveIds.md) — Vitrines ativas
- [geral.hasPerformaAI](04-store/geral-hasperformaai.md) — Integração PerformaAI
- [geral.hasSmartHint](04-store/geral-hassmarthint.md) — Integração SmartHint
