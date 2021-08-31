from auth.persistence.user_repository import UserRepositoryImpl
from dependency_injector import containers, providers


class UserContainer(containers.DeclarativeContainer):
    db_session = providers.Dependency()
    user_respository = providers.Factory(UserRepositoryImpl, db_session=db_session)
