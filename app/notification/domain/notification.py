from typing import Optional

from pydantic import BaseModel
from pydantic.fields import Field

from market.domain import Product


class Notification(BaseModel):
    id: int = Field(default=0)
    title: str
    content: str
    is_read: bool
    created_date: str
    user_id: int
    product: Optional[Product]
