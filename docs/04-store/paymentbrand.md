---
title: "paymentBrand"
slug: "paymentbrand"
doc_type: "reference"
summary: "Método que retorna bandeiras e gateways de pagamento disponíveis na loja com suporte a ícones em múltiplos formatos."
tags:
  - store
  - pagamento
  - bandeiras
  - checkout
related:
  - 04-store/visao-geral-store.md
  - 04-store/cart.md
---

## O que faz

Disponibiliza como retorno as bandeiras de pagamento disponíveis na loja virtual. Este método retorna dados de gateways de pagamento configurados e as bandeiras (Visa, Mastercard, etc) associadas a cada um.

## Sintaxe

```twig
{% set pagamentos = store.paymentBrand() %}
{# com parâmetros #}
{% set pagamentos = store.paymentBrand({mono: false, replaceMonoUnavailable: true}) %}
```

## Quando usar

- Para exibir bandeiras de pagamento na loja
- Em checkout para indicar formas de pagamento aceitas
- Em páginas de confiança/segurança
- Quando precisa de ícones de pagamento em branco ou colorido

## Exemplo

```twig
{% set pagamentos = store.paymentBrand() %}
<div class="brands">
	{% for brand in pagamentos.brand %}
	<span><img src="{{ brand.icone }}" alt="{{ brand.nome }}" /></span>
    {% endfor %}
</div>
```

Saída esperada:
```
Ícones de bandeiras de pagamento exibidos
```

## Retorno dos dados

**gateway** - Array com todas as marcas de pagamento configuradas (Mercado Pago, PagSeguro, Pagar.me...)
- `gateway[x].nome` (string) - Nome do gateway
- `gateway[x].icone` (string) - URL do ícone

**brand** - Array com todas as bandeiras de pagamento disponíveis
- `brand[x].nome` (string) - Nome da bandeira (Mastercard, Visa...)
- `brand[x].brand` (string) - Tipo/código da bandeira
- `brand[x].icone` (string) - URL do ícone da bandeira

## Parâmetros de consulta

| Parâmetro | Padrão | Descrição |
|-----------|---------|-------------|
| mono | false | Quando true, busca imagens brancas com fundo transparente |
| replaceMonoUnavailable | true | Quando false e mono true, não faz troca para imagem colorida se mono não existir |

## Observações

- Retorna gateways configurados na loja virtual
- Suporta versão mono (branco/transparente) dos ícones quando disponível
- É útil para resgatar confiança do cliente ao mostrar formas de pagamento aceitas
- Os ícones já vém prontos para exibição

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
