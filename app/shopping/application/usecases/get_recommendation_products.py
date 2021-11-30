import random
from datetime import datetime, timedelta

from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from shopping.application.repositories.purchase_list_repository import PurchaseListRepository


@inject
def get_recommendation_products(
    purchase_list_repository: PurchaseListRepository = Provide[
        ApplicationContainer.purchase_list_repository_container.purchase_list_respository
    ],
    user_id: int = None,
):
    products = purchase_list_repository.get_all_products(user_id=user_id)

    if len(products) > 1:
        n = random.randint(0, len(products) - 1)
        n2 = random.randint(0, len(products) - 1)
        return [products[n], products[n2]]
    return products
