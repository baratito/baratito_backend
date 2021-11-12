from .config import SessionLocal


def get_db_session():
    print("asdasd")
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
