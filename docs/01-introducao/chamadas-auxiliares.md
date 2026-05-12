---
title: "Chamadas auxiliares"
slug: "chamadas-auxiliares"
doc_type: "reference"
summary: "Chamadas auxiliares para desenvolvimento de templates wBuy. Este documento serve como um espaço para registrar chamadas de API, funções ou métodos que não se encaixam diretamente em outras categorias, mas são úteis para o desenvolvimento de templates personalizados na plataforma wBuy."
tags:
  - chamadas auxiliares
  - funções
  - métodos
  - API
related:
  - 01-introducao/documentacao-api.md
  - 04-store/visao-geral-store.md
  - 03-api/visao-geral-api.md
---

## O que faz

Este documento é um espaço para registrar chamadas de API, funções ou métodos que não se encaixam diretamente em outras categorias, mas são úteis para o desenvolvimento de templates personalizados na plataforma wBuy. Ele serve como um repositório de informações adicionais que podem ser relevantes para desenvolvedores, mas que não se encaixam perfeitamente em outras seções da documentação.

## Sintaxe

Para alguns eventos, você pode executar chamadas auxiliares a fim de tornar seu tema mais dinâmico. As chamadas auxiliares disponíveis atualmente são:

- **`frete_bloqueio_cep`** - Método responsável por retornar a possibilidade de entrega em um determinado CEP pela loja em questão.

  ```js
    $.post('auxiliar', {f:'frete_bloqueio_cep', cep:'87013-150'}, function(d){
      console.log(d);
    }, 'json');
  ```

  Parâmetros:
  - `f`: nome da chamada auxiliar. Neste caso, `frete_bloqueio_cep`.
  - `cep`: string obrigatória, deve conter o CEP que se deseja verificar a elegibilidade para entrega.

## Quando usar

Use chamadas auxiliares quando:

- Você precisar de uma funcionalidade auxiliar, desde que já esteja disponível na plataforma, para complementar a lógica do seu template.
- Você quiser acessar dados ou executar ações que não estão diretamente disponíveis através do objeto `store` ou das chamadas de API documentadas, mas que são oferecidas como chamadas auxiliares pela plataforma.

## Exemplo

Suponha que você queira verificar se um determinado CEP é elegível para entrega antes de permitir que o cliente prossiga com a compra. Você pode usar a chamada auxiliar `frete_bloqueio_cep` para fazer essa verificação:

```js
$.post('auxiliar', {f:'frete_bloqueio_cep', cep:'87013-150'}, function(d){
  if(d.bloqueado) {
    alert(d.mensagem); // Exibe a mensagem de bloqueio configurada no painel
  } else {
    // Permitir que o cliente prossiga com a compra
  }
}, 'json');
```

Saída esperada:

```json
{
  "bloqueado": true, // ou false, dependendo do CEP e configuração da loja
  "mensagem": "[mensagem-configurada-no-painel]", // não se aplica se não houver bloqueio
  "mensagem_html": "[mensagem-configurada-no-painel-em-html]", // não se aplica se não houver bloqueio
}
```

## Observações

- **Chamadas disponíveis:** Só estão  disponíveis para consulta as chamadas auxiliares mencionadas anteriormente. Se houver necessidade de outras chamadas auxiliares, elas devem ser solicitadas à equipe de desenvolvimento da plataforma wBuy para avaliação e possível implementação.
- **Documentação futura:** Este documento pode ser atualizado no futuro para incluir novas chamadas auxiliares à medida que forem disponibilizadas pela plataforma wBuy. Fique atento às atualizações da documentação para conhecer novas funcionalidades e chamadas auxiliares que possam ser úteis para o desenvolvimento de seus templates personalizados.

## Erros comuns

### Erro 1: Chamada a função auxiliar que não existe

**Problema**: Você tenta chamar uma função auxiliar que não está disponível na plataforma.
**Diagnóstico**: Verifique a documentação oficial e este arquivo para confirmar quais chamadas auxiliares estão disponíveis.
**Solução**: Se a funcionalidade que você precisa não estiver disponível, entre em contato com a equipe de desenvolvimento da plataforma wBuy através do email <temas@wbuy.com> para solicitar a implementação da chamada auxiliar necessária.

### Erro 2: Uso incorreto de parâmetros em chamada auxiliar

**Problema**: Você fornece parâmetros incorretos ou em formato errado para uma chamada auxiliar.
**Diagnóstico**: Leia a documentação da chamada auxiliar para entender quais parâmetros são esperados e em qual formato.
**Solução**: Ajuste os parâmetros de acordo com a documentação e teste novamente a chamada auxiliar para garantir que está funcionando corretamente.

## Veja também

- [Documentação de API](01-introducao/documentacao-api.md) — Recursos de API disponíveis para templates
- [Visão geral do Store](04-store/visao-geral-store.md) — dados globais disponíveis no template
- [Visão geral da API detalhada](03-api/visao-geral-api.md) — detalhes técnicos de cada método
