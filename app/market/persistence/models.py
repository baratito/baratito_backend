import datetime

import geoalchemy2
from common.persistence.config import Base
from geoalchemy2 import Geometry
from geoalchemy2.types import Geography
from sqlalchemy import Column, DateTime, Float, String, UniqueConstraint
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
