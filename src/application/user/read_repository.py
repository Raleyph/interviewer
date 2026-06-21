from typing import Protocol

from src.application.user.dto import UserLookupDTO


class IUserReadRepository(Protocol):
    async def get_by_username(self, username: str) -> UserLookupDTO | None: ...
