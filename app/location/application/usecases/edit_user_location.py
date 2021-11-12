from dependency_injector.wiring import Provide, inject

from auth.domain import User
from common.di.containers import ApplicationContainer
from location.application.repositories import UserLocationRepository
from location.application.usecases.get_user_location import get_user_location


@inject
def edit_user_location_usecase(
    user_location_repository: UserLocationRepository = Provide[
        ApplicationContainer.user_location_repository_container.user_location_respository
    ],
    id: int = 0,
    user: User = None,
    user_location=None,
):
    get_user_location(id=id, user=user)

    location = user_location_repository.edit(id, user.id, user_location)
    return location
