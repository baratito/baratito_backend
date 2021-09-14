from typing import List

from market.application import ProductRepository
from sqlalchemy.orm import Session

from .models import Product


class ProductRepositoryImpl(ProductRepository):
    db_session: Session

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def list_products(self, offset: int = 0, limit: int = 100, q: str = None) -> List[Product]:
        query = self.db_session.query(Product)

        if q is not None:
            query = query.filter(Product.name.ilike(f"%{q}%"))

        return query.offset(offset).limit(limit).all()

    def get_by_id(self, id: int) -> Product:
        return self.db_session.query(Product).get(id)

    def total(self) -> int:
        return self.db_session.query(Product).count()
