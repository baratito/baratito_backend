from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from market.domain.establishment import Establishment
from shopping.application.repositories.purchase_list_repository import PurchaseListRepository
from shopping.domain.purchase_item_establishment import PurchaseItemEstablishment
from shopping.domain.purchase_list_item import PurchaseListItem


@inject
def create_purchase_list(
    purchase_list_repository: PurchaseListRepository = Provide[
        ApplicationContainer.purchase_list_repository_container.purchase_list_respository
    ],
    purchase_list_obj=None,
    extra_data=None,
):

    purchase_list = purchase_list_repository.create(purchase_list=purchase_list_obj)

    for i, establishment in enumerate(extra_data.establishments):
        establishment_domain = Establishment(
            id=establishment.id,
            name=establishment.name,
            establishment_type=establishment.establishment_type,
            address=establishment.address,
            latitude=establishment.latitude,
            longitude=establishment.longitude,
            brand=establishment.brand,
        )
        purchase_list_repository.create_establishment_order(
            order=i, establishment_id=establishment_domain.id, purchase_list_id=purchase_list.id
        )
        purchase_item_establishment = PurchaseItemEstablishment(establishment=establishment_domain)
        for product in establishment.products:
            item = PurchaseListItem(
                name=product["product"]["name"],
                price=product["price"],
                quantity=product["quantity"],
                is_bought=False,
                product_price_id=product["product_price_id"],
                product_id=product["product_id"],
                purchase_list_id=purchase_list.id,
                establishment_id=establishment_domain.id,
            )
            purchase_list_item = purchase_list_repository.create_purchase_list(
                purchase_list_item=item
            )
            purchase_item_establishment.purchase_items.append(purchase_list_item)

        purchase_list.establishments.append(purchase_item_establishment)

    return purchase_list
