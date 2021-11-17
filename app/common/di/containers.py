from profile.di import containers as profile_containers

from dependency_injector import containers, providers

from auth.di import containers as auth_containers
from common.persistence import get_db_session
from location.di import containers as location_containers
from market.di import containers as market_containers
from shopping.di import containers as shopping_containers


class ApplicationContainer(containers.DeclarativeContainer):
    db_session_container = providers.Singleton(get_db_session.Database)

    user_repository_container = providers.Container(
        auth_containers.UserContainer, db_session=db_session_container.provided.session
    )

    product_repository_container = providers.Container(
        market_containers.ProductContainer, db_session=db_session_container.provided.session
    )

    profile_repository_container = providers.Container(
        profile_containers.ProfileContainer, db_session=db_session_container.provided.session
    )

    establishment_repository_container = providers.Container(
        market_containers.EstablishmentContainer, db_session=db_session_container.provided.session
    )

    category_repository_container = providers.Container(
        market_containers.CategoryContainer, db_session=db_session_container.provided.session
    )

    user_location_repository_container = providers.Container(
        location_containers.UserLocationContainer, db_session=db_session_container.provided.session
    )

    list_repository_container = providers.Container(
        shopping_containers.ListContainer, db_session=db_session_container.provided.session
    )

    purchase_list_repository_container = providers.Container(
        shopping_containers.PurchaseListContainer, db_session=db_session_container.provided.session
    )
