from typing import Dict
from typing import List as Tylist
from typing import Optional

from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.main import Extra


class EstablishmentProduct(BaseModel):
    id: int = Field(default=0)
    name: str
    establishment_type: str
    address: str
    latitude: float
    longitude: float
    products: Optional[Tylist[Dict]] = []

    def total(self):
        return sum([product["total"] for product in self.products])

    def remove_duplicate(self):
        self.products = list({product["id"]: product for product in self.products}.values())

    def remove_product(self, product_id):
        self.products = list(
            {
                product["id"]: product
                for product in self.products
                if product["product_id"] != product_id
            }.values()
        )
