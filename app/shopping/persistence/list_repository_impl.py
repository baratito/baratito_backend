from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from market.domain import Product as ProductDomain
from shopping.application.repositories.list_repository import ListItemNotFound, ListRepository
from shopping.domain import List as ListDomain
from shopping.domain import ListItem as ListItemDomain

from .models import List, ListItem


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

    def _to_domain_list_item(self, list_item_db):
        list_item = ListItemDomain(
            id=list_item_db.id,
            id_uuid=str(list_item_db.id_uuid),
            quantity=list_item_db.quantity,
            created_date=str(list_item_db.created_date),
            product=ProductDomain(
                id=list_item_db.product.id,
                name=list_item_db.product.name,
                presentation=list_item_db.product.presentation,
                brand=list_item_db.product.brand,
                photo=list_item_db.product.photo,
            ),
            list_id=list_item_db.list_id,
        )
        return list_item

    def create(self, list_obj):
        with self.db_session() as session:
            list_db = List(name=list_obj.name, color=list_obj.color, user_id=list_obj.user_id)
            session.add(list_db)
            session.commit()
            list_obj = self._to_domain(list_db=list_db)
        return list_db

    def list(self, user_id: int):
        with self.db_session() as session:
            lists_db = session.query(List).filter_by(user_id=user_id).order_by(List.name.asc())
            lists = []

            for list_obj in lists_db:
                lists.append(self._to_domain(list_db=list_obj))

        return lists

    def remove_lack_items(self, list_id, item_id):
        with self.db_session() as session:
            list_items_query = session.query(ListItem.id).filter(
                ListItem.id.in_(item_id), ListItem.list_id == list_id
            )

            session.query(ListItem).filter(
                ListItem.id.not_in(list_items_query), ListItem.list_id == list_id
            ).delete(synchronize_session="fetch")

            session.commit()

    def get_list_item_by_id(self, id):
        with self.db_session() as session:
            item_db = None
            try:
                item_db = session.query(ListItem).filter_by(id=id).one()
            except NoResultFound as e:
                raise ListItemNotFound

        return item_db

    def update_list_item(self, list_id, list_item):
        with self.db_session() as session:
            item_db = self.get_list_item_by_id(id=list_item.id)

            if item_db.list_id != list_id:
                print("ojo al piojo eh")

            item_db.quantity = list_item.quantity
            session.commit()

    def create_list_item(self, list_id, list_item):
        with self.db_session() as session:
            list_item_db = ListItem(
                quantity=list_item.quantity,
                product_id=list_item.product_id,
                list_id=list_id,
            )

            session.add(list_item_db)
            session.commit()

    def get_list_item_by_list(self, list_id):
        with self.db_session() as session:
            items_db = session.query(ListItem).filter_by(list_id=list_id)
            items = []
            for item in items_db:
                items.append(self._to_domain_list_item(item))
        return items

    def get_list_by_id(self, id):
        with self.db_session() as session:
            list_db = session.query(List).get(id)
        return self._to_domain(list_db)

    def edit_list(self, user_id, id, new_list_obj):
        with self.db_session() as session:
            update_fields = {
                key: getattr(new_list_obj, key)
                for key in new_list_obj.__fields__
                if getattr(new_list_obj, key) is not None
            }
            session.query(List).filter_by(user_id=user_id, id=id).update(update_fields)
            session.commit()
        return self.get_list_by_id(id)

    def delete_list(self, user_id, list_id):
        with self.db_session() as session:
            session.query(List).filter(List.id == list_id, List.user_id == user_id).delete(
                synchronize_session="fetch"
            )
            session.commit()
