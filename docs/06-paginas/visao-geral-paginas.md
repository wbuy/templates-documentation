---
title: "Visão geral das páginas customizáveis"
slug: "visao-geral-paginas"
doc_type: "concept"
summary: "Páginas da loja que podem ser personalizadas através de templates Twig: página inicial, categorias, busca, detalhes do produto, vitrines e marcas."
tags: ["paginas", "templates", "twig", "customizacao"]
related: ["06-paginas/detalhes-do-produto.md", "06-paginas/pagina-de-busca.md", "06-paginas/pagina-de-categorias.md", "02-twig/visao-geral-twig.md"]
---

## O que faz

A plataforma wBuy permite customizar diversas páginas e telas da loja virtual através de templates desenvolvidos em HTML com a tecnologia Twig v2. Os templates são compostos por HTML, CSS e JavaScript, utilizando a engine de templates Twig para renderizar dados dinamicamente.

Atualmente, as seguintes telas são passíveis de personalização:

- Página inicial
- Página de categorias (níveis 1, 2 e 3)
- Página de busca
- Detalhes do produto
- Vitrines internas dinâmicas (rotas)
- Página de produtos de marca

Além de customizar essas páginas, é possível criar widgets separados que podem ser incluídos em qualquer parte do template através da função `include()` do Twig.

## Sintaxe

Os templates utilizam a sintaxe do Twig v2:

```twig
<ul id="navigation">
    {% for item in navigation %}
    <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}
</ul>
```

Para visualizar dados disponíveis, utilize a função `pr()`:

```twig
{{ pr(api.categoryGetAll()) }}
```

Incluir widgets no template:

```twig
{{ include('widgets/carrinho-suspenso.html') }}
```

## Quando usar

- Quando você precisa customizar a aparência e comportamento das páginas da loja
- Quando deseja criar widgets reutilizáveis para diferentes seções
- Quando necessita acessar dados da API ou store dentro dos templates
- Quando quer exibir dados dinamicamente usando loops e condicionais

## Exemplo

Exemplo básico de utilização de Twig com um loop:

```twig
<ul id="navigation">
    {% for item in navigation %}
    <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}
</ul>
```

Acessar dados da API:

```twig
{{ pr(api.categoryGetAll()) }}
```

## Observações

- Todos os arquivos devem estar em codificação ISO-8859-1 quando salvos através do wBuy Watcher
- É recomendado usar o pacote wBuy Watcher via NPM para desenvolvimento local
- A função `pr()` retorna um array de dados no formato `var_dump()` do PHP encapsulado em uma tag `<pre>`
- Widgets devem ser criados dentro do diretório Widgets
- Cada página customizável possui variáveis globais específicas que podem ser consultadas

## Erros comuns

### Erro: Arquivo não é salvo corretamente

**Problema**: O arquivo foi modificado localmente mas não aparece na loja
**Diagnóstico**: O arquivo pode estar em codificação incorreta ou o wBuy Watcher não está rodando
**Solução**: Certifique-se de que o arquivo está salvo em codificação ISO-8859-1 e que o wBuy Watcher está ativo

### Erro: Variáveis não aparecem no template

**Problema**: As variáveis que deveriam estar disponíveis não são reconhecidas
**Diagnóstico**: A variável pode não ser disponível para aquela página específica
**Solução**: Use a função `pr()` para verificar quais variáveis estão disponíveis naquela página

### Erro: Include do widget não funciona

**Problema**: A função `include()` não encontra o arquivo do widget
**Diagnóstico**: O caminho do arquivo ou o nome do diretório está incorreto
**Solução**: Verifique se o widget está no diretório correto e se o caminho no `include()` está correto

## Veja também

- [02-twig/visao-geral-twig.md](02-twig/visao-geral-twig.md)
- [01-introducao/por-onde-comecar.md](01-introducao/por-onde-comecar.md)
- [06-paginas/detalhes-do-produto.md](06-paginas/detalhes-do-produto.md)
