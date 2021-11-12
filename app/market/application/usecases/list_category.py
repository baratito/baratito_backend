from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from market.application.repositories import CategoryRepository
from market.domain import Category


@inject
def list_category(
    category_repo: CategoryRepository = Provide[
        ApplicationContainer.category_repository_container.category_respository
    ],
) -> Category:
    return category_repo.list()
