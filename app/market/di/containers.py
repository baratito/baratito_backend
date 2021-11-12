from typing import Container

from dependency_injector import containers, providers

from market.persistence import ProductRepositoryImpl
from market.persistence.category_repository_impl import CategoryRepositoryImpl
from market.persistence.establishment_repository_impl import \
    EstablishmentRepositoryImpl


class ProductContainer(containers.DeclarativeContainer):
    db_session = providers.Dependency()
    product_respository = providers.Factory(ProductRepositoryImpl, db_session=db_session)


class EstablishmentContainer(containers.DeclarativeContainer):
    db_session = providers.Dependency()
    establishment_respository = providers.Factory(
        EstablishmentRepositoryImpl, db_session=db_session
    )


class CategoryContainer(containers.DeclarativeContainer):
    db_session = providers.Dependency()
    category_respository = providers.Factory(CategoryRepositoryImpl, db_session=db_session)
