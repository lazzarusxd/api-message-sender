from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer

from app.core.configs import settings

credential_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Credencial inválida.",
    headers={
        "WWW-Authenticate": "Bearer",
        "Authorization": "Bearer token_value",
        "Content-Type": "application/json"
    }
)

oauth2_schema = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1}")


async def auth_api(token: str = Depends(oauth2_schema)) -> bool:
    await _validar_token_api(token)
    return True


async def _validar_token_api(token: str) -> bool:
    if token != settings.API_TOKEN:
        raise credential_exception
    return True
