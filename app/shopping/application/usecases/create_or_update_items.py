from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from shopping.application.repositories.list_repository import ListItemNotFound, ListRepository


@inject
def create_or_update_items(
    list_repository: ListRepository = Provide[
        ApplicationContainer.list_repository_container.list_respository
    ],
    list_id: int = None,
    items=None,
):
    for item in items:
        try:
            list_repository.get_list_item_by_id(id=item.id)
            list_repository.update_list_item(list_id=list_id, list_item=item)
        except ListItemNotFound:
            list_repository.create_list_item(list_id=list_id, list_item=item)

    new_items = list_repository.get_list_item_by_list(list_id=list_id)
    return new_items
