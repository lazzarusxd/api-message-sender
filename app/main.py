from dotenv import load_dotenv
from fastapi import FastAPI

from app.core.configs import settings
from app.api.v1.api import router

load_dotenv()

app = FastAPI(
    title="API de Envio de Mensagens",
    description="""API responsável pelo envio de mensagens através de filas de processamento assíncrono, utilizando RabbitMQ para o gerenciamento.""",
    version="1.0"
)

app.include_router(router, prefix=settings.API_V1)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8001, log_level="debug", reload=True)
