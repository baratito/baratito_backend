from common.persistence.config import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import BIGINT


class User(Base):
    __tablename__ = "user"
    id = Column(BIGINT, primary_key=True, index=True)
    email = Column(String)
    profile = relationship("Profile", back_populates="user", uselist=False, lazy=True)
