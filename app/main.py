import sys

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from auth.application import usecases as auth_usecases
from common.di.containers import ApplicationContainer
from common.routes import get_routes
from common.settings import API_PREFIX
from market.application import usecases


def setup() -> FastAPI:
    application = ApplicationContainer()
    application.wire(modules=[sys.modules[__name__], usecases, auth_usecases])
    app = FastAPI()

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.mount("/static", StaticFiles(directory="/static"), name="static")

    app.include_router(get_routes(), prefix=API_PREFIX)

    return app


app = setup()
