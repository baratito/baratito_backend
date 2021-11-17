from contextlib import contextmanager

from sqlalchemy import orm
from sqlalchemy.engine import create_engine

from common.settings import DB_URL


class Database:
    def __init__(self) -> None:
        self._engine = create_engine(DB_URL)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    @contextmanager
    def session(self):
        session = self._session_factory()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
