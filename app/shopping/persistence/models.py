import datetime

from common.persistence.config import Base
from sqlalchemy import BIGINT, Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class List(Base):
    __tablename__ = "list"
    id = Column(BIGINT, primary_key=True, index=True)
    name = Column(String)
    color = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    user_id = Column(BIGINT, ForeignKey("user.id"))
    user = relationship("User", backref="lists")


class ListItem(Base):
    __tablename__ = "list_item"
    id = Column(BIGINT, primary_key=True, index=True)
    id_uuid = Column(UUID(as_uuid=True), index=True, unique=True)
    quantity = Column(Integer)
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    product_id = Column(BIGINT, ForeignKey("product.id"))
    product = relationship("Product", backref="list_items")

    list_id = Column(BIGINT, ForeignKey("list.id"))
    list_obj = relationship("List", backref="list_items")
