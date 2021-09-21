from typing import List

from pydantic import BaseModel
from pydantic.fields import Field


class Category(BaseModel):
    id: int = Field(default=0)
    parent: int = Field(default=0)
    name: str
    external_id: str
    sub_categories: List["Category"] = []


Category.update_forward_refs()
