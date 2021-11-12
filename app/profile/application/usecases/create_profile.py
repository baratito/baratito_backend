from profile.application.repositories.profile_repository import \
    ProfileRepository
from profile.domain import Profile

from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer


@inject
def create_profile(
    profile_repo: ProfileRepository = Provide[
        ApplicationContainer.profile_repository_container.profile_respository
    ],
    data: dict = {},
    user_id: int = 0,
) -> Profile:
    profile = profile_repo.create(data, user_id)
    return profile
