from dependency_injector import containers, providers

from shopping.persistence.list_repository_impl import ListRepositoryImpl
from shopping.persistence.purchase_list_impl import PurchaseListRepositoryImpl


class ListContainer(containers.DeclarativeContainer):
    db_session = providers.Dependency()
    list_respository = providers.Factory(ListRepositoryImpl, db_session=db_session)


class PurchaseListContainer(containers.DeclarativeContainer):
    db_session = providers.Dependency()
    purchase_list_respository = providers.Factory(
        PurchaseListRepositoryImpl, db_session=db_session
    )
