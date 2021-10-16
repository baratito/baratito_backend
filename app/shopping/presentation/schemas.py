from typing import Optional

from pydantic.main import BaseModel


class ListCreate(BaseModel):
    name: str
    color: str
    user_id: Optional[int]


class ListItemCreate(BaseModel):
    quantity: int
    id_uuid: str
    product_id: int
    id: Optional[int] = None
