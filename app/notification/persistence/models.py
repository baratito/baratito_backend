import datetime

from sqlalchemy import BIGINT, Boolean, Column, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from common.persistence.config import Base


class Notification(Base):
    __tablename__ = "notification"
    id = Column(BIGINT, primary_key=True, index=True)

    title = Column(String)
    content = Column(String)
    is_read = Column(Boolean)

    user_id = Column(BIGINT, ForeignKey("user.id"))
    user = relationship("User", backref="notifications")

    created_date = Column(DateTime, default=datetime.datetime.utcnow)
