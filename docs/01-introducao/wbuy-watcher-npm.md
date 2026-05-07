---
title: "wBuy Watcher (NPM)"
slug: "wbuy-watcher-npm"
doc_type: "reference"
summary: "Explicação do que é o wBuy Watcher (NPM) e sua função no desenvolvimento de templates para a plataforma wBuy."
tags: ["placeholder", "pendente"]
related:
  - 01-introducao/por-onde-comecar.md
  - 01-introducao/encoding-iso-8859-1.md
  - 01-introducao/telas-customizaveis.md
---

## O que faz

O wBuy Watcher é uma ferramenta de desenvolvimento que permite a sincronização em tempo real das alterações feitas nos arquivos do template com a plataforma wBuy. Ele monitora as mudanças nos arquivos locais e atualiza automaticamente a visualização na plataforma, facilitando o processo de desenvolvimento e teste dos templates.

## Sintaxe

Comandos principais do wBuy Watcher:

- **`npm i -g wbuy-watcher`**: Instala o wBuy Watcher globalmente via NPM.
- **`wbuy configure`**: Configura o watcher para o seu projeto, com as credenciais de acesso, preenchendo o arquivo de configuração `watcher-config.json`.
- **`wbuy run`**: Inicia o watcher, permitindo que ele monitore as alterações nos arquivos do template e sincronize com a plataforma wBuy.

Variáveis de configuração no `watcher-config.json`:

- **`username`**: Seu nome de usuário da plataoforma wBuy, que se encontra em **Plataforma > API & Webhooks > Opções > Integração Rest API**.
- **`keycode`**: Sua senah de acesso à API da plataforma wBuy, que se encontra em **Plataforma > API & Webhooks > Opções > Integração Rest API**.
- **`template`**: O SKU do template que você deseja desenvolver, por exemplo: `wbuy-template-2020-01`.

```json
{
  "username": "seu_usuario",
  "keycode": "sua_senha",
  "template": "sku-do-template"
}
```

## Quando usar

**Instale e use o wBuy Watcher quando:**

- Você estiver iniciando o desenvolvimento de um template para a plataforma wBuy e deseja utilizar sua própria IDE local para editar os arquivos.
- Você quer ter uma experiência de desenvolvimento mais fluida, com atualizações em tempo real na plataforma wBuy à medida que edita os arquivos do template.
- Você precisa testar rapidamente as alterações feitas nos arquivos do template sem precisar fazer upload manual ou esperar por processos de sincronização demorados.
- Você trabalha em equipe e deseja compartilhar as mesmas credenciais de acesso para o desenvolvimento do template, garantindo que todos tenham acesso às mesmas funcionalidades do watcher.

**Pré-requisitos:**

- Node.js versão 12+ instalado em sua máquina (baixe em https://nodejs.org/).
- Credenciais de integração Rest API geradas na plataforma wBuy **(Plataforma > API e Webhooks > Integração Rest API)**.
- SKU do template obtido em **Temas > Editar código > Ações > Configurações do tema**.
- Template baixado em .zip e descompactado localmente.
- Encoding ISO-8859-1 configurado em seu editor (obrigatório).

## Exemplo

Passo a passo completo de instalação e primeira execução:

### 1. Abra o terminal e instale o Watcher globalmente

  ```sh
  npm install -g wbuy-watcher
  ```

Saída esperada:

```sh
npm notice installed [XX packages]
+ wbuy-watcher@X.X.X
added XX packages in Xs
```

### 2. Navegue até a pasta do seu template

```sh
cd ~/Documentos/meu-template-wbuy
```

### 3. Execute o comando de configuração e preencha as credenciais

wbuy configure

Saída e prompts:

```sh
? username: seu-username
? keycode: sua-keycode-secreto
? template-sku: SKU123456
✓ Arquivo salvo com sucesso!
```

### 4. Inicie o Watcher

```sh
wbuy run
```

Saída esperada (contínua durante o monitor):

```sh
$ wbuy run
✓ Escutando alterações em: /caminho/para/seu/template/
```

### 5. Edite qualquer arquivo .html e salve. O Watcher detectará automaticamente

```sh
? Salvando...
✓ change: arquivo-editado.ext 010: success
```

### 6. Acesse a plataforma no navegador e veja a mudança refletida em tempo real

## Observações

- **Sincronização contínua**: O Watcher permanece ativo no terminal e monitora continuamente. Não feche o terminal durante desenvolvimento.

- **Encoding obrigatório**: Todos os arquivos devem estar em ISO-8859-1. O Watcher pode falhar silenciosamente com UTF-8.

- **Autenticação**: Credenciais são salvas localmente em watcher-config.json. Nunca commite este arquivo em repositório público (adicione a .gitignore).

- **Performance**: Em projetos grandes com muitos arquivos, o Watcher pode levar alguns segundos para sincronizar. Isso é normal.

- **Cache**: Mudanças podem ser cacheadas pela plataforma. Use modo "Sem cache" no navegador ou incognito para garantir atualização.

- **Network**: Certifique-se de ter conexão estável com internet. O Watcher reconectará automaticamente se a conexão cair.

- **Mobile**: Teste o template em dispositivos mobile durante desenvolvimento para validar layout responsivo.

## Erros comuns

### Erro 1: "Template não sincroniza"

Problema: Você altera um arquivo e salva, mas a mudança não aparece na plataforma mesmo após 30 segundos.

Diagnóstico: O Watcher pode ter travado, a conexão caiu, ou há erro de encoding no arquivo.

Solução:

1. Verifique a saída do terminal. Se estiver parado, reinicie: Ctrl+C, depois `wbuy run`.
2. Confirme que o arquivo está em ISO-8859-1 (File > Save with Encoding em editores como VS Code).
3. Verifique se há caracteres especiais (acentos, símbolos) que ISO-8859-1 não suporte.
4. Tente fazer uma pequena alteração em um arquivo simples (como um espaço em branco) para confirmar que o monitor está ativo.
5. Verifique sua conexão de internet.

### Erro 2: "Estrutura de arquivo não reconhecida"

Problema: Você cria um novo arquivo ou renomeia uma pasta, mas o Watcher não a sincroniza.

Diagnóstico: A estrutura de diretórios ou nomeação de arquivo não segue o padrão esperado pelo template.

Solução:

1. Certifique-se de que você está usando a estrutura padrão: `assets/`, `estruturas/`, `paginas/`, `widgets/`.
2. Não renomeie ou mova pastas críticas.
3. Se criou um subdiretório customizado dentro de widgets/, confirme que o path está correto no template Twig que o referencia.

### Erro 3: Forçar a parada da execução do Watcher

Problema: Fechou o terminal ou digitou `Ctrl+C` acidentalmente, parando o Watcher.

Diagnóstico: O Watcher não está mais rodando, então nenhuma mudança será sincronizada.

Solução:

1. Abra o terminal novamente.
2. Navegue até a pasta do template: `cd ~/Documentos/meu-template-wbuy`.
3. Execute `wbuy run` para reiniciar o Watcher.

## Veja também

- [Por Onde Começar](01-introducao/por-onde-comecar.md) — Guia passo a passo para iniciar desenvolvimento.
- [Encoding ISO-8859-1](01-introducao/encoding-iso-8859-1.md) — Configuração obrigatória de encoding em arquivos.
- [Telas Customizáveis](01-introducao/telas-customizaveis.md) — Lista de páginas que suportam customização.
- [Visão Geral de Templates](01-introducao/visao-geral.md) — Panorama da stack tecnológica wBuy.
- [Sintaxe Básica do Twig](02-twig/sintaxe-basica.md) — Introdução à engine de templates Twig.