from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from auth.application.repositories import UserRepository
from auth.application.repositories.user_repository import UserNotFound

from .models import User


class UserRepositoryImpl(UserRepository):
    db_session: Session

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def get_by_email(self, email: str) -> User:
        user = None
        try:
            user = self.db_session.query(User).filter_by(email=email).one()
        except NoResultFound as e:
            raise UserNotFound
        return user

    def create(self, email: str) -> User:
        user = User(email=email)
        self.db_session.add(user)
        self.db_session.commit()
        return user
