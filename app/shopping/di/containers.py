from dependency_injector import containers, providers
from shopping.persistence.list_repository_impl import ListRepositoryImpl


class ListContainer(containers.DeclarativeContainer):
    db_session = providers.Dependency()
    list_respository = providers.Factory(ListRepositoryImpl, db_session=db_session)
