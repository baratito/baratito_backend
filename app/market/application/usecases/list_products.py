from typing import List

from common.di.containers import ApplicationContainer
from dependency_injector.wiring import Provide, inject
from market.application.repositories import ProductRepository
from market.domain import Product


@inject
def list_products(
    product_repo: ProductRepository = Provide[
        ApplicationContainer.product_repository_container.product_respository
    ],
    offset: int = 0,
    limit: int = 100,
) -> List[Product]:
    return product_repo.list_products(offset=offset, limit=limit)
