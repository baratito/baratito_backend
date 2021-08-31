from auth.application.repositories.user_repository import UserRepository
from auth.domain import User
from common.di.containers import ApplicationContainer
from dependency_injector.wiring import Provide, inject


@inject
def get_user_by_email(
    user_repository: UserRepository = Provide[
        ApplicationContainer.user_repository_container.user_respository
    ],
    email: str = "",
) -> User:
    user = user_repository.get_by_email(email=email)
    return user
