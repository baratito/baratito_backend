import random
from typing import List

from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from market.application.repositories import ProductRepository
from market.domain import Product
from shopping.application.usecases.get_recommendation_products import get_recommendation_products


@inject
def get_recommendations(
    product_repo: ProductRepository = Provide[
        ApplicationContainer.product_repository_container.product_respository
    ],
    user_id: int = None,
) -> List[Product]:

    products_recommendation = get_recommendation_products(user_id=user_id)

    if len(products_recommendation) > 0:
        offset = random.randint(1, 250)
        n = random.randint(1, 9)
        product = product_repo.list_products(limit=1, offset=offset, category=n)
        products_recommendation.append(product[0])
        return products_recommendation

    products = []
    for _ in range(3):
        offset = random.randint(1, 250)
        n = random.randint(1, 9)
        product = product_repo.list_products(limit=1, offset=offset, category=n)
        if len(product):
            products.append(product[0])

    return products
