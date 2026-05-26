---
title: "Exemplo: Carrinho suspenso assíncrono"
slug: "carrinho-suspenso-assincrono"
doc_type: "example"
summary: "Modelo de carrinho suspenso com carregamento assíncrono de itens em painel lateral."
tags:
  - exemplos
  - carrinho
  - widget
  - assíncrono
  - javascript
related:
  - 04-store/cart.md
  - 04-store/listeners-readlistener.md
  - 04-store/visao-geral-store.md
---

## O que faz

Modelo de exemplo para implementação de carrinho suspenso com carregamento assíncrono via AJAX. O painel lateral é acionado quando o usuário adiciona produtos ao carrinho, exibindo lista de itens, cálculos de valores (subtotal, desconto, total) e opções de ação (continuar comprando ou finalizar compra).

## Sintaxe

### HTML (no Topo)

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

### CSS/SCSS (estilos principais)

```scss
.suspended-cart{
    position: fixed;
    z-index: 9999999999;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    visibility: hidden;

    &.open{
        visibility: visible;

        .cover{
            visibility: visible;
            opacity: 1;
        }

        .drop_new{
            right: 0;
        }
    }

    .cover{
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

    .drop_new{
        position: fixed;
        top: 0;
        right: -500px;
        width: 100%;
        max-width: 500px;
        height: 100%;
        background-color: #FFF;
        z-index: 2;
        transition: all .25s;

        .drop-header{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px;
            border-bottom: solid 1px #DDD;

            h3{
                font-size: 20px;
                font-weight: bold;
            }

            .fechar{
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

        .msg-empty{
            padding: 30px;
            font-size: 23px;
            line-height: 26px;
            text-align: center;
        }

        .drop-list{
            height: calc(100% - 290px);
            overflow: auto;

            .item{
                padding: 20px;

                .foto{
                    width: 100px;
                    display: inline-block;
                    margin-right: 20px;
                    vertical-align: top;
                }

                .det{
                    width: calc(100% - 130px);
                    display: inline-block;
                    vertical-align: top;
                    position: relative;

                    .produto{
                        width: calc(100% - 30px);
                        display: inline-block;
                    }

                    .valores{
                        margin-top: 10px;
                        display: flex;
                        justify-content: space-between;
                    }

                    .item-delete{
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

        .drop-footer{
            padding: 20px;

            .item{
                display: flex;
                justify-content: space-between;
                padding: 5px 0;
            }

            .botoes{
                display: flex;
                justify-content: space-between;
                padding-top: 15px;
                margin-top: 10px;
                border-top: solid 1px #DDD;
                text-align: center;
                line-height: 15px;

                a{
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

                    &:active{
                        opacity: 0.7;
                    }

                    &:first-child{
                        margin-left: 0;
                    }

                    &.bt-finalizar{
                        background-color: #666;
                        color: #FFF;
                    }
                }
            }
        }
    }
}
```

### Widget new-suspended-cart.html

```twig
# HTML
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

- Quando há necessidade de carrinho rápido e acessível
- Para melhorar experiência do usuário ao adicionar produtos
- Em lojas com múltiplas categorias de produtos
- Para visualização rápida de totais antes de checkout

## Exemplo

O exemplo completo acima implementa um carrinho suspenso completo. Resumidamente:

1. Ativa-se quando `global.var_carrinho_suspenso` é true
2. Carrega via AJAX ao adicionar produto
3. Exibe overlay semi-transparente
4. Painel desliza da direita com animação CSS
5. Lista itens com opções de remover
6. Exibe cálculos de subtotal, desconto e total
7. Oferece botões para continuar comprando ou finalizar

Saída esperada:

```html
<div class="suspended-cart open">
  <div class="cover" style="visibility: visible; opacity: 1;"></div>
  <div class="drop_new" style="right: 0;">
    <div class="drop-header">
      <h3>CARRINHO CUSTOMIZADO</h3>
      <span class="fechar">&times;</span>
    </div>
    <div class="drop-list"><!-- itens --></div>
    <div class="drop-footer"><!-- totais e botões --></div>
  </div>
</div>
```

## Observações

- Carregamento assíncrono via `$.post()` jQuery
- Listeners automáticos para atualização: `totalItensCarrinho` e `onAddProductCart`
- Animação suave com CSS transitions (0.25s)
- Overlay escuro com opacity 0.7
- Painel padrão 500px de largura (ajustável)
- Scroll automático na lista de itens
- Mobile: Funciona em largura 100%, máximo 500px
- Performance: Carregamento sob demanda, sem impacto inicial

## Erros comuns

### Erro 1: Widget não carrega

**Problema**: Painel abre mas fica vazio ou com erro
**Diagnóstico**: Arquivo `widgets/new-suspended-cart.html` não encontrado
**Solução**: Criar widget com nome exato e colocar no caminho correto

### Erro 2: Carrinho não abre ao adicionar produto

**Problema**: `onAddProductCart` não é disparado
**Diagnóstico**: Sistema de listeners não inicializado
**Solução**: Verificar se `readListener()` está disponível no escopo global

### Erro 3: Itens duplicam ao atualizar

**Problema**: Ao adicionar novos itens, os anteriores duplicam
**Diagnóstico**: `$.post()` não limpa antes de renderizar
**Solução**: Adicionar `.empty()` ou `.html('')` antes de inserir novo conteúdo

### Erro 4: Fechar painel não funciona

**Problema**: Clique em "x" ou "continuar comprando" não fecha
**Diagnóstico**: Event handler não conectado corretamente
**Solução**: Adicionar handler para `.fechar` com `.off('click').on('click'...)`

## Veja também

- [store.cart()](04-store/cart.md) — Dados do carrinho
- [readListener()](04-store/listeners-readlistener.md) — Sistema de listeners
- [Painel suspenso tutorial](06-paginas/carrinho-suspenso.md) — Guia passo a passo
