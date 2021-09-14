from common.persistence.get_db_session import get_db_session
from fastapi import APIRouter
from market.application.usecases import (
    detail_product,
    list_establisment,
    list_products,
    total_establishment,
)
from market.application.usecases.total_product import total_products

router = APIRouter()


@router.get("/products", name="market:products")
@router.get("/products/", name="market:products", include_in_schema=False)
def get_products(offset: int = 0, limit: int = 100, q: str = None):
    """
    Get list of products
    """
    products = list_products(offset=offset, limit=limit, q=q)
    total = total_products()
    return {"total": total, "results": products}


@router.get("/product/{id}", name="market:product")
@router.get("/product/{id}/", name="market:product", include_in_schema=False)
def get_product(id: int = 0):
    """
    Get detail product
    """
    product = detail_product(id=id)
    return product


@router.get("/establishments", name="market:establishments")
@router.get("/establishments/", name="market:establishments", include_in_schema=False)
def get_establishments(offset: int = 0, limit: int = 100):
    """
    Get list of establishments
    """
    establishments = list_establisment(offset=offset, limit=limit)
    total = total_establishment()
    return {"total": total, "results": establishments}
