from common.persistence import get_db_session
from dependency_injector import containers, providers
from market.di import containers as market_containers


class DBSessionContainer(containers.DeclarativeContainer):
    db_session = providers.Resource(get_db_session)


class ApplicationContainer(containers.DeclarativeContainer):
    db_session_container = providers.Container(DBSessionContainer)
    product_repository_container = providers.Container(
        market_containers.ProductContainer, db_session=db_session_container.db_session
    )
