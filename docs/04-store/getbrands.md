---
title: "getBrands"
slug: "getbrands"
doc_type: "reference"
summary: "Método que retorna as marcas cadastradas na loja virtual com logos e informações para exibição em carrosséis ou listagens."
tags:
  - store
  - marcas
  - brands
  - produtos
related:
  - 04-store/visao-geral-store.md
  - 04-store/producttobox.md
---

## O que faz

Disponibiliza como retorno as marcas cadastradas na loja virtual. Este método recupera todas as marcas configuradas e permite exibi-las em diversos formatos, como carrosséis ou listas.

## Sintaxe

```twig
{% set marcas = store.getBrands() %}
{# com parâmetro #}
{% set marcas = store.getBrands({destaque: '1'}) %}
```

### Retorno

```json
{
  "items": [
    {
      "id": 0,
      "marca": "",
      "marca_url": "",
      "logo": "",
      "total_produtos": 0
    }
  ],
  "showOnHomePage": false
}
```

## Quando usar

- Para exibir marcas cadastradas da loja
- Em seções de destaque na página inicial
- Em carrosséis ou galerias de marcas
- Para filtrar apenas marcas de destaque

## Exemplo

```twig
{% set marcas = store.getBrands() %}
{% if marcas.items|length > 0 %}
<section id="marcas" class="block mb-3">
    <div class="central">
        <div class="itens owl-carousel owl-theme px-3">
            {% for marca in marcas.items %}
            <div class="item text-center bg-white p-2">
                <a href="{{ marca.marca_url }}">
                    {% if marca.logo %}
                    <img src="{{ marca.logo }}" alt="{{ marca.marca }}" />
                    {% else %}
                    <h6 class="marca">{{ marca.marca }}</h6>
                    {% endif %}
                </a>
            </div>
            {% endfor %}
        </div>
    </div>
</section>
{% endif %}
```

Saída esperada:

```text
Carrossel de marcas com logos e links
```

## Observações

- Retorna dados das marcas cadastradas na loja virtual
- Permite filtrar por destaque (marcas em foco)
- É ideal para criar vitrine de marcas
- As marcas devem ter logo configurada para melhor apresentação

## Erros comuns

### Erro 1: Iterar sem validar `marcas.items`

**Problema**: Loop em lista vazia gera seção sem conteúdo.
**Diagnóstico**: Carrossel aparece vazio.
**Solução**: Verificar `if marcas.items|length > 0` antes de renderizar.

### Erro 2: Assumir que todas as marcas têm logo

**Problema**: Imagens quebradas quando a marca não tem logo.
**Diagnóstico**: `<img>` sem `src` válido.
**Solução**: Usar fallback de texto quando `marca.logo` estiver vazio.

### Erro 3: Usar `destaque` com tipo incorreto

**Problema**: Filtro não é aplicado e retorna todas as marcas.
**Diagnóstico**: Parâmetro passado como número ou boolean.
**Solução**: Enviar `destaque` como string (`'1'`, `'0'` ou `''`).

## Veja também

- [Visão geral store](04-store/visao-geral-store.md)
- [Product To Box](04-store/producttobox.md)
