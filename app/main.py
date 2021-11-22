import sys
from profile.application import usecases as profile_usecases

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from auth.application import usecases as auth_usecases
from common.di.containers import ApplicationContainer
from common.routes import get_routes
from common.settings import API_PREFIX
from location.application import usecases as location_usecases
from market.application import usecases
from middleware import Chartset
from notification.application import usecases as notification_usecases
from shopping.application import usecases as shopping_usecases


def setup() -> FastAPI:
    application = ApplicationContainer()
    application.init_resources()
    application.wire(
        modules=[
            sys.modules[__name__],
            usecases,
            auth_usecases,
            profile_usecases,
            location_usecases,
            shopping_usecases,
            notification_usecases,
        ]
    )
    app = FastAPI()

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(Chartset)
    app.mount("/static", StaticFiles(directory="/static"), name="static")
    app.include_router(get_routes(), prefix=API_PREFIX)

    return app


app = setup()
