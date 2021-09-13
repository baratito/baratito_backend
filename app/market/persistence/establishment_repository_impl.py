from typing import List

from geoalchemy2 import func
from market.application.repositories.establishment_repository import EstablishmentRepository
from market.domain import Establishment
from market.persistence.models import Establishment as EstablishmentModel
from sqlalchemy.orm.session import Session


class EstablishmentRepositoryImpl(EstablishmentRepository):
    db_session: Session

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def _to_domain(self, establishment_db):
        establishments = []

        for establishment in establishment_db:
            establishments.append(
                Establishment(
                    id=establishment.id,
                    name=establishment.name,
                    establishment_type=establishment.establishment_type,
                    address=establishment.address,
                    county=establishment.county,
                    latitude=establishment.latitude,
                    longitude=establishment.longitude,
                    brand=establishment.brand,
                    external_id=establishment.external_id,
                )
            )
        return establishments

    def list(self, offset: int, limit: int) -> List[Establishment]:
        establishments_db = (
            self.db_session.query(EstablishmentModel).offset(offset).limit(limit).all()
        )
        establishments = self._to_domain(establishment_db=establishments_db)
        return establishments

    def nearby(self, lat: float, lng: float, distance: float = 1500):
        filter = func.ST_DWithin(
            Establishment.location,
            func.Geometry(func.ST_GeographyFromText("POINT({} {})".format(lng, lat))),
            distance,
        )
        query = self.session_db.query(EstablishmentModel).filter(filter)
        establishment_db = query.all()
        establishments = self._to_domain(establishment_db=establishment_db)
        return establishments

    def total(self) -> int:
        return self.db_session.query(EstablishmentModel).count()
