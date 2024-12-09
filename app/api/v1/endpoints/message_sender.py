from fastapi import APIRouter, Depends

from app.core.auth import auth_api
from app.services.message_sender_service import MessageSenderService
from app.schemas.message_schema import MessageRequest, MessageSenderWrapper, MessageTypeEnum
from app.api.v1.endpoints.router_config.message_sender_config import RouteConfig

router = APIRouter()


@router.post("/send", **RouteConfig.enviar_mensagem())
async def enviar_mensagem(mensagem: MessageRequest, _auth: auth_api = Depends()) -> MessageSenderWrapper:
    routing_key, queue = None, None
    if mensagem.message_type == MessageTypeEnum.SMS:
        routing_key, queue = "sms_rk", "sms_queue"
    if mensagem.message_type == MessageTypeEnum.EMAIL:
        routing_key, queue = "email_rk", "email_queue"
        mensagem.to_address.upper()


    mensagem_response = await MessageSenderService.enviar_mensagem(
        mensagem=mensagem,
        exchange="message_exchange",
        routing_key=routing_key,
        queue=queue
    )

    return MessageSenderWrapper(
        status_code=mensagem_response["status_code"],
        message=mensagem_response["message"],
        data=mensagem_response["data"]
    )
