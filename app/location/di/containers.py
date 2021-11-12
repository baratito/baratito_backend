from dependency_injector import containers, providers

from location.persistence.user_location_repository_impl import \
    UserLocationRepositoryImpl


class UserLocationContainer(containers.DeclarativeContainer):
    db_session = providers.Dependency()
    user_location_respository = providers.Factory(
        UserLocationRepositoryImpl, db_session=db_session
    )
