from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from shopping.application.repositories.list_repository import (
    ListItemNotFound, ListRepository)


@inject
def list_items(
    list_repository: ListRepository = Provide[
        ApplicationContainer.list_repository_container.list_respository
    ],
    list_id: int = None,
):
    items = list_repository.get_list_item_by_list(list_id=list_id)
    return items
