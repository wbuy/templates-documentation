---
title: "userStore"
slug: "userstore"
doc_type: "reference"
summary: "Método que retorna dados personalizados da loja do ponto de vista do usuário logado com histórico e preferências."
tags:
  - store
  - usuário
  - personalização
  - perfil
related:
  - 04-store/visao-geral-store.md
  - 04-store/customerprofiles.md
---

## O que faz

Retorna dados da loja visão do usuário. Este método oferece informações personalizadas baseadas no perfil e histórico de compras do usuario logado.

## Sintaxe

```twig
{% set user_store = store.userStore() %}
```

### Retorno

```json
{
  "logged": false,
  "data": {
    "id": 0,
    "nome": "",
    "tabela": 0,
    "credito": 0.0,
    "pontos": 0
  }
}
```

## Quando usar

- Para personalização baseada em usuário logado
- Para exibir histórico de compras
- Em áreas de cliente/minha conta
- Para ofertas personalizadas

## Exemplo

```twig
{% set user_store = store.userStore() %}
{% if user_store and user_store.usuario_id %}
<div class="user-dashboard">
	<h2>Bem-vindo, {{ user_store.nome }}!</h2>
	<p>Total de compras: {{ user_store.total_compras }}</p>
	<p>Valor gasto: R$ {{ user_store.valor_total }}</p>
	{% if user_store.ultimas_compras %}
	<h3>Últimas Compras</h3>
	<ul>
		{% for compra in user_store.ultimas_compras %}
		<li>{{ compra.titulo }} - {{ compra.data|date('d/m/Y') }}</li>
		{% endfor %}
	</ul>
	{% endif %}
</div>
{% endif %}
```

Saída esperada:
```
Dashboard personalizado do usuário com histórico
```

## Retorno dos dados

**usuario_id** (int) - ID do usuário logado

**nome** (string) - Nome do usuário

**email** (string) - Email

**total_compras** (int) - Total de pedidos realizados

**valor_total** (float) - Valor total gasto

**ultimas_compras** (array) - Array com últimos pedidos

**preferencias** (object) - Preferências do usuário

## Parâmetros de consulta

Nenhum parâmetro obrigatório.

## Observações

- Só retorna dados se usuário estiver logado
- Dados personalizados por usuário
- Excelente para fidelização de clientes
- Suporta ofertas personalizadas

## Erros comuns

### Erro 1: Acessar dados sem validar login
**Problema**: `usuario.data` não existe para visitantes.
**Diagnóstico**: `usuario.logged` é false.
**Solução**: Usar condicional antes de acessar `usuario.data`.

### Erro 2: Assumir dados completos do usuário
**Problema**: Campos como `credito` ou `pontos` nulos.
**Diagnóstico**: Loja sem programa de pontos ou crédito ativo.
**Solução**: Validar cada campo antes de exibir.

## Veja também

- [Customer Profiles](04-store/customerprofiles.md)
- [Visão geral store](04-store/visao-geral-store.md)
