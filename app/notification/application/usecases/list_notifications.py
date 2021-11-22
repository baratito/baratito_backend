from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from notification.application.repositories import NotificationRepository
from notification.domain import Notification


@inject
def list_notifications(
    notification_repo: NotificationRepository = Provide[
        ApplicationContainer.notification_repository_container.notification_respository
    ],
    user_id: int = None,
) -> Notification:
    return notification_repo.list(user_id=user_id)
