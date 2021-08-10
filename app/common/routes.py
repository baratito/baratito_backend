from fastapi.routing import APIRouter
from market.presentation import routes as products_routes


def get_routes():
    router = APIRouter()
    router.include_router(products_routes.router, tags=["product"])  # prefix="/shopping"
    return router
