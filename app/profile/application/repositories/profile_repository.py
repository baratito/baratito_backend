from abc import ABC, abstractmethod
from typing import List


class ProfileRepository(ABC):
    @abstractmethod
    def get_by_user_id(self, id: int):
        ...

    @abstractmethod
    def create(self, data: dict):
        ...
