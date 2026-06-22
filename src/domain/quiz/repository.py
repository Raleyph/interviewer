from typing import Protocol
from uuid import UUID

from src.domain.shared.repository import IRepository
from src.domain.quiz import Quiz


class IQuizRepository(IRepository[Quiz], Protocol):
    async def delete(self, id_: UUID) -> None: ...
