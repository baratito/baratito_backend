from abc import ABC, abstractmethod
from typing import List

from market.domain import Category


class CategoryRepository(ABC):
    @abstractmethod
    def list() -> List[Category]:
        ...
