from common.persistence.config import Base
from sqlalchemy import Column, Float, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import BIGINT


class Profile(Base):
    __tablename__ = "profile"
    id = Column(BIGINT, primary_key=True, index=True)
    email = Column(String)
    avatar = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    user_id = Column(BIGINT, ForeignKey("user.id"))
    user = relationship("User", back_populates="profile")
