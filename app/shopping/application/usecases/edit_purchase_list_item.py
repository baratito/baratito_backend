from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from shopping.application.repositories.purchase_list_repository import PurchaseListRepository


@inject
def edit_purchase_list_item(
    purchase_list_repository: PurchaseListRepository = Provide[
        ApplicationContainer.purchase_list_repository_container.purchase_list_respository
    ],
    item_id: int = None,
    data=None,
):
    print(item_id)
    item = purchase_list_repository.update_purchase_list_item(item_id=item_id, data=data)

    return item
