from profile.persistence.profile_repository import ProfileRepositoryImpl

from dependency_injector import containers, providers


class ProfileContainer(containers.DeclarativeContainer):
    db_session = providers.Dependency()
    profile_respository = providers.Factory(ProfileRepositoryImpl, db_session=db_session)
