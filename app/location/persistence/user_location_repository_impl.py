from location.application.repositories import UserLocationRepository
from location.domain import UserLocation as UserLocationDomain
from sqlalchemy.orm import Session

from .models import UserLocation


class UserLocationRepositoryImpl(UserLocationRepository):
    db_session: Session

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def create(self, user_location: UserLocationDomain):
        location = UserLocation(
            name=user_location.name,
            address=user_location.address,
            latitude=user_location.latitude,
            longitude=user_location.longitude,
            enable=user_location.enable,
            city=user_location.city,
            country=user_location.country,
            user_id=user_location.user_id,
        )
        self.db_session.add(location)
        self.db_session.commit()

    def filter(self, user_id, enable=None):
        query = self.db_session.query(UserLocation).filter_by(user_id=user_id)

        if enable is not None:
            query = query.filter_by(enable=enable)

        return query.all()
