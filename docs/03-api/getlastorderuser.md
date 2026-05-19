---
title: "getLastOrderUser"
slug: "getlastorderuser"
doc_type: "reference"
summary: "Função API que recupera o último pedido realizado pelo usuário logado na conta. Ideal para exibir histórico recente, sugestões de compra e informações de entrega do pedido anterior."
tags:
  - api
  - pedidos
  - usuário
  - server-side
  - twig
  - autenticação
related:
  - 03-api/productget.md
  - 03-api/visao-geral-api.md
  - 04-store/customerprofiles.md
---

## O que faz

A função `getLastOrderUser()` busca na API o último pedido realizado pelo usuário logado na conta. Retorna dados completos do pedido como data, valor total, status de entrega, itens comprados e informações de faturamento/envio.

Ideal para renderizar "Meu Último Pedido", sugestões de recompra e informações de acompanhamento de entrega.

## Sintaxe

```twig
{# Sem parâmetros - retorna último pedido do usuário logado #}
{% set ultimopedido = api.getLastOrderUser() %}

{# Retorna array vazio se usuário não tem pedidos #}
{% if ultimopedido %}
  Pedido encontrado
{% else %}
  Nenhum pedido anterior
{% endif %}
```

### Parâmetros

A função **não aceita parâmetros** — retorna sempre o último pedido do usuário logado.

### Retorno

Retorna um **array com dados do pedido** ou **array vazio** se nenhum pedido encontrado. Dados incluem:
- ID do pedido, data, status
- Valor total, desconto, frete
- Itens do pedido (produtos, quantidades, preços)
- Informações de faturamento (endereço, nome)
- Informações de entrega (endereço, rastreamento)
- Status de pagamento

## Quando usar

- Exibir **"Meu Último Pedido"** em dashboard do usuário
- Criar **sugestões de recompra** baseadas no último pedido
- Mostrar **informações de entrega** e **rastreamento**
- Renderizar **reorder buttons** — permitir recomprar mesmos itens
- Quando usuário está **logado e tem histórico de pedidos**

### Pré-condições

- Usuário deve estar **logado na conta** (autenticado)
- Usuário deve ter realizado **pelo menos um pedido** anteriormente
- Pedido deve estar registrado no sistema com dados completos

### Limitações

- Retorna **apenas o último pedido** — não histórico completo
- Funciona **apenas para usuários logados** — retorna vazio se anônimo
- Não permite filtros ou parâmetros — resultado é fixo por usuário
- Para histórico completo, seria necessário AJAX client-side com paginação

## Exemplo

```twig
{# Arquivo: templates/user-dashboard.twig #}
<section class="last-order-section">
  {% set ultimopedido = api.getLastOrderUser() %}
  
  {% if ultimopedido %}
    <div class="last-order-card">
      <h3>Seu Último Pedido</h3>
      
      <div class="order-header">
        <p><strong>Pedido #{{ ultimopedido.id }}</strong></p>
        <p>Data: {{ ultimopedido.created_at|date('d/m/Y') }}</p>
        <p>Status: <span class="badge status-{{ ultimopedido.status }}">{{ ultimopedido.status|capitalize }}</span></p>
      </div>
      
      <div class="order-items">
        <h4>Itens Comprados</h4>
        <ul>
          {% for item in ultimopedido.items %}
            <li>
              {{ item.product_name }} - 
              Qtd: {{ item.quantity }} x 
              R$ {{ item.unit_price|number_format(2, ',', '.') }}
            </li>
          {% endfor %}
        </ul>
      </div>
      
      <div class="order-totals">
        <p>Subtotal: R$ {{ ultimopedido.subtotal|number_format(2, ',', '.') }}</p>
        <p>Frete: R$ {{ ultimopedido.shipping|number_format(2, ',', '.') }}</p>
        <p><strong>Total: R$ {{ ultimopedido.total|number_format(2, ',', '.') }}</strong></p>
      </div>
      
      <div class="order-actions">
        <a href="/pedidos/{{ ultimopedido.id }}" class="btn btn-primary">
          Ver Detalhes
        </a>
        <button class="btn btn-secondary" onclick="reorderItems({{ ultimopedido.id }})">
          Recomprar
        </button>
      </div>
    </div>
  {% else %}
    <div class="no-orders">
      <p>Você ainda não realizou nenhum pedido.</p>
      <a href="/produtos" class="btn btn-primary">Continuar Comprando</a>
    </div>
  {% endif %}
</section>
```

