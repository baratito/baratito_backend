from shopping.application.repositories.list_repository import ListItemNotFound, ListRepository
from shopping.domain import List as ListDomain
from shopping.domain import ListItem as ListItemDomain
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

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
            product_id=list_item_db.product_id,
            list_id=list_item_db.list_id,
        )
        return list_item

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

    def remove_lack_items(self, list_id, list_uuid):
        list_items_query = self.db_session.query(ListItem.id_uuid).filter(
            ListItem.id_uuid.in_(list_uuid), ListItem.list_id == list_id
        )
        self.db_session.query(ListItem).filter(ListItem.id_uuid.not_in(list_items_query)).delete(
            synchronize_session="fetch"
        )
        self.db_session.commit()

    def get_list_item_by_uuid(self, id_uuid):
        item_db = None
        try:
            item_db = self.db_session.query(ListItem).filter_by(id_uuid=id_uuid).one()
        except NoResultFound as e:
            raise ListItemNotFound

        return item_db

    def update_list_item(self, list_item):
        item_db = self.get_list_item_by_uuid(id_uuid=list_item.id_uuid)

        item_db.quantity = list_item.quantity
        self.db_session.commit()

        return self._to_domain_list_item(item_db)

    def create_list_item(self, list_id, list_item):
        list_item_db = ListItem(
            id_uuid=list_item.id_uuid,
            quantity=list_item.quantity,
            product_id=list_item.product_id,
            list_id=list_id,
        )

        self.db_session.add(list_item_db)
        self.db_session.commit()
        list_item = self._to_domain_list_item(list_item_db)
        return list_item

    def get_list_item_by_list(self, list_id):
        items_db = self.db_session.query(ListItem).filter_by(list_id=list_id)
        items = []
        for item in items_db:
            items.append(self._to_domain_list_item(item))
        return items
