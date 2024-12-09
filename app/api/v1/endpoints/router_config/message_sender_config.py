from fastapi import status

from app.api.v1.endpoints.responses.message_sender_response import Responses
from app.schemas.message_schema import MessageSenderWrapper


class RouteConfig:

    @staticmethod
    def enviar_mensagem():
        return {
            "response_model": MessageSenderWrapper,
            "status_code": status.HTTP_200_OK,
            "summary": "Enviar mensagem",
            "description": "Envia uma mensagem de acordo com as informações fornecidas..",
            "responses": {
                **Responses.EnviarMensagem.sucesso_response,
                **Responses.EnviarMensagem.erros_validacao
            }
        }
