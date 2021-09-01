from profile.application.usecases.detail_profile import detail_profile

from auth.presentation.utils import get_current_user
from fastapi import APIRouter
from fastapi.params import Depends

router = APIRouter()


@router.get("/profile", name="profile:profile")
def get_profile(user=Depends(get_current_user)):
    """
    Get profile detail
    """
    profile = detail_profile(id=user.id)
    return profile
