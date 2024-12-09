from os import environ

from pydantic import BaseModel


class Settings(BaseModel):

    API_V1: str = "/api/v1"
    API_TOKEN: str = environ.get("API_TOKEN")

    class Config:
        case_sensitive = True


settings: Settings = Settings()