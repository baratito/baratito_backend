from typing import List as Tylist

from pydantic import BaseModel
from pydantic.fields import Field

from market.domain import Establishment


class PurchaseList(BaseModel):
    id: int = Field(default=0)
    name: str
    color: str
    user_id: int
    distance: float
    duration: int
    spent: float
    list_id: int
    establishments: Tylist[Establishment]
    created_date: str
