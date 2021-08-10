from pydantic import BaseModel
from pydantic.fields import Field


class Product(BaseModel):
    id: int = Field(default=0)
    name: str
    presentation: str
    brand: str
