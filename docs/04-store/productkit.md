---
title: "productKit"
slug: "productkit"
doc_type: "reference"
summary: "Método que retorna Kits/Looks de produtos criados para promoções e coleções especiais com múltiplos formatos de exibição."
tags:
  - store
  - produtos
  - kits
  - looks
related:
  - 04-store/visao-geral-store.md
  - 04-store/producttobox.md
---

## O que faz

Disponibiliza como retorno os Kits de Produtos criados na loja virtual. Kits são agrupamentos de produtos oferecidos como promoções ou coleções especiais.

## Sintaxe

```twig
{% set kits = store.productKit() %}
{# com parâmetro #}
{% set kits = store.productKit({limit: '10'}) %}
```

### Retorno

```json
{
  "config": {
    "show_menu": false,
    "show_principal": false,
    "formato": 0,
    "total": 0,
    "url": "",
    "url_kit": "",
    "name": "",
    "names": ""
  },
  "items": [
    {
      "id": 0,
      "titulo": "",
      "foto": "",
      "url": "",
      "frete_gratis": false
    }
  ]
}
```

## Quando usar

- Para exibir Kits/Looks criados na loja
- Em seções de destaque na página inicial
- Para criar promoções de produtos combinados
- Em carrosséis ou galerias de kits

## Exemplo

```twig
{% set kits = store.productKit() %}
{% if kits.items|length > 0 and kits.config.show_principal == '1' %}
<section id="kits" class="block{{ kits.config.formato == '1' ? ' mb-4' : '' }}">
  <h2 class="titulo mb-3">{{ kits.config.names }}</h2>

  <div class="block {{ kits.config.formato == '1' ? 'carousel owl-carousel owl-theme px-3' : 'row justify-content-center' }}">
    {% for kit in kits.items %}
    <div class="block text-center {{ kits.config.formato == '1' ? 'p-1' : 'col-md-3 col-sm-6 mb-4' }}">
      <div class="item block">
        <a href="{{ kit.url }}">
          <div class="foto">
            <img src="{{ kit.foto }}" alt="{{ kit.titulo }}" class="img-cover lazy" />
          </div>
          <div class="det">
            <h3 class="t">{{ kit.titulo }}</h3>
            {% if kit.frete_gratis %}
            <p class="mb-3"><span class="bg-success px-2 py-1 text-white">FRETE GRÁTIS</span></p>
            {% endif %}
            <span class="bt-comprar">CONFERIR O {{ kits.config.name|upper }}</span>
          </div>
        </a>
      </div>
    </div>
    {% endfor %}
  </div>
</section>
{% endif %}
```

Saída esperada:

```text
Carrossel ou grid de kits/looks com imagens e títulos
```

## Retorno dos dados

**config** - Configurações dos kits

- `config.show_menu` (bool) - Se permite link no menu de categorias
- `config.show_principal` (bool) - Se permite mostrar na página inicial
- `config.formato` (int) - Formato: 1 = Carrossel; 2 = Livre
- `config.total` (int) - Quantidade total de kits
- `config.url` (string) - URL para listagem de todos os kits
- `config.name` (string) - Nomenclatura singular (Kit, Look, etc)
- `config.names` (string) - Nomenclatura plural

**items** - Lista de kits disponíveis

- `items[x].id` (int) - ID do kit
- `items[x].titulo` (string) - Título do kit
- `items[x].foto` (string) - URL da imagem
- `items[x].url` (string) - URL de acesso direto
- `items[x].frete_gratis` (bool) - Se tem frete grátis

## Parâmetros de consulta

| Parâmetro | Padrão | Descrição                                   |
| --------- | ------ | ------------------------------------------- |
| id        | ''     | ID do kit específico                        |
| ids       | ''     | IDs dos kits (separar com vírgula: 1,2,3,4) |
| cid       | ''     | ID da categoria nível 1                     |
| sid       | ''     | ID da categoria nível 2                     |
| ssid      | ''     | ID da categoria nível 3                     |
| limit     | 4      | Quantidade de itens a retornar              |

## Observações

- Suporta dois formatos de exibição: carrossel e grid livre
- A nomenclatura (Kit, Look, Coleção) pode ser customizada
- Permite filtro por categoria
- É ideal usar OWL Carousel para formato carrossel

## Erros comuns

### Erro 1: Renderizar quando `show_principal` está desativado

**Problema**: Seção aparece mesmo com módulo desabilitado.
**Diagnóstico**: `kits.config.show_principal` não é `'1'`.
**Solução**: Validar `kits.config.show_principal == '1'` antes de renderizar.

### Erro 2: Ignorar lista vazia de kits

**Problema**: Estrutura aparece sem itens.
**Diagnóstico**: `kits.items|length == 0`.
**Solução**: Checar `kits.items|length > 0` antes do loop.

## Veja também

- [Product To Box](04-store/producttobox.md)
- [Visão geral store](04-store/visao-geral-store.md)
