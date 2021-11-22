from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer
from notification.application.repositories import NotificationRepository
from notification.domain import Notification


@inject
def read_all_notifications(
    notification_repo: NotificationRepository = Provide[
        ApplicationContainer.notification_repository_container.notification_respository
    ],
    user_id: int = None,
) -> Notification:
    return notification_repo.read_all(user_id=user_id)
