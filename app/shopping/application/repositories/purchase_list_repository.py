from abc import ABC, abstractclassmethod

from shopping.domain.purchase_list import PurchaseList
from shopping.domain.purchase_list_item import PurchaseListItem


class PurchaseListRepository(ABC):
    @abstractclassmethod
    def create(self, purchase_list: PurchaseList):
        ...

    @abstractclassmethod
    def create_purchase_list(self, purchase_list_item: PurchaseListItem):
        ...

    @abstractclassmethod
    def list(self, user_id, in_progress: int = None):
        ...

    @abstractclassmethod
    def create_establishment_order(self, order, establishment_id, purchase_list_id):
        ...
