from typing import List as Tylist
from typing import Optional

from pydantic import BaseModel
from pydantic.fields import Field


class PurchaseListItem(BaseModel):
    id: int = Field(default=0)
    name: str
    prince: float
    quantity: int
    is_buyed: Optional[bool] = False
    purchase_list_id: int
    establishment_id: int
    photo: str
    presentation: str
