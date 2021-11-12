from typing import List as Tylist

from pydantic import BaseModel
from pydantic.fields import Field

from market.domain.product import Product


class ListItem(BaseModel):
    id: int = Field(default=0)
    product: Product
    list_id: int
    quantity: int
    created_date: str
