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
