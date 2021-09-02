from fastapi import APIRouter
from market.application.usecases import detail_product, list_products

router = APIRouter()


@router.get("/products", name="market:products")
@router.get("/products/", name="market:products", include_in_schema=False)
def get_products(offset: int = 0, limit: int = 100):
    """
    Get list of products
    """
    products = list_products(offset=offset, limit=limit)
    return {"results": products}


@router.get("/product/{id}", name="market:product")
@router.get("/product/{id}/", name="market:product", include_in_schema=False)
def get_product(id: int = 0):
    """
    Get detail product
    """
    product = detail_product(id=id)
    return product
