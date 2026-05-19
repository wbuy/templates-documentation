---
title: "Configurações config_tema.json"
slug: "configuracoes-config-tema-json"
doc_type: "reference"
summary: "Arquivo de configuração que define opções customizáveis do tema no painel de administração. Estrutura JSON que expõe controles para lojista (texto, número, switch, select) que podem ser acessados em templates via recursos.config_tema."
tags:
  - configuração
  - json
  - tema
  - customização
  - config_tema
  - painel
related:
  - 01-introducao/telas-customizaveis.md
  - 01-introducao/visao-geral.md
  - 04-store/getstoredata.md
---

## O que faz

O arquivo `config_tema.json` é usado para definir configurações customizáveis do tema que aparecem no painel de administração da loja. Permite ao lojista alterar valores de texto, números, switches (ativar/desativar) e selecionar entre opções predefinidas, sem necessidade de modificar código.

As configurações definidas neste arquivo são acessíveis no template via `recursos.config_tema.{var_name}`, permitindo comportamentos dinâmicos baseados nas escolhas do lojista.

## Sintaxe

Estrutura geral do arquivo `config_tema.json`:

```json
{
  "configuracoesTema": [
    {
      "type": "divider",
      "title": "Título da Seção"
    },
    {
      "var": "nomeVariavel",
      "text": "Descrição que aparece no painel",
      "type": "text|number|switch|select",
      "value": "valor_padrão"
    }
  ]
}
```

### Tipos de Campo

#### 1. **divider** — Separador visual

```json
{
  "type": "divider",
  "title": "Nome da Seção"
}
```

- Organiza campos em seções
- Se `title` não for definido, será apenas uma linha divisória

#### 2. **text** — Campo de texto

```json
{
  "var": "meuTexto",
  "text": "Descrição do campo",
  "type": "text",
  "value": "valor padrão"
}
```

- Aceita qualquer string
- `value` é o padrão quando criar novo tema

#### 3. **number** — Campo numérico

```json
{
  "var": "quantidade",
  "text": "Quantidade de items",
  "type": "number",
  "value": "10"
}
```

- Aceita apenas números
- `value` deve ser string representando número

#### 4. **switch** — Ativar/Desativar (checkbox)

```json
{
  "var": "mostrarAvaliações",
  "text": "Mostrar avaliações dos produtos",
  "type": "switch",
  "value": true
}
```

- Booleano: `true` (ativado) ou `false` (desativado)
- Renderiza como toggle no painel

#### 5. **select** — Lista com opções

```json
{
  "var": "colunas",
  "text": "Quantidade de colunas no grid",
  "type": "select",
  "options": [
    {"value": 2, "label": "Duas colunas"},
    {"value": 3, "label": "Três colunas"},
    {"value": 4, "label": "Quatro colunas"}
  ],
  "value": "3"
}
```

- Array `options` com pares `value` e `label`
- `value` define opção selecionada por padrão

## Quando usar

- **Expor opções customizáveis** para lojista sem alterar código do tema
- **Criar configurações** de aparência (cores, quantidades, textos)
- **Habilitar/desabilitar funcionalidades** via switch no painel
- **Oferecer alternativas** de comportamento via select
- Quando precisa manter **flexibilidade sem acessar código-fonte**

### Pré-condições

- Arquivo deve estar na raiz do tema: `/config_tema.json`
- JSON deve ter sintaxe válida (sem erros)
- Variáveis (`var`) devem ser válidas em Twig (sem espaços, caracteres especiais)

### Limitações

- Apenas tipos simples: text, number, switch, select (sem complexidade)
- Sem validação personalizada (apenas tipo padrão)
- Mudanças requerem reload de página/cache para aparecer

## Exemplo

**Arquivo `config_tema.json` completo:**

```json
{
  "configuracoesTema": [
    {
      "type": "divider",
      "title": "Contato"
    },
    {
      "var": "telefoneTopo",
      "text": "Telefone no topo à esquerda (deixe vazio para não exibir)",
      "type": "text",
      "value": "(11) 3000-0000"
    },
    {
      "var": "emailContato",
      "text": "Email de contato (deixe vazio para não exibir)",
      "type": "text",
      "value": "contato@loja.com.br"
    },
    {
      "type": "divider",
      "title": "Exibição de Produtos"
    },
    {
      "var": "qntColunas",
      "text": "Quantidade de produtos por linha (desktop)",
      "type": "select",
      "options": [
        {"value": 2, "label": "Dois"},
        {"value": 3, "label": "Três"},
        {"value": 4, "label": "Quatro"},
        {"value": 6, "label": "Seis"}
      ],
      "value": "4"
    },
    {
      "var": "mostrarAvaliações",
      "text": "Mostrar estrelas de avaliação nos produtos",
      "type": "switch",
      "value": true
    },
    {
      "var": "mostrarPreço",
      "text": "Mostrar preço dos produtos",
      "type": "switch",
      "value": true
    },
    {
      "type": "divider",
      "title": "Configurações Gerais"
    },
    {
      "var": "itemsPorPagina",
      "text": "Quantidade de itens por página (paginação)",
      "type": "number",
      "value": "20"
    },
    {
      "var": "mostrarMiniCarrinho",
      "text": "Mostrar mini carrinho no header",
      "type": "switch",
      "value": true
    }
  ]
}
```

