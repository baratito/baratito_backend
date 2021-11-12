from pydantic import BaseModel
from pydantic.fields import Field


class ProductPrice(BaseModel):
    product_price_id: int = Field(default=0)
    product_id: int
    establishment_id: int
    price: float
