from abc import ABC, abstractclassmethod

from location.domain import UserLocation


class UserLocationRepository(ABC):
    @abstractclassmethod
    def filter(self, user_id, enable):
        ...

    @abstractclassmethod
    def create(self, user_location: UserLocation):
        ...

    @abstractclassmethod
    def get_by_id(self, id: int):
        ...

    @abstractclassmethod
    def enable_for_user(self, id: int, user_id: int):
        ...
