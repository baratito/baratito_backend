from abc import ABC, abstractclassmethod

from location.domain import UserLocation


class UserLocationRepository(ABC):
    @abstractclassmethod
    def filter(self, user_id, enable):
        ...

    @abstractclassmethod
    def create(self, user_location: UserLocation):
        ...