**Como usar em template Twig:**

```twig
{# Arquivo: widgets/header.html #}
<header>
  {% if recursos.config_tema.telefoneTopo %}
    <div class="contact-info">
      <span class="phone">{{ recursos.config_tema.telefoneTopo }}</span>
    </div>
  {% endif %}
  
  {% if recursos.config_tema.mostrarMiniCarrinho %}
    <div class="mini-cart">
      {# Renderizar mini carrinho #}
    </div>
  {% endif %}
</header>

{# Arquivo: widgets/product-list.html #}
<div class="product-grid" 
     style="grid-template-columns: repeat({{ recursos.config_tema.qntColunas }}, 1fr);">
  {% for product in products %}
    <div class="product-item">
      <h3>{{ product.name }}</h3>
      
      {% if recursos.config_tema.mostrarAvaliações %}
        <div class="rating">
          ★★★★★ (42 avaliações)
        </div>
      {% endif %}
      
      {% if recursos.config_tema.mostrarPreço %}
        <p class="price">R$ {{ product.price|number_format(2, ',', '.') }}</p>
      {% endif %}
    </div>
  {% endfor %}
</div>
```

Saída esperada (HTML quando `telefoneTopo` e `mostrarMiniCarrinho` estão ativados):

```html
<header>
  <div class="contact-info">
    <span class="phone">(11) 3000-0000</span>
  </div>
  
  <div class="mini-cart">
    {# Conteúdo do mini carrinho #}
  </div>
</header>

<div class="product-grid" style="grid-template-columns: repeat(4, 1fr);">
  <div class="product-item">
    <h3>Camiseta</h3>
    
    <div class="rating">
      ★★★★★ (42 avaliações)
    </div>
    
    <p class="price">R$ 79,90</p>
  </div>
</div>
```

## Observações

### Performance

- `config_tema.json` é **carregado uma única vez** no bootstrap do tema
- Acessar `recursos.config_tema.{var}` tem **zero impacto de performance** (dados em memória)
- Tamanho do arquivo é negligenciável — não afeta velocidade

### Cache

- Configurações são **cacheadas durante a sessão** do usuário
- Mudanças no painel requerem **reload de página** ou **clear cache do tema**
- Usar versioning do arquivo para invalidar cache de temas em produção

### Segurança

- Nunca incluir **senhas, tokens ou API keys** neste arquivo
- Dados são públicos — visitantes podem ver valores (consultar fonte)
- Validar/sanitizar valores em Twig se vierem de entrada do lojista

### Impacto SEO e Mobile

- Configurações não afetam SEO diretamente
- Layout baseado em `qntColunas` melhora **mobile UX** quando responsivo
- Opções de exibição (mostrar preço, avaliações) não prejudicam SEO

## Erros comuns

### Erro frequente 1: "JSON inválido, configurações não carregam"

**Problema**: Arquivo tem erro de sintaxe (vírgula faltante, aspas desbalanceadas).
**Diagnóstico**: Painel de administração mostra erro ou não exibe campos. Validador JSON marca erro.
**Solução**: Validar com [JSONLint](https://jsonlint.com/). Verificar:

- Todas as propriedades entre aspas duplas
- Sem vírgula após último item
- Valores em formato correto (strings entre aspas, booleanos sem aspas)

### Erro frequente 2: "Variável não reconhecida no template"

**Problema**: `recursos.config_tema.meuCampo` retorna undefined/null em Twig.
**Diagnóstico**: Variável não está definida no `config_tema.json` ou nome está diferente.
**Solução**:

- Verificar se `var` está definido e sem typos
- Usar `{{ pr(recursos.config_tema) }}` para ver todas disponíveis
- Assegurar que nome em `var` corresponde ao acesso em Twig

### Erro frequente 3: "Valor padrão não é usado"

**Problema**: Campo aparece vazio no painel mesmo com `value` definido.
**Diagnóstico**: Pode haver valores salvos anteriormente sobrescrevendo o padrão.
**Solução**:

- Clear cache/configurações do tema no painel
- Valor padrão (`value`) é usado apenas em temas novos
- Para alterar padrão em tema existente, modificar direto no painel

## Veja também

- [Telas Customizáveis](../01-introducao/telas-customizaveis.md) — Interface de configuração no painel
- [Visão geral](../01-introducao/visao-geral.md) — Estrutura geral do projeto
- [getStoreData](../04-store/getstoredata.md) — Dados gerais da loja
