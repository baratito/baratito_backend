from dependency_injector import containers, providers
from market.persistence import ProductRepositoryImpl


class ProductContainer(containers.DeclarativeContainer):
    db_session = providers.Dependency()
    product_respository = providers.Factory(ProductRepositoryImpl, db_session=db_session)
