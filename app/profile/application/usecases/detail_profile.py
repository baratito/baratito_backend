from profile.application.repositories.profile_repository import \
    ProfileRepository
from profile.domain import Profile

from dependency_injector.wiring import Provide, inject

from common.di.containers import ApplicationContainer


@inject
def detail_profile(
    profile_repo: ProfileRepository = Provide[
        ApplicationContainer.profile_repository_container.profile_respository
    ],
    id: int = 0,
) -> Profile:
    profile = profile_repo.get_by_user_id(id)
    return profile
