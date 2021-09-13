from abc import ABC, abstractmethod
from typing import List

from market.domain.establishment import Establishment


class EstablishmentRepository(ABC):
    @abstractmethod
    def list(offset: int = 0, limit: int = 100) -> List[Establishment]:
        ...
