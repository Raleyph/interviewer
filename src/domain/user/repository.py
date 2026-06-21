from typing import Protocol

from src.domain.shared.repository import IRepository
from src.domain.user.model import User


class IUserRepository(IRepository[User], Protocol):
    async def get_by_email(self, email: str) -> User | None: ...
