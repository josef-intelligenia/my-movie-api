from fastapi import HTTPException
from fastapi.security import HTTPBearer
from fastapi.requests import Request
from utils.jwt_manager import decode_token


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = decode_token(auth.credentials)
        if data['username'] != 'admin':
            raise HTTPException(status_code=401, detail="Unauthorized")
