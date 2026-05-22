---
title: "featuredIcon()"
slug: "featuredicon"
doc_type: "reference"
summary: "Método que retorna alertas destaque da loja com ícones customizáveis, cores e links."
tags:
  - store
  - alertas
  - ícones
  - destaque
  - visual
related:
  - 04-store/visao-geral-store.md
  - 04-store/cart.md
---

## O que faz

O método `store.featuredIcon()` recupera alertas/badges de destaque configurados na loja, com suporte a ícones Font Awesome ou imagens customizadas. Cada alerta pode ter cores customizadas, texto, link de ação e configuração de abertura em nova aba, ideal para promoções, avisos e destaques visuais.

## Sintaxe

```twig
{% set alertas = store.featuredIcon() %}

{# Com parâmetro de limite #}
{% set alertas = store.featuredIcon({limit: '10'}) %}
```

**Parâmetro**: `limit` (string) — Quantidade de alertas a retornar (padrão: 5)

## Quando usar

- Exibir seção de alertas/destaques na página
- Mostrar promoções especiais com ícones
- Criar badges de avisos importante
- Destacar funcionalidades com ícones visuais

## Exemplo

```twig
{% set alertas = store.featuredIcon() %}
<div id="alerts">
  <div class="central">
    {% for alerta in alertas %}
      {% set icone = alerta.icone_tipo == '1' ?
        '<i class="fa ' ~ alerta.icone ~ '" style="color: ' ~ alerta.cor_icone ~ '"></i>' :
        '<img src="' ~ alerta.icone ~ '" alt="' ~ alerta.nome ~ '" />'
      %}
      
      {% if alerta.link %}
      <p><a href="{{ alerta.link }}" target="{{ alerta.target }}" style="background-color: {{ alerta.cor_fundo }}">
        {{ icone|raw }} 
        <span style="color: {{ alerta.cor_texto }}">{{ alerta.nome }}</span>
      </a></p>
      {% else %}
      <p style="background-color: {{ alerta.cor_fundo }}">
        {{ icone|raw }} 
        <span style="color: {{ alerta.cor_texto }}">{{ alerta.nome }}</span>
      </p>
      {% endif %}
    {% endfor %}
  </div>
</div>
```

Saída esperada:
```html
<div id="alerts">
  <p><a href="promocoes" target="_blank" style="background-color: #ff6b6b">
    <i class="fa fa-gift" style="color: white"></i>
    <span style="color: white">Promoção Especial</span>
  </a></p>
</div>
```

## Observações

- Tipo 1: Usa ícones Font Awesome (campo `icone` contém classe fa)
- Tipo 2: Usa imagens customizadas (campo `icone` contém URL)
- Cores hexadecimais: `cor_fundo`, `cor_texto`, `cor_icone`
- Target: `_blank` abre em nova aba, vazio abre na mesma
- Padrão: 5 alertas se limite não for especificado

## Erros comuns

### Erro 1: Esquecer o `|raw` para renderizar HTML
**Problema**: Ícone aparece como string `<i class="fa...">`
**Diagnóstico**: HTML do ícone é exibido como texto
**Solução**: Usar filtro Twig `{{ icone|raw }}`

### Erro 2: Confundir tipos de ícone
**Problema**: Tentar usar Font Awesome com tipo 2 ou vice-versa
**Diagnóstico**: Ícone não exibe corretamente
**Solução**: Verificar `icone_tipo`: se 1, usar classe fa; se 2, usar URL

### Erro 3: Cores sem verificação
**Problema**: Acessar `cor_fundo` quando não está configurada
**Diagnóstico**: Retorna vazio ou string vazia
**Solução**: Sempre incluir cor ou verificar antes de aplicar

## Veja também

- [Visão geral store](04-store/visao-geral-store.md)
- [Cart](04-store/cart.md)
- [Main Banner](04-store/mainbanner.md)
