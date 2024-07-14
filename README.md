# Encriptação e Desencriptação com Tkinter

Este projeto utiliza a biblioteca Tkinter para criar uma interface gráfica que permite encriptar e desencriptar mensagens utilizando base64.

## Instalação de arquivos necessários
  pip install -r requiriments.txt

## Funcionalidades

- **Encriptação:** Transforma a mensagem em um formato encriptado utilizando base64.
- **Desencriptação:** Reverte a mensagem encriptada de volta ao formato original.
- **Mensagens de Erro:** Notifica o usuário se a senha não for inserida ou estiver incorreta.

## Interface

- **Campo de Texto:** Para inserir a mensagem a ser encriptada ou desencriptada.
- **Campo de Senha:** Para inserir a senha (neste exemplo, a senha correta é '1234').
- **Botões:** Para executar as funções de encriptação, desencriptação e resetar os campos.

## Segurança

- A senha é verificada para permitir o acesso às funções de encriptação e desencriptação.

## Dependências

- `tkinter`: Para a interface gráfica.
- `base64`: Para encriptação e desencriptação das mensagens.

## Como Usar

1. Clone este repositório.
2. Execute o arquivo Python para abrir a interface gráfica.
3. Insira o texto que deseja encriptar ou desencriptar.
4. Insira a senha (a senha correta é '1234').
5. Clique no botão apropriado para encriptar ou desencriptar a mensagem.

