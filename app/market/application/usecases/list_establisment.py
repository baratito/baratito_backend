from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from market.application.repositories.establishment_repository import \
    EstablishmentRepository


@inject
def list_establisment(
    establisment_repo: EstablishmentRepository = Provide[
        ApplicationContainer.establishment_repository_container.establishment_respository
    ],
    offset: int = 0,
    limit: int = 100,
):
    return establisment_repo.list(offset=offset, limit=limit)
