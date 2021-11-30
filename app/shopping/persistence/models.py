import datetime

from sqlalchemy import BIGINT, Column, DateTime, Float, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean

from common.persistence.config import Base


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

    list_id = Column(BIGINT, ForeignKey("list.id", ondelete="cascade"))
    list_obj = relationship("List", backref=backref("list_items", cascade="all,delete"))


class PurchaseList(Base):
    __tablename__ = "purchase_list"
    id = Column(BIGINT, primary_key=True, index=True)

    name = Column(String)
    color = Column(String)
    status = Column(Boolean)

    distance = Column(Float)
    duration = Column(Integer)
    estimated_price = Column(Float)
    spent = Column(Float)
    overview_polyline = Column(String)

    latitude_southwest = Column(Float)
    longitude_southwest = Column(Float)
    latitude_northeast = Column(Float)
    longitude_northeast = Column(Float)

    start_longitude = Column(Float)
    start_latitude = Column(Float)

    list_id = Column(BIGINT, ForeignKey("list.id", ondelete="SET NULL"))
    list_obj = relationship("List", backref=backref("purchase_lists"))

    user_id = Column(BIGINT, ForeignKey("user.id"))
    user = relationship("User", backref="purchase_lists")

    created_date = Column(DateTime, default=datetime.datetime.utcnow)


class PurchaseListItem(Base):
    __tablename__ = "purchase_list_item"
    id = Column(BIGINT, primary_key=True, index=True)

    name = Column(String)

    price = Column(Float)
    quantity = Column(Integer)
    is_bought = Column(Boolean)

    product_price_id = Column(BIGINT, ForeignKey("product_price.id"))
    product_price = relationship("ProductPrice", backref="purchase_list_items")

    product_id = Column(BIGINT, ForeignKey("product.id"))
    product = relationship("Product", backref="purchase_list_items")

    purchase_list_id = Column(BIGINT, ForeignKey("purchase_list.id", ondelete="SET NULL"))
    purchase_list = relationship("PurchaseList", backref=backref("purchase_list_items"))

    establishment_id = Column(BIGINT, ForeignKey("establishment.id"))
    establishment = relationship("Establishment", backref="purchase_list_items")


class EstablishmentPurchaseListOrder(Base):
    __tablename__ = "establishment_purchase_list_order"
    id = Column(BIGINT, primary_key=True, index=True)

    order = Column(Integer)

    purchase_list_id = Column(BIGINT, ForeignKey("purchase_list.id"))
    purchase_list = relationship(
        "PurchaseList", backref=backref("establishment_orders", cascade="all,delete")
    )

    establishment_id = Column(BIGINT, ForeignKey("establishment.id"))
    establishment = relationship("Establishment", backref="establishment_orders")
