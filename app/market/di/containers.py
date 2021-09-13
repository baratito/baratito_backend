from dependency_injector import containers, providers
from market.persistence import ProductRepositoryImpl
from market.persistence.establishment_repository_impl import EstablishmentRepositoryImpl


class ProductContainer(containers.DeclarativeContainer):
    db_session = providers.Dependency()
    product_respository = providers.Factory(ProductRepositoryImpl, db_session=db_session)


class EstablishmentContainer(containers.DeclarativeContainer):
    db_session = providers.Dependency()
    establishment_respository = providers.Factory(
        EstablishmentRepositoryImpl, db_session=db_session
    )
