from sqlalchemy.orm import Session

from location.application.repositories import UserLocationRepository
from location.domain import UserLocation as UserLocationDomain

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
            name=location_db.name,
        )
        return location

    def create(self, user_location: UserLocationDomain):
        with self.db_session() as session:
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
            session.add(location)
            session.commit()
        location = self._to_domain(location_db=location)
        return location

    def filter(self, user_id, enable=None):
        with self.db_session() as session:
            query = session.query(UserLocation).filter_by(user_id=user_id)

            if enable is not None:
                query = query.filter_by(enable=enable)

            locations_db = query.all()
            locations = []
            for location in locations_db:
                locations.append(self._to_domain(location))
        return locations

    def get_by_id(self, id: int):
        with self.db_session() as session:
            location = session.query(UserLocation).get(id)
            location = self._to_domain(location) if location else None
        return location

    def enable_for_user(self, id: int, user_id: int):
        with self.db_session() as session:
            session.query(UserLocation).filter_by(user_id=user_id).update({"enable": False})
            session.query(UserLocation).filter_by(user_id=user_id, id=id).update({"enable": True})
            session.commit()

    def disable_all_user_location(self, user_id: int):
        with self.db_session() as session:
            session.query(UserLocation).filter_by(user_id=user_id).update({"enable": False})
            session.commit()

    def edit(self, id: int, user_id, new_user_location):
        update_fields = {
            key: getattr(new_user_location, key)
            for key in new_user_location.__fields__
            if getattr(new_user_location, key) is not None
        }
        with self.db_session() as session:
            session.query(UserLocation).filter_by(user_id=user_id, id=id).update(update_fields)
            session.commit()
        return self.get_by_id(id)

    def get_enable_location_by_user(self, user_id: int = 0):
        with self.db_session() as session:
            location = session.query(UserLocation).filter_by(user_id=user_id, enable=True).one()
        location = self._to_domain(location) if location else None
        return location
