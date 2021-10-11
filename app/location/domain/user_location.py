from pydantic import BaseModel
from pydantic.fields import Field


class UserLocation(BaseModel):
    id: int = Field(default=0)
    name: str
    address: str
    latitude: float
    longitude: float
    enable: bool
    city: str
    country: str
    user_id: int
