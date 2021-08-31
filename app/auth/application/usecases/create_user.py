from auth.application.repositories.user_repository import UserRepository
from common.di.containers import ApplicationContainer
from dependency_injector.wiring import Provide, inject


@inject
def create_user(
    user_repository: UserRepository = Provide[
        ApplicationContainer.user_repository_container.user_respository
    ],
    email: str = "",
):
    user = user_repository.create(email)
    return user
