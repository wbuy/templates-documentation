---
title: "socialIcons"
slug: "socialicons"
doc_type: "reference"
summary: "Método que retorna ícones e links de redes sociais configuradas para exibição em footer e áreas de integração social."
tags:
  - store
  - redes-sociais
  - ícones
  - integração
related:
  - 04-store/visao-geral-store.md
  - 04-store/widgetfacebook.md
---

## O que faz

Disponibiliza como retorno os ícones de redes sociais configuradas para a loja. Este método retorna URLs e informações de redes sociais para exibição em templates.

## Sintaxe

```twig
{% set redes = store.socialIcons() %}
```

### Retorno

```json
{
  "items": [
    {
      "id": 0,
      "tipo": 0,
      "icone": "",
      "titulo": "",
      "url": "",
      "cor_fundo": "",
      "cor_icone": ""
    }
  ],
  "raw": [
    ""
  ]
}
```

## Quando usar

- Para exibir ícones de redes sociais no footer
- Em áreas de contato/conectar-se
- Para criar links de seguir nas redes
- Em shares de conteúdo

## Exemplo

```twig
{% set redes = store.socialIcons() %}
{% if redes.raw|length > 0 %}
<div class="social-icons">
	{% for item in redes.raw %}
		{{ item|raw }}
	{% endfor %}
</div>
{% endif %}
```

Saída esperada:
```
Links das redes sociais com ícones
```

## Retorno dos dados

**items** - Array de redes sociais
- `items[x].tipo` (int) - 1 = ícone interno; 2 = ícone externo
- `items[x].icone` (string)
- `items[x].titulo` (string)
- `items[x].url` (string)
- `items[x].cor_fundo` (string)
- `items[x].cor_icone` (string)

**raw** - Array de itens prontos para renderização no template

## Parâmetros de consulta

Nenhum parâmetro obrigatório.

## Observações

- Dados são configuráveis no painel de controle
- É comum usar em footers de templates
- Suporte a múltiplas redes sociais
- URLs já vem formatadas e prontas

## Erros comuns

### Erro 1: Esquecer `|raw` na saída
**Problema**: HTML dos ícones aparece como texto.
**Diagnóstico**: Tags visíveis no layout.
**Solução**: Renderizar `{{ item|raw }}` ao iterar `redes.raw`.

### Erro 2: Não validar retorno vazio
**Problema**: Área de redes sociais sem conteúdo.
**Diagnóstico**: `redes.raw|length` igual a 0.
**Solução**: Condicionar a renderização com `if redes.raw|length > 0`.

## Veja também

- [Widget Facebook](04-store/widgetfacebook.md)
- [Visão geral store](04-store/visao-geral-store.md)
