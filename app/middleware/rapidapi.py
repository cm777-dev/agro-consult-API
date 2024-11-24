from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.config import settings

class RapidAPIMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Get the RapidAPI key from headers
        rapidapi_key = request.headers.get("X-RapidAPI-Key")
        rapidapi_host = request.headers.get("X-RapidAPI-Host")

        # Skip authentication for documentation endpoints
        if request.url.path in ["/docs", "/redoc", "/openapi.json"]:
            return await call_next(request)

        # Validate RapidAPI headers
        if not rapidapi_key or not rapidapi_host:
            raise HTTPException(
                status_code=403,
                detail="RapidAPI key and host are required"
            )

        # Continue with the request
        response = await call_next(request)
        return response
