import os

API_PREFIX = "/api"

# Database variables setups
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# AUTH settings

ACCESS_TOKEN_EXPIRE_DAYS = 60
REFRESH_TOKEN_EXPIRE_DAYS = 365
GOOGLE_CLIENT_IDS = os.environ.get("GOOGLE_CLIENT_IDS").split(",")

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
