from dependency_injector import containers, providers

from notification.persistence.notification_repostory_impl import NotificationRepositoryImpl


class NotificationContainer(containers.DeclarativeContainer):
    db_session = providers.Dependency()
    notification_respository = providers.Factory(NotificationRepositoryImpl, db_session=db_session)
