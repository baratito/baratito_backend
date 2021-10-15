from common.di.containers import ApplicationContainer
from dependency_injector.wiring import Provide, inject
from shopping.application.repositories.list_repository import ListRepository


@inject
def list_lists(
    list_repository: ListRepository = Provide[
        ApplicationContainer.list_repository_container.list_respository
    ],
    user_id: int = None,
):
    lists = list_repository.list(user_id=user_id)
    return lists
