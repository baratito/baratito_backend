from dependency_injector.wiring import Provide, inject

from auth.domain import User
from common.di.containers import ApplicationContainer
from location.application.repositories import UserLocationRepository
from location.domain import UserLocation


@inject
def get_enable_location(
    user_location_repository: UserLocationRepository = Provide[
        ApplicationContainer.user_location_repository_container.user_location_respository
    ],
    user_id: int = None,
):
    user_location = user_location_repository.get_enable_location_by_user(user_id=user_id)
    return user_location
