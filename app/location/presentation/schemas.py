from typing import Optional

from pydantic import BaseModel


class UserLocationCreate(BaseModel):
    name: str
    address: str
    latitude: float
    longitude: float
    enable: Optional[bool] = False
    city: Optional[str] = ""
    country: Optional[str] = ""
    user_id: Optional[int] = 0
