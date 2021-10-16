from abc import ABC, abstractclassmethod


class ListItemNotFound(Exception):
    ...


class ListRepository(ABC):
    @abstractclassmethod
    def create(self, list_obj):
        ...

    @abstractclassmethod
    def list(self, user_id: int):
        ...

    @abstractclassmethod
    def remove_lack_items(self, list_id, list_uuid):
        ...

    @abstractclassmethod
    def get_list_item_by_uuid(self, id_uuid):
        ...

    @abstractclassmethod
    def update_list_item(self, list_item):
        ...

    @abstractclassmethod
    def create_list_item(self, list_id, list_item):
        ...

    @abstractclassmethod
    def get_list_item_by_list(self, list_id):
        ...
