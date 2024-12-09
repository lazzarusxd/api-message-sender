import enum
from typing import Optional

from fastapi import HTTPException, status
from pydantic import BaseModel, EmailStr, Field, model_validator


class MessageTypeEnum(str, enum.Enum):
    SMS = "SMS"
    EMAIL = "EMAIL"


class MessageRequest(BaseModel):
    message_type: MessageTypeEnum = Field(
        title="Tipo da mensagem",
        description="Tipo da mensagem a ser enviada (SMS ou EMAIL).",
        examples=["SMS", "EMAIL"]
    )
    to_address: Optional[EmailStr] = Field(
        None,
        title="Destinatário do e-mail",
        description="Endereço de e-mail do destinatário, preenchido apenas se a mensagem for do tipo EMAIL.",
        examples=["MARIADASILVA@EMAIL.COM"]
    )
    to_number: Optional[str] = Field(
        None,
        title="Número do destinatário",
        description="Número de telefone do destinatário, preenchido apenas se a mensagem for do tipo SMS.",
        examples=["+5511987654321"]
    )
    subject: Optional[str] = Field(
        None,
        title="Assunto do e-mail",
        description="Assunto da mensagem, preenchido apenas se a mensagem for do tipo EMAIL.",
        examples=["ALTERAÇÃO DE SENHA"]
    )
    message: str = Field(
        title="Mensagem do EMAIL/SMS",
        description="Corpo do e-mail ou da mensagem SMS.",
        examples=["Sua senha foi alterada com sucesso."]
    )

    @model_validator(mode="before")
    def check_fields(cls, v):
        message_type = v.get("message_type")
        to_address = v.get("to_address")
        to_number = v.get("to_number")
        subject = v.get('subject')

        if message_type == MessageTypeEnum.SMS.value:
            if to_number is None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Para o tipo SMS, o campo 'to_number' é obrigatório."
                )
            if to_address is not None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Para o tipo SMS, o campo 'to_address' não deve ser preenchido."
                )
            if subject is not None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Para o tipo SMS, o campo 'subject' não deve ser preenchido."
                )

        elif message_type == MessageTypeEnum.EMAIL.value:
            if to_address is None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Para o tipo EMAIL, o campo 'to_address' é obrigatório."
                )
            if subject is None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Para o tipo EMAIL, o campo 'subject' é obrigatório."
                )
            if to_number is not None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Para o tipo EMAIL, o campo 'to_number' não deve ser preenchido."
                )

        return v


class Config:
        from_attributes = True


class MessageSenderWrapper(BaseModel):
    status_code: int = Field(
        title="Código HTTP",
        description="Código HTTP indicando o status da operação."
    )
    message: str = Field(
        title="Mensagem de resposta",
        description="Mensagem que descreve o resultado da operação."
    )
    data: dict = Field(
        title="Dados da mensagem",
        description="Dados da mensagem enviada."
    )
