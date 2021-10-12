import datetime

from common.persistence.config import Base
from sqlalchemy import BIGINT, Column, DateTime, String
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
