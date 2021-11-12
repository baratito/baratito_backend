from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from market.application.repositories.establishment_repository import \
    EstablishmentRepository


@inject
def get_available_markets_count(
    establisment_repo: EstablishmentRepository = Provide[
        ApplicationContainer.establishment_repository_container.establishment_respository
    ],
    lat: float = 0,
    lng: float = 0,
    distance: float = 5,
):
    distance = distance * 1000
    return establisment_repo.nearby(lat=lat, lng=lng, distance=distance)
