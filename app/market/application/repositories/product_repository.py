from abc import ABC, abstractmethod
from typing import List

from market.domain import Product


class ProductRepository(ABC):
    @abstractmethod
    def list_products(offset: int = 0, limit: int = 100, q: str = None) -> List[Product]:
        ...

    @abstractmethod
    def get_by_id(self, id: int):
        ...

    @abstractmethod
    def total(self):
        ...
