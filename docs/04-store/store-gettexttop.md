---
title: "store.getTextTop()"
slug: "store-gettexttop"
doc_type: "reference"
summary: "Método que retorna texto customizado configurável para exibição no topo das páginas de produtos com suporte a HTML."
tags:
  - store
  - texto
  - customização
  - mensagens
related:
  - 04-store/visao-geral-store.md
  - 04-store/store-productdetail.md
---

## O que faz

Retorna um texto customizado configurado para exibição no topo das páginas de produtos. Este texto pode ser usado para mensagens de promoção, avisos ou informações gerais.

## Sintaxe

```twig
{% set texto_topo = store.getTextTop() %}
```

### Retorno

```json
"Texto configurado para o topo"
```

## Quando usar

- Para exibir mensagens no topo de página de produtos
- Para avisos ou informações de promoção
- Em textos dinâmicos configurados no painel
- Para comunicações com cliente

## Exemplo

```twig
{% set texto_topo = store.getTextTop() %}
{% if texto_topo.ativo %}
<div class="top-message alert">
	{{ texto_topo.conteudo|raw }}
</div>
{% endif %}
```

Saída esperada:
```
Mensagem de promoção ou aviso exibida no topo
```

## Retorno dos dados

**ativo** (bool) - Se o texto está ativo para exibição

**conteudo** (string) - Conteúdo do texto (pode conter HTML)

**titulo** (string) - Título opcional do texto

## Parâmetros de consulta

Nenhum parâmetro obrigatório.

## Observações

- Texto customizável no painel de controle
- Suporta HTML no conteúdo
- Étimo para comunicações dincâmicas
- Pode ser ligado/desligado conforme necessidade

## Erros comuns

### Erro 1: Renderizar sem validar texto
**Problema**: Área vazia no topo da página.
**Diagnóstico**: `televendas` vazio.
**Solução**: Verificar `if televendas` antes de renderizar.

### Erro 2: Não usar `|raw` quando há HTML
**Problema**: Tags aparecem como texto.
**Diagnóstico**: Conteúdo com HTML configurado no painel.
**Solução**: Renderizar com `{{ televendas|raw }}` quando necessário.

## Veja também

- [Store Product Detail](04-store/store-productdetail.md)
- [Visão geral store](04-store/visao-geral-store.md)
