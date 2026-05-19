---
title: "Exemplo: Loop com pr() para debugar dados"
slug: "exemplo-loop-pr"
doc_type: "example"
summary: "Exemplo prático de iteração sobre arrays de produtos usando `for` combinado com `pr()` para inspecionar e entender a estrutura de dados disponível em cada item."
tags:
  - twig
  - loops
  - debug
  - exemplo
  - pr
  - for
related:
  - 02-twig/funcao-pr.md
  - 02-twig/loops-for.md
  - 02-twig/sintaxe-basica.md
  - 04-store/pageproducts.md
---

# Exemplo: Loop com pr() para debugar dados

> Este exemplo mostra como combinar loops `for` com a função `pr()` para entender a estrutura de dados de cada item enquanto itera, acelerando o desenvolvimento e reduzindo erros de template.

## O que faz

Este exemplo demonstra um **padrão prático de desenvolvimento** onde você:

1. Recupera uma coleção de dados (ex.: lista de produtos);
2. Inicia um loop `for` para iterar sobre cada item;
3. Usa `pr()` **uma vez** (fora ou no início da iteração) para visualizar a estrutura de um item;
4. Constrói o template sabendo exatamente quais campos estão disponíveis.

É especialmente útil quando você não conhece a estrutura exata de um retorno da API ou store, pois evita "tentar de adivinhação" quais campos existem.

## Sintaxe

Não há nova sintaxe aqui — é uma **combinação de dois recursos existentes**:

```twig
{% set dados = store.funcao_que_retorna_colecao() %}

{# Inspecione um item para ver a estrutura #}
{{ pr(dados[0]) }}

{# Depois, construa o loop sabendo os campos #}
{% for item in dados %}
  {# Agora você sabe quais campos usar #}
  {{ item.campo1 }}
  {{ item.campo2 }}
{% endfor %}
```

Ou, alternativamente, você pode inspecionar **dentro do loop**, na primeira iteração:

```twig
{% for item in dados %}
  {# Visualize a estrutura (remova depois) #}
  {% if loop.first %}
    {{ pr(item) }}
  {% endif %}
  
  {# Renderize normalmente #}
  {{ item.campo1 }}
{% endfor %}
```

## Quando usar

Use este padrão quando:

- você está desenvolvendo um novo template e não conhece a estrutura dos dados;
- você recebeu um retorno de API inesperado e precisa entender rapidamente quais campos existem;
- você está debugando um template que renderiza vazio ou com erro (campo não encontrado);
- você quer acelerar o desenvolvimento sem perder tempo consultando documentação de API.

Evite deixar `pr()` no código final:

- remova antes de publicar em produção (é uma ferramenta de debug);
- pode expor dados sensíveis ou poluir o HTML renderizado;
- impacta performance se usado em loops muito grandes.

## Exemplo

### Cenário: Renderizar uma vitrine de produtos

Você recebe `pageProducts` (lista de produtos) de uma página de categoria. Você não sabe exatamente quais campos cada produto possui.

- **Passo 1: Inspecione um produto para entender a estrutura**

  ```twig
  {% set vitrine = store.pageProducts %}

  {# Visualize a estrutura de um produto #}
  {{ pr(vitrine[0]) }}

  {# Resultado no navegador (exemplo):
    Array (
      [id] => 123456
      [name] => Produto Exemplo
      [description] => Descrição do produto
      [price] => Array (
        [amount] => 99.90
        [original] => 120.00
        [discount] => 20%
      )
      [image] => https://cdn.example.com/product.jpg
      [url] => /produto-exemplo
      [rating] => 4.5
      [reviews] => 150
    )
  #}
  ```

