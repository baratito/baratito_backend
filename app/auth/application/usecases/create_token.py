from datetime import datetime, timedelta

from jose import jwt

from common.settings import ALGORITHM, SECRET_KEY


def create_token(*, data: dict, expires: datetime = None) -> str:
    """
    Create JWT token with expiration date.
    """
    to_encode = data.copy()
    if not expires:
        expires = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expires})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
