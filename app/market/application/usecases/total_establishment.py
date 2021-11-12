from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from market.application.repositories.establishment_repository import \
    EstablishmentRepository


@inject
def total_establishment(
    establisment_repo: EstablishmentRepository = Provide[
        ApplicationContainer.establishment_repository_container.establishment_respository
    ],
):
    return establisment_repo.total()
