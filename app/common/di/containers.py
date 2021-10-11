from profile.di import containers as profile_containers

from auth.di import containers as auth_containers
from common.persistence import get_db_session
from dependency_injector import containers, providers
from location.di import containers as location_containers
from market.di import containers as market_containers


class DBSessionContainer(containers.DeclarativeContainer):
    db_session = providers.Resource(get_db_session)


class ApplicationContainer(containers.DeclarativeContainer):
    db_session_container = providers.Container(DBSessionContainer)

    user_repository_container = providers.Container(
        auth_containers.UserContainer, db_session=db_session_container.db_session
    )

    product_repository_container = providers.Container(
        market_containers.ProductContainer, db_session=db_session_container.db_session
    )

    profile_repository_container = providers.Container(
        profile_containers.ProfileContainer, db_session=db_session_container.db_session
    )

    establishment_repository_container = providers.Container(
        market_containers.EstablishmentContainer, db_session=db_session_container.db_session
    )

    category_repository_container = providers.Container(
        market_containers.CategoryContainer, db_session=db_session_container.db_session
    )

    user_location_repository_container = providers.Container(
        location_containers.UserLocationContainer, db_session=db_session_container.db_session
    )
