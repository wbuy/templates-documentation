---
title: "Carrinho Suspenso"
slug: "carrinho-suspenso"
doc_type: "reference"
summary: "Implementação de carrinho suspenso (dropdown modal) que aparece quando produtos são adicionados ao carrinho ou via acionamento de evento."
tags: ["carrinho", "modal", "widget", "twig", "javascript"]
related:
  - 04-store/cart.md
  - 04-store/listeners-readlistener.md
  - 07-modelos/topo-modelo-01.md
---

## O que faz

O carrinho suspenso é um widget flutuante que exibe o resumo do carrinho de compras do cliente. É acionado quando um produto é adicionado ao carrinho ou pode ser aberto manualmente. Ele mostra a lista de itens, subtotal, descontos e total, além de botões para continuar comprando ou finalizar a compra.

O componente utiliza listeners para atualizar automaticamente quando itens são adicionados ao carrinho, mantendo a interface sincronizada com o estado do carrinho em tempo real.

## Implementação

O carrinho suspenso é implementado em três partes:

### 1. HTML no Topo (Header)

Insira o seguinte código no HTML do seu modelo de topo:

```twig
{% if global.var_carrinho_suspenso %}
<div class="suspended-cart">
  <div class="cover"></div>
  <div class="drop_new"></div>
</div>
{% endif %}

<script>
  $(function(){
    loadSuspendedCartTheme();

    readListener('totalItensCarrinho', function(){
      loadSuspendedCartTheme();
    });

    readListener('onAddProductCart', function(){
      openSuspendedCartTheme();
    });
  });

  function openSuspendedCartTheme(){
    $('.suspended-cart').addClass('open');
    $('body').css({'overflow': 'hidden'});
  }

  function loadSuspendedCartTheme(){
    $.post('load-widget.php', {widget:'widgets/new-suspended-cart.html'}, function(d){
      $('.suspended-cart .drop_new').html(d);
    });
  }
</script>
```

### 2. CSS/SCSS

Adicione os estilos na aba de CSS/SCSS:

```scss
.suspended-cart {
  position: fixed;
  z-index: 9999999999;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  visibility: hidden;

  &.open {
    visibility: visible;

    .cover {
      visibility: visible;
      opacity: 1;
    }

    .drop_new {
      right: 0;
    }
  }

  .cover {
    background-color: rgba(0,0,0,0.7);
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    visibility: hidden;
    opacity: 0;
    transition: all .25s;
  }

  .drop_new {
    position: fixed;
    top: 0;
    right: -500px;
    width: 100%;
    max-width: 500px;
    height: 100%;
    background-color: #FFF;
    z-index: 2;
    transition: all .25s;

    .drop-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px;
      border-bottom: solid 1px #DDD;

      h3 {
        font-size: 20px;
        font-weight: bold;
      }

      .fechar {
        width: 35px;
        height: 35px;
        border: solid 1px #DDD;
        border-radius: 3px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 14px;
        cursor: pointer;
      }
    }

    .msg-empty {
      padding: 30px;
      font-size: 23px;
      line-height: 26px;
      text-align: center;
    }

    .drop-list {
      height: calc(100% - 290px);
      overflow: auto;

      .item {
        padding: 20px;

        .foto {
          width: 100px;
          display: inline-block;
          margin-right: 20px;
          vertical-align: top;
        }

        .det {
          width: calc(100% - 130px);
          display: inline-block;
          vertical-align: top;
          position: relative;

          .produto {
            width: calc(100% - 30px);
            display: inline-block;
          }

          .valores {
            margin-top: 10px;
            display: flex;
            justify-content: space-between;
          }

          .item-delete {
            width: 25px;
            height: 25px;
            position: absolute;
            top: 0;
            right: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            border: solid 1px #DDD;
            border-radius: 3px;
          }
        }
      }
    }

    .drop-footer {
      padding: 20px;

      .item {
        display: flex;
        justify-content: space-between;
        padding: 5px 0;
      }

      .botoes {
        display: flex;
        justify-content: space-between;
        padding-top: 15px;
        margin-top: 10px;
        border-top: solid 1px #DDD;
        text-align: center;
        line-height: 15px;

        a {
          margin-left: 10px;
          border: solid 1px #666;
          color: #000;
          font-size: 12px;
          width: 50%;
          display: flex;
          justify-content: center;
          align-items: center;
          height: 60px;
          padding: 5px;

          &:active {
            opacity: 0.7;
          }

          &:first-child {
            margin-left: 0;
          }

          &.bt-finalizar {
            background-color: #666;
            color: #FFF;
          }
        }
      }
    }
  }
}
```

