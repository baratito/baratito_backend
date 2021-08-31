from abc import ABC, abstractclassmethod

from auth.domain import User


class UserNotFound(Exception):
    pass


class UserRepository(ABC):
    @abstractclassmethod
    def get_by_email(email: str) -> User:
        ...
