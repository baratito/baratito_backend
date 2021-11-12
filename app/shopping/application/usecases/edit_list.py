from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from shopping.application.repositories.list_repository import ListRepository


@inject
def edit_list(
    list_repository: ListRepository = Provide[
        ApplicationContainer.list_repository_container.list_respository
    ],
    user_id=None,
    list_id=None,
    list_obj=None,
):
    list_obj = list_repository.edit_list(user_id=user_id, id=list_id, new_list_obj=list_obj)
    return list_obj
