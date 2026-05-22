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
```
Carrossel de marcas com logos e links
```

## Retorno dos dados

**items** - Array com dados das marcas
- `items[x].id` (int) - ID da marca
- `items[x].marca` (string) - Nome da marca
- `items[x].marca_url` (string) - Link para página de produtos da marca
- `items[x].logo` (string) - URL da logo
- `items[x].total_produtos` (int) - Total de produtos cadastrados

**showOnHomePage** - Boolean indicando se permite mostrar o módulo na página inicial

## Parâmetros de consulta

| Parâmetro | Padrão | Descrição |
|-----------|---------|-------------|
| destaque | '' | 1 = Apenas destaque; 0 = Não destaque; '' (vazio) = Todos |

## Observações

- Retorna dados das marcas cadastradas na loja virtual
- Permite filtrar por destaque (marcas em foco)
- É ideal para criar vitrine de marcas
- As marcas devem ter logo configurada para melhor apresentação

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
