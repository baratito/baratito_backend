from common.di.containers import ApplicationContainer
from dependency_injector.wiring import Provide, inject
from shopping.application.repositories.list_repository import ListRepository


@inject
def create_list(
    list_repository: ListRepository = Provide[
        ApplicationContainer.list_repository_container.list_respository
    ],
    list_obj=None,
):
    list_obj = list_repository.create(list_obj=list_obj)
    return list_obj
