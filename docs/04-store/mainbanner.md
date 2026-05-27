---
title: "mainBanner"
slug: "mainbanner"
doc_type: "reference"
summary: "Método que retorna banners principais da loja com suporte a layouts responsivos para desktop e mobile."
tags:
  - store
  - banners
  - slides
  - carrossel
related:
  - 04-store/visao-geral-store.md
  - 04-store/publicitybanner.md
---

## O que faz

Disponibiliza como retorno os banners principais (slides) da loja virtual. Este método retorna dados de banners criados no painel de controle e oferece elementos HTML prontos para renderização.

## Sintaxe

```twig
{% set slides = store.mainBanner() %}
{# com parâmetro opcional #}
{% set slides = store.mainBanner({titulo: 'Banner especial'}) %}
```

### Retorno

```json
{
  "items": [
    {
      "id": "",
      "titulo": "",
      "foto": "",
      "foto_mobile": "",
      "link": "",
      "target": "",
      "desktop_raw": "",
      "mobile_raw": "",
      "avancado": {
        "texto": "",
        "cor_texto": "#000000"
      }
    }
  ],
  "items_per_view": 0,
  "raw": {
    "desktop": [
      ""
    ],
    "mobile": [
      ""
    ]
  },
  "width": "block"
}
```

## Quando usar

- Na página inicial para exibir banners principais
- Em seções de destaque com imagens e links
- Para criar carrosséis de imagens
- Quando precisa de banners responsivos (desktop e mobile)

## Exemplo

```twig
{% set slides = store.mainBanner() %}
{% if slides.raw|length >= 1 %}
<div class="{{ slides.width == 'block' ? 'block' : 'central' }}{{ slogan == '' ? ' mb-0' : '' }}">
	<div id="slider" class="mb-0 owl-carousel owl-theme">
		{% for slide in slides.items %}
		<div class="item">
			<div class="{{ slide.foto_mobile == '' ? 'block' : 'd-none d-md-block' }}">
				{{ slide.desktop_raw|raw }}
			</div>
			{% if slide.foto_mobile %}
			<div class="d-block d-md-none">
				{{ slide.mobile_raw|raw }}
			</div>
			{% endif %}
		</div>
		{% endfor %}
	</div>
</div>
{% endif %}
```

Saída esperada:
```
Carrossel de banners responsivos (desktop/mobile)
```

## Retorno dos dados

**items** - Array de itens (banners/slides)
- `items[x].id` (string) - ID do banner
- `items[x].titulo` (string) - Título do banner
- `items[x].foto` (string) - URL da imagem desktop
- `items[x].foto_mobile` (string) - URL da imagem mobile
- `items[x].link` (string) - URL do link do banner
- `items[x].target` (string) - Target do link (_blank, _self, etc)
- `items[x].desktop_raw` (string raw) - Imagem pronta para renderização desktop
- `items[x].mobile_raw` (string raw) - Imagem pronta para renderização mobile
- `items[x].avancado` (array) - Opções avançadas (texto, cor de texto, etc)

**items_per_view** - Int indicando quantidade de banners por visualização

**raw** - Array com elementos HTML prontos
- `raw.desktop` - Imagens prontas para desktop
- `raw.mobile` - Imagens prontas para mobile

**width** - String indicando largura ('block' = 100%, 'center' = centralizado)

## Parâmetros de consulta

| Parâmetro | Padrão | Descrição |
|-----------|---------|-------------|
| titulo | '' | Filtra pelo título do item |

## Observações

- Suporta imagens diferentes para desktop e mobile
- Os dados "*_raw" já vém preparados para inserção no HTML
- É recomendado usar OWL Carousel para melhor apresentação
- Suporta seções em formato block (100%) ou centralizado

## Erros comuns

### Erro 1: Esquecer `|raw` nos campos preparados
**Problema**: HTML de banner aparece como texto.
**Diagnóstico**: Tags renderizadas na tela.
**Solução**: Usar `{{ slide.desktop_raw|raw }}` e `{{ slide.mobile_raw|raw }}`.

### Erro 2: Renderizar sem validar retorno
**Problema**: Carrossel vazio em lojas sem banners.
**Diagnóstico**: Estrutura do slider aparece sem itens.
**Solução**: Verificar `if slides.raw|length >= 1` antes de montar o HTML.

## Veja também

- [Publicity Banner](04-store/publicitybanner.md)
- [Visão geral store](04-store/visao-geral-store.md)
