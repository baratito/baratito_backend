from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from shopping.application.repositories.list_repository import ListRepository


@inject
def remove_deleted_items(
    list_repository: ListRepository = Provide[
        ApplicationContainer.list_repository_container.list_respository
    ],
    list_id: int = None,
    item_id=None,
):
    list_repository.remove_lack_items(list_id=list_id, item_id=item_id)
