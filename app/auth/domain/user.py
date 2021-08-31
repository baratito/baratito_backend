from pydantic import BaseModel
from pydantic.fields import Field


class User(BaseModel):
    id: int = Field(default=0)
    email: str = None
