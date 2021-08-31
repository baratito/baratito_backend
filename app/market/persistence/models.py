import datetime

from sqlalchemy import Column, DateTime, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import BIGINT

Base = declarative_base()


class Product(Base):
    __tablename__ = "product"
    id = Column(BIGINT, primary_key=True, index=True)
    name = Column(
        String,
    )
    presentation = Column(String)
    brand = Column(String)
    max_price = Column(Float)
    min_price = Column(Float)
    # created_date = Column(DateTime, default=datetime.datetime.utcnow)
    # update_date = Column(DateTime, default=datetime.datetime.utcnow)
