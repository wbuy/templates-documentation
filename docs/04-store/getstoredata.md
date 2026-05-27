---
title: "getStoreData"
slug: "getstoredata"
doc_type: "reference"
summary: "Retorna as informações básicas e de contato da loja, como endereço, CNPJ, telefone, e-mail e redes sociais."
tags:
  - loja
  - contato
  - endereço
  - redes-sociais
related:
  - 04-store/visao-geral-store.md
  - 04-store/socialicons.md
---

## O que faz

O método `getStoreData` retorna um objeto consolidado com todas as informações institucionais cadastradas no painel da wBuy. É a fonte principal para dados de rodapé e páginas de contato.

Inclui dados como nome fantasia, razão social, CNPJ, endereços completos, múltiplos telefones, e-mail de atendimento e links para redes sociais principais (Facebook, Instagram, etc).

## Sintaxe

```twig
{% set storeData = store.getStoreData() %}

{{ storeData.nome_fantasia }}
{{ storeData.cnpj }}
{{ storeData.email }}
```

**Retorno**: Objeto contendo chaves como `nome_fantasia`, `cnpj`, `endereco`, `telefone`, `redes_sociais` (array), etc.

### Retorno

```json
{
  "id": 0,
  "loja": "",
  "razao": "",
  "doc1": "",
  "cep": "",
  "endereco": "",
  "endnum": "",
  "complemento": "",
  "bairro": "",
  "cidade": "",
  "uf": "",
  "telefone": "",
  "celular": ""
}
```

## Quando usar

- Inserir o CNPJ e Razão Social no rodapé (exigência legal).
- Montar seções de "Fale Conosco".
- Renderizar links de redes sociais dinamicamente.
- Exibir o endereço físico da loja para retirada ou confiança.

## Exemplo

```twig
{% set info = store.getStoreData() %}
<footer class="footer-info">
  <p>{{ info.razao_social }} - CNPJ: {{ info.cnpj }}</p>
  <p>Endereço: {{ info.logradouro }}, {{ info.numero }} - {{ info.cidade }}/{{ info.uf }}</p>
  <p>Fale conosco: <a href="mailto:{{ info.email }}">{{ info.email }}</a></p>
</footer>
```

Saída esperada:
```html
<footer class="footer-info">
  <p>Minha Loja Virtual LTDA - CNPJ: 00.000.000/0001-00</p>
  <p>Endereço: Rua Principal, 123 - São Paulo/SP</p>
  <p>Fale conosco: <a href="mailto:contato@minhaloja.com.br">contato@minhaloja.com.br</a></p>
</footer>
```

## Observações

- Os nomes das chaves podem variar dependendo da versão da API, mas geralmente seguem o padrão snake_case.
- Alguns campos podem estar vazios se não preenchidos no painel; sempre valide antes de exibir.
- Para ícones de redes sociais, pode ser mais prático usar o método dedicado `store.getSocialIcons()`.

## Erros comuns

### Erro 1: Não validar campos opcionais
**Problema**: Tentar exibir um telefone ou rede social que a loja não possui, resultando em espaços vazios ou links quebrados.
**Solução**: Usar `{% if info.campo %}` ao redor do HTML correspondente.

### Erro 2: Expor dados sensíveis indevidamente
**Problema**: Exibir e-mails ou números internos no front-end por engano.
**Solução**: Verificar no painel administrativo quais dados estão marcados como públicos para o template.

## Veja também

- [Ícones sociais](04-store/socialicons.md)
- [Visão geral store](04-store/visao-geral-store.md)
