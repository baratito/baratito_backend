from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.main import Extra


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

    class Config:
        extra = Extra.allow

    def __str__(self) -> str:
        return f"{self.name}"
