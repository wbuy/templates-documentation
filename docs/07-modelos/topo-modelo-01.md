---
title: "Topo - Modelo 01"
slug: "topo-modelo-01"
doc_type: "reference"
summary: "Modelo completo de header/topo com logo, menu navegável, categorias em dropdown, busca com autocomplete, carrinho e login/meus pedidos."
tags: ["topo", "header", "navegação", "menu", "twig"]
related:
  - 07-modelos/carrinho-suspenso.md
  - 04-store/store-categories.md
  - 04-store/store-categoriesmenu.md
---

## O que faz

Este modelo implementa o header (topo) completo da loja com navegação principal. Inclui logo, menu expandível com categorias em múltiplos níveis, busca com autocomplete, carrinho de compras flutuante e área de login/perfil de clientes. Possui suporte total a responsividade com menu mobile em sandwich (hamburguer).

O topo é fixo no topo da página (fixed positioning) com sombra de scroll progressiva, mostrando sempre visível ao usuário mesmo durante navegação.

## Estrutura HTML

```twig
{% set usuario = store.userStore() %}
{% set categorias = store.categories() %}
{% set categorias_menu = store.categoriesMenu() %}

<header class="block">
  <component data-modulo="ofertasperiodicas" loading="false" data-paddingtop="true" data-hidescroll="true"></component>
  <div class="central">
    <div class="mobile-inc"></div>
    <span class="openmenu">
      <i class="fa fa-bars"></i>
      <span class="t">MENU</span>
    </span>
    <h1><a href="./" id="btLogo" style="background-image:url({{ store.getLogo() }});">{{ seo.title }}</a></h1>
    <div class="links">
      <nav>
        <ul>
          {% if global.show_menu_todaloja %}
          <li>
            <a href="todos-produtos/">
              {% if store.showMenuIcons() == '2' %}
              <i class="fa fa-th"></i>
              {% endif %}
              <strong>{{ recursos.categoria_geral_titulo_menu }}</strong>
              <span class="fa fa-angle-down"></span>
            </a>
            {% if categorias|length > 1 %}
            <div class="drop">
              <div class="central">
                <div class="grid">
                  {% for categoria in categorias %}
                  <ul class="list">
                    <li class="t"><a href="{{ categoria.url }}"{{ categoria.cor != '' ? (' style="color:' ~ categoria.cor ~ '"')|raw : '' }}>{{ categoria.nome }}</a></li>
                    {% for level2 in categoria.subs %}
                    <li><a href="{{ level2.url }}"><i class="fa fa-caret-right muted"></i> {{ level2.nome }}</a></li>
                    {% for level3 in level2.subs %}
                    <li class="indent"><a href="{{ level3.url }}">- {{ level3.nome }}</a></li>
                    {% endfor %}
                    {% endfor %}
                  </ul>
                  {% endfor %}
                </div>
              </div>
            </div>
            {% endif %}
          </li>
          {% endif %}

          {% for cat in categorias_menu|slice(0,8) %}
          <li>
            <a href="{{ cat.url }}">
              {{ cat.icone_categoria|raw }}
              <span{{ cat.cor != '' ? (' style="color:' ~ cat.cor ~ '"')|raw : '' }}>{{ cat.nome }}</span>
              {% if cat.subs|length >= 1 %}
              <span class="fa fa-angle-down"></span>
              {% endif %}
            </a>
            {% if cat.subs|length >= 1 %}
            <div class="drop{{  cat.banner != '' ? ' subs' : '' }}">
              <div class="central">
                <div class="grid">
                  {% for level2 in cat.subs %}
                  <ul class="list">
                    <li class="t"><a href="{{ level2.url }}">{{ level2.nome }}</a></li>
                    {% for level3 in level2.subs %}
                    <li><a href="{{ level3.url }}"><i class="fa fa-caret-right muted"></i> {{ level3.nome }}</a></li>
                    {% endfor %}
                  </ul>
                  {% endfor %}
                </div>
                {% if cat.banner != '' %}
                <div class="bnr">
                  {{ cat.banner|raw }}
                </div>
                {% endif %}
              </div>
            </div>
            {% endif %}
          </li>
          {% endfor %}
        </ul>
      </nav>
    </div>

    <div class="pull-right">
      <div class="search">
        <div class="d-none d-md-block">
          <form action="busca/" method="get">
            <input type="text" class="form-control" name="q" data-url="produtos_autocomplete.php" placeholder="Buscar">
            <button type="submit"><i class="fa fa-search"></i></button>
          </form>
          <span class="cover"></span>
          <span class="rm"> &times;</span>
          <span class="cover-all"></span>
        </div>
        <div class="d-block d-md-none">
          <a href="" class="bt-mobile mymodal" data-include="inc.php?meio=modal_search" data-title="Pesquisar"><i class="fa fa-search fa-2x"></i></a>
        </div>
      </div>
      {% if not global.var_mostruario %}
      <div class="dropdown">
        <p><i class="fa fa-user-o"></i> Meus pedidos</p>
        <div class="list">
          {% if not usuario.logged %}
          <a href="login/">Entrar</a>
          {% else %}
          <a href="central/pedidos/">Central de pedidos</a>
          <a href="central/dados/">Meus dados</a>
          <a href="#" id="b-desconectar" class="text-danger">Desconectar</a>
          {% endif %}
        </div>
      </div>
      <div class="shopcart"></div>
      {% elseif global.var_mostruario and not global.var_bloquear_cadastros %}
      <div class="dropdown">
        <p><i class="fa fa-user-o"></i> Central de informações</p>
        <div class="list">
          {% if usuario.logged %}
          <a href="login/">Entrar</a>
          <a href="#" class="mymodal" data-include="inc.php?meio=inc_cadastro" data-width="500" title="Efetuar cadastro">Cadastrar</a>
          {% else %}
          <a href="central/dados/">Meus dados</a>
          <a href="#" id="b-desconectar" class="text-danger">Desconectar</a>
          {% endif %}
        </div>
      </div>
      {% endif %}
    </div>
  </div>
</header>

<script defer>
$(function(){
  $(window).scroll(function(){
    var scr = $(this).scrollTop(),
      w = $(this).width();
    if(scr >= 10 && w > 800)
      !$('header').hasClass('scroll') ? $('header').addClass('scroll') : '';
    else
      $('header').hasClass('scroll') ? $('header').removeClass('scroll') : '';
  });

  {% if not global.var_mostruario %}
  $('.shopcart').load('inc.php?meio=shop_inc');
  {% endif %}
  $('.mobile-inc').load('inc.php?meio=menu_mobile');
});
</script>
```

