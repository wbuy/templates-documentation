---
title: "getRatings"
slug: "getratings"
doc_type: "reference"
summary: "Recupera as avaliações e depoimentos de clientes sobre a loja ou produtos específicos."
tags:
  - avaliações
  - ratings
  - depoimentos
  - clientes
related:
  - 04-store/getstoredata.md
  - 04-store/getcommentsproduct.md
---

## O que faz

O método `getRatings` é utilizado para buscar depoimentos e avaliações deixadas pelos clientes. Ele pode retornar tanto avaliações gerais da loja quanto avaliações focadas em produtos, dependendo do contexto e dos parâmetros.

Estas avaliações incluem o nome do cliente, a nota (geralmente de 1 a 5), o comentário e a data da avaliação, permitindo exibir "provas sociais" para aumentar a confiança dos novos visitantes.

## Sintaxe

```twig
{% set ratings = store.getRatings() %}

{% for rating in ratings %}
  <div class="rating-item">
    <span>{{ rating.cliente_nome }}</span>
    <span>Nota: {{ rating.nota }}</span>
    <p>{{ rating.mensagem }}</p>
  </div>
{% endfor %}
```

### Retorno

```json
{
  "items": [
    {
      "id": 0,
      "pid": 0,
      "nome": "",
      "email": "",
      "comentario": "",
      "data": "YYYY-MM-DD HH:MM:SS",
      "ip": "",
      "voto": 0.0,
      "produto": "",
      "produto_url": ""
    }
  ],
  "raw": ""
}
```

## Quando usar

- Exibir depoimentos de clientes na página inicial (Home).
- Criar uma página dedicada a "O que nossos clientes dizem".
- Mostrar a média de satisfação da loja no rodapé.

## Exemplo

```twig
<div class="testemunhos">
  {% for item in store.getRatings() %}
    <div class="box-depoimento">
      <strong>{{ item.cliente_nome }}</strong>
      <div class="estrelas">Nota: {{ item.nota }}</div>
      <p>"{{ item.mensagem }}"</p>
      <small>{{ item.data_formatada }}</small>
    </div>
  {% endfor %}
</div>
```

Saída esperada:
```html
<div class="testemunhos">
  <div class="box-depoimento">
    <strong>João Silva</strong>
    <div class="estrelas">Nota: 5</div>
    <p>"Excelente atendimento e entrega super rápida!"</p>
    <small>15/05/2023</small>
  </div>
</div>
```

## Observações

- Apenas avaliações aprovadas no painel administrativo são exibidas.
- A quantidade de avaliações retornadas pode ser limitada por configurações globais.
- Para avaliações de um produto específico na página de detalhes, verifique se há um método específico no objeto `product`.

## Erros comuns

### Erro 1: Não tratar notas vazias ou zero
**Problema**: Exibir 0 estrelas para um cliente que não atribuiu nota (se permitido).
**Solução**: Validar se a nota existe antes de renderizar as estrelas.

### Erro 2: Layout quebrado com mensagens longas
**Problema**: Clientes escrevendo textos muito grandes que quebram o design.
**Solução**: Usar filtros como `truncate` ou CSS para limitar a exibição do texto.

## Veja também

- [Informações da loja](04-store/getstoredata.md)
- [Página de produto](04-store/store-productdetail.md)
