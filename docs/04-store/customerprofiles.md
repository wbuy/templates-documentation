---
title: "customerProfiles()"
slug: "customerprofiles"
doc_type: "reference"
summary: "Método que retorna perfis de clientes criados no módulo de Vitrine Personalizada de Clientes, disponível apenas para usuários logados."
tags:
  - store
  - perfis
  - clientes
  - usuário
  - vitrine-personalizada
related:
  - 04-store/visao-geral-store.md
  - 04-store/cart.md
  - 04-store/userstore.md
---

## O que faz

O método `store.customerProfiles()` recupera perfis criados pelo cliente logado no módulo de Vitrine Personalizada de Clientes. Cada perfil contém dados como nome, data de nascimento, ID da combinação, e URL direta para produtos relacionados. Essencial para criar experiências de compra personalizadas por perfil.

## Sintaxe

```twig
{% set perfis = store.customerProfiles() %}

{# Exemplo completo #}
{% if user_logado %}
  {% set perfis = store.customerProfiles() %}
{% endif %}
```

**Retorna**: Array com perfis do cliente (se logado) ou null/vazio (se não-logado)

## Quando usar

- Exibir lista de perfis criados pelo cliente
- Criar widgets de vitrine personalizada
- Oferecer botões de editar/deletar perfil
- Pré-condição: Usuário **deve estar logado**

## Exemplo

```twig
{% set perfis = store.customerProfiles() %}

{% if perfis and perfis|length > 0 %}
<div class="perfis-container">
  <h3>Meus Perfis</h3>
  {% for perfil in perfis %}
  <div class="perfil-card">
    <h4>{{ perfil.titulo }}</h4>
    <p>Data de nascimento: {{ perfil.nascimento }}</p>
    <p>Idade: {{ perfil.idade }} anos</p>
    <a href="{{ perfil.url_produtos }}" class="btn">Ver Produtos</a>
    
    <button class="btn btn-info bt-central-editar-perfil" 
            data-id="{{ perfil.id }}" 
            data-title="Editar perfil"
            data-width="400">
      Editar
    </button>
    
    <button class="btn btn-danger bt-central-excluir-perfil" 
            data-id="{{ perfil.id }}">
      Excluir
    </button>
  </div>
  {% endfor %}
</div>
{% else %}
<p>Você ainda não criou nenhum perfil.</p>
{% endif %}
```

Saída esperada:
```html
<div class="perfis-container">
  <h3>Meus Perfis</h3>
  <div class="perfil-card">
    <h4>Minha Filha</h4>
    <p>Data de nascimento: 2018-05-15</p>
    <p>Idade: 5 anos</p>
    <a href="...">Ver Produtos</a>
  </div>
</div>
```

## Observações

- Retorna `null` ou array vazio se usuário não está logado
- Dados do perfil incluem combinação para produtos recomendados
- Classes CSS `bt-central-editar-perfil` e `bt-central-excluir-perfil` são hooks para ações
- A idade é calculada automaticamente
- Perfis são gerenciados via painel do cliente

## Erros comuns

### Erro 1: Não verificar se usuário está logado
**Problema**: `customerProfiles()` retorna vazio/null em usuário não-logado
**Diagnóstico**: Template tenta acessar dados inexistentes
**Solução**: Verificar `if perfis and perfis|length > 0`

### Erro 2: Classe CSS incorreta para botões
**Problema**: `bt-editar-perfil` em vez de `bt-central-editar-perfil`
**Diagnóstico**: Botão não funciona
**Solução**: Usar exatamente: `bt-central-editar-perfil` e `bt-central-excluir-perfil`

### Erro 3: Não passar `data-id` nos botões
**Problema**: Botão de ação sem identificar qual perfil atualizar
**Diagnóstico**: Sistema não sabe qual perfil editar
**Solução**: Sempre incluir `data-id="{{ perfil.id }}"`

## Veja também

- [Visão geral store](04-store/visao-geral-store.md)
- [Cart](04-store/cart.md)
- [UserStore](04-store/userstore.md)
