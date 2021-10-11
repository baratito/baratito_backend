from typing import Optional

from pydantic import BaseModel
from pydantic.fields import Field


class Product(BaseModel):
    id: int = Field(default=0)
    name: str
    presentation: str
    brand: str
    photo: Optional[str] = None
    category: Optional[int] = None
