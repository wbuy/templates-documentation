---
title: "getInfoPages"
slug: "getinfopages"
doc_type: "reference"
summary: "Retorna a lista de páginas institucionais ou informativas cadastradas na loja, como 'Sobre Nós', 'Política de Privacidade', entre outras."
tags:
  - páginas
  - institucional
  - informação
  - conteúdo
related:
  - 04-store/visao-geral-store.md
  - 04-store/getdynamicpages.md
---

## O que faz

O método `getInfoPages` recupera um array de objetos contendo informações sobre as páginas institucionais da loja. Essas páginas são geralmente criadas no painel administrativo para fornecer informações estáticas ao cliente.

Este método é ideal para construir menus de rodapé ou barras laterais que listam links para páginas de ajuda, termos de uso e outras informações institucionais.

## Sintaxe

```twig
{% set infoPages = store.getInfoPages() %}

{% for page in infoPages %}
    <a href="{{ page.url }}">{{ page.nome }}</a>
{% endfor %}
```

**Retorno**: Array de strings com HTML pronto para links das páginas.

### Retorno

```json
[
  "<a href=\"/p/sobre-nos\">Sobre Nós</a>"
]
```

## Quando usar

- Criar menus institucionais no rodapé.
- Listar links de políticas de troca e privacidade.
- Criar uma página de índice de conteúdos informativos.
- Pré-condição: As páginas devem estar cadastradas e ativas no painel da wBuy.

## Exemplo

```twig
<ul class="footer-links">
  {% for page in store.getInfoPages() %}
    <li><a href="{{ page.url }}" title="{{ page.nome }}">{{ page.nome }}</a></li>
  {% endfor %}
</ul>
```

Saída esperada:
```html
<ul class="footer-links">
  <li><a href="/p/sobre-nos" title="Sobre Nós">Sobre Nós</a></li>
  <li><a href="/p/politica-de-privacidade" title="Política de Privacidade">Política de Privacidade</a></li>
</ul>
```

## Observações

- A ordem das páginas segue a ordenação definida no painel administrativo.
- Páginas desativadas não são retornadas por este método.
- O campo `url` já vem formatado com o caminho completo relativo à raiz da loja.

## Erros comuns

### Erro 1: Não verificar se o array está vazio
**Problema**: O loop tenta rodar mas não há páginas cadastradas.
**Diagnóstico**: O HTML gerado fica vazio ou com tags de lista órfãs.
**Solução**: Usar uma condicional `if infoPages|length > 0`.

### Erro 2: Confundir com páginas de blog
**Problema**: Tentar listar posts de blog usando `getInfoPages`.
**Diagnóstico**: Posts não aparecem no resultado.
**Solução**: Usar o método `getBlogPosts` para conteúdos dinâmicos de blog.

## Veja também

- [Visão geral store](04-store/visao-geral-store.md)
- [Páginas dinâmicas](04-store/getdynamicpages.md)