## CSS/SCSS Principal

```scss
body {
  padding-top: 70px;
}

header {
  position: fixed;
  left: 0;
  top: 0;
  width: 100%;
  z-index: 999;
  background-color: #000;
  color: #FFF;

  &.scroll {
    box-shadow: 0 2px 2px #DDD;
  }

  .links {
    float: left;
    max-width: 640px;
    height: 70px;
    white-space: nowrap;

    ul > li {
      display: inline-block;

      > a {
        float: left;
        font-size: 14px;
        line-height: 68px;
        padding: 0 10px;
        color: #FFF;
        border-bottom: solid 2px #000;
        transition: all .01s ease;

        i.fa {
          margin-right: 5px;
          font-size: 20px;
          vertical-align: middle;
        }
      }

      &:hover > a {
        border-bottom: solid 2px #F60;
      }
    }
  }

  .search {
    width: 190px;
    float: left;
    margin: 15px 10px;
    position: relative;

    input {
      width: calc(100% - 40px);
      float: left;
      background-color: #333;
      color: #FFF;
      padding: 0 15px;
      line-height: 40px;
      height: 40px;
      border: 0;
    }

    button {
      width: 40px;
      height: 40px;
      float: left;
      background-color: #F60;
      color: #FFF;
      font-size: 20px;
    }
  }
}

.drop {
  position: absolute;
  width: 100%;
  max-height: 400px;
  overflow: auto;
  left: 0;
  top: 100%;
  padding: 15px 15px 0 15px;
  background-color: #FFF;
  visibility: hidden;
  opacity: 0;
  transition: all .25s ease;
  box-shadow: 0px 5px 10px rgba(0,0,0,0.2);

  .list {
    width: calc(25% - 10px);
    display: inline-block;
    vertical-align: top;
    margin-bottom: 15px;
    float: left;

    li {
      width: 100%;
      float: left;
      text-indent: 5px;

      &.t {
        text-indent: 0;

        a {
          font-size: 16px;
          line-height: 18px;
          padding: 5px 10px;
          transition: all .25s ease;
          font-weight: bold;

          &:hover {
            text-decoration: none !important;
            background-color: #000;
            color: #FFF;
          }
        }
      }
    }
  }
}
```

## Quando usar

- Para criar o header/topo padrão de uma loja wBuy
- Quando há necessidade de navegação por categorias em múltiplos níveis
- Para implementar busca com autocomplete de produtos
- Quando é preciso exibir carrinho e perfil de cliente no topo

## Observações

- O topo é position: fixed, ocupando sempre a altura 70px
- A classe "scroll" é adicionada quando usuário desce na página (10px), adicionando sombra
- Menu mobile é carregado via include dinâmico em `menu_mobile`
- Carrinho é carregado via include em `shop_inc` (somente se não for vitrine)
- Ofertas periódicas são mostradas em banner acima do topo
- Categoria "Todos os produtos" pode ser controlada via `global.show_menu_todaloja`
- Modo vitrine pode ocultar carrinho e mostrar apenas opção de cadastro
- Ícones de categorias são renderizados como SVG via `cat.icone_categoria|raw`
- Banners de categoria pode aparecer no dropdown

## Erros comuns

### Erro frequente 1
**Problema**: Menu mobile não funciona ou está vazio
**Diagnóstico**: Widget `menu_mobile` não está criado
**Solução**: Criar arquivo widget com nome exatamente `menu_mobile.html` na pasta widgets

### Erro frequente 2
**Problema**: Busca não retorna autocomplete, apenas leva à página de busca
**Diagnóstico**: URL `produtos_autocomplete.php` não está respondendo
**Solução**: Verificar permissão de acesso ao arquivo e que jQuery está carregado

## Veja também

- [07-modelos/carrinho-suspenso.md](../../07-modelos/carrinho-suspenso.md)
- [04-store/store-categories.md](../../04-store/store-categories.md)
- [04-store/store-categoriesmenu.md](../../04-store/store-categoriesmenu.md)

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
