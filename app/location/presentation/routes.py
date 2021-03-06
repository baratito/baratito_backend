from fastapi import APIRouter
from fastapi.param_functions import Depends
from fastapi.responses import JSONResponse

from auth.presentation.utils import get_current_user
from location.application.usecases import UserLocationForbidden
from location.application.usecases import enable_user_location as enable_user_location_usecase
from location.application.usecases.create_user_location import create_user_location
from location.application.usecases.edit_user_location import edit_user_location_usecase
from location.application.usecases.list_user_location import list_user_location
from location.presentation.schemas import UserLocationCreate, UserLocationEdit

router = APIRouter()


@router.get("/user_locations", name="location:user_locations")
@router.get(
    "/user_locations/",
    name="location:user_location",
    include_in_schema=False,
)
def get_user_locations(user=Depends(get_current_user), user_location: UserLocationCreate = None):
    """
    List user location
    """
    locations = list_user_location(user=user)
    return {"results": locations}


@router.post("/user_locations", name="location:user_location", status_code=201)
@router.post(
    "/user_locations/",
    name="location:user_location",
    include_in_schema=False,
    status_code=201,
)
def post_user_location(user=Depends(get_current_user), user_location: UserLocationCreate = None):
    """
    Create user location
    """

    user_location.user_id = user.id

    user_location = create_user_location(user_location=user_location, user=user)
    return user_location


@router.patch("/user_locations/{id}/enable", name="location:enable_user_location")
@router.patch(
    "/user_locations/{id}/enable/", name="location:enable_user_location", include_in_schema=False
)
def enable_user_location(id: int = 0, user=Depends(get_current_user)):
    """
    Enable user location
    """

    try:
        user_location = enable_user_location_usecase(id=id, user=user)
    except UserLocationForbidden:
        return JSONResponse(status_code=404, content="User location does not exists")

    return user_location


@router.patch("/user_locations/{id}", name="location:enable_user_location")
@router.patch(
    "/user_locations/{id}", name="location:enable_user_location", include_in_schema=False
)
def edit_user_location(
    id: int = 0, user=Depends(get_current_user), user_location: UserLocationEdit = None
):
    """
    Edit user location
    """
    try:
        user_location = edit_user_location_usecase(id=id, user=user, user_location=user_location)
    except UserLocationForbidden:
        return JSONResponse(status_code=404, content="User location does not exists")

    return user_location
