from typing import List

from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from market.application.repositories import ProductRepository
from market.domain import Product


@inject
def list_products(
    product_repo: ProductRepository = Provide[
        ApplicationContainer.product_repository_container.product_respository
    ],
    offset: int = 0,
    limit: int = 100,
    q: str = None,
    category: int = None,
) -> List[Product]:
    return product_repo.list_products(offset=offset, limit=limit, q=q, category=category)
