---
title: "footerText()"
slug: "footertext"
doc_type: "reference"
summary: "Método que retorna textos customizáveis para a base e rodapé do site, permitindo conteúdo dinâmico em HTML."
tags:
  - store
  - rodapé
  - footer
  - texto-dinâmico
  - apresentação
related:
  - 04-store/visao-geral-store.md
  - 04-store/store-gettexttop.md
---

## O que faz

O método `store.footerText()` recupera textos personalizados para serem exibidos em duas áreas principais da página: base do site (geralmente parte inferior da página) e rodapé (footer tag). Ambos suportam HTML raw, permitindo conteúdo rico e formatado customizado pelo lojista via painel administrativo.

## Sintaxe

```twig
{% set footerText = store.footerText() %}

{# Acessar propriedades #}
{{ footerText.base|raw }}     {# HTML base do site #}
{{ footerText.rodape|raw }}   {# HTML do rodapé #}
```

**Retorna**: Objeto com duas propriedades string (HTML raw)

## Quando usar

- Exibir texto/conteúdo na base da página
- Renderizar rodapé com informações customizadas
- Integrar conteúdo dinâmico em footer
- Exibir políticas, avisos legais ou créditos

## Exemplo

```twig
{% set footerText = store.footerText() %}

{# Área de base (geralmente antes do footer) #}
<div class="site-base">
  {% if footerText.base %}
    {{ footerText.base|raw }}
  {% else %}
    <p>© 2024 Loja Virtual. Todos os direitos reservados.</p>
  {% endif %}
</div>

{# Footer tag (rodapé) #}
<footer class="site-footer">
  {% if footerText.rodape %}
    {{ footerText.rodape|raw }}
  {% else %}
    <nav>
      <a href="/sobre">Sobre</a>
      <a href="/contato">Contato</a>
    </nav>
  {% endif %}
</footer>
```

Saída esperada:
```html
<div class="site-base">
  <p>© 2024 Loja Virtual. Todos os direitos reservados.</p>
</div>

<footer class="site-footer">
  <nav><a href="/sobre">Sobre</a></nav>
</footer>
```

## Observações

- Ambos os campos suportam HTML; use `|raw` para renderizar
- Textos são customizáveis pelo lojista no painel
- Podem conter links, formatação, e conteúdo rico
- Recomenda-se sempre ter fallback em caso de texto vazio
- Performance: Acesso muito rápido

## Erros comuns

### Erro 1: Esquecer `|raw` para renderizar HTML
**Problema**: Conteúdo HTML aparece como texto: `<p>...</p>`
**Diagnóstico**: HTML é exibido literalmente ao invés de renderizado
**Solução**: Usar filtro Twig: `{{ footerText.base|raw }}`

### Erro 2: Não verificar se propriedade está vazia
**Problema**: Rodapé vazio quando lojista não configurou
**Diagnóstico**: Página sem rodapé ou sem conteúdo na base
**Solução**: Usar condicional `if footerText.base` e fornecer fallback

### Erro 3: XSS se não usar footerText oficialmente
**Problema**: Segurança: footerText já é sanitizado pelo servidor
**Diagnóstico**: N/A se usar método oficial
**Solução**: Confiar apenas em `store.footerText()`, não em entrada do usuário

## Veja também

- [Visão geral store](04-store/visao-geral-store.md)
- [Cart](04-store/cart.md)
- [Recursos gerais](04-store/recursos-gerais.md)
