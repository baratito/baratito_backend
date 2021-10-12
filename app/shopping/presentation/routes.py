from fastapi import APIRouter

router = APIRouter()


@router.get("/", name=":")
def get_products():
    """
    Get list of 
    """
    return {"": {}}
