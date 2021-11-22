from abc import ABC, abstractclassmethod


class NotificationRepository(ABC):
    @abstractclassmethod
    def list(self, user_id: int):
        ...
