from auth.domain import User
from common.di.containers import ApplicationContainer
from dependency_injector.wiring import Provide, inject
from location.application.repositories import UserLocationRepository
from location.application.usecases.get_user_location import get_user_location
from location.domain import UserLocation


@inject
def enable_user_location(
    user_location_repository: UserLocationRepository = Provide[
        ApplicationContainer.user_location_repository_container.user_location_respository
    ],
    id: int = None,
    user: User = None,
):
    user_location = get_user_location(id=id, user=user)

    user_location_repository.enable_for_user(user_id=user.id, id=id)

    user_location.enable = True
    return user_location
