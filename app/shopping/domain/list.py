from typing import List as Tylist

from pydantic import BaseModel
from pydantic.fields import Field


class List(BaseModel):
    id: int = Field(default=0)
    name: str
    color: str
    created_date: str
    user_id: int
