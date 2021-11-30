from sqlalchemy.orm import Session

from market.domain import Establishment
from market.domain import Product as ProductDomain
from market.persistence.models import Product
from shopping.application.repositories.purchase_list_repository import PurchaseListRepository
from shopping.domain.purchase_list import PurchaseList as PurchaseListDomain
from shopping.domain.purchase_list_item import PurchaseListItem as PurchaseListItemDomain
from shopping.persistence.models import (
    EstablishmentPurchaseListOrder,
    PurchaseList,
    PurchaseListItem,
)


class PurchaseListRepositoryImpl(PurchaseListRepository):
    db_session: Session

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def _to_domain(self, list_db):
        purchase = PurchaseListDomain(
            id=list_db.id,
            name=list_db.name,
            color=list_db.color,
            user_id=list_db.user_id,
            distance=list_db.distance,
            duration=list_db.duration,
            spent=list_db.spent,
            list_id=list_db.list_id,
            status=list_db.status,
            estimated_price=list_db.estimated_price,
            created_date=str(list_db.created_date),
            overview_polyline=list_db.overview_polyline,
            boundaries={
                "northeast": {
                    "latitude": list_db.latitude_northeast,
                    "longitude": list_db.longitude_northeast,
                },
                "southwest": {
                    "latitude": list_db.latitude_southwest,
                    "longitude": list_db.longitude_southwest,
                },
            },
            starting_point={
                "latitude": list_db.start_latitude,
                "longitude": list_db.start_longitude,
            },
        )
        return purchase

    def _to_domain_item(self, item_db):
        item = PurchaseListItemDomain(
            id=item_db.id,
            name=item_db.name,
            price=item_db.price,
            quantity=item_db.quantity,
            is_bought=item_db.is_bought,
            product_price_id=item_db.product_price_id,
            product_id=item_db.product_id,
            purchase_list_id=item_db.purchase_list_id,
            establishment_id=item_db.establishment_id,
        )

        return item

    def _to_domain_order(self, order_db):

        establishment = Establishment(
            id=order_db.establishment.id,
            name=order_db.establishment.name,
            establishment_type=order_db.establishment.establishment_type,
            address=order_db.establishment.address,
            county=order_db.establishment.county,
            latitude=order_db.establishment.latitude,
            longitude=order_db.establishment.longitude,
            brand=order_db.establishment.brand,
        )

        return establishment

    def _to_domain_product(self, product):
        product = ProductDomain(
            id=product.id,
            name=product.name,
            presentation=product.presentation,
            brand=product.brand,
            photo=product.photo,
        )
        return product

    def create(self, purchase_list: PurchaseListDomain):
        with self.db_session() as session:
            list_db = PurchaseList(
                name=purchase_list.name,
                color=purchase_list.color,
                user_id=purchase_list.user_id,
                distance=purchase_list.distance,
                duration=purchase_list.duration,
                spent=purchase_list.spent,
                list_id=purchase_list.list_id,
                estimated_price=purchase_list.estimated_price,
                status=bool(purchase_list.status),
                overview_polyline=purchase_list.overview_polyline,
                latitude_southwest=purchase_list.boundaries["southwest"]["latitude"],
                longitude_southwest=purchase_list.boundaries["southwest"]["longitude"],
                latitude_northeast=purchase_list.boundaries["northeast"]["latitude"],
                longitude_northeast=purchase_list.boundaries["northeast"]["longitude"],
                start_latitude=purchase_list.starting_point["latitude"],
                start_longitude=purchase_list.starting_point["longitude"],
            )
            session.add(list_db)
            session.commit()
            list_obj = self._to_domain(list_db=list_db)
        return list_obj

    def create_purchase_list(self, purchase_list_item: PurchaseListItemDomain):
        with self.db_session() as session:
            item_db = PurchaseListItem(
                name=purchase_list_item.name,
                price=purchase_list_item.price,
                quantity=purchase_list_item.quantity,
                is_bought=purchase_list_item.is_bought,
                product_price_id=purchase_list_item.product_price_id,
                product_id=purchase_list_item.product_id,
                purchase_list_id=purchase_list_item.purchase_list_id,
                establishment_id=purchase_list_item.establishment_id,
            )
            session.add(item_db)
            session.commit()

            item = self._to_domain_item(item_db=item_db)

        return item

    def list(self, user_id, in_progress: int = None, from_date=None):
        with self.db_session() as session:
            query = session.query(PurchaseList).filter_by(user_id=user_id)

            if in_progress is not None:
                query = query.filter_by(status=not bool(in_progress))

            if from_date is not None:
                query = query.filter(PurchaseList.created_date >= from_date).order_by(
                    PurchaseList.created_date.asc()
                )

            purchases = []

            for p in query:
                purchases.append(self._to_domain(p))
        return purchases

    def create_establishment_order(self, order, establishment_id, purchase_list_id):
        with self.db_session() as session:
            order_db = EstablishmentPurchaseListOrder(
                order=order, establishment_id=establishment_id, purchase_list_id=purchase_list_id
            )
            session.add(order_db)
            session.commit()
        return order_db

    def get_by_id(self, id):
        with self.db_session() as session:
            purchase_db = session.query(PurchaseList).get(id)
            return self._to_domain(purchase_db)

    def complete(self, user_id, purchase_id, spent):
        with self.db_session() as session:
            session.query(PurchaseList).filter_by(user_id=user_id, id=purchase_id).update(
                {"status": True, "spent": spent}
            )
            session.commit()
            return self.get_by_id(purchase_id)

    def get_establishment_order(self, purchase_id):
        with self.db_session() as session:
            query = (
                session.query(EstablishmentPurchaseListOrder)
                .filter_by(purchase_list_id=purchase_id)
                .order_by(EstablishmentPurchaseListOrder.order.asc())
            )

            orders = []
            for order in query.all():
                orders.append(self._to_domain_order(order_db=order))

        return orders

    def get_items_by_purchase_id(self, purchase_id):
        with self.db_session() as session:
            query = (
                session.query(PurchaseListItem)
                .filter_by(purchase_list_id=purchase_id)
                .order_by(PurchaseListItem.name.asc())
            )

            items = []
            for item in query.all():
                items.append(self._to_domain_item(item))

        return items

    def get_purchase_item_by_id(self, item_id):
        with self.db_session() as session:
            purchase_db = session.query(PurchaseListItem).get(item_id)
            return self._to_domain_item(purchase_db)

    def update_purchase_list_item(self, item_id, data):
        update_fields = {
            key: getattr(data, key) for key in data.__fields__ if getattr(data, key) is not None
        }
        with self.db_session() as session:
            session.query(PurchaseListItem).filter_by(id=item_id).update(update_fields)
            session.commit()
        return self.get_purchase_item_by_id(item_id)

    def get_all_products(self, user_id):
        with self.db_session() as session:
            query = (
                session.query(Product)
                .join(PurchaseListItem)
                .join(PurchaseList)
                .filter(PurchaseList.user_id == user_id)
            ).distinct()

            items = []
            for item in query.all():
                items.append(self._to_domain_product(item))

        return items
