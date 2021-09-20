from fastapi import APIRouter
from market.application.usecases import (
    create_categories,
    detail_product,
    list_establisment,
    list_products,
    total_establishment,
)
from market.application.usecases.list_category import list_category
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


@router.get("/categories", name="market:categories")
@router.get("/categories/", name="market:categories", include_in_schema=False)
def get_categories():
    """
    Get list of categories
    """
    categories = list_category()
    return {"results": categories}


@router.get("/categories/test", name="market:test")
@router.get("/categories/test", name="market:test", include_in_schema=False)
def get_test():
    """
    Get list of categories
    """
    create_categories()
    return {"results": "categories"}
