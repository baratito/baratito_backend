from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from shopping.application.repositories.purchase_list_repository import PurchaseListRepository


@inject
def list_purchase_lists(
    purchase_list_repository: PurchaseListRepository = Provide[
        ApplicationContainer.purchase_list_repository_container.purchase_list_respository
    ],
    user_id: int = None,
    in_progress: int = None,
):
    purchases = purchase_list_repository.list(user_id=user_id, in_progress=in_progress)

    return purchases
