from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from market.domain import establishment
from shopping.application.repositories.purchase_list_repository import PurchaseListRepository
from shopping.domain.purchase_item_establishment import PurchaseItemEstablishment


@inject
def detail_purchase_list(
    purchase_list_repository: PurchaseListRepository = Provide[
        ApplicationContainer.purchase_list_repository_container.purchase_list_respository
    ],
    purchase_id: int = None,
):
    purchase = purchase_list_repository.get_by_id(id=purchase_id)

    orders = purchase_list_repository.get_establishment_order(purchase_id=purchase_id)

    for order in orders:
        items = purchase_list_repository.get_items_by_purchase_id(purchase_id=purchase_id)
        purchase_item_establishment = PurchaseItemEstablishment(
            establishment=order, purchase_items=items
        )

        purchase.establishments.append(purchase_item_establishment)

    return purchase
