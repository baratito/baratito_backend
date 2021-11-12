from typing import List

from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from market.application.repositories.establishment_repository import \
    EstablishmentRepository


@inject
def get_product_prices(
    establisment_repo: EstablishmentRepository = Provide[
        ApplicationContainer.establishment_repository_container.establishment_respository
    ],
    establishment_id: id = 0,
    product_ids: List[int] = [],
):

    return establisment_repo.get_products_prices(
        establishment_id=establishment_id, product_ids=product_ids
    )
