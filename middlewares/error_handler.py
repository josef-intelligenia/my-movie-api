from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from typing import Union

class ErrorHandler(BaseHTTPMiddleware):
    def __init__(self, app: FastAPI):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next) -> Union[Response, JSONResponse]:
        try:
            response = await call_next(request)
        except Exception as e:
            response = JSONResponse(status_code=500, content={"error": str(e)})
        return response
