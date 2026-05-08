---
title: "Codificacao ISO-8859-1"
slug: "encoding-iso-8859-1"
doc_type: "concept"
summary: "Explicação sobre a importância de usar a codificação ISO-8859-1 (Latin-1) para arquivos de template wBuy, garantindo compatibilidade e evitando erros de caracteres acentuados."
tags:
  - "encoding"
  - "iso-8859-1"
  - "latin-1"
related:
  - 01-introducao/por-onde-comecar.md
  - 01-introducao/wbuy-watcher-npm.md
  - 01-introducao/telas-customizaveis.md
---

## O que faz

Instrui os desenvolvedores sobre a necessidade de configurar seus arquivos de template com a codificação ISO-8859-1 (Latin-1) para garantir que caracteres acentuados e símbolos sejam exibidos corretamente na plataforma wBuy, evitando erros comuns relacionados à codificação de caracteres.

## Sintaxe

Não se aplica. Este documento é um guia conceitual, não possui assinatura ou parâmetros.

## Quando usar

Use este guia quando:

- Você está configurando seu ambiente de desenvolvimento para criar templates wBuy e precisa garantir que seus arquivos estejam com a codificação correta.
- Você está enfrentando problemas de caracteres acentuados aparecendo como símbolos estranhos ou "?" na plataforma wBuy e quer entender como resolver isso.
- Você quer evitar erros de codificação que podem ocorrer durante o desenvolvimento e teste dos templates, garantindo uma experiência de desenvolvimento mais fluida e sem frustrações.
- Você está colaborando com outros desenvolvedores e quer garantir que todos estejam usando a mesma codificação para evitar problemas de compatibilidade.

## Exemplo

### Configurando a codificação no VS Code

1. Abra o arquivo do template no VS Code.
2. Vá para o menu "File" (Arquivo) e selecione "Save with Encoding" (Salvar com Codificação).
3. Escolha "ISO-8859-1" na lista de opções.
4. Salve o arquivo e confirme que a codificação foi aplicada corretamente.

### Configurando a codificação no PhpStorm

1. Abra o arquivo do template no PhpStorm.
2. Vá para o menu "File" (Arquivo) e selecione "File Properties" (Propriedades do Arquivo).
3. Na seção "Encoding" (Codificação), escolha "ISO-8859-1" (Latin-1) na lista de opções.
4. Salve as alterações e confirme que a codificação foi aplicada corretamente.

### Outras IDEs

A maioria das IDEs modernas tem uma opção similar para configurar a codificação de arquivos. Procure por "Encoding" ou "Character Set" nas configurações do arquivo ou projeto e selecione "ISO-8859-1" ou "Latin-1". Alternativamente, consulte o manual de ajuda da sua IDE para instruções específicas sobre como configurar a codificação de arquivos.

## Observações

- A codificação ISO-8859-1 é essencial para garantir que caracteres acentuados e símbolos sejam exibidos corretamente na plataforma wBuy, evitando erros comuns de codificação.
- Certifique-se de que todos os arquivos do template estejam configurados com a mesma codificação para evitar problemas de compatibilidade e garantir uma experiência de desenvolvimento mais fluida.
- Se você estiver colaborando com outros desenvolvedores, é importante estabelecer uma convenção de codificação para garantir que todos estejam usando a mesma configuração e evitar problemas de compatibilidade.
- Se possível, configure seu editor para sempre salvar arquivos com codificação ISO-8859-1 por padrão ao trabalhar com templates wBuy, para evitar ter que configurar manualmente cada arquivo.

## Erros comuns

### Erro 1: "Caracteres acentuados aparecem como símbolos estranhos"

Problema: Você editou um arquivo do template, mas os caracteres acentuados aparecem como símbolos estranhos ou "?" na plataforma wBuy.

Solução:

1. Verifique a codificação do arquivo no seu editor. Certifique-se de que está configurada para ISO-8859-1 (Latin-1).
2. Se o arquivo estava em uma codificação diferente, como UTF-8, converta-o para ISO-8859-1 usando a opção "Save with Encoding" (Salvar com Codificação) no seu editor.
3. Evite usar caracteres que não sejam suportados por ISO-8859-1, como emojis ou caracteres de idiomas asiáticos, pois eles podem causar problemas de codificação.

## Veja também

- [Por Onde Começar](01-introducao/por-onde-comecar.md) — Guia passo a passo para iniciar desenvolvimento.
- [wBuy Watcher NPM](01-introducao/wbuy-watcher-npm.md) — Configuração e uso do Watcher para desenvolvimento local.
- [Telas Customizáveis](01-introducao/telas-customizaveis.md) — Visão geral das telas que suportam customização.
- [Visão Geral de Templates](01-introducao/visao-geral.md) — Panorama da stack tecnológica wBuy.
- [Sintaxe Básica do Twig](02-twig/sintaxe-basica.md) — Introdução à engine de templates Twig.
