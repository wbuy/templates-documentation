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

Retorna um **array com dados do pedido** ou **array vazio** se nenhum pedido encontrado.

> Para estrutura JSON completa e atualizada com todos os campos, consulte a [API Postman](https://documenter.getpostman.com/view/4141833/RWTsquyN?version=latest).

#### Estrutura do Retorno

**Campos Principais do Pedido:**

| Campo | Tipo | Descrição |
| ------- | ------ | ----------- |
| `id` | int | ID único do pedido |
| `identificacao` | string | Código identificador do pedido (ex: "XK9MBR2ZT7CVQ3") |
| `data` | string | Data/hora do pedido (formato: "YYYY-MM-DD HH:MM:SS") |
| `status.id` | int | ID do status (ex: 3 = "Pagamento aprovado") |
| `status.nome` | string | Nome legível do status |

**Objeto Cliente:**

| Campo | Tipo | Descrição |
| ------- | ------ | ----------- |
| `cliente.id` | int | ID único do cliente |
| `cliente.nome` | string | Nome completo |
| `cliente.email` | string | Email principal |
| `cliente.telefone1` | string | Telefone principal |
| `cliente.doc1` | string | CPF ou CNPJ |
| `cliente.cep` | string | CEP de entrega |
| `cliente.endereco` | string | Logradouro |
| `cliente.bairro` | string | Bairro |
| `cliente.cidade` | string | Cidade |
| `cliente.uf` | string | Estado (UF) |

**Objeto Valores:**

| Campo | Tipo | Descrição |
| ------- |------ | ----------- |
| `valor_total.subtotal` | float | Soma dos produtos sem desconto |
| `valor_total.desconto` | float | Valor do desconto/cupom |
| `valor_total.frete` | float | Valor do frete |
| `valor_total.acrescimo` | float | Acréscimos (ex: gift pack) |
| `valor_total.total` | float | Total final do pedido |

**Objeto Frete:**

| Campo | Tipo | Descrição |
| ------- | ------ | ----------- |
| `frete.valor` | float | Valor do frete |
| `frete.prazo` | int | Prazo em dias |
| `frete.estimativa` | string | Data estimada de entrega |
| `frete.nome` | string | Nome da transportadora (ex: "PAC", "SEDEX") |
| `frete.rastreio` | string | Código de rastreio |
| `frete.rastreio_url` | string | URL para rastrear |

**Array Produtos:**

Cada produto em `produtos[]` contém:

| Campo | Tipo | Descrição |
| ------- | ------ | ----------- |
| `produto_id` | int | ID do produto |
| `sku` | string | SKU do produto |
| `produto` | string | Nome do produto |
| `qtd` | int | Quantidade |
| `valor` | float | Valor unitário (com desconto se houver) |
| `cor` | string | Cor selecionada |
| `variacaoValor` | string | Tamanho ou outra variação |

**Objeto Pagamento:**

| Campo | Tipo | Descrição |
| ------- | ------ | ----------- |
| `pagamento.servico` | string | Forma de pagamento (ex: "Mercado Pago") |
| `pagamento.tipo` | string | Tipo (ex: "CARTAO_CREDITO") |
| `pagamento.parcelas` | int | Número de parcelas |
| `pagamento.confirmed` | string | Data de confirmação |
| `pagamento.info.card.brand` | string | Bandeira do cartão |
| `pagamento.info.card.last_digits` | string | Últimos 4 dígitos |

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
{# Arquivo: templates/user-last-order.twig #}
{% set pedido = api.getLastOrderUser() %}

{% if pedido %}
  <section class="last-order">
    <h2>Seu Último Pedido</h2>
    
    <div class="order-info">
      <p><strong>Pedido #{{ pedido.identificacao }}</strong></p>
      <p>Data: {{ pedido.data|date('d/m/Y') }}</p>
      <p>Status: <span class="badge status-{{ pedido.status.id }}">
        {{ pedido.status.nome }}
      </span></p>
    </div>
    
    <div class="order-items">
      <h3>Produtos</h3>
      {% for produto in pedido.produtos %}
        <div class="item">
          <strong>{{ produto.produto }}</strong> 
          ({{ produto.cor }}, {{ produto.variacaoValor }})
          <br>
          Qtd: {{ produto.qtd }} × R$ {{ produto.valor|number_format(2, ',', '.') }}
        </div>
      {% endfor %}
    </div>
    
    <div class="order-totals">
      <p>Subtotal: R$ {{ pedido.valor_total.subtotal|number_format(2, ',', '.') }}</p>
      <p>Desconto: -R$ {{ pedido.valor_total.desconto|number_format(2, ',', '.') }}</p>
      <p>Frete: R$ {{ pedido.frete.valor|number_format(2, ',', '.') }}</p>
      <p><strong>Total: R$ {{ pedido.valor_total.total|number_format(2, ',', '.') }}</strong></p>
    </div>
    
    {% if pedido.frete.rastreio %}
      <div class="tracking">
        <h3>Rastreamento</h3>
        <p>Código: <a href="{{ pedido.frete.rastreio_url }}" target="_blank">
          {{ pedido.frete.rastreio }}
        </a></p>
        <p>Estimativa: {{ pedido.frete.estimativa|date('d/m/Y') }}</p>
      </div>
    {% endif %}
    
    <button onclick="reorderItems({{ pedido.id }})">Recomprar Estes Itens</button>
  </section>
{% else %}
  <div class="no-orders">
    <p>Você ainda não realizou nenhum pedido.</p>
    <a href="/produtos" class="btn">Continuar Comprando</a>
  </div>
{% endif %}
```

Saída esperada (HTML):

```html
<section class="last-order">
  <h2>Seu Último Pedido</h2>
  
  <div class="order-info">
    <p><strong>Pedido #XK9MBR2ZT7CVQ3</strong></p>
    <p>Data: 15/04/2026</p>
    <p>Status: <span class="badge status-3">Pagamento aprovado</span></p>
  </div>
  
  <div class="order-items">
    <h3>Produtos</h3>
    <div class="item">
      <strong>camiseta masculina slim fit</strong> (preto, M)
      <br>
      Qtd: 3 × R$ 89,90
    </div>
  </div>
  
  <div class="order-totals">
    <p>Subtotal: R$ 269,70</p>
    <p>Desconto: -R$ 15,00</p>
    <p>Frete: R$ 18,90</p>
    <p><strong>Total: R$ 273,60</strong></p>
  </div>
  
  <div class="tracking">
    <h3>Rastreamento</h3>
    <p>Código: <a href="https://melhorrastreio.com.br/..." target="_blank">
      BR123456789BR
    </a></p>
    <p>Estimativa: 20/04/2026</p>
  </div>
  
  <button onclick="reorderItems(98732051)">Recomprar Estes Itens</button>
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

## Campos principais vs. completos

A resposta da API é extensa. Para a maioria dos casos de uso, você precisará de apenas estes campos:

**Essenciais (sempre usar):**
- `id`, `identificacao` — Identificar o pedido
- `data`, `status.nome` — Informação de status
- `cliente.nome`, `cliente.email` — Dados do cliente
- `produtos[]` — Itens do pedido
- `valor_total.total` — Valor final
- `frete.rastreio`, `frete.rastreio_url` — Rastreamento

**Comuns (geralmente úteis):**
- `valor_total.desconto`, `valor_total.subtotal`, `valor_total.frete`
- `cliente.telefone1`, `cliente.endereco`, `cliente.cidade`
- `pagamento.tipo`, `pagamento.parcelas`, `pagamento.confirmed`
- `frete.estimativa`, `frete.prazo`

**Avançados (casos específicos):**
- `cupom.cupom`, `cupom.valor` — Para recompra com mesmo cupom
- `pagamento.info.card.*` — Dados do cartão (cuidado: PCI compliance)
- `historico[]` — Timeline de mudanças de status
- `observacoes_internas` — Notas internas (acesso restrito)

> Use `{{ pr(pedido) }}` para debugar e ver todos os campos disponíveis na resposta.

## Erros comuns

### Erro frequente 1: "Retorna vazio mesmo com pedidos anteriores"

**Problema**: `api.getLastOrderUser()` retorna array vazio mas usuário tem histórico de pedidos no sistema.
**Diagnóstico**: Usuário pode estar anônimo/não-logado, ou não tem permissão de acesso aos dados.
**Solução**: 
- Verificar se usuário está autenticado com `{{ app.user }}`
- Debugar com `{{ pr(app.user) }}` para confirmar login
- Se autenticado mas ainda vazio, pode não haver pedidos ou dados corrompidos

### Erro frequente 2: "Campos de cliente/frete retornam undefined"

**Problema**: Tentando acessar `pedido.cliente.telefone1` ou `pedido.frete.rastreio` gera undefined.
**Diagnóstico**: Campos podem estar vazios, nulos ou ausentes na resposta.
**Solução**: 
```twig
{# Sempre validar antes de acessar #}
{% if pedido.cliente and pedido.cliente.telefone1 %}
  Telefone: {{ pedido.cliente.telefone1 }}
{% endif %}
```

### Erro frequente 3: "Data em formato inválido ou incorreta"

**Problema**: Campo `data` renderiza como `2026-04-15 09:32:10` em vez de formato legível.
**Diagnóstico**: Data não está sendo formatada com filtro Twig.
**Solução**: Usar filtro de data: `{{ pedido.data|date('d/m/Y') }}` ou `{{ pedido.data|date('d/m/Y H:i') }}`.

### Erro frequente 4: "Array produtos vazio"

**Problema**: Pedido existe mas `pedido.produtos` está vazio ou não renderiza itens.
**Diagnóstico**: Pode haver pedidos sem SKU vinculado ou dados inconsistentes.
**Solução**: Validar com `{% if pedido.produtos %}` e debugar com `{{ pr(pedido.produtos) }}` para ver estrutura real.

## Veja também

- [productGet](./productget.md) — Dados detalhados de produtos
- [Visão geral da API](./visao-geral-api.md) — Contexto e diferenças server-side vs client-side
- [Customer Profiles](../04-store/customerprofiles.md) — Dados completos de usuário logado
