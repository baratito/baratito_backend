from pydantic import BaseModel
from pydantic.fields import Field

from market.domain import Establishment, Product


class ProductPriceEstablishment(BaseModel):
    id: int = Field(default=0)
    establishment: Establishment
    product: Product
    price: int
