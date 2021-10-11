from typing import List

from market.application import ProductRepository
from market.domain import Product as ProductDomain
from sqlalchemy.orm import Session

from .models import CategoryProduct, Product


class ProductRepositoryImpl(ProductRepository):
    db_session: Session

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def _to_domain(self, product):
        category_id = product.categories[0].category_id if len(product.categories) else None
        product = ProductDomain(
            id=product.id,
            name=product.name,
            presentation=product.presentation,
            brand=product.brand,
            photo=product.photo,
            category=category_id,
        )
        return product

    def list_products(
        self, offset: int = 0, limit: int = 100, q: str = None, category: int = None
    ) -> List[Product]:
        query = self.db_session.query(Product)

        if q is not None:
            query = query.filter(Product.name.ilike(f"%{q}%"))

        if category is not None:
            query = query.join(CategoryProduct).filter_by(category_id=category)

        products_db = query.offset(offset).limit(limit).all()
        products = []
        for product in products_db:
            products.append(self._to_domain(product))
        return products

    def get_by_id(self, id: int) -> Product:
        product_db = self.db_session.query(Product).get(id)
        product = self._to_domain(product_db)
        return product

    def total(self) -> int:
        return self.db_session.query(Product).count()