Saída esperada (HTML):
```html
<section class="last-order-section">
  <div class="last-order-card">
    <h3>Seu Último Pedido</h3>
    
    <div class="order-header">
      <p><strong>Pedido #12345</strong></p>
      <p>Data: 15/03/2026</p>
      <p>Status: <span class="badge status-entregue">Entregue</span></p>
    </div>
    
    <div class="order-items">
      <h4>Itens Comprados</h4>
      <ul>
        <li>
          Camiseta Azul - 
          Qtd: 2 x 
          R$ 49,90
        </li>
        <li>
          Calça Jeans - 
          Qtd: 1 x 
          R$ 129,90
        </li>
      </ul>
    </div>
    
    <div class="order-totals">
      <p>Subtotal: R$ 229,70</p>
      <p>Frete: R$ 15,00</p>
      <p><strong>Total: R$ 244,70</strong></p>
    </div>
    
    <div class="order-actions">
      <a href="/pedidos/12345" class="btn btn-primary">
        Ver Detalhes
      </a>
      <button class="btn btn-secondary" onclick="reorderItems(12345)">
        Recomprar
      </button>
    </div>
  </div>
</section>
```

## Observações

### Performance

- `getLastOrderUser()` é **operação leve** — retorna apenas um pedido
- Ideal executar uma única vez e reutilizar em template
- Use **cache de sessão** (tempo de vida da sessão do usuário) ou **cache por usuário** (tempo curto: 5-30 minutos)

### Cache

- Resultado é **candidato para cache session-specific** (cache por usuário logado)
- Invalidar cache quando: novo pedido é criado para o usuário, ou status do pedido muda
- Usar **cache por user_id** se possível — dados diferentes por usuário

### Segurança

- **Retorna apenas dados do próprio usuário logado** — seguro por design
- Nunca retorna dados de outro usuário
- Dados sensíveis (endereço, pagamento) — transmitir via HTTPS apenas

### Impacto SEO e Mobile

- Renderizado **server-side** — não afeta SEO (conteúdo privado do usuário)
- Ótima **user experience** em mobile — acesso rápido ao último pedido
- Reorder buttons em mobile melhor conversão

## Erros comuns

### Erro frequente 1: "Retorna vazio mesmo com pedidos anteriores"
**Problema**: `api.getLastOrderUser()` retorna array vazio mas usuário tem histórico de pedidos.
**Diagnóstico**: Usuário pode estar anônimo/não-logado, ou não tem permissão de acesso aos dados.
**Solução**: 
- Verificar se `{{ app.user }}` ou contexto de usuário está preenchido
- Debugar com `{{ pr(app.user) }}` para confirmar autenticação
- Se autenticado mas ainda vazio, pode não haver pedidos no sistema

### Erro frequente 2: "Itens do pedido não aparecem"
**Problema**: Array de pedido existe mas `ultimopedido.items` está vazio.
**Diagnóstico**: Campo pode ter nome diferente (ex: `order_items`, `products`, etc).
**Solução**: Debugar com `{{ pr(ultimopedido) }}` para ver estrutura exata. Usar nome correto do campo.

### Erro frequente 3: "Data do pedido em formato inválido"
**Problema**: Data renderiza como `2026-03-15 10:30:00` em vez de formato legível.
**Diagnóstico**: Campo data não está sendo formatado.
**Solução**: Usar filtro Twig: `{{ ultimopedido.created_at|date('d/m/Y') }}` para formatar com padrão pt-BR.

## Veja também

- [productGet](./productget.md) — Dados detalhados de produtos
- [Visão geral da API](./visao-geral-api.md) — Contexto e diferenças server-side vs client-side
- [Customer Profiles](../04-store/customerprofiles.md) — Dados completos de usuário logado
