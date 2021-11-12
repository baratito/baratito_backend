from typing import List

from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from market.application.repositories.establishment_repository import \
    EstablishmentRepository


@inject
def get_product_price(
    establisment_repo: EstablishmentRepository = Provide[
        ApplicationContainer.establishment_repository_container.establishment_respository
    ],
    establishment_ids: List[int] = [],
    product_id: int = 0,
):

    return establisment_repo.get_product_price(
        establishment_ids=establishment_ids, product_id=product_id
    )
