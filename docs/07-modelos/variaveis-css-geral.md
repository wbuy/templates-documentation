---
title: "Variáveis CSS - Geral"
slug: "variaveis-css-geral"
doc_type: "reference"
summary: "Conjunto completo de variáveis CSS (custom properties) para personalização de cores, tamanhos e estilos gerais da loja via painel de customização rápida."
tags: ["css", "variáveis", "custom-properties", "temas", "customização"]
related:
  - 07-modelos/pagina-inicial-modelo-01.md
  - 07-modelos/topo-modelo-01.md
---

## O que faz

As variáveis CSS (custom properties) permitem que o lojista customize cores e tamanhos de elementos da loja sem precisar editar código. Definindo essas variáveis no arquivo `global.css`, o painel de customização rápida wBuy passa a exibir campos de configuração para cada uma delas.

Estas variáveis controlam aspectos globais como fontes, cores de fundo, cores de texto, tamanhos de elementos e comportamentos visuais de componentes como produtos, banners e menus.

## Implementação

Adicione as variáveis no escopo `:root` do seu arquivo `global.css`:

```css
:root {
  /* FONTS */
  --global_fonte: 'Lato', sans-serif;

  /* BACKGROUND */
  --loja_fundo: #FFF;
  --loja_fundo_imagem: inherit;

  /* MOBILE PRODUTOS */
  --mobile_produto_box_altura: 220px;
  --mobile_produto_kit_altura: 480px;

  /* MOBILE SAUDAÇÃO */
  --mobile_saudacao_fundo: #000;
  --mobile_saudacao_fundo_active: #444;
  --mobile_saudacao_texto: #FFF;
  --mobile_saudacao_texto_active: #FFF;

  /* MOBILE ATENDIMENTO */
  --mobile_atendimento_fundo: inherit;
  --mobile_atendimento_titulo: #666;
  --mobile_atendimento_texto: inherit;

  /* MOBILE MENU */
  --mobile_produto_menu_fundo: #444;
  --mobile_produto_menu_texto: #FFF;

  /* PRODUTO BOX */
  --produto_box_fundo: #FFF;
  --produto_box_fundo_hover: #F5F5F5;
  --produto_box_borda_cor: inherit;
  --produto_box_borda_cor_hover: #FFF;
  --produto_box_borda_espessura: 0px;
  --produto_box_borda_estilo: none;

  /* PRODUTO TEXTO */
  --produto_nome_cor: inherit;
  --produto_codigo_cor: inherit;
  --produto_foto_altura: 300px;
  --produto_valorpromocional_cor: inherit;
  --produto_valorfinal_cor: #F60;
  --produto_valorfinal_tamanho: 18px;
  --produto_texto_qtdminima: inherit;
  --produto_info_adicional: inherit;
  --produto_parcelamento: #666;

  /* PRODUTO LOGIN */
  --produto_login_fundo: #2BD162;
  --produto_login_texto: #FFF;

  /* PRODUTO ATACADO */
  --produto_atacado_titulo: #000;
  --produto_atacado_borda: #F60;
  --produto_atacado_valor: #000;

  /* PRODUTO DESCONTO */
  --produto_desconto_texto: #FFF;
  --produto_desconto_fundo: #F60;

  /* PRODUTO AÇÕES */
  --produto_categorias: #333;
  --produto_acao_fundo: rgba(0, 0, 0, 0.5);
  --produto_acao_olhar_fundo: rgba(0, 0, 0, 0.8);
  --produto_acao_olhar_texto: #FFF;
  --produto_acao_comprar_fundo: #F60;
  --produto_acao_comprar_texto: #FFF;
  --produto_acao_rounded: 0px;

  /* DETALHES PRODUTO */
  --detalhes_comprar_texto: #FFF;
  --detalhes_comprar_fundo: #16A326;
  --detalhes_comprar_rounded: 0px;
  --detalhes_olhar_fundo: #3E8ED8;
  --detalhes_olhar_texto: #FFF;

  /* DETALHES FRETE */
  --detalhes_frete_fundo: #FFF;
  --detalhes_frete_texto: #3E8ED8;
  --detalhes_frete_borda: #3E8ED8;

  /* DETALHES VARIAÇÃO */
  --detalhes_variacao_fundo: #b4ff95;
  --detalhes_variacao_texto: #000;

  /* DETALHES MEDIDAS */
  --detalhes_medidas_fundo: #FF0;
  --detalhes_medidas_texto: inherit;
  --detalhes_medidas_fundo_hover: #FFFF72;
  --detalhes_medidas_texto_hover: inherit;

  /* DETALHES CARRINHO */
  --detalhes_carrinho_fundo: inherit;
  --detalhes_carrinho_texto: inherit;

  /* DETALHES LAYOUT */
  --detalhes_altura_maxima_foto: inherit;

  /* TÍTULOS */
  --titulos_fundo: inherit;
  --titulos_texto: inherit;
  --titulos_tamanho: inherit;
  --titulos_alinhamento: inherit;
  --titulos_borda_altura: inherit;
  --titulos_borda_cor: inherit;

  /* WIDGETS */
  --kits_altura: 480px;

  /* BLOG WIDGET */
  --blogwidget_fundo: #EEE;
  --blogwidget_titulo_cor: inherit;
  --blogwidget_titulo_fundo: inherit;
  --blogwidget_titulo_borda: inherit;

  /* BLOG POST */
  --blogpost_fundo: #FFF;
  --blogpost_fundo_hover: #EEE;
  --blogpost_texto: #000;
  --blogpost_texto_hover: inherit;

  /* SLOGAN */
  --slogan_fundo: #000;
  --slogan_texto: #FFF;

  /* BANNERS */
  --banners_slide: inherit;
  --alertas_destaque: inherit;

  /* MODAL */
  --modal_fundo: inherit;
  --modal_texto: inherit;
}
```

