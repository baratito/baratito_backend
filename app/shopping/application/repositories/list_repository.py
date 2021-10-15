from abc import ABC, abstractclassmethod


class ListRepository(ABC):
    @abstractclassmethod
    def create(self, list_obj):
        ...
