from typing import Optional

from pydantic.main import BaseModel


class ListCreate(BaseModel):
    name: str
    color: str
    user_id: Optional[int]
