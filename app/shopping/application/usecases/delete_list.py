import random

from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from shopping.application.repositories.list_repository import ListRepository


@inject
def delete_list(
    list_repository: ListRepository = Provide[
        ApplicationContainer.list_repository_container.list_respository
    ],
    user_id=None,
    list_id=None,
):
    list_obj = list_repository.delete_list(user_id=user_id, list_id=list_id)
    return list_obj
