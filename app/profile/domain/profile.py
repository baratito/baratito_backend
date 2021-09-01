from pydantic import BaseModel
from pydantic.fields import Field


class Profile(BaseModel):
    id: int = Field(default=0)
    email: str
    avatar: str
    first_name: str
    last_name: str
