from profile.application.repositories.profile_repository import ProfileRepository

from sqlalchemy.orm import Session

from .models import Profile


class ProfileRepositoryImpl(ProfileRepository):
    db_session: Session

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def create(self, data: dict, user_id: int):
        with self.db_session() as session:
            profile = Profile(
                email=data["email"],
                avatar=data["picture"],
                first_name=data["given_name"],
                last_name=data["family_name"],
                user_id=user_id,
            )

            session.add(profile)
            session.commit()

        return profile

    def get_by_user_id(self, id: int):
        with self.db_session() as session:
            return session.query(Profile).filter_by(user_id=id).one()
