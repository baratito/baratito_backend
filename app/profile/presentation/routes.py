from profile.application.usecases.detail_profile import detail_profile

from fastapi import APIRouter
from fastapi.params import Depends

from auth.presentation.utils import get_current_user

router = APIRouter()


@router.get("/profile", name="profile:profile")
@router.get("/profile/", name="profile:profile", include_in_schema=False)
def get_profile(user=Depends(get_current_user)):
    """
    Get profile detail
    """
    profile = detail_profile(id=user.id)
    return profile
