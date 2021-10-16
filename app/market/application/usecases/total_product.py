from typing import List

from common.di.containers import ApplicationContainer
from dependency_injector.wiring import Provide, inject
from market.application.repositories import ProductRepository
from market.domain import Product


@inject
def total_products(
    product_repo: ProductRepository = Provide[
        ApplicationContainer.product_repository_container.product_respository
    ],
    q: str = None,
    category: int = None,
) -> int:
    return product_repo.total(q=q, category=category)
