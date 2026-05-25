---
title: "Página Inicial - Modelo 01"
slug: "pagina-inicial-modelo-01"
doc_type: "reference"
summary: "Modelo completo de página inicial com slogan, banners, vitrines de produtos, avaliações, marcas e integração com widgets dinâmicos."
tags: ["página-inicial", "modelo", "twig", "vitrines", "banners"]
related:
  - 07-modelos/widget-de-banners-principais-slides-da-pagina-inicial.md
  - 07-modelos/variaveis-css-geral.md
  - 04-store/store-gettexttop.md
---

## O que faz

Este é o modelo completo da página inicial (home) da loja. Estrutura a exibição de elementos principais como slogan, banners principais em carrossel, kits/looks, vitrines de produtos cadastradas, avaliações de clientes, marcas e posts do blog.

Utiliza componentes dinâmicos que carregam dados de marketing (banners, promoções) e integrações opcionais como SmartHint e Performa AI, criando uma página visualmente rica e interativa.

O modelo é responsivo e adequado tanto para desktop quanto para dispositivos móveis, com suporte a shimmer loading e lazy loading.

## Estrutura HTML

```twig
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

## Componentes Principais

| Componente | Função | Variável de Controle |
|-----------|--------|--------------------|
| home-slides.html | Carrossel de banners principais | N/A |
| Slogan | Texto de boas-vindas | `store.getSlogan()` |
| Alertas Destaque | Avisos e promoções | widgets/alertas-destaque.html |
| Banners Medium | Banners secundários de marketing | `store.publicityBanner({tipo:'25'})` |
| Banner Header | Banner principal grande | `store.publicityBanner({tipo:'21'})` |
| Kits/Looks | Componente de kits de produtos | data-modulo="kits" |
| Vitrines | Vitrines de produtos cadastradas | `store.showcaseActiveIds()` |
| Avaliações | Widget de avaliações de clientes | widgets/avaliacoes.html |
| Marcas | Widget de marcas | widgets/marcas.html |
| Instagram | Widget de posts do Instagram | widgets/widget-instagram.html |
| Blog Posts | Widget de posts do blog | widgets/widget-blog-posts.html |

## CSS Principal

```scss
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

  .owl-dots,
  .owl-nav {
    visibility: hidden;
    opacity: 0;
    transition: all .25s ease;
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
  color: #FFF;
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
```

## Quando usar

- Para criar a página inicial de uma loja wBuy
- Quando se deseja exibir produtos destacados, vitrines e promoções
- Para implementar integração com SmartHint ou Performa AI
- Quando há necessidade de múltiplas vitrines dinâmicas

## Observações

- O modelo utiliza componentes dinâmicos que carregam via AJAX
- O `data-shimmer` permite exibição de skeleton loading (esqueleto de carregamento)
- SmartHint posições (1-5) servem para inserção de recomendações personalizadas
- Performa AI pode ser ativado/desativado via `geral.hasPerformaAI`
- Produtos visitados podem aparecer em posição configurável (antes ou depois das vitrines)
- Responsive design com breakpoints em 1200px, 992px, 768px e 576px

## Erros comuns

### Erro frequente 1

**Problema**: Vitrines vazias ou não carregam produtos
**Diagnóstico**: Componente `vitrine` com data-id não retorna dados
**Solução**: Verificar se a vitrine foi criada em Painel > Marketing > Vitrines personalizadas

### Erro frequente 2

**Problema**: SmartHint ou Performa AI não aparecem mesmo com ativação
**Diagnóstico**: Scripts de integração não carregam ou JS das bibliotecas não foi incluído
**Solução**: Verificar que os scripts são carregados globalmente e que a ativação está correta

## Veja também

- [07-modelos/widget-de-banners-principais-slides-da-pagina-inicial.md](../../07-modelos/widget-de-banners-principais-slides-da-pagina-inicial.md)
- [07-modelos/variaveis-css-geral.md](../../07-modelos/variaveis-css-geral.md)
- [04-store/store-gettexttop.md](../../04-store/store-gettexttop.md)
