from typing import List as Tylist
from typing import Optional

from pydantic import BaseModel
from pydantic.fields import Field


class PurchaseListItem(BaseModel):
    id: int = Field(default=0)
    name: str
    price: float
    quantity: int
    is_buyed: Optional[bool] = False
    product_price_id: int
    product_id: int
    purchase_list_id: int
    establishment_id: int
