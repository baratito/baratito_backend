from pydantic import BaseModel
from pydantic.fields import Field


class Category(BaseModel):
    id: int = Field(default=0)
    parent: int = Field(default=0)
    name: str
    external_id: str
