from auth.domain import User
from common.di.containers import ApplicationContainer
from dependency_injector.wiring import Provide, inject
from location.application.repositories import UserLocationRepository
from location.domain import UserLocation


@inject
def list_user_location(
    user_location_repository: UserLocationRepository = Provide[
        ApplicationContainer.user_location_repository_container.user_location_respository
    ],
    user: User = None,
):
    locations = user_location_repository.filter(user_id=user.id)
    return locations
