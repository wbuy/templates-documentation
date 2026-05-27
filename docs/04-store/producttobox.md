---
title: "productToBox"
slug: "producttobox"
doc_type: "reference"
summary: "Método que retorna array estruturado de produtos prontos para exibição em boxes com suporte a múltiplas ordenações."
tags:
  - store
  - produtos
  - array
  - galeria
related:
  - 04-store/visao-geral-store.md
  - 04-store/productboxdefault.md
  - 04-store/pageproducts.md
---

## O que faz

Retorna um array estruturado de produtos prontos para serem exibidos em caixas/boxes. Este método recupera dados formatados de produtos para uso em listagens, buscas e vitrines, sendo a base para construção de galerias de produtos.

## Sintaxe

```twig
{% set produtosBox = store.productToBox() %}
{# com parâmetros #}
{% set produtosBox = store.productToBox({limit: '4', order: 'random'}) %}
```

### Retorno

```json
{
  "total": 0, // Total de produtos retornados na consulta
  "data": [
    {
      "id": 0,
      "cod": "", // Código do produto
      "produto": "",
      "produto_url": "",
      "isPromo": false,
      "data_promo": "YYYY-MM-DD", // Validade final da promoção
      "valor_original": 0.0,
      "valor_venda": 0.0,
      "valor_venda_boleto": 0.0,
      "porcentagem_desconto": 0.0,
      "quantidade_minima": 0, // Quantidade mínima para venda
      "venda": true, // Se disponível para venda
      "frete_gratis": false,
      "marca": {
        "id": 0,
        "nome": "",
        "url": ""
      },
      "categoria_level1": {
        "id": 0,
        "nome": "",
        "url": "",
        "tabela": 0
      },
      "categoria_level2": {
        "id": 0,
        "nome": "",
        "url": ""
      },
      "categoria_level3": {
        "id": 0,
        "nome": "",
        "url": ""
      },
      "produto_online": true,
      "url_relative": "",
      "url_sku": "",
      "valores": {
        "varejo_apartir": true,
        "atacado": 0.0
      },
      "cores": [
        {
          "id": 0,
          "nome": "",
          "primaria": "#hex",
          "secundaria": "#hex",
          "img": "",
          "ativo": "",
          "posicao": "",
          "estoque": "",
          "foto": {
            "cor_id": 0,
            "codigo": "",
            "foto": "",
            "foto_mini": "",
            "legenda": "",
            "oculto": "",
            "video": ""
          }
        }
      ],
      "variacoes": [
        {
          "id": 0,
          "variacao_id": 0,
          "nome": "",
          "valor": "",
          "posicao": 0,
          "ativo": true
        }
      ],
      "fotos": [
        {
          "cor_id": 0,
          "codigo": "",
          "foto": "",
          "foto_mini": "",
          "legenda": "",
          "oculto": "",
          "video": ""
        }
      ],
      "quantidade_total_em_estoque": 0,
      "esgotado": false,
      "parcelamento": "", // raw - Matriz com informações do parcelamento do produto com base no valor e nos gateways ativos
      "parcelamento_list": {
        "tipo": "",
        "boleto": false, // Se true, este gateway está configurado para receber por boleto
        "parcelas": 0, // Quantidade de parcelas possíveis para pagamento
        "valor_parcela": 0.0, // Valor de cada parcela
        "has_juros": false, // Se true, o valor_parcela está calculado com juros
        "perc_desconto": 0.0 // Percentual de desconto quando existente
      },
      "grade_tipo": 0,
      "campos_adicionais": {
        "title": "",
        "valores": ""
      }
    }
  ]
}
```

## Quando usar

- Para exibir galeria de produtos de forma padronizada
- Em listagens de produtos com filtros
- Para criar vitrines de destaque
- Com store.productBoxDefault() para renderizar caixas formatadas

## Exemplo

```twig
{% set produtosBox = store.productToBox({limit:'4', order:'lancamento'}) %}
<div class="row">
  {% for produto in produtosBox.data %}
  <div class="col-md-3">
    {{ store.productBoxDefault(produto) }}
  </div>
  {% endfor %}
</div>
```

Saída esperada:

```text
Galeria de 4 produtos últimos lançamentos com informações completas
```

## Retorno dos dados

**data** - Array de produtos com estrutura completa

- `data[x].id` (int) - ID do produto
- `data[x].titulo` (string) - Título/nome
- `data[x].url` (string) - URL do produto
- `data[x].foto` (string) - URL da imagem principal
- `data[x].preco` (float) - Preço do produto
- `data[x].preco_desconto` (float) - Preço com desconto
- `data[x].descricao` (string) - Descrição breve
- E demais propriedades de produto

**total** - Total de produtos encontrados

## Parâmetros de consulta

| Parâmetro | Padrão | Descrição |
|-----------|---------|-------------|
| limit | 12 | Quantidade de produtos a retornar |
| order | valor-asc | Ordem (valor-asc, valor-desc, random, lancamento) |
| cid | '' | ID da categoria nível 1 |
| sid | '' | ID da categoria nível 2 |

## Observações

- Retorna dados estruturados prontos para rendering
- É usado frequentemente com store.productBoxDefault()
- Suporta múltiplas ordenações
- Performance otimizada para grandes listas

### Erro frequente 2

**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
