---
title: "Listeners readListener"
slug: "listeners-readlistener"
doc_type: "reference"
summary: "Sistema de listeners JavaScript que permite recuperar informações da loja em tempo real, atualizando dados quando mudanças ocorrem."
tags:
  - listeners
  - javascript
  - tempo-real
  - eventos
  - carrinho
related:
  - 04-store/cart.md
  - 04-store/visao-geral-store.md
  - 04-store/recursos-gerais.md
---

## O que faz

Os listeners JavaScript (ouvintes) funcionam como um sistema de eventos que permite recuperar informações da loja virtual em tempo real. Quando eventos específicos ocorrem na loja (como adicionar produto ao carrinho), os listeners são acionados, retornando dados atualizados sem necessidade de recarregar a página.

O método principal é `readListener()`, que aguarda mudanças em variáveis ou eventos da loja e executa uma função callback quando o evento ocorre. Isso é essencial para criar interfaces dinâmicas e responsivas que se atualizam instantaneamente.

## Sintaxe

```javascript
readListener('nome_do_evento', function(dados) {
    // código a executar quando evento ocorre
    console.log('Dados recebidos:', dados);
});
```

**Parâmetros:**

- `'nome_do_evento'` (string) — Nome do evento a monitorar
- `função(dados)` — Callback executado quando o evento dispara

## Quando usar

- Atualizar quantidade de itens no carrinho em tempo real
- Ser notificado quando um produto é adicionado/removido do carrinho
- Executar ações customizadas quando mudanças ocorrem na loja
- Atualizar widgets dinâmicos sem recarregar página
- Integrar com sistemas externos que reagem a eventos da loja
- Pré-condição: Deve estar em um arquivo JavaScript do projeto

## Exemplo

```javascript
// Monitorar quantidade de itens no carrinho
readListener('totalItensCarrinho', function(qtd) {
    console.log('A quantidade de itens foi alterada para:', qtd);
    
    // Atualizar elemento HTML
    $('.shop_cart .qtd').text(qtd);
    
    // Atualizar widget do carrinho via AJAX
    $.post('load-widget.php', {widget: 'widgets/carrinho-suspenso.html'}, function(html) {
        $('.shop_cart .drop').html(html);
    });
});

// Notificação quando produto é adicionado
readListener('onAddProductCart', function(fetch) {
    console.log('Produto adicionado ao carrinho!');
    
    // Mostrar notificação visual
    showNotification('Produto adicionado com sucesso!', 'success');
});
```

Saída esperada:

```text
A quantidade de itens foi alterada para: 3
Produto adicionado ao carrinho!
```

## Observações

- Listeners funcionam apenas com JavaScript habilitado no navegador
- Cada listener opera em seu próprio contexto; múltiplos listeners podem monitorar o mesmo evento
- Performance: Listeners não impactam significativamente a performance
- Cache: Não afeta listeners; eventos ocorrem em tempo de execução
- SEO: Não impacta indexação, é execução client-side

## Erros comuns

### Erro 1: Esquecer que readListener retorna dados

**Problema**: Usar `readListener()` pensando que é apenas para efeitos colaterais
**Diagnóstico**: Valores dentro do callback estão undefined
**Solução**: Acessar e usar o parâmetro da função callback

```javascript
// Errado: ignorar dados
readListener('totalItensCarrinho', function() {
    console.log(qtd); // undefined
});

// Correto: acessar parâmetro
readListener('totalItensCarrinho', function(qtd) {
    console.log(qtd); // número de itens
});
```

### Erro 2: Listeners em múltiplas instâncias

**Problema**: Listener definido múltiplas vezes causa eventos duplicados
**Diagnóstico**: Função callback executada várias vezes por um único evento
**Solução**: Usar IIFE ou module pattern para evitar duplicação

### Erro 3: Confundir com eventos DOM

**Problema**: Tentar usar listeners wBuy em elementos HTML normais
**Diagnóstico**: Eventos não disparam
**Solução**: Usar listeners apenas com eventos de loja pré-definidos

## Veja também

- [Cart](04-store/cart.md)
- [Recursos gerais](04-store/recursos-gerais.md)
- [Visão geral store](04-store/visao-geral-store.md)
