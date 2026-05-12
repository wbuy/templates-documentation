---
title: "Criacao de widgets com include"
slug: "criacao-de-widgets-com-include"
doc_type: "concept"
summary: "Guia para criar widgets reutilizáveis usando a diretiva include do Twig, permitindo a inclusão de componentes em várias páginas do template wBuy."
tags:
  - Twig
  - include
  - widgets
related:
  - 01-introducao/por-onde-comecar.md
  - 01-introducao/wbuy-watcher-npm.md
  - 01-introducao/encoding-iso-8859-1.md
  - 01-introducao/visao-geral.md
  - 02-twig/visao-geral-twig.md
  - 04-store/visao-geral-store.md
---

## O que faz

A diretiva `include` do Twig permite que você reutilize componentes em várias páginas do template wBuy, facilitando a manutenção e a consistência visual. Este guia irá orientá-lo sobre como criar widgets reutilizáveis usando `include`, organizando seus arquivos de forma eficiente e garantindo que suas alterações sejam refletidas em todas as páginas onde o widget é incluído.

## Sintaxe

Os widgets criados no seu tema (que devem ser criados dentro da pasta `widets`) podem ser incluídos em qualquer parte do seu template usando a diretiva `include()` do Twig. A sintaxe básica para incluir um widget é a seguinte:

```twig
{% include('widgets/widget.html') %}
```

## Quando usar

Use a diretiva `include` para criar widgets reutilizáveis quando:

- Você tem um componente que precisa ser exibido em várias páginas do seu template, como um banner, um rodapé ou um menu de navegação.
- Você deseja manter a consistência visual em todo o seu template, garantindo que as alterações feitas em um widget sejam refletidas em todas as páginas onde ele é incluído.
- Você quer facilitar a manutenção do seu template, centralizando a lógica e o design de componentes comuns em arquivos separados, tornando mais fácil atualizar ou modificar esses componentes no futuro.
- Você está criando um template complexo e quer organizar seus arquivos de forma eficiente, mantendo os widgets em uma pasta dedicada para facilitar a navegação e a gestão do seu projeto.

## Exemplo

Suponha que você queira criar um widget de banner promocional que será exibido na página inicial e na página de categorias do seu template. Você pode criar um arquivo chamado `banner.html` dentro da pasta `widgets` com o seguinte conteúdo:

```html
<div class="banner">
  <h2>Promoção Especial!</h2>
  <p>Aproveite descontos incríveis em nossos produtos.</p>
</div>
```

Em seguida, você pode incluir esse widget em suas páginas usando a diretiva `include` do Twig. Por exemplo, na página inicial (`home.html`), você pode adicionar o seguinte código para incluir o banner:

```twig
{% include('widgets/banner.html') %}
```

E na página de categorias (`categories.html`), você também pode incluir o mesmo widget:

```twig
{% include('widgets/banner.html') %}
```

Dessa forma, o banner promocional será exibido em ambas as páginas, e qualquer alteração feita no arquivo `banner.html` será refletida automaticamente em todas as páginas onde o widget é incluído, garantindo consistência e facilitando a manutenção do seu template.

## Observações

- Certifique-se de que o caminho para o arquivo do widget esteja correto ao usar a diretiva `include`, para evitar erros de carregamento.
- Organize seus widgets em uma pasta dedicada para facilitar a navegação e a gestão do seu projeto, especialmente se você tiver muitos componentes reutilizáveis.
- Lembre-se de que as alterações feitas em um widget incluído serão refletidas em todas as páginas onde ele é utilizado, então teste suas mudanças cuidadosamente para garantir que elas não causem problemas em outras partes do seu template.

## Erros comuns

### Erro 1: "O arquivo do widget não foi encontrado"

**Problema:** O arquivo do widget que você está tentando incluir não existe ou o caminho especificado está incorreto.
**Diagnóstico:** Verifique a mensagem de erro para identificar o nome do arquivo e o caminho que está sendo procurado. Certifique-se de que o arquivo do widget realmente exista na pasta `widgets` e que o nome do arquivo esteja correto, incluindo a extensão.
**Solução:** Corrija o caminho no código de inclusão para apontar para o local correto do arquivo do widget. Por exemplo, se o widget estiver localizado em `widgets/banner.html`, certifique-se de usar `{% include('widgets/banner.html') %}`.

### Erro 2: "Erro de sintaxe no arquivo do widget"

**Problema:** O arquivo do widget contém um erro de sintaxe, como uma tag Twig malformada ou um erro de HTML.
**Diagnóstico:** Verifique o arquivo do widget para identificar qualquer erro de sintaxe. Use um editor de código com suporte para Twig e HTML para ajudar a identificar erros de sintaxe.
**Solução:** Corrija os erros de sintaxe no arquivo do widget. Certifique-se de que todas as tags Twig estejam corretamente fechadas e que o HTML esteja bem formado. Depois de corrigir os erros, teste novamente para garantir que o widget seja incluído corretamente sem erros.

## Veja também

- [Visão geral do Twig](02-twig/visao-geral-twig.md)
- [Visão geral do Store](04-store/visao-geral-store.md)
- [Configurações do tema](03-api/configuracoes-config_tema.json.md)
