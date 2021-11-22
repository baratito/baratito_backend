from pydantic import BaseModel
from pydantic.fields import Field


class Notification(BaseModel):
    id: int = Field(default=0)
    title: str
    content: str
    is_read: bool
    created_date: str
    user_id: int
