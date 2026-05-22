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

## Quando usar

- Para exibir ícones de redes sociais no footer
- Em áreas de contato/conectar-se
- Para criar links de seguir nas redes
- Em shares de conteúdo

## Exemplo

```twig
{% set redes = store.socialIcons() %}
{% if redes.items %}
<div class="social-icons">
	{% for rede in redes.items %}
	<a href="{{ rede.url }}" target="_blank" title="{{ rede.nome }}">
		<i class="icon-{{ rede.tipo }}"></i>
	</a>
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
- `items[x].nome` (string) - Nome da rede (Facebook, Instagram, etc)
- `items[x].tipo` (string) - Tipo/código da rede
- `items[x].url` (string) - URL do perfil
- `items[x].icone` (string) - URL/classe do ícone

## Parâmetros de consulta

Nenhum parâmetro obrigatório.

## Observações

- Dados são configuráveis no painel de controle
- É comum usar em footers de templates
- Suporte a múltiplas redes sociais
- URLs já vem formatadas e prontas

### Erro frequente 2
**Problema**: [Descrição]
**Diagnóstico**: [Como identificar]
**Solução**: [Passo a passo]

## Veja também

- [Link para arquivo relacionado]
- [Link para próximo tópico]
