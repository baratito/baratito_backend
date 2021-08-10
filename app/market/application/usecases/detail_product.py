from common.di.containers import ApplicationContainer
from dependency_injector.wiring import Provide, inject
from market.application.repositories import ProductRepository
from market.domain import Product


@inject
def detail_product(
    product_repo: ProductRepository = Provide[
        ApplicationContainer.product_repository_container.product_respository
    ],
    id: int = 0,
) -> Product:
    print(product_repo)
    return product_repo.get_by_id(id=id)
