from fastapi import APIRouter
from fastapi.param_functions import Depends

from auth.presentation.utils import get_current_user
from notification.application.usecases.list_notifications import list_notifications
from notification.application.usecases.read_all_notifications import read_all_notifications

router = APIRouter()


@router.get("/notifications", name="notificaiton:list")
@router.post("/notifications/ ", name="notificaiton:list", include_in_schema=False)
def get_notifications(user=Depends(get_current_user)):
    """
    Get list of notifications
    """
    notifications = list_notifications(user_id=user.id)
    return {"results": notifications}


@router.patch("/notifications/read_all", name="notificaiton:read_all")
@router.post("/notifications/read_all/ ", name="notificaiton:read_all", include_in_schema=False)
def pathc_read_all_notifications(user=Depends(get_current_user)):
    """
    Read all notifications
    """
    notifications = read_all_notifications(user_id=user.id)
    return {"results": notifications}
