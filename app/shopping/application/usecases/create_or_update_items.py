from common.di.containers import ApplicationContainer
from dependency_injector.wiring import Provide, inject
from shopping.application.repositories.list_repository import ListItemNotFound, ListRepository


@inject
def create_or_update_items(
    list_repository: ListRepository = Provide[
        ApplicationContainer.list_repository_container.list_respository
    ],
    list_id: int = None,
    items=None,
):
    new_items = []
    for item in items:
        try:
            list_repository.get_list_item_by_uuid(id_uuid=item.id_uuid)
            new_items.append(list_repository.update_list_item(list_item=item))
        except ListItemNotFound:
            new_items.append(list_repository.create_list_item(list_id=list_id, list_item=item))
    return new_items