## Categorias de Variáveis

### Fonte Global

| Variável | Padrão | Uso |
|----------|--------|-----|
| `--global_fonte` | Lato, sans-serif | Fonte padrão de toda a loja |

### Fundo da Loja

| Variável | Padrão | Uso |
|----------|--------|-----|
| `--loja_fundo` | #FFF | Cor de fundo principal |
| `--loja_fundo_imagem` | inherit | Imagem de fundo (URL) |

### Mobile - Produtos

| Variável | Padrão | Uso |
|----------|--------|-----|
| `--mobile_produto_box_altura` | 220px | Altura do card de produto mobile |
| `--mobile_produto_kit_altura` | 480px | Altura do kit de produto mobile |

### Mobile - Menu e Interfaces

| Variável | Padrão | Uso |
|----------|--------|-----|
| `--mobile_saudacao_fundo` | #000 | Fundo da saudação mobile |
| `--mobile_saudacao_texto` | #FFF | Cor do texto saudação |
| `--mobile_produto_menu_fundo` | #444 | Fundo do menu de produto |
| `--mobile_produto_menu_texto` | #FFF | Cor do texto do menu |

### Produto - Box

| Variável | Padrão | Uso |
|----------|--------|-----|
| `--produto_box_fundo` | #FFF | Fundo do card produto |
| `--produto_box_fundo_hover` | #F5F5F5 | Fundo ao passar mouse |
| `--produto_box_borda_cor` | inherit | Cor da borda |
| `--produto_box_borda_espessura` | 0px | Espessura da borda (px) |
| `--produto_box_borda_estilo` | none | Estilo (solid, dashed, etc) |

### Produto - Valores

| Variável | Padrão | Uso |
|----------|--------|-----|
| `--produto_valorfinal_cor` | #F60 | Cor do valor final/promocional |
| `--produto_valorfinal_tamanho` | 18px | Tamanho da fonte do valor |
| `--produto_desconto_fundo` | #F60 | Fundo do badge desconto |

### Detalhes do Produto

| Variável | Padrão | Uso |
|----------|--------|-----|
| `--detalhes_comprar_fundo` | #16A326 | Fundo do botão comprar |
| `--detalhes_olhar_fundo` | #3E8ED8 | Fundo do botão visualizar |
| `--detalhes_frete_fundo` | #FFF | Fundo da seção de frete |
| `--detalhes_variacao_fundo` | #b4ff95 | Fundo de variações disponíveis |
| `--detalhes_medidas_fundo` | #FF0 | Fundo da tabela de medidas |

### Widgets Especiais

| Variável | Padrão | Uso |
|----------|--------|-----|
| `--kits_altura` | 480px | Altura do card kit |
| `--blogwidget_fundo` | #EEE | Fundo do widget blog |
| `--blogpost_fundo` | #FFF | Fundo de post individual |
| `--slogan_fundo` | #000 | Fundo da seção slogan |

## Quando usar

- Ao customizar cores via painel wBuy Quick Customizer
- Quando se deseja manter consistência de tema em toda a loja
- Para permitir mudanças visuais sem editar código CSS
- Ao criar temas reutilizáveis

## Observações

- Variáveis CSS só funcionam em navegadores modernos (IE 11 não suporta)
- Use `inherit` para valores que devem herdar do elemento pai
- Prefira valores `#FFF` ou `#000` para cores bases
- Para gradientes, use notação CSS padrão (não como variável simples)
- As variáveis afetam todo o site, portanto teste em múltiplas páginas
- O painel de customização rápida detecta automaticamente variáveis definidas em `:root`

## Erros comuns

### Erro frequente 1

**Problema**: Variável CSS definida em `:root` não aparece no painel de customização
**Diagnóstico**: Variável não é acessível via seletores globais
**Solução**: Verificar que está em `:root` e não em escopo limitado; recarregar painel

### Erro frequente 2

**Problema**: Ao mudar variável no painel, alguns elementos não mudam cor
**Diagnóstico**: CSS inline ou especificidade alta sobrescreve a variável
**Solução**: Refatorar CSS para usar `var(--variavel)` em vez de cores diretas

## Veja também

- [07-modelos/pagina-inicial-modelo-01.md](../../07-modelos/pagina-inicial-modelo-01.md)
- [07-modelos/topo-modelo-01.md](../../07-modelos/topo-modelo-01.md)
