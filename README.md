# API - Envio de Mensagens

## Descrição

A API é uma solução para o envio de mensagens utilizando filas de processamento assíncrono. Ela utiliza RabbitMQ para gerenciar as mensagens, que podem ser enviadas via e-mail ou SMS. Esta API é um microsserviço responsável apenas por publicar as mensagens nas filas de processamento. A lógica de consumo das filas, como o envio real das mensagens, deve ser implementada separadamente.

## Funcionalidades

- **Envio de Mensagens:** Permite o envio de mensagens para um destinatário específico. As mensagens são enfileiradas no RabbitMQ para processamento assíncrono e posterior consumo.

## Segurança e Autenticação

A autenticação na API é realizada através de um token JWT. O token recebido na requisição é comparado com o valor armazenado no arquivo ".env" (API_TOKEN). Apenas usuários que fornecerem o token correto terão acesso aos recursos protegidos da API.

## Estrutura do Projeto

```plaintext
api-message-sender/
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── responses/
│   │   │   │   │   └── message_sender_response.py
│   │   │   │   ├── router_config/
│   │   │   │   │   └── message_sender_config.py
│   │   │   │   └── message_sender.py
│   │   │   └── api.py
│   ├── core/
│   │   ├── auth.py
│   │   └── configs.py
│   ├── schemas/
│   │   └── message_schema.py
│   ├── services/
│   │   ├── message_sender_service.py
│   │   └── rabbitmq_publisher.py
│   └── main.py
├── .gitignore
├── Dockerfile
├── README.md
├── docker-compose.yml
└── pyproject.toml
```

## Como Usar

1- Clone este repositório:
   ```bash
   git clone https://github.com/lazzarusxd/api-message-sender.git
   ```


2- Navegue até o diretório do projeto:
   ```bash
   cd api-message-sender
   ```


3- Configure o arquivo ".env":
- Crie um arquivo ".env" na raiz do projeto, contendo as váriaveis necessárias:
   ```bash
    RABBITMQ_DEFAULT_USER=seu_user
    RABBITMQ_DEFAULT_PASS=sua_senha
    RABBITMQ_HOST=container_rabbitmq
    RABBITMQ_PORT=porta_rabbitmq
    API_TOKEN=token único para todo o projeto, deve ser obrigatoriamente do tipo JWT.
   ```


4- Crie seu ambiente de desenvolvimento e instale as dependências usando Poetry:
   ```bash
   poetry install
   ```


5- Execute seu ambiente de desenvolvimento com as dependências usando Poetry:
   ```bash
   poetry shell
   ```


6- Configure o interpretador Python na sua IDE:
- Caso seu ambiente de desenvolvimento tenha sido criado no WSL, selecione-o e escolha a opção "System Interpreter".
  
- Navegue até o diretório retornado no terminal após a execução do comando do Passo 5.
  
- Procure o executável do Python dentro do ambiente virtual.


7- Crie e execute os containers Docker necessários:
   ```bash
   docker-compose up --build
   ```


8- Realize a requisição conforme próximo tópico (Endpoints):
   - O arquivo ".env" deve ser solicitado ou configurado na raiz do projeto, conforme as necessidades da API.
     
   - Verifique as portas corretas dos serviços utilizando o aplicativo Docker Desktop ou o comando:

      ```bash
      docker ps
      ```


## Endpoints

### **Enviar Mensagem (requer autenticação)**:

- ***Rota***: POST /api/v1/message_sender/send
- ***Descrição***: Envia uma mensagem (sms ou e-mail) para o destinatário especificado.

**Exemplo de entrada:**

**SMS:**

```plaintext
{
  "message_type": "SMS",
  "to_number": "+5564987654321",
  "message": "Sua senha foi alterada com sucesso."
}
```

**EMAIL:**

```plaintext
{
  "message_type": "EMAIL",
  "to_address": "MARIADASILVA@EMAIL.COM",
  "subject": "ALTERAÇÃO DE SENHA",
  "message": "Sua senha foi alterada com sucesso."
}
```

**Exemplo de resposta bem sucedida:**

**SMS:**

```plaintext
{
  "status_code": 200,
  "message": "SMS enviado com sucesso.",
  "data": {
    "action": "SMS sent",
    "content": {
      "message_type": "SMS",
      "to_number": "5564987654321",
      "message": "Senha alterada com sucesso."
    }
  }
}
```

**EMAIL:**

```plaintext
{
  "status_code": 200,
  "message": "EMAIL enviado com sucesso.",
  "data": {
    "action": "EMAIL sent",
    "content": {
      "message_type": "EMAIL",
      "to_address": "JOAODASILVA@EMAIL.COM",
      "subject": "Alteração de senha",
      "message": "Senha alterada com sucesso."
    }
  }
}
```


### **Possíveis Erros**:

- ***400***: Erros de validação (campos preenchidos incorretamente).
- ***422***: Erros relacionados a parâmetros enviados.
- ***500***: Erro interno do servidor ao processar a requisição.


## Contato:

João Lázaro - joaolazarofera@gmail.com

Link do projeto - https://github.com/lazzarusxd/api-message-sender
