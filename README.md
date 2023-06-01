Este é um projeto de exemplo para demonstrar um serviço de gerenciamento de postagens usando Flask. O objetivo deste projeto é fornecer uma API simples para criar, ler, atualizar e excluir postagens.

# Tecnologias Utilizadas
O projeto utiliza as seguintes tecnologias:

- Python
- Flask

# Como Usar
Siga as instruções abaixo para configurar e executar o projeto em sua máquina local.

Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

- Python (versão 3.x)
- Flask (instalado via pip) `pip install flask`

Clone o repositório para sua máquina local:
```bash
git clone <URL_DO_REPOSITORIO>
```
Navegue até o diretório do projeto:
```bash
cd apiflask
```
Inicie o servidor Flask. Execute o seguinte comando no terminal:
```bash
python main.py
```
O servidor Flask será executado na porta 7777 e estará pronto para receber solicitações.

# Endpoints da API
A API possui os seguintes endpoints disponíveis:

- `GET` / : Retorna todas as postagens.
- `GET` /postagens : Retorna todas as postagens.
- `GET` /postagens/<int:indice> : Retorna uma postagem específica com base no índice fornecido.
- `POST` /postagem : Cria uma nova postagem. Envie os dados da postagem no formato JSON no corpo da solicitação.
- `PUT` /postagem/<int:indice> : Atualiza uma postagem existente com base no índice fornecido. Envie os dados da postagem atualizada no formato JSON no corpo da solicitação.
- `DELETE` /postagem/<int:indice> : Exclui uma postagem específica com base no índice fornecido.

# Considerações Finais

Este projeto é apenas um exemplo básico para demonstrar o uso do Flask na criação de uma API de gerenciamento de postagens. Sinta-se à vontade para personalizá-lo e aprimorá-lo de acordo com suas necessidades.
