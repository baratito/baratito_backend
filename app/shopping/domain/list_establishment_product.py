from typing import Dict
from typing import List as Tylist
from typing import Optional

from pydantic import BaseModel
from pydantic.fields import Field
from pydantic.main import Extra

from shopping.domain.establishment_products import EstablishmentProduct


class ListEstablishmentProduct(BaseModel):
    establishments: Optional[Tylist[EstablishmentProduct]] = []

    def total(self):
        return sum([establishment.total() for establishment in self.establishments])

    def total_products(self):
        return sum([len(establishment.products) for establishment in self.establishments])

    def add_establishment(self, new_establishment):
        exists = False

        for establishment in self.establishments:
            if establishment.id == new_establishment.id:
                exists = True
                break

        if not exists:
            self.establishments.append(new_establishment)

    def get_products_ids(self):
        products_id = []
        for establishment in self.establishments:
            for product in establishment.products:
                products_id.append(product["id"])
        return products_id
