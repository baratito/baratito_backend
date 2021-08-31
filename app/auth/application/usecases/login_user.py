from datetime import datetime, timedelta

from auth.application.repositories.user_repository import UserNotFound
from auth.application.usecases import create_user, get_user_by_email
from auth.application.usecases.create_token import create_token
from common.settings import ACCESS_TOKEN_EXPIRE_DAYS, GOOGLE_CLIENT_IDS, REFRESH_TOKEN_EXPIRE_DAYS
from fastapi.encoders import jsonable_encoder
from google.auth.transport import requests
from google.oauth2 import id_token


def login_user(auth_code: str) -> dict:
    idinfo = id_token.verify_oauth2_token(auth_code, requests.Request())

    if idinfo["aud"] not in GOOGLE_CLIENT_IDS:
        raise ValueError("Could not verify audience.")

    if idinfo["iss"] not in ["accounts.google.com", "https://accounts.google.com"]:
        raise ValueError("Wrong issuer.")

    if idinfo["email"] and idinfo["email_verified"]:
        email = idinfo.get("email")
    else:
        raise ValueError("Unable to validate social login")

    try:
        user = get_user_by_email(email=email)
    except UserNotFound:
        user = create_user(email=idinfo["email"])

    access_token_expires = datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    refresh_token_expires = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)

    access_token = create_token(data={"sub": user.email}, expires=access_token_expires)

    refresh_token = create_token(data={"sub": user.email}, expires=refresh_token_expires)

    token = jsonable_encoder(access_token)
    refresh_token = jsonable_encoder(refresh_token)

    return {
        "access_token": token,
        "refresh_token": refresh_token,
        "expiration_access_token": access_token_expires,
        "expiration_refresh_token": refresh_token_expires,
    }
