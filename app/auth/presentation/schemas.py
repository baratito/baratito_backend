from pydantic.main import BaseModel


class RefreshTokenIn(BaseModel):
    refresh_token: str
