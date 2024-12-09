class Responses:

    class EnviarMensagem:

        sucesso_response = {
            200: {
                "description": "SMS ou E-mail enviado com sucesso.",
                "content": {
                    "application/json": {
                        "examples": {
                            "sms": {
                                "summary": "Exemplo de SMS",
                                "value": {
                                    "status_code": 200,
                                    "message": "SMS enviado com sucesso.",
                                    "data": {
                                        "action": "SMS sent",
                                        "data": {
                                            "message_type": "SMS",
                                            "to_number": "5564987654321",
                                            "message": "Senha alterada com sucesso."
                                        }
                                    }
                                }
                            },
                            "email": {
                                "summary": "Exemplo de E-mail",
                                "value": {
                                    "status_code": 200,
                                    "message": "EMAIL enviado com sucesso.",
                                    "data": {
                                        "action": "EMAIL sent",
                                        "data": {
                                            "message_type": "EMAIL",
                                            "to_address": "JOAODASILVA@EMAIL.COM",
                                            "subject": "Alteração de senha",
                                            "message": "Senha alterada com sucesso."
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }

        erros_validacao = {
            400: {
                "description": "Erro de validação (campos preenchidos incorretamente).",
                "content": {
                    "application/json": {
                        "example": {
                            "detail": [
                                "Para o tipo SMS, o campo 'to_number' é obrigatório.",
                                "Para o tipo SMS, o campo 'to_address' não deve ser preenchido.",
                                "Para o tipo SMS, o campo 'subject' não deve ser preenchido.",
                                "Para o tipo E-MAIL, o campo 'to_address' é obrigatório.",
                                "Para o tipo E-MAIL, o campo 'subject' é obrigatório.",
                                "Para o tipo E-MAIL, o campo 'to_number' não deve ser preenchido."
                            ]
                        }
                    }
                }
            }
        }
