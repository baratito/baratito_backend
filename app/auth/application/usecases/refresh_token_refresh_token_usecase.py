from datetime import datetime, timedelta

from fastapi.encoders import jsonable_encoder
from jose import jwt

from auth.application.repositories.user_repository import UserNotFound
from auth.application.usecases import create_token, get_user_by_email
from common.settings import (ACCESS_TOKEN_EXPIRE_DAYS, ALGORITHM,
                             REFRESH_TOKEN_EXPIRE_DAYS, SECRET_KEY)


def refresh_token_usecase(refresh_token: str):
    payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
    email: str = payload.get("sub")

    try:
        user = get_user_by_email(email=email)
    except UserNotFound:
        raise ValueError("User does not exists")
    access_token_expires = datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    refresh_token_expires = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)

    access_token = create_token(data={"sub": email}, expires=access_token_expires)
    refresh_token = create_token(data={"sub": email}, expires=refresh_token_expires)
    token = jsonable_encoder(access_token)
    refresh_token = jsonable_encoder(refresh_token)
    return {
        "access_token": token,
        "refresh_token": refresh_token,
        "expiration_access_token": access_token_expires,
        "expiration_refresh_token": refresh_token_expires,
    }
