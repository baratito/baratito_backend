from shopping.application.repositories.list_repository import ListRepository
from shopping.domain import List as ListDomain
from sqlalchemy.orm import Session

from .models import List


class ListRepositoryImpl(ListRepository):
    db_session: Session

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def _to_domain(self, list_db):
        list_domain = ListDomain(
            id=list_db.id,
            user_id=list_db.user_id,
            name=list_db.name,
            created_date=str(list_db.created_date),
            color=list_db.color,
        )

        return list_domain

    def create(self, list_obj):
        list_db = List(name=list_obj.name, color=list_obj.color, user_id=list_obj.user_id)
        self.db_session.add(list_db)
        self.db_session.commit()
        list_obj = self._to_domain(list_db=list_db)
        return list_db

    def list(self, user_id: int):
        lists_db = self.db_session.query(List).filter_by(user_id=user_id)
        lists = []

        for list_obj in lists_db:
            lists.append(self._to_domain(list_db=list_obj))

        return lists
