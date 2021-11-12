import random

from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from shopping.application.repositories.list_repository import ListRepository


@inject
def detail_list(
    list_repository: ListRepository = Provide[
        ApplicationContainer.list_repository_container.list_respository
    ],
    list_id=None,
):
    list_obj = list_repository.get_list_by_id(id=list_id)
    return list_obj
