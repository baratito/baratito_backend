from starlette.middleware.base import BaseHTTPMiddleware


class Chartset(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["Content-Type"] = "application/json; charset=utf-8"
        return response
