from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from market.domain import establishment
from shopping.application.repositories.purchase_list_repository import PurchaseListRepository
from shopping.application.usecases.get_purchase_list_items import get_purchase_list_items
from shopping.domain.purchase_item_establishment import PurchaseItemEstablishment


@inject
def detail_purchase_list(
    purchase_list_repository: PurchaseListRepository = Provide[
        ApplicationContainer.purchase_list_repository_container.purchase_list_respository
    ],
    purchase_id: int = None,
):
    purchase = purchase_list_repository.get_by_id(id=purchase_id)

    items = get_purchase_list_items(purchase_id=purchase_id)
    purchase.establishments = items

    return purchase
