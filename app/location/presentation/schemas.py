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


class UserLocationEdit(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    enable: Optional[bool] = None
    city: Optional[str] = None
    country: Optional[str] = None
    user_id: Optional[int] = None
