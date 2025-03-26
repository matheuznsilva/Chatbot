# CHATBOT PYTHON

Este repositório possui um chatbot feito em Python utilizando o modelo `llama3` da `Ollama`.

## Requisitos

<div>
  <img src="https://img.shields.io/badge/Python-F4D03F?style=for-the-badge&amp;logo=Python&amp;logoColor=black" alt="PYTHON">
  <img src="https://img.shields.io/badge/Llama3-3B5998?style=for-the-badge&amp;logo=Llama&amp;logoColor=black" alt="LLAMA">
</div>

## Instalação

Todas as instalações abaixo são referentes ao Ubuntu

### Instalar Python

O Python geralmente já está instalado no Ubuntu, mas você pode verificar a versão digitando:

    $ python3 --version

Se não estiver instalado ou você precisar de uma versão específica, você pode instalar usando o apt:

    $ sudo apt update
    $ sudo apt install python3

### Instalar Llama3 via Ollama

Antes de executar o chatbot, você precisa instalar o Ollama e baixar o modelo llama3.

    $ curl -fsSL https://ollama.com/install.sh | sh
    $ ollama pull llama3

### Instalar dependências do projeto

Entre no diretório do projeto e instale os pacotes necessários:

    $ cd Chatbot-Python
    $ pip install -r requirements.txt

## Uso

Entre no diretorio do projeto e execute:

    $ python3 app.py

O chatbot estará pronto para interagir. Digite suas perguntas e ele responderá de acordo com o contexto. Para encerrar, 
digite "sair".

## Status do Projeto

**Status do Projeto: Em desenvolvimento**

O projeto está funcional, mas futuras melhorias estão planejadas.

**Conquistas Atuais:**
- Funcionalidades básicas implementadas com sucesso.
<!-- 
**Melhorias Futuras**
- Adição de novos modelos de linguagem.
- Suporte para diferentes idiomas.
- Integração com outras plataformas. -->

**Desenvolvido por [Matheus N Silva]**