from auth.domain import User
from common.di.containers import ApplicationContainer
from dependency_injector.wiring import Provide, inject
from location.application.repositories import UserLocationRepository
from location.domain import UserLocation


class UserLocationForbidden(Exception):
    ...


@inject
def enable_user_location(
    user_location_repository: UserLocationRepository = Provide[
        ApplicationContainer.user_location_repository_container.user_location_respository
    ],
    id: int = None,
    user: User = None,
):
    user_location = user_location_repository.get_by_id(id=id)

    if (user_location is not None and user_location.user_id != user.id) or user_location is None:
        raise UserLocationForbidden

    user_location_repository.enable_for_user(user_id=user.id, id=id)

    user_location.enable = True
    return user_location
