import datetime

from common.persistence.config import Base
from geoalchemy2.types import Geography
from sqlalchemy import Column, DateTime, Float, String, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import BIGINT


class Product(Base):
    __tablename__ = "product"
    id = Column(BIGINT, primary_key=True, index=True)
    name = Column(String)
    presentation = Column(String)
    brand = Column(String)
    max_price = Column(Float)
    min_price = Column(Float)
    external_id = Column(String, unique=True)
    # created_date = Column(DateTime, default=datetime.datetime.utcnow)
    # update_date = Column(DateTime, default=datetime.datetime.utcnow)


class Establishment(Base):
    __tablename__ = "establishment"
    id = Column(BIGINT, primary_key=True, index=True)
    name = Column(String)
    establishment_type = Column(String)
    address = Column(String)
    county = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    brand = Column(String)
    external_id = Column(String, unique=True)
    location = Column(Geography("POINT", srid=4326))


class Category(Base):
    __tablename__ = "category"
    id = Column(BIGINT, primary_key=True, index=True)
    name = Column(String)
    external_id = Column(String, unique=True)
    parent_id = Column(BIGINT, ForeignKey("category.id"), index=True)
    parent = relationship(lambda: Category, remote_side=id, backref="sub_categories")


class CategoryProduct(Base):
    __tablename__ = "category_product"
    __table_args__ = (UniqueConstraint("product_id", "category_id"),)
    id = Column(BIGINT, primary_key=True, index=True)
    product_id = Column(BIGINT, ForeignKey("product.id"), index=True)
    product = relationship("Product", backref="categories")
    category_id = Column(BIGINT, ForeignKey("category.id"), index=True)
    category = relationship("Category", backref="products")
