---
title: "Cache - Recursos gerais"
slug: "cache-recursos-gerais"
doc_type: "reference"
summary: "Configuração de temas para compatibilidade com estratégias de cache da plataforma wBuy, incluindo carregamento assíncrono de dados de usuário e carrinho."
tags:
  - cache
  - async
  - carrinho
  - usuário
  - performance
related:
  - 01-introducao/visao-geral.md
  - 04-store/cart.md
  - 04-store/userstore.md
---

## O que faz

A plataforma wBuy implementa cache automático para otimizar performance: 1 minuto para subdomínios de teste (.wbuy.com.br) e 5 minutos para domínios finais. Para que seu tema funcione corretamente com essa estratégia, é essencial que dados sensíveis do usuário logado e do carrinho sejam carregados de forma assíncrona via JavaScript, nunca fixados diretamente no HTML. Isso garante que cada visitante receba dados atualizados mesmo quando a página está cacheada.

## Sintaxe

As chamadas assíncronas utilizam jQuery POST para recuperar dados:

```javascript
// Estrutura geral de chamada assíncrona
$.post('action.php', {funcao: 'nomeFunc'}, function(d){
    // Manipular resposta d
}, 'json');

$.post('load-widget.php', {widget: 'caminho/widget.html'}, function(d){
    // Inserir widget na página
});
```

## Quando usar

**Use este padrão quando:**

- Necessitar exibir informações do usuário logado no topo/header
- Precisar mostrar totalizadores do carrinho (quantidade, valor)
- Quiser implementar carrinho suspenso ou funcionalidades dependentes de estado do usuário
- Seu tema será publicado em modo mostruário (showcase apenas)
- Precisar suportar domínios finais com cache de 5 minutos

**Estrutura HTML recomendada:**

```html
<!-- Elementos que receberão dados via JavaScript -->
<div class="login load-action-login">
  <a href="central/">
    <i class="ri-user-3-line"></i>
  </a>
</div>

<div class="fav">
  <a href="central/favoritos/" aria-label="Favoritos">
    <i class="ri-heart-line"></i>
  </a>
</div>

<div class="shopcart{{ global.var_carrinho_suspenso ? ' suspended' : '' }}">
  <a href="carrinho/" class="cart">
    <i class="ri-shopping-cart-line"></i>
    <span class="cart-header-total-items">0</span>
    <span class="cart-header-total-amount">R$0,00</span>
  </a>
</div>
```

## Exemplo

**Carregar dados do usuário logado:**

```javascript
$.post('action.php', {funcao:'userdata'}, function(d){
    let html = '';
    if(d.logged !== '1'){
        // Usuário não logado
        html = '<a href="login/"><i class="ri-user-line"></i><p>olá, faça seu login<br>ou cadastre-se</p></a>';
    }else{
        // Usuário logado - usar primeiro_nome
        html = '<a href="central/"><i class="ri-user-line"></i><p>olá, '+d.data.primeiro_nome+'<br><strong>minha conta</strong></p></a>';
    }
    $('.load-action-login').html(html);
}, 'json');
```

**Carrinho suspenso (quando habilitado):**

Use Twig para renderizar o container:

```twig
{% if global.var_carrinho_suspenso %}
    <div class="suspended-cart">
        <div class="cover"></div>
        <div class="content"></div>
    </div>
{% endif %}
```

Depois preencha via JavaScript:

```javascript
$.post('load-widget.php', {widget:'widgets/suspended-cart.html'}, function(d){
    $('.suspended-cart .content').html(d);
});
```

## Observações

- **Tempo de cache:** Subdomínios .wbuy.com.br = 1 minuto; domínios finais = 5 minutos
- **Dados obrigatórios assíncronos:** Informações de usuário logado, totalizadores de carrinho, estado de favoritos
- **Nomes de classes:** Os seletores `.load-action-login`, `.load-mostruario-login`, `.cart-header-total-items`, etc., são **opcionais**. Você pode renomeá-los conforme seu design
- **Modo mostruário:** Quando `var_mostruario` está ativo, a loja funciona apenas como vitrine; ajuste a lógica JavaScript conforme necessário

## Erros comuns

### Erro 1: Fixar dados do usuário diretamente no HTML

**Problema**: Renderizar `{{ user.nome }}` ou `{{ global.usuario.primeiro_nome }}` diretamente no Twig resulta em dados cacheados
**Diagnóstico**: Dados do usuário não atualizam ou aparecem incorretos quando múltiplos visitantes acessam a loja
**Solução**: Use sempre `$.post('action.php', {funcao:'userdata'}, ...)` e preencha via JavaScript após carregar

### Erro 2: Não validar estado mostruário

**Problema**: Exibir botões "Comprar" ou formulários de carrinho mesmo quando `var_mostruario` é true
**Diagnóstico**: Modo showcase mostra opções de compra, causando confusão no cliente
**Solução**: Sempre validar com `{% if not var_mostruario %}` ou `if(var_mostruario)` em JavaScript antes de renderizar elementos de venda

### Erro 3: Esquecer classe CSS `.suspended` no carrinho

**Problema**: Não adicionar `.suspended` quando carrinho suspenso está habilitado
**Diagnóstico**: Carrinho suspenso ativado pelo lojista, mas layout do header não se adapta
**Solução**: Use `{{ global.var_carrinho_suspenso ? ' suspended' : '' }}` na classe do div do carrinho

### Erro 4: Chamar APIs backend diretamente

**Problema**: Tentar fazer requisições diretas sem passar por `action.php`
**Diagnóstico**: Erros de CORS, respostas não formatadas ou ausência de dados
**Solução**: Sempre use `$.post('action.php', ...)` para garantir resposta formatada pelo sistema

## Veja também

- [Visão geral - Fundamentos de temas](01-introducao/visao-geral.md)
- [Carrinho - Store global](04-store/cart.md)
- [Dados do usuário - Store global](04-store/userstore.md)
