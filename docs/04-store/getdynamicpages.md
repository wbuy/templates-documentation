---
title: "getDynamicPages()"
slug: "getdynamicpages"
doc_type: "reference"
summary: "Método que retorna páginas dinâmicas cadastradas na loja virtual, com opções de filtro por localização e formatação de texto."
tags:
  - store
  - páginas
  - dinâmico
  - menu
  - conteúdo
related:
  - 04-store/visao-geral-store.md
  - 04-store/getinfopages.md
  - 04-store/formularios-dinamicos.md
---

## O que faz

O método `store.dynamicPages()` recupera páginas customizáveis criadas no painel da loja. Retorna HTML pronto com links formatados, permitindo filtragem por tipo (Menu, Institucional, Precisa de ajuda), e opções de transformação de texto (maiúsculas). Ideal para criar menus dinâmicos e seções de links institucionais.

## Sintaxe

```twig
{% set paginas = store.dynamicPages() %}
{% set paginas = store.dynamicPages({menu: '1', text_upper: true}) %}
```

**Parâmetros**:

- `menu` (string) — '1' para páginas no menu, '0' para não-menu
- `local` (string) — '' (todas), '1' (Institucional), '2' (Precisa de ajuda)
- `text_upper` (boolean) — true para maiúsculas
- `return_simple` (boolean) — true para array puro

### Retorno

```json
[
  "<a href=\"blog/\">Nosso blog</a>"
]
```

## Quando usar

- Criar menu de links institucionais dinâmico
- Exibir seção "Precisa de ajuda?"
- Renderizar links de footer
- Construir navegação customizada

## Exemplo

```twig
{% set paginas = store.dynamicPages({text_upper: true}) %}
<div class="links">
  {% for pagina in paginas %}
    <p>{{ pagina|raw }}</p>
  {% endfor %}
</div>
```

## Observações

- Retorna HTML já formatado e pronto
- Página deve estar criada no painel
- `return_simple` para dados brutos

## Erros comuns

### Erro 1: Esquecer `|raw`

**Problema**: HTML como texto `<a href...`
**Solução**: `{{ pagina|raw }}`

### Erro 2: Parâmetro incorreto

**Problema**: `menu: 1` (número) em vez de `'1'` (string)
**Solução**: Sempre string: `menu: '1'`

## Veja também

- [Get Info Pages](04-store/getinfopages.md)
- [Formulários Dinâmicos](04-store/formularios-dinamicos.md)
