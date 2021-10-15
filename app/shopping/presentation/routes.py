from auth.presentation.utils import get_current_user
from fastapi import APIRouter
from fastapi.param_functions import Depends
from shopping.application.usecases.create_list import create_list
from shopping.application.usecases.list_lists import list_lists

from .schemas import ListCreate

router = APIRouter()


@router.post("/list", name="shopping:create_list")
@router.post("/list/", name="shopping:create_list", include_in_schema=False)
def post_list(user=Depends(get_current_user), list_obj: ListCreate = None):
    """
    Create list
    """

    list_obj.user_id = user.id
    list_obj = create_list(list_obj=list_obj)

    return list_obj


@router.get("/lists", name="shopping:list_lists")
@router.get("/lists/", name="shopping:list_lists", include_in_schema=False)
def get_list(user=Depends(get_current_user)):
    """
    List lists
    """

    lists = list_lists(user_id=user.id)

    return {"results": lists}
