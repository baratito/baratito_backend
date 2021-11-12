from dependency_injector.wiring import Provide, inject

from auth.domain import User
from common.di.containers import ApplicationContainer
from location.application.repositories import UserLocationRepository
from location.domain import UserLocation


@inject
def create_user_location(
    user_location_repository: UserLocationRepository = Provide[
        ApplicationContainer.user_location_repository_container.user_location_respository
    ],
    user_location: UserLocation = None,
    user: User = None,
):
    locations = user_location_repository.filter(user_id=user.id)
    if len(locations) == 0:
        user_location.enable = True

    if user_location.enable:
        user_location_repository.disable_all_user_location(user_id=user.id)

    user_location = user_location_repository.create(user_location)
    return user_location
