---
title: "Por onde começar a desenvolver templates wBuy"
slug: "por-onde-comecar"
doc_type: "concept"
summary: "Guia passo a passo para iniciar o desenvolvimento de templates wBuy: configuração do ambiente, estrutura de arquivos, uso do watcher e primeiros passos com Twig e store."
tags:
  - introducao
  - wbuy
  - templates
  - desenvolvimento
related:
  - 01-introducao/wbuy-watcher-npm.md
  - 01-introducao/visao-geral.md
  - 01-introducao/telas-customizaveis.md
  - 02-twig/visao-geral-twig.md
  - 04-store/visao-geral-store.md
  - 03-api/configuracoes-config_tema.json.md
---

## O que faz

Se você está começando a desenvolver templates para a plataforma wBuy, este guia passo a passo irá orientá-lo pelos primeiros passos essenciais para configurar seu ambiente de desenvolvimento, entender a estrutura de arquivos e começar a trabalhar com Twig e o objeto `store`.

## Sintaxe

Não se aplica. Este documento é um guia conceitual e prático, não possui assinatura ou parâmetros.

## Quando usar

Use este guia quando:

- Você é um desenvolvedor iniciante na plataforma wBuy e quer configurar seu ambiente de desenvolvimento local.
- Você precisa entender a estrutura de arquivos do template wBuy e como organizar seus arquivos de forma eficiente.
- Você quer aprender a usar o wBuy Watcher para sincronizar suas alterações em tempo real com a plataforma.
- Você está pronto para começar a escrever código Twig e interagir com o objeto `store` para criar templates dinâmicos e personalizados.

### Estrutura de arquivos do template wBuy

A estrutura de arquivos do template wBuy é organizada para facilitar o desenvolvimento e a manutenção. Aqui estão os principais diretórios e arquivos que você encontrará:

- **`assets/`**: Contém arquivos estáticos como imagens, ícones etc.
- **`estruturas/`**: Contém pastas referentes às estruturas de layout padrão da wBuy. São elas: `center`, `bottom` e `top`:
  - **`center/`**: Estrutura de layout central, usada para páginas como a home e categorias.
  - **`bottom/`**: Estrutura de layout inferior, usada para rodapés e seções finais.
  - **`top/`**: Estrutura de layout superior, usada para cabeçalhos e seções iniciais (como o módulo **Ofertas periódicas**, por exemplo).
- **`paginas/`**: Armazena os arquivos de página específicos, como a página inicial, página de produto, etc. Aqui são armazenados tanto os arquivos `html` quanto os arquivos `css` e `js` de cada página.
- **`widgets/`**: Contém componentes reutilizáveis que podem ser incluídos em várias páginas, como carrosséis, banners, box de produto, etc.
- **`config_tema.json`**: Arquivo de configuração do template, onde você pode definir variáveis globais e outras configurações.

## Exemplo

Após configurar o watcher você terá uma estrutura assim:

```md
meu-template/
├── assets/
│   ├── logo.png
│   ├── favicon.ico
│   └── ...
├── estruturas/
│   ├── center/
│   ├── bottom/
│   └── top/
├── paginas/
│   ├── home/
│   │   ├── home.html
│   │   ├── home.css
│   │   └── home.js
│   ├── produto/
│   │   ├── produto.html
│   │   ├── produto.css
│   │   └── produto.js
│   └── ...
├── widgets/
│   ├── carrossel/
│   │   ├── carrossel.html
│   │   ├── carrossel.css
│   │   └── carrossel.js
│   ├── banner/
│   │   ├── banner.html
│   │   ├── banner.css
│   │   └── banner.js
│   └── ...
└── config_tema.json
```

## Observações

- **Sincronização em tempo real**: O wBuy Watcher sincroniza automaticamente todas as alterações com a plataforma, permitindo visualização imediata sem recarregamento manual.
- **Encoding obrigatório**: Sempre use encoding **ISO-8859-1** em seus arquivos para garantir compatibilidade total com a plataforma.
- **Cache**: Alterações em estruturas Twig podem ser cacheadas; use o modo de desenvolvimento para testes sem cache.
- **Mobile**: Teste sempre em dispositivos mobile, pois a estrutura de layout responsivo é crítica na plataforma wBuy.
- **Performance**: Minimize includes e loops Twig em seções que são renderizadas frequentemente; considere usar AJAX para dados dinâmicos em áreas críticas de performance.

## Erros comuns

### Erro 1: "Credenciais inválidas na configuração do watcher"

**Problema**: Ao executar `wbuy configure`, recebe erro de autenticação apesar de usar as credenciais corretas.
**Diagnóstico**: As credenciais podem estar armazenadas no arquivo `config.json` local de forma incorreta, ou a integração Rest API não está habilitada na plataforma.
**Solução**:

1. Verifique que a integração Rest API está ativa em **Plataforma > API e Webhooks > Opções > Integração Rest API**
2. Regenere as credenciais (username e keycode) se necessário
3. Execute `wbuy configure` novamente e insira os valores com cuidado (sem espaços extras)

### Erro 2: "Arquivo não sincroniza após alteração"

**Problema**: Altera um arquivo Twig ou HTML mas não vê a mudança refletida na plataforma, mesmo após salvar.
**Diagnóstico**: O watcher pode ter parado ou a sincronização falhou silenciosamente.
**Solução**:

1. Verifique se o watcher está rodando (observe a saída do terminal `wbuy run`)
2. Reinicie o watcher: `Ctrl+C` e execute `wbuy run` novamente
3. Verifique se o arquivo está em encoding ISO-8859-1 (não UTF-8)
4. Confirme que você não tem arquivos com caracteres não suportados
5. Verifique se o arquivo não possui erros de sintaxe que possam impedir a renderização (ex.: loops sem fechamento)

### Erro 3: "Estrutura de arquivo não reconhecida"

**Problema**: Cria um novo arquivo ou diretório mas o watcher não o sincroniza.
**Diagnóstico**: A estrutura de diretórios deve estar exatamente como esperado pelo template; nomes incorretos ou diretórios ausentes impedem sincronização.
**Solução**:

1. Confirme que você está usando a estrutura padrão: `assets/`, `estruturas/`, `paginas/`, `widgets/`
2. Não crie diretórios fora da estrutura padrão
3. Se precisar de organização adicional dentro de `widgets/`, crie subpastas dentro desse diretório

## Veja também

- [Visão Geral — Templates wBuy](01-introducao/visao-geral.md) — Panorama geral da stack tecnológica
- [Telas Customizáveis](01-introducao/telas-customizaveis.md) — Lista completa de páginas que podem ser customizadas
- [Visão Geral do Twig](02-twig/visao-geral-twig.md) — Conceitos fundamentais de templates Twig
- [Visão Geral do Store](04-store/visao-geral-store.md) — Arquitetura do objeto global store
- [wBuy Watcher NPM](01-introducao/wbuy-watcher-npm.md) — Instalação detalhada e configuração do watcher
