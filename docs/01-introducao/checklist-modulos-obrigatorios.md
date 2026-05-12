---
title: "Checklist de modulos obrigatorios"
slug: "checklist-modulos-obrigatorios"
doc_type: "concept"
summary: "Checklist de módulos obrigatórios para desenvolvimento de templates wBuy. Este documento serve como um guia para garantir que os desenvolvedores incluam todos os módulos essenciais em seus projetos de template, seguindo as melhores práticas e requisitos da plataforma wBuy."
tags:
  - checklist
  - módulos obrigatórios
  - desenvolvimento de templates
  - melhores práticas
related:
  - 01-introducao/visao-geral.md
  - 01-introducao/por-onde-comecar.md
  - 02-twig/visao-geral-twig.md
  - 03-api/visao-geral-api.md
  - 04-store/visao-geral-store.md
---

## O que faz

Este documento serve como um guia para garantir que os desenvolvedores incluam todos os módulos essenciais em seus projetos de template, seguindo as melhores práticas e requisitos da plataforma wBuy. Ele lista os módulos obrigatórios que devem estar presentes em qualquer template desenvolvido para a plataforma, garantindo assim a funcionalidade básica, a compatibilidade com os recursos da wBuy, e a aprovação do template pela equipe de revisão.

## Sintaxe

Não se aplica. Este documento é uma checklist conceitual, não possui sintaxe de código ou parâmetros específicos.

## Quando usar

Use este checklist quando:

- Você está iniciando o desenvolvimento de um template para a plataforma wBuy e quer garantir que está incluindo todos os módulos obrigatórios desde o início do projeto.
- Você quer revisar seu template antes de submetê-lo para aprovação, para garantir que todos os módulos essenciais estão presentes e configurados corretamente.
- Você quer entender quais são os módulos básicos que comppõem um template funcional na plataforma wBuy, para planejar melhor a estrutura do seu projeto e evitar omissões que possam comprometer a funcionalidade ou a aprovação do template.
- Você quer seguir as melhores práticas recomendadas pela plataforma wBuy para o desenvolvimento de templates, garantindo que seu projeto esteja alinhado com os padrões de qualidade e requisitos técnicos exigidos pela plataforma, o que pode facilitar a aprovação do template e melhorar a experiência dos usuários finais.

## Exemplo

A seguir, um exemplo de checklist de módulos obrigatórios para um template wBuy:

- Manter a Logo da plataforma wBuy (embora não faça parte do template, seria possível remover por CSS)
- Formulário para busca de produtos
- `store.getLogo()` - Logo da loja  
- `store.userStore()` - Verificação e/ou identificação do usuário logado e exibição de opções de login/cadastro ou área do cliente
- `store.cart()` - Ícone/botão para o carrinho de compras
- `store.paymentBrand()` - Ícones de formas de pagamento
- `store.securitySeal()` - Selos de segurança
- `store.footerText()` - Informações de atendimento
- `store.socialIcons()` - Icones de redes sociais
- `store.widgetNews()` - Formuláro para cadastramento na newsletter (junte-se a nós)
- `store.mainBanner()` - Banners principais (slide)
- `store.publicityBanner()` - Banners de publicidade
- `store.getSlogan()` - Slogan da loja
- `store.categories()` e/ou `store.categoriesMenu()` - Categorias/departamentos da loja
- `store.getTextTop()` - Texto para o topo da loja
- `store.dynamicPages()` - Links para páginas dinâmicas
- `store.widgetFacebook()` - Widget do Facebook
- `store.widgetInstagram()` - Widget do Instagram
- `store.periodicOffers()` - Widget de ofertas periódicas
- `store.featuredIcon()` - Widget de alertas destaque
- `store.getRatings()` - Widget de avaliações
- `store.getBrands()` - Widget de marcas
- `store.blogPosts()` - Widget de posts do Blog
- `global.var_mostruario` - Verificações sobre se a loja permite venda ou não através da variável de mostruário
- `store.showcaseActiveIds()` - Verificação se a loja tem vitrines para serem mostradas na página inicial no lugar da lista padrão de produtos
- `geral.hasSmartHint` - Indicação de locais para aparecimento das vitrines do SmartHint
- `geral.hasperformaAI` - Indicação de locais para aparecimento das vitrines do PerformaAI

## Observações

- **Atualização da checklist:** Esta checklist pode ser atualizada no futuro para incluir novos módulos obrigatórios à medida que a plataforma wBuy evolui e adiciona novos recursos. Fique atento às atualizações da documentação para garantir que seu template esteja sempre alinhado com os requisitos mais recentes da plataforma.
- **Personalização:** Embora esta checklist liste os módulos obrigatórios, os desenvolvedores têm liberdade para personalizar a aparência e a disposição desses módulos de acordo com as necessidades do projeto, desde que a funcionalidade essencial de cada módulo seja mantida e que o template continue atendendo aos requisitos de aprovação da plataforma wBuy.
**Revisão e aprovação:** A inclusão de todos os módulos obrigatórios é um critério fundamental para a aprovação do template pela equipe de revisão da plataforma wBuy. Templates que não incluírem todos os módulos listados nesta checklist podem ser rejeitados ou solicitados para ajustes antes de serem aprovados para uso na plataforma. Portanto, é essencial seguir esta checklist cuidadosamente durante o desenvolvimento do template para garantir uma aprovação tranquila e rápida. Envie seu template para revisão através do email <temas@wbuy.com.br>.

## Erros comuns

### Erro 1: Omitir um módulo obrigatório

**Problema**: Você esquece de incluir um dos módulos obrigatórios listados na checklist, o que pode levar à rejeição do template durante a revisão.
**Diagnóstico**: Revise a checklist de módulos obrigatórios e compare com os módulos incluídos no seu template para identificar qual módulo está faltando.
**Solução**: Adicione o módulo obrigatório que está faltando ao seu template, garantindo que ele esteja configurado corretamente e funcionando como esperado. Depois de fazer as correções, revise novamente a checklist para garantir que todos os módulos obrigatórios estão presentes antes de submeter o template para aprovação.

### Erro 2 - Configurar incorretamente um módulo obrigatório

**Problema**: Você inclui um módulo obrigatório, mas ele não está configurado corretamente, o que pode comprometer a funcionalidade do template ou levar à rejeição durante a revisão.
**Diagnóstico**: Teste cada módulo obrigatório para garantir que ele está funcionando corretamente e que as configurações estão de acordo com os requisitos da plataforma wBuy. Verifique a documentação de cada módulo para entender as configurações necessárias e os parâmetros que devem ser utilizados.
**Solução**: Ajuste as configurações do módulo obrigatório para garantir que ele esteja funcionando corretamente e atendendo aos requisitos da plataforma wBuy. Certifique-se de seguir as melhores práticas recomendadas na documentação para cada módulo, e teste novamente o template para garantir que todas as funcionalidades estão operando como esperado antes de submeter o template para aprovação.

## Veja também

- [Visão geral dos templates wBuy](01-introducao/visao-geral.md) — contexto geral da stack
- [Documentação de API](01-introducao/documentacao-api.md) — Recursos de API disponíveis para templates
- [Visão geral do Store](04-store/visao-geral-store.md) — dados globais disponíveis no template
- [Visão geral do Twig](02-twig/visao-geral-twig.md) — detalhes sobre o motor de templates Twig
