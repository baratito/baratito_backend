from enum import Enum, IntEnum
from typing import Optional

from pydantic.main import BaseModel


class ListCreate(BaseModel):
    name: str
    color: Optional[str] = None
    user_id: Optional[int]


class ListEdit(BaseModel):
    name: Optional[str] = None
    color: Optional[str] = None


class ListItemCreate(BaseModel):
    quantity: int
    product_id: int
    id: Optional[int] = None


class MarketDistanceEnum(IntEnum):
    less_than_one_kilometer = 1
    less_than_five_kilometer = 5
    less_than_ten_kilometer = 10


class ModeEnum(str, Enum):
    driving = "driving"
    walking = "walking"
    bicycling = "bicycle"


class BuySetting(BaseModel):
    max_market_count: Optional[int] = 1
    max_market_distance: Optional[MarketDistanceEnum] = MarketDistanceEnum.less_than_five_kilometer
    mode: Optional[ModeEnum] = ModeEnum.driving

    class Config:
        use_enum_values = True


class PurchaseListItemEdit(BaseModel):
    is_bought: bool
