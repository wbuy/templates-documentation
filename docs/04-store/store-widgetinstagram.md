---
title: "store.widgetInstagram()"
slug: "store-widgetinstagram"
doc_type: "reference"
summary: "Método que disponibiliza widget de Instagram com feed de posts do lojista para integração social na loja."
tags:
  - store
  - widget
  - instagram
  - redes-sociais
related:
  - 04-store/visao-geral-store.md
  - 04-store/widgetfacebook.md
  - 04-store/socialicons.md
---

## O que faz

Disponibiliza um widget de Instagram configurado para a loja virtual. Este método integra o feed/posts do Instagram do lojista diretamente no template.

## Sintaxe

```twig
{% set instagram = store.widgetInstagram() %}
```

### Retorno

```json
{
  "token": "",
  "username": "",
  "limit": ""
}
```

## Quando usar

- Para exibir feed de Instagram na loja
- Em rodapé ou áreas de destaque social
- Para integração com redes sociais
- Para criar seções de "Siga-nos no Instagram"

## Exemplo

```twig
{% set instagram = store.widgetInstagram() %}
{% if instagram.token %}
<section class="instagram-widget">
 <h3>{{ instagram.username }}</h3>
 <div id="instagram-feed" class="instagram-feed">
  {# O widget se autorenderiza via JavaScript #}
 </div>
 <script src="{{ base_system }}/jquery2/instafeed2.min.js"></script>
</section>
{% endif %}
```

Saída esperada:

```
Widget de Instagram renderizado com posts
```

## Retorno dos dados

**token** (string) - Token de acesso para autenticação do widget

**username** (string) - Nome de usuário do Instagram

**limit** (string) - Limite máximo de posts a exibir

## Parâmetros de consulta

Nenhum parâmetro obrigatório.

## Observações

- Requer configuração de conta Instagram no painel
- O widget usa JavaScript para renderização
- Ideal para integração social
- Suporta customização de layout

## Erros comuns

### Erro 1: Não validar `instagram.token`
**Problema**: O feed não carrega.
**Diagnóstico**: `instagram.token` vazio.
**Solução**: Renderizar o bloco apenas quando `instagram.token` estiver definido.

### Erro 2: Não carregar o script do Instafeed
**Problema**: A seção aparece, mas sem posts.
**Diagnóstico**: Console com erro de `Instafeed is not defined`.
**Solução**: Incluir o script `instafeed2.min.js` antes de executar.

## Veja também

- [Widget Facebook](04-store/widgetfacebook.md)
- [Social Icons](04-store/socialicons.md)
- [Visão geral store](04-store/visao-geral-store.md)
