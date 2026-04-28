---
title: "Taxonomia de tipos de documentos"
slug: "taxonomia-documentacao"
doc_type: "concept"
summary: "Define os quatro tipos de documentos (concept, reference, how-to, example) e como utilizá-los na documentação IA-ready."
tags:
    - documentacao
    - ia-ready
    - taxonomia
related:
    - 00-indice/sidebar.md
    - 01-introducao/como-usar-esta-documentacao.md
---

# Taxonomia de tipos de documentos

Esta documentação utiliza quatro tipos de arquivos (`doc_type`) para organizar o conhecimento de forma previsível para humanos e agentes de IA.

Cada tipo representa uma interação diferente: entender, consultar, executar ou ver um caso completo.

---

## O que faz

Define como os conteúdos da documentação são classificados em quatro categorias:

- **concept** -> explica o que é
- **reference** -> explica como funciona
- **how-to** -> ensina como fazer
- **example** -> mostra um caso real completo

Essa classificação permite que sistemas de IA filtrem e combinem conteúdos corretamente para responder perguntas com mais precisão.

---

## Sintaxe

Não se aplica. Este documento descreve uma estrutura conceitual e não possui assinatura ou parâmetros.

---

## Quando usar

Use esta taxonomia ao:

- Criar novos arquivos na documentação
- Definir o campo `doc_type` no YAML front matter
- Estruturar conteúdos de forma consistente
- Decidir se um conteúdo deve ser dividido em mais de um arquivo

---

## Exemplo

### Pergunta do usuário

"Como faço para criar um widget?"

### Como a IA usa a taxonomia

1. Busca arquivos `how-to` → `criacao-de-widgets-com-include.md`
2. Complementa com `reference` → `include-no-twig.md`
3. Pode adicionar `example` → `home-com-banners-e-vitrine.md`

Resultado: resposta completa e contextualizada.

---

## Tipos de documentos

### 1. Concept (Conceito)

**Objetivo:** explicar o que algo é e por que existe

**Características:**

- Foco em entendimento
- Pouca ou nenhuma sintaxe
- Leitura mais linear

**Exemplos:**

- `visao-geral.md`
- `visao-geral-twig.md`
- `visao-geral-store.md`

---

### 2. Reference (Referência)

**Objetivo:** documentar um recurso específico

**Características:**

- Sintaxe obrigatória
- Parâmetros e retorno
- Consulta rápida (não-linear)

**Exemplos:**

- `funcao-pr.md`
- `categorygetall.md`
- `cart.md`
- `mainbanner.md`

---

### 3. How-to (Guia prático)

**Objetivo:** ensinar como executar uma tarefa

**Características:**

- Passo a passo
- Foco em resultado
- Pode ter pré-requisitos

**Exemplos:**

- `por-onde-comecar.md`
- `criacao-de-widgets-com-include.md`
- `checklist-modulos-obrigatorios.md`

---

### 4. Example (Exemplo)

**Objetivo:** mostrar um caso completo real

**Características:**

- Integra múltiplos conceitos
- Código funcional
- Depende de referências

**Exemplos:**

- `home-com-banners-e-vitrine.md`
- `pagina-produto-com-sku.md`
- `carrinho-suspenso-assincrono.md`

---

## Observações

- Cada arquivo deve ter apenas um `doc_type`
- Evite misturar tipos no mesmo arquivo
- Se um conteúdo mistura conceito + passo a passo, divida em dois arquivos
- A taxonomia melhora a recuperação semântica e reduz respostas incorretas

---

## Erros comuns

- **Usar `concept` para tudo**  
  → dificulta busca e execução prática

- **Misturar how-to com reference**  
  → deixa o conteúdo confuso (não é nem guia nem consulta)

- **Criar exemplos sem referência**  
  → o usuário vê o código mas não entende como adaptar

---

## Veja também

- [Como usar esta documentação](../01-introducao/como-usar-esta-documentacao.md)
- [Mapa da documentação](./sidebar.md)