---
title: "Documentação da API wBuy"
slug: "documentacao-api"
doc_type: "concept"
summary: "Visão geral da API wBuy para desenvolvimento de templates. Explora os recursos disponíveis, endpoints principais e as referências técnicas necessárias para integrar chamadas de API em temas personalizados."
tags:
  - api
  - templates
  - documentação
  - referência
related:
  - 01-introducao/visao-geral.md
  - 01-introducao/por-onde-comecar.md
  - 04-store/visao-geral-store.md
  - 03-api/visao-geral-api.md
---

## O que faz

A API da plataforma wBuy fornece um conjunto de métodos que você pode chamar a partir de seus templates para recuperar dados dinâmicos da loja — como informações de produtos, categorias, variações, cores e dados do cliente. Esses métodos complementam o objeto global `store` e são essenciais para criar templates interativos e personalizados.

A documentação da API está disponível em dois formatos complementares:

- **Recursos disponíveis para templates** (mais voltado ao desenvolvedor):
  <https://doc-templates.wbuy.com.br/recursos/api/>  
  Este link detalha quais recursos da API estão disponíveis especificamente para uso em temas, com exemplos práticos de implementação.

- **Referência técnica completa** (Postman):  
  <https://documenter.getpostman.com/view/4141833/RWTsquyN?version=latest#intro>  
  Esta é a referência técnica oficial da API com todos os endpoints, parâmetros, respostas e exemplos testáveis.

## Sintaxe

Não se aplica. Este documento é uma visão geral conceitual, não documenta uma função ou método específico.

## Quando usar

Leia este arquivo quando:

- você está começando a trabalhar com a API wBuy e precisa entender seu papel no desenvolvimento de templates;
- você quer saber quais recursos da API estão disponíveis para temas personalizados;
- você precisa acessar as referências técnicas completas para implementar chamadas de API;
- você deseja entender como a API se integra com o objeto `store` e o Twig.

## Exemplo

Fluxo típico de uso da API em um template:

1. **Consultar dados via API** (no Twig server-side):

   ```twig
   {% set categories = categoryGetAll() %}
   {% for category in categories %}
     {{ category.name }}
   {% endfor %}
   ```

2. **Ou recuperar dados client-side** (via AJAX no JavaScript):

   ```js
   fetch('/api/products/get?id=123')
     .then(response => response.json())
     .then(data => { /* processar dados */ });
   ```

3. **Usar dados combinados** com o objeto `store`:

   ```js
   if (store.cart.items) {
     // Dados do carrinho já estão disponíveis globalmente
     console.log(store.cart.items.length);
   }
   ```

## Observações

- **Métodos divididos**: alguns métodos são chamados server-side (dentro de templates Twig) e retornam arrays/objetos processados; outros são chamados client-side via AJAX. Verifique a documentação para cada recurso.

- **Autenticação**: a maioria das chamadas de API públicas não requer autenticação especial quando feitas no contexto do template. Dados sensíveis (como dados do cliente logado) já são injetados automaticamente pelo servidor.

- **Cache**: algumas respostas de API são cacheadas para melhorar performance. Consulte a documentação técnica e o diretório `08-cache/` para detalhes sobre comportamento de cache.

- **CORS e segurança**: chamadas client-side (AJAX) respeitam políticas de CORS. Consulte a referência técnica para endpoints seguros e limitações.

- **Consulta a endpoints que não estão na documentação de temas:** nem todos os endpoints da API estão disponíveis para uso em templates. Mas você pode utilizar estes métodos via AJAX, sendo necessário o uso de autenticação e respeitando as políticas de segurança da plataforma. Consulte a documentação técnica para detalhes sobre quais endpoints são públicos e quais exigem autenticação.

## Erros comuns

### Erro 1: Chamada a endpoint que não existe no contexto do tema

**Problema**: Você tenta chamar um método que não está documentado em <https://doc-templates.wbuy.com.br/recursos/api/> para uso em templates.  
**Diagnóstico**: Verifique se o método está listado nos recursos disponíveis para templates (nem todos os endpoints da API estão disponíveis para uso em temas).  
**Solução**: Consulte a documentação de recursos disponíveis e use apenas os métodos documentados para templates.

### Erro 2: Confundir métodos de API com propriedades do objeto `store`

**Problema**: Você tenta chamar uma função que na verdade é uma propriedade do objeto `store`.
**Diagnóstico**: Leia a referência técnica e diferencie entre chamadas de função (`function()`) e acesso a propriedades (`object.property`).
**Solução**: Consulte `04-store/visao-geral-store.md` para entender a estrutura do objeto `store`.

## Veja também

- [Visão geral dos templates wBuy](01-introducao/visao-geral.md) — contexto geral da stack
- [Visão geral do Store](04-store/visao-geral-store.md) — dados globais disponíveis no template
- [Visão geral da API detalhada](03-api/visao-geral-api.md) — detalhes técnicos de cada método
- [Recursos de API disponíveis](https://doc-templates.wbuy.com.br/recursos/api/) — documentação oficial
- [Referência técnica completa](https://documenter.getpostman.com/view/4141833/RWTsquyN?version=latest#intro) — Postman com todos os endpoints
