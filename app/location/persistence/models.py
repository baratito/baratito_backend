from common.persistence.config import Base
from sqlalchemy import Column, Float, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import BIGINT, Boolean


class UserLocation(Base):
    __tablename__ = "user_location"
    id = Column(BIGINT, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    enable = Column(Boolean)
    city = Column(String)
    country = Column(String)

    user_id = Column(BIGINT, ForeignKey("user.id"))
    user = relationship("User", backref="user_locations")
