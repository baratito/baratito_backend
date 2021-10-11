from location.application.repositories import UserLocationRepository
from location.domain import UserLocation as UserLocationDomain
from sqlalchemy.orm import Session

from .models import UserLocation


class UserLocationRepositoryImpl(UserLocationRepository):
    db_session: Session

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def _to_domain(self, location_db):
        location = UserLocation(
            id=location_db.id,
            address=location_db.address,
            latitude=location_db.latitude,
            longitude=location_db.longitude,
            enable=location_db.enable,
            city=location_db.city,
            country=location_db.country,
            user_id=location_db.user_id,
        )
        return location

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
        location = self._to_domain(location_db=location)
        return location

    def filter(self, user_id, enable=None):
        query = self.db_session.query(UserLocation).filter_by(user_id=user_id)

        if enable is not None:
            query = query.filter_by(enable=enable)

        locations_db = query.all()
        locations = []
        for location in locations_db:
            locations.append(self._to_domain(location))
        return locations

    def get_by_id(self, id: int):
        location = self.db_session.query(UserLocation).get(id)
        location = self._to_domain(location) if location else None
        return location

    def enable_for_user(self, id: int, user_id: int):
        self.db_session.query(UserLocation).filter_by(user_id=user_id).update({"enable": False})
        self.db_session.query(UserLocation).filter_by(user_id=user_id, id=id).update(
            {"enable": True}
        )
        self.db_session.commit()
