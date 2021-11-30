from sqlalchemy.orm import Session

from market.domain.product import Product
from notification.application.repositories import NotificationRepository
from notification.domain import Notification as NotificaitonDomain
from notification.domain import notification

from .models import Notification


class NotificationRepositoryImpl(NotificationRepository):
    db_session: Session

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def _to_domain(self, notification_db):
        return NotificaitonDomain(
            id=notification_db.id,
            title=notification_db.title,
            content=notification_db.content,
            is_read=notification_db.is_read,
            created_date=str(notification_db.created_date),
            user_id=notification_db.user_id,
            product=Product(
                id=notification_db.product.id,
                name=notification_db.product.name,
                presentation=notification_db.product.presentation,
                brand=notification_db.product.brand,
                photo=notification_db.product.photo,
            ),
        )

    def list(self, user_id: int):
        with self.db_session() as session:
            notifications_db = (
                session.query(Notification)
                .filter_by(user_id=user_id)
                .order_by(Notification.created_date.desc())
            )
            notifications = []

            for notification in notifications_db:
                notifications.append(self._to_domain(notification_db=notification))

        return notifications

    def read_all(self, user_id: int):
        with self.db_session() as session:
            session.query(Notification).filter_by(user_id=user_id).update({"is_read": True})
            session.commit()
        return self.list(user_id=user_id)

    def get_by_id(self, id):
        with self.db_session() as session:
            notification_db = session.query(Notification).get(id)
            return self._to_domain(notification_db=notification_db)

    def read(self, user_id: int, notification_id: int):
        with self.db_session() as session:
            session.query(Notification).filter_by(user_id=user_id, id=notification_id).update(
                {"is_read": True}
            )
            session.commit()
        return self.get_by_id(id=notification_id)
