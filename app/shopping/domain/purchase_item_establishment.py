from typing import List as Tylist
from typing import Optional

from pydantic import BaseModel
from pydantic.fields import Field

from market.domain import Establishment
from shopping.domain.purchase_list_item import PurchaseListItem


class PurchaseItemEstablishment(BaseModel):
    establishment: Establishment
    purchase_items: Tylist[PurchaseListItem] = []
