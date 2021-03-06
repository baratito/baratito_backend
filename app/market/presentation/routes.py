from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Depends

from auth.presentation.utils import get_current_user
from location.application.usecases.get_enable_location import get_enable_location
from market.application.usecases import (
    detail_product,
    list_establisment,
    list_products,
    total_establishment,
)
from market.application.usecases.get_available_markets_count import get_available_markets_count
from market.application.usecases.get_product_price import get_product_price
from market.application.usecases.get_recommendations import get_recommendations
from market.application.usecases.list_category import list_category
from market.application.usecases.total_product import total_products

router = APIRouter()


@router.get("/products", name="market:products")
@router.get("/products/", name="market:products", include_in_schema=False)
def get_products(offset: int = 0, limit: int = 100, q: str = None, category: int = None):
    """
    Get list of products
    """
    products = list_products(offset=offset, limit=limit, q=q, category=category)
    total = total_products(q=q, category=category)
    return {"total": total, "results": products}


@router.get("/product/{id}", name="market:product")
@router.get("/product/{id}/", name="market:product", include_in_schema=False)
def get_product(id: int = 0):
    """
    Get detail product
    """
    product = detail_product(id=id)
    return product


@router.get("/prices/product/{id}", name="market:product_price")
@router.get("/prices/product/{id}/", name="market:product_prices", include_in_schema=False)
def get_product_prices(user=Depends(get_current_user), id: int = 0):
    """
    Get product price
    """

    location = get_enable_location(user_id=user.id)
    markets = get_available_markets_count(
        lat=location.latitude, lng=location.longitude, distance=5
    )

    if len(markets) == 0:
        raise HTTPException(status_code=400, detail="No markets near")

    market_ids = [market.id for market in markets]
    prices = get_product_price(establishment_ids=market_ids, product_id=id)

    return {"results": prices}


@router.get("/establishments", name="market:establishments")
@router.get("/establishments/", name="market:establishments", include_in_schema=False)
def get_establishments(offset: int = 0, limit: int = 100):
    """
    Get list of establishments
    """
    establishments = list_establisment(offset=offset, limit=limit)
    total = total_establishment()
    return {"total": total, "results": establishments}


@router.get("/categories", name="market:categories")
@router.get(
    "/categories/",
    name="market:categories",
    include_in_schema=False,
)
def get_categories():
    """
    Get list of categories
    """
    categories = list_category()
    return {"results": categories}


@router.get("/products/recommendations", name="market:establishments")
@router.get("/products/recommendations/", name="market:establishments", include_in_schema=False)
def recommendations(user=Depends(get_current_user)):
    """
    Get list of establishments
    """

    products = get_recommendations(user_id=user.id)
    return {"results": products}
