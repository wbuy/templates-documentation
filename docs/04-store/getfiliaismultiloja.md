---
title: "getFiliaisMultiloja()"
slug: "getfiliaismultiloja"
doc_type: "reference"
summary: "[MULTILOJA] Retorna filiais cadastradas na matriz com possibilidade de filtro por categorias."
tags:
  - store
  - multiloja
  - filiais
  - matriz
  - categorias
related:
  - 04-store/visao-geral-store.md
  - 04-store/store-categories.md
---

## O que faz

Método disponível apenas em lojas do tipo matriz (multiloja). Retorna lista de filiais cadastradas com informações como nome, cidade, estado, logo e URL interna. Suporta filtros por categoria para exibir apenas filiais que vendem determinados produtos.

## Sintaxe

```twig
{% set filiais = store.getFiliaisMultiloja() %}
{% set filiais = store.getFiliaisMultiloja({cid:'123', sid:'456'}) %}
```

Parâmetros:

- `cid` - ID da categoria principal (nível 1)
- `sid` - ID da subcategoria (nível 2)
- `order` - Ordenacao dos resultados (possiveis: 'nome,asc', 'random'); padrão: 'nome,asc'

### Retorno

```json
[
  {
    "nome": "",
    "cidade": "",
    "uf": "",
    "url_interna_matriz": "",
    "logo": ""
  }
]
```

## Quando usar

- Exibir carrossel de fornecedores/filiais
- Criar seletor de loja
- Listar parceiros

## Exemplo

```twig
{% set filiais = store.getFiliaisMultiloja() %}
{% for filial in filiais %}
  <img src="{{ filial.logo }}" alt="{{ filial.nome }}">
  <a href="{{ filial.url_interna_matriz }}">{{ filial.nome }}</a>
{% endfor %}
```

## Observações

- Apenas em ambientes multiloja
- Suporta filtros por categoria

## Erros comuns

### Erro 1: Usar em loja simples

**Problema**: Método não existe
**Solução**: Verificar se é multiloja

### Erro 2: Parâmetros inválidos

**Solução**: Usar IDs corretos

## Veja também

- [Visão geral store](04-store/visao-geral-store.md)
- [Store Categories](04-store/store-categories.md)
