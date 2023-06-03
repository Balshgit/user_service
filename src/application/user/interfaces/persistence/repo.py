from typing import Protocol

from src.domain.user import entities
from src.domain.user.value_objects import UserId, Username


class UserRepo(Protocol):
    async def acquire_user_by_id(self, user_id: UserId) -> entities.User:
        raise NotImplementedError

    async def add_user(self, user: entities.User) -> None:
        raise NotImplementedError

    async def update_user(self, user: entities.User) -> None:
        raise NotImplementedError

    async def check_user_exists(self, user_id: UserId) -> bool:
        raise NotImplementedError

    async def check_username_exists(self, username: Username) -> bool:
        raise NotImplementedError
