from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from shopping.application.repositories.purchase_list_repository import PurchaseListRepository


@inject
def complete_purchase_list(
    purchase_list_repository: PurchaseListRepository = Provide[
        ApplicationContainer.purchase_list_repository_container.purchase_list_respository
    ],
    user_id: int = None,
    purchase_id: int = None,
):
    items = purchase_list_repository.get_items_by_purchase_id(purchase_id=purchase_id)
    spent = sum([item.price * item.quantity for item in items if item.is_bought])
    purchase = purchase_list_repository.complete(
        user_id=user_id, purchase_id=purchase_id, spent=spent
    )

    return purchase
