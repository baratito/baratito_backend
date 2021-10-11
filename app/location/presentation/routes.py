from auth.presentation.utils import get_current_user
from fastapi import APIRouter
from fastapi.param_functions import Depends
from location.application.usecases.create_user_location import create_user_location
from location.presentation.schemas import UserLocationCreate

router = APIRouter()


@router.post("/user_location", name="location:user_location", status_code=201)
@router.post(
    "/user_location/", name="location:user_location", include_in_schema=False, status_code=201
)
def post_user_location(user=Depends(get_current_user), user_location: UserLocationCreate = None):
    """
    Create user location
    """

    user_location.user_id = user.id

    print(user_location)
    user_location = create_user_location(user_location=user_location, user=user)

    return user_location
