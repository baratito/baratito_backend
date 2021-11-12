from enum import IntEnum
from typing import List as Tylist
from typing import Optional

from pydantic import BaseModel
from pydantic.fields import Field

from shopping.domain.purchase_item_establishment import PurchaseItemEstablishment


class PurchaseListStatus(IntEnum):
    in_progress: int = 0
    completed: int = 1


class PurchaseList(BaseModel):
    id: int = Field(default=0)
    name: str
    color: str
    user_id: int
    distance: float
    duration: int
    spent: float = 0
    estimated_price: float
    list_id: int
    status: PurchaseListStatus = bool(PurchaseListStatus.in_progress)
    establishments: Optional[Tylist[PurchaseItemEstablishment]] = []
    created_date: Optional[str]
    overview_polyline: Optional[str]
