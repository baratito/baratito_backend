from typing import List as Tylist

from pydantic import BaseModel
from pydantic.fields import Field


class Item(BaseModel):
    id: int = Field(default=0)
    product_id: int
    list_id: int
    quantity: int
    creation_date: str