### 3. Widget Template

Crie um novo widget com o nome exato `new-suspended-cart`. Insira o seguinte HTML:

```twig
{% set carrinho = store.cart() %}
{% set valores = carrinho.cart.amount %}
{% set valor_carrinho_str = valores.total %}

<div class="drop-header">
  <h3>CARRINHO CUSTOMIZADO</h3>
  <span class="fechar"> &times;</span>
</div>

{% if carrinho.total_items == 0 %}
<div class="msg-empty">
  <p><strong>Seu carrinho está vazio</strong>, que tal adicionar um produto?</p>
</div>
{% else %}

<div class="drop-list">
  {% for item in carrinho.cart.items %}
  <div class="item" data-sku="{{ item.sku }}">
    <div class="foto">
      <img src="{{ item.foto }}" alt="{{ item.produto }}" class="img-fluid" />
    </div>
    <div class="det">
      <h3 class="produto mb-2"><strong>{{ item.produto }}</strong></h3>
      {% if item.prazo_entrega > 0 %}
      {{ item.prazo_entrega_raw }}
      {% endif %}
      {% if item.cor or item.variacao %}
      {{ item.cor_raw }}
      {{ item.variacao_raw }}
      {% endif %}
      <p class="valores">
        <span>{{ item.quantidade }}x R${{ item.valor_unitario|valor }}</span>
        <span class="text-right"><strong>R${{ item.valor_parcial|valor }}</strong></span>
      </p>
      <span class="item-delete text-danger"><i class="fa fa-trash"></i></span>
    </div>
  </div>
  {% endfor %}
</div>
<div class="drop-footer">
  <p class="item">
    <span>Subtotal</span>
    <span class="text-right">R${{ valores.subtotal|valor }}</span>
  </p>
  <p class="item">
    <span>Desconto</span>
    <span class="text-right">R${{ valores.discount|valor }}</span>
  </p>
  <p class="item">
    <span><strong>Total</strong></span>
    <span class="text-right"><strong>R${{ valores.total|valor }}</strong></span>
  </p>
  <div class="botoes">
    <a href="#" class="bt-continuar fechar">CONTINUAR COMPRANDO</a>
    <a href="carrinho/" class="bt-finalizar">FINALIZAR COMPRA</a>
  </div>
</div>
{% endif %}

<script>
  $(function(){
    $('header .cart .sup').html('{{ carrinho.total_items }}');
    $('header .cart-total .cart-total-label').html('R${{ valores.total|valor }}');
  });
</script>
```

## Quando usar

- Quando a loja deseja feedback imediato ao adicionar produtos ao carrinho
- Para melhorar a experiência de compra sem sair da página atual
- Quando há necessidade de visualizar resumo do carrinho sem navegar

## Observações

- O carrinho suspenso depende da variável global `global.var_carrinho_suspenso` estar ativa nas configurações
- Usa listeners via `readListener()` para atualização em tempo real
- O z-index alto (9999999999) garante visibilidade acima de outros elementos
- A animação de transição utiliza `transition: all .25s` para suavidade
- O overlay (cover) bloqueia cliques em elementos de fundo quando o carrinho está aberto

## Erros comuns

### Erro frequente 1

**Problema**: Carrinho suspenso não abre quando produto é adicionado
**Diagnóstico**: Evento `onAddProductCart` não dispara ou variável global não está ativa
**Solução**: Verificar em Configurações da Loja que a opção "Carrinho suspenso" está habilitada

### Erro frequente 2

**Problema**: Widget `new-suspended-cart` não carrega conteúdo
**Diagnóstico**: Função `loadSuspendedCartTheme()` retorna página em branco
**Solução**: Verificar nome exato do widget (deve ser `new-suspended-cart.html`) e que está na pasta widgets

## Veja também

- [04-store/cart.md](../../04-store/cart.md)
- [04-store/listeners-readlistener.md](../../04-store/listeners-readlistener.md)
- [07-modelos/topo-modelo-01.md](../../07-modelos/topo-modelo-01.md)
