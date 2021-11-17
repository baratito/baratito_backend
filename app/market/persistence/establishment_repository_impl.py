from typing import List

from geoalchemy2 import func
from sqlalchemy.orm.session import Session

from market.application.repositories.establishment_repository import EstablishmentRepository
from market.domain import Establishment, ProductPrice
from market.domain.product import Product
from market.domain.product_price_establishment import ProductPriceEstablishment
from market.persistence.models import Establishment as EstablishmentModel
from market.persistence.models import Product as ProductModel
from market.persistence.models import ProductPrice as ProductPriceModel


class EstablishmentRepositoryImpl(EstablishmentRepository):
    db_session: Session

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def _to_domain(self, establishment_db):
        establishments = []

        for establishment in establishment_db:
            establishments.append(
                Establishment(
                    id=establishment.id,
                    name=establishment.name,
                    establishment_type=establishment.establishment_type,
                    address=establishment.address,
                    county=establishment.county,
                    latitude=establishment.latitude,
                    longitude=establishment.longitude,
                    brand=establishment.brand,
                    external_id=establishment.external_id,
                )
            )
        return establishments

    def _to_domain_price(self, price_db):
        price = ProductPrice(
            product_price_id=price_db.id,
            product_id=price_db.product_id,
            establishment_id=price_db.establishment_id,
            price=price_db.price,
        )

        return price

    def _to_domain_price_establishment(self, price_db, establishment, product):
        price = ProductPriceEstablishment(
            id=price_db.id,
            product_id=price_db.product_id,
            price=price_db.price,
            establishment=Establishment(
                id=establishment.id,
                name=establishment.name,
                establishment_type=establishment.establishment_type,
                address=establishment.address,
                county=establishment.county,
                latitude=establishment.latitude,
                longitude=establishment.longitude,
                brand=establishment.brand,
                external_id=establishment.external_id,
            ),
            product=Product(
                id=product.id,
                name=product.name,
                presentation=product.presentation,
                brand=product.brand,
                photo=product.photo,
            ),
        )

        return price

    def list(self, offset: int, limit: int) -> List[Establishment]:
        with self.db_session() as session:
            establishments_db = session.query(EstablishmentModel).offset(offset).limit(limit).all()
            establishments = self._to_domain(establishment_db=establishments_db)
        return establishments

    def nearby(self, lat: float, lng: float, distance: float = 1500):
        with self.db_session() as session:
            filter = func.ST_DWithin(
                EstablishmentModel.location,
                func.Geometry(func.ST_GeographyFromText("POINT({} {})".format(lng, lat))),
                distance,
            )
            query = session.query(EstablishmentModel).filter(filter)
            establishment_db = query.all()
            establishments = self._to_domain(establishment_db=establishment_db)
        return establishments

    def total(self) -> int:
        with self.db_session() as session:
            return session.query(EstablishmentModel).count()

    def get_products_prices(self, establishment_id: int, product_ids):
        with self.db_session() as session:
            prices_db = (
                session.query(ProductPriceModel)
                .filter(ProductPriceModel.product_id.in_(product_ids))
                .filter_by(establishment_id=establishment_id)
            )

            prices = []

            for price in prices_db:
                prices.append(self._to_domain_price(price))

        return prices

    def get_product_price(self, establishment_ids, product_id):
        with self.db_session() as session:
            prices_db = (
                session.query(ProductPriceModel, EstablishmentModel)
                .filter(ProductPriceModel.establishment_id.in_(establishment_ids))
                .filter_by(product_id=product_id)
                .filter(EstablishmentModel.id == ProductPriceModel.establishment_id)
            )

            prices = []

            product = session.query(ProductModel).get(product_id)
            for price, establishment in prices_db:
                prices.append(self._to_domain_price_establishment(price, establishment, product))

        return prices
