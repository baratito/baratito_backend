from pydantic import BaseModel
from pydantic.fields import Field


class Establishment(BaseModel):
    id: int = Field(default=0)
    name: str
    establishment_type: str
    address: str
    county: str
    latitude: float
    longitude: float
    brand: str
    external_id: str
