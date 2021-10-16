from typing import List

from auth.presentation.utils import get_current_user
from fastapi import APIRouter
from fastapi.param_functions import Depends
from shopping.application.usecases.create_list import create_list
from shopping.application.usecases.create_or_update_items import create_or_update_items
from shopping.application.usecases.list_items import list_items
from shopping.application.usecases.list_lists import list_lists
from shopping.application.usecases.remove_deleted_items import remove_deleted_items

from .schemas import ListCreate, ListItemCreate

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


@router.post("/list/{id}/item", name="shopping:create_item")
@router.post("/list/{id}/item", name="shopping:create_item", include_in_schema=False)
def post_item(user=Depends(get_current_user), id: int = None, items: List[ListItemCreate] = None):
    """
    Create List items
    """

    items_uuid = [item.id_uuid for item in items]

    remove_deleted_items(list_id=id, list_uuid=items_uuid)

    items = create_or_update_items(list_id=id, items=items)

    return {"results": items}


@router.get("/list/{id}/item", name="shopping:create_item")
@router.get("/list/{id}/item", name="shopping:create_item", include_in_schema=False)
def get_item(user=Depends(get_current_user), id: int = None):
    """
    Create List items
    """

    items = list_items(list_id=id)
    return {"results": items}