- **Passo 2: Agora que você sabe a estrutura, construa o loop**

  ```twig
  {% set vitrine = store.pageProducts %}

  <div class="vitrine">
    {% for produto in vitrine %}
      <div class="product-box">
        <img src="{{ produto.image }}" alt="{{ produto.name }}">
        <h3>{{ produto.name }}</h3>
        <p class="description">{{ produto.description }}</p>
        <span class="price">R$ {{ produto.price.amount }}</span>
        <span class="discount">{{ produto.price.discount }}</span>
        <div class="rating">{{ produto.rating }} ({{ produto.reviews }} reviews)</div>
        <a href="{{ produto.url }}" class="btn">Ver mais</a>
      </div>
    {% else %}
      <p>Nenhum produto encontrado.</p>
    {% endfor %}
  </div>
  ```

**Resultado esperado:**

- Vitrine exibindo 6-12 produtos com imagem, nome, preço e avaliação;
- Sem erros de campos inválidos (porque você conferiu com `pr()` antes);
- Template claro e sem condicionais desnecessárias.

### Padrão avançado: Inspecionar na primeira iteração apenas

```twig
{% set vitrine = store.pageProducts %}

<div class="vitrine">
  {% for produto in vitrine %}
    
    {# Remova este bloco após entender a estrutura #}
    {% if loop.first %}
      {# Inspecione apenas o primeiro item #}
      {{ pr(produto) }}
    {% endif %}

    <div class="product-box">
      <img src="{{ produto.image }}" alt="{{ produto.name }}">
      <h3>{{ produto.name }}</h3>
      <span class="price">R$ {{ produto.price.amount }}</span>
    </div>
  {% endfor %}
</div>
```

## Observações

- **Remova `pr()` antes de publicar**: é uma ferramenta de desenvolvimento. Deixar no código renderizado é um risco de segurança e impacta a experiência visual.
- **Use `pr()` uma única vez**: não é necessário chamar em cada iteração — veja a estrutura de um item, remova `pr()` e prossiga.
- **Performance**: loops com muitos itens (100+) com `pr()` renderizado ficarão muito lentos. Inspecione fora do loop ou apenas no primeiro item.
- **Cache**: se o resultado for cacheado, `pr()` pode "vazar" para usuários. Sempre remova antes do deploy.
- **Alternativas ao `pr()`**: se você tiver acesso ao código backend, consulte a documentação da API ou da função store que retorna os dados. Mas `pr()` é mais rápido durante desenvolvimento.

## Erros comuns

### Esquecer de remover `pr()` do template final

**Problema**: O site renderiza com blocos de debug visíveis.

**Diagnóstico**: Você vê blocos `<pre>` com arrays impressos no HTML da página, ou a página fica muito lenta.

**Solução**: Procure por `{{ pr(` no template e remova todas as chamadas de debug antes de publicar.

### Chamar `pr()` em cada iteração de um loop grande

**Problema**: A página fica extremamente lenta ou não carrega.

**Diagnóstico**: O loop tem 100+ itens e `pr()` é chamado para cada um (300+ linhas de output).

**Solução**: Mova `pr()` para fora do loop ou use `{% if loop.first %}` para chamar uma única vez.

### Assumir a estrutura sem conferir

**Problema**: Template renderiza vazio ou com campos inválidos.

**Diagnóstico**: Você tentou acessar `{{ produto.title }}`, mas o campo real é `{{ produto.name }}`.

**Solução**: Use `pr()` para visualizar exatamente quais campos existem. Não adivinhe.

### Confusão entre `pr()` e `dump()`

**Problema**: Você usa `dump()` e nada aparece, ou vice-versa.

**Diagnóstico**: `pr()` é específico do wBuy; `dump()` é Twig puro. A plataforma pode não ter ativado `dump()`.

**Solução**: Use `pr()` em templates wBuy. Se `pr()` não funcionar, verifique se a função está disponível na store.

## Veja também

- [Função pr()](./funcao-pr.md)
- [Loops for](./loops-for.md)
- [Sintaxe básica do Twig](./sintaxe-basica.md)
- [Page Products (pageProducts)](../04-store/pageproducts.md)
