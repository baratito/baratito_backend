from typing import List

from sqlalchemy.orm import Session

from market.application.repositories.category_repository import \
    CategoryRepository
from market.domain import Category as CategoryDomain

from .models import Category


class CategoryRepositoryImpl(CategoryRepository):
    db_session: Session

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def _to_domain(self, categories_db):
        categories = []

        for category in categories_db:
            categories.append(
                CategoryDomain(
                    id=category.id,
                    name=category.name,
                    external_id=category.external_id,
                    parent_id=category.parent_id,
                    sub_categories=self._to_domain(category.sub_categories),
                )
            )
        return categories

    def list(self) -> List[Category]:
        categories_db = self.db_session.query(Category).filter_by(parent_id=None).all()
        categories = self._to_domain(categories_db=categories_db)
        return categories

    def get_by_external_id(self, external_id: str) -> Category:
        return self.db_session.query(Category).filter_by(external_id=external_id).one()

    def create(self, name, external_id, parent_id=None):
        category = Category(name=name, external_id=external_id, parent_id=parent_id)
        self.db_session.add(category)
        self.db_session.commit()
