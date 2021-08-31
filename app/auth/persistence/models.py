from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import BIGINT

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(BIGINT, primary_key=True, index=True)
    email = Column(String)
