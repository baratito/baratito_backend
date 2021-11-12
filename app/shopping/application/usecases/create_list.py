import random

from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from shopping.application.repositories.list_repository import ListRepository

LIST_COLORS = [
    "7CA9FF",
    "C9A7A7",
    "FFAAEA",
    "C8AFFF",
    "FFC0AE",
    "ABFBE5",
    "B3E3FE",
    "E5B1FD",
    "FF93B3",
]


@inject
def create_list(
    list_repository: ListRepository = Provide[
        ApplicationContainer.list_repository_container.list_respository
    ],
    list_obj=None,
):
    list_obj.color = random.choice(LIST_COLORS)
    list_obj = list_repository.create(list_obj=list_obj)
    return list_obj
