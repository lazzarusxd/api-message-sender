from fastapi import status, HTTPException

from app.services.rabbitmq_publisher import RabbitmqPublisher
from app.schemas.message_schema import MessageRequest, MessageTypeEnum


class MessageSenderService:

    async def enviar_mensagem(mensagem: MessageRequest, exchange: str, routing_key: str, queue: str) -> dict:
        data = {}

        try:
            publisher = RabbitmqPublisher.publisher(exchange, routing_key, queue)
            if mensagem.message_type == MessageTypeEnum.SMS:
                data = {
                    "action": f"{mensagem.message_type.value} sent",
                    "data": {
                        "message_type": mensagem.message_type,
                        "to_number": mensagem.to_number,
                        "message": mensagem.message
                    }
                }
                await publisher.send_message(data)

                print(data)

            if mensagem.message_type == MessageTypeEnum.EMAIL:
                data = {
                    "action": f"{mensagem.message_type.value} sent",
                    "data": {
                        "message_type": mensagem.message_type,
                        "to_address": mensagem.to_address.upper(),
                        "subject": mensagem.subject,
                        "message": mensagem.message
                    }
                }
                await publisher.send_message(data)

        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao efetuar o envio da mensagem ao RabbitMQ."
            )

        return {
            "status_code": status.HTTP_200_OK,
            "message": f"{mensagem.message_type.value} enviado com sucesso.",
            "data": data
        }
