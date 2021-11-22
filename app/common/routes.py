from profile.presentation import routes as profile_routes

from fastapi.param_functions import Depends
from fastapi.routing import APIRouter

from auth.presentation import routes as auth_routes
from auth.presentation.utils import get_current_user
from location.presentation import routes as location_routes
from market.presentation import routes as products_routes
from notification.presentation import routes as notification_routes
from shopping.presentation import routes as shopping_routes


def get_routes():
    router = APIRouter()
    router.include_router(
        products_routes.router, tags=["product"], dependencies=[]
    )  # prefix="/shopping"
    router.include_router(auth_routes.router, tags=["auth"])
    router.include_router(profile_routes.router, tags=["profile"])
    router.include_router(location_routes.router, tags=["location"])
    router.include_router(shopping_routes.router, tags=["shopping"])
    router.include_router(notification_routes.router, tags=["notification"])
    return router
