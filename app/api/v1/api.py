from fastapi import APIRouter

from app.api.v1.endpoints import message_sender

router = APIRouter()

router.include_router(message_sender.router, prefix="/message_sender", tags=["Message Sender"])
