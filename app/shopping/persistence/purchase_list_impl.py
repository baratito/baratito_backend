from sqlalchemy.orm import Session

from shopping.application.repositories.purchase_list_repository import PurchaseListRepository
from shopping.domain.purchase_list import PurchaseList as PurchaseListDomain
from shopping.domain.purchase_list_item import PurchaseListItem as PurchaseListItemDomain
from shopping.persistence.models import PurchaseList, PurchaseListItem


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
        )
        return purchase

    def _to_domain_item(self, item_db):
        item = PurchaseListItemDomain(
            id=item_db.id,
            name=item_db.name,
            price=item_db.price,
            quantity=item_db.quantity,
            is_buyed=item_db.is_buyed,
            product_price_id=item_db.product_price_id,
            product_id=item_db.product_id,
            purchase_list_id=item_db.purchase_list_id,
            establishment_id=item_db.establishment_id,
        )

        return item

    def create(self, purchase_list: PurchaseListDomain):
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
        )
        self.db_session.add(list_db)
        self.db_session.commit()
        list_obj = self._to_domain(list_db=list_db)
        return list_obj

    def create_purchase_list(self, purchase_list_item: PurchaseListItemDomain):
        item_db = PurchaseListItem(
            name=purchase_list_item.name,
            price=purchase_list_item.price,
            quantity=purchase_list_item.quantity,
            is_buyed=purchase_list_item.is_buyed,
            product_price_id=purchase_list_item.product_price_id,
            product_id=purchase_list_item.product_id,
            purchase_list_id=purchase_list_item.purchase_list_id,
            establishment_id=purchase_list_item.establishment_id,
        )
        self.db_session.add(item_db)
        self.db_session.commit()

        item = self._to_domain_item(item_db=item_db)

        return item
