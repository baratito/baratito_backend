from typing import List

from market.application.repositories.category_repository import CategoryRepository
from sqlalchemy.orm import Session

from .models import Category


class CategoryRepositoryImpl(CategoryRepository):
    db_session: Session

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def list(self) -> List[Category]:
        return self.db_session.query(Category).all()

    def get_by_external_id(self, external_id: str) -> Category:
        return self.db_session.query(Category).filter_by(external_id=external_id).one()

    def create(self, name, external_id, parent_id=None):
        category = Category(name=name, external_id=external_id, parent_id=parent_id)
        self.db_session.add(category)
        self.db_session.commit()
