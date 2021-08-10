from abc import ABC, abstractmethod
from typing import List

from market.domain import Product


class ProductRepository(ABC):
    @abstractmethod
    def list_products(offset: int = 0, limit: int = 100) -> List[Product]:
        ...
