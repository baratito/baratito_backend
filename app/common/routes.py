from profile.presentation import routes as profile_routes

from auth.presentation import routes as auth_routes
from auth.presentation.utils import get_current_user
from fastapi.param_functions import Depends
from fastapi.routing import APIRouter
from market.presentation import routes as products_routes


def get_routes():
    router = APIRouter()
    router.include_router(
        products_routes.router, tags=["product"], dependencies=[]
    )  # prefix="/shopping"
    router.include_router(auth_routes.router, tags=["auth"])
    router.include_router(profile_routes.router, tags=["profile"])
    return router
