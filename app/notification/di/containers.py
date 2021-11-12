from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    db_session = providers.Dependency()
    product_respository = providers.Factory(..., db_session=db_session)
